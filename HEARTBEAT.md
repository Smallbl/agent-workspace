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

文件内容即完整简报正文，发送使用 feishu 工具主动推送。
若文件内容为"无新内容"或"无相关内容"则只删除文件、不发送飞书。

注意：读取文件时要判断文件是否已完整写入（可检查文件大小是否符合预期，或等待文件修改时间超过5秒再读取）。
