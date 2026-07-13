---
name: personal-wiki-setup
description: 基于 llm-wiki 模式搭建的个人知识 Wiki 的架构和约定
metadata:
  type: project
---

# 个人 Wiki 搭建记录

基于 llm-wiki.md 模式搭建的个人知识 Wiki，位于 `d:\personal-wiki\`。

**架构**：三层 — raw/（原始资料，只读）、wiki/（LLM 维护的页面）、CLAUDE.md（Schema 层）

**用途**：技术学习笔记 + 个人成长记录

**约定**：
- 文件名英文 kebab-case，内容中文为主
- 页面使用 YAML frontmatter（title, tags, created, updated, source）
- 交叉引用使用 `[[page-name]]` 语法
- 标签使用英文小写（如 react, javascript, journal, goal）

**工作流**：
- `/ingest` — 摄入新资料到 raw/ → 讨论 → 写 wiki 页面 → 更新索引和日志
- `/query` — 基于 Wiki 回答问题，有价值的回答归档到 wiki/
- `/lint` — 健康检查：矛盾、孤立页、过期声明、缺失页面
- **记忆维护** — 每次对话结束前，将当前 Wiki 状态拍成时间快照，存入 wiki/memory/

**角色设定**：用户称呼我为「大麦」。当用户说"你好大麦"时，检索所有记忆后以热情有条理的助手身份回应。

**目录**：`raw/{tech,life,assets}/`、`wiki/{tech,life,templates,memory}/` + `wiki/index.md` + `log.md`

**工具**：VS Code 浏览 markdown

**Why:** 一次性搭建好结构后，后续需要记住这些约定才能正确维护 Wiki。

**How to apply:** 每次与用户交互时，自动读取 CLAUDE.md 中的工作流定义来执行摄入、查询和维护操作。每次对话结束时，拍一张 Wiki 状态快照存入 wiki/memory/。
