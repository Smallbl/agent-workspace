#!/bin/bash
# 自动备份脚本 - 每天 23:30 执行
# 主推送目标: backup 远端 (SSH, git@github.com:Smallbl/agent-workspace.git) 的 backup/project-tracker 分支
# origin 远端保留尝试, 失败仅告警不中断 (origin 的 HTTPS token 已失效, 401 Bad credentials)
cd /Users/doujiang/.openclaw/workspace/work/projects || exit 1

git add -A
if ! git diff --cached --quiet; then
    git commit -m "auto backup: $(date '+%Y-%m-%d %H:%M')" || exit 1
fi

# 1) 推送主备份分支到 backup 远端 (SSH)
echo "==> pushing to backup:backup/project-tracker"
if ! git push backup main:refs/heads/backup/project-tracker 2>&1; then
    echo "警告: 推送到 backup 远端失败, 本地提交已保留" >&2
fi

# 2) 尝试推送 origin, 失败仅告警, 不影响脚本退出码
echo "==> pushing to origin (best-effort)"
if ! git push origin main 2>&1; then
    echo "警告: 推送到 origin 失败 (凭据可能已失效), 已降级为告警, 备份不受影响" >&2
fi

exit 0
