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

## 工具并发标记

派发任务时，可并行的工具标注 `🔗`，必须串行的标注 `🔒`：

| 工具 | 标记 | 说明 |
|------|------|------|
| tavily_search | 🔗 | 可并行，多源同时搜索 |
| feishu_bitable_* | 🔗 | 可并行，多表同时读写 |
| feishu_doc read | 🔗 | 可并行，多文档同时读取 |
| feishu_doc write | 🔒 | 串行，避免写入冲突 |
| exec | 🔒 | 必须串行，副作用强 |
| git | 🔒 | 必须串行，文件锁 |
| read/write/edit | 🔗 | 可并行，同一文件不同区域 |
| message send | 🔗 | 可并行，多人同时通知 |

**并行派发原则**：
- 独立任务优先并行（搜索、读取、格式化）
- 写入类必须串行
- 有副作用的命令必须串行

## 服务重启规则

**任何代码修改后必须立即重启服务**：
- 项目跟踪系统：`bash /tmp/run-server.sh`（先 kill 旧进程）
- 重启后验证服务正常运行

## 目录结构

```
memory/
├── topics/          # 永久记忆分主题
├── sessions/        # Session 摘要
├── cron-output/    # 定时简报输出
└── YYYY-MM-DD.md   # 每日记忆
```

Add whatever helps you do your job. This is your cheat sheet.
