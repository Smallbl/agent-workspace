# AGENTS.md - 测试智能体

## 网络隔离注意事项
subagent 的 exec 运行在沙盒模式，无法直接访问 localhost。
**重要**：派发网络测试任务时，必须指定 `sandbox: "inherit"` 参数，否则 exec 无法访问 localhost:8765。

## 项目路径
`/Users/doujiang/.openclaw/workspace/work/projects/`

## 访问地址
- 本机：`http://localhost:8765`
- 局域网：`http://192.168.3.136:8765`

## 测试范围

### 功能测试
- [ ] 标签页切换（全部/四建/亚太/会议）
- [ ] 项目编辑弹窗（名称、状态、节点、截止日期、问题）
- [ ] 状态标签自定义（文字、颜色）
- [ ] 任务操作（新增完成勾选、优先级切换、日期设置/清空）
- [ ] 任务名称修改

### 界面测试
- [ ] 日期显示完整无遮挡
- [ ] 弹窗居中显示
- [ ] 移动端基本适配

### 回归测试
- [ ] 所有表单提交后 Tab 保持不变
- [ ] 页面刷新后滚动位置正确
- [ ] 数据持久化正确

## 测试报告输出位置
`/Users/doujiang/.openclaw/workspace/work/projects/TEST-REPORT.md`

## 网络隔离注意事项
subagent 的 exec 默认运行在沙盒模式，无法直接访问 localhost:8765。
**解决方案**：
- **代码审查优先**：通过 `exec` + `cat/grep/head` 等命令直接读取代码文件进行静态验证
- **API测试**：如果确实需要网络测试，使用 `curl http://192.168.3.136:8765`（局域网IP）尝试
- **数据验证**：直接读取 `data/projects.json` 和 `data/uploads/` 目录内容

## 禁止事项
- 不得修改任何代码
- 不得直接操作生产数据
- 发现问题必须记录并上报，不得自行修复
