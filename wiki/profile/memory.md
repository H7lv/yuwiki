---
title: 大麦的对话记忆
tags: [profile, memory, meta]
created: 2026-06-25
updated: 2026-07-13
type: memory
---

# 跨对话记忆

记录和你之间的重要对话、突破性发现、关键决策等。

## 重要瞬间

- **2026-06-25** — Wiki 全面重构！基于模板升级了目录结构、工作流和 CLAUDE.md。新增了 profile 系统、inbox、Deep Think 等功能。Wiki 从单纯的 tech 知识库扩展为覆盖技术、生活、健康、决策的综合 Wiki。
- **2026-06-26** — 收到日月重工 MES 开发经理&架构师面试消息（年薪40万以内，鄞州区）。用户选择暂不推进，等正式面试邀请再准备。
- **2026-07-13** — **AI Agent 找工地狱计划启动！** 用户主动要求地狱难度标准，说"底子差、自制力差"。大麦制定了"地狱压缩版"22 周路线，砍掉一切花里胡哨，只留面试要考的核心。设计了 5 条地狱规则（每天 push、禁看视频、禁止 copy-paste、周末休息、周报）。用户当天就创建了 GitHub 仓库 `AiAgentWikiLearning`，装好 Python 3.13 + FastAPI，跑通第一个接口，push 成功。**S0 第 1 天任务超额完成。**

## 上次对话精简记录

**对话时间**：2026-07-13

**做了什么**：
1. 用户说"你好大麦"，要求制定年底找到 AI Agent 开发工作的地狱难度学习计划
2. 大麦分析了用户情况（Java 3年+、底子差、自制力差），设计了 5 条地狱规则（每天 push 代码、禁看视频、禁止 copy-paste、周一到周五干活周末休息、周报）
3. 在 `learning/ai-agent-roadmap.md` 追加「地狱压缩版：22周到年底找工」路线
4. 用户创建了 GitHub 仓库 `AiAgentWikiLearning`（私有），大麦指导配置了 SSH 连接
5. 用户用 FastAPI 写了一个 Hello MES Agent 接口并成功运行
6. 学习了 Python 类型注解（`str/int/Optional/Union`）、Pydantic 模型、字段验证、FastAPI 完整 CRUD 路由
7. 记录了 GitHub SSH Key 和仓库配置到 `wiki/reference/github-config.md`

**当前状态**：Wiki 新增了**地狱压缩版学习路线**和 **GitHub 配置参考页**。用户已经完成了 S0 生存期的全部任务（比计划提前 2 天）。本地有两个仓库：`D:\ai\personal-wiki`（Wiki）和 `D:\ai\AiAgentWikiLearning`（学习代码）。

**待办**：
- 继续推进地狱计划 S1 Agent 期（手写 Agent Loop）
- 日月重工 MES 面试 — 等收到正式面试申请再推进（仍挂起）
- 大麦作为监督员，每周检查用户进度

---

## 关于本文件

- 这是你的「跨对话记忆」文件
- 「上次对话精简记录」区块在每次对话**结束时更新覆盖**（始终只有一条记录）
- 「重要瞬间」区块持续追加，不删除
- 时间快照（`wiki/memory/snapshot-*.md`）提供完整的 Wiki 状态历史，与此文件互补
