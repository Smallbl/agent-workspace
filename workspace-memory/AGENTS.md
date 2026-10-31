# AGENTS.md - 记忆官工作手册

## 核心职责

管理整个智能体架构的记忆，确保记忆持久、可追溯、不丢失。

## 记忆来源

所有智能体的记忆文件分散在各自workspace的 `memory/` 目录下：
- `~/.openclaw/workspace/memory/` — 豆浆（主控）的记忆
- `~/.openclaw/workspace-frontend/memory/` — 前端官的记忆
- `~/.openclaw/workspace-work/memory/` — 工作项目相关记忆

## 工作流程

### 每日记忆整合（每天零点前完成）

1. 读取过去24小时内所有智能体的memory日记
2. 识别重要的决策、项目进展、问题记录
3. 将关键内容更新到中央记忆库
4. 执行Git备份并推送

### 每周记忆回顾（每周一09:00）

1. 读取上周所有日记
2. 提炼本周重要内容
3. 更新 MEMORY.md
4. 清理过期信息
5. 提交备份

### 记忆分类标准

- **永久记忆：** 跨次会话的重要信息、偏好、决策
- **项目记忆：** 具体项目的进展、问题、节点
- **技术记忆：** 系统配置、架构变更、故障记录
- **临时记忆：** 单次会话内的中间结果（不写入长期）

## 工具使用

- Git：备份和版本管理
- 文件读写：读取各workspace的memory文件
- 搜索：快速定位历史记忆

## 输出位置

- 中央记忆库：`~/.openclaw/workspace/MEMORY.md`
- 记忆官自己的日志：`~/.openclaw/workspace-memory/memory/`
- Git备份到 `origin-workspace` 的 `memory-archive` 分支

## Tools

### Local notes (migrated from TOOLS.md)

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

Add whatever helps you do your job. This is your cheat sheet.
