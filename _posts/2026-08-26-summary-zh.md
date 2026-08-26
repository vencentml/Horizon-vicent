---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
lang: zh
---

> From 121 items, 15 important content pieces were selected

---

1. [Next.js v16.3.3 修复关键未认证 RCE 漏洞](#item-1) ⭐️ 9.0/10
2. [Next.js v15.5.24 修复两个严重 RCE 漏洞](#item-2) ⭐️ 9.0/10
3. [OpenAI 定制推理芯片“Jalapeño”据称超越英伟达 Blackwell](#item-3) ⭐️ 9.0/10
4. [加拿大以高达 50%的关税回击特朗普关税](#item-4) ⭐️ 9.0/10
5. [美加贸易战升级：50%关税与对等报复](#item-5) ⭐️ 9.0/10
6. [FDA 首款酮体与血糖连续监测穿戴设备获批](#item-6) ⭐️ 8.0/10
7. [Firefox 157 默认启用 JPEG XL，Chromium 或跟进](#item-7) ⭐️ 8.0/10
8. [SpaceX 宣布 Starbase LA：路易斯安那州新发射设施](#item-8) ⭐️ 8.0/10
9. [SiFive 推出首款 RISC-V 服务器平台](#item-9) ⭐️ 8.0/10
10. [量化感知修复：4 位模型超越全精度原版](#item-10) ⭐️ 8.0/10
11. [llama.cpp v0.3.0 新增多模态 dots3-note 支持与 DeepSeek 4 张量拆分](#item-11) ⭐️ 7.0/10
12. [苹果发布 M6 与 M5 Ultra 芯片，AI 算力大幅跃升](#item-12) ⭐️ 7.0/10
13. [Nitter 项目收到停止函，所有实例无限期关停](#item-13) ⭐️ 7.0/10
14. [Qwen 发布 Qwen3.8-Flash-Next：125B 参数 MoE 模型，6B 激活参数](#item-14) ⭐️ 7.0/10
15. [EVE Online 启动大规模 Python 2 到 3 迁移](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Next.js v16.3.3 修复关键未认证 RCE 漏洞](https://github.com/vercel/next.js/releases/tag/v16.3.3) ⭐️ 9.0/10

Vercel 发布了 Next.js v16.3.3，其中包含两个严重安全公告的修复：Windows 服务器上的未认证远程代码执行，以及 Image Optimization API 处理 AVIF 文件时的未认证远程代码执行。对应公告编号为 GHSA-p293-qw3h-jr36 和 GHSA-2xp9-vwfh-vxw4。 Next.js 是目前使用最广泛的 React 框架之一，因此这类严重的未认证 RCE 漏洞可能使大量生产环境 Web 应用面临风险。开发者应立即升级到 v16.3.3，防止远程攻击者在受影响服务器上执行任意代码。 其中一个公告专门影响托管在 Windows 上的 Next.js 服务器，另一个则影响内置 Image Optimization API 在处理 AVIF 文件时的情况。两者均被评定为严重级别，且不需要认证，这意味着只要漏洞代码路径可被访问，任何远程攻击者都可能利用它们。

github · eps1lon · Aug 25, 16:17

**背景**: Next.js 是 Vercel 创建的热门开源 React 框架，以服务器端渲染、静态站点生成和内置的 Image Optimization API 等功能著称。Image Optimization API 是默认的图像加载器，它优化来自网络上任意位置的图像，并直接从 Next.js 服务器提供服务。AVIF 是一种基于 AV1 视频编解码器的现代图像格式，压缩效率优于旧格式。RCE 即远程代码执行，是一种严重的安全问题，可让攻击者在易受攻击的系统上运行任意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nextjs.org/docs/14/app/building-your-application/optimizing/images">Optimizing: Images | Next.js</a></li>
<li><a href="https://uploadcare.com/blog/avif-image-format/">What is an AVIF file? Learn the AVIF format (2026) | Uploadcare</a></li>

</ul>
</details>

**标签**: `#security`, `#next.js`, `#RCE`, `#vulnerability`

---

<a id="item-2"></a>
## [Next.js v15.5.24 修复两个严重 RCE 漏洞](https://github.com/vercel/next.js/releases/tag/v15.5.24) ⭐️ 9.0/10

Next.js v15.5.24 修复了两个严重的未认证远程代码执行漏洞：一个影响 Windows 托管的服务器，另一个在使用 AVIF 文件时影响 Image Optimization API。 这些漏洞可被主动利用，影响广泛使用的 React 框架，使许多生产部署面临风险。必须立即打补丁，防止服务器上未授权的代码执行。 安全公告编号分别为 GHSA-p293-qw3h-jr36 和 GHSA-2xp9-vwfh-vxw4，均被评为严重（Critical）。Image Optimization API 的问题由 AVIF 文件触发，而 Windows 服务器问题无需认证即可利用。

github · eps1lon · Aug 25, 16:16

**背景**: Next.js 是一个流行的 React 框架，用于构建服务端渲染和静态 Web 应用。Image Optimization API 是内置功能，可即时调整和优化图像；AVIF 是一种现代图像格式，压缩率优于 JPEG 或 WebP。Windows 服务器上的漏洞可能与 Windows 的路径处理或区域设置行为有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AVIF">AVIF - Wikipedia</a></li>
<li><a href="https://www.contentful.com/blog/load-avif-webp-using-html/">What is an AVIF image? The AVIF image format explained | Contentful</a></li>
<li><a href="https://nextjs.org/docs/app/api-reference/components/image">Components: Image Component | Next.js</a></li>

</ul>
</details>

**标签**: `#security`, `#next.js`, `#remote-code-execution`, `#vulnerability`, `#web-framework`

---

<a id="item-3"></a>
## [OpenAI 定制推理芯片“Jalapeño”据称超越英伟达 Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 9.0/10

据彭博社和 SemiAnalysis 报道，OpenAI 与博通合作设计的定制推理芯片“Jalapeño”在基准测试中据称优于英伟达 Blackwell 架构，具有更高的吞吐量、更低的延迟和更好的能效。 如果该说法得到验证，可能通过降低每 token 成本重塑 AI 推理经济，并减少 OpenAI 对英伟达的依赖，从而可能改变 AI 硬件和云服务领域的竞争格局。 报道中的对比涉及 FP4 精度、裸片尺寸和 token/Joule 能效；一张对比表显示其裸片面积与英伟达的 Rubin 相近，但 NVFP4 PFLOPS 仅为后者的三分之一。Jalapeño 被描述为一款面向 LLM 优化的推理芯片，是 OpenAI 多代计算平台计划的第一步，但该说法目前仍属媒体报道，且文章与表格在某些数字上据称并不一致。

hackernews · bmulholland · Aug 25, 14:06

**背景**: 英伟达的 Blackwell 架构是 Hopper 和 Ada Lovelace 的继任者，采用台积电定制的 4NP 工艺，集成 2080 亿个晶体管，是目前 AI 训练和推理的重要参考标杆。OpenAI 一直在通过与博通合作设计定制芯片来减少对英伟达的依赖，据报道 Jalapeño 正是这一合作的首个成果。由于推理是持续发生的运营成本，而非一次性的训练投入，推理效率的提升会直接影响大规模部署大语言模型的经济性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/">The Engine Behind AI Factories | NVIDIA Blackwell Architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.nxcode.io/resources/news/openai-broadcom-jalapeno-inference-chip-developer-guide-2026">OpenAI Jalapeño Chip Guide: What It Means for AI Coding... | NxCode</a></li>

</ul>
</details>

**社区讨论**: 评论呈现出好奇、怀疑与历史视角的混合。mchusma 猜测未来是否可能将模型权重直接烧入定制芯片，并指出旧模型仍有长期实用价值；corford 将初生的推理芯片市场比作早期 3dfx/Riva/PowerVR 时代，并质疑最终的赢家会是谁。epistasis 对 FP4 对比提出质疑，指出裸片尺寸存在出入；fraboniface 则指出，按 token/Joule 计算，人脑仍比该芯片高效 22 倍。

**标签**: `#AI hardware`, `#OpenAI`, `#Nvidia`, `#semiconductors`, `#inference`

---

<a id="item-4"></a>
## [加拿大以高达 50%的关税回击特朗普关税](https://www.nytimes.com/2026/08/25/world/canada/canada-tariffs-trump-carney-retaliatory.html) ⭐️ 9.0/10

加拿大宣布对美国一系列商品征收最高达 50%的报复性关税，包括铝箔、洗碗机和鱼类。此举发生在 2026 年 8 月 25 日，此前美国总统整个上午都在抨击加拿大，称其是他打交道中'最棘手'的国家。 这标志着美加贸易战显著升级，对两国跨境企业、供应链和消费者都有直接影响。加拿大的举动表明，它将保护本国工人和制造商免受美国关税冲击，这可能会提高依赖双边贸易的行业的成本和不确定性。 报复性关税涵盖铝箔、洗碗机等日常用品以及鱼类产品，目标针对美国对加拿大的出口。此外，特朗普总统否认了有关谈判破裂部分原因是由于一项会削弱法语保护的提案，称这是总理卡尼为获取政治支持而编造的'谎言'。

rss · NYTimes World · Aug 25, 18:42

**背景**: 在特朗普政府对加拿大商品征收新关税后，美加两国陷入了贸易冲突。作为回应，加拿大表示提高关税是为了保护受美国措施损害的工人、生产商和制造商。贸易紧张局势也引发了对更广泛经济扰乱以及美加关系稳定性的担忧。

**标签**: `#trade war`, `#tariffs`, `#Canada`, `#US policy`, `#economy`

---

<a id="item-5"></a>
## [美加贸易战升级：50%关税与对等报复](https://www.nytimes.com/2026/08/23/world/canada/canada-us-trade-war-trump-carney.html) ⭐️ 9.0/10

加拿大暂停了贸易谈判，促使特朗普总统对一系列加拿大商品征收 50%的关税；总理马克·卡尼随即以“一元对一元”的方式实施对等报复。 这是美加这两个全球最大贸易伙伴之间贸易战的重大升级，可能扰乱双边贸易、冲击市场并推高消费品价格。此举也表明贸易政策风险上升，影响范围可能超出北美，波及全球供应链。 关税适用于一系列加拿大商品，但现有报道中未列出具体产品清单。卡尼的回应被称为“一元对一元”，意思是加拿大报复性关税的价值意在与美国关税相当。

rss · NYTimes World · Aug 25, 18:49

**背景**: 美国与加拿大互为最大贸易伙伴之一，在汽车、能源和农业等领域的供应链高度一体化。贸易战是指一国加征关税、另一国以报复性关税回应的过程。关税是对进口商品征收的税，通常由进口商支付，但往往通过更高价格转嫁给消费者。暂停谈判使两国失去了一个可能的外交缓冲，破坏范围扩大的风险随之上升。

**标签**: `#trade-war`, `#tariffs`, `#us-canada`, `#macro`, `#policy`

---

<a id="item-6"></a>
## [FDA 首款酮体与血糖连续监测穿戴设备获批](https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar) ⭐️ 8.0/10

美国 FDA 首次批准了一款可穿戴设备，该设备通过单个传感器连续监测酮体和血糖水平。这一监管里程碑为糖尿病患者提供实时双指标监测。 这项批准意义重大，因为连续酮体监测有助于及早发现糖尿病酮症酸中毒（DKA）这一危及生命的并发症，而血糖追踪则支持日常糖尿病管理。它还可能减少对指尖采血检测的依赖，并为 1 型糖尿病患者及生酮饮食者改善护理。 该设备将连续血糖和酮体监测集成于单个传感器，基于 Abbott 的 FreeStyle Libre CGM 平台。Abbott 的这类双指标传感技术已在欧洲获得 CE 认证，但在美国的报销政策和临床推广仍是待解问题。

hackernews · sunnynagra · Aug 25, 19:07

**背景**: 酮体是身体分解脂肪供能时产生的物质，对于糖尿病患者来说，酮体水平升高可能预示着糖尿病酮症酸中毒（DKA）。传统上，酮体通过尿试纸或指尖血检测，而血糖则通过 CGM 系统单独监测。Abbott 一直在开发葡萄糖/酮体双指标生物可穿戴设备，其 FreeStyle Libre DUO 系统被视为这一类别中的未来产品。FDA 的这次授权标志着从单一分析物传感器向多分析物可穿戴生物传感器的转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.abbott.com/en-us/corpnewsroom/strategy-and-strength/abbotts-biowearable-one-sensor-for-glucose-ketones">Abbott's Biowearable: One Sensor for Glucose, Ketones | Newsroom</a></li>
<li><a href="https://beyondtype1.org/ketone-monitoring-timeline/">From Urine Strips to Continuous Monitoring : The Evolution of Ketone ...</a></li>

</ul>
</details>

**社区讨论**: 评论总体积极，有人表达个人情感并希望该设备能预防酮症酸中毒死亡。但也有评论者提出保留意见：有人质疑“可穿戴”这一说法，因为传感器需插入手臂；有人认为酮体监测对普通糖尿病患者用处不大；还有人强调需要解决报销问题，并对无创血糖传感持怀疑态度。

**标签**: `#FDA`, `#medical devices`, `#diabetes`, `#health technology`, `#wearables`

---

<a id="item-7"></a>
## [Firefox 157 默认启用 JPEG XL，Chromium 或跟进](https://groups.google.com/a/mozilla.org/g/dev-platform/c/3YMV4MS34KA?pli=1) ⭐️ 8.0/10

Mozilla 在 dev-platform 上宣布，Firefox 157 将在所有平台上默认启用 JPEG XL。与此同时，Chromium 的 Blink-dev 讨论显示 Chrome 可能也将跟进支持该格式。 这标志着主流浏览器向 JPEG XL 采用迈出了重要一步，可能改变网页图像的压缩、存储和传输方式。开发者和用户将受益于 JPEG XL 更优秀的压缩率和现代特性，从而降低带宽和存储成本。 Mozilla 的公告提到了基于 Rust 的 jxl-rs 实现，而苹果已经随其平台提供了 C++ 版 libjxl 库，这引发了关于跨平台一致性的讨论。评论中附带的 Chromium 讨论链接进一步表明 Chrome 可能在 JPEG XL 支持上与 Firefox 保持一致。

hackernews · yboris · Aug 25, 17:55

**背景**: JPEG XL 是由联合图像专家组（JPEG）、Google 和 Cloudinary 开发的自由开放标准图像格式，由 ISO/IEC 18181 定义。它支持有损和无损压缩、广色域、高动态范围和高位深，非常适合网页传输和专业摄影。此前浏览器支持一直有限，因此 Firefox 和 Chromium 的举措可能加速其广泛采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>
<li><a href="https://jpeg.org/jpegxl/">JPEG - JPEG XL</a></li>

</ul>
</details>

**社区讨论**: 社区总体情绪积极，不少人希望 JPEG XL 能在日常使用中完全取代旧版 JPEG。部分评论者提到实际担忧，即一些网站和上传框尚不支持 JXL，建议提供自动转换或回退选项。还有人对基于 Rust 的 jxl-rs 与 C++ libjxl 的基准对比感到好奇，并关注苹果未来对格式的态度。

**标签**: `#jpeg-xl`, `#firefox`, `#chromium`, `#image-format`, `#web-standard`

---

<a id="item-8"></a>
## [SpaceX 宣布 Starbase LA：路易斯安那州新发射设施](https://www.spacex.com/sites/starbase-la) ⭐️ 8.0/10

SpaceX 正式在官网宣布 Starbase LA，这是位于路易斯安那州的新发射设施。报道称该基地可能成为 SpaceX 第四个也是最大的发射设施，预计投资达 1000 亿美元，满负荷时每天可进行超过 30 次 Starship 发射。 这一战略扩张使 SpaceX 的发射基础设施不再局限于得克萨斯州和佛罗里达州，并为美国最贫困地区之一带来显著经济发展。该选址还提供了进入太阳同步轨道的有利条件，对地球观测和侦察卫星发射非常有价值。 据媒体报道，该基地将包含五个发射综合体，每个综合体配有两个发射台和一个推进剂储存区，此外还有推进剂生产设施和发电基础设施。此公告结束了数月以来的猜测，当地房地产经纪人和 Ars Technica 在 2026 年早些时候已报道过相关传闻。

hackernews · bilsbie · Aug 25, 16:37

**背景**: 在轨道力学中，发射场的纬度会影响到达不同轨道所需的能量。较低的纬度可为向东发射提供免费助力，而太阳同步轨道（常用于地球观测）需要向南发射并形成近极地轨迹，发射场的纬度会影响所需方位角。SpaceX 目前在得克萨斯州和佛罗里达州运营 Starship 发射设施，Starbase LA 将为其第四个发射场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.spacex.com/sites/starbase-la">SpaceX - Starbase , LA</a></li>
<li><a href="https://qz.com/spacex-starbase-louisiana-spaceport-100-billion-082526">SpaceX announces $100 billion Starbase Louisiana spaceport</a></li>
<li><a href="https://space.stackexchange.com/questions/40842/why-does-launching-east-result-in-an-orbital-inclination-equal-to-the-latitude-o">Why does launching east result in an orbital inclination equal to the...</a></li>

</ul>
</details>

**社区讨论**: 评论者总体持乐观态度，强调这可能会为经济萧条的沿海路易斯安那州带来长期建筑工作，并称赞这是‘有雄心的、真实的’项目。有人指出了太阳同步轨道通道等战略优势，也有评论者质疑页面文案部分由 AI 生成，因为环境相关段落措辞重复。

**标签**: `#spacex`, `#space`, `#louisiana`, `#economic-development`, `#aerospace`

---

<a id="item-9"></a>
## [SiFive 推出首款 RISC-V 服务器平台](https://chipsandcheese.com/p/sifives-first-server-platform) ⭐️ 8.0/10

SiFive 推出了其首个服务器平台，将 RISC-V 处理器引入数据中心服务器设计。这标志着 RISC-V 进入长期由 x86 和 ARM 主导的服务器市场的一个具体里程碑。 一个可行的 RISC-V 服务器平台有望挑战 x86/ARM 的双头垄断，并减少云数据中心的供应商锁定。它为硬件买家提供了开放架构的替代选择，也标志着 RISC-V 正在从嵌入式和边缘应用走向更广阔的市场。 根据 Chips and Cheese 的分析，该平台据称支持最高 450W 的双宽 GPU。社区讨论指出了 GPU 驱动成熟度以及引导固件是开源还是依赖专有 blob 等开放问题。

hackernews · geerlingguy · Aug 25, 03:06

**背景**: RISC-V 是一种开放指令集架构（ISA），其规范以宽松的开源许可证发布，与 x86 和 ARM 等专有 ISA 不同，实现 RISC-V 无需支付许可费。开放架构服务器旨在使组件的添加、升级和更换更加容易，这是云和数据中心运营商追求灵活性与成本节省的关键卖点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_architecture">Open architecture - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍乐观地认为 RISC-V 进入真正的服务器平台是一个巨大里程碑，但也有多人提出实际担忧。有人质疑免许可的 ISA 是否真的能改变这个细分市场的经济性，还有人担心 GPU 驱动的各种小毛病和引导固件中的 blob，也有人提供了 RISC-V 向量基准测试结果链接。

**标签**: `#RISC-V`, `#SiFive`, `#Server`, `#CPU`, `#Open Source`

---

<a id="item-10"></a>
## [量化感知修复：4 位模型超越全精度原版](https://huggingface.co/blog/MultiverseComputingCAI/quantization-aware-healing) ⭐️ 8.0/10

量化感知修复（QAH）通过从原始未压缩模型（而非恢复的全精度检查点）进行蒸馏，生成了一个 4 位量化模型，其性能超越了全精度原版模型。 这一反直觉的结果挑战了模型大小与精度之间存在取舍的传统量化观念。它可能重塑模型压缩和部署策略，使高效的低位模型在生产环境和边缘环境中更具吸引力。 该技术被描述为一种实用方法，用于恢复同时经过结构压缩和 4 位量化的 LLM。arXiv 论文详细介绍了 QAH 的方法，即从原始未压缩模型中蒸馏压缩后的学生模型。

rss · Hugging Face Blog · Aug 25, 11:39

**背景**: 量化会降低模型参数的数值精度（例如从 32 位降到 4 位），从而减少内存占用并加快推理速度，但通常会带来轻微精度损失。量化感知训练（QAT）通过在训练中模拟低精度来恢复精度。量化感知修复（QAH）扩展了这一思路，使用原始未压缩模型作为蒸馏教师，从而获得一个精度可能超过原版的 4 位模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.20953v1">Quantization-Aware Healing: A Practical Recipe for Recovering Compressed, 4-Bit LLMs</a></li>
<li><a href="https://www.ibm.com/think/topics/quantization-aware-training">What is Quantization Aware Training? | IBM</a></li>
<li><a href="https://developer.nvidia.com/blog/how-quantization-aware-training-enables-low-precision-accuracy-recovery/">How Quantization Aware Training Enables Low-Precision Accuracy Recovery | NVIDIA Technical Blog</a></li>

</ul>
</details>

**标签**: `#quantization`, `#model compression`, `#machine learning`, `#AI efficiency`, `#Hugging Face`

---

<a id="item-11"></a>
## [llama.cpp v0.3.0 新增多模态 dots3-note 支持与 DeepSeek 4 张量拆分](https://github.com/ggml-org/llama.cpp/releases/tag/v0.3.0) ⭐️ 7.0/10

llama.cpp v0.3.0 版本新增了对 dots3-note 多模态模型的支持，采用新的 DSA-ISWA KV 缓存类型，并为 GLM-4.5-Air 引入 MTP 支持，同时为 DeepSeek 4 增加了张量拆分（-sm tensor）和多序列回滚修复。此外，ggml 升级到 v0.22.0。 此次更新意义重大，因为 llama.cpp 是最广泛使用的开源 LLM 推理引擎之一，这些改动增强了多模态能力，并提升了 DeepSeek 4 等前沿模型的性能。依赖本地推理的开发者与产品将受益于更高的效率、更广的模型支持以及新的调试工具。 值得注意的细节包括 ggml v0.22.0，其具有 meta-backend 张量拆分、带并行编译的逐算子 Metal 内核以及非原地 ggml_clamp；服务器新增 LLAMA_SERVER_SLOTS_N_DIFF 调试开关，Web UI 增加了标签式聊天导航。dots3-note 模型是一个 280B 参数的 MoE 多模态模型，具有 16B 活跃参数和 512K 上下文窗口。

github · github-actions[bot] · Aug 25, 10:22

**背景**: llama.cpp 是一个广受欢迎的开源 C/C++ 库，用于在本地高效运行大型语言模型，支持 CPU/GPU 推理，采用 GGUF 格式，并支持 Metal 和 CUDA 等后端。DSA-ISWA KV 缓存是为 dots3-note 模型引入的新缓存类型。多令牌预测（MTP）是一种同时预测多个未来令牌以加速生成的技术，而张量拆分则是将模型张量分布到多个设备上进行计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://korshunov.ai/en/article/20686-llama-cpp-0-3-0-adds-dots3-note-model-and-tensor-split-for-deepseek-4/">llama.cpp 0.3.0 adds dots3-note model and tensor-split for DeepSeek 4</a></li>
<li><a href="https://aiweekly.co/alerts/xiaohongshu-opens-dots3-note-a-280b-moe-multimodal-model">Xiaohongshu opens dots 3 - note , a 280B MoE multimodal model</a></li>
<li><a href="https://www.emergentmind.com/topics/multi-token-prediction-mtp">Multi-Token Prediction ( MTP )</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#LLM inference`, `#open source`, `#multimodal`, `#AI tools`

---

<a id="item-12"></a>
## [苹果发布 M6 与 M5 Ultra 芯片，AI 算力大幅跃升](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 7.0/10

2026 年 8 月 25 日，苹果发布了 M6 和 M5 Ultra 芯片。M6 是苹果首款 2nm 芯片，配备 12 核 CPU、12 核 GPU 和双 16 核神经网络引擎；M5 Ultra 则采用四芯粒架构，是苹果迄今最强大的芯片。 这标志着 Mac 产品线在性能和端侧 AI 算力上的一次重大飞跃，可能重塑人们对本地 AI 工作负载的期待。开发者、专业用户以及越来越依赖神经网络引擎性能的整个苹果生态都会受到影响。 M5 Ultra 通过新一代 UltraFusion 技术连接两颗双芯粒 M5 Max 芯片，这是苹果芯片首次采用四芯粒架构。UltraFusion 将芯粒间带宽提升至超过 4.4TB/s，连接密度提升超过 6 倍。

hackernews · interpol_p · Aug 25, 13:01

**背景**: Apple silicon 是苹果自 2020 年推出 M1 以来使用的 ARM 架构系统级芯片系列，取代了 Mac 中的 Intel 处理器。M 系列后来扩展出 Pro、Max 和 Ultra 版本，其中 Ultra 芯片通过 UltraFusion 技术将两颗 Max 芯片组合以获得更强性能。神经网络引擎是苹果专用于机器学习和 AI 任务的硬件，新的双 16 核神经网络引擎旨在将 AI 相关性能大约提升一倍。此次发布延续了苹果向先进制程的过渡，M6 是苹果首款 2nm 芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M6 and M 5 Ultra for a big leap in... - Apple</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M6">Apple M 6 - Wikipedia</a></li>
<li><a href="https://www.macrumors.com/2026/08/25/apple-debuts-m5-ultra/">Apple Debuts M 5 Ultra as Most Powerful Chip Ever - MacRumors</a></li>

</ul>
</details>

**社区讨论**: 社区反应兼具兴奋与谨慎。一些用户称赞性能提升显著，并感叹 Apple silicon 进步之大；也有用户拿竞争和性价比开玩笑，认为其性价比在历史上相当惊人。讨论还集中在高配版价格，以及彭博社传闻——苹果可能跳过 M6 Pro/Max/Ultra，集中精力打造具备强大 AI 能力的 M7 芯片。

**标签**: `#Apple`, `#Silicon`, `#AI Compute`, `#Hardware`, `#Chip`

---

<a id="item-13"></a>
## [Nitter 项目收到停止函，所有实例无限期关停](https://github.com/zedeus/nitter/issues/1442) ⭐️ 7.0/10

Nitter 项目宣布收到停止和终止函（cease and desist），所有公共 Nitter 实例已无限期下线，等待法律意见。 Nitter 是一个被广泛使用的、注重隐私的 X/Twitter 替代前端，对它采取法律行动可能为其他第三方客户端开创先例，进一步限制用户访问社交媒体内容的方式。 公告除提到收到停止和终止函以及所有实例无限期关停外，几乎没有提供细节。维护者表示正在等待法律意见，目前没有恢复时间表。

hackernews · Banditoz · Aug 25, 17:08

**背景**: Nitter 是一个免费、开源的 Twitter（现为 X）替代前端，灵感来自 Invidious 项目。它通过去除 JavaScript 和广告、让所有请求经过后端来保护隐私。该项目托管在 GitHub 上，并曾获得 NLnet 的支持。长期以来，用户常用它在不被追踪或无需登录的情况下浏览推文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nlnet.nl/project/Nitter/">NLnet; Nitter</a></li>
<li><a href="https://alternativeto.net/software/nitter/about/">Nitter : Free and open-source front-end mirror of Twitter... | AlternativeTo</a></li>
<li><a href="https://sourceforge.net/projects/nitter.mirror/">Nitter download | SourceForge.net</a></li>

</ul>
</details>

**社区讨论**: 评论者表示失望，认为当地议会等机构仍依赖 X 发布信息，还有人呼吁中等强国为这类项目提供法律保护。也有人指出公告细节太少，并认为社区项目应得到支持，而不是被以违反服务条款相威胁。

**标签**: `#nitter`, `#twitter`, `#legal`, `#privacy`, `#censorship`

---

<a id="item-14"></a>
## [Qwen 发布 Qwen3.8-Flash-Next：125B 参数 MoE 模型，6B 激活参数](https://modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) ⭐️ 7.0/10

Qwen 宣布推出 Qwen3.8-Flash-Next，这是一个总参数 125B、激活参数 6B 的混合专家（MoE）模型，计划于明天发布。该模型已在 ModelScope 和 Hugging Face 的 Qwen 组织下上架。 此次发布可能改变本地 AI 推理格局，使大型开放权重模型能够在 128GB Strix Halo 系统、GB10 设备或 Mac Studio 等高带宽消费级硬件上实用运行。这也加剧了开放权重模型领域与 Qwen 27B、Gemma 31B 等模型的竞争。 125B 总参数/6B 激活参数的比例意味着每个 token 只使用模型的一小部分，从而降低内存带宽需求，同时保留较大的知识容量。不过，目前尚未公布任何基准测试结果或官方性能声明，这一发布基于社区公告和模型页面列表。

hackernews · garo-pro · Aug 25, 11:49

**背景**: 混合专家（MoE）是一种架构，模型包含多个专门的子网络（即“专家”），路由器为每个输入只激活其中少数几个。这种设计将总参数与激活参数解耦：总参数决定存储大小和容量，激活参数决定计算成本和推理速度。开放权重模型会公开发布训练后的权重，允许任何人下载并在本地运行。这些特性使 MoE 模型特别适合本地推理，因为一个 125B 参数但只有 6B 激活参数的模型运行速度会比其体积所暗示的要快。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters: What’s the Difference?</a></li>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极且充满期待，用户认为该模型终于让 128GB Strix Halo 或 Mac Studio 等高带宽设备有了用武之地，并可能实现实用的本地 MoE 推理。也有人表达了实际担忧：一位用户对 OpenRouter 上的 Qwen 模型感到失望（容量低且不稳定），另一位则指出该模型的影响将取决于 FreeToken 等推理引擎能否将 MoE 工作负载分配到 CPU/内存和 GPU/显存之间。

**标签**: `#Qwen`, `#MoE`, `#open-weights`, `#local AI`, `#inference`

---

<a id="item-15"></a>
## [EVE Online 启动大规模 Python 2 到 3 迁移](https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/) ⭐️ 7.0/10

EVE Online 宣布开始从 Stackless Python 2.7 迁移到 Python 3。计划使用 futurize 脚本处理 240 万行代码，并人工审查约 2 万个行为差异。 这是游戏行业规模最大、最复杂的 Python 2 到 3 迁移之一，为遗留代码库提供了可借鉴的经验。迁移结果将决定 EVE Online 在使用了二十多年不受维护的解释器之后如何继续在技术上演进。 公告没有说明将如何替换 Stackless，但此前的一次会议演讲介绍了在 EVE Frontier 的 Carbon 引擎中使用开源的 carbonengine/scheduler 库来替换 Stackless。迁移将处理 Python 2 和 3 行为不同的约 2 万个位置，例如整数除法。

rss · Simon Willison · Aug 25, 22:59

**背景**: Stackless Python 是 CPython 的一个分支，增加了轻量级微线程（tasklet）和通道，避免了操作系统线程的开销。自 2003 年以来，它一直是 EVE Online 的运行时，但该项目已正式停止维护，其 GitHub 仓库自 2025 年 2 月起被归档。futurize 是一种自动化工具，先将 Python 2 代码转换为 Python 2/3 兼容形式，再添加 Python 3 支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stackless_Python">Stackless Python</a></li>
<li><a href="https://python-future.org/futurize.html">futurize: Py2 to Py2/3 — Python-Future documentation</a></li>
<li><a href="https://github.com/stackless-dev/stackless/wiki/">Home · stackless-dev/stackless Wiki · GitHub</a></li>

</ul>
</details>

**标签**: `#Python`, `#EVE Online`, `#Software Migration`, `#Stackless Python`, `#Game Development`

---