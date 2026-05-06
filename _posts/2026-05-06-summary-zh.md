---
layout: default
title: "Horizon Summary: 2026-05-06 (ZH)"
date: 2026-05-06
lang: zh
---

> From 51 items, 16 important content pieces were selected

---

1. [Transformers v5.8.0 新增 DeepSeek-V4 支持](#item-1) ⭐️ 8.0/10
2. [langchain-core 1.3.3 发布安全修复，加固 load() 函数](#item-2) ⭐️ 8.0/10
3. [DENIC 的 DNSSEC 配置错误导致 .de 域名中断](#item-3) ⭐️ 8.0/10
4. [扎克伯格被指授权 Meta AI 版权侵权](#item-4) ⭐️ 8.0/10
5. [GPT-5.x 在理论物理学上取得新成果](#item-5) ⭐️ 8.0/10
6. [微软与苹果财报：代理式 AI 对阵供应瓶颈](#item-6) ⭐️ 8.0/10
7. [llama.cpp b9045 新增 IBM Granite 语音支持](#item-7) ⭐️ 7.0/10
8. [Ollama v0.23.1 新增 Gemma 4 MTP 推测解码支持](#item-8) ⭐️ 7.0/10
9. [Langchain 0.3.29 修复反序列化漏洞](#item-9) ⭐️ 7.0/10
10. [LangChain-core 0.3.85 强化 load() 函数应对不可信清单](#item-10) ⭐️ 7.0/10
11. [Cloudflare 允许 AI 代理自主购买域名并部署](#item-11) ⭐️ 7.0/10
12. [美光开始出货 245TB 数据中心 SSD，容量最大](#item-12) ⭐️ 7.0/10
13. [Gemma 4 使用多令牌预测草稿器加速推理](#item-13) ⭐️ 7.0/10
14. [计算机使用成本比结构化 API 高 45 倍](#item-14) ⭐️ 7.0/10
15. [五角大楼试图让《星条旗报》申诉专员噤声](#item-15) ⭐️ 7.0/10
16. [德尔蒙破产后加州农民将销毁 42 万棵桃树](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Transformers v5.8.0 新增 DeepSeek-V4 支持](https://github.com/huggingface/transformers/releases/tag/v5.8.0) ⭐️ 8.0/10

HuggingFace Transformers v5.8.0 新增对 DeepSeek-V4 的支持，这是一种下一代混合专家（MoE）语言模型，采用了混合局部与长程注意力、流形约束超连接（mHC）以及静态 token-id 到 expert-id 哈希表引导机制。 DeepSeek-V4 引入了相对于前代模型的架构创新，可能提升效率与性能，其集成到广泛使用的 transformers 库中使机器学习从业者能够轻松使用。 该版本涵盖了 DeepSeek-V4-Flash、DeepSeek-V4-Pro 及其 -Base 变体，这些变体共享相同架构但规模不同。值得注意的是，它将多头潜在注意力（MLA）替换为混合注意力设计，并将残差连接替换为 mHC。

github · vasqu · May 5, 16:52

**背景**: 混合专家（MoE）模型每次输入仅激活部分参数，从而在较低计算成本下实现更大的模型容量。混合注意力机制高效结合了局部与全局上下文。流形约束超连接（mHC）由 DeepSeek 在 2025 年的一篇论文中提出，通过将超连接空间投影到流形上以恢复恒等映射，从而改进残差连接，提升训练稳定性与性能。哈希引导机制利用静态哈希表初始化专家路由，减少了训练早期对学习路由的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.24880">[2512.24880] mHC: Manifold-Constrained Hyper-Connections</a></li>

</ul>
</details>

**标签**: `#huggingface`, `#transformers`, `#DeepSeek-V4`, `#MoE`, `#language-model`

---

<a id="item-2"></a>
## [langchain-core 1.3.3 发布安全修复，加固 load() 函数](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.3.3) ⭐️ 8.0/10

LangChain 发布了 langchain-core 1.3.3 版本，该补丁加固了 load() 函数，防止来自不可信清单的反序列化注入攻击。 此补丁修复了 CVE-2025-68664，这是一个严重的反序列化注入漏洞，可能允许攻击者提取机密或执行任意代码，影响许多 LangChain 组件和用户应用程序。 修复包括默认禁用 Jinja2 模板并将 'secrets_from_env' 设置为 False，以防止自动从环境变量加载机密。使用受影响版本的用户应立即升级。

github · github-actions[bot] · May 5, 19:02

**背景**: LangChain 是一个用于构建大型语言模型（LLM）应用程序的流行框架。load() 函数用于反序列化序列化对象，在此修复之前，如果攻击者控制了输入，可能会被利用，导致任意代码执行或机密泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2025/12/critical-langchain-core-vulnerability.html">Critical LangChain Core Vulnerability Exposes Secrets via Serialization Injection</a></li>
<li><a href="https://www.upwind.io/feed/cve-2025-68664-langchain-serialization-injection">CVE-2025-68664: LangChain Serialization Injection in dumps() and load()</a></li>
<li><a href="https://cyata.ai/blog/langgrinch-langchain-core-cve-2025-68664/">All I Want for Christmas is Your Secrets: LangGrinch hits LangChain Core (CVE-2025-68664) - Cyata | The Control Plane for Agentic Identity</a></li>

</ul>
</details>

**标签**: `#security`, `#langchain`, `#python`, `#release`

---

<a id="item-3"></a>
## [DENIC 的 DNSSEC 配置错误导致 .de 域名中断](https://status.denic.de/pages/incident/592577eab611ce1e0d00046f/69fa60ef9d12f5057a974f38) ⭐️ 8.0/10

2026 年 4 月 2 日，.de 域名注册管理机构 DENIC 发布了一个格式错误的 DNSSEC 签名（RRSIG），导致全球的验证解析器对所有 .de 域名返回 SERVFAIL。该事件在大约两小时后得到解决。 这一事件展示了 DNSSEC 在现实世界中的脆弱性——顶层域名注册管理机构的一个配置错误就可能使依赖 DNSSEC 验证的数百万域名解析失败。同时，它也凸显了运营方的应对方式，例如 Cloudflare 的 1.1.1.1 等主要解析器暂时禁用验证以减轻影响。 具体问题是一个带有 keytag 33834 的 NSEC3 记录的 RRSIG 格式错误，无法通过相应的区域签名密钥（ZSK）验证。强制 DNSSEC 验证的解析器拒绝回答，而非验证查询（例如使用 +cd 标志）则正常工作。

hackernews · warpspin · May 5, 20:16

**背景**: DNSSEC（域名系统安全扩展）通过为 DNS 记录添加加密签名来确保真实性和完整性。验证解析器会检查这些签名，如果验证失败则返回 SERVFAIL。DENIC 是德国国家顶级域名 .de 的注册管理机构。此事件是注册机构级别 DNSSEC 运营失败的一个显著例子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DNSSEC">DNSSEC</a></li>
<li><a href="https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/">How Does DNSSEC Work? | Cloudflare</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出该问题并非名称服务器宕机，而是 DNSSEC 配置错误，并对格式错误的 RRSIG 进行了详细分析。有人开玩笑说 DENIC 团队在聚会，也有人注意到 Cloudflare 已在其 1.1.1.1 解析器上禁用 DNSSEC 验证作为应对。

**标签**: `#DNSSEC`, `#DNS`, `#outage`, `#.de`, `#infrastructure`

---

<a id="item-4"></a>
## [扎克伯格被指授权 Meta AI 版权侵权](https://variety.com/2026/digital/news/meta-ai-mark-zuckerberg-copyright-infringement-lawsuit-publishers-scott-turow-1236738383/) ⭐️ 8.0/10

由出版商和作家斯科特·特罗（Scott Turow）提起的一项集体诉讼指控 Meta 首席执行官马克·扎克伯格（Mark Zuckerberg）亲自授权使用盗版受版权保护的书籍和文章来训练 Meta 的 Llama AI 模型。 此案可能为 AI 训练数据实践设定法律先例，可能使高管个人承担责任，并重塑 AI 公司获取数据的方式，从而影响整个行业。 诉讼称 Meta 使用了来自 Library Genesis 等盗版网站的数百万部作品，并忽视了 robots.txt 指令，扎克伯格涉嫌参与隐瞒受版权保护材料的使用。

hackernews · spankibalt · May 5, 18:04

**背景**: 像 Llama 这样的 AI 模型依赖于从互联网上抓取的大量文本语料库进行训练，这引发了版权问题。先前的案件（如 Anthropic 和解）认定盗版作品用于 AI 训练构成侵权，但转换性使用辩护仍存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://variety.com/2026/digital/news/meta-ai-mark-zuckerberg-copyright-infringement-lawsuit-publishers-scott-turow-1236738383/">Mark Zuckerberg ‘Personally Authorized and Actively Encouraged’ Meta’s Massive Copyright Infringement to Train AI Systems, Publishers and Scott Turow Allege in Lawsuit</a></li>
<li><a href="https://www.reuters.com/sustainability/boards-policy-regulation/major-publishers-sue-meta-copyright-infringement-over-ai-training-2026-05-05/">Major publishers sue Meta for copyright infringement over AI training | Reuters</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama_(language_model)">Llama (language model) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一些人认为这可能导致 Meta 承担责任，而另一些人则辩称许多 AI 公司都这样做。有人指出 Meta 在实践中无视 robots.txt，少数人则为 AI 训练辩解称是合理使用。

**标签**: `#AI`, `#copyright`, `#Meta`, `#lawsuit`, `#regulation`

---

<a id="item-5"></a>
## [GPT-5.x 在理论物理学上取得新成果](https://www.latent.space/p/lupsasca) ⭐️ 8.0/10

OpenAI 研究员 Alex Lupsasca 在 Latent Space 播客中详细报告，GPT-5.x 成功推导出了理论物理学和量子引力领域的新结果。 这标志着 AI 驱动科学发现的一个重要里程碑，表明大型语言模型能够为基础物理学贡献原创见解，可能加速量子引力及相关领域的研究。 GPT-5.x 于 2025 年 8 月发布，是 OpenAI 最先进的多模态模型，在编码、数学和科学方面均达到顶尖性能。可用内容中未完全披露具体的物理学成果及其验证方法。

rss · Latent Space · May 5, 20:34

**背景**: “Vibe physics”（物理氛围）一词将“vibe coding”（编程氛围）的概念扩展到科学研究中，即 AI 辅助或自主完成理论工作。GPT-5 是 OpenAI 的第五代大型语言模型，继 GPT-4 之后，可通过 ChatGPT 和 Microsoft Copilot 公开访问。此前 Anthropic 的“vibe physics”文章等实验已探索了 AI 在理论物理学中的作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5">GPT-5</a></li>
<li><a href="https://www.anthropic.com/research/vibe-physics">Vibe physics: The AI grad student</a></li>

</ul>
</details>

**标签**: `#AI`, `#theoretical physics`, `#quantum gravity`, `#OpenAI`, `#scientific discovery`

---

<a id="item-6"></a>
## [微软与苹果财报：代理式 AI 对阵供应瓶颈](https://stratechery.com/2026/microsoft-earnings-apple-earnings/) ⭐️ 8.0/10

微软在财报中公布了新的代理式商业模式，而苹果则报告了内存和芯片短缺，尽管 AI 驱动的 Mac 带来好处。 这一转变标志着微软战略性地向自主 AI 代理作为核心收入驱动因素靠拢，而苹果的供应短缺可能阻碍其 AI 硬件雄心并影响市场竞争。 微软的代理式商业模式可能按任务或结果收费，而非按用户；苹果的短缺据称源于 AI 对高内存带宽的需求以及受限的芯片制造产能。

rss · Stratechery · May 6, 10:00

**背景**: 代理式商业模式是指 AI 代理代表用户或企业自主执行多步骤任务的变现策略，通常与使用量或结果挂钩。摩根大通和沃尔玛等公司正在探索用此类代理来自动化复杂流程。苹果越来越多地依赖自研芯片（如 M 系列）来处理 AI 工作负载，但对先进内存和制造能力的高需求造成了供应瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>
<li><a href="https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era">The agentic organization: A new operating model for AI | McKinsey</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/how-digital-business-models-are-evolving-age-agentic-ai">How digital business models are evolving in the age of agentic AI | MIT Sloan</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Apple`, `#AI`, `#business strategy`, `#supply chain`

---

<a id="item-7"></a>
## [llama.cpp b9045 新增 IBM Granite 语音支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9045) ⭐️ 7.0/10

llama.cpp b9045 版本引入了对 IBM Granite 4.0-1b 语音模型的支持，集成了带有 Shaw 相对位置编码的 Conformer 编码器和 QFormer 投影器，用于语音转文本推理。 这将 llama.cpp 的能力扩展到语音 AI，使其成为更通用的多模态推理工具，并允许开发者在边缘设备上本地运行语音模型。 该实现包括 GLU 门控、折叠批归一化、SSM 深度可分离卷积以及 QFormer 的窗口式交叉注意力。音频预处理使用对数梅尔频谱图并进行 2 倍帧堆叠，转换器处理批归一化折叠和 Conv1d 权重重塑。

github · github-actions[bot] · May 6, 13:33

**背景**: llama.cpp 是一个用于大语言模型的开源 C/C++ 推理引擎，针对本地和边缘部署进行了优化。IBM Granite 4.0-1b 语音模型是一个将语音转换为文本的多模态模型。Conformer 是一种用于语音识别的卷积增强 Transformer 架构，而 QFormer 使用可学习的查询令牌将编码器特征压缩到语言模型的嵌入空间中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sooftware/conformer">GitHub - sooftware/conformer: [Unofficial] PyTorch implementation of "Conformer: Convolution-augmented Transformer for Speech Recognition" (INTERSPEECH 2020) · GitHub</a></li>
<li><a href="https://medium.com/@duongtr/askmore-building-a-vqa-model-from-scratch-in-pytorch-part-3-q-former-projector-7f1c8fd6b81c">Askmore: Building a VQA Model from Scratch in PyTorch — Part 3: Q-Former Projector | by Duong Tran | Medium</a></li>
<li><a href="https://arxiv.org/pdf/1803.02155">Self-Attention with Relative Position Representations Peter Shaw Google</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#speech recognition`, `#model inference`, `#IBM`, `#open-source`

---

<a id="item-8"></a>
## [Ollama v0.23.1 新增 Gemma 4 MTP 推测解码支持](https://github.com/ollama/ollama/releases/tag/v0.23.1) ⭐️ 7.0/10

Ollama 发布了 v0.23.1 版本，为 Mac 上的 Gemma 4 模型系列引入了多标记预测（MTP）推测解码功能，在使用 Gemma 4 31B 模型进行编码任务时实现了超过 2 倍的加速效果。 此次更新显著提升了 Mac 用户在本地运行大语言模型的推理速度，使 Gemma 4 等工具在实时编码辅助中更加实用。同时也展示了推测解码技术正在被主流 LLM 工具广泛采用。 该功能仅通过 MLX 运行器在 Mac 上可用，需使用特定模型 'gemma4:31b-coding-mtp-bf16'。其他变更包括 MLX 的线程修复以及 Go 版本升级至 1.26。

github · github-actions[bot] · May 5, 17:13

**背景**: 推测解码是一种推理优化技术，通过一个小型草稿模型生成多个候选标记，再由大型目标模型并行验证，从而在保持输出质量的同时降低延迟。多标记预测（MTP）是其中一种变体，草稿模型一次预测多个标记。MLX 是 Apple 针对 Apple Silicon 优化的机器学习框架，可在 Mac 上实现高效的模型推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>

</ul>
</details>

**标签**: `#ollama`, `#gemma-4`, `#speculative-decoding`, `#macos`, `#performance`

---

<a id="item-9"></a>
## [Langchain 0.3.29 修复反序列化漏洞](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D0.3.29) ⭐️ 7.0/10

Langchain 发布了 0.3.29 版本，其中包括安全修复：限制 `langchain.storage._lc_store` 中的反序列化，并增强了 `load()` 函数对不可信清单的防护。 此更新对于广泛使用的 AI 库用户至关重要，因为它缓解了反序列化漏洞的潜在利用，攻击者可能通过精心构造的输入提取机密或执行任意代码。 这些修复解决了 CVE-2025-68664 相关的问题，其中 `dumps()` 和 `dumpd()` 函数未能正确转义包含保留键 'lc' 的用户控制字典，导致序列化数据被解释为受信任的 LangChain 对象。

github · github-actions[bot] · May 5, 21:02

**背景**: LangChain 是一个用于构建基于大型语言模型 (LLM) 的应用程序的流行框架。反序列化漏洞发生在解析并执行不可信数据时，可能导致远程代码执行或数据泄露。最近的 CVE-2025-68664 揭示了 LangChain 序列化处理中的缺陷，从而促使了此补丁版本的发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/advisories/GHSA-c67j-w6g6-q2cm">LangChain serialization injection vulnerability enables secret extraction in dumps/loads APIs · CVE-2025-68664 · GitHub Advisory Database · GitHub</a></li>
<li><a href="https://cyata.ai/blog/langgrinch-langchain-core-cve-2025-68664/">All I Want for Christmas is Your Secrets: LangGrinch hits LangChain Core (CVE-2025-68664) - Cyata | The Control Plane for Agentic Identity</a></li>

</ul>
</details>

**标签**: `#langchain`, `#security`, `#patch`, `#python`, `#AI`

---

<a id="item-10"></a>
## [LangChain-core 0.3.85 强化 load() 函数应对不可信清单](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D0.3.85) ⭐️ 7.0/10

LangChain 于 2025 年 12 月 27 日发布了 langchain-core 0.3.85 版本，该版本包含对 load() 函数的安全强化修复，以防范不可信清单。 此修复解决了 CVE-2025-68664 这一严重的序列化注入漏洞，该漏洞可允许攻击者通过受大语言模型影响的元数据泄露机密或实例化不安全对象，影响所有反序列化不可信数据的 LangChain 用户。 该漏洞被命名为 'LangGrinch'，因对包含 'lc' 键的字典转义不当而影响 dumps() 和 load() 函数；0.3.85 补丁专门强化了 load() 函数以应对不可信清单，建议用户立即升级。

github · github-actions[bot] · May 5, 20:43

**背景**: LangChain 是一个流行的开源框架，用于构建基于大语言模型（LLM）的应用。它提供序列化函数（dumps、load）来保存和恢复链、代理等对象。漏洞源于 dumps() 未转义包含 'lc' 键的元数据，导致恶意清单在反序列化时可执行任意代码或泄露机密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyata.ai/blog/langgrinch-langchain-core-cve-2025-68664/">All I Want for Christmas is Your Secrets: LangGrinch hits LangChain Core (CVE-2025-68664) - Cyata | The Control Plane for Agentic Identity</a></li>
<li><a href="https://www.upwind.io/feed/cve-2025-68664-langchain-serialization-injection">CVE-2025-68664: LangChain Serialization Injection in dumps() and load()</a></li>

</ul>
</details>

**标签**: `#security`, `#langchain`, `#open-source`, `#python`, `#fix`

---

<a id="item-11"></a>
## [Cloudflare 允许 AI 代理自主购买域名并部署](https://blog.cloudflare.com/agents-stripe-projects/) ⭐️ 7.0/10

Cloudflare 宣布，AI 代理现在可以通过与 Stripe Atlas 的集成，自主创建账户、购买域名并部署服务。 这一能力可能极大简化基础设施自动化，但也引发了关于欺诈的重大担忧，例如域名抢注和网络钓鱼攻击。 该功能很可能利用了目前处于测试阶段的 Cloudflare 注册商 API，并通过 Stripe Atlas 处理支付。博文缺乏具体示例，表明该实现仍处于实验阶段。

hackernews · rolph · May 6, 03:10

**背景**: 自主 AI 代理是能够独立执行复杂任务而无需持续人工监督的系统。Cloudflare 最近推出了其注册商 API 的测试版，允许通过编程方式注册域名。结合这些技术，代理可以自主配置完整的网络存在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Autonomous_agent">Autonomous agent - Wikipedia</a></li>
<li><a href="https://blog.cloudflare.com/registrar-api-beta/">Register domains wherever you build: Cloudflare Registrar API now in beta</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍持怀疑态度：有人质疑实际用例，也有人警告称域名抢注和复杂欺诈会增加。一位用户提到自己曾因涉嫌欺诈被永久封禁，讽刺 Cloudflare 现在却允许自动创建账户。

**标签**: `#AI agents`, `#cloudflare`, `#domain registration`, `#automation`, `#fraud`

---

<a id="item-12"></a>
## [美光开始出货 245TB 数据中心 SSD，容量最大](https://investors.micron.com/news-releases/news-release-details/industry-leading-245tb-micron-6600-ion-data-center-ssd-now) ⭐️ 7.0/10

这一里程碑提升了数据中心的存储密度上限，有望减少大规模存储的物理占用和功耗，但同时也凸显了容量与写入性能之间的权衡。 该 245TB 硬盘采用 QLC NAND，拥有 276 层 6 平面架构，顺序读取达 13,700 MB/s，但顺序写入仅 2,700 MB/s，提供 U.2 和 E3.L 两种外形规格。

hackernews · neilfrndes · May 6, 03:37

**背景**: QLC NAND 每个单元存储 4 位数据，相比 TLC 或 MLC 实现了更高密度，但写入速度和耐用性较低。数据中心 SSD 通常优先考虑顺序带宽和能效；美光 6600 ION 专为 AI 数据湖和分析等读取密集型工作负载设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.micron.com/products/storage/ssd/data-center-ssd/6600-ion">Micron 6600 ION NVMe SSD | 245TB & 122TB | Micron Technology Inc.</a></li>
<li><a href="https://www.micron.com/about/blog/storage/ssd/micron-6600-ion-redefining-data-center-storage">Micron 6600 ION 245TB is now shipping — redefining data center storage at scale | Micron Technology Inc.</a></li>
<li><a href="https://www.blocksandfiles.com/flash/2026/05/05/microns-new-ssd-replaces-disk-for-fast-access-storage/5219265">Micron's new SSD replaces disk for fast access storage</a></li>

</ul>
</details>

**社区讨论**: 社区评论对消费级 SSD 价格上涨和 245TB 硬盘的慢写入速度（顺序写入 2,700 MB/s）表示失望。一些人提到了外形规格和散热挑战，另一些则将其与 KIOXIA 类似容量的 SSD 进行了比较。

**标签**: `#SSD`, `#Data Center`, `#Storage`, `#Micron`, `#Hardware`

---

<a id="item-13"></a>
## [Gemma 4 使用多令牌预测草稿器加速推理](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) ⭐️ 7.0/10

Google 发布了 Gemma 4 系列的多令牌预测（MTP）草稿器，可在不降低质量的情况下实现高达 3 倍的每秒令牌数推理速度提升。 该技术显著降低了开源大语言模型的延迟，使 Gemma 4 更适用于实时应用和本地部署，尤其是在显存有限的消费级 GPU 上。 草稿器采用推测解码架构：小型草稿模型生成候选令牌，主 Gemma 4 模型并行验证。该方法正在被集成到 llama.cpp 中，Qwen 模型的支持已添加。

hackernews · amrrs · May 5, 16:14

**背景**: 推测解码是一种推理时优化技术，使用小型草稿模型每步生成多个令牌，再由大型模型验证，以确保输出分布一致。它与 CPU 的推测执行类似。Medusa 和 EAGLE 是其他方法，但 MTP 内置于模型中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-05-06-google-boosts-gemma-4-performance-multi-token-prediction-drafters-deliver-3x-faster-inference">Google Gemma 4 MTP Drafters: 3x Faster AI Inference Speed | AIToolly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞推测解码的巧妙，并指出 Gemma 每次输出使用的令牌更少。他们讨论了集成到 llama.cpp 以及本地部署的显存限制，部分人注意到本地模型速度和质量的快速提升。

**标签**: `#speculative decoding`, `#Gemma 4`, `#inference acceleration`, `#multi-token prediction`, `#open-source LLMs`

---

<a id="item-14"></a>
## [计算机使用成本比结构化 API 高 45 倍](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/) ⭐️ 7.0/10

Reflex 博客量化了使用基于计算机视觉的 AI 代理（计算机使用）执行相同任务时，成本是使用结构化 API 的 45 倍。 这种巨大的成本差异迫使工程团队重新考虑何时使用计算机使用代理，尤其是对于拥有结构化 API 的内部应用。它提供了具体数据来指导技术选择和资源分配。 成本差异源于架构差异：计算机使用代理处理大型视觉输入（如截图）并生成操作，而结构化 API 处理高效的基于文本的事务。测试显示，使用视觉的计算机使用成本是 API 调用的 45 倍。

hackernews · palashawas · May 5, 16:34

**背景**: 计算机使用代理是像人类一样与图形用户界面交互的 AI 系统，利用视觉观察并执行操作。相比之下，结构化 API 是允许系统间直接数据交换的程序化接口。Reflex 文章基于 OpenAI 的 CUA 等计算机使用代理概念，提供了实际的成本比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/">Computer use is 45x More Expensive Than Structured APIs</a></li>
<li><a href="https://openai.com/index/computer-using-agent/">Computer-Using Agent | OpenAI</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论包括讽刺性地建议让 UI 对代理不友好，一位开发者分享使用 macOS 无障碍 API 创建代理工作流的解决方案，以及普遍认为对于自有数据库的计算机使用是最后手段。总体情绪认为成本差异在意料之中，应避免在已有 API 的情况下使用计算机使用。

**标签**: `#AI agents`, `#computer use`, `#structured APIs`, `#cost comparison`, `#software engineering`

---

<a id="item-15"></a>
## [五角大楼试图让《星条旗报》申诉专员噤声](https://www.stripes.com/opinion/2026-04-23/stripes-former-ombudsman-pentagon-trying-to-silence-21465037.html) ⭐️ 7.0/10

《星条旗报》（Stars and Stripes）前申诉专员报告称，五角大楼正试图让她噤声。该报是国会授权的面向美军人员的独立新闻机构。 此举威胁到军方唯一独立报纸的编辑自主权，可能损害新闻自由以及军人获取未经过滤新闻的权利。 国会在 1991 年设立了申诉专员职位，以监督编辑独立性，此前曾有压制不利新闻的尝试。当前的冲突凸显了一种审查模式。

hackernews · petethomas · May 6, 03:24

**背景**: 《星条旗报》是一份美国军方报纸，自 20 世纪 80 年代末以来一直根据国会授权保持编辑独立性。设立申诉专员角色是为了确保读者获得真实、非宣传性的报道。五角大楼所谓的噤声努力违背了这一安排。

**社区讨论**: 评论者表达了对申诉专员的支持，有人称赞她敢于发声。其他人则进行历史对比，指出国会旨在防止压制不利新闻，并将此情况与其他申诉专员被解职的事件相提并论。

**标签**: `#press freedom`, `#Pentagon`, `#censorship`, `#military news`, `#ombudsman`

---

<a id="item-16"></a>
## [德尔蒙破产后加州农民将销毁 42 万棵桃树](https://www.sfgate.com/centralcoast/article/usda-aid-california-farmers-22240694.php) ⭐️ 7.0/10

德尔蒙公司破产导致用于罐头的粘核桃主要市场消失，加州农民被迫销毁 42 万棵桃树。 这揭示了农业中单一作物和单一买家依赖的脆弱性，将影响中央海岸的经济和几代农村生计。 粘核桃是专门为罐头培育的，不适合鲜食；加州仅剩的一家罐头厂只能采购其能加工的数量。

hackernews · littlexsparkee · May 5, 18:13

**背景**: 粘核桃的果肉紧贴果核，适合罐装但鲜食口感不佳。这是一种依赖加工设施的特种作物，德尔蒙的关闭使农民失去了销售渠道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Clingstone_peach">Clingstone peach</a></li>
<li><a href="https://fruitguys.com/blog/cling-peaches/">Cling Peaches vs. Freestone Peaches: What’s the Difference? - The FruitGuys</a></li>

</ul>
</details>

**社区讨论**: 评论者强调运输如此大量水果的物流困难，指出即使免费赠送也无法运走，因为运输和包装成本高昂。有人指责过度依赖工业罐头产业，建议多元化种植。

**标签**: `#agriculture`, `#supply chain`, `#monoculture`, `#bankruptcy`

---