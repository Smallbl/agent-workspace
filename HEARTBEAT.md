# HEARTBEAT.md

> 版本：2026-10-31（豆浆维护）
> 路径修正：Gateway 真实日志在 `~/Library/Logs/openclaw/gateway-auto.log`，
> `~/.openclaw/logs/gateway.log` 与 `gateway.err.log` 已停留在 2026-05（历史文件，不再更新）。

## Session 摘要检查

当检测到长对话（超过20轮交互）时，主动生成会话摘要：

1. 创建 `memory/sessions/{date}-{topic}.md`
2. 按 `memory/sessions/SESSION-TEMPLATE.md` 填写：关键决策、待办、发现、相关记忆
3. 在对话开头或结尾简短告知王已生成摘要

**触发条件（满足任一）：**
- 单次对话超过 20 轮
- 上下文 token 估计超过 15000
- 对话涉及重要决策或新任务

---

## 定时简报检查发送

检查目录 `~/.openclaw/workspace/memory/cron-output/`，若存在以下文件则读取内容并通过飞书发送给王（openId: ou_748c15a782356f78466b01436dbbcbe8），发送成功后删除文件：

- `openclaw-daily-news.txt` → 格式：【OpenClaw日报】📅日期 + 内容
- `ai-evening-briefing.txt` → 格式：【AI晚报】📅日期 + 内容
- `ai-work-briefing.txt` → 格式：【工作AI简报】📅日期 + 内容
- `ai-morning-briefing.txt` → 格式：【AI早报】📅日期 + 内容
- `openclaw-version-alert.txt` → 格式：【OpenClaw版本警报】📅日期 + 版本信息 + 升级建议

文件内容即完整简报正文，发送使用 feishu 工具主动推送，**必须指定 `accountId: "main"`**（否则报 "Feishu account default not configured"）。
若文件内容为"无新内容"或"无相关内容"则只删除文件、不发送飞书。

注意：
- 读取文件时要判断文件是否已完整写入（检查文件大小是否符合预期，或等待文件修改时间超过5秒再读取）。
- **cron 的 announce 投递在 isolated 任务上实际不落地**（cron 列表显示 `ok (not delivered)`），简报真正送达靠心跳推送。因此每轮心跳都必须检查这个目录，否则会持续积压。
- `weekly-work-review.txt` 由「每周工作回顾」cron 单独推送推送后自行清理，不属于本节范围。

---

## 🩺 启动自检（每次心跳执行）

心跳启动时优先执行以下自检，发现问题主动通知王：

### 1. Gateway 健康检查
```bash
ps aux | grep "[o]penclaw-gateway" | awk '{print $2, $9}'
ps -o lstart= -p <PID>
```
- 真实 PID 必须从完整进程列表确认（`pgrep -f openclaw-gateway` 可能取到空值）。
- 如果启动时间在最近 30 分钟内 → 飞书通知王："⚠️ Gateway 近期重启过（时间：XXX），请确认是否异常"

### 2. 微信第二账号检查
```bash
grep "aa1b373441f2.*channel exited" ~/Library/Logs/openclaw/gateway-auto.log | tail -1
```
- 如果有 `channel exited: Cannot read properties of undefined` → 通知王："⚠️ 战灵微信启动失败（openclaw-weixin v2.1.9 bug），需升级"
- 已知：最近一次记录为 2026-05-16，属历史；只要近期无新增即可视为正常。

### 3. LaunchAgent 安全检查
```bash
ls ~/Library/LaunchAgents/*.plist 2>/dev/null
launchctl list | grep -iE "openclaw|projecttracker"
```
- 除 `ai.openclaw.gateway-auto.plist` 外的自定义 agent：
  - `com.projecttracker.plist`（项目跟踪系统 Flask 服务，端口 8765）→ **已知且属正常**，不必告警；只需确认 `curl -o /dev/null -w "%{http_code}" http://127.0.0.1:8765/` 返回 401（无 token 被拒 = 服务活着）。
  - 其余 Google Updater / Keystone 属系统组件，忽略。
- 若出现**其它**自定义 LaunchAgent → 告警。

### 4. Dreaming 超时检查
```bash
grep "narrative generation ended with status=timeout" ~/Library/Logs/openclaw/gateway-auto.log | tail -3
```
- 如果 3 个 phase 全部 timeout → 记录但不告警（非致命，可能是模型慢）

### 5. Cron 任务健康检查
```bash
openclaw cron list
openclaw cron runs --id <ID> --limit 1   # 查 cause
```
- 关注状态：`error (Nx)` / `skipped` / `ok (not delivered)`。
- 已知：`skill-collection-review-*` 部分子任务因 10 分钟 run 超时失败（`cause: "timeout"`，durationMs ≈ 600000）；属子代理过重，非 Gateway 故障，观察即可，累积过多再调整。

### 自检频率
- 每次心跳都执行步骤 1（gateway 启动时间）
- 每天凌晨 3:30 和 上班 8:00 执行全量自检（步骤 1-5）

---

## 📱 飞书状态同步（每次心跳执行）

每次心跳执行时，检查 `~/.openclaw/workspace/memory/cron-output/pending-feishu.txt` 文件（如果存在则读取内容并发送到飞书，然后删除文件）。

**豆浆的工作流程：当我需要通知王处理状态时，主动写入此文件而非直接调用 message 工具。**

文件内容格式：`【状态更新】` + 简要内容（不超过2000字），发送成功后删除文件。

**注意**：简报文件（ai-*.txt / openclaw-*.txt）的推送逻辑见上方「定时简报检查发送」章节，与此机制独立。

---

## 🧠 子代理派发注意事项（2026-10-31 新增）

1. **子代理工具集不含 `message` 工具** —— 若派发"给王发消息"的任务，子代理会自行退化为 `openclaw message send` CLI（违反工具规范）。派发时必须写明："使用 message 工具；若当前工具集中不存在 message，则不要发送，只把待发内容返回给主代理"。
2. **spawn 时显式设置 `completionTarget="parent"`** —— 否则完成交付会走默认 feishu account `default`（未配置）而报 "Required completion delivery failed"。
3. 任务描述里必须填全标准字段：任务标题 / 问题描述 / 已定位信息 / 已知根因 / 已尝试方案 / 需要执行内容 / API字段要求 / 依赖文件 / 预期结果 / 超时设置。
