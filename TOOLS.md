# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## Session 管理

基于 Claude Code Session Memory 设计：

- **触发阈值**：10,000 tokens 初始化 + 每 5,000 tokens 增量
- **摘要文件**：`memory/sessions/{date}-{topic}.md`
- **模板**：见 `memory/sessions/SESSION-TEMPLATE.md`
- **限制**：每条摘要不超过 2000 tokens

## 目录结构

```
memory/
├── topics/          # 永久记忆分主题
├── sessions/        # Session 摘要
├── cron-output/    # 定时简报输出
└── YYYY-MM-DD.md   # 每日记忆
```

Add whatever helps you do your job. This is your cheat sheet.
