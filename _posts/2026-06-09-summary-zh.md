---
layout: default
title: "Horizon Summary: 2026-06-09 (ZH)"
date: 2026-06-09
lang: zh
---

> From 140 items, 16 important content pieces were selected

---

1. [小米千亿参数模型实现每秒千词推理](#item-1) ⭐️ 9.0/10
2. [苹果发布 Core AI 框架，取代 Core ML](#item-2) ⭐️ 9.0/10
3. [Signal 警告英国监控提案威胁隐私](#item-3) ⭐️ 9.0/10
4. [伊朗战争迫使能源进口国转向国内资源](#item-4) ⭐️ 9.0/10
5. [伊朗、以色列与黎巴嫩之间冲突升级](#item-5) ⭐️ 9.0/10
6. [习近平抵达朝鲜，旨在修复紧张关系](#item-6) ⭐️ 9.0/10
7. [OpenAI 秘密提交 S-1 文件筹备上市](#item-7) ⭐️ 8.0/10
8. [AI 发展趋缓，行业需到 2030 年收入 3 万亿美元](#item-8) ⭐️ 8.0/10
9. [马萨诸塞州通过隐私法案，禁止出售精确位置数据](#item-9) ⭐️ 8.0/10
10. [瑞士将公投限制人口不超过 1000 万](#item-10) ⭐️ 8.0/10
11. [赛默飞抗体数据疑似广泛造假](#item-11) ⭐️ 8.0/10
12. [llama.cpp b9562 新增视频输入支持](#item-12) ⭐️ 7.0/10
13. [Browser-use 0.13.0 推出基于 Rust 的测试版 AI 浏览器控制代理](#item-13) ⭐️ 7.0/10
14. [苹果将谷歌 Gemini 集成到 AI 架构中](#item-14) ⭐️ 7.0/10
15. [欧盟禁用农药在进口大米、茶叶和香料中被检出](#item-15) ⭐️ 7.0/10
16. [Cloudflare 将威胁情报转化为实时 WAF 规则](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [小米千亿参数模型实现每秒千词推理](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) ⭐️ 9.0/10

小米发布了 MiMo-v2.5-Pro-UltraSpeed，这是一个万亿参数（1T）模型，在商用 GPU 上实现了每秒 1000 tokens 的推理速度，这得益于其 TileRT 协同设计。UltraSpeed 模式的输出速度约为标准 MiMo-V2.5-Pro API 的 10 倍，成本极低。 这一突破大幅降低了推理成本和延迟，可能改变 AI 部署策略和竞争格局。它可能加速实时 AI 应用的发展，并迫使其他提供商在性能和定价上追赶。 该模型通过 TileRT 的极致模型-系统协同设计，在商用 GPU 上实现了每秒 1000 tokens。UltraSpeed 模式的定价与 DeepSeek 相当，而常规的 MiMo-V2.5-Pro 在独立基准测试中仍是最强的开放权重代理编码模型。

hackernews · gainsurier · Jun 8, 15:27

**背景**: 万亿参数的大语言模型通常需要昂贵的硬件且推理速度缓慢。小米的 MiMo 系列专注于平衡模型规模、速度和成本。UltraSpeed 变体利用专门系统优化大幅提升生成速度而不牺牲质量，使高性能 AI 更易获取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/blog/mimo-tilert-1000tps">Xiaomi MiMo, Explore and Love</a></li>
<li><a href="https://platform.xiaomimimo.com/docs/en-US/model-intro/mimo-v2.5-pro-ultraspeed">Xiaomi MiMo API Open Platform</a></li>
<li><a href="https://www.gizmochina.com/2026/06/09/xiaomi-mimo-v2-5-pro-ultraspeed-mode-1000-tokens-per-second/">Xiaomi MiMo-V2.5-Pro gets UltraSpeed Mode, breaks 1,000 ... - Gizmochina</a></li>

</ul>
</details>

**社区讨论**: 社区成员反应不一：有人为速度提升带来的生产力感到兴奋，也有人担心工作模式改变（例如匆忙而非深入思考）。大家一致认为中国供应商的价格压力将重塑市场，且 MiMo 的质量相对于其性能被低估了。

**标签**: `#AI`, `#inference speed`, `#cost reduction`, `#Xiaomi`, `#competitive dynamics`

---

<a id="item-2"></a>
## [苹果发布 Core AI 框架，取代 Core ML](https://developer.apple.com/documentation/coreai/) ⭐️ 9.0/10

苹果宣布了 Core AI 新框架，该框架能将 PyTorch 模型转换为可在 CPU、GPU 和 Apple Neural Engine (ANE) 上运行，从 iOS 27 起有效取代 Core ML。 这一转变使 Core AI 成为 Apple 平台上设备端 AI 的标准，使开发者能够高效地在所有 Apple 硬件上部署更强大的模型。 Core AI 支持量化（w4a8、w4a16），并伴随 WWDC 2026 会议详细介绍了模型创作、优化和集成。

hackernews · hmokiguess · Jun 8, 18:47

**背景**: Core ML 是苹果于 2017 年推出的设备端机器学习框架，支持模型转换但仅限于自有格式。Apple Neural Engine (ANE) 首次出现在 A11 芯片中，能高效加速 AI 任务。Core AI 旨在统一和现代化设备端 AI，直接支持 PyTorch 并提供更好的跨硬件优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/core-ai/">Core AI - Apple Developer</a></li>
<li><a href="https://udit.co/blog/apple-core-ai-replaces-core-ml-wwdc-ios-27">Apple replacing Core ML with Core AI at WWDC 2026 changes e</a></li>
<li><a href="https://byteiota.com/apple-core-ai-replaces-core-ml-ios-27/">Apple Core AI Replaces Core ML in iOS 27: Act Now | byteiota</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_Neural_Engine">Apple Neural Engine</a></li>

</ul>
</details>

**社区讨论**: 社区成员对设备端基础模型更新和量化支持感到兴奋，一些人指出大多数 AI 魔法可以蒸馏为在设备上运行的小模型。关于 Core AI 是否完全取代 Core ML 的问题也随之出现。

**标签**: `#apple`, `#ai`, `#on-device-ai`, `#coreml`, `#pytorch`

---

<a id="item-3"></a>
## [Signal 警告英国监控提案威胁隐私](https://signal.org/blog/pdfs/2026-06-08-uk-surveillance-is-not-safety.pdf) ⭐️ 9.0/10

Signal 发布声明反对英国新监控提案，该提案强制要求年龄验证和基于 AI 的监控，认为这些措施破坏了加密和隐私。 这一事件意义重大，因为它标志着政府监控的急剧升级，可能成为全球先例，迫使科技公司实施侵入性的客户端扫描，并可能破坏端到端加密。 提案要求对内容访问进行强制年龄验证，并对通信进行实时 AI 监控，Signal 认为这将危及所有用户的安全。

hackernews · g0xA52A2A · Jun 8, 19:42

**背景**: 英国的《在线安全法案 2023》已经要求对有害内容进行年龄验证。新提案更进一步，要求客户端扫描和远程认证以强制执行，实质上迫使设备监视其用户自身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Age_verification_system">Age verification - Wikipedia</a></li>
<li><a href="https://www.brookings.edu/articles/how-ai-can-enable-public-surveillance/">How AI can enable public surveillance | Brookings</a></li>

</ul>
</details>

**社区讨论**: 评论者表达担忧，认为该提案可能导致“每部手机里都有告密者”和“人工智能斯塔西”监控国家。一些人指出具有讽刺意味的是，行业开发的安全启动和 DRM 等技术正被政府重新用于大规模监控。

**标签**: `#privacy`, `#surveillance`, `#regulation`, `#UK`, `#encryption`

---

<a id="item-4"></a>
## [伊朗战争迫使能源进口国转向国内资源](https://www.nytimes.com/2026/06/08/business/energy-environment/iran-war-energy-oil.html) ⭐️ 9.0/10

这一转变标志着全球能源战略的根本性变化，可能减少对中东石油的依赖，重塑国际能源贸易格局，并推动可再生能源和国内化石燃料生产的投资增加。 各国正同时专注于可再生能源项目和国内化石燃料开采，以增强能源安全。战争带来了前所未有的供应风险，使自给自足成为许多政府的首要任务。

rss · NYTimes World · Jun 8, 17:56

**背景**: 伊朗是重要的石油和天然气生产国，战争扰乱了其出口，导致价格飙升和供应短缺。长期以来，能源进口国（尤其是亚洲和欧洲国家）依赖廉价的中东能源，但这场冲突正迫使它们转向更具韧性的本地化供应链。

**标签**: `#energy`, `#geopolitics`, `#Iran`, `#oil`, `#energy security`

---

<a id="item-5"></a>
## [伊朗、以色列与黎巴嫩之间冲突升级](https://www.nytimes.com/live/2026/06/08/world/iran-israel-lebanon-attacks/heres-the-latest) ⭐️ 9.0/10

《纽约时报》正在实时报道伊朗、以色列和黎巴嫩之间一系列不断升级的军事攻击，表明地区敌对行动显著升级。 这场危机对全球安全、能源市场和军事战略具有直接影响，因为它涉及中东地区的关键参与者，并有可能引发更广泛的冲突。 来自《纽约时报》等主要消息源的实时报道提供了事件发展的官方更新，这可能改变地区风险态势并引发国际反应。

rss · NYTimes World · Jun 8, 20:18

**背景**: 中东地区伊朗和以色列之间长期存在紧张关系，黎巴嫩因真主党（Hezbollah）的存在而经常卷入。这条新闻表明直接对抗达到了新的高峰。

**标签**: `#Geopolitics`, `#Middle East`, `#Iran`, `#Israel`, `#Lebanon`

---

<a id="item-6"></a>
## [习近平抵达朝鲜，旨在修复紧张关系](https://www.theguardian.com/world/2026/jun/08/xi-jinping-kim-jong-un-meeting-north-korea) ⭐️ 9.0/10

习近平抵达平壤进行为期两天的访问，这是近七年来他首次访问朝鲜，表明中方有意振兴因平壤与俄罗斯关系密切而紧张的双边关系。 此次访问具有重要地缘政治意义，可能改变地区联盟格局，影响东亚力量平衡和全球风险态势，尤其是在朝鲜与俄罗斯关系升温的背景下。 访问为期两天，中国新华社发布的画面显示，习近平与夫人彭丽媛乘坐中国国际航空航班抵达平壤顺安国际机场。

rss · The Guardian World · Jun 8, 10:46

**背景**: 中国和朝鲜是传统盟友，但近期因平壤与俄罗斯加强关系（尤其在乌克兰战争背景下），双方关系有所冷却。此次访问是自 2019 年以来习近平首次访朝，旨在重申中国对邻国的影响力。

**标签**: `#geopolitics`, `#China`, `#North Korea`, `#international relations`

---

<a id="item-7"></a>
## [OpenAI 秘密提交 S-1 文件筹备上市](https://openai.com/index/openai-submits-confidential-s-1/) ⭐️ 8.0/10

OpenAI 已确认向美国证券交易委员会秘密提交了 S-1 注册声明草案，表明其有意上市，但尚未确定具体时间表。 此次提交是这家最具影响力的人工智能公司迈向 IPO 的重要一步，可能重塑 AI 行业的资本流动，并影响其他主要参与者的估值。 此次提交是秘密进行的，OpenAI 表示尚未决定具体时间，并补充说目前有些事情作为私营公司操作更为便利。

hackernews · OpenAI News · Jun 8, 21:22

**背景**: S-1 草案是向美国证券交易委员会提交的首次公开募股（IPO）注册声明。秘密提交允许公司在接近公开发行前保持财务和计划的私密性。以 ChatGPT 和 GPT-4 闻名的 OpenAI，正在从非营利向营利结构转型。

**社区讨论**: 社区评论表达了怀疑态度，有用户因 OpenAI 收入增长乏力、高现金消耗和负债而质疑其能否成功上市。其他人则担忧来自苹果的竞争，并注意到埃隆·马斯克对此的不满。

**标签**: `#OpenAI`, `#IPO`, `#SEC`, `#capital markets`, `#AI industry`

---

<a id="item-8"></a>
## [AI 发展趋缓，行业需到 2030 年收入 3 万亿美元](https://www.wheresyoured.at/ai-is-slowing-down/) ⭐️ 8.0/10

Ed Zitron 的分析认为，AI 发展正在减速，且行业必须在 2030 年底前产生超过 3 万亿美元的收入才能维持自身，这是基于基础设施和训练方面的巨大支出。 这一论断挑战了 AI 无限增长的主流叙事，如果投资者和高管认真对待，可能引发科技行业投资策略和商业模式的转变。 3 万亿美元的数字比当前估计高出一个数量级；红杉资本认为年度收入缺口为 5000 亿美元，高盛表示超大规模企业需要每年 1 万亿美元的利润才能证明其支出的合理性。

hackernews · crescit_eundo · Jun 8, 15:46

**背景**: “神经规模定律”的概念表明，AI 性能随参数、数据和计算量的增加而提升。然而，行业可能正面临收益递减和成本攀升。Ed Zitron 的文章警告，如果 AI 不能产生足够收入，当前的投资热潮可能导致泡沫破裂，类似于过去的科技泡沫。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/markbodger_the-ai-industry-needs-a-billion-paying-customers-activity-7438871743529697280-bc1q">AI Industry Revenue Gap: $500B | Mark Bodger ACMA... | LinkedIn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：有人质疑 3 万亿美元数字的准确性，并指出 AI 有实际用途如编程；另一些人则批评文章的语气和逻辑。少数人认为苹果等公司的消费级 AI 产品可能减少对独立 AI 订阅的需求。

**标签**: `#AI`, `#economics`, `#business`, `#investment`, `#policy`

---

<a id="item-9"></a>
## [马萨诸塞州通过隐私法案，禁止出售精确位置数据](https://techcrunch.com/2026/06/08/massachusetts-votes-to-pass-new-privacy-rights-bill-that-bans-sale-of-precise-location-data/) ⭐️ 8.0/10

马萨诸塞州通过了一项新的隐私权利法案，明确禁止出售精确位置数据，加入了州级监管趋势。 这表明州级层面正在大力遏制位置数据的商业利用，可能影响联邦政策，保护消费者隐私免受侵入性追踪。 该法案针对的是“出售”精确位置数据，但社区评论指出“交换”或“转移”等措辞可能成为漏洞。加州也通过了类似法律，通用汽车因转售 OnStar 数据被罚款。

hackernews · 01-_- · Jun 8, 17:07

**背景**: 精确位置数据由应用程序、设备和车辆收集以跟踪用户移动。此类数据经常未经明确同意被出售给广告商、数据中间商或执法机构。像这样的州隐私法旨在让居民更好地控制自己的个人信息。

**社区讨论**: 评论者普遍支持该法案，但表达了对漏洞的担忧：“出售”一词可能不涵盖交换或转移，且车辆数据可能被排除。有人指出，马萨诸塞州使用 Cellebrite 软件可能削弱位置隐私。

**标签**: `#privacy`, `#regulation`, `#location data`, `#Massachusetts`, `#data rights`

---

<a id="item-10"></a>
## [瑞士将公投限制人口不超过 1000 万](https://www.admin.ch/en/sustainability-initiative) ⭐️ 8.0/10

瑞士将举行全国公投，决定是否通过宪法动议将人口上限设为 1000 万，如果接近这一上限，可能会限制庇护和欧盟人员自由流动。 这可能从根本上改变瑞士的移民政策及其与欧盟的关系，因为该动议要求人口一旦超过 950 万就限制庇护和家庭团聚，并在达到 1000 万时可能导致瑞士退出欧盟的人员自由流动协定。 目前人口约为 910 万。该动议提议，在达到 950 万时停止庇护和家庭团聚，达到 1000 万时瑞士需终止与欧盟关于人员自由流动的双边协议。

hackernews · napolux · Jun 8, 19:09

**背景**: 瑞士实行直接民主制度，公民可通过公投决定宪法修正案。瑞士并非欧盟成员国，但参与申根区并与欧盟签订了包含人员自由流动的双边协议。该动议由瑞士人民党（SVP）支持，引发了关于可持续性、移民和主权的辩论。

**社区讨论**: 评论中表达了不同观点。一些瑞士选民指出仍有充足空间并反对这一上限。另一些人则认为这是一个陷阱，旨在触发“瑞士脱欧”并终止与欧盟的双边协议，并指出推动该动议的瑞士人民党曾反对可持续性立法具有讽刺意味。人们对动议背后的理由感到好奇，并对政治动态表示担忧。

**标签**: `#policy`, `#referendum`, `#immigration`, `#Switzerland`, `#EU`

---

<a id="item-11"></a>
## [赛默飞抗体数据疑似广泛造假](https://reeserichardson.blog/2026/05/28/how-much-of-thermo-fishers-antibody-data-has-been-manipulated/) ⭐️ 8.0/10

一篇博客文章分析赛默飞（Thermo Fisher）的抗体数据，揭示可能存在系统性造假，社区评论证实了长期以来的怀疑和资源浪费。 这破坏了生命科学研究的可重复性，造成数百万美元实验浪费，并削弱了对关键研究试剂主要供应商的信任。 举报人 Sholto David（曾揭露达纳-法伯癌症研究所的造假）主导了这项分析。赛默飞的某些抗体声名狼藉，迫使严肃实验室自行验证一切。

hackernews · mhrmsn · Jun 8, 06:56

**背景**: 抗体是生物学研究中检测蛋白质的关键试剂。生命科学的可重复性危机部分归因于验证不充分的抗体。像赛默飞这样的公司是主要供应商，但其质量控制多年来一直受到质疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41467-018-06642-y">Enhanced validation of antibodies for research applications</a></li>
<li><a href="https://www.abcam.com/en-us/stories/articles/what-is-the-reproducibility-crisis-in-life-sciences">What is the reproducibility crisis in life sciences ?</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7807291/">Antibody validation for protein expression on tissue slides: a protocol ...</a></li>

</ul>
</details>

**社区讨论**: 评论指出造假似乎是系统性的，有研究者提到多年前就发现 Ikaros 抗体是伪造的。其他人提到实际影响：浪费时间和金钱、撤稿论文以及需要独立验证。有评论者赞扬 Sholto David 的工作。

**标签**: `#scientific fraud`, `#thermo fisher`, `#antibodies`, `#reproducibility`, `#biotech`

---

<a id="item-12"></a>
## [llama.cpp b9562 新增视频输入支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9562) ⭐️ 7.0/10

llama.cpp 版本 b9562 通过 MTMD 库引入了视频输入支持，实现了包括视频、文本和图像在内的多模态处理能力。 此次更新大幅扩展了 llama.cpp 的能力，使开发者能够构建本地处理视频内容的应用程序，这对于视频摘要和分析等任务至关重要。这巩固了 llama.cpp 作为领先的开源多模态 AI 推理引擎的地位。 视频输入通过 MTMD（多模态数据）库实现，服务器端支持 base64 编码的视频输入，CLI 新增了 --video 参数。该版本还包括适用于 macOS、Linux、Windows 和 Android 等多个平台的预编译二进制文件。

github · github-actions[bot] · Jun 8, 16:41

**背景**: llama.cpp 是一个流行的开源 C++ 实现，用于在消费级硬件上高效运行大型语言模型（LLM）。在此版本之前，它通过 LLaVA 等多模态模型支持文本和图像输入。MTMD 库为处理多种数据模态提供了统一接口，使模型能够将视频帧处理为嵌入向量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md">llama.cpp/docs/multimodal.md at master · ggml-org/llama.cpp</a></li>
<li><a href="https://github.com/crc-org/llama.cpp/blob/main/tools/mtmd/README.md">llama.cpp/tools/mtmd/README.md at main · crc-org/llama.cpp</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#video input`, `#multimodal`, `#open-source`

---

<a id="item-13"></a>
## [Browser-use 0.13.0 推出基于 Rust 的测试版 AI 浏览器控制代理](https://github.com/browser-use/browser-use/releases/tag/0.13.0) ⭐️ 7.0/10

Browser-use 0.13.0 版本推出了一个基于 Rust 的测试版代理，它通过稳健的辅助工具而非脆弱的浏览器抽象层，提供更直接的浏览器控制循环。原有的 Python 代理保持不变。 该版本提升了 AI 驱动浏览器自动化的性能和可靠性，有望降低成本并提高可扩展性。这是该开源工具在 AI 代理生态系统中迈出的重要一步。 该测试版代理旨在让现代 AI 模型通过稳健的辅助工具获得更直接的浏览器控制循环。不过，它仍处于测试阶段，缺乏社区验证和定量基准，建议用户谨慎测试。

github · gregpr07 · Jun 8, 22:07

**背景**: Browser-use 是一个开源工具，允许 AI 代理控制 Web 浏览器执行自动化任务，如网页抓取和表单填写。随着开发者寻求更可靠的 AI 与网站交互方式，该项目的受欢迎程度不断增长。新的基于 Rust 的代理用更高效的控制循环取代了脆弱的抽象层，有望提高稳定性和速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://browser-use.com/">Browser Use - The way AI uses the internet</a></li>
<li><a href="https://github.com/browser-use/browser-use">GitHub - browser - use / browser - use : Make websites accessible for...</a></li>
<li><a href="https://medium.com/@ken_lin/browser-use-ai-web-browsing-is-here-but-its-far-from-perfect-426aa8720036">Browser - Use : AI Web Browsing Is Here — But It’s Far From... | Medium</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#browser automation`, `#Rust`, `#open source`, `#software engineering`

---

<a id="item-14"></a>
## [苹果将谷歌 Gemini 集成到 AI 架构中](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/) ⭐️ 7.0/10

苹果宣布了一种新的 AI 架构，集成了谷歌的 Gemini 模型，并通过其私有云计算系统强调设备端处理和隐私保护。 这标志着苹果的战略转变，在保持隐私优先立场的同时，利用谷歌先进的多模态模型，可能重塑 AI 助手市场的竞争格局。 苹果的架构利用设备端路由和私有云计算，确保用户数据不被苹果或第三方访问，并提供外部验证隐私保障。由于监管担忧，该集成尚未在欧盟推出。

hackernews · unclefuzzy · Jun 8, 19:14

**背景**: 谷歌 Gemini 是由 Google DeepMind 开发的一系列多模态大语言模型，能够处理文本、图像、音频和视频。它于 2023 年 12 月首次发布，此后发展出包括 Nano、Flash、Pro 和 Ultra 在内的版本，具有扩展的上下文窗口和代理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论表达了不同的反应：一些人认为这是苹果典型的将外部工具包装在隐私架构中的做法，而另一些人则质疑其新颖性，认为它与现有助手类似。评论者还希望欧盟能强制要求用户选择外部模型，一些人则对苹果的隐私声明表示怀疑。

**标签**: `#Apple`, `#AI`, `#Google Gemini`, `#privacy`, `#business strategy`

---

<a id="item-15"></a>
## [欧盟禁用农药在进口大米、茶叶和香料中被检出](https://www.foodwatch.org/en/eu-banned-pesticides-found-in-rice-tea-and-spices) ⭐️ 7.0/10

Foodwatch 发布的最新报告显示，由于“回旋镖效应”，欧盟禁用农药在进口大米、茶叶和香料等食品中被检出：欧盟国家向第三国出口禁用农药，这些国家随后将其用于出口至欧盟的作物。 这暴露了一个监管漏洞，削弱了欧盟的食品安全标准，导致消费者可能接触到欧盟境内已禁用的农药。同时，它也凸显了欧盟企业从销售有害农药到国外、最终污染进口食品这一获利行为的道德问题。 在 64 个样本中，有 14 个超过法定最大残留限量，其中 12 种农药未在欧盟获批。受影响最严重的产品包括干辣椒（6 个样本）、小茴香（3 个）、大米（2 个）、茶叶（1 个）、未发酵茶叶（1 个）和混合香料（1 个）。

hackernews · john-titor · Jun 8, 15:59

**背景**: “回旋镖效应”指的是欧盟公司将欧盟禁用或未批准的农药出口到监管较宽松的国家。这些农药随后被用于当地种植的粮食作物，而产出的农产品又出口回欧盟，常常带有这些禁用物质的残留。这一循环使得禁用农药间接进入了欧盟的食品供应链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.foodwatch.org/fileadmin/-INT/transparency_and_food_safety/documents/Foodwatch_background_paper-22-April_2020-Stop_the_poison_boomerang.pdf">Foodwatch report-21-April 2020-Stop the poison boomerang -final-2</a></li>
<li><a href="https://www.publiceye.ch/en/topics/pesticides/banned-in-europe">Banned in Europe : How the EU exports pesticides too dangerous for...</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了“回旋镖效应”是核心问题，有用户指出 64 个样本中有 14 个超出法定限量，包括 12 种未获批农药。另一条评论指出大多数检出值处于定量限水平，未必达到危险级别，而其他人则建议购买有机香料和茶叶以避免此类残留。

**标签**: `#pesticides`, `#food safety`, `#EU regulation`, `#trade policy`

---

<a id="item-16"></a>
## [Cloudflare 将威胁情报转化为实时 WAF 规则](https://blog.cloudflare.com/realtime-threat-intel-waf-rules/) ⭐️ 7.0/10

这一功能使安全团队能够直接在 WAF 中利用 Cloudforce One 的威胁情报，自动化防护并缩短响应时间，从而显著提升安全态势。 新的 cf.intel 字段提供了对 Cloudforce One 威胁行为者指标和行业目标数据的访问，无需编写自定义规则即可实现实时阻断。该集成对 Cloudflare WAF 客户可用。

rss · Cloudflare Blog · Jun 8, 13:00

**背景**: Cloudflare 的 WAF（Web 应用防火墙）通过过滤和监控 HTTP 流量来保护 Web 应用。Cloudforce One 是 Cloudflare 的威胁情报团队和平台，提供关于网络攻击和威胁行为者的实时情报。新的集成将这两个服务连接起来，使威胁情报能够直接为 WAF 规则提供依据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloudflare-docs-7ou.pages.dev/security-center/cloudforce-one/">Cloudforce One · Cloudflare Security Center docs</a></li>
<li><a href="https://www.linkedin.com/posts/securitysenses_cloudflare-expands-threat-intelligence-offering-activity-7307945788821651456-LVBE">Cloudflare launches Cloudforce One for real-time... | LinkedIn</a></li>
<li><a href="https://assets.ctfassets.net/slt3lc6tev37/1MqssP7WjDzWYfZHllzUd0/04da47c276609b78a62e6fcea3403991/BDES-6048-cloudforce-one-data-sheet.pdf">Cloudforce One</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#WAF`, `#threat intelligence`, `#security automation`, `#real-time`

---