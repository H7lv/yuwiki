---
title: AI Agent 应用开发工程师 — 技术栈全景
tags: [ai, reference, career, learning]
created: 2026-06-29
updated: 2026-06-29
source: 百度开发者社区 / 腾讯云 / 市场招聘 JD 综合整理
---

摘要：2026 年 AI Agent 应用开发工程师需要的完整技术栈，分为核心层和加分项，结合你的 Java/MES 背景做了对照分析。

---

## 一、核心必备（按优先级排序）

### 1️⃣ 编程语言

| 语言 | 要求 | 你的现状 |
|------|------|---------|
| **Python** ⭐ | 精通。async/await、Pydantic、FastAPI | 正在学（阶段一） |
| **Java/Go/TS** | 至少一门后端语言辅助 | ✅ Java 3年+，这是你的优势 |

### 2️⃣ AI Agent 核心框架 ⭐

| 框架 | 用途 | 优先级 |
|------|------|--------|
| **LangChain / LangGraph** | Agent 工作流编排、Tool Calling、状态管理 | 🔴 必学（市场第一要求） |
| **CrewAI / AutoGen** | 多 Agent 协作 | 🟡 进阶 |
| **Spring AI Alibaba** | Java 生态 Agent 框架 | 🟢 你的加分项（但建议先学 Python 版） |
| **MCP / A2A 协议** | Agent 间通信协议（2026 新兴） | 🟢 关注 |

### 3️⃣ RAG 技术栈 ⭐

| 组件 | 技术选型 |
|------|---------|
| **向量数据库** | Chroma（入门）/ Milvus / Qdrant / pgvector |
| **Embedding 模型** | text-embedding-3-small / bge 等 |
| **检索策略** | Chunking → Embedding → Hybrid Search → Reranker |
| **评估框架** | Ragas / DeepEval / TruLens |

### 4️⃣ LLM 工程能力

- **Prompt Engineering**：ReAct、CoT、Few-shot、Structured Output
- **Function / Tool Calling**：工具注册 → 意图识别 → 参数填充 → 结果返回
- **Context / Memory 管理**：短期记忆（对话历史）+ 长期记忆（向量存储）
- **Eval 评测**：非确定性输出的评测体系（faithfulness、tool call success rate、hallucination）

### 5️⃣ 工程化能力

| 能力 | 说明 |
|------|------|
| **容器化部署** | Docker + K8s |
| **可观测性** | Langfuse / LangSmith / Prometheus + Grafana |
| **API 设计** | RESTful / WebSocket / SSE（流式输出） |
| **微服务** | 你已具备 🌟 |

---

## 二、你的现状 vs 目标（差距分析）

```
你现在 ──→ 目标
────────────────────────────────────────
Java（3年+）──  ✅  优势：企业级系统经验
      ↓
Python入门     ──  现在在学，目标：精通
      ↓
Spring Cloud   ──  ✅  微服务概念通用
      ↓
MES/ERP领域    ──  ✅  差异化优势：制造+AI
      ↓
LangChain      ──  ❌  目标：熟练
RAG            ──  ❌  目标：能搭建生产级
Eval/监控      ──  ❌  目标：能搭建评测体系
```

---

## 三、对你最有利的学习顺序

### 第一阶段（现在）
```
Python 基础 → FastAPI → 调通 LLM API → Tool Calling → Agent Loop
```
⏱ 约 5 周（按地狱级计划）

### 第二阶段（下一步）
```
LangChain → LangGraph（带状态的多步工作流）→ 简单的 RAG
```
⏱ 约 6-8 周

### 第三阶段（实战）
```
做项目：MES 智能工单 Agent（结合你的行业背景）
       → RAG 知识库问答
       → 多 Agent 协作系统
```

### 第四阶段（面试准备）
```
Eval 评测体系 → 部署 → 简历包装 → 投递
```

---

## 四、你的差异化优势（面试时放大这些）

1. **MES/ERP 行业背景** — 大多数 AI Agent 开发者只有通用开发经验，你有垂直行业 Know-how
2. **企业级系统经验** — 微服务、分布式事务、消息队列、多租户，这是生产级 Agent 需要的工程能力
3. **军工项目** — 涉密离线部署、安全合规，在 toB/信创 方向是稀缺经验
4. **全栈能力** — 从数据库到前端到部署，你能独立搞定一个完整的 Agent 系统

---

## 五、薪资参考（2026）

| 级别 | 经验 | 年薪范围 |
|------|------|---------|
| 初级 Agent 开发 | 0-2年 | 15-25万 |
| 中级 Agent 工程师 | 2-4年 | 25-40万 |
| 高级 Agent 架构师 | 4年+ | 40万+ |

你的 Java 3 年经验 + Agent 转型 = 走**中级路线**，目标 25-40 万。

---

## 相关页面

- [[ai-agent-roadmap]] — 你的学习路线图
- [[career-goal-ai-agent]] — 转行目标
- [[career-profile]] — 你的现有技能
- [[spring-mes-tech-stack]] — 当前项目技术栈
