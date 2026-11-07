#!/usr/bin/env python3
"""Recompute missing material files for the four briefing cron tasks.

Cron DOW mapping (cron: 0-6, 0=Sun, 1=Mon ... 6=Sat)
Python datetime.weekday(): 0=Mon ... 6=Sun
  cron_dow -> python_weekday = (cron_dow - 1) % 7
i.e. cron '1-5' (Mon-Fri) -> python {0,1,2,3,4}
"""
import datetime as dt
import pathlib
import re
import sys

BASE = pathlib.Path(__file__).resolve().parent.parent / "memory" / "cron-history"
TASKS = {
    "ai-morning-briefing": {"cron_dow": {1, 2, 3, 4, 5}, "dir": "ai-morning-briefing"},  # 0 8 * * 1-5
    "ai-work-briefing":    {"cron_dow": {1, 2, 3, 4, 5}, "dir": "ai-work"},              # 30 11 * * 1-5
    "ai-evening-briefing": {"cron_dow": {1, 2, 3, 4, 5}, "dir": "ai-evening"},           # 0 17 * * 1-5
    "openclaw-news":       {"cron_dow": set(range(7)), "dir": "openclaw-news"},          # 0 9 * * *
}

def cron_dow_to_py(dow_set):
    # cron 0=Sun..6=Sat -> python 0=Mon..6=Sun
    return {(d - 1) % 7 for d in dow_set}

def main(start="2026-10-01", end="2026-11-07"):
    s = dt.date.fromisoformat(start)
    e = dt.date.fromisoformat(end)
    total = {}
    for name, cfg in TASKS.items():
        py_dow = cron_dow_to_py(cfg["cron_dow"])
        folder = BASE / cfg["dir"]
        missing = []
        d = s
        while d <= e:
            if d.weekday() in py_dow:
                if not (folder / f"{d.isoformat()}.md").exists():
                    missing.append(d.isoformat())
            d += dt.timedelta(days=1)
        total[name] = missing
        print(f"{name}: missing {len(missing)} -> {missing}")
    return total

if __name__ == "__main__":
    main(*(sys.argv[1:3] or []))
