---
layout: default
title: "Horizon Summary: 2026-05-11 (ZH)"
date: 2026-05-11
lang: zh
---

> From 93 items, 7 important content pieces were selected

---

1. [特朗普拒绝伊朗和平提议后油价飙升](#item-1) ⭐️ 9.0/10
2. [llama.cpp b9095 为 CUDA 添加内部 AllReduce，移除 NCCL 依赖](#item-2) ⭐️ 8.0/10
3. [硬件认证作为垄断助推器](#item-3) ⭐️ 8.0/10
4. [马里兰州居民因外州 AI 数据中心面临 20 亿美元电网升级费用](#item-4) ⭐️ 8.0/10
5. [《纽约时报》因人工智能幻觉更正错误引语](#item-5) ⭐️ 8.0/10
6. [路易斯·罗斯曼为受威胁的 OrcaSlicer 开发者提供法律援助](#item-6) ⭐️ 7.0/10
7. [西班牙成为欧洲最便宜电力市场，但家庭电价更高](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [特朗普拒绝伊朗和平提议后油价飙升](https://www.bbc.com/news/articles/ckgp4ev4yg4o?at_medium=RSS&at_campaign=rss) ⭐️ 9.0/10

在特朗普总统拒绝伊朗的结束战争提议后，油价上涨，霍尔木兹海峡实际上被关闭，严重扰乱了全球能源运输。美国海军的封锁和伊朗的威胁已使大部分航运通过这一关键瓶颈停止。 霍尔木兹海峡承载着全球约四分之一的海运石油贸易，因此其关闭会立即推高油价并威胁全球能源安全。这种升级可能导致消费者长期面临更高的能源成本，并在全球范围内造成严重的经济破坏。 革命卫队威胁称，如果伊朗油轮遭到攻击，将袭击美国在中东的目标，此前美国在阿曼湾袭击了两艘伊朗油轮。由于海军封锁和担心伊朗的袭击，该海峡实际上仍处于关闭状态。

rss · BBC World News · May 11, 01:12

**背景**: 霍尔木兹海峡是位于波斯湾与阿曼湾之间的一条狭窄水道，全球约 20-25%的石油和液化天然气贸易通过此处。它是沙特阿拉伯、阿联酋和伊朗等主要产油国能源运输的关键瓶颈。伊斯兰革命卫队（IRGC）是一支强大的伊朗军事力量，负责保卫政权，并参与了地区冲突以及对美军的威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/03/02/strait-of-hormuz-crisis-us-iran-israel-war-shipping-trade-oil.html">Strait of Hormuz crisis explained: What it means for global ...</a></li>
<li><a href="https://www.britannica.com/place/Strait-of-Hormuz">Strait of Hormuz | Map, Importance, Conflict and Closure ... Strait of Hormuz Disruptions - UNCTAD Strait of Hormuz - About - IEA Top Stories The world’s most important 21 miles | AP News Amid regional conflict, the Strait of Hormuz remains critical ... Why the Strait of Hormuz Is Vital, and Risky, for Shipping</a></li>
<li><a href="https://unctad.org/system/files/official-document/osgttinf2026d1_en.pdf">Strait of Hormuz Disruptions - UNCTAD</a></li>
<li><a href="https://www.cfr.org/backgrounders/irans-revolutionary-guards">The Islamic Revolutionary Guard Corps (IRGC) | Council on Foreign...</a></li>

</ul>
</details>

**标签**: `#Geopolitical Risk`, `#Energy Markets`, `#Oil Supply`, `#Strait of Hormuz`, `#Policy`

---

<a id="item-2"></a>
## [llama.cpp b9095 为 CUDA 添加内部 AllReduce，移除 NCCL 依赖](https://github.com/ggml-org/llama.cpp/releases/tag/b9095) ⭐️ 8.0/10

llama.cpp 版本 b9095 引入了一个内部 AllReduce CUDA 内核，使得张量并行无需依赖 NVIDIA 的 NCCL 库即可实现。该实现采用单阶段 CUDA 内核，通过固定内存标志进行跨 GPU 握手，并在每个 GPU 的一次启动中完成设备到主机拷贝和归约操作。 这一改动移除了 llama.cpp 中多 GPU LLM 推理的主要外部依赖 (NCCL)，简化了配置并减少了潜在的许可或兼容性问题。它使张量并行对于拥有少量 GPU 的用户更加易用，尽管目前仅支持 2 块 GPU 和小张量。 内部 AllReduce 提供者通过将 GGML_CUDA_ALLREDUCE 环境变量设置为 "internal" 来选择；默认仍为 NCCL。当前限制为仅支持 2 块 GPU、FP32 精度以及最大 256 KB 的张量；不支持的配置会回退到通过元后端的 CPU 归约。

github · github-actions[bot] · May 10, 09:43

**背景**: AllReduce 是一种集合通信操作，它将来自多个 GPU 的数据组合起来，并将结果分布回所有 GPU，这对于跨设备的同步训练和推理至关重要。NCCL（NVIDIA 集体通信库）是一个高性能库，提供优化的 AllReduce 及其他原语，但增加了依赖，部分用户可能出于简化或许可原因希望避免。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Collective_operation">Collective operation - Wikipedia</a></li>
<li><a href="https://developer.nvidia.com/nccl">NVIDIA Collective Communications Library (NCCL)</a></li>
<li><a href="https://github.com/NVIDIA/nccl">GitHub - NVIDIA/nccl: Optimized primitives for collective ... Demystifying NCCL: An In-depth Analysis of GPU Communication ... Unpacking NCCL: A Deep Dive into Multi-GPU Communication NVIDIA/nccl | DeepWiki NVIDIA Collective Communications Library (NCCL) nvidia-nccl-cu12 · PyPI</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#CUDA`, `#AllReduce`, `#tensor parallelism`, `#open source`

---

<a id="item-3"></a>
## [硬件认证作为垄断助推器](https://grapheneos.social/@GrapheneOS/116550899908879585) ⭐️ 8.0/10

一份详细的分析指出，苹果和谷歌的硬件认证技术缺乏零知识证明，有风险通过将用户锁定在经批准的设备上来助长数字垄断并侵蚀用户隐私。 这很重要，因为硬件认证正成为欧盟数字钱包等数字身份系统的要求，可能让苹果和谷歌控制对基本服务的访问，形成双头垄断。 认证过程使用绑定硬件的密钥和证书，但如果没有零知识证明，每个认证数据包都可用来将操作链接到特定设备，从而破坏隐私。

hackernews · ChuckMcM · May 10, 17:54

**背景**: 硬件认证是一种技术，设备利用内置的安全硬件向远程服务器证明其身份和完整性。零知识证明允许在不泄露任何额外信息的情况下证明某个陈述的真实性。苹果和谷歌当前的实现并未使用这些保护隐私的技术，这意味着认证会话可以被追踪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.apple.com/en-uz/guide/security/sec97eb9e2f2/web">The attestation process uses hardware -bound keys and certificates.</a></li>
<li><a href="https://developer.android.com/privacy-and-security/security-key-attestation">Verify hardware -backed key pairs with key attestation | Security</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>

</ul>
</details>

**社区讨论**: 评论者表达担忧，认为缺乏零知识证明使得认证可被关联，而欧盟数字钱包的要求实际上将数字身份绑定到美国科技双头垄断。有人将之与英特尔 1999 年 CPU 序列号争议和 TPM 强制要求进行历史类比。

**标签**: `#hardware attestation`, `#privacy`, `#monopoly`, `#digital identity`, `#trusted computing`

---

<a id="item-4"></a>
## [马里兰州居民因外州 AI 数据中心面临 20 亿美元电网升级费用](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises) ⭐️ 8.0/10

马里兰州人民律师办公室向 FERC 投诉 PJM Interconnection，计划向马里兰居民收取 20 亿美元输电升级费用，这些升级主要用于服务外州的 AI 数据中心。 此案例为 AI 基础设施成本的分配树立了先例，可能迫使一个州的居民补贴另一个州的能源密集型数据中心，并可能触发成本分配和纳税人保护方面的监管变革。 20 亿美元是马里兰州在 PJM 更大范围区域输电升级成本中的份额，这些成本根据现有 PJM 成本分摊规则分配。投诉认为这违反了 FERC 的'受益者付费'原则和马里兰的纳税人保护承诺。

hackernews · lemonberry · May 10, 21:16

**背景**: PJM Interconnection 是管理美国中部大西洋和中西部 13 个州电网的区域输电组织（RTO）。根据现行 PJM 成本分摊规则，输电升级成本通常由所有成员公用事业公司共同承担，无论新增负荷来自何处。FERC 的规定通常要求将成本分配给从升级中受益的用户，但实施过程常引发争议。AI 数据中心是电力需求的新主要来源，推动了电网扩建需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises">Maryland citizens slapped with $2 billion power grid upgrade bill for out-of-state AI data centers — state complains to federal energy regulators, says additional cost breaks ‘ratepayer protection pledge’ promises | Tom's Hardware</a></li>
<li><a href="https://www.ferc.gov/explainer-transmission-planning-and-cost-allocation-final-rule">Explainer on the Transmission Planning and Cost Allocation Final Rule | Federal Energy Regulatory Commission</a></li>
<li><a href="https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/fact-sheets/project-cost-allocation.pdf">Who Pays for New Transmission Projects? - pjm.com</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对大型企业利益似乎凌驾于地方监管机构之上的不满，一些人质疑为何公用事业定价依赖固定平台费而非使用费。其他人建议 AI 公司应投资聚变反应堆或完全承担其产生的基础设施成本，而不是将负担转嫁给普通纳税人。

**标签**: `#energy`, `#regulation`, `#ai infrastructure`, `#grid modernization`, `#cost allocation`

---

<a id="item-5"></a>
## [《纽约时报》因人工智能幻觉更正错误引语](https://simonwillison.net/2026/May/10/new-york-times-editors-note/#atom-everything) ⭐️ 8.0/10

《纽约时报》发布编辑说明，更正了一篇文章中错误归因于加拿大保守党领袖皮埃尔·波利耶夫的引语，该引语实际上是人工智能对其观点的摘要。 这一事件凸显了人工智能幻觉在新闻业中的风险，生成式 AI 工具会产生看似合理但虚假的信息，可能削弱对新闻来源的信任。 记者使用了一个 AI 工具，该工具生成了对波利耶夫观点的总结性引语，但将其呈现为直接引语。《纽约时报》更正了文章，并指出记者应核实 AI 输出内容。

rss · Simon Willison · May 10, 23:58

**背景**: AI 幻觉指的是大型语言模型产生事实错误但看似合理的输出。这种错误在需要准确性的场景中尤其有害，例如新闻业。这个案例是一个具体实例，表明一家主要新闻机构因未经核实就信任 AI 生成内容而遭受后果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.evidentlyai.com/blog/ai-hallucinations-examples">8 AI hallucinations examples</a></li>

</ul>
</details>

**标签**: `#ai-ethics`, `#hallucinations`, `#generative-ai`, `#journalism`, `#misinformation`

---

<a id="item-6"></a>
## [路易斯·罗斯曼为受威胁的 OrcaSlicer 开发者提供法律援助](https://www.tomshardware.com/3d-printing/louis-rossmann-tells-3d-printer-maker-bambu-lab-to-go-bleep-yourself-over-its-lawsuit-against-enthusiast-right-to-repair-advocate-offers-to-pay-the-legal-fees-for-a-threatened-orcaslicer-developer) ⭐️ 7.0/10

知名维修权倡导者路易斯·罗斯曼（Louis Rossmann）主动提出承担一名 OrcaSlicer 开发者的法律费用，该开发者因软件分支（据称连接了 Bambu Lab 的私有云 API）而受到 Bambu Lab 的诉讼威胁。 此举升级了 3D 打印领域的维修权争论，可能威慑企业对开源贡献者的恐吓，并影响消费者对 Bambu Lab 生态系统的信任。 争议中的分支据称与 Bambu 的非公开云 API 交互以模仿 Bambu Studio，而非直接连接打印机；罗斯曼的提议涵盖该开发者的法律代理费用。

hackernews · iancmceachern · May 10, 14:47

**背景**: OrcaSlicer 是一个流行的开源 3D 打印机 G 代码生成器，支持包括 Bambu Lab 打印机在内的多种型号。Bambu Lab 此前曾因试图限制离线访问而遭到反对，引发了维修权担忧。路易斯·罗斯曼是一位知名的 YouTuber 和活动家，经常资助针对反维修行为的法律斗争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.orcaslicer.com/">OrcaSlicer — Official Website & Downloads (Orca Slicer)</a></li>
<li><a href="https://github.com/OrcaSlicer/orcaslicer">GitHub - OrcaSlicer/OrcaSlicer: G-code generator for 3D ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持路易斯·罗斯曼的行动，许多人对 Bambu Lab 的行为表示愤怒并誓言抵制其产品。有人指出该分支访问的是私有云 API 而非直接连接打印机，但仍谴责法律威胁。Exabrial 称赞罗斯曼的真实性，而 ChristianJacobs 等人则认为这是 Bambu 反消费者立场的又一例证。

**标签**: `#3d-printing`, `#right-to-repair`, `#open-source`, `#legal`, `#community`

---

<a id="item-7"></a>
## [西班牙成为欧洲最便宜电力市场，但家庭电价更高](https://janrosenow.substack.com/p/spain-just-became-one-of-europes) ⭐️ 7.0/10

由于可再生能源发电量高以及电网互联有限，西班牙的批发电价已成为欧洲最低之一，但西班牙家庭支付的电价仍然高于欧盟平均水平。 这凸显了电力市场设计的复杂性——廉价发电并不自动转化为消费者的低零售电价，并且强调了电网互联在价格形成中的作用。 西班牙与法国的互联容量仅占装机容量的 2.8%，使其与欧洲核心电网隔离，减少了套利机会并保持了低批发价格；然而，管制收费和税收使得家庭电价居高不下。

hackernews · marc__1 · May 10, 16:31

**背景**: 电力市场通常根据满足需求所需的最末电厂的边际成本定价，因此高可再生能源渗透率降低了边际成本。西班牙的地理隔离和低互联容量意味着它无法轻易出口过剩的廉价电力，也无法在需要时进口昂贵电力，使其批发市场与邻国脱钩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.endesa.com/en/the-e-face/energy-sector/how-electricity-market-works-in-spain">How the electricity market works in Spain | Endesa</a></li>
<li><a href="https://www.energymonitor.ai/market-design/can-spain-extend-its-electricity-market-design-to-all-of-europe/">Spain's electricity market design: the ‘Iberian exception ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出标题具有误导性：尽管发电成本低廉，西班牙的家庭电价仍高于欧盟平均水平。一位评论者指出，远期合约（如 CAL27）在西班牙高于法国或北欧国家，表明长期价格令人担忧。另一位强调电网互联而非发电是关键的制约因素，输送能源的成本可能高于发电本身。

**标签**: `#energy`, `#electricity markets`, `#renewables`, `#Spain`, `#policy`

---