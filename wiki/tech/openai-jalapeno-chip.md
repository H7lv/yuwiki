---
title: OpenAI Jalapeño 自研 AI 推理芯片
tags: [ai, hardware, openai, chip, llm-inference]
created: 2026-06-25
updated: 2026-06-25
source: OpenAI/Broadcom 联合发布，2026年6月24日
---

2026年6月24日，OpenAI 联合 Broadcom 发布首款自研 AI 推理芯片 **Jalapeño**，定位为"LLM 优化的智能处理器"，从设计到流片仅用 9 个月，推理成本声称可降低约 50%。这是 OpenAI 从纯软件公司走向软硬件一体化的标志性转折点。

## 背景与动因

### OpenAI 为什么要自研芯片？

- **降低对 NVIDIA 的依赖**：推理工作负载不再完全依赖 NVIDIA GPU，在定价和供应上获得更多筹码
- **全栈控制**：掌控芯片架构 → 内核 → 内存系统 → 网络 → 服务基础设施 → 模型 → 产品的完整链路
- **成本优化**：大模型推理成本极高，定制 ASIC 可比通用 GPU 显著降低成本
- **跟随行业趋势**：Google（TPU）、Amazon（Trainium）、Meta（MTIA）、Microsoft（Maia）均已入局

### 与 Broadcom 的合作模式

| 角色 | 公司 | 职责 |
|------|------|------|
| 芯片设计 | OpenAI | 架构定义、AI 辅助设计 |
| 硅实现 & 网络 | Broadcom | 芯片实现、Tomahawk 网络芯片、连接方案 |
| 板卡/系统集成 | Celestica | 板卡、机架、系统级集成 |
| 制造 | TSMC | 芯片代工生产 |

---

## 技术深度分析

### 芯片架构

Jalapeño 是一颗 **定制 ASIC**，专为大语言模型推理设计：

- **Die 尺寸**：约 **840 mm²**（接近 EUV 光刻最大掩模版尺寸，与 NVIDIA Blackwell 同级）
- **内存**：板上集成 **6 个 HBM 模块**（推测为 HBM3E 或 HBM4），提供超高带宽
- **网络**：集成 Broadcom **Tomahawk** 交换芯片，优化多芯片互联
- **设计理念**：从零开始"空白纸面"设计，专为现代 LLM 推理优化，而非从旧 AI 工作负载改造
- **利用率优化**：通过减少数据搬运、平衡计算/内存/网络三大子系统，使实际利用率"更接近理论峰值"

### 性能与成本

| 指标 | 声称值 | 备注 |
|------|--------|------|
| 能效比 | "大幅优于业界最佳" | 内部测试，尚无独立验证 |
| 推理成本 | 降低约 **50%** | Broadcom CEO 声称 |
| 性能对标 | 与 **NVIDIA Blackwell**、**Google TPU** 相当 | 推理任务 |
| 时延 | 兼具高吞吐和低时延 | 目标是将吞吐与专用推理芯片的时延结合 |

### 训练 vs 推理

| 能力 | 是否支持 |
|------|---------|
| **推理** | ✅ 核心设计目标 |
| **训练** | ❌ 不支持（NVIDIA 仍是训练合作伙伴） |
| **跨模型兼容** | ✅ 支持业界所有 LLM，不限 OpenAI 自家模型 |

---

## 开发与部署时间线

### 惊人的开发速度

从设计到流片（tape-out）仅用 **9 个月**，号称高性能半导体领域最快的 ASIC 开发周期之一。其中一个关键因素是 **AI 辅助设计**——OpenAI 使用自己的 AI 模型加速了芯片设计和优化部分环节，形成了"AI 设计芯片 → 更好的芯片跑 AI"的自我强化飞轮。

### 部署路线图

```
2026年6月   —— 发布，工程样片已在实验室运行 GPT-5.3-Codex-Spark
2026年底   —— 首次部署（Microsoft 等合作伙伴的吉瓦级数据中心）
2027年     —— 量产
2028年上半年 —— 全面运营
2029年     —— 目标 10 吉瓦算力（≈ 10 座核反应堆）
```

---

## 产业影响分析

### 对 NVIDIA 的挑战

Jalapeño 目前仅覆盖推理环节，而 NVIDIA 在训练环节的领先地位未受直接影响。但其意义在于：**OpenAI 获得了定价权和供应链上的谈判筹码**，不再完全受制于 NVIDIA 的供应和定价。

### 对 AI 产业格局的影响

1. **软硬一体化成为主流**：领先的 AI 公司都在自研芯片，纯"模型公司"的模式正在转变
2. **推理成本下降**：定制芯片有望显著降低推理成本，加速 AI 应用普及
3. **算力军备竞赛升级**：从 GPU 数量竞争转向芯片架构和全栈优化竞争
4. **代工厂竞争**：TSMC 作为制造方，核心地位进一步巩固

### 尚需验证的问题

- ⚠️ **尚无独立基准测试** — 所有性能数据来自 OpenAI/Broadcom 自身测试
- ⚠️ **量产良率** — 840mm² 大芯片的量产良率是传统挑战
- ⚠️ **执行风险** — 9 个月流片 ≠ 吉瓦级规模的可靠量产

---

## 同期 AI 进展（2026年6月）

### 🔬 世界模型范式革命 — 智源 悟界·Physis

6月12日，北京智源大会发布全球首款通用世界基座模型 **悟界·Physis-v0.1**，标志着 AI 从"预测下一个 Token"迈向"预测下一个物理状态"。这是中国在 AI 领域首次与世界处于同一起跑线。

### 🧠 AI 攻克数学难题

- OpenAI AI 在"平面单位距离问题"中设计出超越人类几何直觉的新构造
- ChatGPT 辅助破解 **埃尔德什第 1196 号问题**（60 年未解）
- 数学家陶哲轩指出：AI 走出了"人类没想到的路"

### 🤖 田渊栋 Recursive — AI 自我改进

前 Meta FAIR 研究总监田渊栋创立的 **Recursive Superintelligence**（估值 46.5 亿美元）发布首个成果：在 NVIDIA GPU 优化榜单上获得 SOTA，实现"AI 自己改进 AI 本身"的完整闭环。

### 🗣️ BabelTele — AI 语言

上海交大等提出 **BabelTele**：将文本压缩至 27.9%，保留 99.5% 语义，生成人类难懂但模型能懂的精简语言，可减少 40% 通信 Token。

---

## 相关概念

- [[llm-inference-optimization]] — LLM 推理优化技术
- [[ai-chip-landscape]] — AI 芯片产业格局
- [[nvidia-vs-custom-ai-chips]] — 自研 AI 芯片 vs GPU 对比
- [[world-model-paradigm]] — 世界模型范式

---

## 参考资料

- [OpenAI 官方公告](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)
- [Broadcom 官方新闻稿](https://www.globenewswire.com/fr/news-release/2026/06/24/3316887/19933/en/openai-and-broadcom-unveil-llm-optimized-intelligence-processor.html)
- [HPCwire 报道](https://www.hpcwire.com/aiwire/2026/06/24/openai-and-broadcom-unveil-llm-optimized-intelligence-processor/)
- [The Next Web 分析](https://thenextweb.com/news/openai-jalapeno-chip-broadcom-nvidia)
