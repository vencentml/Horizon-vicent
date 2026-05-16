---
layout: default
title: "Horizon Summary: 2026-05-16 (ZH)"
date: 2026-05-16
lang: zh
---

> From 138 items, 16 important content pieces were selected

---

1. [Project Zero 披露 Pixel 10 零点击漏洞链](#item-1) ⭐️ 9.0/10
2. [特朗普在与习近平会晤后警告台湾勿宣布独立](#item-2) ⭐️ 9.0/10
3. [刚果宣布爆发大规模埃博拉疫情，数百人感染](#item-3) ⭐️ 9.0/10
4. [乌克兰的人工智能武器先驱](#item-4) ⭐️ 9.0/10
5. [阿联酋 2027 年建成第二条霍尔木兹海峡绕行管道](#item-5) ⭐️ 9.0/10
6. [美国计划或削减科罗拉多河 40%供水](#item-6) ⭐️ 9.0/10
7. [监察机构称五角大楼废除了法定的平民伤亡预防计划](#item-7) ⭐️ 9.0/10
8. [vLLM v0.21.0 发布：重大变更、KV 卸载与 Blackwell 后端](#item-8) ⭐️ 8.0/10
9. [Zulip 转型为非营利基金会，创始人前往 Anthropic](#item-9) ⭐️ 8.0/10
10. [美国司法部要求苹果和谷歌交出 10 万多名汽车应用用户身份](#item-10) ⭐️ 8.0/10
11. [专家建议独立创业者避免 SOC2 Type 2](#item-11) ⭐️ 8.0/10
12. [npm 的 postinstall 脚本：讽刺凸显反复出现的安全问题](#item-12) ⭐️ 7.0/10
13. [加州法案要求停运网游提供补丁或退款](#item-13) ⭐️ 7.0/10
14. [OCaml/OxCaml 太空应用：GC 优化显著降低延迟](#item-14) ⭐️ 7.0/10
15. [Waymo 因涉水故障召回 3800 辆机器人出租车](#item-15) ⭐️ 7.0/10
16. [Bun 的 Rust 重写在安全 API 中暴露未定义行为](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Project Zero 披露 Pixel 10 零点击漏洞链](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

Google Project Zero 公开披露了一个针对 Pixel 10 的完整零点击漏洞利用链，展示了远程音频解码漏洞如何导致完全的内核控制。该链利用 Dolby 解码漏洞和视频驱动程序漏洞，谷歌在 90 天内相对较快地修复了这些问题。 此漏洞利用链凸显了移动设备上 AI 驱动的消息解码功能所引入的扩展攻击面，这些功能无需用户交互即可预处理媒体。它强调了在 Android 生态系统中快速打补丁的迫切需求，并提高了对基于 AI 的攻击面新兴威胁的认识。 该零点击漏洞利用链无需用户交互；它使用 CVE-2025-54957（Dolby 音频解码漏洞）进行初始攻击，然后利用视频驱动程序漏洞进行内核提权。谷歌的补丁速度对于 Android 驱动程序漏洞来说非常快，但该漏洞直到 2026 年 1 月仍存在于所有 Android 设备上。

hackernews · happyhardcore · May 15, 13:39

**背景**: 零点击漏洞利用是一种无需用户交互（例如点击链接）的攻击类型，可以静默地攻破设备。Google 的 Project Zero 团队研究此类漏洞以提高平台安全性。现代手机上的 AI 功能通常会自动解码消息和媒体以实现搜索和预览，这无意中增加了零点击漏洞利用的攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://projectzero.google/2026/05/pixel-10-exploit.html">A 0-click exploit chain for the Pixel 10: When a Door Closes, a Window ...</a></li>
<li><a href="https://cyberpress.org/zero-click-exploit-chain-for-pixel-10/">Google Project Zero Reveals Zero-Click Exploit Chain for Pixel 10</a></li>
<li><a href="https://gbhackers.com/pixel-10-zero-click-exploit-chain/">Google Project Zero Details Pixel 10 Zero-Click Exploit Chain</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 AI 驱动的功能在用户交互前处理消息表示担忧，一位评论者质疑为什么手机在未经用户同意的情况下解码短信。另一位指出谷歌在 90 天内修复 Android 驱动程序漏洞异常迅速，引发了对 Android 其他部分补丁速度的疑问。还有关于已发布漏洞利用总体上是否增加以及 AI 是否正在放大攻击能力的讨论。

**标签**: `#security`, `#zero-click exploit`, `#Android`, `#AI attack surface`, `#mobile`

---

<a id="item-2"></a>
## [特朗普在与习近平会晤后警告台湾勿宣布独立](https://www.bbc.com/news/articles/ce8p61v7l68o?at_medium=RSS&at_campaign=rss) ⭐️ 9.0/10

特朗普总统在与中国领导人习近平会晤后，警告台湾不要宣布独立，并呼吁北京和台北之间保持冷静。 这一声明重申了美国对台海现状的承诺，可能缓和紧张局势，影响地缘政治风险和全球市场。 这一警告是在特朗普与习近平会晤数小时后发出的，标志着美国对华政策转向更具合作性的立场，并考验了美国长期以来的承诺——在同台湾打交道时不咨询北京。

rss · BBC World News · May 15, 21:28

**背景**: 自 1979 年以来，美国一直奉行“一个中国”政策，承认北京关于台湾是中国一部分的立场，同时与台湾保持非官方关系。美国的传统政策是阻止台独，并反对单方面改变现状。特朗普的警告与此一致，但正值美中关系动态变化之际。

**标签**: `#geopolitics`, `#Taiwan`, `#US-China`, `#policy`, `#tensions`

---

<a id="item-3"></a>
## [刚果宣布爆发大规模埃博拉疫情，数百人感染](https://www.nytimes.com/2026/05/15/world/africa/congo-ebola-outbreak.html) ⭐️ 9.0/10

非洲卫生当局宣布刚果爆发大规模埃博拉疫情，导致数十人死亡、数百人疑似感染，专家对延迟公布感到震惊。 此次疫情存在区域和全球扩散的重大风险，威胁公共卫生体系、旅行及地缘政治稳定。 此次疫情涉及数十人死亡和数百例疑似感染，专家对延迟公布感到震惊，暗示可能存在漏报。

rss · NYTimes World · May 15, 18:15

**背景**: 埃博拉是一种严重且常致命的病毒性疾病，症状包括发烧和内出血。刚果曾多次爆发埃博拉疫情，最大的一次发生在 2018-2020 年，凸显快速反应和国际协调的必要性。

**标签**: `#Ebola`, `#outbreak`, `#Congo`, `#public health`, `#global risk`

---

<a id="item-4"></a>
## [乌克兰的人工智能武器先驱](https://www.nytimes.com/2026/05/15/world/europe/mykhailo-fedorov-ukraine-ai.html) ⭐️ 9.0/10

乌克兰国防部长米哈伊洛·费多罗夫正领导将人工智能驱动的自主武器和机器人系统作为该国对抗俄罗斯国防战略核心的部署。 这标志着现代战争模式的转变，展示了人工智能和机器人技术如何在与更大对手的对抗中创造公平竞争环境，对全球军事预算、战术和军备控制产生深远影响。 35 岁的费多罗夫是全球最年轻的国防部长之一，他的关注点包括无人机、自主车辆和人工智能瞄准系统等前沿技术。

rss · NYTimes World · May 15, 13:41

**背景**: 自 2022 年俄罗斯全面入侵以来，乌克兰大力投资无人机系统和人工智能，应用于侦察和攻击。自主武器能在无直接人工控制下选择和打击目标，这一技术虽有争议，但可能成为决定性的军事能力突破。

**标签**: `#AI warfare`, `#military technology`, `#Ukraine`, `#autonomous weapons`, `#defense strategy`

---

<a id="item-5"></a>
## [阿联酋 2027 年建成第二条霍尔木兹海峡绕行管道](https://www.theguardian.com/business/2026/may/15/uae-oil-pipeline-strait-of-hormuz-by-2027) ⭐️ 9.0/10

阿联酋宣布将建设第二条绕过霍尔木兹海峡的石油管道，预计 2027 年完工，届时其通过替代路线的原油出口能力将翻倍。 此举降低了全球石油供应对霍尔木兹海峡中断的脆弱性，可能稳定能源价格并改变该地区的地缘政治博弈格局。 该管道由国家石油公司加速推进，此前未公开。它将使阿联酋绕过霍尔木兹海峡的出口能力翻倍——目前该海峡已因封锁中断近 11 周。

rss · The Guardian World · May 15, 11:28

**背景**: 霍尔木兹海峡是连接波斯湾产油国与全球市场的狭窄水道，全球约 20%的石油和海运天然气经过此处。持续 11 周的封锁已导致能源价格飙升。新管道为这一战略咽喉提供了替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/business/2026/may/15/uae-oil-pipeline-strait-of-hormuz-by-2027">UAE to complete second oil pipeline bypassing strait of Hormuz by...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-05-15/uae-to-complete-new-hormuz-bypass-oil-pipeline-by-2027">UAE Plans New Oil Pipeline to Bypass Strait of Hormuz by 2027</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#oil pipeline`, `#strait of hormuz`, `#supply chain`

---

<a id="item-6"></a>
## [美国计划或削减科罗拉多河 40%供水](https://www.theguardian.com/us-news/2026/may/15/us-plan-colorado-river-california-arizona-nevada) ⭐️ 9.0/10

特朗普政府提出一项计划，由于严重干旱和水库水位骤降，可能将科罗拉多河对亚利桑那州、加利福尼亚州和内华达州的供水量削减高达 40%。 该提案代表了一项重大政策转变，影响数百万人的供水和关键农业区域，可能引发经济中断和各州间的水权冲突。 该计划由亚利桑那州一位高级水务官员在周三的州会议上公布，此前七个流域州未能就削减用水量达成自愿协议。

rss · The Guardian World · May 16, 00:44

**背景**: 科罗拉多河为美国西南部和墨西哥的超过 4000 万人供水，并灌溉 550 万英亩农田。数十年的干旱和过度分配导致其两个最大水库——米德湖和鲍威尔湖——水位降至历史最低点，迫使联邦政府进行干预。

**标签**: `#water crisis`, `#Colorado River`, `#policy`, `#drought`, `#resource management`

---

<a id="item-7"></a>
## [监察机构称五角大楼废除了法定的平民伤亡预防计划](https://www.theguardian.com/us-news/2026/may/15/pentagon-civilian-death-program) ⭐️ 9.0/10

据美国国防部监察长 2026 年 5 月的一份报告，五角大楼已悄然解散了其平民保护卓越中心及相关平民伤亡预防计划，违反了要求运营这两项计划的两项联邦法规。 这一发现表明，美军缺乏预防和应对平民伤害的基础设施，削弱了其履行法律义务的能力，并可能在未来行动中增加平民死亡。 监察报告指出，五角大楼不再拥有人力、工具或基础设施来遵守《国防授权法》中关于平民伤亡政策和平民保护卓越中心的规定。

rss · The Guardian World · May 15, 21:34

**背景**: 平民保护卓越中心是国防部‘减轻和应对平民伤害行动计划’的机构核心。包括 2018 和 2019 财年《国防授权法》在内的联邦法规要求国防部维持一项平民伤亡政策，并指定一名高级官员负责监督。该中心旨在成为减少军事行动中平民伤害的‘金标准’机构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/us-news/2026/may/15/pentagon-civilian-death-program">Pentagon quietly shut legally required program to prevent civilian ...</a></li>
<li><a href="https://lieber.westpoint.edu/dod-issues-civilian-harm-mitigation-response-action-plan/">An Improved Approach to Civilian Harm Mitigation and Response: The...</a></li>
<li><a href="https://www.justsecurity.org/69088/preventing-and-responding-to-civilian-casualties-an-upcoming-discussion-on-law-policy-and-progress/">Preventing and Responding to Civilian Casualties : An Upcoming...</a></li>

</ul>
</details>

**标签**: `#policy`, `#military`, `#civilian casualties`, `#US government`, `#watchdog`

---

<a id="item-8"></a>
## [vLLM v0.21.0 发布：重大变更、KV 卸载与 Blackwell 后端](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 8.0/10

vLLM v0.21.0 引入了构建层面的重大变更（需 C++20 编译器且弃用 transformers v4），新增基于混合内存分配器（Hybrid Memory Allocator）的 KV 卸载功能、支持推理预算的推测解码，以及面向 Blackwell GPU 的全新 TOKENSPEED_MLA 后端。 此版本要求用户升级工具链和库，影响广泛；同时为内存管理和 NVIDIA Blackwell GPU 上的高性能推理（尤其是 DeepSeek-R1 等推理模型）解锁了新能力，意义重大。 C++20 编译要求和 transformers v5 弃用是重大变更。KV 卸载结合 HMA 包含调度器端滑动窗口组支持和多连接器 HMA；新 TOKENSPEED_MLA 后端基于 TokenSpeed 项目，用于 Blackwell 上的优化 MLA 注意力计算。

github · khluu · May 15, 08:44

**背景**: vLLM 是一个流行的开源 LLM 推理和服务库。KV 缓存卸载将键值数据从 GPU 移动到 CPU 内存以释放 GPU 资源。混合内存分配器（HMA）是 vLLM 中新的内存管理架构，可提高内存效率。TOKENSPEED_MLA 后端是 TokenSpeed 的一部分，后者是针对 Blackwell GPU 上长上下文 Kimi 风格模型优化的推理引擎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.vllm.ai/2026/01/08/kv-offloading-connector.html">Inside vLLM’s New KV Offloading Connector: Smarter Memory Transfer for Maximizing Inference Throughput | vLLM Blog</a></li>
<li><a href="https://github.com/vllm-project/vllm/issues/11382">[RFC]: Hybrid Memory Allocator · Issue #11382 · vllm -project/ vllm</a></li>
<li><a href="https://github.com/lightseekorg/tokenspeed/tree/main/tokenspeed-mla">tokenspeed/tokenspeed-mla at main · lightseekorg/tokenspeed</a></li>

</ul>
</details>

**标签**: `#vllm`, `#LLM inference`, `#breaking changes`, `#speculative decoding`, `#GPU backends`

---

<a id="item-9"></a>
## [Zulip 转型为非营利基金会，创始人前往 Anthropic](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 8.0/10

Zulip 创始人 Tim Abbott 及三位核心团队成员将加入 Anthropic，同时公司将捐赠给新成立的独立非营利组织 Zulip 基金会，该消息于 2026 年 5 月 15 日公布。 这标志着知名开源项目的重大治理转变，可能有助于建立用户对商业化的信任，但也引发了关于核心团队离开后项目可持续性和发展方向的疑问。 Zulip 基金会将以公共利益为使命正式管理该项目；公告在周五发布，一些观察者指出这通常是发布争议性新闻的时机。创始人将以有限身份继续参与，但退出了全职领导岗位。

hackernews · boramalper · May 15, 18:37

**背景**: Zulip 是一款开源团队聊天应用，以基于话题的讨论线程著称，于 2012 年创建。它是 Slack 的主要免费替代品之一，被财富 500 强公司和开源社区使用。该项目此前由一家营利性公司支持，现已转移至基金会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zulip">Zulip - Wikipedia</a></li>
<li><a href="https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/">Announcing the Zulip Foundation</a></li>
<li><a href="https://news.ycombinator.com/item?id=48152168">The Zulip Foundation | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人对核心团队离开感到难过，并对公告时间（周五）表示怀疑，而另一些人则认为基金会是治理上的积极一步。也有人将其与 Bun 最近的收购相比较，但一些评论者信任创始人的诚信。

**标签**: `#open source`, `#governance`, `#Zulip`, `#nonprofit`, `#Anthropic`

---

<a id="item-10"></a>
## [美国司法部要求苹果和谷歌交出 10 万多名汽车应用用户身份](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 8.0/10

美国司法部向苹果和谷歌发出传票，要求其公开一款用于关闭排放控制的汽车改装应用的 10 万多名用户身份。此举是打击非法排放作弊装置行动的一部分。 这为政府从应用商店大规模索取数据开创了先例，引发严重的隐私和法律担忧。可能会影响应用开发者和平台处理用户数据及应对政府请求的方式。 涉案应用很可能是一款允许用户修改车辆排放设置的 ECU 调校应用。司法部声称需要数据来识别证人，但批评者认为这可能导致更广泛的监控，并对合法汽车改装造成影响。

hackernews · tencentshill · May 15, 17:28

**背景**: 排放作弊装置是指任何禁用或干扰排放控制的硬件或软件，使车辆排放超出法定标准。像'ECU Connect'这类 ECU 调校应用可用于刷写发动机控制单元软件，可能移除排放限制。美国环境保护局（EPA）长期打击作弊装置，此次行动将执法延伸至应用商店。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apps.apple.com/us/app/ecu-connect/id1140860609">ECU Connect App - App Store</a></li>
<li><a href="https://play.google.com/store/apps/details?id=com.ecutek.ecuconnect&hl=en_US">ECU Connect - Apps on Google Play</a></li>
<li><a href="https://en.wikipedia.org/wiki/Defeat_device">Defeat device - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论观点不一：有人认为政府应针对制造商而非用户，另一些人则担忧隐私和先例。有评论称这未来可能被用于禁用车辆 GPS 追踪，反映出对监控的忧虑。

**标签**: `#privacy`, `#regulation`, `#legal`, `#app stores`, `#surveillance`

---

<a id="item-11"></a>
## [专家建议独立创业者避免 SOC2 Type 2](https://news.ycombinator.com/item?id=48145524) ⭐️ 8.0/10

一位独立创业者在 Hacker News 上询问 SOC2 Type 2 合规问题；专家们强烈建议不要追求此类认证，因为成本高昂且需要角色分离。 这很重要，因为许多独立创业者面临企业客户要求获得 SOC2 的压力，但社区回应表明这对小公司来说不切实际且可能适得其反。 SOC2 Type 2 需要六个月的审计期和多个不重叠的角色（如开发人员、审查员、内部审计员），这对单人运营来说是不可能的。仅审计费用就超过 2 万美元。

hackernews · sochix · May 15, 07:18

**背景**: SOC2（系统与组织控制 2）是由美国注册会计师协会制定的合规框架，用于服务组织展示对安全性、可用性、处理完整性、保密性和隐私的控制。Type 2 报告评估一段时期内的运营有效性。企业客户常要求此认证，但它是为具有独立团队的较大组织设计的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.imperva.com/learn/data-security/soc-2-compliance/">What is SOC 2 | Guide to SOC 2 Compliance & Certification | Imperva</a></li>
<li><a href="https://www.paloaltonetworks.com/cyberpedia/soc-2">What Is SOC 2 Compliance? - Palo Alto Networks</a></li>
<li><a href="https://www.fortinet.com/resources/cyberglossary/soc-2-compliance">What is SOC 2 Compliance? Guide to SOC 2 Compliance & Certification | Fortinet</a></li>

</ul>
</details>

**社区讨论**: tptacek 和 jwr 的评论强烈建议独立创业者不要追求 SOC2，称其为'企业的 GPL'，并指出哪怕一个'否'答案也会导致审计失败。另一位评论者提到角色分离问题，至少需要 9 个不重叠的角色。但 hughw 评论者表示使用 Thoropass 等服务是可行的。

**标签**: `#compliance`, `#SOC2`, `#startup`, `#solo-entrepreneur`, `#enterprise-sales`

---

<a id="item-12"></a>
## [npm 的 postinstall 脚本：讽刺凸显反复出现的安全问题](https://kevinpatel.xyz/posts/no-way-to-prevent-this/) ⭐️ 7.0/10

一篇讽刺文章批评了 npm 的 postinstall 脚本长期存在的漏洞，这些脚本在包安装期间允许任意代码执行，并已在多次供应链攻击中被利用。 npm 作为最大的包注册中心，其系统性弱点对软件供应链构成重大风险，影响无数依赖 npm 进行前端和 Node.js 开发的开发者和组织。 npm 的 postinstall 脚本在包安装后自动运行，曾被用于部署恶意软件、窃取凭证和窃取数据。讽刺的框架强调该问题已存在多年，但 npm 团队尚未给出明确的修复方案。

hackernews · alligatorplum · May 16, 00:36

**背景**: npm 的生命周期脚本（包括 postinstall）允许包作者在安装期间执行任意命令。虽然这可用于合法目的（如编译原生模块），但经常在供应链攻击中被利用。文章标题模仿了《洋葱新闻》反复使用的讽刺标题模式‘没办法阻止这个，’只有[经常发生这种事的实体]这么说，突出了将此类漏洞视为不可避免的荒谬之处。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.npmjs.com/package/postinstall">postinstall - npm</a></li>
<li><a href="https://stackoverflow.com/questions/23505318/npm-disable-postinstall-script-for-package">node.js - npm : disable postinstall script for package - Stack Overflow</a></li>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了广泛的不满：一位用户建议彻底弃用 postinstall 脚本，另一位描述了组织内部推行安全配置的困难，还有一位质疑为什么 Go 和 Rust 生态系统受到更少攻击。甚至有评论者称其为‘心理健康危机’而非打包问题。

**标签**: `#npm`, `#security`, `#package managers`, `#software supply chain`, `#satire`

---

<a id="item-13"></a>
## [加州法案要求停运网游提供补丁或退款](https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/) ⭐️ 7.0/10

一项加州拟议法案要求游戏发行商在停止在线游戏服务时，要么发布补丁使其可离线运行，要么提供退款。 该法案可能对游戏行业产生重大影响，增加在线游戏的成本和法律风险，可能阻碍新游戏发布或加速向订阅模式转变。 该法案豁免了仅限订阅期间提供的游戏，这可能激励发行商采用订阅模式。据称法案文本可读性高且简洁。

hackernews · Lihh27 · May 15, 19:48

**背景**: 许多在线游戏需要持续运行的服务器才能游玩，当支持结束时游戏无法运行。该立法旨在保护那些购买了后来因服务器关闭而无法游玩的游戏的消费者。

**社区讨论**: 评论者意见不一：有人建议开源服务器代码，也有人警告运营成本高和意外后果。一位分享亲身经历的开发者担心该法案可能使制作在线游戏风险更大。

**标签**: `#policy`, `#gaming`, `#legislation`, `#consumer-protection`, `#regulation`

---

<a id="item-14"></a>
## [OCaml/OxCaml 太空应用：GC 优化显著降低延迟](https://gazagnaire.org/blog/2026-05-14-borealis.html) ⭐️ 7.0/10

一篇博客文章和 Hacker News 讨论报告称，通过使用带栈标注的 OxCaml，太空软件调度热路径上的 p99.9 延迟从 29 纳秒降至 9 纳秒，且完全消除了 GC 压力（在 2500 万个数据包中，从 394 次次要 GC 降为零）。 这表明，通过优化，带有垃圾回收的函数式编程语言也能适用于卫星软件等安全关键、实时系统，这些系统对低延迟和可预测性能有严格要求。 通过在热路径代码中添加栈分配标注，将堆分配移至栈，从而减少 GC 活动，实现了这一改进。吞吐量与原始版本相当。

hackernews · yminsky · May 15, 10:55

**背景**: OCaml 是一种带有垃圾回收器（GC）的函数式编程语言，GC 可能导致不可预测的暂停。OxCaml 是 Jane Street 开发的 OCaml 扩展集，包括栈分配标注，允许开发者显式地将数据放在栈上而非堆上，从而减少 GC 压力并提高延迟可预测性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oxcaml.org/">OxCaml | About</a></li>
<li><a href="https://oxcaml.org/documentation/stack-allocation/intro/">OxCaml | Stack allocation | Intro</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，这并非 OCaml 首次在太空部署；一位评论者描述了 2016 年在 GHGSat-D 上使用 OCaml 的情况。其他人讨论了将带 GC 语言适配实时约束的挑战，指出通过早期大量分配可以长时间禁用 GC 等技术。

**标签**: `#OCaml`, `#space software`, `#systems programming`, `#GC optimization`, `#functional programming`

---

<a id="item-15"></a>
## [Waymo 因涉水故障召回 3800 辆机器人出租车](https://www.cnbc.com/2026/05/12/waymo-recalls-3800-robotaxis-after-able-drive-into-standing-water.html) ⭐️ 7.0/10

Waymo 正在通过空中软件更新召回 3800 辆机器人出租车，以修复一个导致车辆驶入积水的感知故障，此前曾发生车辆被洪水冲走的事件。 此次召回凸显了自动驾驶车辆的一个特定感知挑战——区分湿路面和深水，同时也展示了集中式空中更新的优势，即能够快速在整个车队中部署修复。 修复通过空中软件更新完成，无需前往经销商。该故障是在一辆 Waymo 车辆驶入积水道路并被冲走后发现的。

hackernews · drob518 · May 15, 18:00

**背景**: 自动驾驶车辆依赖摄像头、激光雷达和雷达等传感器感知环境。区分积水和湿路面很困难，因为积水可能表现为反光表面或被误分类。传统汽车召回需要前往服务中心，而 Waymo 的空中更新允许远程修复，类似智能手机更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://electrek.co/2026/05/12/waymo-recalls-3791-robotaxis-flooded-road-ota-software-fix/">Waymo recalls 3,791 robotaxis over flooded road incident... | Electrek</a></li>
<li><a href="https://www.theverge.com/2024/6/12/24175489/waymo-recall-telephone-poll-crash-phoenix-software-map">Waymo issues software and mapping recall after robotaxi... | The Verge</a></li>
<li><a href="http://www.nast-group.caltech.edu/~murray/dgc05/upload/b/b8/Paper-water.pdf">Detecting water hazards for autonomous off-road navigation</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，区分湿路面和深水即使对人类来说也是个难题。有人建议为车辆配备水传感器，也有人称赞空中更新的可扩展性，能够提升整个车队的安全性。关于是否可以通过车辆动力学推理替代专用传感器，存在争议。

**标签**: `#autonomous vehicles`, `#safety`, `#Waymo`, `#software update`, `#sensor technology`

---

<a id="item-16"></a>
## [Bun 的 Rust 重写在安全 API 中暴露未定义行为](https://github.com/oven-sh/bun/issues/30719) ⭐️ 7.0/10

Bun 的 Rust 重写（将代码库从 Zig 翻译到 Rust）被发现存在 API，这些 API 允许从安全 Rust 代码中触发未定义行为（UB），未通过 Miri UB 检测工具的基本检查。 此问题凸显了从 Zig 等允许更多未定义行为灵活性的语言安全翻译到 Rust 并保持安全保证的挑战。这可能影响对 Bun 可靠性的信任及采用，并引发关于大规模迁移中 Rust 安全实践的更广泛讨论。 未定义行为是通过 API 设计暴露的，而不仅仅是内部代码；Miri 只有在编写特定测试时才能捕获。此问题是 Bun 从 Zig 重写到 Rust 更大努力的一部分，Bun 团队描述为‘直接翻译’，随后将进行安全改进。

hackernews · ndiddy · May 15, 16:51

**背景**: Bun 是一个快速 JavaScript 运行时和工具包，最初用 Zig 编写。Rust 以其内存安全保证著称，但如果不正确封装，unsafe 块可能引入未定义行为。Miri 是官方 Rust 工具，用于检测 Rust 程序中的未定义行为。将代码从安全保证较弱语言翻译到 Rust 需要仔细处理 unsafe 代码以保持安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rust-lang/miri">GitHub - rust -lang/ miri : An interpreter for Rust 's mid-level intermediate.....</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不同看法：一些人认为鉴于直接翻译的方法，这个问题并不令人惊讶，并认为这是一个逐步改进的过程；另一些人质疑团队为何不使用诸如 c2rust 的翻译工具来保留保证。大家认识到这种未定义行为暴露在从未安全语言初始移植时是常见的。

**标签**: `#bun`, `#rust`, `#undefined-behavior`, `#software-engineering`, `#zig`

---