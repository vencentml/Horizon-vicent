---
layout: default
title: "Horizon Summary: 2026-05-06 (ZH)"
date: 2026-05-06
lang: zh
---

> From 51 items, 13 important content pieces were selected

---

1. [SGLang v0.5.11 发布，带来重大性能升级](#item-1) ⭐️ 8.0/10
2. [llama.cpp b9045 新增 granite-speech 支持](#item-2) ⭐️ 8.0/10
3. [langchain 0.3.29 修复关键反序列化漏洞](#item-3) ⭐️ 8.0/10
4. [DNSSEC 配置错误导致.de 域名中断](#item-4) ⭐️ 8.0/10
5. [Gemma 4 使用多令牌预测加速推理](#item-5) ⭐️ 8.0/10
6. [计算机使用比结构化 API 贵 45 倍](#item-6) ⭐️ 8.0/10
7. [扎克伯格亲自授权 Meta 侵犯版权](#item-7) ⭐️ 8.0/10
8. [Transformers v5.8.0 新增 DeepSeek-V4 等多个模型](#item-8) ⭐️ 7.0/10
9. [LangChain Core 1.3.3 补丁版本包含安全修复](#item-9) ⭐️ 7.0/10
10. [LangChain Core 0.3.85 增强 load() 对不可信清单的安全性](#item-10) ⭐️ 7.0/10
11. [Langchain-classic 1.0.6 修复安全漏洞](#item-11) ⭐️ 7.0/10
12. [五角大楼试图让《星条旗报》监察员噤声](#item-12) ⭐️ 7.0/10
13. [加州农民因德尔蒙破产销毁 42 万棵桃树](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.11 发布，带来重大性能升级](https://github.com/sgl-project/sglang/releases/tag/v0.5.11) ⭐️ 8.0/10

SGLang v0.5.11 升级至 CUDA 13 和 PyTorch 2.11，将投机解码 V2 设为默认，并为预填/解码（PD）分离部署新增了解码端基数缓存。该版本还提供了对 Gemma 4、GLM-5.1、Qwen3.6、Kimi-K2.6 等模型的首日支持，并引入了新内核以及 DeepSeek-V3 和 Kimi-K2 的 LoRA 支持。 这些更新显著提升了生产环境中 LLM 推理的速度并降低了延迟，特别是通过默认的投机解码 V2 和为 PD 分离提供的解码端基数缓存。新增的首日模型支持以及大型模型的 LoRA 支持，确保了 SGLang 在最新前沿模型和微调场景中的竞争力。 投机解码 V2 使用重叠调度来隐藏 CPU 开销，降低了每步成本。解码端基数缓存可在分离部署中恢复命中率并节省首 Token 延迟（TTFT）。CUDA 13 和 Torch 2.11 解锁了更新的内核，该版本还包括 DFLASH 投机解码、FA3 内核以及增强的上下文并行。

github · Kangyan-Zhou · May 5, 21:28

**背景**: SGLang 是一个开源的 LLM 推理引擎，以高效和灵活执行著称。投机解码通过使用小型草稿模型生成多个 token，再由大模型并行验证，从而加速推理，降低延迟且不损失质量。基数缓存以树结构组织 KV 缓存，实现高效的前缀共享；而预填/解码（PD）分离将预填和解码阶段分开，以优化服务系统中的资源利用率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog</a></li>
<li><a href="https://github.com/tiannuo-yang/radix-cache-llm-serving">GitHub - tiannuo-yang/radix-cache-llm-serving: Radix Cache for LLM Serving</a></li>
<li><a href="https://bentoml.com/llm/inference-optimization/prefill-decode-disaggregation">Prefill-decode disaggregation | LLM Inference Handbook</a></li>

</ul>
</details>

**标签**: `#open-source`, `#LLM inference`, `#CUDA`, `#speculative decoding`, `#radix cache`

---

<a id="item-2"></a>
## [llama.cpp b9045 新增 granite-speech 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9045) ⭐️ 8.0/10

llama.cpp 的 b9045 版本新增了对 IBM granite-speech 多模态模型的支持，包括采用 Shaw 相对位置编码的 Conformer 编码器、QFormer 投影器以及音频预处理流水线。 这使得开发者能够在消费级硬件上本地运行最先进的语音理解模型，使用高效的 llama.cpp 推理引擎，从而拓宽了多模态人工智能能力的可访问性。 该实现包括具有 GLU 门控和 SSM 深度可分离卷积的 Conformer 编码器、使用窗口交叉注意力（窗口=15，查询=3）的 QFormer 投影器，以及通过对数梅尔频谱图进行 2 倍帧堆叠的音频预处理。

github · github-actions[bot] · May 6, 13:33

**背景**: llama.cpp 是一个开源 C++ 库，用于在 CPU 和 GPU 上高效运行大型语言模型。IBM 的 granite-speech 模型是一种结合语音和文本理解的多模态模型。Conformer 是一种卷积增强的 Transformer 架构，对语音识别有效；Q-Former 使用可学习查询来压缩来自模态编码器的特征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sooftware/conformer">GitHub - sooftware/conformer: [Unofficial] PyTorch implementation of "Conformer: Convolution-augmented Transformer for Speech Recognition" (INTERSPEECH 2020) · GitHub</a></li>
<li><a href="https://medium.com/@duongtr/askmore-building-a-vqa-model-from-scratch-in-pytorch-part-3-q-former-projector-7f1c8fd6b81c">Askmore: Building a VQA Model from Scratch in PyTorch — Part 3: Q-Former Projector | by Duong Tran | Medium</a></li>
<li><a href="https://arxiv.org/html/2405.05007">HC-Mamba: Vision MAMBA with Hybrid Convolutional Techniques for Medical Image Segmentation</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#granite-speech`, `#multimodal`, `#inference`, `#open-source`

---

<a id="item-3"></a>
## [langchain 0.3.29 修复关键反序列化漏洞](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D0.3.29) ⭐️ 8.0/10

LangChain 发布了 0.3.29 版本，包含两项安全修复：限制 `langchain.storage._lc_store` 中的反序列化，并加固 `load()` 函数以防范不可信 manifest。 这些修复解决了关键的反序列化漏洞，攻击者可能利用它们执行任意代码或窃取秘密。运行生产系统的用户应立即更新以降低风险。 第一项修复限制了 `_lc_store` 中的反序列化，防止不安全对象实例化；第二项通过验证并拒绝不可信 manifest 来加固 `load()` 函数。这些漏洞与序列化时对保留键 'lc' 处理不当有关。

github · github-actions[bot] · May 5, 21:02

**背景**: LangChain 是一个广泛使用的框架，用于构建大语言模型（LLM）应用。当用户控制的数据未正确转义时，会产生序列化漏洞，攻击者可通过保留键（如 'lc'）注入恶意对象。之前的 CVE（如 CVE-2025-68664）已指出 LangChain Core 中的类似问题，促使本次对 langchain 主包的修补。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.upwind.io/feed/cve-2025-68664-langchain-serialization-injection">CVE-2025-68664: LangChain Serialization Injection in dumps() and load()</a></li>

</ul>
</details>

**标签**: `#security`, `#langchain`, `#deserialization`, `#patch`, `#vulnerability`

---

<a id="item-4"></a>
## [DNSSEC 配置错误导致.de 域名中断](https://status.denic.de/pages/incident/592577eab611ce1e0d00046f/69fa60ef9d12f5057a974f38) ⭐️ 8.0/10

德国.de 域名注册管理机构 DENIC 的一次 DNSSEC 配置错误导致所有验证解析器对.de 域名返回 SERVFAIL。问题在一个员工派对后得到解决，Cloudflare 暂时禁用了其 1.1.1.1 解析器上的 DNSSEC 验证。 此事件凸显了 DNSSEC 部署的脆弱性以及配置错误可能导致大规模中断的潜在风险。它迫使像 Cloudflare 这样的主要解析器运营商禁用验证，从而削弱了 DNSSEC 的安全优势。 配置错误涉及一个针对 NSEC3 记录的 RRSIG，该签名无法与密钥标签为 33834 的区域签名密钥（ZSK）验证。由于 DENIC 名称服务器的任播分布，出现了间歇性问题。

hackernews · warpspin · May 5, 20:16

**背景**: DNSSEC（域名系统安全扩展）为 DNS 记录添加加密签名，以确保真实性和完整性。DENIC 是德国国家代码顶级域名.de 的注册管理机构。产生无效签名的配置错误可能导致验证解析器拒绝该域名的所有查询。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DNSSEC">DNSSEC</a></li>
<li><a href="https://en.wikipedia.org/wiki/DENIC">DENIC</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，这是一个 DNSSEC 验证失败问题，而非名称服务器中断。有人幽默地提到 DENIC 团队正在参加派对，Cloudflare 确认他们禁用了 1.1.1.1 上的 DNSSEC 验证。一位用户评论说，目前还没有出现 tptacek 的 DNSSEC 抨击。

**标签**: `#dnssec`, `#dns`, `#incident`, `#security`, `#infrastructure`

---

<a id="item-5"></a>
## [Gemma 4 使用多令牌预测加速推理](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) ⭐️ 8.0/10

谷歌的 Gemma 4 引入了多令牌预测草稿器，通过每步生成并验证多个令牌来加速推理，且不降低质量。 该技术将延迟降低 2-3 倍，同时保持输出质量，使大型语言模型更具成本效益，更适用于实时应用。 该方法利用投机解码，小型草稿模型提出令牌，主 Gemma 4 模型并行验证。社区报告显示，与其他模型相比，Gemma 每个输出使用的令牌数显著更少。

hackernews · amrrs · May 5, 16:14

**背景**: 投机解码是自回归 LLM 的一种推理优化技术，每步生成多个令牌。小型草稿模型提出候选令牌序列，大型目标模型通过拒绝采样在单次前向传递中验证它们，从而保持原始输出分布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/">A Hitchhiker's Guide to Speculative Decoding - PyTorch</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞投机解码是一项巧妙发明，零质量损失。有人注意到 Gemma 的令牌效率，其他人则讨论了将其整合到 llama.cpp 以及本地部署的硬件限制。

**标签**: `#inference speed`, `#multi-token prediction`, `#Gemma 4`, `#speculative decoding`, `#open source AI`

---

<a id="item-6"></a>
## [计算机使用比结构化 API 贵 45 倍](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/) ⭐️ 8.0/10

Reflex.dev 的一篇博文量化了基于视觉的计算机使用代理执行相同任务的成本是使用结构化 API 的 45 倍。 这种成本差异对 AI 代理的架构设计有重大影响，促使开发者尽可能优先使用结构化 API，而将基于视觉的方法作为最后手段。 该比较的前提是应用程序状态归所有者所有且结构化 API 可用；45 倍的差异包括了视觉处理的令牌和计算成本。

hackernews · palashawas · May 5, 16:34

**背景**: 计算机使用代理依赖视觉（例如屏幕截图）与用户界面交互，模拟人类行为，而结构化 API 允许直接以编程方式访问功能和数据。这使得基于视觉的方法因高令牌使用和延迟而成本更高。

**社区讨论**: 评论者指出，成本可能被对抗性利用（例如移动元素），对于状态归己的应用程序，代理应改用 CLI 或 MCP 接口。还有人认为，通过解耦后端，暴露结构化 API 并不构成一个庞大的工程。

**标签**: `#AI agents`, `#cost optimization`, `#API design`, `#computer vision`, `#engineering tradeoffs`

---

<a id="item-7"></a>
## [扎克伯格亲自授权 Meta 侵犯版权](https://variety.com/2026/digital/news/meta-ai-mark-zuckerberg-copyright-infringement-lawsuit-publishers-scott-turow-1236738383/) ⭐️ 8.0/10

一桩诉讼指控 Meta CEO 马克·扎克伯格亲自授权并鼓励公司使用受版权保护的书籍来训练其 AI 模型，包括 LLaMA 系列。 此案可能为 AI 公司在训练数据中的版权侵权责任树立先例，可能迫使 CEO 对数据来源决策承担个人责任。 该诉讼涉及包括作家 Scott Turow 在内的出版商，声称 Meta 使用数百万本盗版书籍构成侵权。此前 Anthropic 案以 15 亿美元和解，表明可能面临巨额赔偿。

hackernews · spankibalt · May 5, 18:04

**背景**: AI 训练需要大量文本数据，有些公司未经许可使用受版权保护的作品。合理使用是常见的辩护理由，但法院区分了训练（转换性使用）和盗版原始作品。Meta 的 LLaMA 模型在名为‘The Pile’的数据集上训练，其中包含受版权保护的书籍。该诉讼通过指控 CEO 级授权，加剧了法律风险。

**社区讨论**: 评论者观点不一：有人认为所有模型提供商都这样做，单独针对 Meta 不公平；另一些人指出技术执行（例如因忽略 robots.txt 而封锁 Meta 的 ASN）证实了这些指控。少数人认为 AI 训练是合理使用，但盗版规模可能改变这一点。

**标签**: `#AI`, `#copyright`, `#regulation`, `#meta`, `#lawsuit`

---

<a id="item-8"></a>
## [Transformers v5.8.0 新增 DeepSeek-V4 等多个模型](https://github.com/huggingface/transformers/releases/tag/v5.8.0) ⭐️ 7.0/10

Hugging Face Transformers v5.8.0 发布，新增了对 DeepSeek-V4 的官方支持，这是新一代混合专家（MoE）语言模型，具有混合局部和长程注意力、流形约束超连接以及静态专家哈希表。此外还引入了 Gemma 4 Assistant、Granite Speech Plus 和 Granite 4.1 Vision 等模型。 此次发布将最先进的 MoE 架构和高级注意力机制引入 Transformers 库，使研究人员和从业者能够尝试 DeepSeek-V4 的创新组件。新增的 Gemma 4 Assistant 用于推测性解码，Granite Vision 模型用于企业文档分析，扩展了库的功能。 DeepSeek-V4 用混合注意力取代了多头潜在注意力，用流形约束超连接替换了残差连接，并通过静态 token-id 到 expert-id 哈希表来引导早期 MoE 层。该实现涵盖了 Flash、Pro 和 Base 变体，它们在宽度、深度、专家数量和权重上有所不同。

github · vasqu · May 5, 16:52

**背景**: Transformers 是一个广泛使用的开源库，用于自然语言处理和生成式 AI，提供了数千个预训练模型。DeepSeek-V4 是 DeepSeek 的最新产品，以推动混合专家架构而闻名。流形约束超连接（mHC）是 DeepSeek 提出的一种技术，将超连接空间映射到流形以提高训练稳定性和性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/manifold-constrained-hyper-connections">Manifold-Constrained Hyper-Connections</a></li>

</ul>
</details>

**标签**: `#transformers`, `#deepseek`, `#moe`, `#model-release`

---

<a id="item-9"></a>
## [LangChain Core 1.3.3 补丁版本包含安全修复](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.3.3) ⭐️ 7.0/10

LangChain 发布了 langchain-core 1.3.3 版本，包含对 load() 函数的安全加固以防止不可信清单，以及多项错误修复。 此补丁对广泛使用的 LLM 框架 LangChain 至关重要，它防止了恶意序列化对象可能导致的代码执行，增强了所有用户的安全性。 该修复对 load() 函数进行了加固以防止不可信清单，其他变更包括验证 batch_size 以防止无限循环、使 deprecation 警告中的 'removal' 变为可选，以及更新 types-pyyaml 和 notebook 等依赖项。

github · github-actions[bot] · May 5, 19:02

**背景**: LangChain 是一个流行的开源框架，用于构建基于大语言模型（LLM）的应用。load() 函数用于从保存的清单中反序列化对象，如果未适当加固，可能被利用执行任意代码。此版本解决了这一漏洞。

**标签**: `#langchain`, `#security`, `#patch release`, `#python`, `#LLM`

---

<a id="item-10"></a>
## [LangChain Core 0.3.85 增强 load() 对不可信清单的安全性](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D0.3.85) ⭐️ 7.0/10

LangChain core 0.3.85 发布了，其中包含一项安全修复，增强了 load() 函数对不可信清单的防护。 此补丁对所有 LangChain 用户很重要，因为它可以防止来自恶意清单输入的潜在代码执行，提高了框架的安全性。 该修复专门解决了 load() 函数在处理清单时的漏洞，攻击者可能精心构造清单以执行任意代码。

github · github-actions[bot] · May 5, 20:43

**背景**: LangChain 是一个流行的用于构建基于大型语言模型的应用的框架。load() 函数用于从序列化表示中反序列化对象，而清单是描述如何重建对象的结构化数据。在此修复之前，不可信的清单可能导致代码执行漏洞。

**标签**: `#langchain`, `#security`, `#patch`, `#python`

---

<a id="item-11"></a>
## [Langchain-classic 1.0.6 修复安全漏洞](https://github.com/langchain-ai/langchain/releases/tag/langchain-classic%3D%3D1.0.6) ⭐️ 7.0/10

Langchain-classic v1.0.6 已发布，包含限制反序列化和强化清单加载防止不可信输入的安全修复。 这些修复解决了可能导致远程代码执行或数据损坏的关键漏洞，因此仍在依赖旧版 langchain-classic 库的用户应立即升级。 该补丁包含两个主要更改：限制 `langchain_classic.storage._lc_store` 中的反序列化，以及强化 `load()` 函数以防止不可信清单，同时更新了 jupyter-server 版本。

github · github-actions[bot] · May 5, 21:02

**背景**: Langchain-classic 是 LangChain 框架的旧版本，用于构建大型语言模型应用。反序列化漏洞出现在解析不可信数据时，可能允许攻击者执行任意代码，而清单加载问题可能通过精心构造的配置文件导致类似攻击。

**标签**: `#security`, `#langchain`, `#python`, `#patch`

---

<a id="item-12"></a>
## [五角大楼试图让《星条旗报》监察员噤声](https://www.stripes.com/opinion/2026-04-23/stripes-former-ombudsman-pentagon-trying-to-silence-21465037.html) ⭐️ 7.0/10

五角大楼据称试图让《星条旗报》监察员噤声，该监察员是该军事报纸编辑独立性的独立监督者。 这引发了关于新闻自由以及部队获取未经审查新闻能力的严重关切，因为监察员一职正是国会为防止审查而设立的。 撰写专栏的监察员声称五角大楼正试图让她噤声，但该文章是单一来源叙述，未经独立核实。

hackernews · petethomas · May 6, 03:24

**背景**: 《星条旗报》是为美国军方出版的报纸，国会要求其编辑独立，以确保部队获得真实新闻。监察员一职于 1991 年设立，负责监督该指令的遵守情况。过去军方官员试图压制不利新闻（如伊朗门事件）的做法，促使国会采取行动保护编辑独立性。

**社区讨论**: 评论者强调了《星条旗报》编辑独立性的历史背景，并指出其他监督官员也遭遇类似行动，例如特朗普解雇移民拘留监察员。一位评论者将美国的言论自由主张与欧洲标准进行了对比。

**标签**: `#press-freedom`, `#military`, `#government-accountability`, `#ombudsman`, `#censorship`

---

<a id="item-13"></a>
## [加州农民因德尔蒙破产销毁 42 万棵桃树](https://www.sfgate.com/centralcoast/article/usda-aid-california-farmers-22240694.php) ⭐️ 7.0/10

由于德尔蒙公司破产导致粘核桃失去罐头市场，加州农民将销毁 42 万棵桃树。这些树木正通过美国农业部资助的项目被移除，以帮助农民转向新作物。 这一事件凸显了依赖单一买家或加工厂的农业供应链的脆弱性。德尔蒙特罐头厂的停产迫使农民销毁有价值但用途单一的作物，扰乱了当地经济，并凸显了单一作物种植的风险。 粘核桃专为罐头培育，鲜食品质不佳，导致农民没有其他买家。美国农业部为砍伐和重植提供资金，但新作物需要多年才能投产。

hackernews · littlexsparkee · May 5, 18:13

**背景**: 粘核桃果肉紧实，在罐头加工中保持完好，因此是加工水果产品的理想选择。德尔蒙曾是加州粘核桃的最后几家大型罐头厂之一；其在 2025 年初破产后，这种作物的主要市场消失。许多农民数十年来根据与罐头厂的合同种植这些树木，现在失去了替代分销渠道。

**社区讨论**: 评论者指出，农民在运输农产品方面面临高成本和物流挑战，因此销毁成为实际选择。一些人将责任归咎于消费者对罐头桃子需求的减少，另一些人则批评单一作物体系，导致农民别无他用。少数人指出，剩下的罐头厂正在尽力收购，但整个行业已经大幅萎缩。

**标签**: `#agriculture`, `#supply chain`, `#bankruptcy`, `#monoculture`, `#California`

---