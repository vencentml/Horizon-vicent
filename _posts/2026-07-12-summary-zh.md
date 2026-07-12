---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> From 94 items, 5 important content pieces were selected

---

1. [美国在伊朗关闭霍尔木兹海峡后发动空袭](#item-1) ⭐️ 10.0/10
2. [委内瑞拉地震死亡人数超 4300，救援展开](#item-2) ⭐️ 10.0/10
3. [vLLM v0.25.0：默认使用 Model Runner V2，移除 PagedAttention，性能与 Transformers 持平](#item-3) ⭐️ 9.0/10
4. [特朗普政府传唤《纽约时报》记者，涉空军一号报道](#item-4) ⭐️ 9.0/10
5. [llama.cpp b9963 为 DeepSeek-OCR 添加多图块动态分辨率](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [美国在伊朗关闭霍尔木兹海峡后发动空袭](https://www.bbc.co.uk/news/articles/cj9gkpp0dkeo?at_medium=RSS&at_campaign=rss) ⭐️ 10.0/10

在伊朗伊斯兰革命卫队关闭霍尔木兹海峡并攻击一艘塞浦路斯籍船只后，美国对伊朗超过 170 个目标发动了空袭。 这一在关键能源要道的升级威胁全球石油供应，可能推高油价并影响全球经济。同时也增加了中东地区爆发更大规模军事冲突的风险。 美国打击了防空系统、无人机和导弹储存设施以及军用快艇，旨在削弱伊朗攻击民用船只的能力。伊朗在攻击一艘声称使用未经批准航线的船只后关闭了海峡。

rss · BBC World News · Jul 12, 01:55

**背景**: 霍尔木兹海峡是伊朗和阿曼之间的一条狭窄水道，全球约 20%的石油经过这里。伊朗此前曾威胁关闭该海峡作为筹码，伊斯兰革命卫队是一支被美国列为恐怖组织的伊朗主要军事力量。此次关闭和随后的空袭标志着美伊紧张局势的重大升级。

**标签**: `#geopolitical risk`, `#energy`, `#oil`, `#Strait of Hormuz`, `#military conflict`

---

<a id="item-2"></a>
## [委内瑞拉地震死亡人数超 4300，救援展开](https://www.theguardian.com/world/2026/jul/11/venezuela-quake-deaths-passes-4000-recovery-effort) ⭐️ 10.0/10

据委内瑞拉政府称，6 月 24 日发生的双震已造成超过 4300 人死亡、近 17000 人受伤，另有数千人失踪。 这场灾难是委内瑞拉历史上最致命的地震之一，引发了严重的人道主义危机，需要紧急国际援助，并具有广泛的地区影响。 连续地震夷平了沿海州拉瓜伊拉的整个地区，总统德尔西·罗德里格斯和联合国均已呼吁提供资金援助。

rss · The Guardian World · Jul 11, 17:23

**背景**: 委内瑞拉位于加勒比板块边界的地震活跃带。该国此前已面临经济崩溃和政治不稳定，这将严重阻碍灾后恢复工作。

**标签**: `#disaster`, `#Venezuela`, `#earthquake`, `#humanitarian crisis`

---

<a id="item-3"></a>
## [vLLM v0.25.0：默认使用 Model Runner V2，移除 PagedAttention，性能与 Transformers 持平](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，移除了旧的 PagedAttention 实现，并实现了 Transformers 后端与原生 vLLM 的性能持平。 此版本标志着 vLLM 的重大架构转变，简化了执行路径并提供了更快、更易于维护的推理性能。移除 PagedAttention 以及 Transformers 后端的性能提升将影响所有 vLLM 用户，使框架更加稳定和面向未来。 该版本包含来自 232 位贡献者的 558 次提交，新增了 LLaVA-OneVision-2 和 GLM-5/DeepSeek-V3.2 等模型，以及一个新的流式解析引擎用于工具调用/推理解析。此外，还引入了针对异构词表的通用投机解码（TLI）。

github · khluu · Jul 11, 20:06

**背景**: vLLM 是一个用于高吞吐量、内存高效的 LLM 推理和服务的开源库。Model Runner V2 (MRv2) 是对 vLLM 执行核心的重新设计，解决了 V1 中的设计缺陷并提供了更模块化、GPU 原生的输入准备。PagedAttention 是之前 vLLM 使用的一种注意力机制，现已被更新的后端取代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#vLLM`, `#inference`, `#open-source`

---

<a id="item-4"></a>
## [特朗普政府传唤《纽约时报》记者，涉空军一号报道](https://www.theguardian.com/us-news/2026/jul/11/justice-department-subpoenas-new-york-times-air-force-one) ⭐️ 9.0/10

2026 年 7 月 11 日，特朗普政府向多名《纽约时报》记者发出传票，要求他们就一篇关于卡塔尔赠送的空军一号飞机存在安全隐患的报道向联邦大陪审团作证。 此举是政府对媒体监督的显著升级，直接威胁新闻自由和消息来源保护，可能为涉及国家安全的调查性报道树立寒蝉效应的先例。 传票由执法人员送到记者家中，记者需在五天内前往曼哈顿的大陪审团作证，否则将面临处罚。

rss · The Guardian World · Jul 11, 14:17

**背景**: 《纽约时报》发表了一篇报道，详细描述了卡塔尔赠送给特朗普政府的新空军一号飞机存在的安全隐患。特朗普政府此前曾对媒体采取法律行动，但传唤记者到大陪审团作证是罕见且激进的举措，引发第一修正案的严重问题。

**标签**: `#press freedom`, `#government subpoena`, `#journalism`, `#Trump administration`, `#Air Force One`

---

<a id="item-5"></a>
## [llama.cpp b9963 为 DeepSeek-OCR 添加多图块动态分辨率](https://github.com/ggml-org/llama.cpp/releases/tag/b9963) ⭐️ 7.0/10

llama.cpp 版本 b9963 为 DeepSeek-OCR v1 引入了多图块动态分辨率支持，并统一了 DeepSeek-OCR v1 和 v2 的图像预处理。这使得 OCR 模型能够通过将图像分割成图块来处理可变分辨率的图像，从而提高识别精度。 这一更新增强了最流行的 LLM 推理引擎之一的多模态能力，能够在复杂文档上实现更准确、更灵活的 OCR。它降低了开发者将前沿 OCR 集成到本地、保护隐私的应用程序中的门槛。 DeepSeek-OCR v1 中的多图块动态分辨率允许处理高达 6×768×768 再加上一个 1024×1024 图块的图像，改进了对高分辨率文档的处理。统一的预处理器消除了 v1 和 v2 之间的冗余代码，简化了维护和未来的增强。

github · github-actions[bot] · Jul 11, 08:38

**背景**: llama.cpp 是一个开源的、高性能的 C/C++ LLM 推理实现，旨在本地消费级硬件上运行模型。DeepSeek-OCR 是 DeepSeek 推出的一系列光学字符识别模型，能够从图像中提取文本。多图块动态分辨率将输入图像分割成较小的图块，每个图块以不同分辨率处理，以同时捕捉细节和整体结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-OCR">deepseek-ai/ DeepSeek - OCR · Hugging Face</a></li>
<li><a href="https://www.deepseek-ocr.ai/docs">DeepSeek - OCR — Contextual Optical Compression</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#deepseek-ocr`, `#multimodal`, `#OCR`, `#release`

---