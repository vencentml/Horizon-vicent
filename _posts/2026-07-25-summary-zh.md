---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> From 118 items, 16 important content pieces were selected

---

1. [Anthropic 发布 Claude Opus 5，强化隐私保护](#item-1) ⭐️ 9.0/10
2. [安防摄像头登录页面泄露硬编码的 GitHub 管理员令牌](#item-2) ⭐️ 9.0/10
3. [伊朗革命卫队声称摧毁亚马逊巴林数据中心](#item-3) ⭐️ 9.0/10
4. [美国情报称伊朗新领导人对核武器更开放](#item-4) ⭐️ 9.0/10
5. [特朗普考虑升级美以对伊朗战争](#item-5) ⭐️ 9.0/10
6. [美伊冲突升级：军事打击与石油市场动荡](#item-6) ⭐️ 9.0/10
7. [特朗普因科技罚款威胁对欧盟征收‘巨额’关税](#item-7) ⭐️ 9.0/10
8. [美国扩大对伊朗打击，特朗普警告德黑兰与胡塞武装](#item-8) ⭐️ 9.0/10
9. [特朗普政府承认基于政治原因取消清洁能源拨款](#item-9) ⭐️ 9.0/10
10. [SGLang v0.5.16 引入 DSpark 推测解码和 Inkling 支持](#item-10) ⭐️ 8.0/10
11. [Postgres LISTEN/NOTIFY 可达每秒 6 万条通知](#item-11) ⭐️ 8.0/10
12. [英伟达、微软和 Meta 警告不要过度监管开放权重模型](#item-12) ⭐️ 8.0/10
13. [Cloudflare 揭示传输提供商广泛操纵 BGP ORIGIN 属性](#item-13) ⭐️ 8.0/10
14. [印度政府要求 GitHub 移除蓝牙聊天应用 Bitchat](#item-14) ⭐️ 7.0/10
15. [Buz: 基于现代 Zig 的 Bun 分支，实现亚秒级增量构建](#item-15) ⭐️ 7.0/10
16. [Black Forest Labs 发布 FLUX 3 多模态流模型](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Opus 5，强化隐私保护](https://www.anthropic.com/news/claude-opus-5) ⭐️ 9.0/10

Anthropic 宣布推出新旗舰 AI 模型 Claude Opus 5，该模型在通用访问中无需数据保留，并展现出卓越的图片转 HTML 性能。 此次发布为组织提供了一个无需典型 30 天数据保留策略的强大模型，解决了关键隐私问题，同时推动了视觉到代码能力的进步。 Claude Opus 5 无需数据保留要求即可使用，这与 Fable 等需要 30 天保留策略的模型形成对比。根据社区测试，Opus 5 从图片生成的 HTML 比以往最佳模型更准确。

hackernews · alvis · Jul 24, 16:57

**背景**: 零数据保留（ZDR）意味着提示和完成内容在 API 调用生命周期结束后不会被存储，也不会用于训练。虽然许多提供商通过企业协议提供 ZDR，但 Anthropic 的 Opus 5 在通用访问中提供此功能。系统卡是一份提供 AI 系统架构、训练数据和安全性信息透明度的文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://decagon.ai/glossary/what-is-zero-data-retention-ai">What is Zero Data Retention AI? Definition & Vendor Guide | Decagon</a></li>
<li><a href="https://www.redhat.com/en/blog/security-beyond-model-introducing-ai-system-cards">Security beyond the model: Introducing AI system cards</a></li>

</ul>
</details>

**社区讨论**: 评论者强调，Opus 5 无需数据保留要求是其相对于 Fable 等模型的关键优势。一位用户测试了图片转 HTML 功能，发现 Opus 5 更准确；另一位用户指出，Opus 5 在写作风格上保留了标志性的“Claude 习惯用语”，而 Fable 则没有。

**标签**: `#AI`, `#Anthropic`, `#Claude Opus 5`, `#model release`, `#data privacy`

---

<a id="item-2"></a>
## [安防摄像头登录页面泄露硬编码的 GitHub 管理员令牌](https://hhh.hn/hanwha-github-token/) ⭐️ 9.0/10

韩华安防摄像头的登录页面包含一个具有管理员权限的硬编码 GitHub 个人访问令牌，暴露出严重的供应链安全漏洞。 此漏洞可能使攻击者能够未经授权访问供应商的 GitHub 仓库，可能导致代码篡改或进一步的供应链攻击。这凸显了物联网设备制造中安全卫生的严重缺失。 该硬编码令牌以明文形式存在于摄像头网络界面的源代码中，违反了安全最佳实践。任何检查登录页面的人都有可能利用此类凭据。

hackernews · hhh · Jul 24, 11:54

**背景**: 硬编码凭据是直接嵌入源代码或固件中的密码或令牌，是一种已知的不良实践，常导致数据泄露。GitHub 个人访问令牌（PAT）用于 API 和命令行身份验证；一旦暴露，它们将授予与关联账户相同的权限。此事件展示了消费级物联网设备如何成为软件供应链中的薄弱环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">Managing your personal access tokens - GitHub Docs</a></li>
<li><a href="https://cwe.mitre.org/data/definitions/798.html">CWE - CWE-798: Use of Hard - coded Credentials (4.20)</a></li>
<li><a href="https://blog.gitguardian.com/why-its-urgent-to-deal-with-your-hard-coded-credentials/">Hardcoded Credentials Vulnerability : Why Immediate Action Matters</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了震惊，并指出了更广泛的问题，例如固件中包含了美国战争部的 IP 地址。建议包括将摄像头隔离在单独的 VLAN 上并避开某些供应商。舆论对物联网中糟糕的安全实践持批评态度。

**标签**: `#security`, `#iot`, `#supply-chain`, `#vulnerability`

---

<a id="item-3"></a>
## [伊朗革命卫队声称摧毁亚马逊巴林数据中心](https://houseofsaud.com/irgc-claims-destroyed-amazon-bahrain-data-center/) ⭐️ 9.0/10

伊朗伊斯兰革命卫队（IRGC）声称作为对美国资产的报复性攻击的一部分，摧毁了位于巴林的一个亚马逊数据中心。卫星图像和社区分析确认 AWS 的 me-south-1 区域受损，据报道多个数据中心建筑被击中。 此次攻击凸显了云基础设施在地缘政治冲突和物理攻击面前的脆弱性，可能导致中东地区客户服务中断。它强调了在政治不稳定地区集中式云数据中心的风险，并可能加速采用多区域和多云策略。 像 me-south-1 这样的 AWS 区域通常由至少三个相距数公里的数据中心组成，因此整个区域瘫痪表明对多个设施或支持基础设施进行了协调攻击。社区报告显示，为 BAH53 供电的变电站于 2026 年 7 月 16 日受损，随后数据中心本身在 7 月 22 日受损。

hackernews · thisislife2 · Jul 24, 09:52

**背景**: 亚马逊网络服务（AWS）于 2019 年在巴林推出了其首个中东区域（me-south-1），包含三个可用区。该区域因当地持续冲突而中断。AWS 区域设计时数据中心之间有物理隔离，以最小化共同故障点，但协调攻击仍可能导致大范围中断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/aws/now-open-aws-middle-east-bahrain/">Now Open – AWS Middle East (Bahrain) | Amazon Web Services</a></li>
<li><a href="https://www.aboutamazon.com/news/aws-bahrain-region-middle-east-conflict">AWS Bahrain Region disrupted by ongoing conflict</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达讽刺，认为此次攻击后中东唯一运行的 AWS 区域在特拉维夫。用户强调 AWS 区域由多个相距数公里的数据中心组成，暗示了多次攻击。有人指出冲突期间集中式基础设施脆弱性的更广泛教训。

**标签**: `#geopolitics`, `#cloud-infrastructure`, `#AWS`, `#cybersecurity`, `#risk`

---

<a id="item-4"></a>
## [美国情报称伊朗新领导人对核武器更开放](https://www.nytimes.com/2026/07/24/us/politics/iran-nuclear-weapon.html) ⭐️ 9.0/10

美国情报机构评估认为，伊朗新最高领袖（在战争中丧生的前任领袖之子）比其父亲更倾向于寻求核武器，而他的父亲曾放弃核武器。 伊朗核姿态的这一转变可能增加中东核扩散的风险，并对全球安全以及遏制伊朗核计划的外交努力产生重大影响。 该评估基于领导层变动：在战争初期被杀的前任最高领袖曾承诺放弃核武器，而据报道其儿子对制造核弹更感兴趣。

rss · NYTimes World · Jul 24, 18:18

**背景**: 伊朗长期以来被怀疑追求核武器能力，但其最高领袖此前曾发布反对核武器的教令。战争中的领导层变动给伊朗的核意图带来了不确定性。美国情报机构定期评估来自对手的核威胁。

**标签**: `#geopolitics`, `#Iran`, `#nuclear weapons`, `#intelligence`, `#nonproliferation`

---

<a id="item-5"></a>
## [特朗普考虑升级美以对伊朗战争](https://www.nytimes.com/2026/07/24/us/politics/trump-escalation-iran.html) ⭐️ 9.0/10

特朗普总统与高级顾问会面，讨论升级已持续近五个月、远超最初“短程行动”预期的美以对伊朗战争。 重大升级可能严重破坏中东稳定，扰乱全球石油市场，并卷入其他地区强国。这一决定将产生深远的全球地缘政治和经济影响。 特朗普最初坚称战争将是一次短暂行动，但已持续五个月且看不到尽头。此次会议表明战略可能转变，或将把军事行动扩大到当前范围之外。

rss · NYTimes World · Jul 24, 21:41

**背景**: 美国和以色列一直在联合对伊朗进行军事行动，旨在消除其所谓的核威胁和地区代理人。冲突始于定点打击，但已扩大为持续战役。特朗普早期对快速解决的保证被证明不准确，现在政府面临要么寻找出路、要么加大力度的压力。

**标签**: `#geopolitics`, `#Iran`, `#US foreign policy`, `#military conflict`, `#escalation`

---

<a id="item-6"></a>
## [美伊冲突升级：军事打击与石油市场动荡](https://www.nytimes.com/live/2026/07/24/world/iran-war-us-strikes-trump-oil/heres-the-latest) ⭐️ 9.0/10

《纽约时报》正在直播美伊冲突升级的最新情况，包括军事打击及其对全球石油市场的即时影响。 此次升级可能引发重大地缘政治不稳，影响全球能源供应和安全。决策者和投资者正在密切关注事态发展。 报道内容包括军事行动、外交回应以及油价波动的实时更新。局势瞬息万变，可能涉及更广泛的地区参与。

rss · NYTimes World · Jul 24, 23:17

**背景**: 美国与伊朗长期存在紧张关系，主要集中在伊朗核计划及其在中东的影响力上。军事打击可能扰乱全球石油供应，因为伊朗靠近霍尔木兹海峡这一关键航道。

**标签**: `#geopolitical risk`, `#US-Iran conflict`, `#energy markets`, `#military action`, `#foreign policy`

---

<a id="item-7"></a>
## [特朗普因科技罚款威胁对欧盟征收‘巨额’关税](https://www.theguardian.com/us-news/2026/jul/24/trump-european-union-tariffs) ⭐️ 9.0/10

2026 年 7 月 24 日，美国总统特朗普威胁欧盟，若欧盟对美国科技巨头（包括谷歌、苹果、Meta 和亚马逊）处以巨额罚款，将对欧盟征收“巨额”关税。 这标志着美欧贸易紧张局势显著升级，将针对美国科技公司的反垄断执法直接与关税挂钩。这表明美国政府可能利用贸易政策报复外国监管行动，给全球科技监管和市场稳定带来不确定性。 特朗普通过 Truth Social 发帖发出威胁，指责布鲁塞尔“抢劫”美国公司和纳税人。欧盟此前因反竞争行为对谷歌处以 8.9 亿欧元罚款，这是针对美国科技公司的一系列罚款之一。

rss · The Guardian World · Jul 24, 21:22

**背景**: 欧盟一直在积极对美国大型科技公司执行反垄断法，认为它们滥用市场支配地位。这些行动已导致数十亿欧元的罚款和要求改变商业行为的要求。特朗普的回应有可能升级为贸易战，因为关税可能影响欧盟对美国的各类出口。

**标签**: `#trade policy`, `#tariffs`, `#EU`, `#antitrust`, `#geopolitical risk`

---

<a id="item-8"></a>
## [美国扩大对伊朗打击，特朗普警告德黑兰与胡塞武装](https://www.theguardian.com/world/2026/jul/24/us-expands-iran-attacks-as-trump-warns-tehran-and-houthis-over-red-sea-strikes) ⭐️ 9.0/10

美国将军事打击扩大至伊朗纵深，目标直达里海附近，同时特朗普总统威胁要对德黑兰及其胡塞盟友实施“重大军事惩罚”。伊朗以无人机和导弹反击美国在巴林、约旦和科威特的基地，并据报道拒绝了由伊拉克总理转交的美国停火提议。 这标志着美伊直接军事对抗，显著增加了爆发更广泛地区战争的风险，可能破坏全球石油市场和航运安全。冲突现已蔓延至多条战线，威胁中东及更广地区的长期不稳定。 美国打击了伊朗境内包括里海附近的目标，伊朗的报复行动使用无人机和导弹攻击了美国在巴林、约旦和科威特的基地。据报道，伊朗拒绝了由伊拉克总理阿里·扎伊迪转交的美国停火提议，尽管美国国务卿马尔科·卢比奥声称伊朗在乞求停火；伊拉克随后否认该说法。

rss · The Guardian World · Jul 24, 17:58

**背景**: 美国与伊朗的紧张局势在也门胡塞武装（受伊朗支持）加大对红海这一全球贸易关键通道的商船袭击后升级。美国最初打击胡塞目标，但随着伊朗直接攻击美国盟友，冲突扩大。特朗普的“重大军事惩罚”警告以及针对伊朗本土的打击，标志着美国此前遏制政策的重大转变。

**标签**: `#geopolitics`, `#military conflict`, `#US-Iran`, `#Houthis`, `#Red Sea`

---

<a id="item-9"></a>
## [特朗普政府承认基于政治原因取消清洁能源拨款](https://www.theguardian.com/us-news/2026/jul/24/trump-administration-cancel-clean-energy-grants-democrat-states) ⭐️ 9.0/10

在法庭文件中，特朗普政府承认取消了超过 75 亿美元的联邦清洁能源拨款，仅依据各州在 2024 年大选中是否支持特朗普。 这一揭露标志着联邦资金的严重政治化，可能阻碍清洁能源投资，并为利用联邦拨款作为政治筹码树立危险先例。 被取消的拨款针对的是投票支持卡玛拉·哈里斯的民主党领导州的项目，尽管政府在法庭文件中承认了政治依据，但仍称其为‘错误表述’。

rss · The Guardian World · Jul 24, 21:26

**背景**: 这些拨款是《通货膨胀削减法案》及其他旨在加速清洁能源部署的联邦计划的一部分。特朗普政府一贯反对气候倡议，但以政治归属作为终止资金的标准是前所未有的，并引发法律质疑。

**标签**: `#politics`, `#energy policy`, `#regulation`, `#Trump administration`, `#federal funding`

---

<a id="item-10"></a>
## [SGLang v0.5.16 引入 DSpark 推测解码和 Inkling 支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 8.0/10

SGLang v0.5.16 引入了基于置信度的推测解码算法 DSpark，在 DeepSeek-V4-Pro 上达到 383.7 tok/s，并新增对 975B 参数多模态 MoE 模型 Inkling 的支持，输入吞吐量最高达 71.7k tok/s。 这些特性显著提升了大型语言模型的推理吞吐量，使高性能服务更加易用。DSpark 的自适应验证和 Inkling 的原生 MTP 支持展示了推测解码和大规模 MoE 部署方面的实际进展。 DSpark 采用半自回归块式草稿，随后使用基于置信度的验证窗口大小；Inkling 混合了滑动窗口、全局注意力和 Mamba2 线性注意力，并包含 NVFP4 MoE 和可选的视觉/音频塔。该版本还移除了实验性的 QServe 和 FBGEMM FP8 量化路径。

github · Qiaolin-Yu · Jul 25, 00:13

**背景**: 推测解码通过轻量级草稿模型生成候选 token，再由目标模型验证，从而加速 LLM 推理。SGLang 是一个开源的大模型服务框架，此版本基于 DeepSeek 的 DSpark 工作和 Thinking Machines Lab 的开源权重模型 Inkling 的最新进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#LLM serving`, `#speculative decoding`, `#SGLang`, `#high-throughput inference`, `#MoE`

---

<a id="item-11"></a>
## [Postgres LISTEN/NOTIFY 可达每秒 6 万条通知](https://www.dbos.dev/blog/postgres-listen-notify-scalability) ⭐️ 8.0/10

DBOS 的一项基准测试表明，Postgres LISTEN/NOTIFY 每秒能处理 6 万条通知，直接反驳了该功能不具可扩展性的普遍看法。 这一证据为 Postgres 用户评估在生产环境中使用 LISTEN/NOTIFY 提供了具体数据，可能减少对外部消息队列的依赖，尤其适合需要强一致性和实时通知的应用。 测试在中档机器上完成，达到了每秒 6 万条通知；但可扩展性是一个连续谱，实际限制取决于载荷大小和监听者数量等因素。

hackernews · KraftyOne · Jul 24, 19:05

**背景**: Postgres LISTEN/NOTIFY 是一个内置的发布/订阅机制，允许数据库客户端在特定事件发生时接收异步通知。它常用于实时更新、缓存失效和简单消息传递，但一些人认为它只适用于小规模工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/current/sql-notify.html">PostgreSQL : Documentation: 18: NOTIFY</a></li>
<li><a href="https://www.compilenrun.com/docs/database/postgresql/postgresql-advanced-features/postgresql-listen-notify/">PostgreSQL LISTEN / NOTIFY - Real-time... | Compile N Run</a></li>
<li><a href="https://medium.com/@atarax/demystifying-postgresqls-listen-notify-12fe9c2a3907">Implementing pub-sub architecture swiftly using Postgres 's LISTEN ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员指出，可扩展性是一个连续谱而非二元的，每秒 6 万条对某些应用过多，对另一些则不够。一位用户分享了将 LISTEN/NOTIFY 扩展到每天数百万条通知的成功案例，另一位则回忆了早期已修复的性能问题。

**标签**: `#postgresql`, `#scalability`, `#message-queue`, `#performance`, `#database`

---

<a id="item-12"></a>
## [英伟达、微软和 Meta 警告不要过度监管开放权重模型](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html) ⭐️ 8.0/10

英伟达、微软和 Meta 于 2026 年 7 月 24 日联合发出一封公开信，警告不要过度监管开放权重 AI 模型，认为这将损害创新和美国的国家竞争力。 这标志着开放权重支持者与推动更严格监管者之间的重大政策分歧，可能影响美国如何对待 AI 治理，并对全球开源 AI 发展产生冲击。 该信特别针对可能限制开放权重模型发布的拟议法规，认为此类举措会将 AI 领导权拱手让给中国，并扼杀美国的创新。

hackernews · louiereederson · Jul 24, 13:32

**背景**: 开放权重模型是指其训练参数被公开发布的人工智能系统，任何人都可以下载、运行、研究或修改它们。这与闭源模型形成对比，后者只能访问模型的输出。随着前沿模型能力越来越强，关于开放权重监管的争论日益激烈，一些人主张安全控制，另一些人则警告过度监管可能阻碍进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://openai.com/global-affairs/open-weights-and-ai-for-all/">Open weights and AI for all | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 对这封信的评论反映了社区的分化：一些用户批评 Anthropic 的监管立场，并指出使用中国模型（如 Kimi K3）进行安全讨论的讽刺之处；另一些人则将其与 SOPA 抗议相类比，并对这些公司的动机表示好奇。一位版主还链接了关于中国开放权重 AI 以及 OpenAI 与 Anthropic 联合反对开放权重风险的相关讨论。

**标签**: `#regulation`, `#open-weight`, `#AI policy`, `#Nvidia`, `#Microsoft`

---

<a id="item-13"></a>
## [Cloudflare 揭示传输提供商广泛操纵 BGP ORIGIN 属性](https://blog.cloudflare.com/bgp-origin-attribute/) ⭐️ 8.0/10

Cloudflare 的研究表明，近 70% 的 BGP 路径经历传输提供商为了获取流量优势而重写 ORIGIN 属性。 这种广泛的操纵破坏了 BGP 路由安全，可能影响路径选择，导致流量误定向和增加劫持风险。 ORIGIN 属性通常由起源 AS 设置，但传输提供商重写它以操纵 BGP 最佳路径选择算法，通常是为了优先选择自己的路由。

rss · Cloudflare Blog · Jul 24, 17:25

**背景**: BGP（边界网关协议）是指导互联网流量的路由协议。ORIGIN 属性是 BGP 路径选择过程中使用的多个路径属性之一，指示路由的学习方式。根据 BGP 标准，传输提供商不应修改它。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/bgp-origin-attribute/">BGP ORIGIN attribute manipulation and its impact on the Internet</a></li>
<li><a href="https://ipcisco.com/lesson/bgp-path-attributes-origin/">BGP Path Attributes - Origin | BGP Origin Attribute IPCisco</a></li>

</ul>
</details>

**标签**: `#BGP`, `#internet routing`, `#network security`, `#Cloudflare`

---

<a id="item-14"></a>
## [印度政府要求 GitHub 移除蓝牙聊天应用 Bitchat](https://www.thehindu.com/news/national/government-orders-github-to-remove-bluetooth-based-chat-app-bitchat-over-security-concerns-jack-dorsey/article71262049.ece) ⭐️ 7.0/10

印度政府向 GitHub 发出下架命令，要求移除 Bitchat 应用，理由是该应用可能被反国家分子、恐怖组织和犯罪分子滥用。 这凸显了政府对去中心化、抗审查通信工具的审查，引发开发者和隐私倡导者的担忧。这反映了印度在 2008 年孟买袭击后对所有通信进行监控的严格立场。 Bitchat 是一款基于蓝牙的通讯应用，无需手机号，支持离线加密通信，且不收集元数据。该命令据称由印度计算机应急响应小组（CERT-In）发出。

hackernews · rootkea · Jul 24, 14:41

**背景**: Bitchat 是一款点对点聊天应用，利用蓝牙和网状网络实现无需互联网连接的通信，这使得政府难以监控或封锁。印度历史上对可能绕过监控的通信技术实施严格管制，包括卫星电话和 VoIP。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@rajinderdevstory/what-is-bitchat-app-a-complete-guide-for-users-and-developers-in-2025-23fda96ebd68">What Is Bitchat App ? A Complete Guide for Users and... | Medium</a></li>
<li><a href="https://bitchat.free/">bitchat</a></li>

</ul>
</details>

**社区讨论**: 评论表达了怀疑态度：一些人批评政府的理由是为了控制通信，而另一些人则指出 2008 年孟买袭击后的安全背景。一条评论提及正在进行的抗议活动以及政府封锁公共通信的措施。总体情绪对政府的动机持批评态度。

**标签**: `#censorship`, `#open-source`, `#india`, `#bluetooth`, `#privacy`

---

<a id="item-15"></a>
## [Buz: 基于现代 Zig 的 Bun 分支，实现亚秒级增量构建](https://ziggit.dev/t/buz-a-drop-in-replacement-for-bun-using-modern-zig-with-sub-1s-incremental-builds/16891) ⭐️ 7.0/10

Buz 是 Bun JavaScript 运行时的一个分支，通过使用现代 Zig 重写，实现了亚秒级增量构建，并移除了原代码库中超过 11,000 行的死代码。 这表明 Bun 的构建性能本可以一直更快，并凸显了代码维护的重要性。它可能影响未来的运行时开发和社区对代码质量的期望。 该分支仍有一些注意事项：Zig 增量编译尚不支持 aarch64，且只有 Linux 链接器支持二进制补丁。该项目大量依赖 LLM 进行代码清理，一些社区成员对此提出了批评。

hackernews · kristoff_it · Jul 24, 09:26

**背景**: Bun 是一个快速的全能 JavaScript 运行时，最初使用 Zig 构建。Zig 是一种专注于健壮性和性能的系统编程语言。增量构建只编译更改过的代码，从而加快开发速度。这个分支 Buz 对 Zig 代码库进行了现代化改造，以缩短构建时间并消除死代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>

</ul>
</details>

**社区讨论**: 评论者对 11,000 行死代码表示惊讶，并讨论了使用 LLM 进行清理的做法。一些人认为该分支是功能开发与代码维护之间“嘀嗒”循环的一个有价值的例子，而另一些人则质疑依赖 AI 来修复 AI 生成的代码的做法。

**标签**: `#bun`, `#zig`, `#incremental builds`, `#runtime`, `#code quality`

---

<a id="item-16"></a>
## [Black Forest Labs 发布 FLUX 3 多模态流模型](https://www.latent.space/p/ainews-black-forest-labs-flux-3-multimodal) ⭐️ 7.0/10

Black Forest Labs 发布了 FLUX 3，这是一个多模态流模型，据称性能超越了 Seedance 2.0、Gemini Omni 和 Grok Imagine，同时还推出了名为 FLUX-mimic 的机器人模型。 此次发布标志着多模态 AI 的重大进步，通过提供一个在多种任务和模态中表现出色的统一模型，可能改变竞争格局。 FLUX 3 基于 Self-Flow 技术，在单一架构内对齐多模态生成与理解，而 FLUX-mimic 则面向视频动作机器人应用。

rss · Latent Space · Jul 24, 04:30

**背景**: 多模态流模型将流匹配与跨模态交互相结合，处理文本、图像和视频等多种数据类型。Seedance 2.0 是字节跳动推出的文本生成视频模型，以逼真的视频生成著称。Black Forest Labs 是专注于生成模型的一流 AI 研究实验室。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bfl.ai/blog/flux-3">FLUX 3 - Real World Models : Towards Multimodal Flow Models as...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Seedance_2.0">Seedance 2.0</a></li>

</ul>
</details>

**标签**: `#AI`, `#multimodal`, `#FLUX`, `#robotics`, `#model release`

---