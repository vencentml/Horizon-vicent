---
layout: default
title: "Horizon Summary: 2026-05-17 (ZH)"
date: 2026-05-17
lang: zh
---

> From 80 items, 6 important content pieces were selected

---

1. [Cerebras 提交 600 亿美元 IPO，晶圆级 AI 芯片里程碑](#item-1) ⭐️ 9.0/10
2. [特朗普称对台军售是谈判筹码，危及美国信誉](#item-2) ⭐️ 9.0/10
3. [哈马斯加沙最高领导人在以色列空袭中身亡](#item-3) ⭐️ 9.0/10
4. [SGLang v0.5.12 添加对 DeepSeek V4 的完整推理支持](#item-4) ⭐️ 8.0/10
5. [llama.cpp b9180 增加多令牌预测与 GDN 回滚支持](#item-5) ⭐️ 8.0/10
6. [DeepSeek-V4-Flash 让 LLM 定向操控再度引人注目](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Cerebras 提交 600 亿美元 IPO，晶圆级 AI 芯片里程碑](https://www.latent.space/p/ainews-cerebras-60b-ipo-slowly-then) ⭐️ 9.0/10

Cerebras Systems 已提交首次公开募股（IPO）申请，估值达 600 亿美元，这是 AI 硬件行业的重大金融事件。 此次 IPO 表明投资者对晶圆级集成等替代芯片架构的强烈信心，可能改变由 NVIDIA 主导的竞争格局。 Cerebras 的晶圆级引擎 WSE-3 拥有 90 万个 AI 核心和 125 petaflops 算力，理论上相当于约 62 块 NVIDIA H100 GPU。

rss · Latent Space · May 16, 04:36

**背景**: 晶圆级集成（Wafer-scale integration）使用整个硅晶圆作为单一处理器，无需连接多个芯片。Cerebras 的芯片是有史以来最大的 AI 处理器，WSE-2 包含 2.6 万亿个晶体管和 85 万个核心。这些芯片使得单个系统能够训练超过 120 万亿参数的超大规模 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wafer-scale_integration">Wafer-scale integration - Wikipedia</a></li>
<li><a href="https://www.cerebras.ai/chip">Product - Chip - Cerebras</a></li>

</ul>
</details>

**标签**: `#AI`, `#hardware`, `#IPO`, `#Cerebras`, `#semiconductor`

---

<a id="item-2"></a>
## [特朗普称对台军售是谈判筹码，危及美国信誉](https://www.nytimes.com/2026/05/16/world/asia/trump-taiwan-arms-bargaining-chip-china.html) ⭐️ 9.0/10

特朗普总统表示，对台潜在军售可以成为与中国谈判的‘非常好的筹码’，这标志着美国政策的转变，明确将军售与更广泛的谈判挂钩。 这一表态引发了对美国保卫台湾承诺的根本性怀疑，可能破坏地区稳定，并改变印太地区的防御联盟格局。 特朗普的言论没有具体说明是哪个军售案或哪场谈判，但表明对长期战略原则采取交易性做法，给台湾及其其他盟友带来不确定性。

rss · NYTimes World · May 16, 15:11

**背景**: 美国历史上对台湾奉行‘战略模糊’政策，既不完全支持独立，也不放弃防御承诺。对台军售一直是支持台湾自卫同时管理对华关系的关键工具。特朗普将这些军售描述为谈判筹码，打破了这一传统。

**标签**: `#Geopolitics`, `#US-China`, `#Taiwan`, `#Risk`, `#Policy`

---

<a id="item-3"></a>
## [哈马斯加沙最高领导人在以色列空袭中身亡](https://www.nytimes.com/2026/05/15/world/middleeast/israel-gaza-haddad-hamas.html) ⭐️ 9.0/10

哈马斯官员证实，加沙地区哈马斯军事部门的最高领导人伊兹·丁·阿勒-哈达德在以色列的一次空袭中丧生。 这一刺杀事件是重大地缘政治事件，可能加剧以巴冲突，引发报复行动，进一步破坏地区稳定。 哈达德去年才接管哈马斯在加沙的军事部门，他的死亡标志着哈马斯权力结构的重大变化。

rss · NYTimes World · May 16, 14:29

**背景**: 哈马斯是一个控制加沙地带的巴勒斯坦激进组织。以色列和哈马斯多次发生冲突。一名最高领导人的被杀很可能引发哈马斯的强烈回应。

**标签**: `#geopolitical risk`, `#Middle East`, `#Hamas`, `#Israel`, `#conflict`

---

<a id="item-4"></a>
## [SGLang v0.5.12 添加对 DeepSeek V4 的完整推理支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.12) ⭐️ 8.0/10

SGLang v0.5.12 提供了对 DeepSeek V4 的完整推理支持，包括张量并行、专家并行、上下文并行和数据并行注意力，支持 Nvidia B300/B200/H200/H100/GB200/GB300 以及 AMD MI35X GPU，并集成了新的 DeepGemm 和 FlashMLA 内核。 此版本通过提供优化的内核和并行策略，显著降低了在生产环境中部署 DeepSeek V4 的门槛，提高了在多种硬件上大规模 LLM 服务的吞吐量和延迟。 新特性包括用于将非活跃 KV 缓存卸载到 CPU 内存的 HiSparse、精度损失可忽略的 W4A4 MegaMoE 内核，以及适用于所有 Nvidia GPU 的统一 Docker 镜像。该版本还增加了对投机解码 V2 以及 Intern-S2-Preview 和 MiniCPM-V 4.6 等多个新模型的支持。

github · Fridge003 · May 16, 18:23

**背景**: SGLang 是一个面向大语言模型的开源推理引擎，注重性能和灵活性。DeepSeek V4 是一种先进的混合专家（MoE）模型，需要先进的并行化和优化内核才能高效部署。该版本利用了 DeepGemm（一种专门用于 FP8 运算的 GEMM 内核库）和 MegaMoE（将 MoE 计算与通信融合以减少开销）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lmsys.org/blog/2026-04-10-sglang-hisparse/">HiSparse : Turbocharging Sparse Attention with... | LMSYS Org</a></li>
<li><a href="https://github.com/deepseek-ai/DeepGEMM">GitHub - deepseek-ai/DeepGEMM: DeepGEMM: clean and efficient FP8 GEMM ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#llm-inference`, `#open-source`, `#gpu-kernels`

---

<a id="item-5"></a>
## [llama.cpp b9180 增加多令牌预测与 GDN 回滚支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9180) ⭐️ 8.0/10

llama.cpp 版本 b9180 引入了原生多令牌预测支持，并在 CPU、Metal 和 Vulkan 后端实现了 GDN 模型的部分回滚功能。 此更新通过减少草稿令牌被拒绝时的计算浪费，显著提升了推测解码效率，并使得在多样化硬件上部署大型语言模型更加灵活。MTP 通过同时预测多个未来令牌进一步提高推理吞吐量。 MTP 实现使用轻量级头部，共享主模型的嵌入和输出层，每个头部仅需额外一个 transformer 层。GDN 部分回滚通过存储中间状态，允许回滚最多 `draft_max` 个令牌而无需完全重新执行模型。

github · github-actions[bot] · May 16, 16:48

**背景**: 多令牌预测通过修改 transformer 使其一次预测多个未来令牌，提高了效率和长程规划能力。推测解码使用较小的草稿模型提出令牌，再由目标模型验证，从而加速 LLM 推理，但当草稿被拒绝时会浪费计算。Gated Delta Networks 是一种线性 transformer 架构，使用门控增量规则进行内存管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@bingqian/understanding-multi-token-prediction-mtp-in-deepseek-v3-ed634810c290">Understanding Multi - Token Prediction ( MTP ) in ... | Medium</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog</a></li>
<li><a href="https://deepwiki.com/NVlabs/GatedDeltaNet">NVlabs/GatedDeltaNet | DeepWiki</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#MTP`, `#speculative decoding`, `#inference performance`

---

<a id="item-6"></a>
## [DeepSeek-V4-Flash 让 LLM 定向操控再度引人注目](https://www.seangoedecke.com/steering-vectors/) ⭐️ 7.0/10

文章指出，DeepSeek-V4-Flash 中的定向向量可以移除模型的拒绝行为（即“消拒”技术），使 LLM 定向操控再次成为高关注领域。antirez 的 DwarfStar 项目展示了通过定向操控完全移除拒绝行为的实践。 这一发展开启了探索对齐模型中隐藏能力的途径，对 AI 安全与模型对齐具有重大意义。它使研究人员和实践者无需重新训练即可微调模型行为，有望带来更灵活、更有用的 AI 系统。 定向向量通过在推理过程中向模型特定层的内部激活添加计算出的方向来工作。antirez 的 DwarfStar 项目是一个独立的工具，而非 llama.cpp 的简化版，它使用一个小型玩具数据集来演示拒绝移除。

hackernews · Brajeshwar · May 16, 14:58

**背景**: 定向向量是模型潜在空间中的方向，将其添加到激活中可以在不重新训练的情况下将输出导向期望方向。DeepSeek V4 是一种使用混合专家和多头潜在注意力的大型语言模型。此前已有研究表明，通过识别早期模型中的单一拒绝向量，可以实现“消拒”（移除拒绝行为）技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alignmentforum.org/posts/QQP4nq7TXg89CJGBh/a-sober-look-at-steering-vectors-for-llms">A Sober Look at Steering Vectors for LLMs</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/technical-deepseek">A Technical Tour of the DeepSeek Models from V3 to V3.2</a></li>
<li><a href="https://cdn.deepseek.com/policies/en-US/model-algorithm-disclosure.html">Model Mechanism and Training Methods of DeepSeek</a></li>

</ul>
</details>

**社区讨论**: antirez 和 NitpickLawyer 等评论者强调了定向向量在移除拒绝行为方面的有效性。社区对探索隐藏能力以及将定向操控整合到用户界面中感到兴奋，但也有关于 DwarfStar 是否独立于 llama.cpp 的讨论。

**标签**: `#LLM`, `#steering vectors`, `#DeepSeek`, `#AI safety`, `#model alignment`

---