# MEMORY.md - 永久记忆

> 这是豆浆的长期记忆库，存放最重要的信息、决策、偏好。
> **📁 2026-04-04 重大更新：记忆分文件存储，各主题拆分到 memory/topics/ 子目录**

---

## 📂 记忆索引

| 主题 | 文件 | 说明 |
|------|------|------|
| 关于王 | [memory/topics/00-关于王.md](./memory/topics/00-关于王.md) | 基本信息、联系方式 |
| 智能体框架 | [memory/topics/01-智能体框架.md](./memory/topics/01-智能体框架.md) | Agent团队、协作模式 |
| 项目跟踪系统 | [memory/topics/02-项目跟踪系统.md](./memory/topics/02-项目跟踪系统.md) | 项目系统配置 |
| Skill权限管理 | [memory/topics/03-Skill权限管理.md](./memory/topics/03-Skill权限管理.md) | 技能安装规则 |
| 飞书推送任务 | [memory/topics/04-飞书推送任务.md](./memory/topics/04-飞书推送任务.md) | 定时简报配置 |
| 系统稳定性 | [memory/topics/05-系统稳定性.md](./memory/topics/05-系统稳定性.md) | LaunchAgent、运行状态 |
| 工作助手规则 | [memory/topics/06-工作助手规则.md](./memory/topics/06-工作助手规则.md) | 工作流程、跟踪字段 |
| 记忆官定时任务 | [memory/topics/07-记忆官定时任务.md](./memory/topics/07-记忆官定时任务.md) | 备份/回顾任务 |
| 核心配置 | [memory/topics/08-核心配置.md](./memory/topics/08-核心配置.md) | 目录结构、配置文件 |
| Cloud Code架构重构 | [memory/topics/09-CloudCode架构重构.md](./memory/topics/09-CloudCode架构重构.md) | 多Agent开发规范 |
| 战灵学习助手 | [memory/topics/12-战灵项目.md](./memory/topics/12-战灵项目.md) | 皓的学习助手配置 |
| 故障记录 | [memory/topics/11-故障记录.md](./memory/topics/11-故障记录.md) | 问题追踪 |
| **历史档案** | [memory/topics/历史档案.md](./memory/topics/历史档案.md) | **04-17~05-16 每日/每周整合存档** |

---

## 🚨 紧急关注

### OpenClaw 版本
- **当前运行：v2026.5.12**（f066dd2，05-16升级完成）
- **已升级至最新稳定版** ✅

### OpenClaw 国际合作
- **Spotify宣布与OpenClaw合作**进军AI播客
- **香港01企业AI活动**（5月15日）特设OpenClaw专题，与AWS/Cisco/IBM/NVIDIA同台

### 战灵微信 crash（2026-04-29 → ✅ 已修复 05-16）
- 根因：插件重复加载（本地扩展2.1.9 + npm全局2.4.3）
- 修复：删除 `~/.openclaw/extensions/openclaw-weixin`，重启后正常

### GitHub SSH 已配置（2026-05-16）
- SSH Key 已配置，无需 Token 即可 push

---

## 📌 快速链接

- [AGENTS.md](./AGENTS.md) — 多Agent工作流程规范
- [SOUL.md](./SOUL.md) — 角色定义
- [TOOLS.md](./TOOLS.md) — 工具笔记
- [HEARTBEAT.md](./HEARTBEAT.md) — 心跳任务清单
- [memory/daily/](./memory/) — 每日记忆
- [memory/topics/](./memory/topics/) — 主题记忆

