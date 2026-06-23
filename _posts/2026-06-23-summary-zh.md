---
layout: default
title: "Horizon Summary: 2026-06-23 (ZH)"
date: 2026-06-23
lang: zh
---

> From 131 items, 22 important content pieces were selected

---

1. [Codex 日志漏洞可能向本地 SSD 写入 TB 级数据](#item-1) ⭐️ 9.0/10
2. [大语言模型优先考虑风格而非角色标签，导致越狱攻击成功](#item-2) ⭐️ 9.0/10
3. [Meta 大规模部署 AV1 用于实时通信](#item-3) ⭐️ 9.0/10
4. [英国首相斯塔默辞职](#item-4) ⭐️ 9.0/10
5. [卡塔尔天然气工厂爆炸致 13 死 66 伤](#item-5) ⭐️ 9.0/10
6. [欧盟将与塔利班讨论阿富汗驱逐问题](#item-6) ⭐️ 9.0/10
7. [美国暂时解除对伊朗石油制裁 60 天](#item-7) ⭐️ 9.0/10
8. [中国加强对美国企业的稀土控制](#item-8) ⭐️ 9.0/10
9. [五眼联盟警告：AI 网络攻击威胁数月后降临](#item-9) ⭐️ 9.0/10
10. [伊朗同意联合国核检查员返回，与美国达成协议](#item-10) ⭐️ 9.0/10
11. [全球埃博拉病例超 1000 例，联合国警告儿童面临风险](#item-11) ⭐️ 9.0/10
12. [雪佛龙与微软签署 20 年天然气供电协议，为得州数据中心供电](#item-12) ⭐️ 8.0/10
13. [OpenAI 推出 Daybreak：Codex Security 与 GPT-5.5-Cyber](#item-13) ⭐️ 8.0/10
14. [Valve 推出 Steam Machine，采用随机预约系统](#item-14) ⭐️ 7.0/10
15. [GLM-5.2 本地推理：512GB RAM 加双 3090 即可运行](#item-15) ⭐️ 7.0/10
16. [加拿大计划到 2040 年新建最多 10 座核反应堆](#item-16) ⭐️ 7.0/10
17. [警察局长利用 Flock 车牌识别数据跟踪女性](#item-17) ⭐️ 7.0/10
18. [Deno 桌面支持发布，采用 CEF/Webview 后端](#item-18) ⭐️ 7.0/10
19. [Claude Code 的“扩展思考”输出是损耗性摘要](#item-19) ⭐️ 7.0/10
20. [GLM 5.2 表现亮眼，但仍不及 Claude Opus](#item-20) ⭐️ 7.0/10
21. [近半数 LG 智能电视应用包含住宅代理 SDK](#item-21) ⭐️ 7.0/10
22. [Cloudflare 发现 Hyper HTTP 库漏洞](#item-22) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Codex 日志漏洞可能向本地 SSD 写入 TB 级数据](https://github.com/openai/codex/issues/28224) ⭐️ 9.0/10

OpenAI 的 Codex AI 编程助手存在一个严重日志漏洞，导致应用程序持续高速写入 TRACE 级别日志，可能生成 TB 级数据并存在损坏 SSD 的风险。 该漏洞可能因过度写入而缩短 SSD 寿命，耗尽磁盘空间并降低系统性能，影响所有本地运行 Codex 的用户。 该漏洞影响 Codex 的日志系统，数据写入 `~/.codex/logs_2.sqlite` 的 SQLite 数据库。有用户报告运行 VACUUM FULL 将其日志文件从 27GB 缩减至 73MB，还分享了一个使用 SQL 触发器阻止插入的临时解决方法。

hackernews · vantareed · Jun 22, 07:30

**背景**: OpenAI Codex 是一款用于软件工程任务的 AI 编程助手，于 2025 年 4 月作为 Codex CLI 发布，也有桌面应用版本。过度日志记录会向存储写入大量数据，而 SSD 的写入寿命有限，可能导致过早损坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://www.houdao.com/d/14450-Severe-Codex-Logging-Bug-May-Exhaust-SSD-Lifespan-Solutions-Provided">Severe Logging Bug in Codex Could Cause Premature SSD Failure</a></li>
<li><a href="https://baonghean.vn/en/openai-codex-gap-loi-ghi-log-qua-muc-nguy-co-lam-hong-ssd-trong-chua-day-mot-nam-10341573.html">OpenAI Codex encounters excessive logging error: Risk of damaging SSDs ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了不满，有用户称 Codex 为‘垃圾软件’，并报告旋转指示器导致 100% GPU 使用率。已找到一个修复提交，部分用户指出 Codex 的开源特性使得补丁易于应用。

**标签**: `#Codex`, `#OpenAI`, `#logging`, `#bug`, `#SSD`

---

<a id="item-2"></a>
## [大语言模型优先考虑风格而非角色标签，导致越狱攻击成功](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything) ⭐️ 9.0/10

一篇新论文揭示，大语言模型存在角色混淆漏洞：它们优先考虑输入文本的写作风格，而非显式的角色标签（如<system>和<user>），这使得有效的越狱攻击成为可能。 这从根本上挑战了当前的大语言模型安全方法，表明静态基准测试不足，需要真正的角色感知才能实现稳健防御。这对 AI 系统设计有具体影响，尤其是依赖于角色标签来区分特权输入和不可信输入的应用。 研究发现，对输入文本进行“去风格化”处理——将其重写得看起来不像角色标签内的预期格式——可将攻击成功率从 61%降至 10%，这种变化对人类几乎不可见。像 gpt-oss-20b 这样的模型在对抗性输入模仿内部思考块的风格时，可以覆盖其训练结果。

rss · Simon Willison · Jun 22, 23:59

**背景**: 提示注入是一种安全漏洞，恶意输入通过绕过防护措施导致大语言模型产生意外行为。角色标签（如<system>和<user>）通常用于区分特权指令和用户输入，但大语言模型无法可靠地识别它们，从而导致漏洞。越狱是指精心设计提示以覆盖安全过滤器，生成受限内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://medium.com/@TechforHumans/effective-prompt-engineering-mastering-xml-tags-for-clarity-precision-and-security-in-llms-992cae203fdc">Effective Prompt Engineering: Mastering XML Tags for Clarity ... - Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者强调，这些发现证实了模型对写作风格而非标签的依赖，有人指出在多轮对话中，仅通过模仿内部推理风格的请求前缀就能绕过防护。另一位提出了将角色嵌入到 token 嵌入中的潜在解决方案，但也承认其局限性。讨论总体上支持该论文的结论。

**标签**: `#prompt injection`, `#LLM security`, `#jailbreak`, `#AI safety`, `#role confusion`

---

<a id="item-3"></a>
## [Meta 大规模部署 AV1 用于实时通信](https://engineering.fb.com/2026/06/22/video-engineering/adopting-av1-for-real-time-communication-rtc-meta/) ⭐️ 9.0/10

Meta 分享了他们在实时通信中大规模部署 AV1 视频编解码器的多年努力和技术方案，包括码率控制和错误恢复改进。 这展示了 AV1 对延迟敏感的实时通信的可行性，相比旧编解码器可减少约 50%带宽需求，影响 Meta 平台上的数十亿用户。 Meta 开发了新的码率控制算法以应对 AV1 的编码复杂性，以及错误恢复技术来减轻实时场景中的丢包问题。

rss · Meta Engineering · Jun 22, 16:00

**背景**: AV1 是由开放媒体联盟开发的开源、免版税视频编解码器，比 H.264/AVC 压缩效率高 30-50%。实时通信对延迟和丢包有严格要求，使得编解码器采用面临挑战。Meta 的工程博客详细介绍了他们在 RTC 中为 AV1 定制的解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV1">AV1 - Wikipedia</a></li>
<li><a href="http://aomedia.org/specifications/av1/">AV1 Video Codec - Alliance for Open Media</a></li>

</ul>
</details>

**标签**: `#AV1`, `#video codec`, `#real-time communication`, `#Meta`, `#engineering`

---

<a id="item-4"></a>
## [英国首相斯塔默辞职](https://www.nytimes.com/2026/06/22/world/europe/keir-starmer-andy-burnham-prime-minister-britain.html) ⭐️ 9.0/10

英国首相凯尔·斯塔默宣布辞职，为工党市长安迪·伯纳姆成为该国十年来第七位首相铺平道路。 此次领导层更迭凸显了英国持续的政治不稳定，十年内七位首相，可能导致国内政策和国际关系发生重大变化。 安迪·伯纳姆是一位受欢迎的工党市长，以在大曼彻斯特的工作而闻名；他的晋升反映了可能向更具地方性和草根性治理的转变。

rss · NYTimes World · Jun 22, 21:31

**背景**: 过去十年，英国经历了频繁的首相更换，包括鲍里斯·约翰逊、利兹·特拉斯、里希·苏纳克和凯尔·斯塔默。安迪·伯纳姆作为工党市长，代表了与斯塔默不同的党派派系。

**标签**: `#UK politics`, `#leadership change`, `#geopolitical risk`, `#policy shift`

---

<a id="item-5"></a>
## [卡塔尔天然气工厂爆炸致 13 死 66 伤](https://www.nytimes.com/2026/06/22/world/middleeast/qatar-explosion-gas.html) ⭐️ 9.0/10

卡塔尔一处关键天然气工厂发生爆炸，造成至少 13 人死亡、66 人受伤；当局将事故归咎于美以对伊战争后重启过程中的技术故障。 该事件可能扰乱全球天然气供应——卡塔尔是全球最大生产国之一——进而影响世界能源价格和市场稳定，尤其是当前中东地缘政治紧张局势加剧之际。 爆炸发生在一个主要天然气生产设施，该工厂在美以对伊朗军事行动后正重启生产；目前尚未公布具体故障细节。

rss · NYTimes World · Jun 22, 14:09

**背景**: 卡塔尔是全球领先的液化天然气（LNG）出口国之一，其天然气设施对全球能源供应至关重要。此前的美以对伊朗战争已破坏地区稳定和能源市场。重启过程中的技术故障是工业设施的已知风险，但此次事故的时机引发了对更广泛影响的担忧。

**标签**: `#gas plant explosion`, `#Qatar`, `#energy security`, `#geopolitical risk`, `#natural gas`

---

<a id="item-6"></a>
## [欧盟将与塔利班讨论阿富汗驱逐问题](https://www.nytimes.com/2026/06/22/world/europe/afganistan-taliban-brussels-deportees.html) ⭐️ 9.0/10

塔利班代表团已获得比利时签证，将于周二在布鲁塞尔与欧盟就驱逐阿富汗移民问题举行会谈。 此次会议标志着欧盟与塔利班之间正式外交接触的重要一步，可能预示着欧盟移民政策以及对塔利班政府承认的转变。这可能会影响成千上万的阿富汗寻求庇护者，并为国际社会与塔利班的互动开创先例。 塔利班代表团获得了比利时签证以参加会谈，这表明了一定程度的官方合作。会议议程专门聚焦于驱逐阿富汗人，鉴于人权担忧和塔利班的历史记录，这是一个有争议的问题。

rss · NYTimes World · Jun 22, 19:00

**背景**: 自 2021 年塔利班夺取阿富汗政权以来，许多国家拒绝正式承认其政府。欧盟一直在应对移民压力，由于潜在的人权侵犯问题，有关驱逐的讨论一直十分敏感。如果欧盟就此问题与塔利班接触，可能会改变难民遣返的地缘政治格局。

**标签**: `#Geopolitical Risk`, `#EU Policy`, `#Migration`, `#Taliban`, `#Diplomacy`

---

<a id="item-7"></a>
## [美国暂时解除对伊朗石油制裁 60 天](https://www.nytimes.com/2026/06/22/world/middleeast/us-sanctions-reprieve-iran-oil.html) ⭐️ 9.0/10

美国财政部宣布对伊朗石油制裁实施 60 天豁免，允许出售伊朗原油，作为结束战争的初步协议的一部分。 这一政策大幅反转可能对全球石油市场和供应链产生重大影响，可能降低油价并改变中东的地缘政治格局。 此次豁免为期 60 天，是旨在结束战争的美国-伊朗初步协议的一部分。协议条款的具体细节尚未公布。

rss · NYTimes World · Jun 22, 17:30

**背景**: 美国多年来一直对伊朗石油出口实施严格制裁，作为施压伊朗核计划及地区活动政策的一部分。此次暂时解除制裁标志着这一长期立场的重大转变。

**标签**: `#geopolitics`, `#oil`, `#sanctions`, `#macro`, `#US-Iran`

---

<a id="item-8"></a>
## [中国加强对美国企业的稀土控制](https://www.nytimes.com/2026/06/22/business/china-rare-earths.html) ⭐️ 9.0/10

中国加强了对稀土元素的出口管制，针对两家美国制造商，这些制造商对于特朗普政府重建国内高强度永磁体供应链的努力至关重要。 此举加剧了贸易紧张局势，并威胁到美国确保国内稀土磁体供应的努力，这些磁体用于国防、电动汽车和风力涡轮机，可能扰乱多个高科技产业。 这两家目标公司是美国生产烧结钕铁硼（NdFeB）磁体计划的核心，这些磁体依赖钕和镝等稀土元素，而中国在全球占据主导地位。

rss · NYTimes World · Jun 22, 13:34

**背景**: 稀土元素是一组 17 种金属，对磁体、电池和电子产品等高科技产品至关重要。中国控制着全球大部分开采和精炼产能。由稀土制成的永磁体对于电动汽车电机、风力涡轮发电机和军事系统至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rare-earth_element">Rare-earth element - Wikipedia</a></li>
<li><a href="https://www.usgs.gov/media/images/potential-uses-rare-earth-elements-found-marine-minerals">Potential Uses of Rare Earth Elements Found in Marine Minerals | U.S. Geological Survey</a></li>

</ul>
</details>

**标签**: `#rare earths`, `#trade war`, `#supply chain`, `#geopolitics`, `#critical minerals`

---

<a id="item-9"></a>
## [五眼联盟警告：AI 网络攻击威胁数月后降临](https://www.theguardian.com/technology/2026/jun/22/anthropic-claude-fable-ai-model-artificial-intelligence-national-security) ⭐️ 9.0/10

五眼联盟情报机构罕见发布联合声明，警告说能够对政府和企业发动毁灭性网络攻击的强大 AI 模型仅需数月即可问世，此前特朗普政府决定禁止外国公民使用 Anthropic 的 Fable AI 模型。 这一来自最高级别情报合作机制的警告标志着网络战能力即将升级，可能迫使五眼国家及其他地区紧急采取政策和防御措施。 声明特别提及了 Anthropic 的 Fable 模型，特朗普政府于 2026 年 6 月早些时候将其限制仅对美国公民开放，情报机构敦促领导人'立即行动'以应对威胁。

rss · The Guardian World · Jun 22, 13:00

**背景**: 五眼联盟是由澳大利亚、加拿大、新西兰、英国和美国组成的情报联盟，最初根据 UKUSA 协议为信号情报合作而成立。Anthropic 的 Claude Fable 5 是一款最先进的 AI 模型，专为自主知识工作和编程设计，拥有 100 万 tokens 的上下文窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Five_Eyes">Five Eyes - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-fable-5">Claude Fable 5 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#cybersecurity`, `#national security`, `#Five Eyes`, `#policy`

---

<a id="item-10"></a>
## [伊朗同意联合国核检查员返回，与美国达成协议](https://www.theguardian.com/world/2026/jun/22/iran-us-talks-progress-pakistan-qatar-lebanon-israel) ⭐️ 9.0/10

伊朗已同意允许联合国核检查员返回该国，作为与美国协议的一部分，美国将解除对伊朗石油出口的制裁，霍尔木兹海峡将重新开放。 该协议标志着美伊关系的重大转变，可能降低核扩散风险，稳定全球石油市场，并缓解中东的地缘政治紧张局势。 该协议包括对伊朗核计划的长期独立监测，该监测在去年夏天以色列和美国袭击伊朗核设施后停止。德黑兰此前已暂停与国际原子能机构（IAEA）的合作。

rss · The Guardian World · Jun 22, 16:42

**背景**: 伊朗核计划多年来一直是国际紧张局势的根源，IAEA 的监测在伊朗核设施遭袭击后暂停。霍尔木兹海峡是全球石油运输的关键瓶颈，对伊朗石油出口的制裁严重影响了伊朗经济。

**标签**: `#geopolitics`, `#Iran`, `#nuclear`, `#oil`, `#sanctions`

---

<a id="item-11"></a>
## [全球埃博拉病例超 1000 例，联合国警告儿童面临风险](https://news.un.org/feed/view/en/story/2026/06/1167783) ⭐️ 9.0/10

联合国宣布，全球确诊埃博拉病例已超过 1000 例，刚果民主共和国东部近 300 万儿童和青少年面临风险。 这一里程碑凸显了疫情规模的扩大，强调了紧急的人道主义需求，以及如果防控失败可能导致更广泛的区域传播。 目前正在加大力度治疗当前疫情中心附近的囚犯，该疫情集中在刚果民主共和国东部。

rss · UN News · Jun 22, 12:00

**背景**: 埃博拉病毒病是一种严重且常致命的人类疾病。刚果民主共和国当前的疫情始于 2021 年，因冲突和后勤挑战而变得复杂，使得防控困难。

**标签**: `#Ebola`, `#public health`, `#DR Congo`, `#humanitarian crisis`, `#global health`

---

<a id="item-12"></a>
## [雪佛龙与微软签署 20 年天然气供电协议，为得州数据中心供电](https://www.chevron.com/newsroom/2026/q2/chevron-signs-20-year-power-agreement-with-microsoft-for-west-texas-data-center) ⭐️ 8.0/10

雪佛龙宣布与微软签署一项为期 20 年的购电协议，为位于西得克萨斯的新数据中心提供天然气发电，将使用 GE Vernova 和 Solar Turbines 的涡轮机。 该交易凸显了人工智能不断增长的能源需求与企业气候目标之间的冲突，微软计划在 2030 年前实现碳负排放，却为一个大型数据中心承诺使用新的化石燃料发电。 大部分发电将来自大型 GE Vernova 涡轮机，额外容量由 Solar Turbines 提供——卡特彼勒旗下制造工业燃气轮机的子公司。该协议利用了二叠纪盆地持续为负的天然气价格。

hackernews · cdrnsf · Jun 22, 13:43

**背景**: 西得克萨斯州的二叠纪盆地在石油开采过程中伴生大量天然气。当管道运输能力不足时，天然气价格变为负值——生产商需付费让人把气运走。这使得该地区天然气发电极其廉价，尽管有丰富的太阳能和风能资源。选择天然气而非可再生能源，凸显了数据中心清洁能源应用面临的经济和基础设施限制。

**社区讨论**: 评论者指出，该地区负的天然气价格使这笔交易在经济上很划算，但批评其与微软碳负排放承诺的矛盾。有人指出，“Solar Turbines”这个名称对一家燃气轮机制造商具有误导性。其他人则质疑微软为何不利用廉价的太阳能和电池储能，毕竟得州独立电网倾向于选择最低成本的发电方式。

**标签**: `#data center`, `#natural gas`, `#Microsoft`, `#energy agreement`, `#AI infrastructure`

---

<a id="item-13"></a>
## [OpenAI 推出 Daybreak：Codex Security 与 GPT-5.5-Cyber](https://openai.com/index/daybreak-securing-the-world) ⭐️ 8.0/10

OpenAI 宣布推出 Daybreak 套件，包括 Codex Security 和 GPT-5.5-Cyber，以帮助组织大规模自动发现、验证和修补漏洞。 这代表了将人工智能应用于网络安全的重要一步，可能使企业能够自动化漏洞管理，将响应时间从数周缩短到数分钟。 Codex Security 逐次提交扫描 GitHub 仓库并构建项目特定的威胁模型，而 GPT-5.5-Cyber 是一个经过网络调优的模型，仅限于经过审查的防御者执行授权的防御任务。

rss · OpenAI News · Jun 22, 10:00

**背景**: 漏洞管理对组织来说至关重要，但通常过程缓慢。传统工具需要大量人工来分类和修补缺陷。能够自主解释代码和利用链的 AI 代理可以显著加速这一工作流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Codex_Security_OpenAI">Codex Security (OpenAI)</a></li>
<li><a href="https://winbuzzer.com/2026/05/14/openais-gpt-55-matches-claude-mythos-in-security-tests-xcxwbn/">Claude Mythos Leads GPT - 5 . 5 in AISI Cyber Range Tests</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#OpenAI`, `#vulnerability management`

---

<a id="item-14"></a>
## [Valve 推出 Steam Machine，采用随机预约系统](https://store.steampowered.com/news/group/45479024/view/685257114654870245) ⭐️ 7.0/10

Valve 于 2026 年 6 月 22 日开放了 Steam Machine 的随机预约系统，起售价为 1049 美元，并采用基于组件成本的定价方式。 Steam Machine 体现了 Valve 对开放 PC 游戏平台的承诺，其随机预约系统旨在打击黄牛并确保公平获取，可能为硬件发布设立新标准。 随机预约系统接受数天的报名，没有先到先得的激励机制，然后随机分配名额以减少机器人的优势。价格直接与组件成本挂钩，Valve 使用自 2023 年以来的 PC 硬件历史数据来追踪成本变化。

hackernews · theschwa · Jun 22, 17:09

**背景**: Steam Machine 是 Valve 最新推出的游戏硬件，运行开放的 SteamOS 操作系统。它继承了之前 Steam Link 和 Steam Controller 的尝试，但这次强调开放平台，用户可以安装任何软件或操作系统。Valve 采用基于组件成本的定价方式以反映波动的硬件成本，这与固定的主机定价不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/video-games/console-gaming/valve-opens-steam-machine-reservations-details-usd1-049-starting-price-randomized-queue-to-stop-scalpers-and-limited-inventory">Valve opens Steam Machine reservations ... | Tom's Hardware</a></li>
<li><a href="https://www.pcgamer.com/hardware/gaming-pcs/steam-machine-reservations/">Sign up for a Steam Machine before June 25: Valve... | PC Gamer</a></li>
<li><a href="https://www.eurogamer.net/valve-steam-machine-price-availability-reaction">Valve says Steam Machine 's price is "significantly..." | Eurogame...</a></li>

</ul>
</details>

**社区讨论**: 社区成员赞扬了开放平台和随机预约系统的公平性，有用户指出一段展示真实反应的游戏片段非常真实。另一位用户表达了购买意愿，还有评论引用了 Valve 对随机排队以防止黄牛的解释。

**标签**: `#gaming`, `#hardware`, `#valve`, `#steam machine`, `#PC gaming`

---

<a id="item-15"></a>
## [GLM-5.2 本地推理：512GB RAM 加双 3090 即可运行](https://unsloth.ai/docs/models/glm-5.2) ⭐️ 7.0/10

有用户演示了通过 llama.cpp 在 512GB RAM 和两张 RTX 3090 显卡上本地运行大型 MoE 模型 GLM-5.2，在动态 4-bit 量化（Q4_K_XL）下实现每秒 6-9 个 token 的生成速度。 这表明尖端的大型推理模型可以在个人硬件上部署，减少了对昂贵云 API 的依赖，并实现了隐私敏感或离线的 AI 应用。 该方案使用 llama.cpp 并添加 -cmoe 标志，报告称将 DDR4 内存从 2400MHz 升级到 3200MHz 并使用更好的 CPU 可将速度提升至约 11 token/秒。模型至少需要 256GB 系统内存用于 MoE 卸载，以及 24GB 显存。

hackernews · TechTechTech · Jun 22, 21:21

**背景**: GLM-5.2 是 Z.ai 推出的大型推理模型，拥有 100 万 token 的上下文窗口，专为软件工程和多步自动化等复杂任务设计。它采用混合专家（MoE）架构，每 token 仅激活模型参数的一部分，从而在保持每 token 计算量可控的同时实现更大的总参数量。由于总参数量可达数千亿，本地运行该模型需要强大的硬件支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM - 5 . 2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://openrouter.ai/z-ai/glm-5.2">GLM 5 . 2 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了实际经验：segmondy 确认了报告的速度，并指出更好的内存和 CPU 可以提升性能。xrd 强调 192GB 内存不够用，而 skiing_crawling 警告提示处理速度远低于纯 GPU 方案，因此不适合交互式使用。Pheggs 对本地模型缩小与云服务差距表示乐观，CGamesPlay 则质疑“基本无损”量化的说法，因为 token 一致性仅为 97.5%。

**标签**: `#local-llm`, `#hardware`, `#quantization`, `#inference`, `#GLM`

---

<a id="item-16"></a>
## [加拿大计划到 2040 年新建最多 10 座核反应堆](https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509) ⭐️ 7.0/10

加拿大政府宣布计划到 2040 年新建最多 10 座核反应堆，利用其铀储量与 CANDU 反应堆技术专长，重点发展小型模块化反应堆（SMR）。 这标志着加拿大能源政策向核电的重大转变，可能为可再生能源提供可靠的基荷电力支持，并助力工业脱碳。同时也使加拿大成为 SMR 部署的领导者，影响全球核能趋势。 该计划包括大型 CANDU 反应堆和 SMR，预计将进行设计竞争。加拿大已从达林顿翻新项目中积累了经验，并拥有全球最大铀储量之一。

hackernews · geox · Jun 22, 19:06

**背景**: CANDU 反应堆是加拿大设计的重水反应堆，使用天然铀作为燃料，无需浓缩。小型模块化反应堆（SMR）是先进反应堆，单机功率最高 300 兆瓦，设计为工厂制造和可扩展部署。加拿大这一计划顺应了全球为能源安全和气候目标而对核能日益增长的兴趣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CANDU_reactor">CANDU reactor - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Small_modular_reactor">Small modular reactor</a></li>
<li><a href="https://www.iaea.org/newscenter/news/what-are-small-modular-reactors-smrs">What are Small Modular Reactors (SMRs)? | IAEA</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持该计划，提及加拿大的铀储量、CANDU 安全记录以及可再生能源所需的基荷电力。部分人争论哪种 SMR 设计将胜出，也有人指出公众舆论已从安全担忧转向能源独立。一位评论者开玩笑说“核复兴”可能是个矛盾修辞。

**标签**: `#nuclear energy`, `#Canada`, `#energy policy`, `#small modular reactors`, `#uranium`

---

<a id="item-17"></a>
## [警察局长利用 Flock 车牌识别数据跟踪女性](https://ipvm.com/reports/police-chiefs-track) ⭐️ 7.0/10

报告记录显示，警察局长利用 Flock 自动车牌识别（ALPR）数据跟踪女性，这表明在没有授权要求的情况下，监控技术存在明显的滥用。 这一实际滥用案例可能影响关于 ALPR 数据是否需要授权的政策辩论，因为它凸显了监控系统可能被滥用于个人骚扰而非合法执法的风险。 Flock 的 ALPR 系统捕获车牌数据并集中存储；报道的滥用行为涉及警察追踪他们认识的女性。该公司称这种行为罕见，但同时也指出这是最常见的滥用形式。

hackernews · jhonovich · Jun 22, 19:13

**背景**: 自动车牌识别（ALPR）系统使用摄像头和光学字符识别技术读取车牌，并将数据与时间戳和位置一同存储。Flock Safety 是向执法机构提供此类系统的主要供应商，构建了庞大的监控网络。美国公民自由联盟（ACLU）等隐私倡导者警告称，这些系统的普及在没有适当监督的情况下促成了大规模监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.govtech.com/public-safety/joplin-mo-watchdog-group-questions-use-of-flock-cameras">Joplin, Mo., Watchdog Group Questions Use of Flock Cameras</a></li>
<li><a href="https://www.coloradopolitics.com/2025/07/19/as-flock-camera-network-grows-so-do-privacy-and-data-concerns-37abb64a-924e-581c-af05-b4f0090cbfe8/">As Flock camera network grows, so do privacy and... - Colorado Politics</a></li>
<li><a href="https://www.linkedin.com/pulse/how-automatic-license-plate-recognition-alpr-works-dvkuf">How Automatic License Plate Recognition ( ALPR ) Works — In One...</a></li>

</ul>
</details>

**社区讨论**: 社区评论引用了 Scott Adams 的名言：只要有机会且没有监控，欺诈就会发生。关于滥用是“罕见”同时又是最常见形式之间存在争议——这是 Flock 尚未解决的矛盾。一些评论者建议不要与警察有任何交流，并警告与警察约会会危及自身安全。

**标签**: `#surveillance`, `#privacy`, `#police-accountability`, `#ALPR`, `#Flock`

---

<a id="item-18"></a>
## [Deno 桌面支持发布，采用 CEF/Webview 后端](https://docs.deno.com/runtime/desktop/) ⭐️ 7.0/10

Deno 宣布了 Deno Desktop 功能，允许开发者使用 Chromium Embedded Framework (CEF) 或系统 Webview 后端将 Deno 应用打包为桌面应用，并计划推出共享 CEF 运行时。 这使 Deno 成为构建跨平台桌面应用的有力竞争者，通过共享运行时大幅减小二进制体积，并利用 Deno 成熟的安全和权限模型。 该功能在 Deno v2.9.0 canary 版本中提供，支持 CEF、Webview 和 Raw 后端。开发者可通过 deno.json 配置后端，编译后的二进制文件仅包含已授予的权限。

hackernews · GeneralMaximus · Jun 22, 05:38

**背景**: CEF 是一个用于在应用中嵌入 Chromium 浏览器的开源框架，而 Webview 则使用操作系统原生的 Web 引擎。Deno 最初是服务器端 JavaScript/TypeScript 运行时，现在扩展到桌面应用开发，提供比 Electron 更小的打包体积替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.deno.com/runtime/desktop/">Desktop apps | Deno Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chromium_Embedded_Framework">Chromium Embedded Framework - Wikipedia</a></li>
<li><a href="https://docs.deno.com/runtime/desktop/backends/">Backends | Deno Docs</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了热情，讨论聚焦于共享运行时减小二进制体积的潜力、Deno 权限系统与桌面应用的集成，以及增加“在浏览器中启动”选项的建议。

**标签**: `#deno`, `#desktop`, `#runtime`, `#cross-platform`, `#CEF`

---

<a id="item-19"></a>
## [Claude Code 的“扩展思考”输出是损耗性摘要](https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/) ⭐️ 7.0/10

一项分析揭示，Claude Code 的“扩展思考”模式中显示的文本并非模型的实际推理过程，而是其损耗性摘要，这引发了关于 AI 推理展示透明度的担忧。 这很重要，因为用户和开发者依赖查看真实推理过程来信任 AI 输出，而隐藏原始推理会削弱整个行业的可解释性和问责制。 这种损耗性摘要会遗漏细节，可能无法忠实呈现模型的真实思维链，类似于将 JPEG 保存为 BMP 再转换回来——数据在这个过程中丢失。

hackernews · 0o_MrPatrick_o0 · Jun 22, 14:22

**背景**: 扩展思考是 Claude Code 的一项功能，允许模型在输出最终答案之前在草稿纸中逐步推理。包括 Anthropic、OpenAI 和 Google 在内的许多 AI 公司隐藏原始推理过程，以保护专有技术并防止竞争对手提炼其模型。这种做法与日益增长的 AI 透明度和可解释性需求相冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.claudecodecamp.com/p/claude-code-extended-thinking">Claude Code Extended Thinking</a></li>
<li><a href="https://www.anthropic.com/research/team/interpretability">Interpretability Research \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/research">Research \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，隐藏原始推理是主要 AI 公司的标准做法，这是出于竞争考虑。一些用户表示失望，因为他们发现阅读真实推理过程对调试和建立信任确实有用。其他人则指出，即使是原始的草稿纸内容也可能不完全忠实于模型的内部计算。

**标签**: `#AI transparency`, `#reasoning models`, `#interpretability`, `#Claude`, `#Anthropic`

---

<a id="item-20"></a>
## [GLM 5.2 表现亮眼，但仍不及 Claude Opus](https://techstackups.com/comparisons/glm-5.2-vs-opus/) ⭐️ 7.0/10

社区讨论和实际测试表明，GLM 5.2 相比大多数非顶级模型有显著提升，但在编码任务上仍落后于 Claude Opus，尤其是在一次性提示基准测试中。 这一比较有助于开发者为项目选择性价比高的模型，并凸显了将一次性提示作为实际软件工程基准的局限性。 Z. AI 的 GLM 5.2 拥有 100 万 token 的上下文窗口，专为长时程智能体工作流设计。在 PostTrainBench 上，它在开源模型中优于 Opus 4.7 和 GPT-5.5。

hackernews · ritzaco · Jun 22, 07:22

**背景**: 一次性提示是指在要求模型执行任务之前给出一个示例，这种做法常用于基准测试，但批评者认为它不能反映实际使用情况。长时程任务需要多步推理和遵循指令，这是 GLM 5.2 旨在改进的方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM - 5 . 2 - Overview - Z. AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://arxiv.org/html/2406.06608v1">The Prompt Report: A Systematic Survey of Prompting Techniques</a></li>
<li><a href="https://registry.ollama.ai/library/glm-5.2">GLM - 5 . 2 is Z. ai ’s flagship model for the era of long-horizon tasks.</a></li>

</ul>
</details>

**社区讨论**: 社区成员批评了使用单次一次性提示作为基准的做法，认为它不代表实际软件项目的复杂性。一位用户分享说，GLM 5.2 相比其他非顶级模型有巨大进步，但仍不及 Claude Opus；另一位指出该模型在可引导性和幻觉方面存在问题。

**标签**: `#AI models`, `#benchmarking`, `#LLM evaluation`, `#user experience`

---

<a id="item-21"></a>
## [近半数 LG 智能电视应用包含住宅代理 SDK](https://spur.us/blog/smart-tv-apps-residential-proxy-sdks) ⭐️ 7.0/10

spur.us 的研究发现，近半数的 LG 智能电视应用内嵌了住宅代理 SDK，这些 SDK 可能被用于匿名化流量以进行欺诈和滥用。 这构成了重大的隐私和安全风险，因为住宅代理可以将数百万消费者设备变成恶意活动的出口节点，可能牵连无辜用户。 该研究重点关注的是第三方应用而非 LG 自有应用，这些 SDK 通常用于网页抓取等合法目的，但可能被重新用于欺诈。

hackernews · microcode · Jun 22, 20:48

**背景**: 住宅代理 SDK 使设备能够充当代理，通过真实的家庭 IP 地址路由互联网流量。公司利用这些 SDK 提供轮换 IP 以进行数据收集，但它们也可能被滥用于点击欺诈或撞库等恶意活动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://phishfort.com/residential-proxies-security-tips-alert/">Residential Proxies Alert: How Attackers Hijack Home... | PhishFort</a></li>

</ul>
</details>

**社区讨论**: 评论者建议永远不要将智能电视连接到互联网，或使用隔离的 VLAN；其他人指出受影响的是第三方应用而非 LG 自带的。一些人对调查结果表示反感，还有两位评论者指出被标记最多的 SDK 提供商源自以色列。

**标签**: `#security`, `#privacy`, `#smart TV`, `#residential proxy`, `#LG`

---

<a id="item-22"></a>
## [Cloudflare 发现 Hyper HTTP 库漏洞](https://blog.cloudflare.com/hyper-bug/) ⭐️ 7.0/10

Cloudflare 在重新架构其 Images 绑定时，发现了一个存在于多个主要版本的开源 Hyper HTTP 库漏洞。 该漏洞影响一个基础性的 Rust HTTP 库，该库被众多项目和服务使用，可能对广泛用户的可靠性和安全性造成影响。 该漏洞存在于 Hyper 的多个主要版本中，这意味着许多现有部署在升级前可能容易受到攻击。

rss · Cloudflare Blog · Jun 22, 18:00

**背景**: Hyper 是一个用 Rust 编写的快速且安全的 HTTP 库，在 Rust 生态系统中被广泛用作 HTTP 客户端和服务器的基础构件。它是许多高级框架（如 Axum 和 Tower）的基础组件。Cloudflare Images 绑定允许 Workers 与 Cloudflare 的图像优化服务交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lib.rs/web-programming/http-server">HTTP server — list of Rust libraries /crates // Lib.rs</a></li>
<li><a href="https://github.com/joelparkerhenderson/demo-rust-axum">GitHub - joelparkerhenderson/demo- rust -axum: Demo of Rust and...</a></li>
<li><a href="https://developers.cloudflare.com/images/optimization/transformations/bindings/">Bind to Workers API · Cloudflare Images docs</a></li>

</ul>
</details>

**标签**: `#bug`, `#HTTP`, `#Rust`, `#open-source`, `#security`

---