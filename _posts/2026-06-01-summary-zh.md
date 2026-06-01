---
layout: default
title: "Horizon Summary: 2026-06-01 (ZH)"
date: 2026-06-01
lang: zh
---

> From 87 items, 7 important content pieces were selected

---

1. [每日药片 daraxonrasib 使胰腺癌生存期翻倍](#item-1) ⭐️ 9.0/10
2. [1 位 Bonsai Image 4B 实现本地图像生成](#item-2) ⭐️ 8.0/10
3. [Dav2d：首个 AV2 解码器揭示其复杂度为 AV1 的五倍](#item-3) ⭐️ 8.0/10
4. [Cloudflare Turnstile 要求 WebGL 指纹识别，引发隐私担忧](#item-4) ⭐️ 7.0/10
5. [Meta 为 Facebook、Instagram 和 WhatsApp 推出订阅服务](#item-5) ⭐️ 7.0/10
6. [Linux 重启序列实现高效每 CPU 数据结构](#item-6) ⭐️ 7.0/10
7. [监控类 AI 写作的社会代价](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [每日药片 daraxonrasib 使胰腺癌生存期翻倍](https://www.theguardian.com/society/2026/may/31/daily-pill-daraxonrasib-double-survival-time-pancreatic-pancreas-cancer-clinical-trial) ⭐️ 9.0/10

一项 3 期临床试验（RASolute 302）发现，口服药物 daraxonrasib（RMC-6236）在携带 KRAS G12X 突变的晚期胰腺癌患者中，将中位总生存期翻倍至 13.2 个月，而标准化疗组为 6.7 个月。 这项突破为历史上治疗手段有限的致命癌症提供了新的口服治疗方案。研究结果可能改变标准疗法，为成千上万治疗选择有限的患者带来希望。 Daraxonrasib 是一种 RAS(ON)多选择性抑制剂，通过与亲环蛋白 A 形成三重复合物的机制靶向突变型和野生型 GTP 结合的 RAS 蛋白。该试验为开放标签，显示死亡风险降低 60%（风险比 0.40，p<0.0001），且安全性可控。

hackernews · c-oreills · May 31, 15:43

**背景**: 胰腺导管腺癌（PDAC）是最致命的癌症之一，常由 KRAS 突变驱动。历史上，RAS 蛋白被认为是“不可成药的”，直到近年抑制剂设计取得进展。Daraxonrasib 于 2025 年获得 FDA 突破性疗法认定，由 Revolution Medicines 开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Daraxonrasib">Daraxonrasib</a></li>
<li><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2505783">Daraxonrasib in Previously Treated Advanced RAS-Mutated ...</a></li>

</ul>
</details>

**社区讨论**: 评论者提供了 Derek Lowe 的博文和 NEJM 论文的链接，指出该试验的重要性。一些人表达了对资金差异的担忧，另一些人则询问将该药与化疗联合使用以进一步改善疗效的可能性。

**标签**: `#medical research`, `#cancer treatment`, `#clinical trial`, `#pancreatic cancer`, `#drug development`

---

<a id="item-2"></a>
## [1 位 Bonsai Image 4B 实现本地图像生成](https://prismml.com/news/bonsai-image-4b) ⭐️ 8.0/10

Bonsai Image 4B 是首个使用 1 位和三进制权重的图像生成模型，将 40 亿参数的扩散变压器压缩至 1.21 GB，并能在 iPhone 等本地设备上无需云端依赖进行推理。 这一模型压缩突破通过大幅降低硬件需求并消除订阅成本，使高质量图像生成民主化，可能将 AI 格局转向本地、私密推理。 该模型实现了 1 位和三进制量化，相比典型的 16 位模型提供 6.4 倍压缩且质量损失极小，并声称可在消费级 GPU 和 Apple Silicon 上实时运行。

hackernews · modinfo · May 31, 15:04

**背景**: 传统的图像生成扩散模型需要大量内存（7.75 GB 或更多）和强大的云端服务器，限制了本地部署。1 位神经网络由微软的 BitNet 开创，每个权重用单个比特或三进制值表示，大幅减小模型体积和计算成本，同时保持性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/data-science-in-your-pocket/bonsai-image-worlds-1st-1-bit-image-generator-5afb94cb6f20">Bonsai Image : World’s 1st 1-bit Image Generator | Medium</a></li>
<li><a href="https://prismml.com/news/bonsai-image-4b">Introducing 1-bit and Ternary Bonsai Image 4B: Image Generation for...</a></li>
<li><a href="https://github.com/microsoft/BitNet">GitHub - microsoft/BitNet: Official inference framework for 1 ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人质疑内存还是速度是真正的瓶颈，指出即使模型更小，生成时间仍是挑战；其他人对无需订阅的本地 AI 硬件升级表示兴奋；还有人推测 1 位抖动图像生成作为一种替代方法。

**标签**: `#image generation`, `#1-bit models`, `#local AI`, `#model compression`, `#on-device inference`

---

<a id="item-3"></a>
## [Dav2d：首个 AV2 解码器揭示其复杂度为 AV1 的五倍](https://jbkempf.com/blog/2026/dav2d/) ⭐️ 8.0/10

VideoLAN 发布了 Dav2d，这是 AV2 视频编码标准的首个开源软件解码器。它表明 AV2 解码的复杂度大约是 AV1 的五倍，导致在现有硬件上难以实现实时软件播放。 复杂度提升五倍意味着配备 AV1 硬件解码器的设备可能难以通过软件解码 AV2，可能推迟其采用直至新硬件问世。25%的码率节省可能无法证明性能代价的合理性，尤其对流媒体服务和终端用户而言。 Dav2d 基于广泛使用的 AV1 解码器 dav1d 开发。AV2 规范于 2026 年 5 月 28 日正式发布，早期实现显示在相似质量下码率比 AV1 降低约 30%，但解码复杂度显著提高。

hackernews · captain_bender · May 31, 11:44

**背景**: AV2 是 AV1 的继任者，AV1 是由开放媒体联盟（Alliance for Open Media）开发的开源免版税视频编码标准。其目标是在 AV1 基础上将压缩效率提升约 30%，与 VVC 竞争。然而，复杂度增加给现有硬件上的软件解码带来挑战，特别是实时播放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV2_(video_coding_format)">AV2 (video coding format)</a></li>
<li><a href="https://www.phoronix.com/news/AV2-1.0-Specification-Released">AV 2 v1.0 Specification Released For Next-Gen Video Coding - Phoronix</a></li>
<li><a href="https://de.news.hada.io/topic?id=29105">dav 2 d – VideoLANs plattformübergreifender AV 2 - Decoder | GeekNews</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 AV2 解码复杂度五倍提升而体积仅减少 25%的性价比表示怀疑。有人指出 AV1 软件解码已经非常耗费资源，AV2 的基准测试将揭示更多问题。Hacker News 的流量冲击导致原页面带宽超限。

**标签**: `#AV2`, `#video codec`, `#decoder performance`, `#hardware implications`

---

<a id="item-4"></a>
## [Cloudflare Turnstile 要求 WebGL 指纹识别，引发隐私担忧](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting) ⭐️ 7.0/10

Cloudflare 的 Turnstile（一种验证码替代方案）现在要求通过 WebGL 指纹识别来验证用户，据 Hacktivis.me 报道。这意味着用户必须通过 WebGL API 暴露其 GPU 细节才能通过挑战。 这一变化通过启用更精确的浏览器指纹识别来损害用户隐私，与 Turnstile 承诺的隐私友好型机器人检测相矛盾。它尤其影响依赖反指纹措施或使用非主流浏览器的注重隐私的用户。 WebGL 指纹识别提取详细的 GPU 信息，可用于创建唯一的浏览器指纹，因为它依赖于硬件特定的渲染差异。即使启用了 Firefox 的“严格”模式等隐私设置，WebGL 指纹识别可能仍然可用。

hackernews · HypnoticOcelot · May 31, 14:13

**背景**: WebGL 是一种 JavaScript API，允许网页浏览器访问设备的 GPU 进行 3D 图形渲染。通过 WebGL 进行指纹识别的工作原理是测量 GPU 如何处理特定的渲染任务，从而根据硬件和驱动程序的差异产生唯一的签名。Cloudflare Turnstile 是一种验证码替代方案，旨在无需显示谜题即可验证人类用户，但这一新要求损害了其隐私声明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/products/turnstile/">Cloudflare Turnstile - Easy CAPTCHA Alternative</a></li>
<li><a href="https://browserleaks.com/webgl">WebGL Browser Report - WebGL Fingerprinting - BrowserLeaks</a></li>

</ul>
</details>

**社区讨论**: 社区评论对这一举措表示强烈批评。一位用户指出，指纹识别对于机器人检测可能是必要的，但可能被滥用；另一位警告这可能导致互联网变成围墙花园。一个小众浏览器的维护者报告用户受到影响，并且有人猜测谷歌和 Cloudflare 之间存在交易。

**标签**: `#cloudflare`, `#fingerprinting`, `#privacy`, `#webgl`, `#captcha`

---

<a id="item-5"></a>
## [Meta 为 Facebook、Instagram 和 WhatsApp 推出订阅服务](https://techcrunch.com/2026/05/27/meta-officially-launches-instagram-facebook-and-whatsapp-subscriptions-with-more-to-come-including-ai-plans/) ⭐️ 7.0/10

Meta 正式为其三大平台推出订阅计划，提供无广告体验和额外功能。此举旨在广告之外创造新的收入来源。 这标志着 Meta 从纯广告支持模式向混合收入模式的重大转变，很可能受到欧盟监管压力和广告市场变化的驱动。这可能为其他社交媒体平台树立先例，并影响用户体验和广告商关系。 订阅服务据说包括无广告浏览以及验证徽章和增强客户支持等额外福利。定价细节尚未完全披露，但可能因地区而异。

hackernews · tambourine_man · May 31, 17:02

**背景**: Meta 的核心业务一直是广告，但欧盟《数字市场法案》（DMA）等监管行动要求平台提供退出追踪的选项。订阅为用户提供了一种付费获得隐私的方式。其他平台如 Twitter/X 和 Snapchat 也已推出订阅层级。

**社区讨论**: 评论意见分歧：一些用户欢迎为无广告体验付费的选项，并认为这是减少对广告依赖的积极一步；另一些人批评 Meta 并敦促用户删除这些应用，还有一些人表达了特定功能需求，如仅好友动态。总体情绪复杂，对执行和价值的怀疑存在。

**标签**: `#Meta`, `#subscriptions`, `#business model`, `#social media`, `#advertising`

---

<a id="item-6"></a>
## [Linux 重启序列实现高效每 CPU 数据结构](https://justine.lol/rseq/) ⭐️ 7.0/10

Linux 内核提供了重启序列（restartable sequences, rseq）机制，允许用户空间定义临界区，当线程被抢占时内核可重启该临界区，从而无需互斥锁或原子操作即可实现每 CPU 数据结构。 rseq 显著提升了多核性能，消除了每 CPU 数据访问中互斥锁和原子操作的开销，减少了竞争，对高性能计算和系统软件至关重要。 rseq 通过 rseq(2) 系统调用工作，注册每个线程的 struct rseq 内存区域，内核会更新当前 CPU 编号和节点 ID；TCMalloc 已在生产环境中使用 rseq 实现每 CPU 缓存。

hackernews · grappler · May 31, 14:38

**背景**: 现代操作系统将线程调度到多个 CPU 上，访问共享数据时会导致缓存竞争。传统同步方式使用原子操作或互斥锁，开销较大。rseq 允许线程临时假设不会被迁移，若被迁移，内核会重启临界区，从而无需锁即可保证正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.kernel.org/userspace-api/rseq.html">Restartable Sequences — The Linux Kernel documentation</a></li>
<li><a href="https://google.github.io/tcmalloc/rseq.html">Restartable Sequence Mechanism for TCMalloc | tcmalloc</a></li>
<li><a href="https://www.efficios.com/blog/2019/02/08/linux-restartable-sequences/">The 5-year journey to bring restartable sequences to Linux - EfficiOS</a></li>

</ul>
</details>

**社区讨论**: 评论者提供了额外背景：GlenTheMachine 强调 rseq 比互斥锁更优雅；senderista 提到 librseq 库提供了常见用法的辅助函数；khuey 批评文章开头对昂贵工作站的轻蔑口吻；Veserv 指出该技术约 25 年前就已出现；smasher164 探讨了使用 rseq 实现用户空间加载链/存储条件指令的可能性。

**标签**: `#linux`, `#kernel`, `#concurrency`, `#performance`, `#rseq`

---

<a id="item-7"></a>
## [监控类 AI 写作的社会代价](https://mail.cyberneticforests.com/its-not-just-data-its-post-training/) ⭐️ 7.0/10

一篇博客文章指出，公开羞辱类似 AI 写作的文字可能会压制人类的推理和自然表达，尤其是 RLHF 可能导致 AI 习语的出现。 这凸显了随着 AI 文本检测日益普及，对人类表达可能产生的寒蝉效应，将讨论焦点从检测准确性转移到监控写作风格的社会代价上。 文章将 AI 习语的出现归因于 RLHF 而非训练数据，并与学术写作教学法进行了历史类比，警告对误报的恐惧可能阻碍正常的推理语言使用。

hackernews · mooreds · May 31, 21:57

**背景**: 后训练是指在初始预训练之后应用的诸如 RLHF 之类的技术，用于对齐模型。AI 文本检测方法包括统计分析和深度学习分类器，但其性能在不同情境下不一致。AI 习语的来源——来自训练数据还是对齐过程——存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Shift_to_post-training_compute_allocation_in_AI">Shift to post-training compute allocation in AI</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S1574013725000693">AI-generated text detection: A comprehensive review of methods, datasets, and applications - ScienceDirect</a></li>
<li><a href="https://aiwiki.ai/wiki/post-training">Post-training - AI Wiki</a></li>

</ul>
</details>

**社区讨论**: 评论者大体上同意博客的担忧。一位用户认为该论点‘令人恐惧且阐述得很好’，另一位则认为 AI 习语作为水印有价值，但愿意接受人类避免使用它们的代价。其他人则争论习语是否从 RLHF 中产生，并指出评估语言模式的做法早于 LLM。

**标签**: `#AI`, `#society`, `#text detection`, `#post-training`, `#social impact`

---