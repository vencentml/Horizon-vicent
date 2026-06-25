---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> From 123 items, 10 important content pieces were selected

---

1. [OpenAI 携手博通推出首款自研 AI 推理芯片](#item-1) ⭐️ 9.0/10
2. [高通以 40 亿美元收购 Modular，挑战英伟达](#item-2) ⭐️ 9.0/10
3. [NSA 在争议中失去对 Mythos 的访问权限](#item-3) ⭐️ 9.0/10
4. [联合国批准首个全球自动驾驶车辆法规](#item-4) ⭐️ 9.0/10
5. [联合国报告：政府军成为侵害儿童首要施暴者](#item-5) ⭐️ 9.0/10
6. [NVIDIA 的 45°C 液冷设计将数据中心用水降至接近零](#item-6) ⭐️ 8.0/10
7. [Kubernetes v1.37.0-alpha.2 发布](#item-7) ⭐️ 7.0/10
8. [crates.io 发布仍依赖 GitHub 的问题未解决](#item-8) ⭐️ 7.0/10
9. [工程师用 Claude 重写 SQL 解析器，实现 70 倍加速](#item-9) ⭐️ 7.0/10
10. [Claude Slackbot 获得多人、主动、持久升级](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 携手博通推出首款自研 AI 推理芯片](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 发布了其首款自研 AI 推理芯片 Jalapeño，该芯片由 OpenAI 与博通合作开发，并由台积电制造，从设计到生产仅用时九个月。 这标志着 OpenAI 在 AI 硬件领域向垂直整合迈出重大战略一步，可能降低其对英伟达等 GPU 供应商的依赖，并提升推理成本效率，有望重塑供应链格局并为其他 AI 公司树立先例。 该芯片代号 Jalapeño，是一款针对大语言模型加速的推理芯片，着重优化每瓦性能。早期测试显示其每瓦性能显著优于现有方案，但最终性能指标仍在测量中。

hackernews · jamdesk · Jun 24, 17:47

**背景**: AI 芯片是专为机器学习负载设计的处理器。推理芯片专注于运行训练好的模型进行预测，而训练芯片则用于模型训练。此前，OpenAI 在训练和推理环节均依赖英伟达等厂商的 GPU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/forums/threads/openai-unveils-jalapeno-llm-inferencing-accelerator-built-in-collaboration-with-broadcom.350253/">OpenAI Unveils Jalapeno LLM Inferencing Accelerator Built in ...</a></li>
<li><a href="https://www.reddit.com/r/singularity/comments/1ueej55/openai_and_broadcom_unveil_llmoptimized_inference/">OpenAI and Broadcom unveil LLM-optimized inference chip - Reddit</a></li>

</ul>
</details>

**社区讨论**: 评论者对 OpenAI 声称其模型加速了芯片设计表示好奇，并怀疑这可能是营销噱头。其他人则指出制造商是台积电（而非英特尔），并讨论了将权重固化到 ROM 中以实现巨大吞吐量的架构想法。

**标签**: `#OpenAI`, `#Broadcom`, `#AI chip`, `#inference`, `#vertical integration`

---

<a id="item-2"></a>
## [高通以 40 亿美元收购 Modular，挑战英伟达](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 9.0/10

高通于 2026 年 6 月 24 日宣布以 40 亿美元收购 Modular，该公司是 Mojo 编程语言和 MAX 编译器栈的开发商，官方新闻稿已确认此交易。 此次收购将高通的 ARMv9 芯片设计与 Modular 的 CUDA 替代编译器栈相结合，直接挑战英伟达在 AI 推理领域的主导地位，可能降低大规模 AI 部署的成本。 该交易价值 40 亿美元，高通计划将 Modular 的 MAX 框架和 Mojo 语言与其 ARMv9 处理器集成，打造统一的 AI 推理平台。

hackernews · timmyd · Jun 24, 13:49

**背景**: Modular 的 Mojo 语言是一种高性能编程语言，基于 MLIR 编译器框架，能够高效生成 CPU、GPU 及其他加速器的代码。其 MAX 编译器栈提供了 CUDA 兼容的 AI 推理替代方案，使模型可在非英伟达硬件上运行。高通一直在向 AI 和云计算领域多元化发展，包括投资 RISC-V 和 Tenstorrent。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://www.modular.com/max">MAX: A high-performance inference framework for AI</a></li>
<li><a href="https://docs.modular.com/max/intro/">What is Modular | Modular</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，中国 LineShine 超级计算机最近使用 ARMv9 芯片（无 GPU）获得 Top500 第一，高通的收购与这一趋势一致。其他人对 Mojo 的发展持复杂态度，有人认为 Chris Lattner 的精力本可更好地利用，同时赞扬高通包括 RISC-V 和 Tenstorrent 在内的大胆战略举措。

**标签**: `#acquisition`, `#AI`, `#compiler`, `#Qualcomm`, `#ARM`

---

<a id="item-3"></a>
## [NSA 在争议中失去对 Mythos 的访问权限](https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html) ⭐️ 9.0/10

由于合同纠纷，NSA 失去了对 Anthropic 先进 AI 工具“Mythos”的访问权限，有报道称 Mythos 能在数小时内攻破机密系统。 这一事件凸显了领先 AI 实验室与政府情报机构之间日益紧张的关系，揭示了 AI 治理、供应链安全以及国家安全领域中权力平衡的关键问题。 Mythos 是 Anthropic 的 Project Glasswing 项目的一部分，在红队测试中被发现“在计算机安全任务上表现惊人”。与 NSA 的机密合同尚未最终敲定，一些五角大楼官员正在探索替代模型。

hackernews · thm · Jun 24, 11:45

**背景**: Mythos 是一个先进的 AI 工具，专为自主渗透测试和漏洞发现而设计，能够执行通常需要人类专家完成的任务。它代表了 AI 从辅助人类到主动调查和与关键系统交互的转变。NSA 试图获取访问权限以增强情报分析和检测计算机漏洞，但这场争议揭示了控制与风险之间的紧张关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/crk1py1jgzko">What is Anthopic's Claude Mythos and what risks does it pose?</a></li>
<li><a href="https://www.smartcompany.com.au/artificial-intelligence/what-is-anthropic-mythos-ai/">What does Anthropic 's Mythos AI actually do?</a></li>

</ul>
</details>

**社区讨论**: 评论者对政府将 AI 既视为供应链风险又强制要求访问的矛盾立场表示讽刺。一些人批评 NSA 的参与，有评论者称该机构的无能可能阻止其重新获得访问权限，而另一些人则警告该工具的潜在危险。

**标签**: `#NSA`, `#Anthropic`, `#AI security`, `#intelligence`, `#contract dispute`

---

<a id="item-4"></a>
## [联合国批准首个全球自动驾驶车辆法规](https://news.un.org/feed/view/en/story/2026/06/1167797) ⭐️ 9.0/10

联合国车辆法规协调世界论坛已批准首个针对完全自动驾驶系统（ADS）的全球性法规。该法规框架为无人类驾驶员的无人驾驶车辆制定了安全标准和性能要求。 这些法规提供了统一的国际标准，将加速自动驾驶车辆在多个国家的安全部署。制造商现在可以按照单一的全球规则进行设计，从而降低合规成本并加快市场导入。 该法规涵盖能够在无需任何人类干预下运行的完全自动驾驶系统（SAE L4 和 L5 级别）。法规包括功能安全、网络安全和数据记录的要求，以及测试和批准的程序。

rss · UN News · Jun 24, 12:00

**背景**: 自动驾驶车辆按从 0 级到 5 级划分，其中 5 级代表在所有条件下的完全自动化。在此联合国裁决之前，各国已开始制定各自独立的法规，造成标准碎片化，阻碍了全球部署。车辆法规协调世界论坛（WP.29）隶属于联合国欧洲经济委员会（UNECE），此前已为高级驾驶辅助系统（ADAS）制定了法规。这一新框架是首个专门针对无人类驾驶员车辆的法规。

**标签**: `#autonomous vehicles`, `#regulation`, `#UN`, `#global standards`, `#safety`

---

<a id="item-5"></a>
## [联合国报告：政府军成为侵害儿童首要施暴者](https://news.un.org/feed/view/en/story/2026/06/1167795) ⭐️ 9.0/10

联合国安理会辩论了 30 年来首份报告，显示 2025 年政府军在武装冲突中侵犯儿童的程度超过了非国家武装团体，核实了 38558 起严重侵犯行为，涉及 24174 名儿童。 这一历史性转变挑战了非国家行为体是儿童主要威胁的传统假设，可能重塑国际政策、制裁机制和人道主义应对，加强对政府军的问责。 联合国在 2025 年核实了 38558 起严重侵犯行为，包括杀害、招募和绑架，许多儿童遭受多重侵犯。该报告标志着联合国监测儿童与武装冲突 30 年来的一个转折点。

rss · UN News · Jun 24, 12:00

**背景**: 自 1990 年代中期以来，联合国监测冲突中的六种严重侵犯儿童行为：杀害/致残、招募、性暴力、绑架、袭击学校/医院以及拒绝人道准入。历史上，非国家武装团体应对大多数侵犯负责，但 2025 年的数据显示政府军首次超过他们。

**标签**: `#geopolitics`, `#human rights`, `#policy`, `#UN`, `#conflict`

---

<a id="item-6"></a>
## [NVIDIA 的 45°C 液冷设计将数据中心用水降至接近零](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA 推出了一种针对 AI 数据中心的 45°C 液冷架构，大幅降低用水量，并可能集成到区域供暖系统中。 这项创新解决了 AI 数据中心日益增长的用水和能源需求，提供了近乎零用水的路径，并可将废热用于社区供暖，从而降低运营成本和环境影响。 该设计采用直接到芯片的液冷，冷却液温度达 45°C，远高于传统系统。在有利气候下无需压缩机冷却即可高效运行，且 45°C 的废热适合用于区域供暖网络。

hackernews · nitin_flanker · Jun 24, 14:10

**背景**: 传统数据中心冷却消耗大量水和能源。液冷比风冷更高效，但通常运行在较低温度。区域供暖网络将中央热源的热量分配给建筑。将数据中心废热集成到这些网络中可以节省能源并减少碳排放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techbuzz.ai/articles/nvidia-s-45-c-liquid-cooling-redefines-ai-data-center-energy">NVIDIA's 45°C Liquid Cooling Redefines AI Data Center ...</a></li>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers">NVIDIA Unveils 45°C Liquid Cooling Design for AI Data Centers</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1364032125005362">Data center waste heat for district heating networks: A review - ScienceDirect</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了区域供暖协同的潜力，有人指出 45°C 适用于区域供暖回路，可为当地社区带来价值。也有人担忧更高温度的碳足迹以及效率对有利气候的依赖。

**标签**: `#data-center`, `#cooling`, `#liquid-cooling`, `#water-conservation`, `#NVIDIA`

---

<a id="item-7"></a>
## [Kubernetes v1.37.0-alpha.2 发布](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0-alpha.2) ⭐️ 7.0/10

Kubernetes 发布了其即将到来的次要版本 v1.37 的第二个 alpha 版本，标签为 v1.37.0-alpha.2。 Alpha 版本允许社区在稳定版发布前尽早测试新功能并提供反馈，这影响 Kubernetes 用户及生态系统工具。 该版本包含一个变更日志，详细列出了更改、错误修复和新功能，可通过 Kubernetes CHANGELOG-1.37.md 文件查看。

github · k8s-release-robot · Jun 25, 02:40

**背景**: Kubernetes 采用语义化版本控制；v1.37.0-alpha.2 表示 1.37 主版本线的预发布版本。Alpha 版本可能包含不完整或不稳定的功能，旨在用于测试和开发。

**标签**: `#kubernetes`, `#release`, `#infrastructure`, `#devops`

---

<a id="item-8"></a>
## [crates.io 发布仍依赖 GitHub 的问题未解决](https://infosec.exchange/@mttaggart/116806641273303255) ⭐️ 7.0/10

Rust 生态系统中发布到 crates.io 依赖 GitHub 是一个已知问题。一项 RFC（Pull #3963）最近被合并以开始解决此问题，但实施工作仍在进行中，且依赖于志愿者的努力和资金支持。 这种依赖为 Rust 包生态系统造成了单点故障和锁定。解耦将提高弹性并符合开源原则，但由于资源有限，进展缓慢。 官方 issue（crates.io#326）列出了所需的工作。Jon Gjengset 的视频解释了技术挑战。RFC 旨在允许除 GitHub 以外的替代认证方法。

hackernews · speckx · Jun 24, 19:40

**背景**: crates.io 是 Rust 的包注册中心，目前发布包需要 GitHub 账户进行认证。这种设置是在 GitHub 被视为开源乌托邦时建立的，但现在已成为难以移除的深层依赖。Rust 的开发主要由志愿者驱动，使得不受欢迎的基础设施工作难以获得优先处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Crates.io">Crates.io</a></li>
<li><a href="https://doc.rust-lang.org/cargo/reference/publishing.html">Publishing on crates.io - The Cargo Book</a></li>

</ul>
</details>

**社区讨论**: 评论者承认这个问题及其修复难度，并引用了 RFC、官方 issue 和视频解释。大家一致认为，虽然目标是可取的，但需要目前缺乏的大量努力和资金支持。

**标签**: `#rust`, `#crates.io`, `#github`, `#open-source`, `#infrastructure`

---

<a id="item-9"></a>
## [工程师用 Claude 重写 SQL 解析器，实现 70 倍加速](https://posthog.com/blog/sql-parser) ⭐️ 7.0/10

PostHog 的一位工程师使用 Anthropic 的 Claude 重写了公司的 SQL 解析器，通过生成测试数据并用验证器检查正确性，实现了 70 倍的性能提升。 这个案例研究表明，当与可靠的测试验证器结合时，LLM 可以有效用于非平凡的代码优化，为类似的代码重构任务提供了可复现的方法论。 工程师几乎没看原始代码，而是依靠 Claude 生成新解析器，并用自动化测试验证正确性。原始解析器和新解析器都用 Python 编写，重点在于性能提升并保持行为一致。

hackernews · robbie-c · Jun 24, 18:05

**背景**: PostHog 是一个开源的产品分析平台，它使用 SQL 解析器来处理用户对产品数据的查询。SQL 解析器将 SQL 语句转换为结构化格式以便处理。像 Claude 这样的大语言模型可以生成代码，但常常出错；使用“验证器”——即检查正确性的测试套件——可以实现迭代改进并增强对输出的信心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://posthog.com/">PostHog – We make dev tools for product engineers</a></li>
<li><a href="https://www.emergentmind.com/topics/llm-assisted-coding">LLM - Assisted Coding</a></li>

</ul>
</details>

**社区讨论**: 社区赞扬了这种方法，指出当存在验证器来检验输出时，LLM 效果很好。一些人担心长期过度依赖 AI 可能会阻碍知识进步，而另一些人则强调从直接编码向工程规范的转变。

**标签**: `#AI-assisted programming`, `#SQL parser optimization`, `#LLM code generation`, `#software engineering`, `#performance optimization`

---

<a id="item-10"></a>
## [Claude Slackbot 获得多人、主动、持久升级](https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive) ⭐️ 7.0/10

Claude 的 Slack 集成已升级，支持可协作的多人代理、主动采取行动的代理以及跨交互保持上下文的持久代理。 此次升级使 Claude 的 Slackbot 对企业团队更有用，无需手动重新参与即可实现持续的 AI 辅助工作流程，并将 Claude 定位为生产力工具中更具竞争力的 AI 助手。 “多人”功能允许多个代理协同工作，“主动”意味着代理无需提示即可发起行动，“持久”确保代理记住先前的交互；未提供具体版本号或发布日期。

rss · Latent Space · Jun 24, 07:14

**背景**: AI 代理是可以自主执行任务的程序。传统上，代理是反应式且无状态的，需要手动输入。主动和持久代理的新范式使其能够理解上下文并主动采取行动，就像人类员工一样。多人代理允许多个 AI 实体协作，这在复杂工作流程中非常有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://adapt.com/blog/best-ai-agents-slack-2026">The Best AI Agents for Slack in 2026 | Adapt</a></li>
<li><a href="https://www.moltbot.io/">What is OpenClaw? Complete Guide to Personal AI Agents (2026)</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Slack`, `#Agents`, `#Enterprise`

---