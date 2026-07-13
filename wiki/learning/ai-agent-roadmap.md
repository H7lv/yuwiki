---
title: AI Agent 转型学习路线（深度版）
tags: [learning, ai, career, plan]
created: 2026-06-26
updated: 2026-06-29
---

摘要：从 Java 全栈到 AI Agent 应用开发工程师的完整转型路线。**不追求速成，追求真会**。每一阶段都有明确的熟练度标准，确保学完能独立设计、开发、部署生产级 Agent 系统。

## 📌 背景

- **起点：** Java 3年+（Spring Cloud 微服务）+ C++ Qt，ERP/MES 企业级系统背景
- **目标：** 完全具备 AI Agent 应用开发工程师的技术水平（对标中级，25-40万/年）
- **核心动力：** 当前收入不理想，为未来养家做准备（[[career-goal-ai-agent]]）
- **学习理念：** 慢就是深，深就是快。每个概念做到能**不讲稿子讲清楚、不抄代码写出来、不出文档能排错**。

## 🗺️ 六阶段总览

```
阶段 0 ── 地基 ── Python 工程化精通（6周）
       ↓
阶段 1 ── 核心 ── LLM API + Agent 原理 + Loop Engineering（6周）
       ↓
阶段 2 ── 框架 ── LangChain/LangGraph 专业级（6周）
       ↓
阶段 3 ── 深度 ── RAG 工程全栈（6周）
       ↓
阶段 4 ── 生产 ── 多Agent + 可观测 + Harness + Loop 高级（8周）
       ↓
阶段 5 ── 终局 ── 实战项目 + 面试（6周）
```

**总时长：约 38 周（9 个半月），这是学到"真会"的时间，不是"跑通"的时间。**

---

## 🔴 关于"熟练"的标准定义

本计划中每个模块完成后，你需要能通过以下检验才算合格：

```
Level 1 ❌ 看过     — 听课/读文档了，但写不出来
Level 2 ❌ 跑通     — 照着教程能运行，改了就报错
Level 3 ❌ 会用     — 能改参数、调配置，解决简单问题
Level 4 ✅ 熟练     — 不看文档能写出来，能解释原理，能排查问题
Level 5 ✅ 精通     — 能设计架构，能优化性能，能教别人
```

**本计划每个阶段的终点都是 Level 4（熟练），部分核心模块要求 Level 5（精通）。**

---

## 阶段 0：Python 工程化精通（6 周）

**目标**：从"能写 Python 脚本"到"能写生产级 Python 代码"。不要求成为 Python 专家，但要求达到你当前 Java 的开发水准。

### 熟练度标准

完成本阶段后，你应该能：
1. **不看文档**写出符合 PEP8 的 Python 代码
2. **独立设计**一个 Python 项目的目录结构（相当于 Spring 项目的分层）
3. **解释** async/await 的事件循环原理（不只是会用）
4. **写出**带类型注解的 Pydantic 模型，包含自定义验证器
5. **搭建**带中间件、异常处理、日志的 FastAPI 项目
6. **写出**完整的 pytest 单元测试和集成测试

### 详细内容

#### 第 1-2 周：Python 深度基础（Java 对比学习法）

| 主题 | 深度要求 | Java 对照 | 学习活动 |
|------|---------|-----------|---------|
| 类型系统 | Type Hints 全部特性：`Optional`/`Union`/`Literal`/`TypedDict`/`Protocol`/`Generic` | Java Generics + Interface | 给自己现有的 MES 项目写一份类型标注 |
| 装饰器 | 参数化装饰器、类装饰器、`functools.wraps` | AOP 注解 + 反射 | 自己实现一个 `@log_call`、`@retry` 装饰器 |
| 上下文管理器 | `__enter__`/`__exit__`、`contextlib.contextmanager`、`contextlib.suppress` | try-with-resources | 实现一个数据库连接上下文管理器 |
| 迭代器/生成器 | `__iter__`/`__next__`、`yield`、`yield from`、生成器表达式 | Stream API + Iterator | 实现一个分页读取大文件的生成器 |
| 函数式工具 | `map`/`filter`/`reduce`、`functools.partial`、`itertools` 常用组合 | Stream + Collector | 用函数式方式处理一个数据集合 |

**深度练习（不完成不进入下一周）**：
- 实现一个带超时和重试的装饰器 `@retry(max_attempts=3, delay=1)`
- 实现一个上下文管理器，自动统计代码块执行时间
- 用生成器实现一个「流式读取日志文件并按关键词过滤」的功能

#### 第 3 周：Pydantic V2 深度

| 主题 | 深度要求 |
|------|---------|
| 字段类型 | `constr`/`conint`/`confloat` 约束、`EmailStr`/`UrlStr`/`UUID` |
| 验证器 | `@field_validator`、`@model_validator`、`BeforeValidator`/`AfterValidator` |
| 序列化 | `model_dump()`/`model_dump_json()`、`serialization_alias`、自定义序列化器 |
| 配置 | `model_config` 全部选项：`extra`/`frozen`/`validate_default`/`str_strip_whitespace` |

**深度练习**：
- 用 Pydantic 定义你 MES 项目中的「工单」数据模型，包含：工单号约束、状态枚举(ENUM)、时间范围验证、关联字段校验
- 实现一个模型的 Import/Export（dict ↔ JSON ↔ model 的完整转换链，含错误处理）

#### 第 4-5 周：FastAPI 生产级开发

| 主题 | 深度要求 |
|------|---------|
| 路由与依赖注入 | `Depends()` 多层依赖（对比 Spring 的 `@Autowired` + `@Bean`） |
| 中间件 | CORS、鉴权、请求日志、耗时统计中间件 |
| 异常处理 | 全局异常处理器、自定义 HTTPException、统一错误响应格式 `R<T>` |
| 数据库 | SQLAlchemy 2.0（对比 MyBatis-Plus）：模型定义、CRUD、关系映射、事务 |
| 异步 | 异步路由、异步数据库会话、异步 HTTP 请求（httpx） |
| 文件处理 | 文件上传/下载、大文件流式处理（对比 FastDFS/MinIO） |

**深度练习**：
- 用 FastAPI 重写你 MES 系统中的「工单接口」（至少 3 个 CRUD），对比 Spring Boot 版本的差异
- 实现请求日志中间件（记录：请求方法、路径、耗时、状态码）
- 实现统一异常处理，仿照 Spring 的 `@RestControllerAdvice` 模式

#### 第 6 周：Python 测试 + 工程规范

| 主题 | 深度要求 |
|------|---------|
| pytest | `fixture`、`parametrize`、`conftest.py`（对比 JUnit + Mockito）、`mock.patch` |
| 异步测试 | `pytest-asyncio`、异步 fixture |
| 代码质量 | `ruff`（linter）、`mypy`（类型检查，对比 javac 编译检查）、`pre-commit` |

**深度练习**：
- 为第 5 周写的工单接口写完整的 pytest 测试，覆盖率 > 80%
- 配置 ruff + mypy，确保项目零 warning 通过

### 📌 阶段 0 熟练度自检清单

- [ ] 能不看文档解释 `async/await` 的事件循环原理（用你的话，不用术语堆砌）
- [ ] 能自己实现一个装饰器（带参数），中间件（鉴权/日志）
- [ ] 能用 Pydantic 写出带自定义验证、序列化配置的复杂模型
- [ ] 能搭建一个完整的 FastAPI 项目：路由 → 数据库 → 异常处理 → 日志 → 测试
- [ ] 能写出 pytest 测试（fixture/mock/parametrize）
- [ ] 你的 Python 代码风格像你写的 Java 一样整洁

---

## 阶段 1：LLM API + Agent 原理精通（6 周）

**目标**：从"调通 API"到"完全掌握 LLM 交互的每一个细节"。能自己实现 Agent 框架的核心逻辑，不依赖任何第三方框架。

### 熟练度标准

1. **不用 SDK**，直接用 HTTP 请求调 LLM API
2. **理解** Token 计费、上下文窗口、流式输出的底层原理
3. **自己实现** Tool Calling 循环（不依赖 LangChain）
4. **设计** 复杂的 System Prompt 策略（多角色、动态注入、few-shot）
5. **处理** 各种边缘情况：超时、截断、格式错误、幻觉
6. **能对比** 不同模型/参数/策略的优劣

### 详细内容

#### 第 1 周：LLM API 底层理解

**不直接学 SDK，先学 HTTP 协议层**：

```python
# 这才是真正的底层理解——用 HTTP 请求调 API
import httpx
import json

response = httpx.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": "your-key",
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    },
    json={
        "model": "claude-sonnet-4-6",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": "你好"}]
    },
    timeout=30
)
print(response.json()["content"][0]["text"])
```

**深度内容**：
| 主题 | 深度要求 |
|------|---------|
| HTTP 协议层 | 认证方式（API Key/Bearer/OAuth）、请求/响应格式、HTTP 状态码处理 |
| 参数理解 | `temperature`/`top_p`/`top_k`/`frequency_penalty`/`presence_penalty` **各自的数学含义** |
| 上下文窗口 | 了解计数方式（tokenizer）、**不同模型的窗口限制**、超长截断策略 |
| 流式响应 | SSE（Server-Sent Events）原理、`async for` 逐块处理、流式中断恢复 |
| 重试策略 | 指数退避 + jitter、幂等性、不同错误码的处理策略（429 vs 500 vs 401） |

**深度练习**：
- 不用 SDK，只用 httpx 调通 Chat API + 流式输出 ✅
- 对比 `temperature=0` vs `temperature=1` 的输出差异，记录 5 次测试结果 ✅
- 实现一个「自动重试 + 指数退避」的 API 调用包装器 ✅

#### 第 2 周：多 Provider 适配（模型无关抽象）

**目标**：把不同的 LLM 提供商抽象成统一接口（面试常问：模型无关设计）。

```
统一接口：LLMClient.chat(messages, tools, config) → Response
    ├── AnthropicClient  ← Claude
    ├── OpenAIClient     ← GPT
    ├── OllamaClient     ← 本地模型（qwen/deepseek）
    └── AzureClient      ← 企业场景
```

**深度练习**：
- 自己设计一个 `BaseLLMClient` 抽象类，为 2 个不同 Provider 实现子类
- 实现一个 **模型路由**：根据任务类型（简单问答 vs 复杂推理）自动选择模型

#### 第 3 周：结构化输出深度

**不满足于"让 AI 返回 JSON"，要掌握**：

| 技术 | 深度要求 |
|------|---------|
| JSON Mode | 各模型的 JSON Mode 区别、局限性、fallback 策略 |
| Function Calling | 底层原理（tool_use stop_reason）、多 tool 并行调用、嵌套 tool |
| 结构化 Fallback | AI 返回格式不对时怎么自动修正（重试 + re-prompt） |
| 流式结构化 | 流式场景下的结构化输出（逐步解析 JSON chunk） |

**深度练习**：
- 把阶段 0 写的 Pydantic 模型集成到 LLM 输出解析中 ✅
- 实现一个「结构化输出保证器」：AI → JSON 解析失败 → 自动修正 → 重试 3 次 → 兜底方案 ✅
- 实现一个「动态 Tool 注册器」：从配置文件/数据库动态加载工具定义 ✅

#### 第 4 周：Prompt Engineering 工程化

| 主题 | 深度要求 |
|------|---------|
| Prompt 模板化 | Jinja2 模板引擎（对比 Java 的 Thymeleaf/Freemarker）、动态变量注入 |
| Few-shot 策略 | 动态 few-shot selection（向量相似度选取示例）、示例数量对质量的影响 |
| 多角色 Prompt | System/User/Assistant 消息的角色分工、对话历史的 Token 预算 |
| Chain of Thought | CoT 的实现方式、什么时候用/不用、效果量化 |
| Prompt 版本管理 | Prompt 作为代码管理、A/B 测试、变更记录（关键：生产环境一定要有） |

**深度练习**：
- 用 Jinja2 实现一个 Prompt 模板系统（变量注入 + 条件渲染 + 循环渲染）✅
- 设计一个「角色分离」Prompt 方案：系统指令 + 上下文信息 + 用户输入 分层 ✅
- 为一个具体任务（比如工单异常分类）设计 5 个 few-shot 示例，测试不同示例组合的效果 ✅

#### 第 5 周：Agent 原理解析（自己实现 Agent 框架）

**这是阶段 1 的核心——不依赖 LangChain，自己实现 Agent Loop。**

```python
# 你要自己实现的核心逻辑（伪代码）
def agent_loop(user_input, tools, max_steps=10):
    messages = [{"role": "user", "content": user_input}]
    
    for step in range(max_steps):
        response = llm.chat(messages, tools)  # 调用 LLM
        
        if response.has_tool_call():
            for tool_call in response.tool_calls:
                result = execute_tool(tool_call)  # 执行工具
                messages.append(tool_result(tool_call.id, result))  # 放回结果
        else:
            return response.text  # 最终回答
    
    return "超时"  # 达到最大步数
```

**你要深入理解的**：
| 概念 | 深度要求 |
|------|---------|
| ReAct 模式 | Reason + Act 循环的原理、Observation 的注入方式 |
| Agent 状态管理 | 多轮对话的状态、Tool 调用上下文、中断恢复 |
| 决策边界 | Agent 什么时候该停、什么时候该问人（Human-in-the-loop） |
| 错误恢复 | Tool 调用失败 → 重试/跳过/报错/换方案 四种策略的取舍 |

**深度练习**：
- 不依赖 LangChain，自己实现一个完整的 Agent Loop ✅
- 支持：多工具注册、工具并行调用、错误重试、最大步数限制 ✅
- 支持 Human-in-the-loop（工具调用前等用户确认）✅

#### 🌀 Loop Engineering 基础（第 5 周补充）

**目标**：从"跑通 Agent Loop"到"理解 Loop 的每一种设计模式和工程考量"。

| 主题 | 深度要求 |
|------|---------|
| **主循环架构** | ReAct Loop vs Plan-and-Execute Loop vs Reflection Loop 三种模式的**架构区别**和**适用场景**。能画出每种模式的流程图 |
| **循环控制** | 终止条件设计（最大步数 / 无新信息 / 重复检测）、步数限制的副作用（过早截断 vs 死循环）、指数退避防抖 |
| **状态累积** | 每次循环的上下文膨胀问题、Token 窗口管理策略、关键信息摘要压缩（map-reduce 方式） |
| **循环安全** | 死循环检测（重复模式识别）、异常状态恢复（Checkpoint + Resume）、断路器模式（连续失败 N 次后降级） |
| **人机协同** | 三种 HITL 模式：前置审批（tool 调用前确认）、后置审核（结果出来后审核）、异常升级（Agent 不确定时主动问人） |
| **循环可观测** | 每步决策日志（输入 → 推理 → 工具选择 → 结果）、循环轨迹回放（Debug 模式）、耗时/Token 分布分析 |

**深度练习**：
- 在你手写的 Agent Loop 中，添加循环安全机制：死循环检测（连续 3 次相同 tool 调用则中断）+ 断路器 ✅
- 记录一次完整 Agent 决策过程的**循环轨迹**，分析每一步的耗时和 Token 消耗 ✅
- 实现 Plan-and-Execute 模式：Agent 先做计划（Plan），再按计划执行（Execute），最后检查结果 ✅

#### 第 6 周：阶段 1 整合项目

**项目：通用 Agent 运行时**（类似自己实现一个迷你 LangChain）

功能要求：
1. 模型无关（支持切换 Claude / GPT / Ollama）
2. 工具注册系统（从代码注册 + 从配置文件注册）
3. Agent Loop（支持 ReAct + 并行工具调用）
4. 对话记忆（滑动窗口 + 摘要压缩两种策略）
5. Prompt 模板系统（Jinja2 模板）
6. 结构化输出保证（自动重试 + 修正）
7. 完整的日志和监控

**熟练度检验**：
- 你的代码**不能有任何 copy-paste**，每行都是自己写的
- 能解释 Agent Loop 的每一步在干什么
- 能给一个没学过的人讲清楚「Agent 是怎么工作的」

### 📌 阶段 1 熟练度自检清单

- [ ] 不用 SDK，用 HTTP 直接调通 LLM API（含流式）
- [ ] 自己实现了带重试+错误处理的 API 调用封装
- [ ] 自己实现了完整的 Agent Loop（不依赖 LangChain）
- [ ] 能解释 ReAct 模式的原理和你实现中的取舍
- [ ] Prompt 作为代码管理，有模板、有版本、有测试
- [ ] 完成了整合项目：通用 Agent 运行时

---

## 阶段 2：LangChain/LangGraph 专业级（6 周）

**目标**：从"会用框架"到"懂框架的设计思想"。能使用 LangChain/LangGraph 高效开发，也知道它们帮你省了什么、藏了什么。

### 第 1-2 周：LangChain 组件深度

**学习方式**：每学一个组件，**先问自己"如果我自己实现会怎么做"**，再看 LangChain 怎么做的。

| 组件 | 深度要求 | 自己实现的版本 vs LangChain |
|------|---------|---------------------------|
| PromptTemplate | 模板继承、partial 变量、few-shot 模板选择器 | 用 Jinja2 实现对比 |
| OutputParser | PydanticOutputParser、CommaSeparatedListOutputParser | 上阶段已做的结构输出 vs LC 实现 |
| Tool | BaseTool、StructuredTool、@tool 装饰器、Tool 的异常处理 | 对比你之前手写的 Tool 注册 |
| Memory | ConversationBufferMemory、SummaryMemory、VectorStoreMemory、Zep | 实现滑动窗口记忆对比 |
| Retriever | BaseRetriever、VectorStoreRetriever、MultiQueryRetriever、ContextualCompression | 实现简单检索对比 |
| Callback | BaseCallbackHandler、LangChain 事件系统、自定义 handler | 实现简单的事件监听对比 |

**深度练习**：
- 为之前 MES 项目中的「工单查询」场景，用 LangChain 的 Tool + Retriever 实现一个知识检索工具
- 对照你阶段 1 自己写的 Agent 运行时，找出 LangChain 替你做了哪些事 ✅

#### 第 3-4 周：LangGraph 工作流深度

**这是 Agent 开发的核心——掌握有状态、多步骤的工作流编排。**

| 概念 | 深度要求 |
|------|---------|
| StateGraph | State 定义（TypedDict / Pydantic）、Node 和 Edge 的设计模式 |
| Conditional Edge | 路由逻辑、条件判断、默认分支、错误分支 |
| Checkpoint | 状态持久化（内存/数据库/文件）、中断恢复 |
| Streaming | 节点级流式、Token 级流式、自定义流式事件 |
| Human-in-the-loop | `interrupt_before`/`interrupt_after`、审批节点设计 |
| Subgraph | 子图封装、图间通信、复用模式 |
| Parallel | 节点并行、`Send` API、fan-out/fan-in 模式 |

**深度练习**：
- 实现一个「MES 工单审批 Agent」工作流：
  ```
  接收工单 → LLM 判断异常类型 → 自动处理（可选）→ 需人工审批？→ 等待 → 继续执行
  ```
- 为上述工作流添加 Checkpoint 持久化（进程重启能恢复）✅
- 实现 subgraph 封装：把「工单分析」做成一个可复用的子图 ✅

#### 第 5 周：LangSmith + 评测体系

| 主题 | 深度要求 |
|------|---------|
| Tracing | LangSmith 追踪配置、自定义 Run 名称、标签/元数据 |
| Dataset | 测试数据集创建、人工标注 vs 自动标注 |
| Eval | LangSmith Evaluator、自定义 Evaluator、成对对比（A/B test） |
| 线上监控 | 生产环境 Trace 采样、性能分析、成本追踪 |

**深度练习**：
- 为你阶段 1 的 Agent 添加 LangSmith 追踪
- 创建一个包含 20 个测试用例的评估数据集
- 运行评估，记录至少 3 个指标（准确率、调用成功率、响应时间）✅

#### 第 6 周：阶段 2 整合项目

**项目：使用 LangGraph 重构阶段 1 的 Agent 运行时**

要求：
1. 用 LangGraph 的 StateGraph 替代手写的 Agent Loop
2. 支持 Checkpoint 持久化（重启恢复）
3. 支持 Human-in-the-loop（关键步骤需要确认）
4. 添加 LangSmith 可观测性
5. 对比：你手写版本 vs LangGraph 版本的差异，写一篇分析笔记

### 📌 阶段 2 熟练度自检清单

- [ ] 能解释 LangChain 的 Tool 和 Memory 的底层实现原理
- [ ] 能独立用 LangGraph 设计复杂工作流（分支、循环、并行、子图）
- [ ] 理解 LangGraph 的 State 管理和 Checkpoint 机制
- [ ] 能用 LangSmith 做 Trace 和 Eval
- [ ] 清楚知道 LangChain 帮你做了什么、隐藏了什么

---

## 阶段 3：RAG 工程全栈（6 周）

### 第 1-2 周：基础 RAG 深入

| 主题 | 深度要求 |
|------|---------|
| Chunking 策略 | Fixed-size、Semantic、Recursive Character、Agentic Chunking **各自的优劣和适用场景** |
| Embedding 模型 | 主流模型对比（text-embedding-3-small/large、bge-m3、gte-Qwen2）、**选型依据** |
| 向量数据库 | Chroma（入门）→ Qdrant/Milvus（生产）、索引类型（HNSW/IVF）、性能调优 |
| 检索策略 | 相似度检索、MMR（最大边际相关性）、Self-Query |

**深度练习**：
- 用 3 种不同 chunking 策略切分一份文档（比如你的 Wiki 页面），对比结果 ✅
- 测试 2 种不同的 embedding 模型，记录检索准确率差异 ✅
- 实现一个「Wiki 知识库检索器」：把你的 Wiki 内容向量化并支持语义搜索 ✅

#### 第 3-4 周：高级 RAG

| 主题 | 深度要求 |
|------|---------|
| Hybrid Search | 稠密检索（向量）+ 稀疏检索（BM25）混合、加权策略 |
| Reranking | Cohere Rerank / BGE Reranker、Cross-Encoder vs Bi-Encoder、rerank 的时机和成本 |
| Query Transformation | HyDE（假设文档嵌入）、Multi-Query（多角度重写）、Query Routing |
| Agentic RAG | Agent 自主判断是否需要检索、检索不足时自修正、多轮检索 |
| GraphRAG | 实体提取 → 关系构建 → 图检索（理解原理，知道解决什么问题） |

**深度练习**：
- 实现 Hybrid Search（稠密 + 稀疏，带权重调节）✅
- 在检索链中加入 Reranker，对比加入前后的准确率 ✅
- 实现 Agentic RAG：Agent 判断问题是否需要检索 → 检索 → 判断结果是否足够 → 不足则重试 ✅

#### 第 5 周：RAG 评估体系

| 主题 | 深度要求 |
|------|---------|
| Ragas 指标 | Faithfulness（忠实度）、Answer Relevancy（回答相关性）、Context Precision（上下文精确度）、Context Recall（上下文召回率）**能解释每个指标的数学含义** |
| DeepEval | 指标实现、自定义指标、测试集构建 |
| 人工评估 | 评估数据集标注、评分一致性、评估成本 |

**深度练习**：
- 用 Ragas 评估你第 4 周实现的检索系统，记录 4 个核心指标 ✅
- 对比 3 种不同配置（chunk 大小 / top_k / rerank 与否）的指标差异 ✅
- 用 DeepEval 写一个自定义指标（例如：工具调用准确率）✅

#### 第 6 周：阶段 3 整合项目

**项目：企业知识库问答系统**

技术栈：FastAPI + LangChain + Qdrant + Reranker + Ragas

功能要求：
1. 多类型文档上传（PDF/Word/Markdown）
2. 智能 Chunking（根据内容类型自动选择策略）
3. Hybrid Search + Reranker
4. Agentic RAG（检索不足时自动重试）
5. Eval 面板（显示每次检索的质量指标）
6. 对比实验模式（A/B 测试不同配置的检索效果）

### 📌 阶段 3 熟练度自检清单

- [ ] 能解释 3 种以上 Chunking 策略的原理和选型依据
- [ ] 能独立搭建 Hybrid Search + Reranker 的检索管线
- [ ] 理解 Agentic RAG 的设计模式
- [ ] 能用 Ragas/DeepEval 量化评估 RAG 质量
- [ ] 清楚 Embedding 模型的选型标准
- [ ] 完成企业知识库问答系统

---

## 阶段 4：生产级 Agent 系统（8 周）

**目标**：从"能跑"到"能上线"。掌握多 Agent 协作、Agent 运行时框架（Harness）、循环工程、可观测性、安全合规和部署运维的全链路能力。

### 第 1-2 周：多 Agent 系统

| 主题 | 深度要求 |
|------|---------|
| CrewAI | Agent 角色定义、Task 依赖、Process 类型（sequential/hierarchical）、Tool 共享 |
| LangGraph 多 Agent | Supervisor（主管Agent）、Handoff（任务交接）、Swarm（群体协作模式） |
| 通信模式 | 广播式、路由式、流水线式、黑板模式（Agent 通过共享状态通信） |
| 错误恢复 | 子 Agent 失败 → 重试 / 降级 / 报错 / 换 Agent |
| 成本控制 | 多 Agent 场景的 Token 预算、模型选择策略 |

**深度练习**：
- 用 CrewAI 搭建一个「三 Agent 协作系统」：分析员（搜索信息）→ 审核员（验证）→ 报告员（输出）✅
- 用 LangGraph 实现 Supervisor 模式：一个主管 Agent 分配任务给多个 Worker ✅
- 实现一个「MES 异常处理多 Agent 系统」：
  - 检测 Agent → 分析 Agent → 方案 Agent → 审批 Agent → 执行 Agent ✅

---

#### ⛓️ 第 3 周：Harness Engineering（Agent 运行时框架）

**核心问题**：当你不在终端里跑 Agent，而是把它部署成服务时，你需要一个运行时框架来管理 Agent 的全生命周期。这就是 **Harness**。

**你的 Java 对照**：Harness ≈ Spring 容器（管理 Bean 的生命周期、依赖注入、AOP 切面、配置加载）

| 主题 | 深度要求 | Java 对照 |
|------|---------|-----------|
| **Harness 架构** | Agent 运行时的分层设计：配置层 → 生命周期层 → 执行层 → 可观测层。Harness 要管理什么、不管理什么 | Spring 容器架构 |
| **工具注册与发现** | 工具注解/装饰器扫描、自动注册、依赖注入（工具间共享 DB 连接/Client）、工具分类与命名空间 | `@Component` + `@Autowired` |
| **生命周期管理** | Agent 初始化（加载配置 → 构建 Prompt → 注册工具 → 连接向量库）、运行、暂停、销毁。生命周期钩子（`on_start`/`on_tool_call`/`on_error`/`on_shutdown`） | Spring Bean 生命周期（InitializingBean/DisposableBean） |
| **配置管理** | 多环境配置（dev/test/prod）、配置热加载、配置校验（Pydantic Settings）、敏感信息（API Key 从环境变量/密钥管理服务加载） | Spring `@ConfigurationProperties` + `application-{profile}.yml` |
| **上下文管理** | 请求级别的上下文传递（Trace ID、用户 ID、租户 ID）、上下文切换（多用户同时使用）、异步上下文传播 | Spring `RequestContextHolder` / MDC |
| **插件系统** | 插件接口设计、插件热加载、插件隔离（沙箱）、插件通信（Hook 事件系统），**让第三方开发者能扩展你的 Agent 平台** | SPI / Plugin 架构 |
| **错误处理框架** | 层级式错误处理（Harness 级 → Agent 级 → Tool 级）、错误码规范、降级策略链（主方案 → 备选 → 兜底） | Spring `@ExceptionHandler` 层级 |
| **资源管理** | 连接池管理（数据库/LLM Client）、并发控制（semaphore）、超时控制（每个 Tool 独立超时）、清理钩子 | `@PreDestroy` + 连接池 |

**深度练习**：
- 实现一个 **Agent 运行时框架**（mini Harness），包含：
  - 配置加载（支持 YAML/环境变量）✅
  - 工具自动注册（装饰器扫描）✅
  - 生命周期钩子（`on_start` / `on_before_tool` / `on_after_tool` / `on_error` / `on_shutdown`）✅
  - 请求级上下文传递（Trace ID 自动注入每个 Tool 调用）✅
  - 多环境配置切换（dev/test/prod）✅
- 在你阶段 1 的手写 Agent 基础上，把它嵌入到这个 Harness 里运行 ✅
- 设计一个简单的插件接口，实现一个插件（比如「日志插件」）并动态加载 ✅

---

#### 📊 第 4 周：可观测性（Observability）

| 主题 | 深度要求 |
|------|---------|
| 全链路追踪 | Langfuse / LangSmith / OpenTelemetry、Trace ID 在 Harness 中的传递、Agent 决策日志 |
| 监控指标 | Token 消耗、工具调用成功率、响应时间、用户满意度、成本/请求 |
| 日志系统 | 结构化日志（JSON）、Agent 决策过程可审计、敏感信息脱敏 |
| 告警 | 异常检测、成本突增告警、质量下降告警 |
| **Harness 集成** | 将可观测性作为 Harness 的内置能力：所有 Agent 默认获得 Trace/日志/指标，不需要每个 Agent 单独实现 |

**深度练习**：
- 为你之前的所有 Agent 项目添加 Langfuse 追踪 ✅
- 在你实现的 Harness 中集成可观测层（自动为每个 Agent 生成 Trace）✅
- 实现结构化日志，记录每次 Agent 决策的完整链路（输入 → 思考 → 工具调用 → 输出）✅
- 实现一个「Agent 监控面板」：显示实时 Token 消耗、调用次数、错误率 ✅

---

#### 🔒 第 5 周：Guardrails + 安全

| 主题 | 深度要求 |
|------|---------|
| 输入安全 | Prompt Injection 检测（几种已知攻击模式）、PII 脱敏 |
| 输出安全 | 内容过滤、Topic 限制、置信度阈值 |
| Guardrails 框架 | NeMo Guardrails / Guardrails AI / 自定义 Guard |
| **Harness 集成** | 将 Guard 作为 Harness 的中间件层：请求进入 Harness → Guard 链（输入检测 → 限流 → 审计）→ Agent 执行 → Guard 链（输出检测 → 脱敏） |
| 速率限制 | Token 级别 / 请求级别 / 用户级别的限流（类似 Sentinel） |
| 审计 | 完整审计日志（谁、什么时间、问了什么、得到了什么回答）|

**深度练习**：
- 实现 Prompt Injection 检测器（至少检测 3 种常见的注入模式）✅
- 实现 PII 脱敏中间件（手机号、身份证号自动替换）✅
- 在你的 Harness 中实现 Guard 中间件链（输入 Guard → 限流 Guard → 输出 Guard）✅
- 实现一个「安全审查 Agent」：请求进来先过审查，不合规直接拦截 ✅

---

#### 🔄 第 6 周：Loop Engineering 高级

**核心问题**：Agent Loop 不是"调工具 → 等回复"这么简单。生产环境中你需要考虑循环的可控性、效率、安全性和自愈能力。

**前置知识**：阶段 1 的 Loop Engineering 基础（已学过 ReAct/Plan-and-Execute/Reflection 模式）

| 主题 | 深度要求 |
|------|---------|
| **Plan-and-Execute 深度** | Agent 先制定执行计划 → 逐部执行 → 动态调整计划。**计划冲突检测**（计划中步骤 A 和步骤 B 矛盾）、**计划修复**（某步失败后重新规划） |
| **Reflection 模式** | 自省循环：Agent 对自己输出的结果进行自我评估 → 发现错误 → 修正 → 重新输出。**Reflection 的频率控制**（每次都要/仅在高风险场景） |
| **Tree-of-Thought** | Agent 同时探索多条推理路径 → 评估每条路径 → 剪枝 → 选出最优。**适用于**：需要深度推理的任务（如复杂 SQL 生成、代码审查） |
| **循环编织（Loop Weaving）** | 多个子循环的组合：主循环（感知-推理-行动）内嵌子循环（验证循环、检索循环、规划循环）。**循环嵌套的深度控制**和**循环间的状态隔离** |
| **循环成本控制** | 每步 Token 预算分配、**提前终止策略**（答案置信度达到阈值就停止）、循环的 Token 消耗预测和预警 |
| **循环安全（深度）** | **检查点与恢复**（每步的 State 持久化，崩溃后可恢复）、**幂等性保证**（Tool 重复调用不产生副作用）、**死循环逃逸**（N 种逃逸策略：步数限制/重复检测/时间超时/无进展检测） |
| **循环测试** | 循环的单元测试（给定状态 → 执行一步 → 验证状态变更）、集成测试（完整场景跑通）、性能测试（循环步数分布/耗时分布/Token 分布） |

**深度练习**：
- 实现 **Reflection Agent**：Agent 先给出答案 → 自我审查 → 发现错误 → 修正 → 输出最终版 ✅
- 实现 **循环安全框架**：将检查点、幂等性保证、死循环逃逸封装成可复用的 Harness 组件 ✅
- 为你阶段 1 的 Agent 编写循环性能测试：测试 100 个问题的循环步数分布、耗时分布、Token 消耗分布 ✅
- 实现 Tree-of-Thought 模式：同时探索 3 条推理路径 → 评估 → 选最优，用在你 MES 工单异常分析场景 ✅

---

#### 🐳 第 7 周：部署 + CI/CD + 成本优化

| 主题 | 深度要求 |
|------|---------|
| 部署 | Docker 多阶段构建、Docker Compose（前后端 + 向量库 + Agent 服务）、K8s 基础 |
| **Harness 化部署** | 将你的 Harness 打包为 Docker 镜像，支持环境变量配置（API Key/数据库连接等从环境注入） |
| CI/CD | LLM 应用的特殊 CI（Prompt 变更审查、Eval 自动运行、回归测试） |
| Prompt 管理 | Prompt 版本控制、A/B 测试、灰度发布、回滚 |
| 缓存策略 | LLM 响应缓存（语义缓存 vs 精确缓存）、Cache hit ratio 优化 |
| 成本优化 | Token 压缩、模型路由（简单问题用小模型）、Batch 处理、Prompt 缩短策略 |

**深度练习**：
- 为你的 Harness + Agent 写 Dockerfile + docker-compose.yml ✅
- 实现语义缓存：相同/相似的问题不重复调 LLM ✅
- 实现模型路由：根据问题复杂度自动选择模型（Claude Haiku vs Sonnet）✅
- 实现 CI Pipeline：代码变更 → 类型检查（mypy）→ 测试 → Eval 自动运行 → 报告 ✅

---

#### 🏗️ 第 8 周：阶段 4 整合项目

**项目：生产级 Agent 平台**

整合本阶段所有能力：

1. **多 Agent 系统** — CrewAI / LangGraph Supervisor
2. **Harness 运行时** — 配置加载、工具注册、生命周期、上下文传递、插件系统
3. **可观测性** — Langfuse 全链路追踪 + 结构化日志 + 监控面板
4. **安全 Guard** — Prompt Injection 检测 + PII 脱敏 + 限流
5. **循环工程** — Reflection 自省 + 检查点恢复 + 死循环逃逸
6. **成本优化** — 语义缓存 + 模型路由
7. **Docker 部署** — Harness → Docker → Docker Compose → CI

### 📌 阶段 4 熟练度自检清单

- [ ] 能设计多 Agent 协作系统（角色分工、通信、错误恢复）
- [ ] **能实现一个 Agent 运行时框架（Harness）：配置/生命周期/工具注册/插件系统**
- [ ] 能实现 Agent 的可观测性（Trace + 监控 + 日志）
- [ ] 能实现 Prompt Injection 检测和 PII 脱敏
- [ ] **能解释 Loop Engineering 中 Reflection、Plan-and-Execute、Tree-of-Thought 三种模式的原理和选型**
- [ ] **能为 Agent 系统实现循环安全（检查点/幂等性/死循环逃逸）**
- [ ] 能实现语义缓存和模型路由降低 30%+ 成本
- [ ] 能 Docker 化部署完整的 Agent 系统

---

## 阶段 5：终局 — 实战项目 + 面试（6 周）

### 第 1-3 周：旗舰项目 — MES 智能工单 Agent

**结合你的 MES 背景，做一个面试能镇场的作品。**

技术要求（展现你阶段 1-4 的全部能力）：

```
MES 智能工单 Agent
├── 🧠 Agent 层（LangGraph）
│   ├── 工单状态查询（查数据库）
│   ├── 异常分析（LLM 判断异常类型 + 原因）
│   ├── 处理方案推荐（RAG 查历史工单 + 知识库）
│   ├── 审批流程（Human-in-the-loop）
│   └── 自动执行（返工/报修/通知）
├── 📚 RAG 层
│   ├── MES 知识库（工艺路线/不良代码/设备手册）
│   ├── Hybrid Search + Reranker
│   └── Agentic RAG（自我纠错）
├── 🔒 安全层
│   ├── 输入检测（SQL 注入/Prompt Injection）
│   ├── 权限控制（不同角色可见不同数据）
│   └── 审计日志
├── 📊 可观测层
│   ├── Langfuse 全链路追踪
│   ├── 结构化日志
│   └── 成本监控面板
└── 🐳 部署层
    ├── Docker Compose
    ├── 环境配置（dev/test/prod）
    └── CI/CD Pipeline
```

项目交付物：
- GitHub 仓库（完整的 README + 架构图 + 部署文档）
- 演示视频（5 分钟内讲清楚功能和架构）
- 技术选型说明文档（为什么选这个框架/模型/参数）

### 第 4 周：简历 + 作品集包装

**你的独特卖点（USP）：**

```
传统 AI Agent 开发者         你
───────────────────────────────
只有通用开发经验          ✅  MES/ERP 行业 Know-how
只会 Python 生态         ✅  Java 3年+ 微服务架构
没做过生产级系统          ✅  企业级系统（多租户/分布事务）
没接触过安全合规          ✅  军工项目（涉密/安全）
只能做 Demo              ✅  能全栈独立交付
```

### 第 5-6 周：面试准备

**面试考点深度准备：**

| 方向 | 需要能讲透的深度 |
|------|----------------|
| Agent 原理 | ReAct Loop 的每一步、Tool Calling 的底层实现、Agent 为什么有时候会"跑偏"、怎么修复 |
| RAG 深度 | Chunking 策略的选型原因、Embedding 模型的数学直觉、Hybrid Search 的加权策略、Eval 指标的局限性 |
| 工程能力 | 系统设计（设计一个客服 Agent）、生产级考量（成本/延迟/可观测性/安全） |
| 架构对比 | LangChain vs 手写、LangGraph vs CrewAI、Chroma vs Qdrant vs Milvus |
| 行业结合 | MES 工单 Agent 的架构设计、制造业 AI 落地的特殊挑战 |

**模拟面试**：
- 准备 3 个项目的完整讲解（项目背景 → 技术选型 → 挑战 → 解决方案 → 成果）
- 准备 10 个高频面试题的深度回答
- 找至少 2 个人模拟面试

### 📌 阶段 5 熟练度自检清单

- [ ] 完成并部署 MES 智能工单 Agent（GitHub 公开）
- [ ] 简历突出 MES + AI Agent 的差异化定位
- [ ] 能不讲稿子讲清楚 3 个项目的架构和选型
- [ ] 能回答 10+ 个 Agent/RAG 面试题
- [ ] 有明确的目标公司列表和投递计划

---

## ⏰ 时间规划建议

| 时段 | 可以做 |
|------|--------|
| 工作日晚上（1-2h） | 读文档、写小练习、做阶段里的深度练习 |
| 周末（4-6h） | 做大项目推进、整合项目、复习回顾 |
| 碎片时间 | 想今天学的概念能不能讲清楚、想面试题怎么答 |

每个阶段之间留 **3-5 天缓冲**，用于补漏和复习。

---

## 📊 预算规划

参考 [[financial-status]]：

- **必要支出**：LLM API 调用费（每月 100-200 元）
- **可选支出**：向量数据库云服务（如 Qdrant Cloud 免费额度足够练习）
- **省钱策略**：本地模型（Ollama + Qwen）做开发调试，云端模型做最终测试

---

## 🔗 关联信息

- [[career-goal-ai-agent]] — 转行目标
- [[financial-status]] — 财务状况
- [[career-profile]] — 现有技能
- [[ai-agent-developer-tech-stack]] — Agent 岗位技术栈参考
- [[spring-mes-tech-stack]] — 当前项目技术栈

---

# 🔥 地狱压缩版：22周到年底找到工作

> **创建时间**：2026-07-13  
> **目标**：2026年12月31日前找到 AI Agent 应用开发工作（对标年薪20-35万）  
> **适用对象**：Java 3年转行，Python 基础差，自制力差  
> **核心策略**：**不做"学会了再做"，而是"做着做着就学会了"**

## 一、⚠️ 你必须接受五个残忍事实

### 事实 1：你没有时间打好基础了

从0开始学 Python → 学框架 → 做项目 → 找工作，22周是极限。**你不可能学完再动手，必须在做中学。**

### 事实 2：面试官不在乎你会多少

面试官只问三个问题：
1. **你做过什么**（GitHub 上能看到的东西）
2. **你能不能干活**（Agent 原理、RAG 原理）
3. **你有什么特别**（你的 MES 背景）

### 事实 3：你90%的时间应该花在"做"上，不是"学"上

```
❌ 看教程 2 小时 → 写代码 30 分钟   ← 你现在
✅ 写代码 2 小时 → 卡住了查 30 分钟   ← 你要变成这样
```

### 事实 4：你会无数次想放弃

第2周、第5周、第8周、第12周——这四个时间点你大概率会想"算了吧"。**承认这一点，提前设好护栏。**

### 事实 5：每天1小时，比周末狂学8小时有效得多

你的自制力经不起"周末补课"的诱惑。**每天固定时间做一件小事**，比"这周末我要肝一整天"靠谱100倍。

---

## 二、🏴 地狱规则（违反=计划失败）

这些规则**没有商量余地**。如果你做不到，你现在就可以放弃，别浪费半年时间：

1. **每天必须 push 代码到 GitHub** — 哪怕只改了 README 的一个字也算。连续3天没 push = 计划失败
2. **禁止看视频教程** — 视频是最大的时间陷阱。你只需要：文档 + 代码 + AI 助手答疑
3. **禁止 copy-paste** — 每一行代码必须是自己敲的（包括从文档复制）。敲一遍等于理解一遍
4. **周一到周五干活，周末必须休息** — 周末碰代码也算违规。休息是为了下周能启动
5. **每周日晚上写周报** — 在仓库 `log.md` 里写一句话：这周做了什么、下周要做什么

---

## 三、🗓️ 22周总览

```
7月              8月              9月              10月             11月             12月
│                │                │                │                │                │
[ 生存期 ]        [ Agent期 ]       [ 框架期 ]        [ RAG期 ]         [ 全栈期 ]        [ 冲刺期 ]
  2周              3周              4周              4周              4周              5周
Python速成       调通LLM+         LangChain+         RAG+向量库       多Agent+         旗舰项目+
→ FastAPI        手写Agent        LangGraph                          部署             面试准备
```

### 阶段划分

| 阶段 | 时间 | 目标 | 产出 |
|------|------|------|------|
| **S0 生存期** | 7/13 → 7/26 (2周) | Python + FastAPI 能干活 | GitHub: `mes-fastapi` 项目 |
| **S1 Agent期** | 7/27 → 8/16 (3周) | 手写 Agent Loop 跑通 | GitHub: `mini-agent` 项目 |
| **S2 框架期** | 8/17 → 9/13 (4周) | LangChain + LangGraph 熟练 | GitHub: `mes-agent` 项目 |
| **S3 RAG期** | 9/14 → 10/11 (4周) | RAG 知识库搭建 | GitHub: `mes-knowledge-base` 项目 |
| **S4 全栈期** | 10/12 → 11/8 (4周) | 多Agent + 可观测 + 部署 | GitHub: `mes-agent-platform` 项目 |
| **S5 冲刺期** | 11/9 → 12/31 (7周) | 旗舰项目 + 面试 | GitHub: 旗舰项目 + offer |

---

## 四、🚀 S0 生存期（7/13 - 7/26）：Python 能干活就行

**目标**：2周内能写 Python 后端 API，达到你 Java 的6成功力就够了。

### 不需要学的（面试不考）：
❌ 装饰器原理 ❌ 元类 ❌ `__slots__` ❌ async/await 事件循环详解 ❌ 生成器高级用法

### 必须学的：

**第1周：Python 基础 + Pydantic（7/13 → 7/19）**

| 天 | 任务 | 验收标准 |
|----|------|---------|
| 周一 7/13 | 装环境：Python 3.12 + VS Code + pip + venv | `python --version` 能跑 |
| 周二 7/14 | Python 类型系统：`str/int/float/bool/list/dict/Optional/Union` | 写 10 行带类型注解的代码 push 到 GitHub |
| 周三 7/15 | 函数 + 类：`def/class/self/__init__/@staticmethod/@classmethod` | 写一个带方法的类，push |
| 周四 7/16 | Pydantic 基础：`BaseModel`、字段类型、`model_dump()` | 定义一个 MES 工单 Pydantic 模型，push |
| 周五 7/17 | Pydantic 验证：`@field_validator`、`ConfigDict` | 给工单模型加字段验证（工单号格式、状态枚举），push |
| 周六日 | **休息** | ⛔ 不碰代码 |

**checkpoint：第1周结束 = GitHub 上有一个带 Pydantic 模型的 Python 项目**

**第2周：FastAPI + 简单项目（7/20 → 7/26）**

| 天 | 任务 | 验收标准 |
|----|------|---------|
| 周一 7/20 | FastAPI 路由：`@app.get/post/put/delete`、`Path/Query` | 写 1 个 hello world 接口，push |
| 周二 7/21 | FastAPI Pydantic 集成：请求体、响应体 | 写 2 个 CRUD 接口（模拟数据，不连数据库），push |
| 周三 7/22 | FastAPI 异常处理 + 日志 | 加全局异常处理 + 请求日志中间件，push |
| 周四 7/23 | httpx 基础：`httpx.get/post`、异常处理 | 写一个调外部 API 的小脚本，push |
| 周五 7/24 | **整合项目**：用 FastAPI 写 3 个 MES 工单 CRUD 接口（内存存储） | 项目能 run，所有接口能用 curl 测通，push |
| 周六日 | **休息** | ⛔ 不碰代码 |

**checkpoint：第2周结束 = GitHub 上有一个 FastAPI 项目，包含工单 CRUD + 异常处理 + 日志**

### 📦 S0 产出物
- GitHub 仓库：`mes-fastapi`
- 一个 FastAPI 项目（3个工单 CRUD 接口）
- 项目 README（一句话描述 + 如何启动）

### ❓S0 没学的东西
- 装饰器（第3周需要时再学）
- async/await 原理（能写就行，不需要懂底层）
- 测试（第4周再补）
- 数据库（第4周再连）

---

## 五、S1 Agent期（7/27 → 8/16）：写一个你自己的 Agent

### 第3周：调通 LLM API（7/27 → 8/2）

| 天 | 任务 |
|----|------|
| 周一 | 注册 Anthropic/OpenAI 账号，拿到 API Key |
| 周二 | httpx 调通 Claude API（非流式）→ push |
| 周三 | SSE 流式输出 → push |
| 周四 | 实现请求重试（指数退避）→ push |
| 周五 | 实现结构化输出（Pydantic + JSON）→ push |

### 第4-5周：手写 Agent Loop（8/3 → 8/16）

| 天 | 分段 |
|----|------|
| W4 周一至三 | 自己实现 Tool 注册系统 |
| W4 周四至五 | 自己实现 Agent Loop（ReAct 模式） |
| W5 周一至三 | 加 Human-in-the-loop + 错误处理 |
| W5 周四至五 | 整合成 `mini-agent` 项目，写 README |

### 📦 S1 产出物
- GitHub 仓库：`mini-agent`
- 不依赖 LangChain 的手写 Agent
- 能跑通：用户提问 → Agent 思考 → 调用工具 → 返回结果

---

## 六、S2 框架期（8/17 → 9/13）：LangChain + LangGraph

### 第6-7周：LangChain 核心（8/17 → 8/30）
- Tool + Memory + Retriever + Callback
- **产出**：用 LangChain 重构你的手写 Agent

### 第8-9周：LangGraph 工作流（8/31 → 9/13）
- StateGraph + Conditional Edge + Checkpoint + Human-in-loop
- **产出**：GitHub: `mes-agent` — MES 工单审批 Agent 工作流

---

## 七、S3 RAG期（9/14 → 10/11）：知识库

### 第10-11周：RAG 基础（9/14 → 9/27）
- Chunking + Embedding + Chroma/Qdrant + 检索
- **产出**：把你的 Wiki 内容做向量化搜索

### 第12-13周：高级 RAG（9/28 → 10/11）
- Hybrid Search + Reranker + Agentic RAG
- **产出**：GitHub: `mes-knowledge-base` — MES 知识库问答系统

---

## 八、S4 全栈期（10/12 → 11/8）：多 Agent + 生产化

### 第14-15周：多 Agent（10/12 → 10/25）
- CrewAI / LangGraph Supervisor 模式
- **产出**：3-Agent 协作系统（分析 → 审核 → 报告）

### 第16-17周：部署 + 可观测（10/26 → 11/8）
- Docker + Docker Compose + Langfuse + 模型路由 + 缓存
- **产出**：GitHub: `mes-agent-platform` — Docker 化部署的全套系统

---

## 九、S5 冲刺期（11/9 → 12/31）：旗舰项目 + 面试

### 第18-21周：MES 智能工单 Agent（11/9 → 12/6）
**你的王牌项目**。GitHub 公开展示。

技术栈：FastAPI + LangGraph + Qdrant + Docker + Langfuse

功能：
- Agent 根据工单内容自动分析异常
- RAG 查历史方案
- 人工审批确认
- Docker 部署

### 第22-24周：简历 + 面试（12/7 → 12/31）

| 周 | 任务 |
|----|------|
| W22 | 写简历，突出 MES + AI Agent 差异化 |
| W23 | 投递（每天投3家），准备10个面试题深度回答 |
| W24 | 模拟面试 + 查漏补缺 |

---

## 十、📊 你的差异化定位（面试用）

```
传统 Agent 开发者                   你
─────────────────────────────────────
只有 Python 经验                Java 3年 + 微服务 ✅
没做过企业级系统                 MES/ERP 军工项目 ✅
只会跑 Demo                     能全栈独立交付 ✅
没有行业背景                     制造业 Know-how ✅
```

**你的面试故事线**：
> "我做 MES 系统 3 年，看到了 AI 在制造业的机会。我独立做了一个 MES Agent 系统——工单异常分析 + 知识库查询 + 人工审批——把 AI 真正落地到生产场景。"

---

## 🔗 关联信息

- [[career-goal-ai-agent]] — 转行目标
- [[financial-status]] — 财务状况
- [[career-profile]] — 现有技能
- [[ai-agent-developer-tech-stack]] — Agent 岗位技术栈参考
