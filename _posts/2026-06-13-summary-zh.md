---
layout: default
title: "Horizon Summary: 2026-06-13 (ZH)"
date: 2026-06-13
lang: zh
---

> From 140 items, 14 important content pieces were selected

---

1. [vLLM v0.23.0 重大发布：深度优化 DeepSeek-V4](#item-1) ⭐️ 9.0/10
2. [美国政府下令暂停 Anthropic 的 Fable 5 和 Mythos 5](#item-2) ⭐️ 9.0/10
3. [AUR 软件包遭信息窃取器和 Rootkit 入侵](#item-3) ⭐️ 9.0/10
4. [美国计划从北约撤走三分之一战斗机](#item-4) ⭐️ 9.0/10
5. [法院：尹锡悦利用无人机飞越朝鲜以证明戒严令的正当性](#item-5) ⭐️ 9.0/10
6. [纽约时报实时博客：伊朗-以色列-美国冲突更新](#item-6) ⭐️ 9.0/10
7. [联合国：乌克兰 5 月平民伤亡为四年来最高](#item-7) ⭐️ 9.0/10
8. [新 CRISPR Cas12a2 技术选择性摧毁癌细胞](#item-8) ⭐️ 8.0/10
9. [FFmpeg 发现 21 个零日漏洞](#item-9) ⭐️ 8.0/10
10. [苹果将 TrueType 提示解释器从 C 语言迁移至 Swift](#item-10) ⭐️ 8.0/10
11. [llama.cpp b9606 新增 EAGLE3 投机解码支持](#item-11) ⭐️ 7.0/10
12. [雷诺发布无稀土电动汽车电机技术](#item-12) ⭐️ 7.0/10
13. [Bytecode Alliance 发布 WASI 0.3](#item-13) ⭐️ 7.0/10
14. [Cloudflare 将安全洞察扫描能力提升 10 倍无需增加硬件](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.23.0 重大发布：深度优化 DeepSeek-V4](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) ⭐️ 9.0/10

vLLM v0.23.0 是一次重大发布，包含来自 200 位贡献者的 408 次提交。该版本对 DeepSeek-V4 进行了深度优化，包括稀疏 MLA 元数据解耦、TRTLLM 生成注意力内核、Mega-MoE 的 EPLB 支持以及选择性前缀缓存保留。Model Runner V2 现在默认用于 Llama 和 Mistral 密集模型，将覆盖范围扩大到 Qwen3 之外。 此版本显著提升了大型语言模型（尤其是前沿模型 DeepSeek-V4）的推理性能和效率，降低了生产部署成本并提高了吞吐量。Model Runner V2 的扩展为 Llama 和 Mistral 等广泛使用的开源模型带来了性能提升。 值得注意的细节包括：Rust 前端不断成长，新增了流式 generate 端点和动态 LoRA 端点；多级 KV 缓存卸载引入了对象存储二级层；以及一个用于推理和工具调用解析的统一解析器。请注意，此版本尚不支持 Minimax M3。

github · khluu · Jun 12, 23:29

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理服务引擎。DeepSeek-V4 是一种混合专家（MoE）模型，采用多头潜在注意力（MLA）和 Mega-MoE 架构。专家并行负载均衡（EPLB）可将专家计算分布到多个 GPU 上，以避免负载不均。Model Runner V2 是 vLLM 中新的执行引擎，通过更好的调度和内核优化来提升推理性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/mla/flashmla_sparse/">vllm.v1.attention.backends.mla.flashmla_sparse</a></li>
<li><a href="https://deepwiki.com/NVIDIA/TensorRT-LLM/9.2-trtllm-attention-backend">TRTLLM Attention Backend | NVIDIA/TensorRT-LLM | DeepWiki</a></li>
<li><a href="https://github.com/vllm-project/vllm/pull/18343">[Feature] Expert Parallelism Load Balancer (EPLB) by abmfy · Pull Request #18343 · vllm-project/vllm</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#AI infrastructure`, `#open-source`

---

<a id="item-2"></a>
## [美国政府下令暂停 Anthropic 的 Fable 5 和 Mythos 5](https://www.anthropic.com/news/fable-mythos-access) ⭐️ 9.0/10

美国政府发布指令，要求 Anthropic 暂停对其先进 AI 模型 Fable 5 和 Mythos 5 的访问，理由是国家安全隐患。此次暂停同时影响了公开可用的 Fable 5 和更强大但未发布的 Mythos 5 模型。 这标志着 AI 监管的重大升级，可能限制对尖端 AI 能力的访问，并将全球市场动态转向非美国模型。同时引发了担忧：如果政府可以随意限制访问，投资于日益强大的 AI 模型的可行性将受到质疑。 Fable 5 是 Mythos 的公开版本，包含安全分类器；而 Mythos 5 没有这些分类器，仅通过 Project Glasswing 提供给经过审查的防御者。该指令暂停了这两个模型，影响了全球用户。

hackernews · Dylan1312 · Jun 13, 00:51

**背景**: Anthropic 开发以安全功能闻名的先进 AI 模型。Fable 5 于 2026 年 6 月发布，是一款用于编码和推理的高性能模型；Mythos 5 则是功能更强大但未发布的模型。美国政府日益关注 AI 的国家安全风险，尤其是在可能助长网络攻击或其他威胁的模型方面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/sites/ronschmelzer/2026/06/10/anthropic-fable-5-ai-model-cost/">Anthropic's Fable 5 AI Model Offers More Power At A Higher Price - Forbes</a></li>
<li><a href="https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/">Anthropic's Claude Fable 5 is a version of Mythos the public can access ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Anthropic 自身对其模型的安全警告可能引发了政府行动，这具有讽刺意味。一些人担忧这一先例将削弱对美国 AI 模型的信任，推动用户转向中国替代品，并为 AI 投资带来不确定性。

**标签**: `#AI regulation`, `#national security`, `#Anthropic`, `#US policy`, `#AI model access`

---

<a id="item-3"></a>
## [AUR 软件包遭信息窃取器和 Rootkit 入侵](https://discourse.ifin.network/t/400-aur-packages-compromised-with-infostealer-and-rootkit/577) ⭐️ 9.0/10

一场行动正在积极攻陷 AUR 软件包，注入信息窃取器和 Rootkit 恶意软件；攻击者改用 bun 而非 npm 以绕过先前的防护措施。Arch Linux 尚未正式承认此问题。 这表明 AUR 信任模型存在系统性漏洞，影响了众多依赖 AUR 助手而不手动审查 PKGBUILD 的用户。此行动持续进行且官方零回应，削弱了人们对 Arch 生态系统的信任。 该行动通过从 npm 切换到 bun（一种 JavaScript 运行时和包管理器）绕过了早期的防护措施。社区成员报告称，无人维护的软件包被接管并推送恶意提交而未被察觉。

hackernews · keyle · Jun 12, 05:59

**背景**: Arch 用户软件仓库（AUR）是一个由社区驱动的 PKGBUILD 脚本集合，用于从源代码构建软件包，而非托管二进制包。信任依赖于用户在安装前审查代码，但许多人使用 yay 等 AUR 助手自动下载并构建而不加审查。Bun 是一种 JavaScript 运行时和包管理器，可在软件包构建过程中替代 npm 安装依赖项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Arch_Linux">Arch Linux - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://aur.archlinux.org/">AUR (en) - Home</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 Arch Linux 未正式承认此次攻击或阻断 AUR 访问表示失望。部分人重申 AUR 一直需要用户保持警惕，此次事件暴露了长期存在的信任问题，尤其是无人维护的软件包可被任何人接管。

**标签**: `#security`, `#AUR`, `#malware`, `#Arch Linux`, `#supply-chain attack`

---

<a id="item-4"></a>
## [美国计划从北约撤走三分之一战斗机](https://www.nytimes.com/2026/06/12/world/europe/us-nato-cuts-drawdown-jets.html) ⭐️ 9.0/10

据官员和一份书面文件透露，美国已计划从北约在欧洲的战斗机部署中撤走约三分之一。 此举大幅减少美国对北约的军事承诺，将改变联盟的防御能力，并标志着特朗普政府外交政策的重大转变，可能影响欧洲安全及地缘政治格局。 该计划罕见地明确了拟削减的规模，但受影响的具体机型及数量尚未披露。

rss · NYTimes World · Jun 12, 04:01

**背景**: 北约是北美和欧洲国家组成的军事联盟，旨在提供集体防御。长期以来，美国在欧洲部署了大量空中力量以起到威慑作用。此次可能的削减标志着对先前承诺的显著背离。

**标签**: `#geopolitics`, `#NATO`, `#military strategy`, `#US foreign policy`, `#Europe`

---

<a id="item-5"></a>
## [法院：尹锡悦利用无人机飞越朝鲜以证明戒严令的正当性](https://www.nytimes.com/2026/06/11/world/asia/north-korea-drones-martial-law.html) ⭐️ 9.0/10

韩国法院裁定，前总统尹锡悦于 2024 年下令无人机飞越朝鲜，意图制造不稳定，并以此为借口宣布戒严，巩固威权统治。 该裁决揭露了一位民选领导人蓄意破坏地区稳定和民主制度的计划，对韩国的民主、美韩同盟的信誉以及朝鲜半岛的地缘政治稳定具有深远影响。 法院的判决确认，尹锡悦的行为是为 2024 年威权统治辩护的阴谋的一部分，但无人机飞行的具体细节和时间仍属机密。丑闻曝光后，尹锡悦被弹劾。

rss · NYTimes World · Jun 12, 15:09

**背景**: 韩国与朝鲜之间长期存在紧张关系，此前也曾发生无人机入侵事件，但这是首次有韩国领导人被认定为了国内政治利益而故意挑衅朝鲜。戒严令会暂停公民自由，自 1980 年代民主化以来，韩国从未宣布过戒严。

**标签**: `#geopolitics`, `#south korea`, `#north korea`, `#authoritarianism`, `#martial law`

---

<a id="item-6"></a>
## [纽约时报实时博客：伊朗-以色列-美国冲突更新](https://www.nytimes.com/live/2026/06/11/world/iran-war-trump-us-israel/heres-the-latest) ⭐️ 9.0/10

《纽约时报》正在实时发布关于伊朗、以色列和美国之间潜在军事冲突的最新进展，表明该地区出现重大变化。 这场冲突具有重大的地缘政治和市场影响，可能扰乱全球石油供应并重塑中东联盟。 该实时博客持续更新，反映局势的演变；预计会随时报道空袭、外交行动或伤亡等具体细节。

rss · NYTimes World · Jun 12, 04:27

**背景**: 美国和以色列长期以来反对伊朗的核计划及其地区影响力。最近，由于伊朗核进展和代理人活动，紧张局势加剧。该实时报道追踪这场迅速演变的危机的最新进展。

**标签**: `#Geopolitical Risk`, `#Iran`, `#US`, `#Israel`, `#Conflict`

---

<a id="item-7"></a>
## [联合国：乌克兰 5 月平民伤亡为四年来最高](https://news.un.org/feed/view/en/story/2026/06/1167707) ⭐️ 9.0/10

联合国监测员报告称，乌克兰 5 月份的平民伤亡人数达到四年来最高月度水平，表明冲突升级。 这标志着人道主义局势显著恶化，并突显了战争的持续高强度，影响国际政策应对和风险评估。 联合国报告特别指出，2026 年 5 月的平民伤亡人数超过了过去四年中的任何一个月，摘要中未提供具体数字。

rss · UN News · Jun 12, 12:00

**背景**: 俄乌战争始于 2022 年 2 月俄罗斯的全面入侵，导致持续平民伤亡。联合国一直在定期监测并报告伤亡情况。

**标签**: `#Ukraine`, `#civilian casualties`, `#geopolitical risk`, `#war`, `#humanitarian crisis`

---

<a id="item-8"></a>
## [新 CRISPR Cas12a2 技术选择性摧毁癌细胞](https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/) ⭐️ 8.0/10

研究人员利用 Cas12a2 酶设计了一种 CRISPR 技术，该技术能在检测到肿瘤特异性突变后选择性摧毁癌细胞的染色质，相关成果于 2026 年 5 月发表在《自然》杂志上。 该方法通过靶向任何突变（而不仅仅是致癌驱动突变）来治疗以往难以用药的癌症，代表了癌症治疗的范式转变，具有高选择性和高效能的潜力。 与仅在靶点损伤 DNA 的 Cas9 不同，Cas12a2 一旦被激活就会引发广泛的染色质切割，从而更有效地杀死细胞。该技术仍处于临床前阶段，肿瘤演化可能导致耐药性。

hackernews · gmays · Jun 12, 15:15

**背景**: CRISPR-Cas 系统是能够在特定序列切割 DNA 的基因编辑工具。Cas12a2 是一种变体，在识别目标 RNA 后，会变成非特异性核酸酶，无差别地切割 DNA 和 RNA。“不可成药”癌症指那些由传统小分子药物无法靶向的蛋白质驱动的癌症，原因在于这些蛋白质的结构或功能特点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/">New CRISPR Technique Selectively Shreds Cancer Cells, Including “Undruggable” Cancers - Innovative Genomics Institute (IGI)</a></li>
<li><a href="https://www.nature.com/articles/s41586-026-10466-y">RNA-triggered cell killing with CRISPR–Cas12a2 | Nature</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cas12a">Cas12a - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论显示出对治疗遗传疾病潜力的兴奋，但也有用户对 CRISPR 的炒作表示怀疑，指出仅有一款 CRISPR 疗法获得 FDA 批准，而病毒载体疗法却有很多。其他用户讨论了耐药性的可能性以及使用 Cas12a2 破坏性机制的新颖性。

**标签**: `#CRISPR`, `#cancer`, `#biotechnology`, `#gene therapy`

---

<a id="item-9"></a>
## [FFmpeg 发现 21 个零日漏洞](https://depthfirst.com/research/21-zero-days-in-ffmpeg) ⭐️ 8.0/10

安全研究人员公开了广泛使用的多媒体库 FFmpeg 中的 21 个零日漏洞，其中包括一个关键的堆释放后使用漏洞，可能导致远程代码执行。 这些漏洞对任何通过 FFmpeg 处理用户提供媒体流的服务构成严重风险，包括媒体摄入管道、监控系统和转码服务。 这些漏洞包括内存破坏问题，如释放后使用和堆缓冲区溢出，可通过处理恶意的 RTSP 流或基于 AV1 的 RTP 源触发。

hackernews · redbell · Jun 12, 22:13

**背景**: FFmpeg 是一个流行的开源多媒体框架，用于处理视频、音频和其他多媒体文件及流。由于其复杂性和对各种编解码器的广泛支持，它长期以来一直存在安全问题，成为模糊测试和漏洞研究的常见目标。

**社区讨论**: 社区评论强调 FFmpeg 的安全记录非常糟糕，模糊测试工具不断发现内存破坏漏洞。一些评论者指出，虽然披露的漏洞很严重，但实现任意代码执行可能需要额外条件，如可写可执行内存。

**标签**: `#security`, `#vulnerability`, `#ffmpeg`, `#zero-day`, `#memory-corruption`

---

<a id="item-10"></a>
## [苹果将 TrueType 提示解释器从 C 语言迁移至 Swift](https://www.swift.org/blog/migrating-truetype-hinting-to-swift/) ⭐️ 8.0/10

苹果已将核心字体渲染组件 TrueType 提示解释器从 C 语言迁移至 Swift，以提升 Apple 平台的內存安全性和性能。 此次迁移展示了 Swift 在系统编程领域的成熟度，以及苹果对内存安全的承诺，旨在减少 macOS、iOS 等平台字体解析的攻击面。 迁移涉及处理不可信字体数据的 TrueType 提示字节码解释器，这是一个安全关键组件。Swift 实现以 MIT 许可证发布，供参考。

hackernews · DASD · Jun 12, 19:54

**背景**: TrueType 提示使用字节码指令在低分辨率显示器上精确控制字形渲染。传统上用 C 语言编写的解释器因解析来自不可信来源的复杂数据而成为常见攻击目标。迁移至内存安全语言可消除缓冲区溢出等整类漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.swift.org/blog/migrating-truetype-hinting-to-swift/">Swift at Apple: Migrating the TrueType Hinting Interpreter | Swift.org</a></li>
<li><a href="https://github.com/apple/truetype-hinting-interpreter-example">GitHub - apple/ truetype - hinting - interpreter -example: Swift TrueType ...</a></li>
<li><a href="https://freetype.org/freetype2/docs/hinting/subpixel-hinting.html">The new v40 TrueType interpreter mode</a></li>

</ul>
</details>

**社区讨论**: 社区称赞此次迁移是推动 Swift 广泛应用的举措，并注意到该团队正在招聘。然而，有评论者反映使用 Swift 生命周期功能时遇到编译器崩溃，推测解释器可能只使用了该功能的窄子集。

**标签**: `#Apple`, `#Swift`, `#memory safety`, `#TrueType`, `#systems programming`

---

<a id="item-11"></a>
## [llama.cpp b9606 新增 EAGLE3 投机解码支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9606) ⭐️ 7.0/10

llama.cpp b9606 版本新增了 EAGLE3 投机解码支持，这是一种基于草稿模型的高级技术，可加速大语言模型推理。 EAGLE3 可在保持输出质量的同时显著降低推理延迟，使 llama.cpp 在本地 LLM 部署中更具竞争力。此更新通过提供最先进的优化，惠及不断壮大的开源 AI 社区。 该版本包含对 RedHatAI 的 Gemma4 EAGLE3 模型的支持，并需要进行大量的内部重构，例如启用层输入提取和添加草稿到目标词汇映射。此版本中，部分构建配置（如 macOS 上的 KleidiAI）仍处于禁用状态。

github · github-actions[bot] · Jun 12, 08:45

**背景**: 投机解码是一种推理优化技术，它使用较小的草稿模型生成多个候选 token，然后由目标模型在一次前向传播中验证，可将延迟降低 2-3 倍。EAGLE3 是该技术的演进，它在目标模型的层上附加外推草稿头，以获得更大的加速。llama.cpp 是一个广泛使用的开源 C/C++ LLM 推理实现，针对多种平台的 CPU 和 GPU 进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://deepwiki.com/vllm-project/speculators/4.3-eagle3-models">Eagle3 Models | vllm-project/speculators | DeepWiki</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#inference optimization`, `#speculative decoding`, `#EAGLE3`, `#AI infrastructure`

---

<a id="item-12"></a>
## [雷诺发布无稀土电动汽车电机技术](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) ⭐️ 7.0/10

雷诺集团宣布推出无稀土电动汽车电机，采用有刷绕线转子技术，这一设计虽已有百年历史，但由于成本和供应链优势而重新启用。 此举减少了对钕等稀土元素的依赖，稀土在永磁电机中至关重要且面临供应链风险。这可能降低成本并使电动汽车更加可持续，可能影响其他汽车制造商采用无稀土设计。 该电机使用带电刷的绕线转子产生磁场，而非永磁体，电刷寿命可达 15 万至 25 万英里。然而，宝马的无稀土电机功率更高（高达 300 千瓦 vs 160 千瓦），并采用 800 伏架构。

hackernews · bestouff · Jun 12, 22:08

**背景**: 大多数现代电动汽车电机使用含有钕等稀土的永磁体，这些材料价格昂贵且地缘政治敏感。有刷绕线转子电机是最早的电机，但后来被无刷设计取代。雷诺的方法复兴了这项古老技术用于现代电动汽车，以牺牲部分效率换取材料独立性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brushed_DC_electric_motor">Brushed DC electric motor - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1110016825002820">Self-excited wound rotor synchronous motors for electric vehicles ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出该技术并非新事物；绕线转子电机已有百年历史。有人指出宝马已经提供了更先进的无稀土电机，功率更高且采用 800 伏架构。其他人讨论了有刷/无刷的权衡，指出无刷电机（使用稀土）在遥控车领域通常更优，但面临稀土问题。

**标签**: `#electric vehicles`, `#rare earths`, `#motor technology`, `#automotive`, `#supply chain`

---

<a id="item-13"></a>
## [Bytecode Alliance 发布 WASI 0.3](https://bytecodealliance.org/articles/WASI-0.3) ⭐️ 7.0/10

Bytecode Alliance 宣布了 WASI 0.3，这是 WebAssembly 系统接口的一个主要版本更新，包含自 0.2 版本以来的新功能和变更。该公告包括一篇带有示例的博客文章以及 GitHub 上的详细发布说明。 WASI 0.3 的重要性在于它提升了 WebAssembly 在浏览器之外安全运行的能力，实现了跨平台的可移植和高效应用。此次发布完善了标准，这对于生态系统采用以及开发者对 WebAssembly 在服务器端、边缘和嵌入式环境中使用的信心至关重要。 WASI 0.3 的主要变更包括对接口类型和组件模型的更新，详见 GitHub 发布中的 .wit 文件。公告文章澄清了与 WASI 0.2 的差异并提供了示例，但社区反馈显示对复杂性增加和组件模型演进缓慢的担忧。

hackernews · mavdol04 · Jun 12, 13:51

**背景**: WebAssembly (Wasm) 是一种低级二进制指令格式，旨在以接近原生的速度在安全沙箱中运行代码。WebAssembly 系统接口 (WASI) 将 Wasm 的功能扩展到系统级操作，如文件系统访问和网络，使其在浏览器之外也能使用。Bytecode Alliance 是负责管理这些标准和工具的非营利组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bytecodealliance.org/">Bytecode Alliance</a></li>
<li><a href="https://github.com/WebAssembly/WASI">GitHub - WebAssembly/WASI: WebAssembly System Interface · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一；一些开发者对组件模型的缓慢进展和被认为过度复杂化表示失望，认为更简单的类 Unix API 会更好。其他人则认可这项工作，但希望有更多的稳定性和开发透明度。少数人指出，带有自定义集成的独立 Wasm 可能是更实际的未来。

**标签**: `#WebAssembly`, `#WASI`, `#Bytecode Alliance`, `#system interface`, `#standard`

---

<a id="item-14"></a>
## [Cloudflare 将安全洞察扫描能力提升 10 倍无需增加硬件](https://blog.cloudflare.com/scaling-security-scans/) ⭐️ 7.0/10

Cloudflare 的安全洞察系统现已实现每秒处理超过 120 次扫描，通过优化 Kafka 消费者、Postgres 查询和 API，在不增加硬件的情况下将扫描能力提升了 10 倍。 这一改进使得 Cloudflare 能够以规模化方式为所有客户提供频繁的安全洞察，证明了仅通过软件优化即可实现显著的吞吐量提升，从而降低基础设施成本和环境影响。 该系统从较低的基线扩展到每秒超过 120 次扫描，优化目标包括 Kafka 消费者效率、Postgres 查询性能和 API 响应时间。

rss · Cloudflare Blog · Jun 12, 13:00

**背景**: Cloudflare 安全洞察是一项对客户基础设施进行定期扫描以提供安全建议的功能。它涵盖了账户设置、DNS 配置和 SSL/TLS 设置等方面。扫描生成一系列洞察，帮助用户识别和修复潜在安全问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/learning-paths/application-security/security-center/insights/">Security Insights · Cloudflare Learning Paths</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/security-center/security-insights/how-it-works.mdx">github.com/ cloudflare / cloudflare -docs/blob/production/src/content...</a></li>

</ul>
</details>

**标签**: `#scalability`, `#security scanning`, `#engineering`, `#Kafka`, `#Postgres`

---