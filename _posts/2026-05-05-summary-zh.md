---
layout: default
title: "Horizon Summary: 2026-05-05 (ZH)"
date: 2026-05-05
lang: zh
---

> From 47 items, 15 important content pieces were selected

---

1. [美国医保网站通过像素分享种族和公民数据给广告公司](#item-1) ⭐️ 9.0/10
2. [国防部承包商初创公司多租户授权漏洞导致数据泄露](#item-2) ⭐️ 8.0/10
3. [Redis 创始人 Antirez 讲述历时四个月的 LLM 辅助数组开发经历](#item-3) ⭐️ 8.0/10
4. [GameStop 提出 555 亿美元收购 eBay](#item-4) ⭐️ 8.0/10
5. [vLLM v0.20.1 补丁专注于 DeepSeek V4 稳定性](#item-5) ⭐️ 7.0/10
6. [LangGraph v1.2 Alpha 引入 DeltaChannel 与精细化节点控制](#item-6) ⭐️ 7.0/10
7. [Bun 从 Zig 移植到 Rust](#item-7) ⭐️ 7.0/10
8. [OpenAI 使用 WebRTC 实现低延迟语音 AI](#item-8) ⭐️ 7.0/10
9. [就业减缓认知衰退：因果证据](#item-9) ⭐️ 7.0/10
10. [Microsoft Edge 在内存中明文存储密码](#item-10) ⭐️ 7.0/10
11. [对 Bun 被 Anthropic 收购后的担忧](#item-11) ⭐️ 7.0/10
12. [2026 年第一季度欧洲热泵销量猛增 17%](#item-12) ⭐️ 7.0/10
13. [牛顿引力通过宇宙尺度最大检验](#item-13) ⭐️ 7.0/10
14. [假冒 Mac 版 Notepad++ 引发商标警告](#item-14) ⭐️ 7.0/10
15. [Y Combinator 持有 OpenAI 0.6%股份，价值 50 亿美元](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [美国医保网站通过像素分享种族和公民数据给广告公司](https://techcrunch.com/2026/05/04/us-healthcare-marketplaces-shared-citizenship-and-race-data-with-ad-tech-giants/) ⭐️ 9.0/10

一项调查揭露，美国医保市场网站通过跟踪像素将包括公民身份和种族信息在内的敏感用户数据传输给 Meta 和 TikTok 等广告技术公司。 这种信任的破坏损害了患者隐私，并可能引发监管行动，因为医疗数据受 HIPAA 等法律保护，用户在寻求保险时期望保密。 数据共享通过 Meta Pixel 和 TikTok 的等效工具发生，这些工具嵌入用于营销重定向，但自动将个人数据暴露给这些第三方。

hackernews · ZeidJ · May 4, 17:16

**背景**: 跟踪像素是嵌入网站中的微小、通常不可见的代码片段，用于监控用户行为并向第三方传输数据。它们常用于广告分析和重定向。然而，当部署在医保市场等敏感网站时，它们可能未经用户明确同意泄露个人可识别信息（PII）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tracking_pixels">Tracking pixels</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了愤怒和不信任，一位用户在科罗拉多市场输入数据后感到被侵犯。另一人指出分享是为了重定向，但批评 Meta 和字节跳动对数据的使用。许多人呼吁将发送和接收数据都定为非法。

**标签**: `#privacy`, `#healthcare`, `#data-breach`, `#ad-tech`, `#regulation`

---

<a id="item-2"></a>
## [国防部承包商初创公司多租户授权漏洞导致数据泄露](https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup) ⭐️ 8.0/10

一名安全研究人员在一家国防部支持的初创公司中发现了一个严重的多租户授权漏洞，零租户隔离使得任何低权限用户都能访问其他组织的记录，包括敏感的军事训练数据。 该漏洞凸显了初创公司中常见的安全缺陷，即使是通过合规认证的公司也不例外，对敏感数据和更广泛的国防供应链构成严重风险。 该漏洞涉及无意义的组织范围划分、租户隔离或权限检查，导致水平权限提升。披露过程耗时五个月。

hackernews · bearsyankees · May 4, 17:46

**背景**: 多租户应用程序从同一基础架构服务多个客户（租户）；正确的授权确保每个租户只能访问自己的数据。渗透测试（pentest）是一种授权的模拟网络攻击，用于识别漏洞，通常由初创公司或第三方公司执行。该漏洞正是渗透测试人员所寻找的典型例子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup">Securing a DoD Contractor: Finding a Multi - Tenant Authorization ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pentesting">Pentesting</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，即使在顶级风投支持的初创公司中，这种模式也很常见，原因是缺乏注重安全的人员。一些人讨论了 AI 渗透测试工具，但满意度不一。其他人则讽刺地质疑了 SOC2 和 ISO 等合规认证的有效性。

**标签**: `#security`, `#vulnerability`, `#startup`, `#authorization`, `#pentesting`

---

<a id="item-3"></a>
## [Redis 创始人 Antirez 讲述历时四个月的 LLM 辅助数组开发经历](https://antirez.com/news/164) ⭐️ 8.0/10

Redis 的创始人 Antirez 分享了他历时四个月、主要使用 AI 编程工具（如 Claude Code 和 Cursor）开发一个新的 Redis 数组数据结构的经历。 这位传奇开发者的真实经验为当前 AI 编程助手在复杂系统编程中的优势与局限性提供了罕见的洞见。 Antirez 指出，AI 工具作为协作伙伴非常有用，但远未达到替代人类创造力的程度；整个过程涉及超过 22,000 行代码的反复迭代。

hackernews · antirez · May 4, 14:23

**背景**: Redis 是一种内存数据结构存储，广泛用作数据库、缓存和消息代理。像 Claude Code 和 Cursor 这样的 AI 编程工具将大语言模型（LLM）集成到开发工作流程中，帮助进行代码生成、审查和调试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://redis.io/docs/latest/develop/data-types/">Redis data types | Docs</a></li>
<li><a href="https://blog.n8n.io/best-ai-for-coding/">8 best AI coding tools for developers: tested & compared! – n8n Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者强调，Antirez 是一位技能超群的开发者，因此他使用 LLM 花费四个月并不意味着普通开发者应该完全采用 AI 工具。其他人分享了他们自己使用多个 AI 模型相互批评输出的对抗性轮次方法，并指出在没有增量设计讨论的情况下审查如此庞大的代码库的困难。

**标签**: `#AI`, `#software engineering`, `#LLM`, `#Redis`, `#development experience`

---

<a id="item-4"></a>
## [GameStop 提出 555 亿美元收购 eBay](https://www.bbc.co.uk/news/articles/cn0p8yled1do) ⭐️ 8.0/10

GameStop 已向 eBay 提出 555 亿美元的收购要约，每股报价 125 美元。此举标志着这家视频游戏零售商的一次重大战略转变。 如果成功，此次收购将使 GameStop 从一家陷入困境的实体视频游戏零售商转型为大型电子商务平台，可能重塑在线市场格局。鉴于 GameStop 的市值和财务状况，该要约的可行性受到广泛质疑。 每股 125 美元的报价较 eBay 当前股价有溢价，但 GameStop 似乎没有完成交易所需的现金或融资。社区评论指出，CEO 的薪酬与实现 200 亿美元市值挂钩，收购 eBay 可以迅速达成这一目标。

hackernews · n1b0m · May 4, 09:31

**背景**: GameStop 是一家视频游戏零售商，在 2021 年初成为 meme 股票现象的中心，当时一次轧空使其股价大幅上涨。此后，该公司试图通过偿还债务和探索新业务来扭转局面。eBay 是一个以拍卖式和固定价格销售闻名的全球电子商务市场。如此规模的收购对于 GameStop 这样体量的公司来说极不寻常。

**社区讨论**: 社区评论对该要约的可行性持怀疑态度，指出 GameStop 缺乏支付 555 亿美元的资金。一些人认为，该要约可能受到与市值目标挂钩的 CEO 薪酬激励，而另一些人则猜测 GameStop 可以将其实体店用作 eBay 交易的典当行式枢纽。有评论者称 CEO 在 CNBC 的采访不专业。

**标签**: `#business strategy`, `#retail`, `#M&A`, `#ecommerce`

---

<a id="item-5"></a>
## [vLLM v0.20.1 补丁专注于 DeepSeek V4 稳定性](https://github.com/vllm-project/vllm/releases/tag/v0.20.1) ⭐️ 7.0/10

vLLM 发布了 v0.20.1，这是基于 v0.20.0 的补丁版本，主要稳定和优化了 DeepSeek V4 的推理性能，包括多流 GEMM、BF16/MXFP8 all-to-all 支持以及多项错误修复。 此版本对于使用 vLLM 作为 DeepSeek V4（一个 1T 参数的大型模型）推理引擎的生产部署具有重要意义，因为它修复了关键错误并提升了性能，从而能够更可靠、高效地服务最大的开源模型之一。 值得注意的修复包括 TopK=1024 时 persistent topk 的死锁、RadixRowState 中的竞争条件以及非流式工具调用中缺失的类型转换。此补丁还引入了集成 tile 内核以优化头部计算，以及可配置的预注意力 GEMM 旋钮。

github · khluu · May 4, 10:36

**背景**: vLLM 是一个用于高吞吐量 LLM 推理和服务的开源库，广泛应用于生产环境。DeepSeek V4 是一个 1 万亿参数的 MoE 模型，以其 Engram 记忆架构和稀疏注意力而闻名。vLLM v0.20.1 利用 BF16 和 MXFP8（微缩 FP8 格式）等优化实现高效的 all-to-all 通信，并集成 FlashInfer 内核以加速注意力计算。这些技术对于降低内存带宽和提高大型模型的吞吐量至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 : 1T Parameter AI Model Guide | Independent DeepSeek ...</a></li>
<li><a href="https://docs.flashinfer.ai/">FlashInfer 0.6.9 documentation</a></li>
<li><a href="https://github.com/pytorch/ao/blob/main/torchao/prototype/mx_formats/README.md">ao/torchao/prototype/mx_ formats /README.md at main · pytorch/ao</a></li>

</ul>
</details>

**标签**: `#vllm`, `#deepseek`, `#inference`, `#performance`, `#bug-fix`

---

<a id="item-6"></a>
## [LangGraph v1.2 Alpha 引入 DeltaChannel 与精细化节点控制](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0a6) ⭐️ 7.0/10

LangGraph v1.2.0a6 引入了 DeltaChannel，只存储增量变化以实现高效检查点，同时新增了单节点超时、错误恢复处理函数以及新的流式 API。 此版本显著提升了长期运行 AI 代理工作流的性能和可靠性，使 LangGraph 更适合需要高效状态管理和容错能力的生产环境。 DeltaChannel 支持 snapshot_frequency 参数以限制读取延迟；单节点超时可设置为 run_timeout（实际运行时间）或 idle_timeout（进度重置），且仅对异步节点生效。

github · github-actions[bot] · May 4, 13:04

**背景**: LangGraph 是一个用于构建有状态、多步骤 AI 代理的框架，采用基于图的执行方式。检查点用于保存和恢复图状态，但传统上每一步都会序列化整个状态，对于消息列表这类大型状态效率低下。DeltaChannel 通过仅存储变化来解决此问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/langchain-ai/langgraph">GitHub - langchain-ai/ langgraph : Build resilient language agents as...</a></li>
<li><a href="https://deepwiki.com/langchain-ai/langgraph/4.2-checkpoint-implementations">Checkpoint Implementations | langchain-ai/langgraph | DeepWiki</a></li>

</ul>
</details>

**标签**: `#langgraph`, `#llm-agents`, `#state-management`, `#checkpointing`, `#streaming-api`

---

<a id="item-7"></a>
## [Bun 从 Zig 移植到 Rust](https://github.com/oven-sh/bun/commit/46d3bc29f270fa881dd5730ef1549e88407701a5) ⭐️ 7.0/10

Bun（一体化 JavaScript 运行时）正在通过 AI 辅助的大规模代码迁移从 Zig 移植到 Rust，一个分支显示已添加超过 77.3 万行代码。 这一转变可能显著提升 Bun 的内存安全性和生态系统可访问性，同时也会因失去一个高知名度使用者而影响 Zig 社区。它展示了 AI 在大规模代码库迁移中日益重要的作用。 迁移工作在 GitHub 的一个分支中可见，该分支展示了由 Claude（AI）将 Zig 代码重写为 Rust 的过程，共添加 773,950 行，删除 151 行。所引用的初始提交仅为一步；完整的移植似乎正在进行中。

hackernews · SergeAx · May 5, 01:08

**背景**: Bun 是一个快速的 JavaScript 运行时，最初使用 Zig 构建，Zig 是一种旨在替代 C 的系统编程语言。Rust 是另一种以无垃圾收集器实现内存安全著称的系统语言。将 Bun 移植到 Rust 可以利用 Rust 更大的库生态系统和更安全的内存模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**社区讨论**: 评论反映了不同的反应：一些人认为 AI 辅助的迁移是创新之举，而另一些人则担心这对 Zig 的损失并对决策提出质疑。用户提到 Bun 已发布产品（OpenCode）中的段错误，凸显了不安全代码的成本。有人将其与 2015 年 Go 从 C 到 Go 的迁移进行了比较。

**标签**: `#bun`, `#rust`, `#zig`, `#runtime`, `#code migration`

---

<a id="item-8"></a>
## [OpenAI 使用 WebRTC 实现低延迟语音 AI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/) ⭐️ 7.0/10

OpenAI 发布了一篇技术文章，解释了他们如何使用 WebRTC 和 Pion 库为超过 9 亿周活跃用户实现低延迟语音 AI。 这展示了实时语音 AI 的实际扩展能力，会影响其他开发者构建语音接口的方式。然而，用户反馈显示低延迟可能会打断自然的对话停顿，在速度与自然度之间产生权衡。 OpenAI 使用 Pion WebRTC 库（纯 Go 实现）处理实时通信。文章提到三个具体要求：覆盖全球超过 9 亿的周活跃用户，但实际使用语音功能的用户比例可能较小。

hackernews · Sean-Der · May 4, 19:42

**背景**: WebRTC 是一个开源项目，允许浏览器和设备之间进行实时音频、视频和数据通信，无需插件。Pion 是 WebRTC API 的纯 Go 实现，可与基于 Go 的服务高效集成。OpenAI 的语音 AI（称为高级语音模式）旨在提供自然的对话体验，但因在用户停顿期间打断而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebRTC">WebRTC</a></li>
<li><a href="https://github.com/pion/webrtc">GitHub - pion / webrtc : Pure Go implementation of the WebRTC API</a></li>
<li><a href="https://pion.ly/">Pion</a></li>

</ul>
</details>

**社区讨论**: 社区评论包括 Pion 维护者 Sean-Der 对公开宣传表示感谢。用户 legohead 表示不满，认为快速语音 GPT 会打断自然停顿，使随意对话变得困难。另一位评论者 Lucasoato 指出，实时音频模型仍基于 4o 系列，并非前沿模型，并希望有更多竞争。

**标签**: `#voice AI`, `#low-latency`, `#WebRTC`, `#OpenAI`, `#user experience`

---

<a id="item-9"></a>
## [就业减缓认知衰退：因果证据](https://www.nber.org/papers/w35117) ⭐️ 7.0/10

一项 NBER 研究利用当地劳动力市场冲击作为 Bartik 工具变量，估计就业对老年人认知衰退的因果效应，发现负面劳动力需求冲击导致认知能力显著下降，尤其是 51 至 64 岁的男性。 这一因果证据支持了延长工作时间可能延缓与年龄相关的认知衰退的观点，为退休年龄政策和积极老龄化的讨论提供了依据。 该研究使用了健康与退休研究的数据，并基于当地劳动力需求的外生变化构建了 Bartik 工具变量。效应主要集中在 51 至 64 岁的男性中，因为他们的就业对当地劳动力市场状况更为敏感。

hackernews · littlexsparkee · May 4, 15:32

**背景**: 认知衰退是衰老的自然过程，但其速度因人而异。就业可能提供精神刺激、社交互动和结构化生活，有助于维持认知功能。然而，建立因果关系具有挑战性，因为选择工作的人可能在未观测到的方面与退休者不同。Bartik 工具变量通过使用独立于个人选择的当地劳动力需求冲击来分离因果效应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nber.org/papers/w35117">Does Employment Slow Cognitive Decline? Evidence from Labor Market Shocks | NBER</a></li>
<li><a href="https://en.wikipedia.org/wiki/Instrumental_variables_estimation">Instrumental variables estimation</a></li>
<li><a href="https://mixtape.scunning.com/07-instrumental_variables">7 Instrumental Variables – Causal Inference The Mixtape</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了支持该研究的轶事，指出退休常导致不活动和认知衰退，而工作提供了社交和智力参与。有人担心此类研究可能被用来证明延迟退休年龄的合理性，并强调社交生活本身的作用，而非单纯就业。

**标签**: `#economics`, `#cognitive decline`, `#retirement`, `#labor market`, `#public policy`

---

<a id="item-10"></a>
## [Microsoft Edge 在内存中明文存储密码](https://twitter.com/L1v1ng0ffTh3L4N/status/2051308329880719730) ⭐️ 7.0/10

安全研究人员演示了 Microsoft Edge 将所有保存的密码以明文形式保留在进程内存中，即使未使用时也是如此，而 Chrome 则使用操作系统级 API 对密码进行加密。 此漏洞增加了能够读取进程内存的本地攻击者的风险，可能暴露所有存储的密码。这突显了与竞争对手相比的安全差距，并表明 Edge 应采用内存加密实践。 研究人员的工具直接访问 Edge 的内存，而 Chrome 使用 CryptProtectMemory 配合单独的提升权限进程来保护密码。即使具有管理员权限，Chrome 的加密也更难被内存转储攻破。

hackernews · cft · May 4, 18:22

**背景**: 现代浏览器通常会在本地存储用户密码以自动填充登录表单。Chrome 使用 Windows 数据保护 API (DPAPI) 和专用服务对内存中的密码进行加密，从而增加提取难度。基于 Chromium 的 Microsoft Edge 并未实现类似的保护，如果攻击者能够访问进程内存，密码就会暴露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptprotectmemory">CryptProtectMemory function (dpapi.h) - Win32 apps | Microsoft Learn</a></li>

</ul>
</details>

**社区讨论**: 评论者就严重性进行了辩论：一些人认为需要管理员权限使得这个问题影响较低，而另一些人指出即使面对管理员攻击者，Chrome 的加密存储也能提供纵深防御。对比突显了 Edge 的设计安全性较低。

**标签**: `#security`, `#passwords`, `#browser`, `#memory`, `#Microsoft Edge`

---

<a id="item-11"></a>
## [对 Bun 被 Anthropic 收购后的担忧](https://wwj.dev/posts/i-am-worried-about-bun/) ⭐️ 7.0/10

一篇题为《我对 Bun 感到担忧》的博客文章对 Bun 被 Anthropic 收购后的发展方向提出质疑，引发了社区讨论。Bun 开发者 Jared 回应并列举了下个版本的具体改进，包括二进制文件大小缩减和新 CLI 标志。 该文章及随后的讨论凸显了开发者社区对 Bun 被收购后的独立性和质量的担忧，这可能影响采用决策。而 Bun 开发者以具体数据直接回应，为评估 Bun 未来可行性提供了关键信号。 Bun 开发者 Jared 反驳称收购后稳定性有所提升，并列举了具体改进：Windows x64 二进制文件减小 17 MB，Linux 减小 8 MB，新增`--no-orphans` CLI 标志，以及 SSL 上下文缓存。原文章则因 Claude Code 的实践而表达了对 Anthropic 影响的担忧。

hackernews · remote-dev · May 4, 16:45

**背景**: Bun 是一个集 JavaScript 运行时、包管理器、测试运行器和打包器于一身的一体化工具，旨在作为 Node.js 的直接替代品。与 Node.js 和 Deno 使用 V8 引擎不同，Bun 使用 Safari 的 JavaScriptCore 引擎。2024 年，Bun 的创建公司 Oven 被 Anthropic 收购，引发了对运行时长远方向和独立性的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://bun.com/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见不一：一些人赞同原文章对 Anthropic 影响的担忧，另一些人则保持乐观。Bun 开发者 Jared 的发言详细列举了具体改进，另一评论者指出了 Bun 历史上的稳定性问题。讨论还涉及与 Deno 和 Node.js 在性能和功能上的比较。

**标签**: `#Bun`, `#JavaScript`, `#runtime`, `#acquisition`, `#developer-tools`

---

<a id="item-12"></a>
## [2026 年第一季度欧洲热泵销量猛增 17%](https://www.pv-magazine.com/2026/05/04/heat-pump-sales-rise-17-across-europe-in-q1-as-energy-prices-surge/) ⭐️ 7.0/10

2026 年第一季度，受能源价格飙升和政策支持推动，欧洲热泵销量增长了 17%。 这一趋势表明，热泵作为建筑供暖脱碳的关键技术正在加速普及，有助于减少化石燃料依赖并降低消费者的能源成本。 2026 年第一季度同比增长 17%是在能源高价和政府激励措施之后实现的；然而，前期成本和安装复杂性仍是一些家庭的障碍。

hackernews · doener · May 4, 17:35

**背景**: 热泵是一种从空气、地面或水中提取热量，为建筑提供供暖和制冷的设备。其工作原理与空调类似，但可反向运行，效率高（COP 值 3-5），与燃气或燃油锅炉相比碳排放显著降低。欧盟制定了逐步淘汰化石燃料供暖的宏伟目标，使热泵成为其能源转型计划的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Heat_pump">Heat pump - Wikipedia</a></li>
<li><a href="https://ehpa.org/about-heat-pumps/">About heat pumps - European Heat Pump Association</a></li>
<li><a href="https://www.carrier.com/residential/en/us/products/heat-pumps/what-is-a-heat-pump-how-does-it-work/">What Is a Heat Pump? | How Does a Heat Pump Work? | Carrier</a></li>

</ul>
</details>

**社区讨论**: 社区评论提供了实际部署见解：在 TVA 地区（田纳西州），获得高额补贴的热泵热水器可享受 85%的折扣。在德语区国家，热泵因成本和效率优势正成为默认选择。但部分用户指出，对于低能耗住宅，投资回收期超过 20 年，且地源热泵的钻井成本高昂等挑战依然存在。

**标签**: `#energy`, `#heat pumps`, `#Europe`, `#market trends`, `#HVAC`

---

<a id="item-13"></a>
## [牛顿引力通过宇宙尺度最大检验](https://www.science.org/content/article/newton-s-law-gravity-passes-its-biggest-test-ever) ⭐️ 7.0/10

研究人员利用星系团数据在最大宇宙尺度上检验了牛顿引力定律，发现它完全成立，排除了许多修正引力理论，并为暗物质提供了有力证据。 这一结果加强了暗物质范式，并对修正牛顿动力学(MOND)等替代理论施加了严格约束，影响了宇宙学研究方向，使暗物质模型更受青睐。 该分析利用星系团的引力透镜和动力学效应，在远低于 MOND 阈值的加速度下检验该定律，未发现与牛顿预测的偏差。这限制了 MOND 中的加速度标度 a0，并对该理论的修改提出了挑战。

hackernews · pseudolus · May 4, 12:52

**背景**: 牛顿引力定律在太阳系内部作用良好，但在星系尺度上，对星系旋转曲线的观测需要额外的不可见质量，即暗物质。修正牛顿动力学(MOND)提议在低加速度下修改引力以消除对暗物质的需求。这项测试通过检验 MOND 效应本应可见的尺度，提供了迄今为止对 MOND 的最强约束，支持了暗物质假说。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Modified_Newtonian_dynamics">Modified Newtonian dynamics - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2501.17006v1">Chapter 0 Modified Newtonian Dynamics ( MOND )</a></li>

</ul>
</details>

**社区讨论**: 评论者将其与历史上祝融星假说相类比，指出类似的异常曾导致修正理论的出现，直到广义相对论提供了更好的解释。有人提到了 Sabine Hossenfelder 的“MOND 测量仪”，该仪器追踪暗物质与 MOND 之间证据的摇摆，还有人澄清说牛顿引力只是广义相对论的近似，后者在宇宙尺度上更为精确。

**标签**: `#physics`, `#cosmology`, `#dark-matter`, `#gravity`, `#science`

---

<a id="item-14"></a>
## [假冒 Mac 版 Notepad++ 引发商标警告](https://notepad-plus-plus.org/news/npp-trademark-infringement/) ⭐️ 7.0/10

Notepad++ 作者 Don Ho 对假冒的 Mac 版本发出法律威胁，要求立即下架侵权网站。 此事件凸显了假冒软件针对 Mac 用户传播恶意软件的风险，并强调了开源项目商标保护的重要性。 假冒网站未经授权使用 Notepad++ 商标，该移植作者公开抵制重新命名，引发了 Don Ho 的严厉法律警告。

hackernews · maxloh · May 4, 09:40

**背景**: Notepad++ 是一款流行的 Windows 开源文本编辑器，但官方没有 Mac 版本。假冒版本谎称是 Mac 移植版，可能利用受信任的商标传播恶意软件。

**社区讨论**: 社区成员担心假冒移植版可能成为恶意软件的传播载体，批评移植作者的幼稚。其他人讨论了商标法和之前的商标争议案例。

**标签**: `#trademark`, `#malware`, `#open source`, `#Notepad++`, `#legal`

---

<a id="item-15"></a>
## [Y Combinator 持有 OpenAI 0.6%股份，价值 50 亿美元](https://simonwillison.net/2026/May/5/john-gruber/#atom-everything) ⭐️ 7.0/10

John Gruber 通过匿名消息来源报道，Y Combinator 持有 OpenAI 约 0.6%的股份，按 OpenAI 当前 8520 亿美元的估值计算，价值超过 50 亿美元。 这揭示了 Y Combinator 早期投资的巨大回报，并凸显了领先 AI 公司中资本的巨大集中度。 该信息基于了解 OpenAI 投资者基础的匿名消息来源，尚未得到官方确认。OpenAI 的 8520 亿美元估值是其在一篇博文中自行报告的。

rss · Simon Willison · May 5, 00:46

**背景**: Y Combinator 是一家著名的创业加速器，提供早期资助和指导。OpenAI 是 ChatGPT 的创造者，已成为全球最有价值的私营公司之一。私营公司的持股比例通常保密，因此这类数字很少见。

**标签**: `#openai`, `#y-combinator`, `#investment`, `#ai`, `#valuation`

---