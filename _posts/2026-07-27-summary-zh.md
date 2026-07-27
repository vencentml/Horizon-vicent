---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> From 78 items, 8 important content pieces were selected

---

1. [vLLM v0.26.0：支持 Inkling 模型、优化 DeepSeek-V4、跨厂商改进](#item-1) ⭐️ 9.0/10
2. [美国在军方建议后暂停对伊朗的打击](#item-2) ⭐️ 9.0/10
3. [llama.cpp b10142 为 Minimax-M3 增加视觉支持](#item-3) ⭐️ 8.0/10
4. [美国公民因在边境使用紧急 PIN 擦除手机而被起诉](#item-4) ⭐️ 8.0/10
5. [代币中继市场通过账单滥用助长转售和欺诈](#item-5) ⭐️ 8.0/10
6. [欧盟提议用浏览器级隐私设置取代 Cookie 横幅](#item-6) ⭐️ 8.0/10
7. [谷歌披露 SpaceX 持股 941 亿美元，占股 6%](#item-7) ⭐️ 8.0/10
8. [GrapheneOS 阻止从锁定设备提取数据](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0：支持 Inkling 模型、优化 DeepSeek-V4、跨厂商改进](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 9.0/10

vLLM v0.26.0 已发布，包含来自 212 位贡献者的 411 次提交，新增对 Inkling 模型系列的全面支持，为 DeepSeek-V4 带来显著性能优化，并包括跨 GPU 厂商（包括 ROCm 和 XPU）的改进。 此版本意义重大，因为它加入了对 Thinking Machines Lab 的 Inkling（一个大型开放权重混合专家模型）的支持，并包含对 DeepSeek-V4 的关键优化，可将端到端吞吐量提升数个百分比，使生产环境中的推理更高效且跨硬件平台更灵活。 该版本引入了一个专用路由内核，将 DeepSeek-V4 的 TPOT 提升 2.94%，一个 fused_topk_bias 内核速度提升 1.5-2 倍，并移除冗余的重复/复制操作，使 TPOT 额外提升 1.8%，此外还增加了 fp32 lm_head 支持、灵活的注意力后端以及成熟的 KV 卸载功能。

github · khluu · Jul 27, 01:06

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎，广泛用于生产环境。Inkling 是 Thinking Machines Lab 新推出的开放混合专家模型，总参数量 975B，上下文窗口 1M token，在 45 万亿多模态 token 上训练。FlashAttention-4 相对注意力通过优化注意力计算，在 Hopper 和 Blackwell GPU 上带来性能提升。MTP（多 token 预测）是一种推测性解码方法，允许模型每次前向预测多个 token，从而增加吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://docs.vllm.ai/en/stable/api/vllm/models/inkling/nvidia/ops/fa4_rel_attention/">fa 4 _rel_ attention - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>

</ul>
</details>

**社区讨论**: 发布说明中未包含社区评论，但大量的提交和贡献者数量表明社区参与度高且协作开发努力显著。

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#GPU optimization`, `#open source`

---

<a id="item-2"></a>
## [美国在军方建议后暂停对伊朗的打击](https://www.theguardian.com/world/2026/jul/26/us-pauses-trump-netanyahu-attacks-on-iran-talks-hormuz) ⭐️ 9.0/10

美国连续第二晚暂停对伊朗的轰炸行动，此前高级军官建议停止打击，认为空袭已接近效果极限且弹药储备正在减少。 此次暂停标志着美国战略可能从军事升级转向，外交谈判仍在继续以避免全面战争，这直接影响美伊冲突的走向以及因霍尔木兹海峡战略位置而引发的全球能源市场。 以色列总理本雅明·内塔尼亚胡（Benjamin Netanyahu）是美伊谈判的公开批评者，计划于周二访问白宫，敦促美国继续打击；而特朗普正在这场持续近五个月的冲突中权衡外交与军事选项。

rss · The Guardian World · Jul 26, 18:45

**背景**: 美国与伊朗已经陷入近五个月的冲突，美国对伊朗目标实施了轰炸行动。军方官员告知，轰炸行动进一步效果有限且弹药即将耗尽，因此暂停了打击。外交努力正在进行以缓解紧张局势，但内塔尼亚胡领导下的以色列反对谈判，并敦促继续军事行动。

**标签**: `#geopolitics`, `#US-Iran conflict`, `#military strategy`, `#energy risk`, `#diplomacy`

---

<a id="item-3"></a>
## [llama.cpp b10142 为 Minimax-M3 增加视觉支持](https://github.com/ggml-org/llama.cpp/releases/tag/b10142) ⭐️ 8.0/10

llama.cpp b10142 版本为 Minimax-M3 模型引入了视觉能力，集成了文本和视觉塔，并支持稀疏注意力和 GPU 优化。 此次更新扩展了 llama.cpp 的模型支持范围，覆盖了多模态架构，允许在本地对 Minimax-M3 进行视觉输入的推理。这对需要在不依赖专有 GPU API 的情况下部署视觉-语言模型的开发者非常有益。 该实现复用了 MiniMax-M2 和 DeepSeek-V3 的组件，包含对稀疏层的闪存注意力（flash attention），并使用自定义 CUDA 索引器操作以提高效率。视觉支持通过 mmproj 投影和 CLIP 图提供。

github · github-actions[bot] · Jul 27, 00:20

**背景**: llama.cpp 是一个开源的 C++ 库，用于在本地 CPU/GPU 上运行大型语言模型。Minimax-M3 是 MiniMax 公司推出的多模态模型，结合了文本和视觉处理。稀疏注意力是一种降低计算成本的技术，通过只关注相关的 token 对来减少运算量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@ashutoshadhikari141/exploring-sparse-attention-in-transformers-bigbird-longformer-and-their-applications-3e69920c2085">Exploring Sparse Attention in Transformers : BigBird and... | Medium</a></li>
<li><a href="https://medium.com/@bingqian/understanding-multi-token-prediction-mtp-in-deepseek-v3-ed634810c290">Understanding Multi - Token Prediction ( MTP ) in... | Medium</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#vision`, `#AI`, `#open-source`, `#inference`

---

<a id="item-4"></a>
## [美国公民因在边境使用紧急 PIN 擦除手机而被起诉](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html) ⭐️ 8.0/10

此案凸显了在边境使用紧急 PIN 码等安全功能的法律风险——边境设备搜查日益普遍。该案可能为法院如何处理隐私增强工具树立先例，进而抑制旅客因担心监控而采用此类功能。 GrapheneOS 的紧急 PIN 码会不可逆地擦除设备和 eSIM 数据，不留任何可恢复信息。被告面临妨碍司法指控；判决将取决于法院认为擦除是本能的安全措施还是故意销毁证据。

hackernews · eecc · Jul 26, 22:21

**背景**: GrapheneOS 是一款注重安全的基于 Android 的操作系统，提供紧急 PIN 功能：输入特定的虚拟 PIN 码会擦除手机而非解锁。在美国边境，海关与边境保护局（CBP）无需搜查令即可检查设备，但旅客通常无需提供密码。本案将检验使用紧急 PIN 码是否构成妨碍搜查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://www.androidauthority.com/grapheneos-duress-pin-us-prosecution-3691271/">GrapheneOS duress PIN could land a man in prison - Android Authority</a></li>
<li><a href="https://www.reddit.com/r/technology/comments/1v5mels/us_accuses_american_of_allegedly_wiping_his_phone/">US accuses American of allegedly wiping his phone using a 'duress' password during border search : r/technology - Reddit</a></li>

</ul>
</details>

**社区讨论**: Reddit 及科技网站的评论者就法律策略展开辩论：有人认为使用紧急 PIN 与普通 PIN 无异，而意图才是关键；另一些人则建议更实际的缓解措施，例如使用诱饵操作系统（如 VeraCrypt）或在过境前擦除手机。多人指出，该指控反映了政府的立场：安全功能不得妨碍边境搜查。

**标签**: `#security`, `#legal`, `#GrapheneOS`, `#border search`, `#privacy`

---

<a id="item-5"></a>
## [代币中继市场通过账单滥用助长转售和欺诈](https://vectoral.com/blog/token-relay-market) ⭐️ 8.0/10

Matt Lenhard 的调查揭示了代币中继市场如何通过滥用计费系统、被盗凭证和免费云额度，以折扣价系统性地转售 AI 代币，这与广告欺诈模式如出一辙。 这破坏了 AI 服务提供商的收入模式，并为合法客户造成了不公平竞争，凸显了云和订阅计费中的系统性漏洞。 欺诈行为包括盗用信用卡、滥用免费试用以及利用 AWS、Azure 等提供的新公司免费额度，转售商通过汇集 API 密钥以零售价 4%的价格提供代币。

hackernews · mlenhard · Jul 26, 15:17

**背景**: 代币中继市场充当 AI API 用户与提供商之间的中间人，类似于广告展示转售。它们利用计费系统延迟、免费试用限制和信用计划来廉价获取代币，然后转售。这与欺诈者使用类似技术转售廉价广告展示的广告欺诈有相似之处。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/26/relay-market/">An Inside Look at the Relay Market Powering Token Resellers and Fraud</a></li>

</ul>
</details>

**社区讨论**: 评论者指出这并不新鲜，与广告欺诈有相似之处（wtobey1）。一位用户强调免费云额度滥用带来了竞争优势（namanyayg）。另一位认为订阅模式是根本问题（benlivengood），而 tancop 则区分了欺诈、滥用免费试用和合法的订阅转售。

**标签**: `#fraud`, `#AI tokens`, `#cloud credits`, `#market manipulation`, `#subscription models`

---

<a id="item-6"></a>
## [欧盟提议用浏览器级隐私设置取代 Cookie 横幅](https://killthecookiebanner.eu/) ⭐️ 8.0/10

欧盟委员会提出一项新规，允许用户在浏览器中一次性设置隐私偏好，从而不再需要访问每个网站时都面对 Cookie 横幅。 这一提案可能通过简化同意机制大幅改善用户体验和隐私保护，并可能为全球网络跟踪实践树立标准。 该提案针对的是那些经常操纵用户同意机制的误导性 Cookie 横幅，而基于浏览器的设置将自动适用于所有网站。

hackernews · rapnie · Jul 26, 11:53

**背景**: Cookie 横幅是网站为获取用户对跟踪 Cookie 的同意而弹出的窗口，这是根据欧盟《电子隐私指令》和 GDPR 的要求。然而，许多用户觉得这些横幅烦人，经常不看就点过。新提案旨在将同意机制移至浏览器层面，类似于现有的 Global Privacy Control（GPC）等机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://european-union.europa.eu/cookies_en">Use of cookies on our websites | European Union</a></li>
<li><a href="https://thenai.org/how-to-opt-out/web-browser-privacy-settings/">Web Browser Privacy Settings - The NAI: Network Advertising Initiative</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持，有人认为 Cookie 横幅不能构成知情同意。也有人指出，一刀切的设置可能不适合所有网站，建议提供可定制的折中方案。

**标签**: `#privacy`, `#EU regulation`, `#cookie consent`, `#browser`, `#web standards`

---

<a id="item-7"></a>
## [谷歌披露 SpaceX 持股 941 亿美元，占股 6%](https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c) ⭐️ 8.0/10

谷歌（Alphabet）在最近的一份监管文件中披露，其持有的 SpaceX 股份价值 941 亿美元，持股比例为 6%。 这一披露揭示了 Alphabet 最初 9 亿美元投资的巨大回报，凸显了其私人公司持股的战略价值，并为 SpaceX 的估值提供了罕见的视角。 初始投资是在 2015 年左右作为 10 亿美元融资轮的一部分进行的，当时谷歌以 100-120 亿美元的估值获得 7-7.5%的股份；目前 6%的持股比例表明随着时间的推移出现了一定稀释。

hackernews · 1vuio0pswjnm7 · Jul 26, 12:43

**背景**: SpaceX 是埃隆·马斯克创立的私人航空航天公司，因其 Starlink 卫星互联网和 Starship 火箭项目而估值极高。谷歌母公司 Alphabet 在私人公司战略投资方面有着良好记录，类似于伯克希尔·哈撒韦的投资组合方式。

**社区讨论**: 社区评论指出这笔投资并非秘密，谷歌最初持股 7-7.5%。有人将 Alphabet 比作伯克希尔·哈撒韦，因其投资组合；也有人评论 100 倍回报并猜测是否应该卖出。

**标签**: `#finance`, `#investment`, `#spacex`, `#alphabet`, `#valuation`

---

<a id="item-8"></a>
## [GrapheneOS 阻止从锁定设备提取数据](https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices) ⭐️ 7.0/10

一场关于 GrapheneOS 的社区讨论详细介绍了其反取证功能，包括一个可触发工厂重置的胁迫 PIN 码（duress PIN）以及一个 18 小时自动重启功能，该功能将设备恢复至"首次解锁前"（BFU）状态。这些保护措施已通过记者使用案例得到验证。 这表明 GrapheneOS 为针对物理设备攻击提供了强大的实用防御，提高了记者、活动人士及其他敏感数据持有者的安全门槛。同时也凸显了经过适当强化的 Android 系统在安全性上可以媲美甚至超越 iOS。 胁迫 PIN 码会静默地执行工厂重置，而自动重启功能则在设备锁定一段时间（如 18 小时）后将其从"首次解锁后"（AFU）状态切换回 BFU 状态。BFU 状态下数据密钥不可用，即使操作系统也无法访问，从而阻止数据提取。

hackernews · Cider9986 · Jul 26, 05:57

**背景**: "首次解锁前"（BFU）是指设备重启后、用户首次输入密码之前的状态；此时全盘加密密钥未加载到内存中，使得数据提取极其困难。"首次解锁后"（AFU）状态下密钥已在内存中，某些取证工具可以访问数据。GrapheneOS 通过自动重启主动将设备置于 BFU，并包含一个胁迫 PIN 码，在遭遇胁迫时可擦除设备数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Duress_code">Duress code - Wikipedia</a></li>
<li><a href="https://grapheneos.org/features">Features overview | GrapheneOS</a></li>
<li><a href="https://blogs.dsu.edu/digforce/2023/08/23/bfu-and-afu-lock-states/">BFU and AFU Lock States – Blog | DigForCE Lab</a></li>

</ul>
</details>

**社区讨论**: 社区成员强调了这些功能的有效性，其中一位提到 GrapheneOS 通过自动重启功能帮助记者保护了信息来源。其他人指出了缺少完整备份/还原方案这一不足，还有关于密码熵的讨论指出图案锁的安全性远低于长密码。

**标签**: `#security`, `#Android`, `#GrapheneOS`, `#data protection`, `#threat model`

---