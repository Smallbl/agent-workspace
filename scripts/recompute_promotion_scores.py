#!/usr/bin/env python3
"""Recompute short-term promotion scores independently from the raw recall store.

Why this exists
---------------
`openclaw memory promote` prints scores, but the printed score is not
inspectable: we cannot tell whether a candidate still clears the threshold
because it is *good* or because it is *old but heavily retrieved*.  Item 271
of MEMORY.md read the weighting table out of
`dist/short-term-promotion-store-E2BAE-8Z.mjs` and item 278 asked for the
formula to be transcribed into the inspection script so candidate decisions
go through *recomputation*, not through "read the number the CLI printed".

This script is that transcription.  It reads the raw
`plugin_state_entries` / namespace `short-term-recall` rows straight out of
a copy of `~/.openclaw/state/openclaw.sqlite`, recomputes each candidate's
score from the source formula, and prints the result side by side.

Source formula (openclaw 2026.9.5, extensions/memory-core/src/short-term-promotion*)
--------------------------------------------------------------------------------
weights (normalised over their sum, which is 1.0 by default):
    frequency     0.24
    relevance     0.30
    diversity     0.15
    recency       0.15
    consolidation 0.10
    conceptual    0.06

    signalCount      = recallCount + dailyCount + groundedCount
    avgScore         = totalScore / signalCount                (clamped 0..1)
    frequency        = ln(1 + signalCount) / ln(11)             (clamped 0..1)
    uniqueQueries    = len(userQueryHashes)
    diversity        = uniqueQueries / 5                       (clamped 0..1)
    ageDays          = (now - lastRecalledAt) / 1 day
    recency          = exp(-ln2 * ageDays / halfLifeDays)      (clamped 0..1)
    consolidation    = len(recallDays)==0 -> 0
                       len(recallDays)==1 -> 0.2
                       else 0.55 * ln(n)/ln(4) + 0.45 * spanDays/7
                       (max of that and groundedCount/3)
    conceptual       = len(conceptTags) / 6                     (clamped 0..1)
    score            = sum(weight * component) + phaseBoost
                       phaseBoost = 0 here (phase-signal store is frozen,
                       see item 277) -- so the recomputation is exact.

Four gates are replicated from the source as well, otherwise the
recomputation lists candidates the CLI hides:

  isShortTermMemoryPath(path)
      path must match  memory/<anything>/YYYY-MM-DD[-suffix].md
      (or memory/.dreams/session-corpus/YYYY-MM-DD.md|.txt)
      memory/dreaming/** is excluded.
      NOTE: the regex is (?:^|/)memory/(?:[^/]+/)*YYYY-MM-DD[-suffix].md$
      so memory/sessions/2026-11-01-<name>.md DOES pass this gate (item
      332 corrects an earlier claim that it did not).
  isPromotionOriginBlocked(entry)
      provenance.originClass in {untrusted, system} -> dropped.
      THIS is the gate that actually blocks the memory/sessions/ entries
      (they carry originClass=untrusted).
  isContaminatedDreamingSnippet(snippet)
      drops dreaming-narrative / raw-session-metadata / raw-turn /
      memory-flush-prompt / promotion-score-metadata snippets.
  score threshold + maxAgeDays hard cutoff.

Also note: recallDays are parsed as UTC midnight (Date.parse(day +
"T00:00:00.000Z")), not local midnight.  Item 332 found a stale hand
computation (consolidation 0.446 instead of 0.667) that came from
mixing these up.

Usage
-----
    python3 scripts/recompute_promotion_scores.py                # top 20, all thresholds
    python3 scripts/recompute_promotion_scores.py --min-score 0 --min-recall-count 0 --min-unique-queries 0
    python3 scripts/recompute_promotion_scores.py --workspace /Users/doujiang/.openclaw/workspace
    python3 scripts/recompute_promotion_scores.py --db /tmp/oc-state.sqlite

Never point --db at the live database: copy it first.
    cp ~/.openclaw/state/openclaw.sqlite /tmp/oc-state.sqlite
"""
import argparse
import json
import math
import os
import re
import shutil
import sqlite3
import sys
import tempfile
import time

DAY_MS = 24 * 60 * 60 * 1000

# memory/<anything>/YYYY-MM-DD[-suffix].md  |  memory/.dreams/session-corpus/YYYY-MM-DD.md|.txt
SHORT_TERM_PATH_RE = re.compile(
    r"(?:^|/)memory/(?:[^/]+/)*(\d{4})-(\d{2})-(\d{2})(?:-[^/]+)?\.md$"
)
SHORT_TERM_SESSION_CORPUS_RE = re.compile(
    r"(?:^|/)memory/\.dreams/session-corpus/(\d{4})-(\d{2})-(\d{2})\.(?:md|txt)$"
)
DREAMING_MEMORY_PATH_RE = re.compile(r"(?:^|/)memory/dreaming/")
SHORT_TERM_BASENAME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})(?:-[^/]+)?\.md$")

WEIGHTS = {
    "frequency": 0.24,
    "relevance": 0.30,
    "diversity": 0.15,
    "recency": 0.15,
    "consolidation": 0.10,
    "conceptual": 0.06,
}

# promotion policy in force for the Memory Dreaming Promotion job
DEFAULT_MIN_SCORE = 0.750
DEFAULT_MIN_RECALL_COUNT = 3
DEFAULT_MIN_UNIQUE_QUERIES = 3
DEFAULT_HALF_LIFE_DAYS = 14
DEFAULT_MAX_AGE_DAYS = 30
MAIN_WORKSPACE = "/Users/doujiang/.openclaw/workspace"


def clamp(value):
    if not isinstance(value, (int, float)) or math.isnan(value):
        return 0.0
    return max(0.0, min(1.0, float(value)))


def recency_component(age_days, half_life_days):
    if age_days is None or age_days < 0 or half_life_days <= 0:
        return 1.0
    return clamp(math.exp(-math.log(2) * age_days / half_life_days))


def consolidation_component(recall_days):
    if not recall_days:
        return 0.0
    if len(recall_days) == 1:
        return 0.2
    parsed = sorted(
        ms
        for ms in (day_to_ms(d) for d in recall_days)
        if ms is not None
    )
    if len(parsed) <= 1:
        return 0.2
    span_days = max(0.0, (parsed[-1] - parsed[0]) / DAY_MS)
    spacing = clamp(math.log1p(len(parsed) - 1) / math.log1p(4))
    span = clamp(span_days / 7)
    return clamp(0.55 * spacing + 0.45 * span)


def day_to_ms(day):
    """UTC midnight, matching the source: Date.parse(day + "T00:00:00.000Z")."""
    try:
        import calendar
        import time as _time

        y, m, d = (int(part) for part in day.split("-"))
        return calendar.timegm(_time.strptime("%04d-%02d-%02d" % (y, m, d), "%Y-%m-%d")) * 1000
    except Exception:
        return None


# --- contamination gate (short-term-promotion-store-E2BAE-8Z.mjs) ---
DREAMING_TRANSCRIPT_PROMPT_LINE_RE = re.compile(
    r"\[[^\]]*dreaming-narrative[^\]]*]\s*(?:User|Assistant):\s*Write a dream diary entry from these memory fragments:?",
    re.I,
)
RAW_SESSION_METADATA_RE = re.compile(
    r"\bSession Key\b.{0,260}\bSession ID\b|\bSession ID\b.{0,260}\bSession Key\b", re.I
)
RAW_CONVERSATION_SUMMARY_RE = re.compile(r"^(?:[-*+]\s*)?Conversation Summary:", re.I)
RAW_TRANSCRIPT_TURN_RE = re.compile(r"^(?:[-*+]\s*)?(?:user|assistant):\s", re.I)
MEMORY_FLUSH_PROMPT_RE = re.compile(
    r"Save important context from this session to the daily memory file\.\s*STRICT RULES:", re.I
)
PROMOTION_SCORE_METADATA_RE = re.compile(
    r"\[\s*score=\d+(?:\.\d+)?\s+(?:signals=\d+\s+)?recalls=\d+\s+avg=\d+(?:\.\d+)?\s+source=memory/",
    re.I,
)


def is_contaminated_dreaming_snippet(raw, allow_transcript_turn_snippet=False):
    snippet = re.sub(r"\s+", " ", (raw or "").strip())
    if not snippet:
        return False
    if "<!-- openclaw-memory-promotion:" in snippet.lower():
        return True
    if DREAMING_TRANSCRIPT_PROMPT_LINE_RE.search(snippet):
        return True
    if RAW_SESSION_METADATA_RE.search(snippet):
        return True
    if RAW_CONVERSATION_SUMMARY_RE.search(snippet):
        return True
    if not allow_transcript_turn_snippet and RAW_TRANSCRIPT_TURN_RE.search(snippet):
        return True
    if MEMORY_FLUSH_PROMPT_RE.search(snippet):
        return True
    if PROMOTION_SCORE_METADATA_RE.search(snippet):
        return True
    return False


def conceptual_component(concept_tags):
    return clamp(len(concept_tags or []) / 6)


def score_entry(entry, now_ms, half_life_days):
    recall_count = int(entry.get("recallCount") or 0)
    daily_count = int(entry.get("dailyCount") or 0)
    grounded_count = int(entry.get("groundedCount") or 0)
    signal_count = recall_count + daily_count + grounded_count
    if signal_count <= 0:
        return None
    avg_score = clamp(entry.get("totalScore", 0) / signal_count)
    frequency = clamp(math.log1p(signal_count) / math.log1p(10))
    unique_queries = len(entry.get("userQueryHashes") or [])
    diversity = clamp(unique_queries / 5)
    last = entry.get("lastRecalledAt")
    age_days = 0.0
    if last:
        parsed = parse_iso_ms(last)
        if parsed is not None:
            age_days = max(0.0, (now_ms - parsed) / DAY_MS)
    recency = recency_component(age_days, half_life_days)
    consolidation = max(
        consolidation_component(entry.get("recallDays") or []),
        clamp(grounded_count / 3),
    )
    conceptual = conceptual_component(entry.get("conceptTags"))
    score = (
        WEIGHTS["frequency"] * frequency
        + WEIGHTS["relevance"] * avg_score
        + WEIGHTS["diversity"] * diversity
        + WEIGHTS["recency"] * recency
        + WEIGHTS["consolidation"] * consolidation
        + WEIGHTS["conceptual"] * conceptual
    )
    return {
        "key": entry.get("key"),
        "path": entry.get("path"),
        "startLine": entry.get("startLine"),
        "endLine": entry.get("endLine"),
        "signalCount": signal_count,
        "avgScore": avg_score,
        "uniqueQueries": unique_queries,
        "ageDays": age_days,
        "score": clamp(score),
        "components": {
            "frequency": frequency,
            "relevance": avg_score,
            "diversity": diversity,
            "recency": recency,
            "consolidation": consolidation,
            "conceptual": conceptual,
        },
        "promotedAt": entry.get("promotedAt"),
    }


def is_short_term_memory_path(path):
    normalized = (path or "").replace("\\", "/")
    if DREAMING_MEMORY_PATH_RE.search(normalized):
        return False
    if SHORT_TERM_PATH_RE.search(normalized):
        return True
    if SHORT_TERM_SESSION_CORPUS_RE.search(normalized):
        return True
    return bool(SHORT_TERM_BASENAME_RE.match(normalized.split("/")[-1]))


def is_promotion_origin_blocked(entry):
    origin_class = (entry.get("provenance") or {}).get("originClass")
    return origin_class in ("untrusted", "system")


def parse_iso_ms(text):
    if not text:
        return None
    text = text.replace("Z", "+00:00")
    try:
        import datetime

        return datetime.datetime.fromisoformat(text).timestamp() * 1000
    except Exception:
        return None


def read_recall_entries(db_path, workspace_dir):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    rows = list(
        cur.execute(
            "select value_json from plugin_state_entries where namespace='short-term-recall'"
        )
    )
    con.close()
    out = []
    for (raw,) in rows:
        try:
            doc = json.loads(raw)
        except Exception:
            continue
        if doc.get("workspaceDir") != workspace_dir:
            continue
        entry = doc.get("value") or {}
        if entry.get("source") != "memory":
            continue
        path = entry.get("path") or ""
        if not path.startswith("memory/"):
            continue
        if not is_short_term_memory_path(path):
            continue
        if is_promotion_origin_blocked(entry):
            continue
        if is_contaminated_dreaming_snippet(entry.get("snippet") or ""):
            continue
        out.append(entry)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=None, help="path to a COPY of openclaw.sqlite")
    ap.add_argument("--workspace", default=MAIN_WORKSPACE)
    ap.add_argument("--min-score", type=float, default=DEFAULT_MIN_SCORE)
    ap.add_argument("--min-recall-count", type=int, default=DEFAULT_MIN_RECALL_COUNT)
    ap.add_argument("--min-unique-queries", type=int, default=DEFAULT_MIN_UNIQUE_QUERIES)
    ap.add_argument("--half-life-days", type=float, default=DEFAULT_HALF_LIFE_DAYS)
    ap.add_argument("--max-age-days", type=float, default=DEFAULT_MAX_AGE_DAYS)
    ap.add_argument("--include-promoted", action="store_true")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--now-ms", type=int, default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    db_path = args.db
    tmp = None
    if not db_path:
        src = os.path.expanduser("~/.openclaw/state/openclaw.sqlite")
        tmp = tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False)
        tmp.close()
        shutil.copy2(src, tmp.name)
        db_path = tmp.name
    try:
        entries = read_recall_entries(db_path, args.workspace)
    finally:
        if tmp:
            os.unlink(tmp.name)

    now_ms = args.now_ms or int(time.time() * 1000)
    scored = []
    for entry in entries:
        if entry.get("promotedAt") and not args.include_promoted:
            continue
        result = score_entry(entry, now_ms, args.half_life_days)
        if not result:
            continue
        if result["signalCount"] < args.min_recall_count:
            continue
        if result["uniqueQueries"] < args.min_unique_queries:
            continue
        if args.max_age_days >= 0 and result["ageDays"] > args.max_age_days:
            continue
        if result["score"] < args.min_score:
            continue
        scored.append(result)

    scored.sort(key=lambda r: (-r["score"], -r["signalCount"], r["path"] or ""))
    scored = scored[: args.limit]

    if args.json:
        print(json.dumps(scored, ensure_ascii=False, indent=2))
        return

    if not scored:
        print("No candidates meet the thresholds.")
        return
    print(f"Recomputed promotion candidates ({args.workspace})")
    print(
        f"thresholds: minScore={args.min_score} minRecallCount={args.min_recall_count} "
        f"minUniqueQueries={args.min_unique_queries} maxAgeDays={args.max_age_days} "
        f"halfLifeDays={args.half_life_days}"
    )
    for r in scored:
        comp = r["components"]
        print(
            f"{r['score']:.4f} {r['path']}:{r['startLine']}-{r['endLine']} "
            f"signals={r['signalCount']} queries={r['uniqueQueries']} age={r['ageDays']:.1f}d"
        )
        print(
            "    "
            + " ".join(f"{k}={v:.3f}" for k, v in comp.items())
        )


if __name__ == "__main__":
    main()
