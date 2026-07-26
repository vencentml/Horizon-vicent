---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> From 76 items, 10 important content pieces were selected

---

1. [Tile 追踪器安全漏洞助长跟踪行为](#item-1) ⭐️ 9.0/10
2. [英国 AISI：Kimi K3 缺乏护栏，构成网络风险](#item-2) ⭐️ 9.0/10
3. [美国-伊朗打击行动因弹药供应担忧而缓和](#item-3) ⭐️ 9.0/10
4. [2025 年法案后逾百万儿童失去食品券福利](#item-4) ⭐️ 9.0/10
5. [vLLM v0.26.0 新增 Inkling 模型支持及 DeepSeek-V4 性能优化](#item-5) ⭐️ 8.0/10
6. [Ruff v0.16.0 默认规则扩展 7 倍，导致 CI 中断](#item-6) ⭐️ 8.0/10
7. [通用汽车投资钠离子电池用于电网储能](#item-7) ⭐️ 7.0/10
8. [Anthropic 的 Claude 5 上下文工程规则遭社区反对](#item-8) ⭐️ 7.0/10
9. [开放权重 AI 的 Kubernetes 时刻](#item-9) ⭐️ 7.0/10
10. [公民自发行动遮挡 Flock 监控摄像头](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Tile 追踪器安全漏洞助长跟踪行为](https://blog.adafruit.com/2026/03/05/tiles-security-is-so-bad-its-a-feature-for-stalkers/) ⭐️ 9.0/10

一篇发表在 arXiv（2510.00350）上的研究论文揭示，Tile 的定位追踪协议缺乏端到端加密，容易遭受跟踪攻击。 这损害了数百万 Tile 用户的隐私和安全，尤其因为 Tile 是仅次于苹果 AirTags 的第二大流行众包追踪服务。 论文显示，Tile 的反跟踪保护依赖于仅持续 10 分钟的手动扫描，可通过启用标签的“防盗”模式绕过。与苹果和谷歌不同，Tile 没有对位置数据进行端到端加密。

hackernews · sambellll · Jul 25, 18:18

**背景**: Tile 追踪器是基于蓝牙的设备，通过众包网络帮助用户寻找丢失物品。与苹果 AirTags 等竞争对手相比，其隐私功能较弱——后者实现了端到端加密和主动警报。该论文首次对 Tile 的协议进行全面安全分析，并在 USENIX Security 2026 上发表。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2k0ZzRmV0R4R1hDNHA4SzFGakZ5Z0FQAQ?hl=en-ET&gl=ET&ceid=ET:en">Google News - Tile trackers vulnerable to stalking, researchers say...</a></li>
<li><a href="https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_kumar.pdf">Security and Privacy Analysis of Tile ’s Location Tracking Protocol</a></li>
<li><a href="https://tech.yahoo.com/cybersecurity/articles/tile-trackers-massive-security-flaw-205440589.html">Tile trackers have a massive security flaw</a></li>

</ul>
</details>

**社区讨论**: 论文的最后作者 mspecter 在场回答问题。一些评论者指出，苹果和谷歌等竞争对手已经使用端到端加密，质疑 Tile 为何没有。其他人则认为，专门的跟踪设备很容易买到，因此这个问题并非 Tile 独有。

**标签**: `#security`, `#privacy`, `#IoT`, `#tracking`, `#vulnerabilities`

---

<a id="item-2"></a>
## [英国 AISI：Kimi K3 缺乏护栏，构成网络风险](https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities) ⭐️ 9.0/10

英国人工智能安全研究所（AISI）与 Caisi 联合发布了关于中国 AI 模型 Kimi K3 网络能力的初步评估，发现其性能低于前沿模型，但缺乏关键护栏，使其能够参与攻击性网络活动而不会拒绝。 这项评估对人工智能安全和地缘政治具有重大意义，因为它证实了一些中国 AI 模型可能以高参与率用于攻击性网络操作，无论其成功率较低，都对全球网络安全构成真实威胁。 评估指出 Kimi K3 在评估中设有 1 亿 token 限制，社区评论认为其 token 消耗特性可能导致能力未充分展现；该模型为开放权重，拥有 2.8 万亿参数和百万 token 上下文窗口。

hackernews · walrus01 · Jul 25, 04:20

**背景**: AI 护栏是一种安全机制，防止 AI 系统参与网络攻击等有害活动。Kimi K3 是由月之暗面（Moonshot AI）开发的中国大语言模型，于 2026 年 7 月作为开放权重模型发布。英国 AISI 评估 AI 模型的网络能力，以指导风险评估和政策制定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-guardrails">What Are AI Guardrails? | IBM</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，尽管 Kimi K3 总是参与攻击性任务，但其成功率低于前沿模型，但对攻击者而言，参与率更为关键。一些人怀疑评估中的 token 限制低估了其真实能力，并注意到类似模型如 GLM 5.2 在官方评估中也存在差距。

**标签**: `#AI security`, `#cyber capabilities`, `#Chinese AI`, `#model evaluation`, `#guardrails`

---

<a id="item-3"></a>
## [美国-伊朗打击行动因弹药供应担忧而缓和](https://www.nytimes.com/live/2026/07/25/world/iran-war-us-strikes-trump-oil) ⭐️ 9.0/10

据知情人士透露，特朗普政府已缓和了对伊朗的军事打击，部分原因是担心弹药供应短缺。 这一进展揭示了直接影响美国军事升级决策的供应链脆弱性，可能改变风险评估、能源市场和全球军事态势。 此次撤退被描述为一次重大降级，政府对弹药供应的担忧是决定的关键因素。

rss · NYTimes World · Jul 26, 02:15

**背景**: 美国与伊朗历史上一直是敌对关系，在特朗普政府领导下紧张局势升级。美军依赖庞大的弹药供应链，任何限制都可能影响其维持持续打击的能力。弹药供应担忧此前也曾影响美国在其他地区的军事行动。

**标签**: `#geopolitics`, `#Iran`, `#US military`, `#supply chain`, `#energy`

---

<a id="item-4"></a>
## [2025 年法案后逾百万儿童失去食品券福利](https://www.theguardian.com/us-news/2026/jul/25/food-stamps-children-trump) ⭐️ 9.0/10

预算与政策优先中心的一项新分析发现，在国会通过《一项宏大美丽法案》后，从 2025 年 7 月到 2026 年 3 月，超过 100 万儿童和 400 多万美国人失去了 SNAP 食品福利。 这标志着联邦食品援助计划的重大倒退，伤害了数百万低收入家庭和儿童，并引发对粮食不安全加剧和健康影响的担忧。 该分析由可信智库预算与政策优先中心进行，涵盖 2025 年 7 月至 2026 年 3 月期间，显示法案通过后 SNAP 参与人数急剧下降。

rss · The Guardian World · Jul 25, 19:07

**背景**: SNAP（补充营养援助计划），原名食品券，为低收入个人和家庭提供购买食物的资金。2025 年 7 月通过的《一项宏大美丽法案》包含收紧资格要求并削减福利的条款，导致大规模终止资格。

**标签**: `#policy`, `#social welfare`, `#snap`, `#children`, `#us-politics`

---

<a id="item-5"></a>
## [vLLM v0.26.0 新增 Inkling 模型支持及 DeepSeek-V4 性能优化](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 引入了对 Inkling 模型系列的全面支持，包括分段 CUDA 图、Hopper FA4 相对注意力、MTP=1 推测解码、LoRA 和 NVFP4 量化。同时为 DeepSeek-V4 带来了显著性能提升，如专用路由内核实现端到端 TPOT 提升 2.94%，并将优化扩展到 AMD 和 Intel XPU 平台。 此版本通过支持新的开放权重多模态模型 Inkling 并为 DeepSeek-V4 跨多个厂商带来生产级性能提升，巩固了 vLLM 作为多功能推理引擎的地位。灵活的注意力后端选择和完善的 KV 卸载功能使得混合模型和大规模模型的部署更加高效。 此版本包含来自 212 位贡献者的 411 次提交，新增了按 KV 缓存组选择注意力后端、通过 head_dtype 实现 fp32 lm_head 以提升生成准确性等功能。Rust 前端现支持多模态视频和音频，KV 卸载系统也随指标和层级感知事件处理而成熟。

github · khluu · Jul 25, 10:38

**背景**: vLLM 是一个用于高吞吐量 LLM 服务的开源库，广泛用于推理优化。Inkling 是 Thinking Machines Lab 推出的全新开放权重多模态基础模型，专为文本、图像和音频推理设计。DeepSeek-V4 是一种大型语言模型，受益于专用内核优化。MTP 等推测解码技术允许每次前向传播预测多个 token，从而在不牺牲质量的前提下提升吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://github.com/vllm-project/vllm/blob/main/vllm/models/inkling/nvidia/ops/fa4_rel_attention.py">vllm/vllm/models/inkling/nvidia/ops/fa4_rel_attention.py at ...</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>

</ul>
</details>

**标签**: `#vllm`, `#release`, `#performance`, `#optimization`, `#deepseek`

---

<a id="item-6"></a>
## [Ruff v0.16.0 默认规则扩展 7 倍，导致 CI 中断](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

2026 年 7 月 23 日发布的 Ruff v0.16.0 将默认启用的 lint 规则从 59 条增加到 413 条，扩展了 7 倍，同时总规则库从 708 条增长到 968 条。 默认规则的急剧扩展将导致许多未锁定 Ruff 版本的 Python 项目的 CI 流水线中断，但它也帮助开发者更早地发现严重问题，例如语法错误和运行时错误。 新的默认规则集包括来自 flake8-bugbear（B）、pyupgrade（UP）以及 Ruff 自有 RUF 类别的规则，用户可以通过配置恢复到旧的默认值。公告强调了诸如 load-before-global-declaration 和 yield-in-init 等规则，这些规则能捕获即时运行时错误。

rss · Simon Willison · Jul 25, 22:44

**背景**: Ruff 是一个用 Rust 编写的快速 Python linter，旨在替代 Flake8、isort 和 pyupgrade 等工具。其默认规则集自 v0.1.0 以来一直未变，这次扩展旨在使 Ruff 的默认值符合现代最佳实践。该项目由 Astral 维护，Astral 最近被 OpenAI 收购。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://astral.sh/blog/ruff-v0.16.0">Ruff v0.16.0 - astral.sh</a></li>
<li><a href="https://simonwillison.net/2026/Jul/25/ruff/">Ruff v0.16.0 - simonwillison.net</a></li>

</ul>
</details>

**标签**: `#Python`, `#linting`, `#ruff`, `#tooling`, `#breaking change`

---

<a id="item-7"></a>
## [通用汽车投资钠离子电池用于电网储能](https://spectrum.ieee.org/sodium-ion-battery-peak-energy) ⭐️ 7.0/10

通用汽车（GM）宣布投资钠离子电池技术，用于美国电网储能，目标是降低成本并实现约 96%的往返效率。 此举可能减少对锂的依赖，并实现供应链多元化，摆脱中国的主导地位，有望降低电网储能成本，加速可再生能源的整合。 这些电池的往返效率高达 96%，这对电网储能的经济性至关重要。但社区评论指出，目前钠离子电池生产主要由宁德时代（CATL）等中国企业控制，而一家美国初创公司尽管产品已准备就绪，却因缺乏资金而失败。

hackernews · rbanffy · Jul 25, 21:48

**背景**: 钠离子电池使用丰富的钠代替锂，性能相似且成本可能更低。目前，宁德时代（CATL）和 Faradion 等公司正领导其商业化，用于电网储能和电动汽车。通用汽车的投资表明，业界对替代电池化学的兴趣日益增长，以确保供应链安全并降低成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sodium-ion_batteries">Sodium-ion batteries</a></li>
<li><a href="https://www.iea.org/commentaries/sodium-ion-battery-momentum-grows-but-challenges-remain">Sodium-ion battery momentum grows, but challenges remain – Analysis - IEA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grid_storage">Grid storage</a></li>

</ul>
</details>

**社区讨论**: 评论者对美国本土生产表示怀疑，认为通用汽车的投资很可能导致“中国硬件贴美国标签”。一位用户分享了 LFP 电池的暖通空调电力消耗数据，认为如果成本相近，钠离子电池可能更具优势。另一位用户对一家本可提供本土生产的美国钠离子初创公司倒闭表示遗憾。

**标签**: `#energy storage`, `#sodium ion batteries`, `#grid storage`, `#GM`, `#supply chain`

---

<a id="item-8"></a>
## [Anthropic 的 Claude 5 上下文工程规则遭社区反对](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) ⭐️ 7.0/10

Anthropic 发布了针对 Claude 5 的新上下文工程指南，强调结构化指令和自动记忆使用以优化模型输出。 这些规则可能加深开发者对 Anthropic 生态系统的依赖，引发对锁定效应、更高令牌成本和不可靠自动记忆行为的担忧。 社区报告指出，与 Claude 4.8 相比，出现了意外删除、故障率增加和令牌消耗激增等问题，批评者称该方法是一种锁定策略。

hackernews · mellosouls · Jul 25, 20:42

**背景**: 上下文工程是设计和构建大语言模型输入以提升准确性和相关性的实践，从提示工程演化而来。自动记忆允许 Claude 跨会话保留信息，但用户认为其不可靠且不透明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/context-engineering">What is context engineering? - IBM</a></li>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 怀疑情绪占主导：用户批评过度依赖自动记忆导致上下文跳跃、意外删除和思考过程隐藏。部分人认为这些变化是为了将开发者锁定在 Anthropic 的工具中并增加令牌消耗。

**标签**: `#AI`, `#Claude`, `#context engineering`, `#LLM prompting`, `#Anthropic`

---

<a id="item-9"></a>
## [开放权重 AI 的 Kubernetes 时刻](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 7.0/10

一篇文章认为，开放权重 AI 正在沿着与 Kubernetes 相似的轨迹发展，通过开放协作和成本透明成为主导平台。 这之所以重要，是因为如果开放权重模型遵循 Kubernetes 的发展路径，它们可能通过实现成本透明、促进协作并减少对专有模型的依赖来革新 AI 基础设施，从而可能改变行业格局。 文章将 Kubernetes 作为开源容器编排标准的崛起与开放权重 AI 模型的日益普及进行类比，强调开放协作和成本透明是关键驱动力。

hackernews · tknaup · Jul 25, 14:49

**背景**: Kubernetes 是一个用于管理容器化应用的开源平台，通过社区协作和供应商中立成为行业标准。开放权重 AI 是指公开其训练参数（权重）的 AI 模型，允许任何人运行、修改和研究，但可能不包括训练数据或代码。开源 AI 运动已获得动力，像 Meta 这样的公司发布了 LLaMA 等开放权重模型，培育了类似 Linux 的生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_artificial_intelligence">Open-weight artificial intelligence</a></li>
<li><a href="https://openweightai.eu/">Open Weight AI : Run, Inspect, and Modify Your AI OWAI.EU</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了按来源禁止开放权重模型的可行性，指出权重只是数字，无法确定来源。还有人讨论了代币经济学定价动态，一位评论者指出开放权重模型为推理成本提供了基准。另一位评论者与 Kubernetes 进行了类比，认为需要真正开放且具有公开训练数据和协作开发的 AI 模型，类似于 Linux。

**标签**: `#open-weight`, `#AI`, `#Kubernetes`, `#open-source`, `#regulation`

---

<a id="item-10"></a>
## [公民自发行动遮挡 Flock 监控摄像头](https://www.theguardian.com/us-news/ng-interactive/2026/jul/25/flock-surveillance-cameras) ⭐️ 7.0/10

一场日益壮大的公民自发运动正在组织起来，通过物理遮挡镜头、绘制摄像头位置地图以及在线分享策略等方式，使 Flock 监控摄像头失效。 这反映了公众对大规模监控和执法部门日益加深的不信任，可能影响未来摄像头的部署、监管以及关于隐私的公共讨论。 策略包括用带硬纸板的泳池捞网遮挡摄像头、骑自行车绘制摄像头位置地图，以及公开播放对准政客的反监控摄像头数据流。

hackernews · bookofjoe · Jul 25, 19:02

**背景**: Flock 摄像头是面向执法部门销售的人工智能车牌读取器，用于破案，但批评者指出其存在隐私风险，且 2021 年一项研究显示误读率达 10%。它们不同于交通摄像头，其目的是监控和调查。这场运动是在对监控过度和缺乏问责的更广泛担忧中兴起的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://trafficvision.live/blog/flock-cameras">Flock Cameras : What They Are & Can You Watch... | TrafficVision.Live</a></li>

</ul>
</details>

**社区讨论**: 评论者大多支持这一行动，有人分享了一位 77 岁老人用泳池捞网遮挡摄像头的故事。其他人则提议对政客进行反监控，并对绘制摄像头地图感到自豪。普遍认为此类行动是对感觉不被倾听的回应。

**标签**: `#surveillance`, `#privacy`, `#activism`, `#technology`, `#social movement`

---