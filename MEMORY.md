# MEMORY.md - 永久记忆

> 这是豆浆的长期记忆库，存放最重要的信息、决策、偏好。

## 关于王

- 通过飞书联系
- GMT+8 时区
- 只有一个agent（豆浆）
- 重视记忆持久性

## 智能体框架（2026-03-29确立，2026-04-02更新）

### 已注册的独立Agent

| 角色 | Agent ID | 独立Workspace | 状态 |
|------|---------|-------------|------|
| 🧠 豆浆（主控大脑） | main | ~/.openclaw/workspace | ✅ 正常 |
| 🗂️ 记忆官 | memory-agent | ~/.openclaw/workspace-memory | ✅ 正常 |
| 📱 飞书官 | feishu-agent | ~/.openclaw/workspace-feishu | ✅ 正常 |
| 👨‍💻 前端官 | subagent-frontend | ~/.openclaw/agents/subagent-frontend | ✅ 正常 |
| 👨‍💻 后端官 | subagent-backend | ~/.openclaw/agents/subagent-backend | ✅ 正常 |
| 🧪 测试官 | subagent-test | ~/.openclaw/agents/subagent-test | ✅ 正常 |
| 🔍 工具官 | (未注册) | — | 📋 待建立 |

**⚠️ 治理规则：新建智能体需双方评估后建立，不可泛滥**

### ⚠️ 重要架构约束

**飞书_chat工具只能在主session（豆浆）中使用。**
- Isolated session（包括独立agent的session）没有feishu_chat工具
- 飞书官生成内容 → 豆浆负责发送
- Cron简报投递依赖 announce 机制（自动经过豆浆发送）

### 团队协作模式
- 豆浆负责统筹：接收需求、分解任务、分配给专业智能体
- 专业智能体负责执行：完成后返回结果给豆浆
- 豆浆统一协调：所有外部通道（飞书）统一由豆浆发送

## 项目跟踪系统（v2.1）

- 访问地址：`http://localhost:8765`（本机）/ `http://192.168.3.136:8765`（局域网）
- 代码路径：`~/.openclaw/workspace/work/projects/`
- GitHub：`https://github.com/Smallbl/project-tracker`
- 自动备份：每天 23:30 自动 push（crontab）

## Skill 权限管理规则（2026-03-29确立）

### 基础规则
| 类型 | 权限 | 说明 |
|------|------|------|
| 🟢 常规 Skill | 豆浆自主使用 | 如 feishu-*, weather, tavily 等 |
| 🟡 消耗型 API | 豆浆自行管控+月度统计 | 如 tavily 搜索（每月统计一次用量） |
| 🔴 敏感 Skill | 需确认后使用 | 如 skill-creator（可创建新skill） |
| 🟠 飞书权限操作 | 建议单独确认 | 文档/云盘权限变更操作 |

### 新增 Skill 规则
- 新增 Skill 需双方评估后安装，不可自主泛滥
- 安装前检查：权限要求、API额度、依赖项

### 常用 Skill 推荐
- find-skills：搜索/发现新skill（已安装）

## 飞书官主动推送任务（2026-03-29配置）

| 任务 | 时间 | 说明 |
|------|------|------|
| 💼 工作AI简报 | 工作日 11:30 | 招投标行业AI应用动态（工作相关） |
| 🤖 AI早报 | 工作日 08:00 | AI前沿科技新闻（个人兴趣） |
| 🤖 AI晚报 | 工作日 17:00 | AI前沿科技新闻（个人兴趣） |
| 📰 OpenClaw日报 | 每天 09:00 | OpenClaw最新资讯 |

**📋 所有简报规则：中文优先，英文翻译概述，每条必附原文链接**

## 系统稳定性（2026-03-29配置）

### LaunchAgent 开机启动
- ✅ 已安装 LaunchAgent 服务
- 电脑重启后 OpenClaw 自动启动
- 日志：`~/.openclaw/logs/gateway.log`
- 状态：`openclaw daemon status` 查看

### 当前运行状态
- Gateway: 运行中 (pid 48712)
- Dashboard: http://127.0.0.1:18789/

## 工作助手规则（2026-03-29确立）

### 核心流程
- 你随手丢信息给我 → 我整理归档 → 自动提醒跟进

### 跟踪字段（精简5项）
- 项目名称（你定义）
- 状态（进行中/已延期/已完成/已暂停）
- 下一个节点
- 节点截止日期
- 当前问题

### 工作目录
- `/work/projects/` — 项目进度
- `/work/meetings/` — 会议纪要

### 下周会议提醒（已配置）
| 日期 | 时间 | 会议 |
|------|------|------|
| 周一 03-30 | 09:30 | 四建、亚太例会 |
| 周二 03-31 | 09:30 | 新点AI产品介绍 |
| 周三 04-01 | 09:30 | 巨一例会-招投标需求 |
| 周四 04-02 | 09:30 | 中招联合-进度汇报 |

## 记忆官定时任务（2026-03-29配置）

| 任务 | 时间 | 说明 |
|------|------|------|
| 📅 每日备份 | 每天零点 (Asia/Shanghai) | 巡检memory目录，有变更自动commit+push |
| 📊 每周回顾 | 每周一 09:00 (Asia/Shanghai) | 提炼本周重要内容更新到MEMORY.md |

## 核心配置

- 工作目录：`~/.openclaw/workspace`
- 记忆目录：`~/.openclaw/workspace/memory/`
- Git备份：已启用

## Cloud Code 多Agent架构重构（2026-04-02确立）

### 重构目标
基于 Claude Cloud Code 源码架构，解决三大痛点：
1. 子Agent超时后主Agent直接替代干活 → 严格角色隔离
2. 测试Agent假通过 → 全流程真实验证+证据留存
3. Token大量浪费 → 结构化任务传递+上下文精简

### 进度跟踪

| 阶段 | 内容 | 截止日期 | 状态 |
|------|------|----------|------|
| Phase 1 | ✅ AGENTS.md铁律写入（主Agent绝不自写代码） | 2026-04-02 | ✅ 完成 |
| Phase 2 | 流程规范化：测试证据模板、Token监控 | 2026-04-09 | ⏳ 进行中 |
| Phase 3 | 完整流水线：前后端并行、质量闸门、熔断机制 | 长期 | 📋 待开始 |

### Phase 2 任务清单
- [ ] 测试Agent输出标准化模板（必须有运行日志/截图/接口返回）
- [ ] Token使用监控+超限告警
- [ ] 任务状态机配置（PENDING→RUNNING→VERIFIED→COMPLETED）

### 保障机制
- 每3天心跳自检一次，进度写入 memory/
- 里程碑截止前1天自动提醒王
- 执行问题随时上报

---

## 重要决策记录

- **2026-03-29** 老板的前一个AI助手因记忆错乱、修复时配置文件被删导致无法恢复。豆浆必须遵守：修改配置或安装影响运行的程序前，必须先备份并确认。
- **2026-03-31** 建立专业开发团队：前端官、后端官、测试官。豆浆定位为统筹角色，负责任务分解和质量管理，不再亲自兼职写代码。
- **2026-03-31** 项目跟踪系统采用 MiniMax-M2.7 模型进行开发，暂不使用 GPT-4/Codex。

## 学习与成长

### 故障记录（重要）

**2026-04-01 cron任务超时问题**
- **现象：** 所有定时简报任务（AI早报、AI晚报、工作AI简报、OpenClaw日报）连续两天失败，状态为 error
- **根本原因：** cron 任务超时设置默认为 30 秒，但简报生成+搜索+发送需要 50-180 秒
- **解决方案：** 将所有简报任务的 timeoutSeconds 从默认值改为 180 秒
- **修复命令：**
  ```
  openclaw cron edit <job-id> --timeout-seconds 180
  ```
- **涉及任务：**
  - ai-morning-briefing (3f650a3a...)
  - openclaw-daily-news (29418b9f...)
  - ai-work-briefing (9130e296...)
  - ai-evening-briefing (d697e753...)
  - memory-daily-backup (b142b71c...) → 60秒即可
- **经验教训：** 新增 cron 任务时注意检查超时设置，默认 30 秒可能不够用
