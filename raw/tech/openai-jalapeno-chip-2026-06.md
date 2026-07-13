# OpenAI & Broadcom 发布首款自研 AI 推理芯片 Jalapeño

> 原始来源整理自多个新闻源（2026年6月24日）
>
> 来源：
> - [OpenAI 官方公告](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)
> - [GlobeNewswire - Broadcom 官方新闻稿](https://www.globenewswire.com/fr/news-release/2026/06/24/3316887/19933/en/openai-and-broadcom-unveil-llm-optimized-intelligence-processor.html)
> - [HPCwire / AIwire](https://www.hpcwire.com/aiwire/2026/06/24/openai-and-broadcom-unveil-llm-optimized-intelligence-processor/)
> - [The Next Web](https://thenextweb.com/news/openai-jalapeno-chip-broadcom-nvidia)
> - [Business Korea](https://www.businesskorea.co.kr/news/articleView.html?idxno=271972)
> - [Yahoo Tech](https://tech.yahoo.com/ai/articles/openai-reveals-first-ai-chip-164128666.html)

---

## 核心新闻

2026年6月24日，OpenAI 联合 Broadcom（博通）正式发布了其首款自研 AI 芯片 **Jalapeño**，定位为"LLM 优化的智能处理器"（Intelligence Processor）。这是 OpenAI 从纯软件/模型公司走向软硬件一体化战略的关键转折点。

---

## 技术规格

| 规格 | 详情 |
|------|------|
| **芯片类型** | 定制 ASIC（专用集成电路），专为 LLM 推理设计 |
| **制程工艺** | 未公开披露 |
| **Die 尺寸** | 约 **840 mm²**（分析师估算，接近 EUV 光刻最大掩模版尺寸） |
| **内存** | 板上集成 **6 个 HBM 模块**（HBM3E / HBM4） |
| **网络** | 集成 Broadcom **Tomahawk** 网络芯片 |
| **工作负载** | 已成功运行 **GPT-5.3-Codex-Spark** 达到目标生产规格 |

## 性能声称

- **能效比**："大幅优于当前业界最佳"（OpenAI/Broadcom 内部测试）
- **推理成本**：Broadcom CEO Hock Tan 声称推理成本可降低约 **50%**
- **性能对标**：与 NVIDIA Blackwell GPU 和 Google TPU 在推理任务上"相当"
- **利用率**：架构目标是通过减少数据搬运、平衡计算/内存/网络，使实际利用率"更接近理论峰值"
- **时延**：目标是将领先加速器的吞吐量与最快专用推理芯片的时延结合起来

## 开发时间线

- **设计到流片（tape-out）**：仅 **9 个月** — 号称高性能半导体领域最快的 ASIC 开发周期
- **AI 辅助设计**：OpenAI 使用自己的 AI 模型加速了部分芯片设计和优化过程
- **当前状态**：工程样品已在实验室运行 GPT-5.3-Codex-Spark
- **首次部署**：2026 年底，在 Microsoft 等合作伙伴的吉瓦级数据中心进行原型部署
- **量产**：2027 年
- **全面运营**：2028 年上半年
- **长期目标**：到 2029 年达到 10 吉瓦算力（约相当于 10 座核反应堆）

## 合作伙伴

- **Broadcom**：硅实现、网络芯片（Tomahawk）、连接方案
- **Celestica**：板卡、机架和系统集成
- **TSMC**：芯片制造代工厂

## 战略意义

1. **降低对 NVIDIA 的依赖**：推理工作负载不再完全依赖 NVIDIA GPU，在定价和供应上获得更多筹码
2. **全栈控制**：OpenAI 现在掌控芯片架构 → 内核 → 内存系统 → 网络 → 服务基础设施 → 模型 → 产品的完整链路
3. **AI 设计芯片的飞轮**：用 AI 加速芯片设计 → 更好的芯片跑 AI → 形成自我强化的正循环
4. **多代路线图**：已规划多代芯片，下一代目标 2028 年
5. **行业趋势**：加入 Google（TPU）、Amazon（Trainium）、Meta（MTIA）、Microsoft（Maia）的自研 AI 芯片阵营

## 重要须知

- **尚无独立基准测试** — 所有性能数据来自 OpenAI/Broadcom 自身测试
- **推理专用** — 不涉及训练环节（NVIDIA 在训练领域的领先地位未受挑战）
- **跨模型兼容** — 设计上支持业界所有 LLM，不限于 OpenAI 自家模型
- **技术白皮书待发布** — 详细架构和基准测试预计在未来数月内发布

---

## 同期其他 AI 重大进展（2026年6月）

### 🔬 世界模型：智源发布全球首个通用世界基座模型（6月12日）

北京智源大会发布 **悟界·Physis-v0.1**，全球首款通用世界基座模型，标志着 AI 从"预测下一个 Token"迈向"预测下一个物理状态"的范式革命。同步发布具身大脑模型 **悟界·RoboBrain Orca**。

### 🧠 AI 深度融入数学研究

- OpenAI AI 系统在"平面单位距离问题"中设计出全新点集构造方法，突破人类几何直觉
- 23岁英国业余爱好者在 ChatGPT 辅助下破解了困扰数学家 60 年的埃尔德什第 1196 号问题

### 🤖 田渊栋创业公司 Recursive 的首个成果（6月12日）

前 Meta FAIR 研究总监田渊栋创立的 **Recursive Superintelligence**（刚完成6.5亿美元融资）在 NVIDIA GPU 优化榜单上获得整体和4个子类别的 SOTA，实现"AI 自己改进 AI 本身"的闭环。

### 🗣️ 中国科学家提出"AI 语言" BabelTele（6月18日）

上海交大等提出 **BabelTele** 文本压缩方法：将文本压缩至 27.9%，保留 99.5% 语义，生成人类难懂但模型能懂的精简语言。

### 🏥 智源大会医疗与科学 AI 成果

- **悟界·Brainμ1.0**：全球首个多模态神经科学大模型（已刊发 Science）
- **BAAI Cardiac Agent**：心脏磁共振辅助诊断智能体
- **悟界·OpenComplex2.5**：AI 驱动药物发现模型

---

## 2026年6月 AI 趋势总结

1. **从虚拟到物理**：世界模型成为 AI 下一个核心赛道
2. **AI 自我改进**：递归式自我提升成为新范式
3. **软硬一体化**：芯片自研降低推理成本
4. **AI 辅助科研**：数学、医疗、药物发现等领域深度应用
