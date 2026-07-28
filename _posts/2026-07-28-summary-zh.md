---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> From 131 items, 9 important content pieces were selected

---

1. [Kimi-K3 3 万亿参数开源权重模型发布](#item-1) ⭐️ 9.0/10
2. [胡塞武装红海封锁加剧亚洲能源危机](#item-2) ⭐️ 9.0/10
3. [美方在军方建议后暂停对伊朗打击](#item-3) ⭐️ 9.0/10
4. [OpenAI Agents SDK v0.19.0 新增程序化工具调用](#item-4) ⭐️ 8.0/10
5. [Anthropic 支持对开源权重模型进行安全测试](#item-5) ⭐️ 8.0/10
6. [沃尔沃/艾歇尔车队平台遭入侵，账户可完全接管](#item-6) ⭐️ 8.0/10
7. [法官驳回谷歌利用 DMCA 阻止数据抓取的尝试](#item-7) ⭐️ 8.0/10
8. [Bun 的 Rust 重写已在 Claude Code 中发布，公开版本延迟](#item-8) ⭐️ 8.0/10
9. [NVIDIA Cosmos-H-Dreams 实现实时手术模拟](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi-K3 3 万亿参数开源权重模型发布](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 9.0/10

Moonshot AI 在 HuggingFace 上发布了 Kimi-K3，这是一个拥有 2.8 万亿参数的开源权重语言模型，具备 100 万 token 的上下文窗口和原生视觉能力。 作为有史以来最大的开源权重模型之一，Kimi-K3 使初创公司和企业能够广泛定制和微调，促进创新并减少对专有 API 的依赖。 该模型使用原生 mxfp4 精度，托管需要约 1.5TB 显存，并支持多达 16-32 块 GPU 以达到最佳吞吐量。

hackernews · nateb2022 · Jul 27, 06:18

**背景**: 开源权重模型提供训练后的模型权重，允许用户运行、微调和定制，而无需访问训练数据或代码。这与 GPT-4 等仅通过 API 提供的封闭模型形成对比。Kimi-K3 基于 Moonshot AI 专有的 Kimi Delta Attention 和 Attention Residuals 技术构建，实现了大规模高性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi - K 3 · Hugging Face</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://medium.com/@bhagyarana80/why-open-weight-models-matter-more-than-you-think-1d1d8787a4fe">Why Open - Weight Models Matter (More Than You Think) | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论突出了三个主题：托管成本估算（基于 1.5TB 显存的大致每百万 token 价格）、定制化和知识产权主权战略价值，以及对围绕该模型形成的生态系统（包括推理栈和量化工具）的期待。

**标签**: `#AI`, `#open-source`, `#large language model`, `#cost`, `#customization`

---

<a id="item-2"></a>
## [胡塞武装红海封锁加剧亚洲能源危机](https://www.theguardian.com/world/2026/jul/28/asia-energy-oil-crisis-red-sea-blockade-houthis) ⭐️ 9.0/10

也门胡塞武装已对经过曼德海峡的沙特航运实施封锁，威胁到对亚洲的石油出口，而亚洲已因霍尔木兹海峡关闭而陷入困境。 这一封锁切断了日本、韩国、菲律宾等亚洲国家的重要石油供应路线，这些国家高达 90%的进口石油依赖中东，可能引发六个月内的第二次重大能源危机，并推高全球能源价格。 胡塞武装的封锁是在伊朗此前威胁海湾航运之后发生的，目前只有苏伊士运河完全开放供海湾石油运输。曼德海峡是连接红海和亚丁湾的主要全球瓶颈。

rss · The Guardian World · Jul 28, 01:37

**背景**: 曼德海峡是也门与吉布提/厄立特里亚之间的狭窄水道，全球大量石油运输经过此地。胡塞武装是与伊朗结盟的组织，自 2023 年底以来一直在红海袭击船只，宣布与以色列有关的船只为目标。另一个关键瓶颈霍尔木兹海峡已于 2026 年早些时候关闭，加剧了供应中断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bab_el-Mandeb_Strait">Bab el-Mandeb Strait</a></li>
<li><a href="https://en.wikipedia.org/wiki/Red_Sea_crisis">Red Sea crisis - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/world/2026/jul/21/houthis-threaten-attack-tankers-saudi-arabian-ports-red-sea-shipping">Houthis threaten to attack shipping tankers if they use Saudi Arabian ports on Red Sea | Houthis | The Guardian</a></li>

</ul>
</details>

**标签**: `#energy`, `#geopolitics`, `#oil`, `#Asia`, `#Houthi`

---

<a id="item-3"></a>
## [美方在军方建议后暂停对伊朗打击](https://www.theguardian.com/world/2026/jul/26/us-pauses-trump-netanyahu-attacks-on-iran-talks-hormuz) ⭐️ 9.0/10

美国暂停了对伊朗的轰炸行动，此前高级军方官员向特朗普总统建议，打击行动的效果已到极限且弹药储备不足，导致周一油价下跌。 此次暂停标志着可能缓和一场直接影响全球能源市场的重大地缘政治冲突，油价已因此下跌，并可能降低该地区全面战争的风险。 暂停发生在打击行动的第三晚，外交谈判仍在进行以避免全面战争；这一决定更多基于军事评估而非政治考量。

rss · The Guardian World · Jul 27, 06:33

**背景**: 美国与伊朗长期关系紧张，尤其在伊朗核计划及地区影响力方面。最近的轰炸行动是针对据称伊朗对美国资产及盟友的袭击而发起的。暂停行动反映了对军事可持续性和有效性的担忧。

**标签**: `#geopolitics`, `#Iran`, `#US foreign policy`, `#oil`, `#military`

---

<a id="item-4"></a>
## [OpenAI Agents SDK v0.19.0 新增程序化工具调用](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0) ⭐️ 8.0/10

OpenAI 发布了 openai-agents-python SDK 的 v0.19.0 版本，引入了 ProgrammaticToolCallingTool，使模型能够生成并执行 JavaScript 来编排工具。此版本还新增了 @tool 装饰器别名、改进的 SDK 配置以及更安全的日志记录。 程序化工具调用代表了 AI 代理与工具交互方式的范式转变，使模型能够编写代码来协调工具调用，支持循环、条件判断和并行执行。这使得代理工作流更加灵活和强大，可能减少复杂任务所需的模型调用轮次。 新工具支持每个工具的 allowed_callers、结构化函数工具输出，并与 Runner 流式、护栏、审批、会话和 RunState 集成。它使用托管 JavaScript 运行时作为 Responses API 的一部分，相关约束在官方指南中有说明。

github · seratch · Jul 27, 04:10

**背景**: OpenAI Agents SDK 是一个 Python 框架，用于使用 Responses API 构建 AI 代理工作流。它提供了工具调用、移交、护栏和追踪的运行时。程序化工具调用扩展了这一点，允许模型生成 JavaScript 来在单轮中编排多个工具调用，而不是进行顺序的工具调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling">Programmatic Tool Calling | OpenAI API</a></li>
<li><a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK</a></li>

</ul>
</details>

**标签**: `#openai`, `#python`, `#ai-agents`, `#tool-calling`, `#sdk`

---

<a id="item-5"></a>
## [Anthropic 支持对开源权重模型进行安全测试](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic 发布了官方立场，声明不主张禁止开源权重模型，而是要求对所有足够强大的模型（无论是开源还是闭源）进行强制性安全测试。 这一立场意义重大，它将 Anthropic 置于 AI 监管辩论的中心，可能影响政策制定，同时招致开源倡导者的批评，他们认为强制性测试实际上是变相禁止。 据报道，Anthropic CEO Dario Amodei 支持禁止向中国销售芯片和打击走私等措施，批评者认为这与该公司声称不主张禁令的说法相矛盾。

hackernews · surprisetalk · Jul 27, 22:03

**背景**: 开源权重模型是指其训练参数（即权重）公开可下载的 AI 模型，允许任何人自行运行、微调或修改。这与权重保密的闭源模型形成对比。争论的核心在于平衡创新与安全，因为开源模型可能被滥用，但也促进了更广泛的访问和研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open-Weights Model? | AI21</a></li>
<li><a href="https://telnyx.com/resources/open-weight-models">Open Weight Models What They Are and How to Use Them</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 Anthropic 的立场持高度批评态度。评论者如 cogman10 认为，鉴于测试成本和管理权问题，强制性测试实际上是一种禁令。其他人如 vhantz 和 m3h 指责 Anthropic 虚伪且出于利润动机。GodelNumbering 指出 Anthropic 在禁令和对中国芯片销售问题上的立场不一致。

**标签**: `#AI policy`, `#open-weights`, `#AI safety`, `#Anthropic`, `#regulation`

---

<a id="item-6"></a>
## [沃尔沃/艾歇尔车队平台遭入侵，账户可完全接管](https://eaton-works.com/2026/07/27/my-eicher-hack/) ⭐️ 8.0/10

一名安全研究员披露了 VE Commercial Vehicles 的 My Eicher 车队管理平台存在严重漏洞，攻击者可接管任意用户账户，并控制所有关联车辆和车队。 该漏洞可能让恶意行为者远程追踪、禁用或操控整个车队，给物流公司和驾驶员带来重大安全与运营风险。同时，它也凸显了联网汽车行业面临的安全挑战以及及时披露漏洞的重要性。 该漏洞存在于 My Eicher 平台的 API 中，可实现无需认证的账户接管。研究员于 2025 年 11 月 3 日首次报告，但在 11 月 20 日之前未获回应，随后 API 访问被封锁；完整披露于 2026 年 7 月 27 日公布。

hackernews · EatonZ · Jul 27, 15:08

**背景**: My Eicher 是沃尔沃集团与艾歇尔汽车合资公司 VE Commercial Vehicles 推出的车队管理平台，通过云端 API 提供实时车辆跟踪、诊断与控制功能。此类联网车辆平台日益普及，但若安全防护不足，常会引入安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eaton-works.com/2026/07/27/my-eicher-hack/">Exploiting Volvo/Eicher’s fleet management platform to gain control over all users and vehicles</a></li>

</ul>
</details>

**社区讨论**: 评论者对漫长的披露时间和厂商最初未回应表示不满。有人指出车辆对云端依赖这一更广泛的问题，并提及因连接问题导致汽车无法启动的事件。还有人区分了保护用户的安全与保护公司的‘安全剧场’。

**标签**: `#security`, `#vulnerability`, `#connected vehicles`, `#disclosure`, `#IoT`

---

<a id="item-7"></a>
## [法官驳回谷歌利用 DMCA 阻止数据抓取的尝试](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) ⭐️ 8.0/10

一名法官裁定谷歌不能利用《数字千年版权法》（DMCA）来阻止对其搜索结果的抓取，驳回了该公司的法律论据。 这一裁决影响了 AI 训练、市场竞争和网络抓取的合法性，可能限制谷歌控制其公开搜索结果使用的能力。 该裁决澄清了搜索结果不属于 DMCA 下的可版权汇编，且单独的数据抓取不构成版权侵权。

hackernews · cdrnsf · Jul 27, 18:15

**背景**: DMCA 是美国版权法，包含反规避条款。谷歌曾辩称，抓取绕过其保护版权数据库的技术措施。法院不予采纳，指出搜索结果缺乏原创性。

**社区讨论**: 评论者意见不一：有人欢迎这一裁决，认为是对谷歌权力的制衡；也有人指出谷歌自身靠爬取起家的讽刺意味，并提出了对缺乏官方 API 的担忧。

**标签**: `#legal`, `#scraping`, `#copyright`, `#Google`, `#DMCA`

---

<a id="item-8"></a>
## [Bun 的 Rust 重写已在 Claude Code 中发布，公开版本延迟](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 8.0/10

Bun 的 Rust 重写已于一个多月前在 Claude Code 中发布，但 Bun v1.4 的独立公开版本因未达到新设定的 Node.js 测试兼容性目标而延迟。 这次重写展示了 AI 辅助翻译如何加速重大软件重构，并且在 Claude Code 这样的广泛使用的工具中部分部署，证明了其实战生产的就绪程度。延迟则突显了在采用新的实现语言时保持与 Node.js 兼容性的挑战。 Bun 的创建者 Jarred 提到，Rust 重写已在 Claude Code 中悄悄发布，v1.4 版本与一个特定数量的新增通过的 Node.js 测试挂钩，目前尚未达标。相关 PR 已提交但未合并，预计下周二发布。

hackernews · tomlockwood · Jul 27, 11:12

**背景**: Bun 是一个全栈 JavaScript 运行时，设计为 Node.js 的即插即用替代品，以速度快著称。最初用 Zig 编写，该项目正在使用 AI 代码生成进行 Rust 重写。Claude Code 是 Anthropic 推出的智能编码工具，能编辑代码和运行命令，内部已采用了基于 Rust 的 Bun。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>

</ul>
</details>

**社区讨论**: 社区评论观点多样：有人承认这类重写的难度和稳定所需的时间，也有人质疑完全重写的必要性，指出原始 Zig 代码库的问题本可修复。还有人对使用 LLM 进行此类翻译持怀疑态度，认为会带来下游 bug 和 UI 工作。

**标签**: `#bun`, `#rust`, `#javascript runtime`, `#claude code`, `#software rewrite`

---

<a id="item-9"></a>
## [NVIDIA Cosmos-H-Dreams 实现实时手术模拟](https://huggingface.co/blog/nvidia/cosmos-h-dreams) ⭐️ 8.0/10

NVIDIA 推出了 Cosmos-H-Dreams，这是一个面向手术机器人的实时、动作条件生成式模拟器，能够根据实时的机器人指令生成逼真的手术视频。 该技术能够即时生成高保真模拟，从而极大加速手术 AI 系统的开发与测试，有望降低医疗机器人的成本并提升安全性。 Cosmos-H-Dreams 基于之前的 Cosmos 平台构建，并将其扩展至手术领域，可根据机器人动作生成视频序列，实现比物理环境更快速的评估。

rss · Hugging Face Blog · Jul 27, 09:32

**背景**: 生成式模拟利用在大型视觉数据集上训练的 AI 模型，实时创建逼真的视频帧，取代了手动设计的世界模型。在机器人领域，此类模拟器允许在无需物理硬件的情况下进行虚拟训练和测试，从而减少时间和风险。NVIDIA 的 Cosmos-Dreams 系列此前专注于自动驾驶，而 Cosmos-H-Dreams 现在将同样的概念应用于手术机器人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/cosmos-h-dreams">NVIDIA Cosmos-H-Dreams: Bringing Real-Time Generative Simulation to Surgical Robotics</a></li>
<li><a href="https://cornfordandcross.com/healthcare-operations/unlocking-real-time-generative-simulation-in-surgical-ai-using-nvidia-technologi/">Unlocking Real-Time Generative Simulation In Surgical AI Using NVIDIA Technologies - Cornford and Cross</a></li>

</ul>
</details>

**标签**: `#AI`, `#robotics`, `#surgical robotics`, `#generative simulation`, `#NVIDIA`

---