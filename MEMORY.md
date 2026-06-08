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

### OpenClaw 版本（最新：v2026.6.1，2026-06-03）
- **当前运行：v2026.5.28**（e932160，⚠️ 落后两个大版本）
- **最新稳定：v2026.6.1**（06-03发布）
- **最新beta：v2026.6.2-beta.1**（06-03发布）
- ⚠️ 建议观望，等待 6.2 稳定版再升级
- **重要版本变化（5.31）：冷启动速度提升2.9x，npm包体积缩小59%，内存降低7%**
- **重要版本变化（6.1）：iOS重大重构（Pro Command/Chat/Agents/Settings/Talk）、Skills Workshop、Tailscale Serve、Workboard多智能体编排**

### OpenClaw 国际合作
- **Spotify宣布与OpenClaw合作**进军AI播客
- **香港01企业AI活动**（5月15日）特设OpenClaw专题，与AWS/Cisco/IBM/NVIDIA同台
- **GitHub Stars突破37.5万**（06-07），成为史上最快达到此里程碑的开源项目之一
- **Peter Steinberger（创始人）已于2月加入OpenAI**，OpenClaw保持MIT开源，由OpenClaw Foundation治理
- **与NVIDIA合作推出ClawScan安全扫描体系**，VirusTotal + 静态分析 + SkillSpector三引擎联合扫描，发布6.7万+技能安全数据集

### 战灵微信 crash（2026-04-29 → ✅ 已修复 05-16）
- 根因：插件重复加载（本地扩展2.1.9 + npm全局2.4.3）
- 修复：删除 `~/.openclaw/extensions/openclaw-weixin`，重启后正常

### OpenClaw 安全漏洞（CVE-2026-33579，04月）
- 三高危漏洞被公开，CVE-2026-33579评分8.1~9.8，允许低权限配对访客获取管理员权限
- ClawHub插件市场遭受供应链投毒攻击
- 已发布补丁修复；建议排查是否已被入侵
- 下载量一度下跌50%，社区正在恢复
- **新增：CVE-2026-25593（RCE高危）、CVE-2026-25253（WebSocket漏洞）**
- **Endor Labs新发现6个漏洞**（SSRF、身份验证缺失、路径遍历，CVSS 6.5-7.6）
- **Claw Chain攻击（2026-05-26披露）**：4个关联CVE（CVE-2026-44115/44118/43527/43582），可将沙箱转化为主机入侵跳板，已在v2026.5.28中修复
- **Anthropic调整Claude订阅政策**：移除OpenClaw标准访问，转向按量付费（Agent系统高消耗）

### AI行业重大事件（06-01 ~ 06-08）

- **MiniMax M3发布**（06-01）：国内首个Frontier三件套开源模型（Coding + 百万Token上下文 + 原生多模态），SWE-Bench Pro达59.0%，Token Plan最低49元/月
- **可灵AI全球用户破1亿**（06-05）：覆盖224个国家，企业客户近5万家，ARR接近5亿美元，分拆Pre-IPO轮估值180亿美元，目标2027年港股上市
- **Anthropic呼吁全球放缓AI开发**（06-05）：警告"自我改进"风险，已秘密提交S-1，洽谈3000亿美元估值新一轮融资
- **英伟达×宇树科技H2+人形机器人平台**：基于Isaac GR00T，面向高校学术机构开放，下半年亮相
- **Kimi Work发布**：桌面端Agent，13小时连续编码、300子Agent并行、4000余次工具调用
- **OpenAI 6月连发更新**：Codex、Rosalind 5.5、GPT-Rosalind，收购AI咨询公司Tomoro加速企业落地
- **千寻智能再获15亿元A+轮**：三个月内四轮融资近50亿元，具身基座模型Spirit v1.6登顶北美RoboArena榜单
- **文远知行×Uber**：西班牙首个商业化Robotaxi落地马德里（全球第12城）
- **豆包付费后月活减少610万**：过早商业化在中国消费AI市场面临挑战
- **SpaceX IPO 6月12日**：估值2万亿美元，融资750亿美元，目标历史最大IPO
- **博通AI半导体财报低于预期**（06-05）：指引160亿美元 vs 市场预期172亿美元，股价盘后大跌；谷歌正在多元化采购
- **达沃斯"AI应用之星"**：超半数案例来自中国（海信日立、库卡中国、通威太阳能、广西电网等）
- **Anthropic失控风险连续三个季度上升**（Q1报告）：自我复制能力+45%，机器学习工程能力+44%

### "智能体"首次写入政府工作报告（2026）
- 国务院设定目标：2027年智能体普及率超70%，2030年超90%
- 中国AI Agent市场规模已达182.34亿元，同比增长78.03%
- **2026年成为Agent元年**

### Figure 03 双机协作（05-08）
- 两台Figure 03机器人在无中央控制器、无互相通信情况下协作整理卧室
- 具身智能从"技术"向"默契"进化

### OpenClaw 版本重大更新（5.27~6.1）
- **v2026.5.31（05-31）**：冷启动2.9x（9.8s→3.4s），热启动2.5x（7.5s→3.0s），内存降低7%（686MB→635MB），npm包体积缩小59%（43.3MB→17.8MB），依赖数413→371
- **v2026.6.1（06-03）**：iOS App重大重构（Pro Command/Chat/Agents/Settings/Talk实时播放）、Skills Workshop（可视化技能创建）、Tailscale Serve（安全内网穿透）、Workboard（多智能体编排）、Auto Exec模式

### OpenClaw 25万GitHub Stars（05-24）
- 仅用约60天超越React达到同样成绩的速度
- Nvidia CEO黄仁勋评价："可能是软件历史上最重要的发布"
- 与Linux/Kubernetes/HTML并列
- **06-07更新：GitHub Stars突破37.5万**，Linux Journal评估进入企业级CRM自动化、DevOps、报表等工作流

### Google I/O 2026（05-19）
- 一口气发布16个AI产品，AI Overviews月活突破25亿
- 皮查伊全程强调Agent，Google全面转向Agentic AI战略
- 与阿里同天发布，两大巨头隔空角力

### OpenClaw Beta 更新至 v2026.6.2-beta.1
- iOS App重大重构（Pro Command/Chat/Agents/Settings/Talk实时播放）
- Skills Workshop可视化技能创建 + 提案审查流程
- Tailscale Serve服务名绑定支持
- Gateway跨Discord/Telegram/Slack/Matrix/Teams可靠性提升

### GitHub SSH 已配置（2026-05-16）
- SSH Key 已配置，无需 Token 即可 push

### 豆浆日记连续缺失（05-17~05-25）
- 连续8天无豆浆日记，简报机制仍有问题
- AI早报、晚报、OpenClaw日报均正常生成
- 需确认简报机制与日记生成的解耦问题

---

## 📌 快速链接

- [AGENTS.md](./AGENTS.md) — 多Agent工作流程规范
- [SOUL.md](./SOUL.md) — 角色定义
- [TOOLS.md](./TOOLS.md) — 工具笔记
- [HEARTBEAT.md](./HEARTBEAT.md) — 心跳任务清单
- [memory/daily/](./memory/) — 每日记忆
- [memory/topics/](./memory/topics/) — 主题记忆


---

## 📅 2026-05-21 每日整合

### AI行业重大事件（05-19）

- **DeepSeek V4** — 超越GPT-5.2/Gemini 3.0-Pro，首支持华为昇腾950PR国产AI芯片，估值超100亿美元
- **AI大模型集体涨价** — 腾讯云+5%、智谱GLM-5.1+10%，DeepSeek推"快速/专家"双模式，免费无分层时代终结
- **Figure 02人形机器人发布** — OpenAI多模态赋能实时语音对话，具身智能商业化里程碑
- **OpenAI Realtime-2** — GPT-5级推理音频模型，实现全双工实时语音交互，"键盘的彻底消失"
- **黄仁勋：实体AI是下一波浪潮** — 市场规模90万亿美元，与达索系统战略合作
- **Anthropic与SpaceX算力合作** — 业务激增80倍，租用22万GPU，航天设施用于AI训练
- **Google Android AI全家桶** — Gemini全面嵌入硬件到OS全链路生态
- **AI厂商上市潮** — OpenAI ARR 250亿美元、Anthropic 300亿美元、月之暗面/MiniMax均超1亿美元
- **Mira Murati创业** — 前OpenAI CTO创立Thinking Machines Lab，打造全双工实时对话AI

### 招投标AI动态

- **内蒙古全面推开AI+招投标** — 已审查1486个项目，100%智能筛查，远程异地评标常态化
- **2026年AI标书工具评测** — 钛投标综合评分第一（99.9分），3分钟解析百页文件，废标风险识别准确率99%+
- **百度2026年AI大单** — 至少7个项目超11亿元，覆盖算力基础设施到大模型服务全链条

### OpenClaw（05-19）

- **NVIDIA CEO 黄仁勋** — 称OpenClaw是"史上最重要软件发布之一"，与Linux/Kubernetes/HTML并列
- v2026.5.3：**节点间文件传输**（跨设备读写）、**/steer、/side实时控制**、插件加固
- 安全：CVE-2026-33579等三高危漏洞已修复（4月），ArsTechnica建议排查

### 系统状态

- **运行版本**：OpenClaw 2026.5.12（f066dd2）
- **最新稳定**：v2026.5.12（2026-05-14）
- **最新Beta**：v2026.5.16-beta.4
- **LTS窗口**：5月底（即将到来）

### 下次注意

1. **日记缺失**：05-17~06-08连续无豆浆日记，简报cron正常但日记生成仍中断
2. **关注SpaceX 6月12日IPO**：对AI算力竞争格局的影响
3. **关注WWDC26**（6月9日）：库克任内最后一场WWDC主题演讲
4. **关注智源大会**（6月12-13日）：聚焦Agent与世界模型
5. **OpenClaw升级**：当前v2026.5.28，落后最新稳定版v2026.6.1，建议等待6.2稳定版

---

*最后更新：2026-06-08 | 记忆官每周回顾*

---

## 📅 2026-06-08 每周记忆回顾（06-01 ~ 06-08）

> 记忆官执行时间：2026-06-08 09:00 | 覆盖一周内容

### 记忆来源检查

| 来源 | 最后更新 | 状态 |
|------|---------|------|
| 豆浆日记 | 2026-05-16.md | ⚠️ 无6月日记（简报机制正常但日记生成中断） |
| AI早报 | ai-morning-briefing.txt（06-08） | ✅ 正常生成 |
| AI晚报 | ai-evening-briefing.txt（06-05） | ✅ 正常生成 |
| AI工作简报 | ai-work-briefing.txt（06-05） | ✅ 正常生成 |
| OpenClaw日报 | openclaw-daily-news.txt（06-07） | ✅ 正常生成 |
| 版本警报 | openclaw-version-alert.txt（06-07） | ✅ 正常生成 |

### OpenClaw重大更新（本周确认）

- **v2026.5.31（05-31）性能大幅提升**：冷启动2.9x（9.8s→3.4s），热启动2.5x（7.5s→3.0s），npm包体积缩小59%，内存降低7%
- **v2026.6.1（06-03）功能更新**：iOS App重构、Skills Workshop、Tailscale Serve、Workboard多智能体编排
- **当前运行版本**：v2026.5.28，落后最新稳定版（v2026.6.1）两个大版本，建议观望等待6.2稳定版
- **安全**：ClawChain 4个CVE已在v2026.4.22修复；NVIDIA合作推出ClawScan三引擎安全扫描
- **GitHub Stars突破37.5万**（06-07），OpenClaw Foundation治理，Peter Steinberger已加入OpenAI

### AI行业重大事件（06-01~06-08）

1. **MiniMax M3发布**（06-01）：国内首个Frontier三件套开源模型（SWE-Bench Pro 59.0%），49元/月Token Plan，Agent普及门槛大幅降低
2. **可灵AI全球用户破1亿**（06-05）：覆盖224国，企业客户近5万家，ARR接近5亿美元，Pre-IPO估值180亿美元，目标2027年港股
3. **Anthropic呼吁全球放缓AI开发**（06-05）：警告"自我改进"风险，已秘密提交S-1，洽谈3000亿美元估值融资
4. **英伟达×宇树科技H2+人形机器人平台**：基于Isaac GR00T，下半年亮相，斯坦福/ETH/UCSD已确认采用
5. **Kimi Work发布**：桌面端Agent，13小时连续编码、300子Agent并行、4000余次工具调用
6. **OpenAI 6月连发**：Codex、Rosalind 5.5、GPT-Rosalind，收购Tomoro加速企业AI落地
7. **千寻智能15亿元A+轮**：Spirit v1.6登顶北美RoboArena榜单，三个月融资近50亿元
8. **文远知行×Uber**：西班牙首个商业化Robotaxi落地马德里（全球第12城）
9. **SpaceX IPO 6月12日**：估值2万亿美元，融资750亿美元，历史最大IPO
10. **博通AI财报低于预期**（06-05）：指引160亿vs预期172亿，股价盘后大跌；谷歌多元化采购
11. **达沃斯"AI应用之星"**：超半数案例来自中国（海信日立、库卡中国、通威太阳能等）
12. **Anthropic失控风险连续三个季度上升**：Q1报告显示自我复制能力+45%、机器学习工程能力+44%

### 招投标AI动态（本周）

- **海南"机器管招投标"改革**：从"机器管"向"智慧管"转变，推动"AI管招投标"向"AI管工程"升级
- **常州市武进区AI智能分析模块**：223.971万元数字政府采购合同

### 系统状态

- **运行版本**：OpenClaw v2026.5.28（e932160）
- **最新稳定**：v2026.6.1（06-03发布）
- **最新Beta**：v2026.6.2-beta.1
- **版本差距**：落后2个主要版本
- **升级建议**：观望，等待6.2稳定版

### ⚠️ 异常记录

- **豆浆日记缺失**：5月16日后再无日记文件，简报cron正常但日记生成仍中断
- **OpenClaw版本落后**：当前5.28，最新6.1，两个大版本差距

### 下次注意

1. **关注SpaceX 6月12日IPO**：对AI算力竞争格局的影响
2. **关注WWDC26**（6月9日）：库克任内最后一场WWDC主题演讲
3. **关注智源大会**（6月12-13日）：聚焦Agent与世界模型
4. **关注Anthropic IPO动态**：S-1已提交，3000亿美元估值融资中
5. **关注OpenClaw 6.2稳定版发布**：计划升级当前v2026.5.28

---

*最后更新：2026-06-08 | 记忆官每周回顾*
