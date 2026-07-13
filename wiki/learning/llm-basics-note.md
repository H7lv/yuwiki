---
title: LLM 基础概念入门笔记
tags: [learning, ai, llm]
created: 2026-06-27
updated: 2026-06-27
---

摘要：通过 B 站视频课程学习 LLM 核心概念，无电脑实操，纯理论学习。

## 已掌握的概念

### LLM / Token / Context
- LLM = Large Language Model，大语言模型
- Token 是模型的最小输入单位（≈ 0.75 个中文词）
- Context = 上下文窗口，模型一次能"看到"的最大 token 数

### Prompt
- 给模型的指令，决定了输出的质量和方向
- System Prompt / User Prompt 的区别

### Tool / MCP
- Tool = 模型调用的外部工具（计算器、搜索、数据库查询等）
- MCP = Model Context Protocol，标准化模型和工具之间的通信协议

### Agent / AgentSkill
- Agent = 能自主调用工具、规划步骤的 LLM 应用
- AgentSkill = Agent 具备的特定能力模块

## 下一步

- 回自己家用电脑实操：调通 LLM API，写一个对话脚本
- 学习 Function Calling 的具体实现

## 相关页面

- [[ai-agent-roadmap]] — 整体学习路线
- [[career-goal-ai-agent]] — 转行目标
