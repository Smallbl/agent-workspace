# Cloud Code 多Agent架构重构

> 确立于 2026-04-02，基于 Claude Code 源码分析

## 重构目标

基于 Claude Cloud Code 源码架构，解决三大痛点：
1. 子Agent超时后主Agent直接替代干活 → 严格角色隔离
2. 测试Agent假通过 → 全流程真实验证+证据留存
3. Token大量浪费 → 结构化任务传递+上下文精简

## 进度跟踪

| 阶段 | 内容 | 截止日期 | 状态 |
|------|------|----------|------|
| Phase 1 | ✅ AGENTS.md铁律写入（主Agent绝不自写代码） | 2026-04-02 | ✅ 完成 |
| Phase 2 | 流程规范化：测试证据模板、Token监控 | 2026-04-09 | ⏳ 进行中 |
| Phase 3 | 完整流水线：前后端并行、质量闸门、熔断机制 | 长期 | 📋 待开始 |

## 架构整理待办（节后处理）

- [ ] 清理重复 workspace：frontend-dev vs subagent-frontend
- [ ] 确认 tools-agent 是否在使用
- [ ] 验证 cron 超时修复是否生效（明个工作日）
- [ ] 向 OpenClaw 官方反馈 announce bug
- [ ] 考虑简化简报机制：合并到每日一次主动推送

## Phase 2 任务清单

- [ ] 测试Agent输出标准化模板（必须有运行日志/截图/接口返回）
- [ ] Token使用监控+超限告警
- [ ] 任务状态机配置（PENDING→RUNNING→VERIFIED→COMPLETED）

## 保障机制

- 每3天心跳自检一次，进度写入 memory/
- 里程碑截止前1天自动提醒王
- 执行问题随时上报
