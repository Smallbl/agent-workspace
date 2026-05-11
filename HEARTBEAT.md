# HEARTBEAT.md

## Session 摘要检查

当检测到长对话（超过20轮交互）时，主动生成会话摘要：

1. 创建 `memory/sessions/{date}-{topic}.md`
2. 按模板填写：关键决策、待办、发现、相关记忆
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

文件内容即完整简报正文，发送使用 feishu 工具主动推送，**必须指定 `accountId: "main"`**（否则报错"Feishu account default not configured"）。
若文件内容为"无新内容"或"无相关内容"则只删除文件、不发送飞书。

注意：读取文件时要判断文件是否已完整写入（可检查文件大小是否符合预期，或等待文件修改时间超过5秒再读取）。

---

## 🩺 启动自检（每次心跳执行）

心跳启动时优先执行以下自检，发现问题主动通知王：

### 1. Gateway 健康检查
```bash
# 检查 gateway 进程 PID
ps aux | grep openclaw-gateway | grep -v grep
# 检查启动时间（如果 < 30 分钟，说明刚才挂过）
ps -o lstart= -p $(pgrep -f openclaw-gateway | head -1)
```
- 如果启动时间在最近 30 分钟内 → 飞书通知王："⚠️ Gateway 近期重启过（时间：XXX），请确认是否异常"

### 2. 微信第二账号检查
```bash
# 检查战灵微信是否 crash
cat ~/.openclaw/logs/gateway.err.log | grep "aa1b373441f2.*channel exited" | tail -1
```
- 如果有 `channel exited: Cannot read properties of undefined` → 通知王："⚠️ 战灵微信启动失败（openclaw-weixin v2.1.9 bug），需升级"

### 3. LaunchAgent 安全检查
```bash
# 确认只有 gateway plist 在活跃
ls ~/Library/LaunchAgents/*.plist 2>/dev/null | grep -v gateway.plist | grep -v disabled-backup
```
- 如果除 gateway.plist 外有额外文件 → 告警

### 4. Dreaming 超时检查
```bash
# 检查最近一次 dreaming 是否全部 timeout
cat ~/.openclaw/logs/gateway.log | grep "narrative generation ended with status=timeout" | tail -3
```
- 如果 3 个 phase 全部 timeout → 记录但不告警（非致命，可能是模型慢）

### 自检频率
- 每次心跳都执行步骤 1（gateway 启动时间）
- 每天凌晨 3:30 和 上班 8:00 执行全量自检（步骤 1-4）
