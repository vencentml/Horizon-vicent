---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> From 90 items, 4 important content pieces were selected

---

1. [llama.cpp b10232 为 DeepSeek V4 超连接添加了 Metal 支持。](#item-1) ⭐️ 7.0/10
2. [eBay 骚扰运动致 5,600 万美元赔偿及监禁判决](#item-2) ⭐️ 7.0/10
3. [欧盟年龄验证强制要求硬件绑定证明，引发隐私担忧](#item-3) ⭐️ 7.0/10
4. [微软牵头 235 家企业力挺开放权重 AI](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [llama.cpp b10232 为 DeepSeek V4 超连接添加了 Metal 支持。](https://github.com/ggml-org/llama.cpp/releases/tag/b10232) ⭐️ 7.0/10

llama.cpp 的 b10232 版本实现了 DeepSeek V4 超连接操作 GGML_OP_DSV4_HC_COMB、GGML_OP_DSV4_HC_PRE 和 GGML_OP_DSV4_HC_POST，其 Metal 内核使用了 SIMDgroup 寄存器和 shuffle 进行优化。该版本还加入了 Metal 调度支持，并对生产环境的 Sinkhorn 迭代次数和嵌入宽度进行了测试。 这一更新使 Apple Silicon 用户能够通过 llama.cpp 在本地运行 DeepSeek V4——一个以超连接为核心架构特性的新一代模型。它扩展了 llama.cpp 对一个重要模型家族的后端支持，可能加快 Mac 和 iOS 设备上本地推理的普及。 该实现属于拉取请求 #26459，由 Codex 辅助完成，Thiago Padilha 共同撰写。llama.cpp 的操作文档仍将 DSV4_HC_* 操作列为未支持，这表明该版本可能是首批为这些操作提供可用 Metal 内核的版本之一。

github · github-actions[bot] · Aug 2, 18:57

**背景**: DeepSeek V4 是一个即将推出的大型语言模型，据称使用了流形约束超连接（mHC），这是一种残差路径上的改动，有助于提高训练效率并处理长上下文。超连接涉及拆分、加权求和和合并隐藏状态等操作，并使用 Sinkhorn 迭代算法进行归一化。Metal 是 Apple 的 GPU 框架，llama.cpp 利用它在 Apple Silicon 上本地运行大型语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/mhc/">Manifold-Constrained Hyper - Connections | Sebastian Raschka, PhD</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sinkhorn's_theorem">Sinkhorn's theorem - Wikipedia</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/docs/ops.md">llama.cpp/docs/ops.md at master · ggml-org/llama.cpp</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#Metal`, `#DeepSeek V4`, `#GGML`, `#Apple Silicon`

---

<a id="item-2"></a>
## [eBay 骚扰运动致 5,600 万美元赔偿及监禁判决](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2) ⭐️ 7.0/10

eBay 前安全高管因策划针对大卫和伊娜·施泰纳的骚扰运动被判刑，公司同意支付 5600 万美元赔偿。吉姆·鲍夫被判处 57 个月监禁，布赖恩·吉尔伯特被判已服刑时间及 2 万美元罚款。 此案凸显大型科技公司安全团队内部严重的公司治理失败，表明高管可能利用公司资源进行个人报复。这对企业问责制具有重大的法律、声誉和道德影响。 eBay 安全团队的七名成员（包括前警察队长）合作骚扰并恐吓施泰纳夫妇，这对夫妇发布批判 eBay 的新闻通讯。布赖恩·吉尔伯特被判处已服刑时间、一年监督释放及 2 万美元罚款；吉姆·鲍夫被判处 57 个月监禁。

hackernews · JumpCrisscross · Aug 2, 19:19

**背景**: 2019 年，eBay 安全高管发起行动，以压制批评 eBay 的新闻通讯运营者伊娜和大卫·施泰纳。骚扰行为包括威胁信息、包裹和上门监视。民事案件达成 5600 万美元和解，随后进行了刑事判决。此案凸显企业安全部门缺乏监督的危险性。

**社区讨论**: 评论者质疑骚扰是否仅限于施泰纳夫妇，认为很难相信只针对一对批评者，并希望调查人员关注前警察队长的职业生涯。另有评论者提到 eBay 费率过高，alexpotato 引用了斯科特·亚当斯关于缺乏监督导致不当行为的言论。

**标签**: `#corporate-governance`, `#legal`, `#ebay`, `#security`, `#ethics`

---

<a id="item-3"></a>
## [欧盟年龄验证强制要求硬件绑定证明，引发隐私担忧](https://linuxiac.com/eu-age-verification-project-mandates-hardware-bound-attestation/) ⭐️ 7.0/10

欧盟的年龄验证项目已确认，进行年龄检查必须使用硬件绑定证明，即通过设备内置的硬件密钥来证明设备完整性。Linuxiac 报道了这一政策，并引发了关于隐私、身份关联以及开源用户访问权的讨论。 这一强制要求对在线身份、隐私和平台竞争具有广泛影响，实际上迫使用户在基本年龄检查中依赖 Apple、Google 或类似的证明中介机构。桌面 Linux 用户和刷入自定义 ROM 的用户可能被排除在外，除非他们另外拥有一台受支持的设备。 此处的硬件证明不使用零知识证明或盲签名，因此静态硬件 ID 在技术上会暴露给证明中介机构。据称，欧盟委员会将该应用描述为临时性方案，长期目标是推出欧盟数字钱包，让用户只披露自己选择的事实（例如年龄）。

hackernews · RobotToaster · Aug 2, 20:44

**背景**: 硬件绑定证明的原理是在硬件信任根（如 TPM 2.0、Apple Secure Enclave 或 Android Keymaster/Play Integrity）内部生成密钥，并产生由该硬件密钥签名的证明声明。依赖移动设备证明的年龄验证实现，实际上会让不使用 Android 或 iOS 的用户无法使用，这是常见的批评点。欧盟还在推进数字身份框架，目标是让公民在不泄露额外个人信息的情况下证明年龄等事实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://linuxiac.com/eu-age-verification-project-mandates-hardware-bound-attestation/">EU Age Verification Project Mandates Hardware-Bound Attestation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Age_verification">Age verification - Wikipedia</a></li>
<li><a href="https://www.securew2.com/protocols/acme-da-hardware-bound-certificates">ACME Device Attestation: Hardware-Bound Certificates at Scale</a></li>

</ul>
</details>

**社区讨论**: 评论者对公开动机表示怀疑，认为真实目的是将强大的现实身份标识与线上行为关联起来，并质疑欧盟反垄断监管机构为何允许政府强制要求依赖 Apple 或 Google 账号。还有人指出，要求额外购买一台非 Linux 设备实际上是在排斥 Linux 用户；在没有零知识证明的情况下，硬件证明会暴露静态硬件 ID，除非中介机构互相串通。也有人强调该应用只是临时方案，属于欧盟推动选择性披露数字钱包的更广泛努力的一部分。

**标签**: `#age verification`, `#EU policy`, `#hardware attestation`, `#privacy`, `#identity`

---

<a id="item-4"></a>
## [微软牵头 235 家企业力挺开放权重 AI](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

微软牵头起草了一封落款为 2026 年 7 月 24 日的公开信，NVIDIA、亚马逊、OpenAI 等 235 家 AI 相关企业签署，主张开放权重 AI 模型对美国领导地位至关重要，不应被禁止。7 月 28 日发布的另一封公开信《Pacing the Frontier》由 1324 名前沿 AI 公司员工签署，呼吁国际协作以刻意放缓自动化 AI 研发速度。 这种协调一致的行业表态标志着业界在如何监管开放权重 AI 问题上出现重大分歧，直接挑战美国政府以安全为由限制此类模型的任何倾向。这场争论将影响未来多年的 AI 政策、竞争与安全。 值得注意，Anthropic 并未签署这封信；CEO Dario Amodei 警告威权政府可能滥用模型，呼吁打击'工业级蒸馏操作'，同时坚称 Anthropic 从未主张禁止开放权重。微软的公开信还把蒸馏视为正当开发技术加以辩护，而 Anthropic 将其视为安全风险。

rss · Simon Willison · Aug 2, 04:16

**背景**: 开放权重模型会把训练好的神经网络参数（权重）公开发布，供任何人下载和微调，这与完全封闭的模型不同。它也有别于通常同时公开训练代码与架构的开放源代码 AI。矛盾在于：开放权重既能让更多人审查和改进，也会让强大 AI 被广泛获取，增加滥用风险。这些公开信反映了美国政策层面对上述权衡的博弈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-models-why-every-enterprise-should-paying-misra-gi2qc">Open - Weight AI Models : Why Every Enterprise Should Be Paying...</a></li>
<li><a href="https://www.fierce-network.com/content/open-weight-ai-vs-open-source-ai-whats-difference">Open weight AI vs open - source AI : what’s the difference?</a></li>
<li><a href="https://shaam.blog/articles/anthropic-open-weights-position-2026">Anthropic's Open Weights Position Explained : What Dario Amodei...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open weights`, `#Microsoft`, `#regulation`, `#industry lobbying`

---