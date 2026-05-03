---
layout: default
title: "Horizon Summary: 2026-05-03 (ZH)"
date: 2026-05-03
lang: zh
---

> From 21 items, 7 important content pieces were selected

---

1. [DeepSeek V4 预览版发布，开源且代理能力增强](#item-1) ⭐️ 9.0/10
2. [Mercury 公司分享维护 200 万行 Haskell 生产代码的经验](#item-2) ⭐️ 8.0/10
3. [VideoLAN 发布 dav2d：快速开源 AV2 解码器](#item-3) ⭐️ 8.0/10
4. [开发者分享六年打造 watchOS 地图应用历程](#item-4) ⭐️ 8.0/10
5. [VS Code 未经许可在提交中加入 Copilot 署名引发众怒](#item-5) ⭐️ 8.0/10
6. [NASA O2O 激光系统从月球传输 484 GB 数据](#item-6) ⭐️ 8.0/10
7. [iPhone 通过 SSD 流式读取运行 400B 参数模型](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 预览版发布，开源且代理能力增强](https://t.me/zaihuapd/41185) ⭐️ 9.0/10

DeepSeek 开源了 V4 预览版，包含两个版本：DeepSeek-V4-Pro 大幅提升了代理能力，在数学、STEM 和竞赛编程上超越所有已评测开源模型；DeepSeek-V4-Flash 则更小、更快、更便宜，但仍具备强推理和代理能力。 此次发布将开源大模型在代理任务上的能力推至接近顶级闭源模型，可能重塑自主 AI 代理领域的格局，并以更低成本为开发者带来高性能的代理 AI。 DeepSeek-V4-Pro 在代理相关基准上超越所有开源模型，接近‘御三家’（GPT、Claude、Gemini）水平。V4-Flash 凭借更小参数和激活实现更快、更经济的推理，而 ‘Flash-Max’ 版本可通过增加思考预算获得接近 Pro 的推理性能。

telegram · zaihuapd · May 3, 02:21

**背景**: 代理 AI 指能自主行动和决策的 AI 系统，超越简单的辅助功能。中文 AI 圈中的‘御三家’指三大顶级闭源模型系列：GPT (OpenAI)、Claude (Anthropic) 和 Gemini (Google)。DeepSeek-V4 延续了 DeepSeek-V3、R1 等开源模型的路线，推动开源模型挑战闭源系统。V4-Pro 专为需深度推理的高精度任务设计，V4-Flash 则面向低延迟、高吞吐场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.grammarly.com/agentic-ai">What is Agentic AI ? | Agentic AI 101</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1944892815285924215">Gemini、Claude、GPT御三家模型的个人体会和建议 - 知乎</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-deepseek-v4-flash-and-v4-pro-in-microsoft-foundry/4515174">Introducing DeepSeek V4 Flash and V4 Pro in Microsoft Foundry | Microsoft Community Hub</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#LLM`, `#Open Source`, `#AI Agents`, `#Model Release`

---

<a id="item-2"></a>
## [Mercury 公司分享维护 200 万行 Haskell 生产代码的经验](https://blog.haskell.org/a-couple-million-lines-of-haskell/) ⭐️ 8.0/10

Mercury 发布了一篇详细文章，介绍其在生产环境中维护超过 200 万行 Haskell 代码的经验，强调强类型系统如何防止错误，但也指出了可读性和团队生产力的挑战。 该案例为 Haskell 在高风险金融科技环境中大规模应用的可行性提供了罕见证据，有助于组织评估函数式编程语言的决策。 代码库规模达 200 万行，使用类型来强制执行关键业务不变量，但文章警告说过度的类型建模可能导致大量重构和维护负担。

hackernews · unignorant · May 3, 00:01

**背景**: Haskell 是一种静态类型、纯函数式编程语言，以其强大的类型系统和能编码不变量的能力而闻名。Mercury 是一家提供银行服务的金融科技公司，以其工程文化及在生产中使用 Haskell 而著称。函数式编程强调不可变数据和纯函数，与命令式风格形成对比。

**社区讨论**: 评论者普遍认可 Haskell 的类型安全优势，但对可读性、过度使用类型导致代码库僵化以及与 Rust 等语言相比生产力较低表示担忧。一些人还指出，单字母变量名等风格问题困扰着 Haskell 代码库。

**标签**: `#Haskell`, `#production engineering`, `#functional programming`, `#maintainability`, `#case study`

---

<a id="item-3"></a>
## [VideoLAN 发布 dav2d：快速开源 AV2 解码器](https://code.videolan.org/videolan/dav2d) ⭐️ 8.0/10

VideoLAN 发布了 dav2d，一个新的开源 AV2 视频解码器，旨在成为最快、最可移植的实现，支持 x86、ARM 和 RISC-V 等多种 CPU 架构。 AV2 承诺较 AV1 大幅降低比特率，像 dav2d 这样高效的 CPU 解码器可以在硬件解码器普及前推动生态采用，重现 dav1d 对 AV1 的关键作用。 dav2d 代码库目前专注于正确性，并计划为 x86、ARM 和 RISC-V 进行汇编优化；AV2 规范仍处于草案状态，但已在 2026 年 CES 展会上进行了演示。

hackernews · dabinat · May 2, 17:32

**背景**: AV1 是由开放媒体联盟开发的免版税视频编解码器，被 YouTube 和 Netflix 等平台广泛采用。AV2 是其下一代继任者，目标是将压缩效率提高多达 30%。dav1d 解码器通过手写汇编语言实现了高效的 AV1 软件播放，对不具备硬件解码的设备至关重要。dav2d 遵循同样的理念以加速 AV2 的普及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Dav2d-Open-Source-AV2-Decode">VideoLAN Publishes Dav2d For Open-Source AV2 Decoder</a></li>
<li><a href="https://videocardz.com/newz/videolan-publishes-dav2d-an-early-cpu-decoder-for-av2-video-codec">VideoLAN publishes dav2d, an early CPU decoder for AV2 video ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/AV2_(video_coding_format)">AV2 (video coding format)</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 dav2d 被描述为最快的 AV2 解码器，并回忆起 dav1d 对 AV1 采用的变革性影响。有人询问使用方面的技术问题（如将 H.264 转换为 AV2），另有人提到 AV2 规范已推迟，截至 2026 年 5 月仍处于草案状态。

**标签**: `#AV2`, `#video codec`, `#dav2d`, `#open source`, `#multimedia`

---

<a id="item-4"></a>
## [开发者分享六年打造 watchOS 地图应用历程](https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/) ⭐️ 8.0/10

一位开发者分享了六年来在 watchOS 上打磨自定义地图应用的历程，该应用采用独特的制图数据，包含苹果地图所没有的远足小径。 此事凸显了苹果在第一方户外地图功能上的缺失，同时展示了第三方创新如何满足小众用户需求，为可穿戴应用开发提供了宝贵经验。 该应用使用雇佣制图师制作的预渲染图像瓦片，细节丰富，但与苹果地图的动态渲染不同，需要为不同缩放级别和方向单独下载。

hackernews · valzevul · May 2, 21:14

**背景**: watchOS 是苹果手表的操作系统。苹果地图在远足路线和地形信息方面功能有限，即使是面向探险的 Apple Watch Ultra 也不例外。第三方应用可通过自定义制图和专业功能填补这一空白。

**社区讨论**: 评论者对苹果未提供徒步地图感到失望，对应用的定价模式感到困惑，并对技术成就表示赞赏。有人喜欢其定制设计和怀旧轶事，也有人指出缺少 GPX 导入等基本功能。

**标签**: `#watchOS`, `#Apple Watch`, `#maps`, `#software development`, `#hiking`

---

<a id="item-5"></a>
## [VS Code 未经许可在提交中加入 Copilot 署名引发众怒](https://github.com/microsoft/vscode/pull/310226) ⭐️ 8.0/10

在 PR #310226 中，VS Code 将 'git.addAICoAuthor' 的默认值改为 'all'，导致即使 AI 功能被禁用或未使用 Copilot，提交信息中仍被自动添加 'Co-Authored-by: Copilot'。 此举伪造了版本控制记录中的作者归属，破坏开发者信任，而 Git 提交是具有法律和伦理责任的关键记录；这暴露出将 AI 推广置于用户同意之上的不良趋势。 配置 schema 默认值改变后，运行时回退逻辑仍调用 'off'，造成不一致。Copilot 机器人对此提出审阅警告却被忽略，且设置 'disableAIFeatures' 为真也未能阻止该行为。

hackernews · indrora · May 2, 19:57

**背景**: 在 Git 中，'Co-authored-by' 是用于标注多个贡献者的标准提交尾注。未经用户明确操作而误用它会歪曲提交来源。VS Code 是广泛使用的代码编辑器，通过 GitHub Copilot 集成 AI 功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors">Creating a commit with multiple authors - GitHub Docs</a></li>
<li><a href="https://stackoverflow.com/questions/58525836/git-magic-keywords-in-commit-messages-signed-off-by-co-authored-by-fixes">github - Git magic keywords in commit messages (Signed-off-by...)</a></li>

</ul>
</details>

**社区讨论**: 社区普遍谴责此变更，认为是严重破坏信任和违反道德的行为。评论者强调，为营销数据伪造提交作者不可接受，并指出 Copilot 机器人自身的警告被无视。批准者已道歉，但怀疑情绪仍在。

**标签**: `#AI`, `#ethics`, `#version-control`, `#developer-tools`, `#Microsoft`

---

<a id="item-6"></a>
## [NASA O2O 激光系统从月球传输 484 GB 数据](https://dailygalaxy.com/2026/05/nasa-just-beamed-484-gigabytes-from-moon/) ⭐️ 8.0/10

在阿尔忒弥斯二号任务中，NASA 的 O2O 激光通信系统以每秒 260 兆比特的下行速率成功从月球传回 484 吉字节数据，展现了空间通信带宽的重大飞跃。 这一突破使得高清月球图像能够近实时分析，并为公众提供流畅的视频流，为未来月球和火星任务的高带宽通信奠定了基础。 该系统由麻省理工学院林肯实验室开发，地面站包括喷气推进实验室、白沙综合设施和澳大利亚国立大学斯特罗姆洛山天文台，曾在一小时内接收 26 吉字节数据。

telegram · zaihuapd · May 3, 00:50

**背景**: 自由空间光通信使用红外激光束代替无线电波，由于频率更高，提供了远高于射频的数据速率。NASA 自 2013 年起测试激光通信，包括激光通信中继演示（LCRD）。猎户座阿尔忒弥斯二号光通信系统（O2O）是首个用于载人月球任务的实用激光系统，克服了精确指向和大气干扰等挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artemis_II">Artemis II - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Free-space_optical_communication">Free-space optical communication</a></li>

</ul>
</details>

**标签**: `#space exploration`, `#laser communication`, `#NASA`, `#Artemis`, `#optical communications`

---

<a id="item-7"></a>
## [iPhone 通过 SSD 流式读取运行 400B 参数模型](https://x.com/anemll/status/2035901335984611412) ⭐️ 8.0/10

ANEMLL 项目展示了一台 iPhone 17 Pro 运行了一个 4000 亿参数的混合专家（MoE）模型。通过从 SSD 流式读取专家权重，该模型仅占用 5.5 GB 内存，推理速度达到每秒 0.6 个 token。 这证明了超大规模模型可以利用设备存储作为虚拟内存，在移动设备上运行，为无需持续云连接的先进终端 AI 打开了大门。 该模型采用混合专家（MoE）架构，每次推理仅激活部分参数；Flash-MoE 引擎负责管理从 iPhone NVMe SSD 加载专家权重。每秒 0.6 个 token 的推理速度远未达到实时交互的要求。

telegram · zaihuapd · May 3, 10:57

**背景**: 混合专家（MoE）模型通过划分为多个“专家”，每次只激活相关部分，以极高参数量降低计算量。但存储所有权重通常需要大量内存。本方案从 iPhone 的高速 NVMe 固态硬盘按需流式加载权重，大幅降低内存占用，代价是速度变慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agent-wars.com/news/2026-03-24-iphone-17-pro-runs-a-400b-parameter-llm-via-ssd-streaming">iPhone 17 Pro Runs a 400B Parameter LLM via Flash Streaming</a></li>
<li><a href="https://github.com/tonbistudio/moe-ssd-streaming-windows">GitHub - tonbistudio/moe- ssd - streaming -windows: Running a 32 GB...</a></li>

</ul>
</details>

**标签**: `#edge-computing`, `#large-language-models`, `#mobile-inference`, `#Flash-MoE`, `#iPhone`

---