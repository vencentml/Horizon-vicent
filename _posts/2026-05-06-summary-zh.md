---
layout: default
title: "Horizon Summary: 2026-05-06 (ZH)"
date: 2026-05-06
lang: zh
---

> From 50 items, 12 important content pieces were selected

---

1. [SGLang v0.5.11 发布：CUDA 13、推测解码 V2、Radix 缓存](#item-1) ⭐️ 8.0/10
2. [Hugging Face Transformers v5.8.0 新增 DeepSeek-V4 等模型](#item-2) ⭐️ 8.0/10
3. [DNSSEC 故障影响所有.de 域名，已修复](#item-3) ⭐️ 8.0/10
4. [美光开始出货 245TB 6600 ION 固态硬盘，全球最高容量](#item-4) ⭐️ 8.0/10
5. [Gemma 4 多令牌预测草案器加速推理](#item-5) ⭐️ 8.0/10
6. [扎克伯格被指控授权 Meta AI 版权侵权](#item-6) ⭐️ 8.0/10
7. [GPT-5.x 在理论物理学中取得新成果](#item-7) ⭐️ 8.0/10
8. [LangChain 0.3.29 修复关键反序列化漏洞](#item-8) ⭐️ 7.0/10
9. [langchain-classic 1.0.6 修复反序列化安全漏洞](#item-9) ⭐️ 7.0/10
10. [计算机视觉操作比结构化 API 贵 45 倍](#item-10) ⭐️ 7.0/10
11. [Airbyte Agents 发布：AI 代理的统一上下文层](#item-11) ⭐️ 7.0/10
12. [五角大楼试图压制《星条旗报》监察员](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.11 发布：CUDA 13、推测解码 V2、Radix 缓存](https://github.com/sgl-project/sglang/releases/tag/v0.5.11) ⭐️ 8.0/10

SGLang v0.5.11 将默认 CUDA 升级至 13.0、PyTorch 升级至 2.11，默认启用带重叠调度的推测解码 V2，为预填充/解码分离引入了解码侧 radix 缓存，并新增了对 Gemma 4、Qwen3.6、Kimi-K2.6 等众多新模型的支持。 此次发布显著提升了 LLM 推理的性能和灵活性，降低了延迟，并使大型模型在分离式部署中更高效，这对扩展 AI 服务至关重要。 推测解码 V2 通过重叠调度隐藏 CPU 开销，而解码侧 radix 缓存可恢复分离式设置中的缓存命中率。新的 CUDA 13 和 PyTorch 2.11 带来了与新内核的兼容性，LoRA 支持现已扩展到 DeepSeek-V3 等大型基于 MLA 的 MoE 模型。

github · Kangyan-Zhou · May 5, 21:28

**背景**: LLM 推理分为两个阶段：预填充（处理提示）和解码（生成词元）。推测解码使用草稿模型加速生成，V2 版本通过将调度与 GPU 工作重叠来提高效率。预填充/解码分离将这两个阶段分布到不同机器以平衡负载，但可能破坏前缀缓存；新的 radix 缓存解决了这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.sglang.io/docs/advanced_features/speculative_decoding">Speculative Decoding - SGLang Documentation</a></li>
<li><a href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/SGlang_PD_Disagg_On_AMD_GPU.html">LLM distributed inference and PD disaggregation on AMD ...</a></li>

</ul>
</details>

**标签**: `#AI inference`, `#CUDA`, `#open-source`, `#LLM optimization`

---

<a id="item-2"></a>
## [Hugging Face Transformers v5.8.0 新增 DeepSeek-V4 等模型](https://github.com/huggingface/transformers/releases/tag/v5.8.0) ⭐️ 8.0/10

Hugging Face Transformers v5.8.0 新增了对 DeepSeek-V4 的支持，这是 DeepSeek 推出的新一代专家混合（MoE）语言模型，采用了混合局部与长程注意力机制、流形约束超连接（mHC）以及早期 MoE 层的静态 token-id 到 expert-id 哈希表。该版本还支持了 Gemma 4 Assistant、GraniteSpeechPlus、Granite4Vision 和 EXAONE-4.5 等模型。 DeepSeek-V4 引入了重要的架构创新，可能影响下一代高效大型语言模型的设计，特别是用更高效的替代方案取代了传统的残差连接和多头潜在注意力（MLA）。它被纳入 Transformers 库，使这些进展广泛惠及开发者和研究人员。 DeepSeek-V4 的各个变体（Flash、Pro、Base）共享相同的架构，但在宽度、深度、专家数量和权重上有所不同。该模型用混合局部与长程注意力设计取代了 DeepSeek-V3 中的多头潜在注意力（MLA），并用流形约束超连接（mHC）替代了残差连接。

github · vasqu · May 5, 16:52

**背景**: 专家混合（MoE）是一种使用多个专门的子模型（专家）并由门控机制激活的技术，可以在每标记计算成本较低的情况下提高模型容量。多头潜在注意力（MLA）在 DeepSeek-V2 中引入，是一种内存高效的注意力变体，将键值对压缩到潜在空间以减少 KV 缓存大小。流形约束超连接（mHC）是最近的一项进展，通过将残差流投影到流形上来扩展残差连接，以保持恒等映射性质并提高训练稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.24880">[2512.24880] mHC: Manifold-Constrained Hyper-Connections</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://sebastianraschka.com/llms-from-scratch/ch04/05_mla/">Multi-Head Latent Attention (MLA) | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**标签**: `#transformers`, `#deepseek-v4`, `#moe`, `#llm`, `#huggingface`

---

<a id="item-3"></a>
## [DNSSEC 故障影响所有.de 域名，已修复](https://status.denic.de/pages/incident/592577eab611ce1e0d00046f/69fa60ef9d12f5057a974f38) ⭐️ 8.0/10

一个格式错误的 DNSSEC 签名导致所有.de 域名的验证解析器失败，返回 SERVFAIL。DENIC 通过修复签名解决了问题，但 Cloudflare 暂时禁用了 1.1.1.1 上的 DNSSEC 验证作为临时方案。 此次事件凸显了 DNSSEC 在大规模部署中的脆弱性，一个无效签名就能使验证解析器后的整个顶级域名瘫痪。同时也表明，像 Cloudflare 这样的主要解析器在安全性和可用性之间面临抉择。 根本原因是一个针对 NSEC3 记录的 RRSIG 未能通过密钥标签 33834 的区签名密钥（ZSK）验证。DENIC 为.de 区域发布了这个格式错误的签名，导致所有验证解析器拒绝所有.de 查询。

hackernews · warpspin · May 5, 20:16

**背景**: DNSSEC（域名系统安全扩展）是一组协议，为 DNS 响应添加加密验证，确保数据的完整性和真实性。DENIC 是.de（德国国家顶级域名）的注册管理机构，负责管理其 DNS 基础设施。当 DNSSEC 签名无效时，验证解析器（如 1.1.1.1、8.8.8.8）会返回 SERVFAIL，以防止接受伪造数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DNSSEC">DNSSEC</a></li>
<li><a href="https://en.wikipedia.org/wiki/DENIC">DENIC</a></li>

</ul>
</details>

**社区讨论**: 社区成员迅速确认这是一个 DNSSEC 验证失败问题，而非域名服务器宕机。Cloudflare 决定在 1.1.1.1 上禁用验证引起了关注，一些人指出这是安全性与可用性之间的权衡。有评论幽默地提到 DENIC 团队当时正在聚会，还有人注意到这次讨论中缺少常见的 DNSSEC 批评。

**标签**: `#DNSSEC`, `#DNS`, `#incident`, `#infrastructure`, `#security`

---

<a id="item-4"></a>
## [美光开始出货 245TB 6600 ION 固态硬盘，全球最高容量](https://investors.micron.com/news-releases/news-release-details/industry-leading-245tb-micron-6600-ion-data-center-ssd-now) ⭐️ 8.0/10

美光宣布现已开始出货 245TB 的 Micron 6600 ION 固态硬盘，这是全球容量最高的商用数据中心固态硬盘，专为 AI 和超大规模工作负载设计。 这一里程碑显著提高了机架级存储密度，可能减少所需驱动器数量并降低能耗，美光声称其能效比机械硬盘高出 84 倍。 该固态硬盘采用美光第九代 G9 NAND 闪存，顺序读取速度达 13,700 MB/s，但顺序写入速度仅为 2,700 MB/s，这是一个显著的局限性，可能是由于高密度所致。

hackernews · neilfrndes · May 6, 03:37

**背景**: 数据中心固态硬盘通常要么侧重容量，要么侧重性能。Micron 6600 ION 是一款容量优化型驱动器，采用 PCIe 5.0 接口和 E3.L 外形规格。它面向读密集型工作负载，如 AI 训练数据摄取和云对象存储，这些场景对高写入速度要求不高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.micron.com/products/storage/ssd/data-center-ssd/6600-ion">Micron 6600 ION NVMe SSD | 245TB & 122TB</a></li>
<li><a href="https://hothardware.com/news/micron-ships-245tb-ssd-ai-data-center-storage-demands-surge">Micron Ships Massive 245TB SSD as AI Data Center Storage ...</a></li>
<li><a href="https://wccftech.com/micron-6600-ion-ssd-the-worlds-highest-storage-capacity-245-tb/">Micron’s New 245 TB SSD Crushes HDDs With 84x Better Energy ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了消费者对固态硬盘价格上涨的不满，并渴望获得价格合理的高容量固态硬盘。一些评论者也质疑 245TB 驱动器较低的写入性能，认为这可能是极端密度带来的权衡。

**标签**: `#data-center`, `#SSD`, `#micron`, `#storage`, `#hardware`

---

<a id="item-5"></a>
## [Gemma 4 多令牌预测草案器加速推理](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) ⭐️ 8.0/10

Google 为 Gemma 4 模型系列发布了多令牌预测（MTP）草案器，通过推测解码实现高达 3 倍的推理加速，且输出质量无损。 该技术显著降低了推理延迟和成本，使大型语言模型在实时应用和资源受限环境中部署更加实用。 MTP 草案器是一个轻量级模型，并行预测多个未来令牌；然后目标模型通过修改后的拒绝采样方案在单次前向传播中验证这些令牌，从而保持原始输出分布。

hackernews · amrrs · May 5, 16:14

**背景**: 推测解码是一种自回归语言模型的优化技术，其中一个小型草案模型提出候选令牌，由较大的目标模型并行验证。这种方法类似于 CPU 中的推测执行，可以在产生相同结果的同时将延迟降低两到三倍。传统解码每一步生成一个令牌，而 MTP 草案器通过一次预测多个令牌进一步提高了吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-05-06-google-boosts-gemma-4-performance-multi-token-prediction-drafters-deliver-3x-faster-inference">Google Gemma 4 MTP Drafters: 3x Faster AI Inference Speed | AIToolly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>

</ul>
</details>

**社区讨论**: 社区对推测解码的巧妙性和实际好处充满热情。用户指出，Gemma 模型本就使用更少令牌输出，MTP 进一步放大了速度优势。社区对 llama.cpp 增加 MTP 支持感兴趣，但仍有关于如何在有限 VRAM（如 24GB）中配置最佳模型的担忧。

**标签**: `#AI`, `#inference optimization`, `#speculative decoding`, `#Gemma 4`, `#multi-token prediction`

---

<a id="item-6"></a>
## [扎克伯格被指控授权 Meta AI 版权侵权](https://variety.com/2026/digital/news/meta-ai-mark-zuckerberg-copyright-infringement-lawsuit-publishers-scott-turow-1236738383/) ⭐️ 8.0/10

在一场诉讼中，Meta 首席执行官马克·扎克伯格被指控亲自授权并鼓励使用受版权保护的书籍来训练 Meta 的 Llama AI 模型。诉状由包括 Scott Turow 在内的作者提交，声称扎克伯格指示员工绕过版权保护。 对 CEO 的直接指控提高了 AI 公司的法律风险，可能在版权案件中确立高管的个人责任。如果被证实，这可能极大地改变 AI 公司处理受版权保护的训练数据的方式，并加强监管审查。 诉讼特别提到了 Meta 的 Llama 语言模型，这些模型使用的训练数据集据称包含来自非法来源的盗版书籍。如果数百万部作品被侵权，法定赔偿金可能高达数十亿美元，因为每次侵权最低赔偿 750 美元。

hackernews · spankibalt · May 5, 18:04

**背景**: 像 Meta 的 Llama 这样的大型语言模型需要大量的文本数据，这些数据通常来自互联网，包括受版权保护的材料。使用受版权保护的作品进行 AI 训练的合法性存在争议；早前的 Anthropic 案裁定，虽然训练可能是变革性的，但为此目的盗版作品仍然是侵权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama_(language_model)">Llama (language model) - Wikipedia</a></li>
<li><a href="https://www.reuters.com/legal/legalindustry/copyright-law-2025-courts-begin-draw-lines-around-ai-training-piracy-market-harm--pracin-2026-03-16/">Copyright Law in 2025: Courts begin to draw lines around AI training, piracy, and market harm | Reuters</a></li>

</ul>
</details>

**社区讨论**: 社区评论存在分歧：一些人希望追究扎克伯格的个人责任，引用 Anthropic 和解案作为先例，而另一些人则认为 AI 训练属于合理使用。一位用户报告称，由于 Meta 的 ASN 忽略 robots.txt 并大量请求访问其服务器，他们不得不将其屏蔽。

**标签**: `#AI`, `#copyright`, `#meta`, `#regulation`, `#legal`

---

<a id="item-7"></a>
## [GPT-5.x 在理论物理学中取得新成果](https://www.latent.space/p/lupsasca) ⭐️ 8.0/10

OpenAI 的 Alex Lupsasca 使用 GPT-5.x 在理论物理和量子引力领域生成了新颖的结果，展示了人工智能驱动科学发现的新范式。 这一突破表明，大型语言模型不仅可以辅助研究，还能积极贡献于前沿科研，可能加速基础物理学的发展，并重新定义人工智能在科学中的角色。 这项工作被称为“氛围物理学”，跟随了研究者用自然语言提供高层直觉而 AI 处理复杂计算的趋势，类似于 Anthropic 之前使用 Claude 进行的实验。

rss · Latent Space · May 5, 20:34

**背景**: “氛围物理学”一词受“氛围编程”启发，指研究者使用自然语言引导 AI 模型进行科学研究。GPT-5 于 2025 年 8 月发布，是 OpenAI 最新的大型语言模型，在多个领域拥有最先进的性能。该概念最早由 Anthropic 通过 Claude Opus 4.5 展示，一位教授在不直接操作文件的情况下监督 AI 完成了一个真实的物理计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5">GPT-5 - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/research/vibe-physics">Vibe physics: The AI grad student \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 该新闻未提供社区评论。

**标签**: `#AI`, `#physics`, `#quantum gravity`, `#GPT-5`, `#scientific discovery`

---

<a id="item-8"></a>
## [LangChain 0.3.29 修复关键反序列化漏洞](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D0.3.29) ⭐️ 7.0/10

LangChain 发布了 0.3.29 版本，该版本强化了 `langchain.storage._lc_store` 和 `load()` 函数中的反序列化功能，以抵御不受信任的清单（manifest）。 此补丁修复了一个关键的反序列化注入漏洞（CVE-2025-68664），攻击者可通过用户可控数据注入恶意对象来窃取机密信息，影响众多基于 LangChain 的应用。 漏洞源于 `dumps()` 和 `dumpd()` 未转义包含 'lc' 键的字典，使得精心构造的清单可以从受信任的命名空间实例化任意 `Serializable` 子类。0.3.29 版本限制了存储和加载函数中的反序列化。

github · github-actions[bot] · May 5, 21:02

**背景**: LangChain 是一个流行的用于构建大语言模型（LLM）应用的框架。它使用序列化来保存和加载提示词、链等对象。该漏洞（CVE-2025-68664）允许攻击者通过用户可控的字段（如元数据）注入恶意清单，在反序列化时实例化危险对象，并在启用 secrets_from_env 时读取环境变量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2025/12/critical-langchain-core-vulnerability.html">Critical LangChain Core Vulnerability Exposes Secrets via Serialization Injection</a></li>
<li><a href="https://cyata.ai/blog/langgrinch-langchain-core-cve-2025-68664/">All I Want for Christmas is Your Secrets: LangGrinch hits LangChain Core (CVE-2025-68664) - Cyata | The Control Plane for Agentic Identity</a></li>
<li><a href="https://github.com/advisories/GHSA-c67j-w6g6-q2cm">LangChain serialization injection vulnerability enables secret extraction in dumps/loads APIs · CVE-2025-68664 · GitHub Advisory Database · GitHub</a></li>

</ul>
</details>

**标签**: `#security`, `#langchain`, `#python`, `#deserialization`, `#vulnerability`

---

<a id="item-9"></a>
## [langchain-classic 1.0.6 修复反序列化安全漏洞](https://github.com/langchain-ai/langchain/releases/tag/langchain-classic%3D%3D1.0.6) ⭐️ 7.0/10

LangChain 发布了 langchain-classic 1.0.6，该补丁增强了库对反序列化攻击的处理，并在 `load()` 函数和存储组件中加强了不可信清单的处理。 此补丁对于任何使用 LangChain 序列化功能的应用程序至关重要，因为不安全的反序列化可能导致远程代码执行。强烈建议更新以防止潜在漏洞。 该修复限制了 `langchain_classic.storage._lc_store` 中的反序列化，并增强了 `load()` 对不可信清单的处理。这些更改减轻了与基于 pickle 的反序列化和 JSON 清单操作相关的风险。

github · github-actions[bot] · May 5, 21:02

**背景**: 当不可信数据被传递给诸如 Python 的 `pickle.loads()` 之类的反序列化函数时，就会产生反序列化漏洞，可能导致任意代码执行。LangChain 的序列化系统使用了此类机制，因此成为攻击目标。CVE-2025-68664 公告强调了这些漏洞的严重性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/advisories/GHSA-c67j-w6g6-q2cm">LangChain serialization injection vulnerability enables ...</a></li>
<li><a href="https://semgrep.dev/docs/learn/vulnerabilities/insecure-deserialization/python">Insecure Deserialization in Python | Semgrep</a></li>
<li><a href="https://docs.langchain.com/oss/python/security-policy">Security policy - Docs by LangChain</a></li>

</ul>
</details>

**标签**: `#security`, `#patch`, `#langchain`, `#deserialization`, `#fix`

---

<a id="item-10"></a>
## [计算机视觉操作比结构化 API 贵 45 倍](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/) ⭐️ 7.0/10

Reflex Dev 博客的一项新分析表明，使用计算机视觉（基于截图）进行自动化的成本是使用结构化 API（如 MCP 或 REST）的 45 倍，凸显了基于代理的 UI 交互中显著的成本低效。 这一发现对于决定使用计算机视觉还是基于 API 方法的 AI 代理开发者至关重要，尤其是在构建与内部应用交互的代理时。它表明，由于成本高昂，计算机视觉应作为最后手段，从而引导行业转向更高效的结构化接口。 成本比较假设计算机视觉涉及截图捕获、视觉模型推理和动作模拟，而结构化 API 提供直接、轻量的调用。45 倍的代价包括货币成本和延迟，分析侧重于代理已经拥有后端访问权限的场景。

hackernews · palashawas · May 5, 16:34

**背景**: AI 代理通常需要与软件界面交互。它们可以使用计算机视觉像人类一样查看和点击屏幕元素（计算机视觉操作），也可以利用暴露编程端点的结构化 API（例如 REST、MCP）。虽然计算机视觉适用于任何视觉界面，但计算成本高且速度慢，而 API 专为高效的机器间通信而设计。社区讨论指出，对抗性 UI 设计会进一步增加计算机视觉代理的难度和成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fuselabcreative.com/ui-design-for-ai-agents/">Agent UX: UI Design for AI Agents in 2026 - fuselabcreative.com</a></li>

</ul>
</details>

**社区讨论**: 社区评论提出了微妙的反对意见：一些人认为，在生成 API 工作流之前，计算机视觉仍可用于探索未知的 UI，而另一些人指出，对抗性 UI 设计（例如动态标签、隐藏元素）可能使计算机视觉更加困难。用户 merlindru 建议使用无障碍 API 作为折中方案，提供类似 DOM 的结构化接口，而无需完整的视觉推理成本。

**标签**: `#AI agents`, `#cost analysis`, `#automation`, `#API design`, `#engineering tradeoffs`

---

<a id="item-11"></a>
## [Airbyte Agents 发布：AI 代理的统一上下文层](https://news.ycombinator.com/item?id=48023496) ⭐️ 7.0/10

Airbyte 发布了 Airbyte Agents，这是一个上下文层，将来自多个运营系统（如 Slack、Salesforce、Linear）的数据索引到 Context Store 中，使 AI 代理能够跨源发现信息并采取行动。该公司还发布了一项基准测试，显示与供应商特定的 MCP 相比，token 消耗降低了 16%–90%。 这直接解决了企业工作流中 AI 代理的关键瓶颈：无法高效地访问和推理分散在多个孤立 API 中的数据。如果被采用，Airbyte Agents 可以显著减少代理错误、延迟和集成工作，使业务 AI 代理更加实用和可靠。 Context Store 由 Airbyte 现有的 350 多个复制连接器填充，为代理提供结构化发现，同时仍允许对上游系统进行读写访问。基准测试工具已在 GitHub 上开源，但公司承认作为产品构建者可能存在潜在偏见。

hackernews · mtricot · May 5, 15:03

**背景**: Model Context Protocol (MCP) 由 Anthropic 于 2024 年底推出，标准化了 AI 代理连接外部工具的方式。然而，大多数 MCP 服务器是薄 API 包装器，让代理处理分页、模式、跨系统实体匹配等低级细节。Airbyte Agents 基于 Airbyte 六年的数据连接器基础设施，提供预索引的上下文层，解决了代理在推理之前常常不知道要查询什么这一发现问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.airbyte.com/ai-agents">Airbyte Agents | Airbyte Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 前员工 swyx 等人的评论验证了该方法，认为 Airbyte Agents 可以作为 MCP 网关，类似于 Anthropic 内部使用 MCP 的方式。一些用户对 Airbyte 的客户支持表示不满，而另一些用户则赞赏开放的基准测试，并讨论了安全性和加密考虑。

**标签**: `#AI agents`, `#data integration`, `#MCP`, `#context layer`

---

<a id="item-12"></a>
## [五角大楼试图压制《星条旗报》监察员](https://www.stripes.com/opinion/2026-04-23/stripes-former-ombudsman-pentagon-trying-to-silence-21465037.html) ⭐️ 7.0/10

五角大楼正试图压制《星条旗报》的独立监察员，该职位是由国会于 1991 年设立，旨在保护编辑独立性。监察员已公开反对这种干预。 这代表了对国会授权的监督机制的直接挑战，威胁到军方独立报纸的编辑独立性。这可能为行政部门干预内部媒体和政府监督开创先例。 《星条旗报》监察员职位于 1991 年设立，此前国会对伊朗门事件期间试图压制负面新闻的行为表示担忧。监察员作为独立监督者，确保未经过滤的新闻传达给部队。

hackernews · petethomas · May 6, 03:24

**背景**: 《星条旗报》是一份面向海外美国军人的报纸，由国防部资助，但国会要求其保持编辑独立性。监察员是一个监督角色，旨在监控编辑独立性的遵守情况并向国会报告。现任监察员声称五角大楼试图让她沉默，这将破坏这种独立性。

**社区讨论**: 评论显示了对监察员的支持，并引用了历史类比：一位用户指出了监察员概念的瑞典起源，另一位强调了特朗普政府针对其他监察员办公室的类似压制行为。总体情绪是批评五角大楼的行动，支持监察员的立场。

**标签**: `#free speech`, `#military`, `#government oversight`, `#media independence`

---