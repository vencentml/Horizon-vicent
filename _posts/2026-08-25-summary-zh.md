---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> From 117 items, 11 important content pieces were selected

---

1. [MetaRoCE：面向 AI 级以太网的全新 RDMA 传输协议](#item-1) ⭐️ 9.0/10
2. [人工智能引导无人机完成首次全自主致命攻击](#item-2) ⭐️ 9.0/10
3. [美加贸易战升级：特朗普对加拿大商品加征 50%关税](#item-3) ⭐️ 9.0/10
4. [MS Paint 和照片应用为 AI 图片隐式添加 GUID 水印](#item-4) ⭐️ 8.0/10
5. [全球海洋温度创历史新高，标志着气候变化加速](#item-5) ⭐️ 8.0/10
6. [seL4 在 AArch64 上的安全证明已完成](#item-6) ⭐️ 8.0/10
7. [FDA 批准 PrecivityAD2 血液检测用于阿尔茨海默病评估](#item-7) ⭐️ 8.0/10
8. [llama.cpp b10604 新增 DeepSeek 4 支持与张量并行](#item-8) ⭐️ 7.0/10
9. [IPFS 维护团队 Shipyard 逐步停止实施支持](#item-9) ⭐️ 7.0/10
10. [OpenAI 将 GPT-5.6 Sol 价格下调最高 33%，持续至 2026 年 11 月](#item-10) ⭐️ 7.0/10
11. [Meta 推出 MTIA 300：首款内置 NIC 的自研训练芯片](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [MetaRoCE：面向 AI 级以太网的全新 RDMA 传输协议](https://engineering.fb.com/2026/08/24/networking-traffic/metaroce-rdma-transport-ai-ethernet/) ⭐️ 9.0/10

Meta 发布了 MetaRoCE，这是一个为商品化以太网上的 AI 工作负载从头设计的 RDMA 传输协议。Meta 同时公开了 MetaRoCE 规范、参考软件实现和一致性测试。 MetaRoCE 为 AI 基础设施构建者提供了一个基于以太网的开放 RDMA 选项，可能减少对 InfiniBand 等专用网络硬件的依赖。若被广泛采用，它有望降低大规模 GPU 训练和推理集群的成本并提高灵活性。 该协议专为 AI 工作负载设计，旨在运行于商品化以太网而非专有网络之上。Meta 提供了规范、参考软件和一致性测试，以支持互操作性和生态采用。

rss · Meta Engineering · Aug 24, 18:02

**背景**: RDMA（远程直接内存访问）允许一台计算机通过网络直接读取另一台计算机的内存，而无需操作系统介入，从而实现高吞吐量和低延迟通信。以太网是广泛使用且成本效益高的网络标准，400Gbps 和 800Gbps 等高速版本正针对 AI 级工作负载进行优化。MetaRoCE 正是为这种基于以太网的 AI 网络环境从头构建的 RDMA 传输协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Remote_direct_memory_access">Remote direct memory access - Wikipedia</a></li>
<li><a href="https://blogs.nvidia.com/blog/what-is-rdma/">What Is RDMA and RoCE and How Did They Fuel... | NVIDIA Blog</a></li>
<li><a href="https://www.techtarget.com/searchnetworking/feature/Ethernet-scale-up-networking-powers-AI-infrastructure">Ethernet scale-up networking powers AI infrastructure | TechTarget</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#networking`, `#RDMA`, `#Ethernet`, `#Meta`

---

<a id="item-2"></a>
## [人工智能引导无人机完成首次全自主致命攻击](https://www.nytimes.com/2026/08/24/world/europe/russia-drones-autonomous-ai-kill-ukraine-war.html) ⭐️ 9.0/10

据乌克兰官员称，一架搭载 Nvidia 芯片并由完全自主人工智能引导的俄罗斯无人机造成三名乌克兰人死亡。这似乎是已知的首起完全由 AI 决策、无需人工干预的致命攻击。 这标志着战争形态的范式转变，表明致命性自主武器已不再是假设。它对军事理论、AI 伦理和军备控制具有深远影响，并对 Nvidia 等先进 AI 芯片的商业可及性提出紧迫问题。 该无人机使用了 Nvidia 芯片，很可能是为边缘 AI 计算设计的 Jetson 系列模块。乌克兰官员确认了此次袭击，《纽约时报》的报道将其视为武器脱离人类控制的反乌托邦式里程碑。

rss · NYTimes World · Aug 24, 14:24

**背景**: 致命性自主武器系统（LAWS）又称“杀手机器人”，利用 AI 在无人干预的情况下识别并攻击目标。Nvidia Jetson 系列（如 Jetson TX2）是市售的嵌入式 AI 平台，广泛用于无人机和机器人，使先进的 AI 制导变得相对容易获取。专家指出，无人载具和游荡弹药自主性不断提高，正使 AI、自主性与军事系统之间的界限日益模糊。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapon">Lethal autonomous weapon - Wikipedia</a></li>
<li><a href="https://fsi.stanford.edu/sipr/content/lethal-autonomous-weapons-next-frontier-international-security-and-arms-control">Lethal Autonomous Weapons: The Next Frontier in International Security and Arms Control | FSI</a></li>
<li><a href="https://www.electronicdesign.com/technologies/embedded/article/21804914/exploring-the-jetson-tx2">Exploring the Jetson TX 2 | Electronic Design</a></li>

</ul>
</details>

**标签**: `#AI weapons`, `#autonomous drones`, `#warfare`, `#military technology`, `#AI ethics`

---

<a id="item-3"></a>
## [美加贸易战升级：特朗普对加拿大商品加征 50%关税](https://www.nytimes.com/2026/08/23/world/canada/canada-us-trade-war-trump-carney.html) ⭐️ 9.0/10

加拿大暂停贸易谈判，促使特朗普总统宣布自 2027 年 1 月 1 日起对加拿大汽车、卡车、汽车零部件和钢铁加征 50%关税。加拿大总理马克·卡尼誓言要进行“对等”报复。 这标志着两个历史上经济联系紧密的邻国之间的贸易战大幅升级，威胁跨境供应链并给双方经济增加市场风险。争端可能导致两国消费者价格上涨并扰乱制造业。 关税将于 2027 年 1 月 1 日生效，涵盖汽车、卡车、汽车零部件和钢铁。特朗普还指责加拿大多年来“敲诈”美国，提到加拿大对美国农民征收的关税；卡尼则承诺进行“一分对一分”的报复。

rss · NYTimes World · Aug 24, 20:54

**背景**: 美国和加拿大长期以来互为重要贸易伙伴，在汽车和钢铁等行业深度融合。当前争端是两国因关税和贸易失衡问题关系恶化的最新表现，报复措施可能导致更广泛的经济冲突升级。

**标签**: `#trade-war`, `#tariffs`, `#US-Canada`, `#geopolitical-risk`, `#macro`

---

<a id="item-4"></a>
## [MS Paint 和照片应用为 AI 图片隐式添加 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

微软的画图（Paint）和照片（Photos）应用现在会在经过 AI 处理的图片中静默嵌入不可见的 GUID 水印，即使处理是在本地设备上由本地模型完成的。水印会自动添加，用户不会收到任何通知，也无法关闭。 这之所以重要，是因为每个水印都包含一个唯一的 GUID，可与用户的微软账户关联，从而事实上消除了 AI 编辑图片的匿名性。这会让用户面临法律风险，因为第三方可以传唤微软，以识别任何带水印图片的创建者。 根据分析，不可见水印的载荷由一个头部字节（0x4c）、一个 16 字节的 GUID 和一个校验和字节组成。即使 AI 操作完全在设备本地运行，微软似乎也会使用这种水印，而且用户无法在界面中禁用该机制。

hackernews · ComputerGuru · Aug 24, 15:28

**背景**: 不可见数字水印技术将机器可读的信息嵌入图像像素中，人眼无法察觉，但软件可以提取。GUID（全局唯一标识符）是常用于追踪对象或用户的 128 位值。为 AI 生成内容加水印的做法是更广泛行业趋势的一部分——C2PA 和谷歌的 SynthID 等倡议都旨在添加出处元数据，不过许多实现依赖云端生成或元数据，而不是设备本地的不可见水印。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://byteiota.com/ms-paint-invisible-server-guid-watermark-ai-image/">MS Paint Embeds Invisible Server GUIDs in Every AI Image | byteiota</a></li>
<li><a href="https://github.com/osoleve/GUIDWatermark">osoleve/GUIDWatermark: Proof of concept for discreetly watermarking ...</a></li>
<li><a href="https://github.com/ShieldMnt/invisible-watermark">GitHub - ShieldMnt/invisible-watermark: python library for invisible image watermark (blind image watermark) · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者表示，隐藏水印本身就是隐私问题，与 AI 无关，因为任何图片都可能通过传票追溯到微软账户。还有人指出微软在水印实现上曾出过疏漏，举了早前 Copilot 水印被错误地应用到所有 Azure DevOps 提交的例子，并因此建议避免使用画图或其他启用大语言模型的应用。

**标签**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI`, `#security`

---

<a id="item-5"></a>
## [全球海洋温度创历史新高，标志着气候变化加速](https://www.bbc.com/news/articles/c62m4gpnp78o) ⭐️ 8.0/10

据 BBC 报道，全球海洋已达到有记录以来的最高温度。这一纪录凸显了气候变化加速的态势，以及极端天气和海平面上升等相关风险。 创纪录的海洋高温是重要的气候指标，对极端天气、海洋生态系统和全球海平面有直接影响。这一消息表明，全球迫切需要加强气候行动和适应措施。 自 2017 年以来，海洋热含量每年都在打破纪录，趋势证实了长期海洋变暖的快速加速。海洋的高热容量使其能够吸收大量能量，而最新的纪录延续了这一令人担忧的趋势。

hackernews · tcp_handshaker · Aug 24, 19:19

**背景**: 海洋覆盖地球表面约 70%，具有很高的热容量，能够在温度变化较小的情况下储存大量能量。海洋热含量是衡量全球变暖的关键指标，而海洋热浪——海洋温度的极端上升——近几十年来频率和强度都在增加。监测海洋热量对于理解和模拟气候变化至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ocean_heat_content">Ocean heat content - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Marine_heatwave">Marine heatwave - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了担忧和对政府不作为的失望，有人指出美国正在扩大化石燃料开采并攻击可再生能源。其他人强调在气候科学中，几度之差可能意味着生存与毁灭的区别，还有人解释了冰融化的物理机制及其对海洋升温的作用。总体情绪是警惕与对政策应对的批评。

**标签**: `#climate`, `#oceans`, `#global warming`, `#environment`

---

<a id="item-6"></a>
## [seL4 在 AArch64 上的安全证明已完成](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

seL4 的安全证明现已在 AArch64 上完成，这标志着高可信系统形式化验证的一个重要里程碑。这一公告由 Proofcraft Systems 于 2026 年 8 月发布。 AArch64 广泛应用于移动、嵌入式和服务器系统，因此这一证明将 seL4 的保证扩展到主流架构。这增强了在自动驾驶、军事系统和云基础设施等安全关键型应用中使用 seL4 的理由。 该证明覆盖非 MCS（混合关键性系统）变体，且仅限单核（unicore），因此多核和 MCS 配置尚未包含在内。这一限制缩小了其在需要混合关键性或多核支持的系统中的即时应范围。

hackernews · snvzz · Aug 24, 11:32

**背景**: seL4 是一种为高安全性和高可靠性设计的微内核，也是首个具备功能正确性形式化证明的操作系统内核。形式化验证利用数学方法证明软件满足其规范，从而消除整类错误。AArch64 是 ARM 架构的 64 位执行状态，常见于智能手机、嵌入式设备以及日益增多的服务器。这一里程碑将 seL4 已验证的安全属性扩展到这一广泛采用的架构上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SeL4">seL4 - Wikipedia</a></li>
<li><a href="https://sel4.systems/">The seL4 Microkernel | seL4</a></li>
<li><a href="https://itsfoss.com/arm-aarch64-x86_64/">arm vs aarch 64 vs amd64 vs x86_64: What's the Difference</a></li>

</ul>
</details>

**社区讨论**: 评论者指出该证明仅限于非 MCS 和单核配置，一位用户开玩笑预测侧信道时序攻击将使该结果失效。还有人讨论生态系统，询问哪些操作系统使用 seL4，以及除 GenodeOS、LionsOS 和中国汽车制造商之外还有哪些私人部署。一个关键的反驳观点是，嵌入式与军工市场未来可能继续资助 seL4，但需要原生的 seL4/Linux 才能以能力模型令人信服地提升系统安全性。

**标签**: `#seL4`, `#formal verification`, `#AArch64`, `#security`, `#operating systems`

---

<a id="item-7"></a>
## [FDA 批准 PrecivityAD2 血液检测用于阿尔茨海默病评估](https://medicine.washu.edu/news/fda-clears-blood-test-to-aid-evaluation-for-alzheimers-disease/) ⭐️ 8.0/10

美国食品药品监督管理局（FDA）已批准基于 p-tau217 生物标志物的血液检测 PrecivityAD2，用于辅助阿尔茨海默病的评估。这标志着基于血液的痴呆症诊断取得了监管方面的里程碑式进展。 像 PrecivityAD2 这样的血液检测有望比目前的 PET 扫描或腰椎穿刺更易普及、创伤更小，从而推动阿尔茨海默病的筛查。此次监管批准可能会加速其在临床实践中的应用，并改变对认知衰退患者的评估方式。 PrecivityAD2 结合了 %p-tau217 生物标志物与 Aβ42/40 比值来识别大脑淀粉样蛋白沉积，与淀粉样蛋白 PET 和脑脊液检测高度一致。该检测定价约为 1,400–1,500 美元，一些评论者指出这一价格可能使其仅适用于已确诊疾病的患者。

hackernews · dabinat · Aug 24, 06:30

**背景**: 阿尔茨海默病的特点是大脑中 β-淀粉样蛋白斑块和 tau 蛋白缠结的积累。p-tau217 是一种磷酸化 tau 蛋白，已成为一种有前景的血液生物标志物，无需侵入性操作即可帮助识别阿尔茨海默病病理。由 C2N Diagnostics 开发的 PrecivityAD2 检测采用质谱法测量这些生物标志物，并通过算法得出可供临床使用的结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pblassaysci.com/blog/p-tau217-informative-biomarker-alzheimers-disease">P-tau217: An Informative Biomarker for Alzheimer's Disease? | PBL Assay Science</a></li>
<li><a href="https://c2n.com/news-releases/cnnbspdiagnostics-releases-the-precivityad2-blood-test-for-clinical-care">C₂N Diagnostics Releases the PrecivityAD2™ Blood Test for Clinical Care, A Robust Assay with High Concordance to Amyloid PET and CSF — C2N Diagnostics</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/38491912/">Clinical validation of the PrecivityAD2 blood test: A mass spectrometry-based test with algorithm combining %p-tau217 and Aβ42/40 ratio to identify presence of brain amyloid - PubMed</a></li>

</ul>
</details>

**社区讨论**: 社区评论者对这一获批普遍持欢迎态度，但也提出了实际担忧。有评论者指出，按 1,400–1,500 美元的定价，该检测可能仅对已确诊疾病患者具有成本效益，而更便宜的 p-tau217 检测（200–300 美元）或许更适合广泛筛查。另一位评论者质疑，对于检测呈阳性的人，是否存在经科学验证的干预或缓解措施；还有一位该领域从业者表示愿意回答关于该检测临床应用的问题。

**标签**: `#FDA`, `#Alzheimer's`, `#blood test`, `#biomarker`, `#diagnostics`

---

<a id="item-8"></a>
## [llama.cpp b10604 新增 DeepSeek 4 支持与张量并行](https://github.com/ggml-org/llama.cpp/releases/tag/b10604) ⭐️ 7.0/10

llama.cpp b10604 版本新增了对 DeepSeek 4 的支持，引入了张量模型并行模式（`-sm tensor`），并为多 GPU 推理实现了共享专家延迟全规约（shared expert delayed allreduce）。这使得 DeepSeek 4 模型可以在多 GPU 上运行，并减少通信等待开销。 DeepSeek 4 是重要的开放权重模型系列，而 llama.cpp 是最广泛使用的本地推理引擎；官方支持让个人用户和企业都能在消费级硬件上运行这些大型 MoE 模型。张量并行和延迟全规约优化对多 GPU 吞吐量至关重要，降低了自托管前沿模型的门槛。 新的 `-sm tensor` 模式实现了张量模型并行，对 head 拆分采用了更粗的粒度，并引入共享专家延迟全规约，将共享专家的通信与主 allreduce 解耦。此版本还包含 DeepSeek 4 的模型保存支持、dspark 修复和 dflash 按设备返回功能；需要注意的是，本构建中 macOS KleidiAI 支持被禁用。

github · github-actions[bot] · Aug 24, 07:17

**背景**: llama.cpp 是一个开源的 C/C++ 推理引擎，能在 CPU、GPU 等后端高效运行大语言模型。张量并行是将模型的不同层拆分到多个 GPU 上，而 allreduce（全规约）是一种跨设备对梯度或激活张量求和的集合通信操作；在 DeepSeek 这类混合专家（MoE）模型中，'共享专家'（shared experts）是对每个 token 都会执行的层，容易成为通信瓶颈。延迟全规约（delayed allreduce）技术通过错开共享专家的规约时机，使通信与计算重叠。DeepSeek 是一家中国 AI 实验室，以 V3、R1 等高性能开放权重模型闻名，本次版本面向的是其第四代 V4 系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>
<li><a href="https://docs.flashinfer.ai/generated/flashinfer.comm.trtllm_moe_finalize_allreduce_fusion.html">flashinfer.comm.trtllm_moe_finalize_ allreduce _fusion - FlashInfer...</a></li>
<li><a href="https://www.emergentmind.com/topics/ring-allreduce">Ring AllReduce : Distributed Gradient Sync</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek`, `#tensor parallelism`, `#local inference`, `#open-source AI`

---

<a id="item-9"></a>
## [IPFS 维护团队 Shipyard 逐步停止实施支持](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 7.0/10

IPFS 的主要维护组织 Interplanetary Shipyard 正在逐步停止其集中式实施支持，但 IPFS 项目本身将通过个人维护者资助继续推进。该公告澄清这并不意味着 IPFS 协议或项目终止。 这一变化标志着 IPFS 开发维护方式的重要转变，可能影响协议改进的速度和重点。依赖 IPFS 的开发者和组织应关注治理与资金如何从专门团队转向个人资助。 Shipyard 只是多个 IPFS 实现维护者之一，其集中式支持将被个人维护者资助取代。该公告仅涉及 Shipyard，不涉及更广泛的 IPFS 项目，后者仍在继续运行。

hackernews · iand · Aug 24, 15:48

**背景**: IPFS（星际文件系统）是一种分布式存储与访问系统，通过将内容与对等节点关联来保存和访问文件、网站、应用和数据，从而减少对中心服务器的依赖。Interplanetary Shipyard 是一个维护者组织，长期参与 IPFS 和 libp2p 的实现工作，包括面向浏览器的 WebRTC 项目，以推动 IPFS 在 Web 上的应用。此次转型也反映出开源去中心化基础设施在可持续资金方面的持续挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/">The end of IPFS at Shipyard</a></li>
<li><a href="https://docs.ipfs.eth.link/concepts/what-is-ipfs/">What is IPFS ? | IPFS Docs</a></li>
<li><a href="https://blog.ipfs.tech/2024-shipyard-improving-ipfs-on-the-web/">IPFS on the Web in 2024: Update From Interplanetary Shipyard</a></li>

</ul>
</details>

**社区讨论**: 社区情绪较为复杂：长期维护者对此感到遗憾，同时多位评论者强调应区分 Shipyard 停止运营与 IPFS 项目关闭。有人推荐 Iroh 等其他 p2p 方案，也有人批评 IPNS 和 Web 应用支持等技术决策，还有用户幽默地指出，要提交评论却要填写 Google 表单，这与去中心化理念有些矛盾。

**标签**: `#IPFS`, `#decentralized-storage`, `#open-source-maintenance`, `#p2p`, `#protocol-labs`

---

<a id="item-10"></a>
## [OpenAI 将 GPT-5.6 Sol 价格下调最高 33%，持续至 2026 年 11 月](https://developers.openai.com/api/docs/pricing) ⭐️ 7.0/10

OpenAI 已将 GPT-5.6 Sol 的输入 token 价格下调 20%，输出 token 价格下调 33%，优惠持续至至少 2026 年 11 月 21 日。新价格为每百万输入 token 4.00 美元、每百万输出 token 20.00 美元。 此次降价标志着 AI 推理价格战进一步加剧，直接影响开发者的成本结构和模型选型。它也对 Anthropic 等竞争对手构成压力，并反映出大语言模型推理日益商品化的趋势。 根据调整后的价格表，GPT-5.6 Sol 现在每百万 token 分别为：输入 4.00 美元、缓存输入 0.40 美元、缓存写入 5.00 美元、输出 20.00 美元，仍是 Luna 档位的 20 倍。此外，OpenRouter 仍叠加 50%折扣，实际价格降至每百万 token 输入 2.00 美元、输出 10.00 美元。

hackernews · tosh · Aug 24, 15:22

**背景**: GPT-5.6 是 OpenAI 于 2026 年 7 月 9 日发布的大语言模型系列，按能力从低到高分为 Luna、Terra 和 Sol 三个版本。Sol 是旗舰款、性能最强的模型，面向企业工作、编程、科学研究和网络安全等最高能力需求场景。此次降价发生在行业竞争加剧、推理成本持续下降的背景下。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6_Sol">GPT-5.6 Sol</a></li>
<li><a href="https://artificialanalysis.ai/articles/gpt-5-6-has-landed">GPT - 5 . 6 benchmarks across Intelligence, Speed... | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 评论者大多欢迎这场价格战，有人指出模型易于蒸馏和复制，削弱了 OpenAI 的护城河，使智能销售走向‘逐底竞争’。其他人则感谢具体的价格细节，强调 OpenRouter 的额外折扣，并讨论 Sol 在实际编程任务中相比 Claude Fable 5 的表现优劣。

**标签**: `#OpenAI`, `#AI pricing`, `#inference`, `#competition`, `#LLM economy`

---

<a id="item-11"></a>
## [Meta 推出 MTIA 300：首款内置 NIC 的自研训练芯片](https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/) ⭐️ 7.0/10

Meta 发布了 MTIA 300，这是其 MTIA 定制加速器家族中的首款训练芯片，内置 NIC chiplets 和通信卸载引擎。该芯片与 HCCL 通信库协同设计，使通信成为硬件中的一等公民。 这标志着 Meta 从通用 GPU 转向定制芯片的战略举措，旨在为大规模推荐模型训练协同设计计算与网络。如果成功，MTIA 300 可为 Meta 的排序和推荐工作负载带来更优异的性能与效率。 NIC chiplets 直接集成在芯片上，HCCL 构建使用网络 chiplets 和 NMC 引擎的工作包与子图来卸载通信。根据 ISCA 2026 论文，计算 chiplet 还包含带有 PCIe、DMA 和安全启动处理器的主机接口。

rss · Meta Engineering · Aug 24, 17:45

**背景**: MTIA 是 Meta Training and Inference Accelerator 的缩写，是 Meta 面向 AI 工作负载的定制芯片项目。深度学习推荐模型（DLRM）依赖海量嵌入表，并需要在成百上千个加速器之间频繁进行集合通信。在传统 GPU 系统中，通信由独立 NIC 和通用核心处理，会产生额外开销。MTIA 300 旨在通过将网络直接嵌入训练芯片来消除这一瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/">MTIA 300 : Meta's First Training Chip with Built-in NICs and...</a></li>
<li><a href="https://aisystemcodesign.github.io/papers/MTIA300_ISCA2026.pdf">MTIA 300 : Meta’s First Training Chip Featuring</a></li>
<li><a href="https://encord.com/blog/meta-ai-chip-mtia-explained/">All You Need to Know About Meta ’s New AI Chip MTIA</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Meta`, `#custom silicon`, `#networking`, `#training accelerators`

---