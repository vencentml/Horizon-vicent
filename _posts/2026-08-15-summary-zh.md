---
layout: default
title: "Horizon Summary: 2026-08-15 (ZH)"
date: 2026-08-15
lang: zh
---

> From 127 items, 11 important content pieces were selected

---

1. [GLM-5.3：前沿编程能力与涌现式网络攻击能力](#item-1) ⭐️ 9.0/10
2. [特朗普威胁将霍尔木兹海峡宣布为美国领土](#item-2) ⭐️ 9.0/10
3. [刚果（金）埃博拉疫情每 30 分钟夺一命](#item-3) ⭐️ 9.0/10
4. [Qwen 3.8 27B 本地测试表现出色，但推理较慢](#item-4) ⭐️ 8.0/10
5. [“走向黑暗”辩论转向执法黑客时代](#item-5) ⭐️ 8.0/10
6. [Firefox 成为唯一支持 uBlock Origin 的主流浏览器](#item-6) ⭐️ 8.0/10
7. [Cloudflare Gateway 检测并保护 MCP 流量](#item-7) ⭐️ 8.0/10
8. [RustDesk 现已支持 Wayland 下的真正无人值守远程访问](#item-8) ⭐️ 7.0/10
9. [澳洲家用电池热潮降低批发电价](#item-9) ⭐️ 7.0/10
10. [法国最高法院推翻社交媒体年龄验证法](#item-10) ⭐️ 7.0/10
11. [用 Cloudflare Access for Workers 一键保护内部 vibe-coding 应用](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [GLM-5.3：前沿编程能力与涌现式网络攻击能力](https://z.ai/blog/glm-5.3) ⭐️ 9.0/10

Z.ai 发布了 GLM-5.3，这是一个建立在与 GLM-5.2 相同的 743B 基座模型之上的开源旗舰模型，所有改进均来自扩展后的后训练。早期用户报告了涌现出的自主网络攻击能力，包括对 WordPress 插件的 0-day 漏洞发现、RCE（远程代码执行）以及内核漏洞利用的适配，Z.ai 还在 cvd.z.ai 披露了一批 CVE。 这一发布表明，前沿编程模型开始展现出可信的自主安全研究能力，改变了开源权重 AI 的风险评估逻辑，也提高了外界对 LLM 智能体的预期。强大的代码基准表现加上涌现出的漏洞利用行为，可能会给闭源实验室带来压力，并改变漏洞发现与披露的方式。 GLM-5.3 在 Z.ai Code Bench 上比 GLM-5.2 提升了 50%，并在 Terminal-Bench 3.0 和 Agents' Last Exam (CLI) 上取得了开源模型最佳成绩。Z.ai 运营着一个漏洞披露门户，其中许多 CVE 尚处于保密期；据报道，本次发布未重新训练基座模型，所有提升都来自在更多任务环境上的后训练。

hackernews · pella · Aug 14, 05:19

**背景**: GLM-5.3 是 Z.ai 的 GLM 系列最新的开源权重模型。与完整重新训练不同，该版本保留了与 GLM-5.2 相同的 743B 基座模型，并通过更多任务环境的扩展来扩大后训练规模。研究者用“涌现能力”（emergent abilities）描述大语言模型在规模扩大时不可预测地出现的能力，此次发布也被舆论与这类涌现出的网络能力联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/08/14/z-ai-ships-glm-5-3-without-retraining-the-base-model-better-at-complex-coding-and-long-horizon-tasks/">Z.ai Ships GLM-5.3 Without Retraining the Base Model: Better at Complex Coding and Long-Horizon Tasks - MarkTechPost</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.3">GLM-5.3 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://arxiv.org/abs/2206.07682">[2206.07682] Emergent Abilities of Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 社区反应大体积极但保持谨慎。一位用户称 GLM-5.3 是第一个无缝完成红队场景的模型，在让另一个 GLM 智能体充当防守方时，发现了 WordPress 插件中的 0-day、RCE 和内核漏洞利用适配；另一位用户则注意到 Z.ai 在规模化扫描开源软件并披露 CVE，质疑其成本并拿来与 Anthropic 的 Project Glasswing 比较。还有人认为它距离“Sol 和 Fable”只差一点，但尚不足以成为放弃 OpenAI 的经济理由，也有人赞赏其博客文字更像研究人员所写，而非营销炒作。

**标签**: `#AI`, `#cybersecurity`, `#GLM`, `#LLM`, `#vulnerability research`

---

<a id="item-2"></a>
## [特朗普威胁将霍尔木兹海峡宣布为美国领土](https://www.theguardian.com/us-news/2026/aug/14/trump-threat-strait-hormuz-us-territory) ⭐️ 9.0/10

在纽约长岛警察学院的一次演讲中，唐纳德·特朗普表示“很快”将把霍尔木兹海峡指定为“美国领土”。目前尚不清楚这一言论的严肃性以及它是否意味着新的政策立场。 霍尔木兹海峡是全球关键的能源咽喉要道，全球约五分之一的海洋石油运输通常经过此地。将其宣布为美国领土将对石油市场、航运和军事冲突产生重大影响，并可能使持续的美伊战争进一步升级。 该言论于周五在纽约发表，但其严肃性尚不确定。据报道，美国政府正努力结束与伊朗的战争，目前尚不清楚这一声明是反映正式政策转变，还是仅仅是一种言辞威胁。

rss · The Guardian World · Aug 14, 21:38

**背景**: 霍尔木兹海峡是位于伊朗、阿曼和阿联酋之间的狭窄水道，连接波斯湾与阿曼湾及开阔海域。它是全球最具战略意义的石油运输路线之一，任何将其宣称为美国领土的企图都可能遭到伊朗及其他地区大国的强烈反对，从而引发更广泛的军事对抗。

**标签**: `#geopolitics`, `#energy security`, `#oil markets`, `#Trump`, `#US-Iran`

---

<a id="item-3"></a>
## [刚果（金）埃博拉疫情每 30 分钟夺一命](https://news.un.org/feed/view/en/story/2026/08/1168148) ⭐️ 9.0/10

刚果（金）东部的埃博拉疫情目前每 30 分钟导致一人死亡。这使其成为有记录以来传播最快的埃博拉疫情，并有可能成为最致命的一次。 这表明刚果（金）东部的公共卫生紧急状况正在加剧，亟需全球关注和资源投入。若不迅速干预，疫情可能进一步失控，给该地区带来广泛苦难。 疫情发生在刚果民主共和国东部，该地区受冲突影响且医疗卫生基础设施薄弱。据联合国新闻报道，此次疫情是有记录以来传播最快的，预计将成为历史上最致命的埃博拉疫情。

rss · UN News · Aug 14, 12:00

**背景**: 埃博拉是一种严重的病毒性出血热，病死率很高，通过与感染者的体液直接接触传播。刚果（金）过去曾多次爆发埃博拉疫情，但当前东部疫情的传播速度超过以往任何一次。社区抵制、持续冲突和地形复杂等因素使该地区的疫情控制尤为困难。

**标签**: `#Ebola`, `#DRC`, `#Public Health`, `#Epidemic`, `#Humanitarian Crisis`

---

<a id="item-4"></a>
## [Qwen 3.8 27B 本地测试表现出色，但推理较慢](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

阿里巴巴的 Qwen 3.8 27B FP8 模型现已上架 Hugging Face。早期社区测试显示，它能通过此前只有 Gemma 4 通过的私有基准，并画出了 Simon Willison 所说“笔记本模型画得最好的自行车-鹈鹕图”。 这为在本地运行 LLM 的用户提供了一个 27B 规模的新强选项，表明开放权重模型与更成熟的产品差距正在缩小。不过速度和显存占用的取舍意味着用户需要根据硬件条件权衡能力。 FP8 版本在一位测试者的对比中比同类模型更慢、显存效率也更低，启用多 token 预测后解决基准耗时 12 分 30 秒。另一位用户在 RTX 5090 上用 ninfer 引擎测到约 138 tokens/秒，大约是朴素 llama.cpp 配置的两倍；评测者还注意到其思维链比 Qwen 3.6 更碎片化。

hackernews · erdaltoprak · Aug 14, 15:00

**背景**: Qwen 是阿里巴巴云推出的大型语言模型系列，2023 年 4 月首次上线测试版。本地运行模型是指在自有硬件上执行模型，而不是通过云端 API 调用，这样可以降低成本并提升隐私性。对本地 LLM 来说，显存（VRAM）是关键硬件资源，因为 GPU 需要存放模型参数和工作数据，显存越大，能运行的模型就越大或越快。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://prajnaaiwisdom.medium.com/what-is-local-llm-inference-a-beginners-guide-b31043768d4f">What Is Local LLM Inference? A Beginner’s Guide</a></li>
<li><a href="https://runpod.ghost.io/understanding-vram-and-how-much-your-llm-needs/">What is VRAM ? Understanding VRAM for your LLM Deployment</a></li>

</ul>
</details>

**社区讨论**: 评论整体积极但保持谨慎：一位测试者称该模型“非常好”，认为开放模型的实力正接近 Fable/Sol 级别且不来自美国大公司，其他人则指出了具体的取舍。CMay 提到它通过了私有基准，但耗费了 5 倍的 token，且显存效率不如 Gemma 4 或 Glimmer；dofm 怀疑新的“穴居人式”思维链模式可能损害 MTP 预测。大家还分享了针对特定硬件的性能建议，比如在 RTX 5090 上使用 ninfer。

**标签**: `#AI`, `#Open Source`, `#LLM`, `#Local Models`, `#Qwen`

---

<a id="item-5"></a>
## [“走向黑暗”辩论转向执法黑客时代](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/) ⭐️ 8.0/10

在 2026 年 8 月的一篇博文中，密码学工程师 Matthew Green 认为，“走向黑暗”的辩论正从加密后门转向执法黑客时代。文章指出，执法部门越来越多地使用网络调查技术（NIT）和软件漏洞来访问设备。 这一转变意义重大，因为执法黑客行为依赖于安全漏洞，而这些漏洞也可能被犯罪分子和国家行为者利用，从而可能削弱整体软件安全性。它引发了关于漏洞披露、正当程序和政府黑客行为法律边界的重大政策问题，影响技术人员、政策制定者和公众。 这篇文章借鉴了历史背景，例如前数字时代窃听的物理成本，并讨论了可利用软件漏洞的供应是否会达到上限。社区评论者还提到了 FBI 自至少 2002 年以来使用的“网络调查技术”（一种“路过下载”恶意软件），并指出 AI 生成的代码可能带来更多漏洞。

hackernews · vslira · Aug 14, 20:52

**背景**: “走向黑暗”是执法部门用来描述其无法访问加密通信和数据的术语，他们认为这阻碍了刑事调查。早期的辩论集中在要求加密产品植入后门，但这一做法遭到安全专家的强烈反对。近年来，执法部门转而采用“合法黑客”手段——使用 NIT 等技术工具（通常通过“路过下载”方式投递）来访问嫌疑人的设备。这种方法引发了透明度方面的担忧，因为有关这些工具及其法律保障措施的细节往往保密，法律学者和政策分析人士也指出了这一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Network_Investigative_Technique">Network Investigative Technique</a></li>
<li><a href="https://www.csis.org/blogs/strategic-technologies-blog/encryption-and-going-dark-cutting-through-gordian-knot">Encryption and Going Dark – Cutting through the Gordian Knot | CSIS</a></li>
<li><a href="https://www.justsecurity.org/60785/shining-light-federal-law-enforcements-computer-hacking-tools/">Shining a Light on Federal Law Enforcement ’s Use of Computer...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不同的观点：有人指出物理窃听的历史成本和后勤负担；有人不同意作者关于可利用漏洞供应可能达到平台期的观点，认为 AI 生成的代码让软件漏洞更多；还有人嘲笑“走向黑暗”的说法，指出监控摄像头和元数据收集无处不在；另有人将高端攻击者与常见的组织安全失误进行对比。

**标签**: `#encryption`, `#law enforcement`, `#surveillance`, `#security`, `#policy`

---

<a id="item-6"></a>
## [Firefox 成为唯一支持 uBlock Origin 的主流浏览器](https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html) ⭐️ 8.0/10

随着谷歌完成向 Manifest V3 的过渡，uBlock Origin 等 Manifest V2 扩展在 Chrome 中已无法使用，Firefox 成为唯一仍完全支持 uBlock Origin 的主流浏览器。该变化已于 2026 年年中在 Chrome 稳定版中生效。 这标志着浏览器扩展生态的结构性转变：使强力广告拦截成为可能的 webRequestBlocking API 正受到限制，Firefox 作为最后一个有效的广告拦截主流选项的地位得到巩固。数百万追求隐私和广告控制的用户将需要转向 Firefox 或诸如 uBlock Origin Lite 之类的较弱替代品。 uBlock Origin 依赖 webRequest API 的阻塞版本，而在 Manifest V3 中，该 API 仅对企业侧载扩展可用。Firefox 继续支持完整的 webRequest API，并且有一个非官方的 uBlock Origin MV3 移植版，但其功能存在局限。

hackernews · DemiGuru · Aug 14, 19:03

**背景**: Manifest V3 是谷歌为 Chrome 推出的最新扩展平台，旨在提升隐私、安全和性能，但它弃用了广告拦截器所依赖的阻塞型网络请求 API。uBlock Origin 是一个广受欢迎的免费开源内容拦截器，支持 Firefox 和基于 Chromium 的浏览器，以低 CPU 和内存占用以及高效的广告过滤著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eff.org/deeplinks/2021/12/googles-manifest-v3-still-hurts-privacy-security-innovation">Google’s Manifest V 3 Still Hurts Privacy, Security, and Innovation</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V 3 | Chrome for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Firefox 还会对 uBlock Origin 的每次更新进行审核和验证以防止间谍软件，另一些人则批评谷歌的决定削弱了扩展的自由度。一位用户提到 uBlock Origin 有一个非官方的 MV3 移植版，另一位用户表示因 Manifest V3 而关闭了自己的 Google 搜索广告过滤工具，还有一位用户询问 uBlock Origin Lite 的拦截效果。

**标签**: `#browsers`, `#privacy`, `#ad-blocking`, `#manifest-v3`, `#uBlock-Origin`

---

<a id="item-7"></a>
## [Cloudflare Gateway 检测并保护 MCP 流量](https://blog.cloudflare.com/mcp-security-updates/) ⭐️ 8.0/10

Cloudflare Gateway 现在通过协议级启发式规则识别 MCP 请求，使安全团队能够发现影子 MCP 流量、对已批准的服务器强制执行 Portal-only 访问，并阻止受管网络路径上的直接连接。 随着 AI 代理越来越多地使用 MCP 连接企业系统，不受监控的影子 MCP 流量正成为一个重大的安全风险。这项新能力让安全团队对 AI 到系统的流量获得可见性和强制控制，填补了企业网络安全中日益扩大的盲区。 检测工作在协议层面进行，而非仅依赖域名或端口，因此即使 MCP 流量使用非标准端点，Gateway 也能识别。强制措施在受管网络路径上执行，而 Portal-only 访问将用户限制在已批准的 MCP 服务器上。

rss · Cloudflare Blog · Aug 14, 13:12

**背景**: MCP（Model Context Protocol）是 Anthropic 推出的一个开放标准，用于将 AI 应用连接到外部数据源、工具和工作流。随着 AI 应用的普及，企业需要像治理 Web 和云流量一样，对 AI 流量进行治理和安全防护。Cloudflare 的公告将其 Gateway 安全平台扩展到这一新兴协议，以应对企业中影子 AI 使用日益增多的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/mcp-security-updates/">How Cloudflare detects MCP traffic and helps secure it</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )?</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#MCP`, `#AI security`, `#enterprise networking`, `#shadow AI`

---

<a id="item-8"></a>
## [RustDesk 现已支持 Wayland 下的真正无人值守远程访问](https://rustdesk.com/blog/unattended-remote-access-wayland/) ⭐️ 7.0/10

RustDesk 宣布支持 Wayland 下真正意义上的无人值守远程访问，填补了 Linux 远程支持中长期存在的空白。用户现在可以远程连接基于 Wayland 的 Linux 机器，而无需有人在电脑前进行操作。 这很重要，因为 Wayland 已成为大多数主流 Linux 发行版的默认显示服务器，但远程桌面工具一直难以安全地支持它。此功能使 RustDesk 成为 Linux 用户替代 TeamViewer 和 AnyDesk 等专有工具的更可行开源选择。 公告指出，此前在 Wayland 上实现真正的无人值守访问需要变通方案；而且根据社区反馈，自托管服务器的加密连接问题仍未解决。此外，客户端到主机的麦克风输入透传功能也仍然不支持。

hackernews · rustdesk · Aug 14, 16:12

**背景**: Wayland 是一种现代显示服务器协议，旨在替代老旧的 X11/Xorg 系统，现已是 Fedora、Ubuntu 等主要发行版的默认显示服务器。RustDesk 是一款开源远程桌面应用，支持自建服务器，定位为专有工具的安全替代方案。以往远程访问工具依赖 X11 宽松的架构，而 Wayland 的安全模型限制了屏幕捕获和输入注入，使无人值守访问变得更加复杂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayland_(protocol)">Wayland (protocol) - Wikipedia</a></li>
<li><a href="https://wayland.freedesktop.org/">Wayland</a></li>
<li><a href="https://rustdesk.com/">RustDesk : Open-Source Remote Desktop with Self-Hosted Server...</a></li>

</ul>
</details>

**社区讨论**: 社区总体反馈积极，用户称赞 RustDesk 并对其修复 Wayland 相关空白表示欣慰。不过，有用户指出自托管连接仍不支持加密，也有人提到与专有解决方案相比，麦克风透传功能仍然缺失。

**标签**: `#RustDesk`, `#Wayland`, `#Remote Access`, `#Open Source`, `#Linux`

---

<a id="item-9"></a>
## [澳洲家用电池热潮降低批发电价](https://e360.yale.edu/digest/australia-home-batteries) ⭐️ 7.0/10

澳大利亚家用电池的快速普及帮助降低了批发电价，表明分布式储能能够显著影响能源市场。这一热潮发生在太阳能繁荣之后，后者曾使白天电价转为负值。 这件事意义重大，因为它提供了一手证据，表明家用电池能为电网提供服务并降低所有用户的成本，而不仅仅是电池拥有者。它可能影响其他国家的能源政策和公用事业决策，例如在美国，公用事业公司一直抵制类似的采用。 社区评论指出，澳大利亚的补贴计划已花费约 25 亿澳元，支持了 11 吉瓦时的安装量，部分个人补贴覆盖了约 70%的成本。对于将公共资金用于电网级储能是否会更好，存在争议。

hackernews · speckx · Aug 14, 14:07

**背景**: 分布式储能系统（DESS）是并网设备，用于储存来自屋顶太阳能等可再生能源的电力。它们有助于管理太阳能和风能的波动性，减轻输电网络的压力，并能提供备用电源。澳大利亚廉价的太阳能板加上动态电网定价，鼓励家庭采用电池，电池在白天吸收多余的太阳能发电，并在高峰时段放电。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Distributed_energy_storage_system">Distributed energy storage system</a></li>
<li><a href="https://en.wikipedia.org/wiki/Distributed_generation">Distributed generation - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/engineering/distributed-energy-storage">Distributed Energy Storage - an overview | ScienceDirect Topics</a></li>

</ul>
</details>

**社区讨论**: 评论者大多称赞电池热潮，将其归功于廉价的太阳能板和动态定价，同时批评美国公用事业公司的反对。也有人批评澳大利亚的补贴是累退性的，指出它把税收资金输送给了相对富裕的家庭，电网级储能可能更高效，但总体情绪对分布式储能的市场影响持积极态度。

**标签**: `#energy`, `#batteries`, `#Australia`, `#electricity markets`, `#solar`

---

<a id="item-10"></a>
## [法国最高法院推翻社交媒体年龄验证法](https://www.reuters.com/world/frances-top-court-rules-social-media-ban-curtails-freedom-expression-2026-08-14/) ⭐️ 7.0/10

2026 年 8 月 14 日，法国宪法委员会（Conseil constitutionnel）否决了一项要求社交媒体平台验证用户年龄并禁止 15 岁以下未成年人使用的法律，裁定该法律过度限制言论自由和隐私权。 这一裁决为欧洲各地的年龄验证强制要求开创了重要的法律先例，并可能影响其他国家的监管思路。它为科技公司和隐私倡导者提供了有力论据，表明年龄检查往往实际上成为身份检查，进一步印证了数据保护方面的担忧。 法院认为，虽然保护未成年人上网是合理的立法目标，但该法律要求的系统性年龄验证会在缺乏足够保障的情况下侵犯所有用户的权利。该裁决符合数据保护原则，呼应了“年龄验证系统可能滑向身份验证并被挪作他用”的担忧。

hackernews · BlueBerry2001 · Aug 14, 16:06

**背景**: 法国宪法委员会（Conseil constitutionnel）负责审查法律是否符合宪法，并可在法律颁布前或颁布后予以否决。近年来，社交媒体平台面临日益增大的未成年人保护压力，促使各国提出年龄检查措施；但由于验证年龄往往需要身份证件等敏感数据，这类措施引发了隐私和言论自由方面的争议。

**社区讨论**: 评论者普遍欢迎这一裁决，但就替代执法方案展开辩论。有人认为该法律为了揪出少数违规者而牺牲全体用户的权利，并与“Chat Control”提案相提并论；另有评论者建议采用儿童锁定设备或 HTTP 头等技术方案；一位法国用户则表示议会浪费了时间，因为宪法委员会的否决原本就可预料。

**标签**: `#policy`, `#privacy`, `#age-verification`, `#regulation`, `#france`

---

<a id="item-11"></a>
## [用 Cloudflare Access for Workers 一键保护内部 vibe-coding 应用](https://blog.cloudflare.com/workers-protected-by-access/) ⭐️ 7.0/10

Cloudflare 推出了 Access for Workers，允许开发者一键将 Access 策略附加到 Worker 上。该策略会自动保护所有路由、自定义域名、workers.dev 和预览。 随着 vibe-coding 内部应用越来越普遍，它们往往缺乏适当的安全控制。这种一键集成让开发者轻松保护内部工具，无需复杂配置即可提升安全态势。 Access 策略会应用到 Worker 运行的所有位置，包括预览环境。Cloudflare Access 是一种零信任网络访问（ZTNA）解决方案，无需传统 VPN。

rss · Cloudflare Blog · Aug 14, 13:00

**背景**: Vibe-coding 是一种用自然语言描述而不是编写详细代码来构建应用程序的新方式，通常借助 AI 工具完成。这导致快速构建的内部应用激增。Cloudflare Access 是一种零信任网络访问解决方案，为员工和承包商保护应用访问安全。新的 Access for Workers 功能将两者结合，为开发者提供了一种保护 vibe-coding 应用的简单方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/workers-protected-by-access/">Secure all your internal vibe-coded applications — in... | Cloudflare Blog</a></li>
<li><a href="https://www.cloudflare.com/sase/products/access/">Access | Zero Trust Network Access (ZTNA) solution | Cloudflare</a></li>
<li><a href="https://aistudio.google.com/vibe-code">Vibe Coding | Google AI Studio</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#security`, `#access-control`, `#workers`, `#vibe-coding`

---