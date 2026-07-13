# 操作日志

> 按时间顺序记录 Wiki 的所有重要操作：摄入、查询、检查、重构。
> 格式：`## [日期] 操作类型 | 简短描述`

---

## [2026-06-25] init | 初始化 Wiki

- 创建目录结构：`raw/`（tech, life, assets）、`wiki/`（tech, life, templates）
- 编写 `CLAUDE.md`（Schema 层，定义工作流和约定）
- 创建 `wiki/index.md`（内容索引）
- 创建页面模板（concept, source-note, personal）
- 初始化完成，Wiki 准备就绪

## [2026-06-25] ingest | OpenAI Jalapeño 自研 AI 推理芯片

- 搜索并收集 2026 年 6 月 AI 最前沿新闻（Jalapeño 芯片发布 + 同期多项突破）
- 保存原始文章到 `raw/tech/openai-jalapeno-chip-2026-06.md`
- 创建 Wiki 详情页 `wiki/tech/openai-jalapeno-chip.md`（含技术分析、产业影响、时间线、同期进展）
- 更新 `wiki/index.md` 索引
- 更新本日志
- 相关标签：`ai`, `hardware`, `openai`, `chip`, `llm-inference`

## [2026-06-25] config | 记忆系统迁移到时间快照模式

- 记忆文件从外部目录 (`C:\Users\86130\.claude\projects\...\memory`) 迁移到 Wiki 项目内部 `wiki/memory/`
- 新增约定：每次对话结束拍一张完整快照，保留所有旧快照，形成可回溯的时间线
- 创建第一张快照 `wiki/memory/snapshot-2026-06-25.md`
- 更新 `CLAUDE.md` 中的目录结构和记忆维护流程

## [2026-06-25] redesign | Wiki 全面重构 — 基于模板升级

- 基于 `template.prompt.md` 全面重构 Wiki 架构
- 新增目录：`profile/`、`inbox/`、`me/`、`health/`、`projects/`、`learning/`、`journal/`、`decisions/`、`reference/`、`sources/`
- 创建 `profile/profile.md`（大麦人格档案）和 `profile/memory.md`（跨对话记忆）
- 创建各新目录的 README 指引文件
- 重写 `CLAUDE.md`：新增 Deep Think 工作流、inbox 整理、定期审查、对话终止仪式、反退化三层体系、搜索方式文档
- 触发指令精细化：说"你好大麦"才进入 Wiki 模式，普通聊天不动 wiki
- 对话终止仪式：更新 profile/memory.md + 拍时间快照 + 更新索引/日志
- 所有内容严格保存在 Wiki 项目内部
