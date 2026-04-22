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

---

## 🚨 紧急关注

### announce bug 重复发送问题（2026-04-16 发现）
- **症状**：cron 任务执行成功后，announce 投递模块内部重试队列未正确清空，导致重复发送或发送空内容
- **具体案例**：
  - AI工作简报 4/16 发送了两次（11:01 正常，12:00 重试成功）
  - OpenClaw日报 4/16 9:30 发送了空内容（9:01 发送成功后重试队列残留）
- **处理**：4/16 晚已重启 OpenClaw 服务清空重试队列
- **后续**：4/21 观察正常，未再复发 ✅

---

## 📌 快速链接

- [AGENTS.md](./AGENTS.md) — 多Agent工作流程规范
- [SOUL.md](./SOUL.md) — 角色定义
- [TOOLS.md](./TOOLS.md) — 工具笔记
- [HEARTBEAT.md](./HEARTBEAT.md) — 心跳任务清单
- [memory/daily/](./memory/) — 每日记忆

---

*最后更新：2026-04-22 | 记忆官每周整合*

---

## 📝 2026-04-17 每日整合

### OpenClaw 重要更新（2026-04-16）

1. **OpenClaw v2026.4.5 发布** — 新增 Memory Dreaming（做梦记忆）实验功能，系统自动整理记忆；新增 video_generate 和 music_generate 工具
2. **OpenClaw 创始人 Peter Steinberger 加入 OpenAI** — 项目将转由基金会维护，继续开源发展
3. **安全更新（3.13 & 3.31）** — 新增 trusted-proxy 验证、SSRF 防护；如部署暴露公网需立即更新
4. **ClawHub 插件市场上线** — 社区生态持续扩大
5. **MiniMax M2.7 支持** — 新模型选项

### Heartbeat 故障修复（2026-04-16 20:01）

- **问题**：`message` 工具发送飞书报错 "Feishu account default not configured"
- **原因**：多飞书账号环境下，默认账号未设置
- **解决**：发送时必须指定 `accountId: "main"`
- **验证**：HEARTBEAT 兜底机制验证成功——cron生成 → 文件检测 → 飞书推送 → 文件删除

### ⚠️ 升级注意事项

- 跨版本升级：备份配置 → 查看 release notes → `openclaw doctor --fix` → 重启服务
- 第三方插件（尤其飞书）需重点关注兼容性，3.31 SDK 变更可能影响 feishu-lark 插件
- 升级前先用 `openclaw doctor --fix` 预处理

### 2026.4.1 announce bug 状态

- 记忆备份、AI日报、OpenClaw日报曾受影响
- 2026-04-16 各简报均正常推送，bug 可能已修复或兜底机制生效

## Promoted From Short-Term Memory (2026-04-18)

<!-- openclaw-memory-promotion:memory:memory/2026-04-05.md:1:42 -->
- # 2026-04-05 每日记忆 ## 📅 日期 2026-04-05（周日） --- ## 🤖 今日主要工作 ### 1. OpenClaw 备援方案搭建 - OpenClaw 2026.4.1 announce bug 导致所有 cron 任务失效 - 搭建外部系统 cron 作为备援方案 - 编写统一备援脚本：`~/scripts/openclaw-fallback.sh` - 配置 crontab 5个定时任务（00:30~17:30，每30分钟备援窗口） - Tavily API Key：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 - 搜索词已改为中文，优先返回国内源 ### 2. 项目跟踪系统 v3/v4 开发 **今天解决的问题：** - Bug: tab白名单写死，中招联合等新公司无法正常使用 - Bug: 空公司无法添加项目 - 优化: 任务默认折叠，点击展开 - 优化: 项目统计卡片（全部项目tab显示） - 优化: 任务汇总条（优先级+完成率，每项目卡片上方） **UI重构 v4：** - 固定顶部header（56px，深色背景） - 两级导航（项目/会议/每日任务 + 全部/四建/亚太/中招联合） - 紧凑统计卡片5列布局 - 紧凑项目卡片 - 拖拽排序功能 - 会议管理（新增/编辑/删除/标记完成） **代码路径：** `~/.openclaw/workspace/work/projects/` **访问地址：** `http://localhost:8765` --- ## ⚠️ 问题记录 ### 1. 子Agent超时问题 - v4 UI重构任务太大，导致多次超时 [score=0.812 recalls=5 avg=0.733 source=memory/2026-04-05.md:1-42]

---

## 📝 2026-04-19 每日整合

### 重要发现：OpenClaw v2026.4.10 Active Memory 功能

4/18 OpenClaw日报整理出关键功能更新：

- **Active Memory 记忆系统**（v2026.4.10 新增）
  - 自动实现"用户消息 → 记忆检索 → 上下文增强"
  - 支持三种模式：message（当前消息）/ recent（近期记忆）/ full（全部记忆）
  - 当前豆浆依赖 MEMORY.md + HEARTBEAT.md 手动读取，Active Memory 可自动化此过程
  - **建议**：待王确认后更新到最新版本并测试 Active Memory

- **内置 Codex 提供商**（v2026.4.11）
  - 配置更简单，使用 `codex/gpt-5` 即可自动路由

- **版本状态确认**：当前运行 v2026.4.14，最新 v2026.4.15（差1个小版本，可择机更新）

### 定时任务状态（4/17-4/19 观察）

| 任务 | 最后执行 | 状态 |
|------|---------|------|
| ai-morning-briefing | 4/17 08:00 | ✅ ok（lastDurationMs: 128227） |
| openclaw-daily-news | 4/19 09:00 | ✅ ok（写入cron-history） |
| ai-work-briefing | 4/17 12:00 | ✅ 最后一次在4/17 |
| ai-evening-briefing | 4/17 17:01 | ✅ 最后一次在4/17 |

> 4/18-4/19 是周末+周一，ai-work/ai-evening 因非工作日未触发，符合预期

### 做梦系统运行正常

- 4/18 凌晨3点做梦系统正常运行，生成了 `2026-04-19.md`（含Light/REM内容）
- 4/19 MEMORY.md 已在凌晨3点被更新（来自做梦的"Promoted From Short-Term Memory"）
- 做梦候选池来源：主要是 4/15-4/17 的 session 历史

### 下次注意

1. **版本更新**：v2026.4.15 可择机更新，建议先备份配置再操作
2. **Active Memory 测试**：更新后可测试主动记忆检索功能
3. **验证4/20工作日的各简报是否正常推送**

---

## 📝 2026-04-22 每日整合（记忆官）

### 定时任务状态（4/21 观察）

| 任务 | 执行时间 | 状态 |
|------|---------|------|
| ai-morning-briefing | 4/21 08:05 | ✅ 正常（含10条新闻，含链接） |
| openclaw-news | 4/21 09:00+ | ✅ 正常（版本修正为v2026.4.14，包含4条新闻） |
| ai-work-briefing | 4/21 12:00 | ✅ 正常（政采AI、招投标数字化等内容） |
| ai-evening-briefing | 4/21 17:02 | ✅ 正常（10条，含谷歌/Kimi/苹果/亚马逊等） |
| 战灵每日备份 | 4/21 01:00 | ✅ 成功，备份大小10K |

> **OpenClaw日报版本bug已修复**：之前cron prompt缺少版本获取步骤导致版本号错误，4/20修复后4/21版本显示正确（v2026.4.14）

### 重要新闻摘录（4/21）

**AI/科技：**
- 谷歌成立"突击队"追赶AI Coding，谢尔盖·布林要求员工"果断转向"Agent技术
- Kimi 2.6 发布（4/21凌晨），国产大模型持续迭代
- 字节跳动2025年AI投入超1600亿元，净利润暴跌超70%
- 苹果换帅：John Ternus接棒CEO，库克转任执行董事长（9/1生效）
- 亚马逊将向Anthropic追加最高250亿美元投资（累计430亿）

**行业：**
- 工信部：一季度工业机器人产量同比增长33.2%，AI眼镜等日益丰富
- 它石智航完成4.55亿美金Pre-A轮融资（中国具身智能最高单轮纪录）
- 德塔智能成立三月融资超亿元，专注通用人形机器人基础模型
- 群核科技上市首日股价大涨144%，市值超316亿港元

**政策：**
- 国办：推动修订招标投标法，强化制度刚性约束
- 安徽"十五五"规划：加快人工智能在招标投标、政府采购中的应用
- 欧盟打造AI"第三极"，德国启动最大AI创新园

### 技术记录

- daily.html 备注显示优化已完成（展开/收起按钮，长备注≥30字触发）
- 战灵机器人运行正常，备份机制已验证

### 待处理

1. **版本更新**：v2026.4.15 可择机更新，建议备份配置后操作
2. **Active Memory 测试**：待王确认后更新并测试主动记忆检索功能
3. **MEMORY.md 分支备份**：已验证config文件备份路径正常

---

## 📝 2026-04-22 每周整合（本周 4/13-4/22）

### 本周重大事项

#### 1. OpenClaw v2026.4.15 发布（4/16）
- 里程碑级更新：126项代码变更、230+修复细节
- 核心五大方向：Anthropic模型升级Claude Opus 4.7、LanceDB本地向量库、Copilot向量嵌入、Deep Research集成、代码沙盒强化
- **当前运行版本**：v2026.4.14，最新 v2026.4.15（差1个小版本，择机更新）

#### 2. Ollama 本地向量搜索落地（4/17）
- 安装 Ollama（macOS 安装包方式）+ nomic-embed-text 嵌入模型
- OpenClaw memorySearch 从 `fts-only` 升级为 **`hybrid`**（向量+全文混合搜索）
- 向量搜索已激活，Relevance 维度恢复精准评分

#### 3. 定时任务体系多项修复（4/16-4/18）

| 问题 | 修复 | 状态 |
|------|------|------|
| memory-daily-backup sessionTarget 错误 | sessionTarget: isolated | ✅ |
| memory-weekly-review payload.kind 错误 | payload.kind: agentTurn | ✅ |
| git submodule 不能直接 git add | 排除 workspace/memory/ | ✅ |
| 备份任务超时（300s不够） | 延长至 600s | ✅ |
| 备援脚本9:30与cron重叠导致重复推送 | 从crontab删除9:30任务 | ✅ |

#### 4. Cron Prompt 配置错误修复（4/20）
- **问题**：openclaw-daily-news cron prompt 缺少版本获取步骤，子agent编造版本号
- **根因**：prompt 未要求执行 `openclaw --version`
- **修复**：第一步强制获取版本 + 每条新闻必须包含原文链接
- **教训**：配置 cron/agent prompt 时必须要求获取实际状态，禁止自行编造

#### 5. 战灵学习助手项目启动（4/20）
- 飞书机器人「战灵」已创建，App ID: `cli_a96ca544d1785ccb`
- 独立 Agent：zhanling，workspace 隔离
- 群组：无极限（oc_7ffa2ca99242ae246037198f4bde6030）
- 成员：战灵机器人 + 王 + 皓（孩子，上海初一学生）
- **重要规则**：配置修改需王审批确认后方可执行
- **皓的学习特点**：英文偏弱，语文缺乏积累，数学有畏难情绪
- **下一步**：王陪皓明晚一起测试战灵

#### 6. 项目跟踪系统 - 每日任务备注优化（4/20）
- 备注 < 30字：直接显示「💬 备注：xxx」
- 备注 ≥ 30字：显示前30字 + 「展开」按钮，点击展开/收起
- 已上线运行

### 本周已解决的问题

| 问题 | 来源日期 | 解决日期 | 状态 |
|------|---------|---------|------|
| heartbeat 飞书发送 accountId 错误 | 4/15 | 4/15 | ✅ |
| 备援脚本返回0条（后发现是双推导致） | 4/17 | 4/18 | ✅ |
| announce 重复投递（重试队列残留） | 4/16 | 4/16重启 | ✅ |
| cron+备援双重执行重复推送 | 4/21 | 4/18修复 | ✅ |
| OpenClaw日报版本号错误 | 4/20 | 4/20 | ✅ |
| 飞书文件上传 Excel 权限 | 4/13 | 4/13 | ✅ |

### 本周新闻亮点（值得记忆）

- **荣耀人形机器人半马夺冠**：50分26秒完赛，破人类世界纪录（4/19）
- **DeepSeek 首次外部融资**：目标估值≥100亿美元（4/20）
- **谷歌追赶AI Coding**：谢尔盖·布林要求员工"果断转向"Agent技术
- **苹果换帅**：John Ternus接棒CEO，库克转任执行董事长（9/1生效）
- **亚马逊追加Anthropic投资**：累计430亿美元（4/21）
- **群核科技上市**：首日股价大涨144%，市值316亿港元

### 定时任务本周状态（4/13-4/22）

| 任务 | 状态 | 备注 |
|------|------|------|
| ai-morning-briefing | ✅ 正常 | 每天8点，含链接 |
| openclaw-daily-news | ✅ 正常 | 版本号已修复 |
| ai-work-briefing | ✅ 正常 | 工作日11:30 |
| ai-evening-briefing | ✅ 正常 | 工作日17:00 |
| memory-daily-backup | ✅ 正常 | 600s超时已够 |
| memory-weekly-review | ✅ 正常 | 本次执行 |
| 战灵每日备份 | ✅ 正常 | 每天1:00 |

### 教训总结

1. **Cron prompt 必须包含实际状态获取步骤**：禁止子agent自行编造信息
2. **备援机制需避免与主任务时间重叠**：防止双重执行
3. **git submodule 不能直接 git add**：需在子仓库单独操作
4. **Ollama 不需要 Homebrew**：macOS 直接下载安装包即可
