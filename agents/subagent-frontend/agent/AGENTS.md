# AGENTS.md - 前端开发智能体

## 项目路径
`/Users/doujiang/.openclaw/workspace/work/projects/`

## 技术栈
- HTML5 + CSS3 + Vanilla JavaScript
- Flask + Jinja2 模板（后端渲染）
- 无框架依赖，保持轻量

## 当前系统结构
```
projects/
├── server.py          # Flask 后端
├── templates/
│   └── index.html     # 主页面（所有UI逻辑）
├── static/            # 静态资源
└── data/
    └── projects.json  # 项目数据
```

## 开发规范
- 修改前先备份：`git add -A && git commit -m "backup before [功能名]"`
- 修改后必须测试功能正常
- 每次提交附上简洁的 commit message
- 遇到问题先尝试解决，解决不了再上报豆浆

## UI 优化方向
- 保持现有配色方案（渐变紫蓝色系）
- 日期、优先级、任务状态清晰易读
- 弹窗和表单交互流畅
- 移动端基本适配

## 禁止事项
- 不得删除或破坏已有功能
- 不得在未沟通情况下大幅重构
- 不得提交未测试的代码
