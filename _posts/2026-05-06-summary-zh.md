---
layout: default
title: "Horizon Summary: 2026-05-06 (ZH)"
date: 2026-05-06
lang: zh
---

> From 48 items, 13 important content pieces were selected

---

1. [SGLang v0.5.11：CUDA 13、推测解码 V2、新模型支持](#item-1) ⭐️ 8.0/10
2. [Hugging Face Transformers v5.8.0 新增对 DeepSeek-V4 的支持](#item-2) ⭐️ 8.0/10
3. [LangChain Core 0.3.85 加固 load() 以抵御不可信清单](#item-3) ⭐️ 8.0/10
4. [DNSSEC 配置错误导致.de 域名解析中断，现已恢复](#item-4) ⭐️ 8.0/10
5. [Gemma 4 使用多令牌预测草稿模型加速推理](#item-5) ⭐️ 8.0/10
6. [扎克伯格亲自授权 Meta 版权侵权](#item-6) ⭐️ 8.0/10
7. [Hugging Face 添加私有数据对抗 ASR 基准过拟合](#item-7) ⭐️ 8.0/10
8. [微软推出代理商业模式，苹果面临内存短缺](#item-8) ⭐️ 8.0/10
9. [llama.cpp b9045 新增 Granite Speech 支持](#item-9) ⭐️ 7.0/10
10. [美光开始出货 245TB 数据中心 SSD](#item-10) ⭐️ 7.0/10
11. [计算机使用比结构化 API 贵 45 倍](#item-11) ⭐️ 7.0/10
12. [博客作者担忧生物计算，专家评论驳斥炒作](#item-12) ⭐️ 7.0/10
13. [加州农民因德尔蒙破产将砍伐 42 万棵桃树](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.11：CUDA 13、推测解码 V2、新模型支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.11) ⭐️ 8.0/10

SGLang v0.5.11 将默认 CUDA 版本升级到 13.0，PyTorch 升级到 2.11，默认启用推测解码 V2（Speculative Decoding V2），并为预填充-解码（PD）分离架构新增了解码侧基数缓存（decode radix cache），同时支持了 Gemma 4、GLM-5.1、Qwen3.6 等新模型。 该版本显著提升了 LLM 推理服务的性能和成本效率，尤其是通过推测解码 V2 降低了 CPU 开销，以及改进了分离部署中的前缀缓存，这对大规模生产用户非常有利。 升级到 CUDA 13 可以使用更新的 GPU 内核，而新的解码侧基数缓存可在分离部署中恢复基数缓存的命中率并节省首令牌时间（TTFT）。LoRA 支持现已扩展到 DeepSeek-V3 和 Kimi-K2 模型。

github · Kangyan-Zhou · May 5, 21:28

**背景**: 预填充-解码（PD）分离架构将 LLM 推理的预填充阶段和解码阶段分配到不同的 GPU 上，以优化资源利用率。基数缓存（Radix Cache）以前缀树的形式存储 KV 缓存，支持跨请求的高效复用。推测解码（Speculative Decoding）通过使用草稿模型每步生成多个令牌，并并行验证它们，从而加速推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://bentoml.com/llm/inference-optimization/prefill-decode-disaggregation">Prefill-decode disaggregation | LLM Inference Handbook</a></li>
<li><a href="https://deepwiki.com/sgl-project/mini-sglang/7.3-radix-cache">Radix Cache | sgl-project/mini-sglang | DeepWiki</a></li>

</ul>
</details>

**标签**: `#open-source`, `#LLM-inference`, `#SGLang`, `#performance`, `#CUDA`

---

<a id="item-2"></a>
## [Hugging Face Transformers v5.8.0 新增对 DeepSeek-V4 的支持](https://github.com/huggingface/transformers/releases/tag/v5.8.0) ⭐️ 8.0/10

Hugging Face Transformers v5.8.0 新增了对 DeepSeek-V4 的支持，这是一个下一代 MoE 语言模型，采用混合局部和长程注意力、流形约束超连接以及静态 token-id 到 expert-id 哈希路由。该版本还包括对 Gemma 4 Assistant、GraniteSpeechPlus、Granite4Vision 和 EXAONE-4.5 模型的支持。 此版本带来了架构创新，可显著提高大型语言模型的效率和上下文处理能力，让从业者更轻松地实验和部署最先进的 MoE 模型。多个新模型家族的加入扩展了该库在多种 NLP 和多模态任务中的通用性。 DeepSeek-V4 将多头潜在注意力替换为混合注意力设计，将残差连接替换为流形约束超连接，并使用静态哈希表引导早期 MoE 层。实现涵盖 Flash、Pro 和 Base 变体，它们在规模、层数和权重上有所不同。

github · vasqu · May 5, 16:52

**背景**: 混合专家（MoE）是一种每 token 仅激活部分模型参数的技术，可提高效率。DeepSeek-V4 引入了多项创新：混合注意力结合局部和长程机制以高效处理长上下文；流形约束超连接（mHC）改善梯度流动；基于哈希的路由确定性地将 token 分配给专家，简化了训练稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.24880">[2512.24880] mHC: Manifold-Constrained Hyper-Connections</a></li>
<li><a href="https://apxml.com/courses/mixture-of-experts-advanced-implementation/chapter-2-advanced-routing-mechanisms/hash-based-routing">Hash-based Routing in MoE Models - apxml.com</a></li>

</ul>
</details>

**标签**: `#transformers`, `#deepseek-v4`, `#MoE`, `#language-model`, `#release`

---

<a id="item-3"></a>
## [LangChain Core 0.3.85 加固 load() 以抵御不可信清单](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D0.3.85) ⭐️ 8.0/10

LangChain 发布了 langchain-core 0.3.85 版本，修复了 load() 函数中的一个安全漏洞，以防止不可信清单的攻击。 此修复至关重要，因为 load() 在 LangChain 中广泛使用，该漏洞可能允许攻击者通过序列化注入窃取敏感密钥或进行提示注入。用户应立即更新。 该漏洞编号为 CVE-2025-68664，影响 langchain-core 的早期版本。此次更新加固了 load() 以防范不可信输入，并且最近的更改还默认阻止了 Jinja2 模板，并禁用了从环境自动加载密钥。

github · github-actions[bot] · May 5, 20:43

**背景**: LangChain 是一个流行的用于构建大语言模型（LLM）应用的框架。load() 函数将 JSON 字符串反序列化为 LangChain 对象，但如果传入不可信的 JSON，它可能会像 eval() 一样被利用。此次更新通过加固该函数来降低风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.langchain.com/oss/python/security-policy">Security policy - Docs by LangChain</a></li>
<li><a href="https://thehackernews.com/2025/12/critical-langchain-core-vulnerability.html">Critical LangChain Core Vulnerability Exposes Secrets via Serialization Injection</a></li>
<li><a href="https://secdim.com/blog/post/langchain-load-is-basically-eval-17661/">LangChain load() is basically eval()</a></li>

</ul>
</details>

**标签**: `#security`, `#langchain`, `#python`, `#vulnerability`

---

<a id="item-4"></a>
## [DNSSEC 配置错误导致.de 域名解析中断，现已恢复](https://status.denic.de/pages/incident/592577eab611ce1e0d00046f/69fa60ef9d12f5057a974f38) ⭐️ 8.0/10

德国.de 域名注册机构 DENIC 的 DNSSEC 配置错误导致所有.de 域名解析大面积失败，事件发生在当晚。DENIC 修复了无效的 RRSIG 记录，Cloudflare 等主要提供商重新启用 DNSSEC 验证后，问题得以解决。 这一事件凸显了 DNSSEC 在实际部署中的脆弱性——单个签名配置错误即可导致整个国家顶级域名的解析中断。它迫使主要 DNS 提供商暂时禁用 DNSSEC 验证，削弱了 DNSSEC 旨在提供的安全保障。 配置错误涉及 DENIC 发布了一个针对 NSEC3 记录的无效 RRSIG，该签名无法通过标签为 33834 的区域签名密钥（ZSK）的验证。Google Public DNS（8.8.8.8）等验证解析器返回 SERVFAIL，并附带扩展 DNS 错误代码表明签名格式错误，而非验证查询则正常。

hackernews · warpspin · May 5, 20:16

**背景**: DNSSEC（域名系统安全扩展）是一种为 DNS 响应添加加密认证的协议，可防止缓存投毒和欺骗攻击。DENIC 是管理.de 顶级域名的合作注册机构。当注册机构发布无效的 DNSSEC 签名时，强制进行 DNSSEC 验证的解析器将拒绝回答查询，导致该顶级域名下的所有域名解析失败。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DNSSEC">DNSSEC</a></li>
<li><a href="https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/">How Does DNSSEC Work? | Cloudflare</a></li>
<li><a href="https://en.wikipedia.org/wiki/DENIC">DENIC</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出根本原因是 NSEC3 记录的 RRSIG 配置错误，并提到 Cloudflare 临时在其 1.1.1.1 解析器上禁用 DNSSEC 验证作为缓解措施。有用户开玩笑称 DENIC 团队去聚会了，而另一些人则指出该帖中缺少常有的 DNSSEC 批评者发言。

**标签**: `#DNSSEC`, `#DNS`, `#outage`, `#.de`, `#TLD`

---

<a id="item-5"></a>
## [Gemma 4 使用多令牌预测草稿模型加速推理](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) ⭐️ 8.0/10

Google 为 Gemma 4 系列发布了多令牌预测（MTP）草稿模型，在不损失输出质量或推理逻辑的前提下，实现了高达 3 倍的推理加速。 这显著提高了大型语言模型的效率，降低了部署延迟和运营成本，对实时应用和 AI 的普及至关重要。 MTP 草稿模型采用专门的推测解码架构，较小的草稿模型并行提出多个令牌，目标 Gemma 4 模型通过单次前向传递验证它们。

hackernews · amrrs · May 5, 16:14

**背景**: 推测解码是一种推理优化技术，通过使用快速的草稿模型生成候选令牌，再由主模型并行验证，从而加速自回归语言模型。多令牌预测（MTP）进一步扩展了这一技术，同时预测多个令牌，从而减少顺序解码步骤。该技术匹配目标模型的输出分布，确保不损失质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://github.com/Xiaohao-Liu/Awesome-Multi-Token-Prediction">GitHub - Xiaohao-Liu/Awesome-Multi-Token-Prediction: A curated list of papers, tools, and resources on Multi-Token Prediction (MTP) and related techniques in Large Language Models (LLMs), Speech-Language Models (SLMs), and more. · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞推测解码是一项巧妙的发明，能在不损失质量的情况下加速推理。有用户指出，Gemma 模型每个输出使用的令牌比竞争对手更少，并且正在推进将 MTP 支持添加到 llama.cpp 中以支持 Qwen 等其他模型。用户还讨论了在基于代理的场景中，更小、更高效的模型的潜力。

**标签**: `#AI`, `#LLM`, `#inference optimization`, `#Google`, `#speculative decoding`

---

<a id="item-6"></a>
## [扎克伯格亲自授权 Meta 版权侵权](https://variety.com/2026/digital/news/meta-ai-mark-zuckerberg-copyright-infringement-lawsuit-publishers-scott-turow-1236738383/) ⭐️ 8.0/10

一项新诉讼指控 Meta CEO 马克·扎克伯格亲自授权并鼓励盗取数百万本受版权保护的图书，用于训练 Llama AI 模型，这使得他可能承担个人责任。 此案可能开创先例，让科技高管在 AI 训练中的版权侵权行为承担个人责任，从而重塑公司使用受版权保护数据的方式，并改变创作者与 AI 开发者之间的平衡。 Meta 据称使用了包含来自 Bibliotik 等来源的盗版图书的数据集“Books3”，无视合理使用论点。该诉讼紧随 Anthropic 案之后，后者裁定为训练而盗版作品构成侵权，并达成 15 亿美元和解。

hackernews · spankibalt · May 5, 18:04

**背景**: 像 Meta 的 Llama 这样的大型语言模型需要大量文本数据进行训练。版权持有者认为未经许可使用受保护作品是盗版，而科技公司通常主张合理使用。之前的裁决区分了对数据的变革性使用与非法获取数据的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/may/05/publishers-sue-meta-copyright-ai">Major publishers sue Meta for copyright infringement over AI ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama_(language_model)">Llama (language model) - Wikipedia</a></li>
<li><a href="https://www.usatoday.com/story/tech/news/2026/05/05/meta-ai-training-piracy-lawsuit/89947090007/">Meta faces new AI training lawsuit from publishers and authors</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：一些人支持扎克伯格的个人责任，指出与过去的反盗版运动形成讽刺对比；另一些人则认为 AI 训练属于变革性合理使用。技术用户报告 Meta 无视 robots.txt 进行激进抓取，加剧了不满情绪。

**标签**: `#copyright`, `#AI`, `#Meta`, `#Zuckerberg`, `#liability`

---

<a id="item-7"></a>
## [Hugging Face 添加私有数据对抗 ASR 基准过拟合](https://huggingface.co/blog/open-asr-leaderboard-private-data) ⭐️ 8.0/10

Hugging Face 宣布 Open ASR 排行榜将新增来自 Appen 和 DataoceanAI 的私有高质量英文 ASR 数据集，以防止基准测试造假。 此举直接解决了基准过拟合问题，确保模型排名反映真实性能而非测试集记忆，从而增强对排行榜的信任。 私有数据集涵盖多种英语口音（美式、英式、澳式、加拿大、印度）的脚本和对话语音，且对模型开发者隐藏，仅由 Hugging Face 进行评估。

rss · Hugging Face Blog · May 6, 00:00

**背景**: Open ASR 排行榜是一个比较自动语音识别模型的平台。基准过拟合是指模型在公开测试数据上训练或调优导致分数虚高。私有测试数据通过保持评估数据集不可见来防止这种情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/open-asr-leaderboard-private-data">Adding Benchmaxxer Repellant to the Open ASR Leaderboard</a></li>
<li><a href="https://app.daily.dev/posts/adding-benchmaxxer-repellant-to-the-open-asr-leaderboard-nmod3ukfj">Adding Benchmaxxer Repellant to the Open ASR Leaderboard</a></li>
<li><a href="https://www.appen.com/blog/hugging-face-open-llm-leaderboard">Appen Contributes Private Benchmark Data to the Open ASR ...</a></li>

</ul>
</details>

**标签**: `#ASR`, `#leaderboard`, `#benchmark`, `#evaluation`, `#open-source`

---

<a id="item-8"></a>
## [微软推出代理商业模式，苹果面临内存短缺](https://stratechery.com/2026/microsoft-earnings-apple-earnings/) ⭐️ 8.0/10

微软推出了新的代理商业模式，利用 AI 代理自动化工作流程和客户互动；而苹果则面临内存和芯片短缺，尽管其 Mac 系列受益于 AI 功能。 这标志着企业软件变现和交付方式的范式转变，从静态工具转向自主代理。苹果的供应限制凸显了 AI 硬件生态系统中日益严重的瓶颈，可能影响产品供应和定价。 微软的模型与麦肯锡和麻省理工斯隆管理学院描述的行业趋势一致，即 AI 代理充当客户的代理或自动化复杂任务。苹果的短缺是 2024 年至今全球内存供应短缺的一部分，AI 数据中心对 DRAM 和 HBM 的需求加剧了这一情况。

rss · Stratechery · May 6, 10:00

**背景**: 代理 AI 是指能够自主执行任务、做出决策并与用户或其他系统交互的 AI 系统，超越了简单的聊天界面。摩根大通和沃尔玛等公司正在探索使用 AI 代理处理客户服务、欺诈检测和规划。与此同时，半导体内存市场自 2024 年起出现短缺，原因是 AI 数据中心对高带宽内存（HBM）和 DRAM 的需求激增，这影响了苹果 Mac 等消费电子产品的供应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>
<li><a href="https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era">The agentic organization: A new operating model for AI | McKinsey</a></li>
<li><a href="https://en.wikipedia.org/wiki/2024–present_global_memory_supply_shortage">2024–present global memory supply shortage - Wikipedia</a></li>

</ul>
</details>

**标签**: `#business strategy`, `#AI`, `#supply chain`, `#tech earnings`

---

<a id="item-9"></a>
## [llama.cpp b9045 新增 Granite Speech 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9045) ⭐️ 7.0/10

llama.cpp 版本 b9045 增加了对 IBM Granite Speech 模型（ibm-granite/granite-4.0-1b-speech）的支持，通过 Conformer 编码器、QFormer 投影器和 GGUF 转换，实现了本地语音理解。 此次更新将先进的语音理解模型引入流行的开源 LLM 推理引擎，使开发者能够在消费级硬件上完全离线运行多模态语音 AI。 实现包括带有 Shaw 相对位置编码和 GLU 门控的 Conformer 编码器、具有窗口交叉注意力的 QFormer 投影器，以及使用 80 频段梅尔滤波器组和 2 倍帧堆叠的音频预处理。GGUF 转换器处理了批归一化折叠和 Conv1d 权重重塑。

github · github-actions[bot] · May 6, 13:33

**背景**: llama.cpp 是一个轻量级、高性能的 C++ LLM 推理实现，专为本地执行优化。GGUF 格式是一种二进制模型格式，旨在实现高效的加载和推理。Granite Speech 模型结合了用于音频特征提取的 Conformer 编码器和用于桥接音频与文本表示的 QFormer 投影器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2005.08100">[2005.08100] Conformer: Convolution-augmented Transformer for Speech Recognition</a></li>
<li><a href="https://huggingface.co/docs/hub/gguf">GGUF · Hugging Face</a></li>

</ul>
</details>

**标签**: `#llm`, `#opensource`, `#speech-recognition`, `#multimodal`, `#machine-learning`

---

<a id="item-10"></a>
## [美光开始出货 245TB 数据中心 SSD](https://investors.micron.com/news-releases/news-release-details/industry-leading-245tb-micron-6600-ion-data-center-ssd-now) ⭐️ 7.0/10

美光宣布开始出货业界首款 245TB SSD——Micron 6600 ION，专为数据中心设计，采用 QLC NAND 和 PCIe Gen5 接口。 该硬盘在 U.2 外形规格中提供了前所未有的存储密度，使数据中心能够大幅提高单台服务器的容量。然而，其相对较低的连续写入速度（2,700 MB/s）以及消费者 SSD 价格普遍上涨的趋势引发了批评。 Micron 6600 ION 提供高达 13,700 MB/s 的连续读取速度和 2,700 MB/s 的写入速度，采用 4 比特每单元（QLC）NAND。它采用 U.2 外形规格，通过 PCIe Gen5 x4 通道支持 NVMe 协议。

hackernews · neilfrndes · May 6, 03:37

**背景**: U.2 是一种 2.5 英寸 SSD 外形规格，专为企业级应用设计，相比 M.2 提供更好的散热管理，同时使用相同的 PCIe 接口。QLC NAND 每单元存储 4 比特，实现更高密度，但写入速度和耐用性通常低于 TLC 或 MLC。美光的 ION 系列针对需要海量存储容量的超大规模数据中心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.micron.com/products/storage/ssd/data-center-ssd/6600-ion">Micron 6600 ION NVMe SSD | 245TB & 122TB | Micron Technology Inc.</a></li>
<li><a href="https://en.wikipedia.org/wiki/U.2">U.2 - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/searchstorage/definition/U2-SSD-formerly-SFF-8639">What is U.2 SSD? | Definition from TechTarget</a></li>

</ul>
</details>

**社区讨论**: 社区评论对消费者 SSD 价格上涨以及消费市场缺乏创新表示失望。一些用户肯定了该硬盘的惊人容量，但批评其写入性能平庸；另一些用户则希望出现价格实惠的大容量便携式 SSD。

**标签**: `#storage`, `#SSD`, `#data center`, `#Micron`, `#hardware`

---

<a id="item-11"></a>
## [计算机使用比结构化 API 贵 45 倍](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/) ⭐️ 7.0/10

Reflex.dev 的一篇博客文章量化指出，使用基于视觉的计算机使用代理执行相同任务的成本是使用结构化 API 的 45 倍。 这种成本差异凸显了在内部或受控环境中使用基于视觉的代理的低效，促使开发人员出于成本和安全原因优先考虑 API 优先的方法。 这个 45 倍的数值考虑了使用大型多模态模型解释截图并模拟鼠标移动时的令牌和计算成本，与直接 API 调用相比而得出的。

hackernews · palashawas · May 5, 16:34

**背景**: 计算机使用代理通过视觉解析图形用户界面来自动化任务，类似于人类的交互方式。相比之下，结构化 API 提供对功能的直接程序化访问，绕过了用户界面，从而降低了延迟和成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use">Automate web and desktop apps with computer use (preview)</a></li>
<li><a href="https://arxiv.org/abs/2604.27151">Step-level Optimization for Efficient Computer-use Agents</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出了对敌方用户界面设计以阻止代理的启示，并建议后端解耦或无障碍 API 可以减少对计算机使用的需求。一些人认为计算机使用只是针对无法提供 API 的外部应用的最后手段。

**标签**: `#AI agents`, `#cost comparison`, `#structured APIs`, `#computer vision`, `#adversarial design`

---

<a id="item-12"></a>
## [博客作者担忧生物计算，专家评论驳斥炒作](https://kuber.studio/blog/Reflections/I%27m-Scared-About-Biological-Computing) ⭐️ 7.0/10

一位博主对生物计算表达了恐惧，引用了一个神经元培养物玩《毁灭战士》的演示，但社区评论指出该演示依赖于完整的 PyTorch 栈，并非纯粹的生物计算。 这一讨论对关于生物计算的夸大说法提供了关键的纠正，防止了无谓的恐惧，并澄清了实际的技术局限性。 《毁灭战士》演示的代码（github.com/SeanCole02/doom-neuron）显示其使用了包含 PyTorch 的标准机器学习流水线，生物神经元仅作为一个小部件，而非整个系统。

hackernews · kuberwastaken · May 5, 16:03

**背景**: 生物计算利用生物衍生分子（如 DNA 或蛋白质）或活细胞来执行计算。这是一个交叉学科领域，旨在利用生物系统处理信息，但实际实现通常整合了传统电子设备和软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Biological_computing">Biological computing</a></li>
<li><a href="https://www.polytechnique-insights.com/en/columns/science/biocomputing-the-promise-of-biological-computingbrains/">Biocomputing: the promise of biological computing - Polytechnique Insights</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈的怀疑，指出作者对《毁灭战士》演示的描述不准确，演示的 GitHub 代码显示其使用了常规的 ML 栈。一位评论者认为意识需要脑干和情感，因此一盘神经元不太可能具有意识。

**标签**: `#biological computing`, `#AI ethics`, `#neuroscience`, `#machine learning`, `#hype`

---

<a id="item-13"></a>
## [加州农民因德尔蒙破产将砍伐 42 万棵桃树](https://www.sfgate.com/centralcoast/article/usda-aid-california-farmers-22240694.php) ⭐️ 7.0/10

由于德尔蒙破产导致罐头厂关闭，加州农民将销毁 42 万棵桃树，因为无法为过剩的黏核桃找到其他销路或加工渠道。 此事件暴露了专门化农业供应链的脆弱性：单一买家倒闭便可能造成巨大浪费和农民的经济困难。 被销毁的桃树是专为制罐培育的黏核桃品种，不适合鲜食；加州仅剩的罐头厂无法吸收剩余产量，被迫销毁。

hackernews · littlexsparkee · May 5, 18:13

**背景**: 黏核桃的果肉紧贴果核，适合制罐。德尔蒙的罐头厂是加州最后几家大型加工厂之一，其破产使农民失去市场。砍伐树木可改种新作物，但对行业而言是长期损失。

**社区讨论**: 评论者指出大规模运输的物流困难，并强调黏核桃不适合鲜售。有人建议将木材用作烟熏燃料，但普遍认为鉴于经济性，销毁是唯一可行方案。

**标签**: `#agriculture`, `#supply chain`, `#bankruptcy`, `#food industry`

---