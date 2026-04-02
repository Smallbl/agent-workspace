# HEARTBEAT.md

## 定时简报检查发送

检查目录 `~/.openclaw/workspace/memory/cron-output/`，若存在以下文件则读取内容并通过飞书发送给王（openId: ou_748c15a782356f78466b01436dbbcbe8），发送成功后删除文件：

- `openclaw-daily-news.txt` → 格式：【OpenClaw日报】📅日期 + 内容
- `ai-evening-briefing.txt` → 格式：【AI晚报】📅日期 + 内容
- `ai-work-briefing.txt` → 格式：【工作AI简报】📅日期 + 内容

文件内容即完整简报正文，发送使用 feishu 工具主动推送。
若文件内容为"无新内容"或"无相关内容"则只删除文件、不发送飞书。

注意：读取文件时要判断文件是否已完整写入（可检查文件大小是否符合预期，或等待文件修改时间超过5秒再读取）。
