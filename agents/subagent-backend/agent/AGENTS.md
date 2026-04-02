# AGENTS.md - 后端开发智能体

## 项目路径
`/Users/doujiang/.openclaw/workspace/work/projects/`

## 技术栈
- Python 3 + Flask
- JSON 文件存储（`data/projects.json`）
- Jinja2 模板引擎

## 当前 API 接口
```
GET  /                    # 首页
POST /toggle_task         # 切换任务完成状态
POST /update_priority     # 更新优先级
POST /update_due          # 更新截止日期
POST /clear_due          # 清空截止日期
POST /update_project      # 更新项目信息
POST /update_task_name    # 更新任务名称
```

## 数据结构 (projects.json)
```json
{
  "四建": [{ id, name, status, node, deadline, issues, tasks: [{text, done, priority, due}] }],
  "亚太": [...],
  "meetings": [{date, name, time, remark}]
}
```

## 开发规范
- 修改前先备份
- API 改动需要同步更新前端表单
- JSON 操作注意编码（UTF-8）
- 提交前测试接口返回正常
- 遵循 Flask 路由命名规范

## 禁止事项
- 不得直接修改 data/projects.json（通过 API 操作）
- 不得删除已有接口
- 不得在未沟通情况下改动数据结构
