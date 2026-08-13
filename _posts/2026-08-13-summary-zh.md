---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> From 138 items, 10 important content pieces were selected

---

1. [Qwen3.8-2.4T-A95B：2.4 万亿参数开源 MoE 模型发布](#item-1) ⭐️ 9.0/10
2. [Tailscale 将数据库损坏追溯到存在 16 年的 SQLite WAL-Reset 漏洞](#item-2) ⭐️ 8.0/10
3. [xAI 发布 Grok 4.6，引发基准测试可信度辩论](#item-3) ⭐️ 8.0/10
4. [llama.cpp b10369 新增 Pocket-TTS 支持，解码器提速 80%](#item-4) ⭐️ 7.0/10
5. [DeepSeek V4 Pro 0813 登陆 OpenRouter，低成本高性能报告涌现](#item-5) ⭐️ 7.0/10
6. [Chrome 解码小尺寸 JPEG 时产生伪影，与 Firefox 不同](#item-6) ⭐️ 7.0/10
7. [高尔斯分析 LLM 擅长哪些数学问题](#item-7) ⭐️ 7.0/10
8. [Woxi：用 Rust 重写的开源 Wolfram 语言解释器](#item-8) ⭐️ 7.0/10
9. [研究者借投机解码窃取专有大模型的推理轨迹](#item-9) ⭐️ 7.0/10
10. [WhatsApp 宣布推出兼顾端到端加密与可验证性的诈骗警报功能](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Qwen3.8-2.4T-A95B：2.4 万亿参数开源 MoE 模型发布](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen 发布了 Qwen3.8-2.4T-A95B，这是一个拥有 2.4 万亿参数、950 亿活跃参数的混合专家（MoE）模型，提供了 BF16（4.9TB）和 FP8 量化版本，以及一个可在消费级硬件上运行的 397GB 1 比特量化版。模型卡称其性能介于 Opus 4.8 和 Fable 5 之间。 这是一次前沿规模的开源权重发布，使开放模型接近顶级性能。397GB 的 1 比特量化版本可能让个人用户在单台工作站上运行与领先专有系统竞争能力的模型，从而改变本地 AI 推理的实用性格局。 完整 BF16 模型为 4.9TB，FP8 版本体积小得多；1 比特量化版惊人的仅有 397GB，包含 950 亿 MoE 活跃参数。许可证允许内部或年收入低于 5000 万美元的公司免费使用，超过该门槛则有相应限制。

hackernews · Philpax · Aug 12, 15:01

**背景**: 混合专家（MoE）架构每个 token 只激活一部分参数，从而在可控计算成本下实现巨大的总参数量。FP8 和 BF16 等低精度格式降低了显存和带宽需求，而 1 比特量化则大幅缩小模型体积，尽管可能影响质量。这些技术推动着越来越大、且能在更易获得的硬件上运行的开源权重模型的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cameronrwolfe.substack.com/p/moe-llms">Mixture-of-Experts (MoE) LLMs - by Cameron R. Wolfe, Ph.D.</a></li>
<li><a href="https://www.runpod.io/articles/guides/fp16-bf16-fp8-mixed-precision-speed-up-my-model-training">How can using FP16, BF16, or FP8 mixed precision speed up my model training?</a></li>
<li><a href="https://en.wikipedia.org/wiki/1.58-bit_large_language_model">1.58-bit large language model - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Qwen3.8-2.4T-A95B 定位为 Kimi k3 的竞争对手，但发布时仅提供 BF16 和 FP8 版本，因此服务难度更大。397GB 的 1 比特量化版本受到称赞，认为它把 Opus 4.5 级别的性能带到了消费级硬件上；也有人对开源权重版本缺少视觉输入和 100 万上下文表示遗憾。

**标签**: `#AI`, `#open-source-llm`, `#qwen`, `#model-release`, `#inference`

---

<a id="item-2"></a>
## [Tailscale 将数据库损坏追溯到存在 16 年的 SQLite WAL-Reset 漏洞](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale 发布了一篇事后分析，说明其反复出现的数据库损坏事件最终被追溯到 SQLite WAL 模式中一个已存在至少 16 年的竞态条件。他们与 SQLite 开发者合作，并资助了一个开源 VFS shim，帮助定位了这一被 SQLite 团队命名为“WAL-Reset bug”的问题。 这件事很重要，因为 SQLite 是世界上部署最广泛的数据库之一，WAL 模式被许多生产系统使用；一个无声的损坏 bug 可能多年未被发现。它也展示了一种企业资助开源调试工具的有说服力的模式。 据估计，WAL-Reset bug 存在于大约 2010 年以来的每个 SQLite 版本中，调查还发现了第二个过期的表达式索引 bug。Tailscale 的环境使用单个 Go 进程独占访问数据库，但损坏仍然发生，可见该竞态条件有多么隐蔽。

hackernews · ropbear · Aug 12, 14:22

**背景**: SQLite 的预写日志（WAL）模式通过将更改追加到 WAL 文件并定期将它们检查点写回主数据库，从而允许多个读取器与一个写入器并发运行。WAL-index 文件协调访问，而 WAL-reset 路径中的竞态会损坏索引。VFS shim 是围绕 SQLite 操作系统接口的轻量包装器，可以拦截并监测 I/O 操作；Tailscale 资助了一个这样的 shim 来帮助重现和追踪损坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL - Reset bug</a></li>
<li><a href="https://sqlite.org/vfs.html">The SQLite OS Interface or "VFS"</a></li>
<li><a href="https://sourcefeed.dev/a/a-16-year-old-sqlite-bug-was-eating-tailscales-databases">A 16-Year-Old SQLite Bug Was Eating... — SourceFeed</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏这篇详尽的文章，以及公司资助特定开源调试工具这一不寻常的案例（simonw）。一些人称赞 Tailscale 还购买了 SQLite 支持合同，另一些人则质疑 SQLite 是否适合高并发系统，认为它“替代的是 fopen，而不是 Postgres”（inigyou）。还有评论者引用了 Dijkstra 的名言：测试只能证明 bug 的存在，而不能证明其不存在。

**标签**: `#sqlite`, `#database`, `#debugging`, `#open-source`, `#tailscale`

---

<a id="item-3"></a>
## [xAI 发布 Grok 4.6，引发基准测试可信度辩论](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI 发布了 Grok 4.6，这是其前沿 AI 模型的最新版本，独立基准测试表明其性能可与其它领先模型竞争。官方新闻页面公布了这一发布，并附有 Artificial Analysis 的基准分析。 此次发布表明 xAI 已经达到或接近领先 AI 实验室设定的质量门槛，加剧了前沿模型市场的竞争。它也推动了业界关于快速基准提升究竟源于真正研究进展还是基准操纵的持续争论，这影响开发者与企业如何选择 AI 系统。 Grok 4.6 属于增量更新而非范式转变（依据新闻评分理由）。Artificial Analysis 的独立基准分析显示其性能具有竞争力；然而，社区反馈称 SpaceXAI API 现在会注入默认系统提示，可能覆盖用户指令并导致拒绝讨论系统提示。

hackernews · iLuddite · Aug 12, 15:32

**背景**: 前沿模型（frontier model）是一种高能力、通用用途的 AI 系统，能在大型数据上进行推理并在单个工作流中串联多个操作，通常代表某个时间段内最先进的 AI 模型。基准操纵（benchmark gaming）则指 AI 公司以人为手段抬高其在公开评估基准上的得分，从而侵蚀这些得分作为真实能力信号的可信度。围绕 Grok 4.6 基准结果的争论再次凸现了行业普遍担忧：当各实验室在极短时间内普遍出现指标大幅提升时，人们开始怀疑这些数字究竟来自真正的算法突破，还是被操纵的评测环境。Artificial Analysis 等独立基准分析正是为了绕过各家实验室的自我报告而提供更客观的对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nhimg.org/glossary/frontier-model/">What Is Frontier Model ? Definition & Examples</a></li>
<li><a href="https://www.mindstudio.ai/blog/benchmark-gaming-ai-inflated-scores-explained">What Is Benchmark Gaming in AI? Why Self-Reported Scores Are Often Inflated | MindStudio</a></li>

</ul>
</details>

**社区讨论**: 社区讨论总体持怀疑态度：一位评论者质疑如何在两个月内多个实验室突然达到 Fable 水平，暗示存在基准操纵。其他人承认 Grok 的竞争力及其作为良性竞争的价值，还有人称赞 Grok 4.5 相比话多的竞争对手更加简洁、快速。另有用户抱怨 API 的默认系统提示限制了对系统提示本身的讨论。

**标签**: `#AI`, `#Grok`, `#xAI`, `#benchmarks`, `#model release`

---

<a id="item-4"></a>
## [llama.cpp b10369 新增 Pocket-TTS 支持，解码器提速 80%](https://github.com/ggml-org/llama.cpp/releases/tag/b10369) ⭐️ 7.0/10

llama.cpp 的 b10369 版本新增了对 Kyutai 公司 Pocket-TTS 的支持，这是一个 1 亿参数的轻量级文本转语音模型。同时，它把 mtmd 解码器中的转置卷积重构为 GEMM + col2im 形式，使每帧生成时间在 CUDA 上降低 80%、在 CPU 上降低 50%。 这件事很重要，因为 llama.cpp 是使用最广泛的开源推理框架之一，加入一个适合 CPU 运行的 TTS 模型，使其成为更完整的本地多模态运行时。卷积优化还让语音生成在普通硬件上大幅提速，进一步支持完全在设备端运行的 TTS 应用。 旧的深度可分离上采样每个通道都构造一次卷积和一次拼接，导致计算图充满小节点；新方法将卷积核重塑为 [IC, K*OC]，并用一次 col2im_1d 散点累加完成，overlap-add 尾部、流式状态和偏置均保持不变。现有的 mmproj 文件需要重新转换，以携带新的可选键 clip.gen.audio.frames_after_eos 和 clip.gen.audio.pad_short_text。

github · github-actions[bot] · Aug 12, 04:52

**背景**: llama.cpp 是一个开源 C/C++ 项目，允许用户在 CPU 和消费级 GPU 上运行大语言模型和多模态模型，而无需专用服务器。Pocket-TTS 来自 Kyutai Labs，是一个 1 亿参数、设计为可在 CPU 上运行的文本转语音模型。转置卷积用于在音频解码器中上采样信号；将其表示为 GEMM（矩阵乘）加 col2im（列到图像）散点累加是一种常见优化，可以减少内核启动次数并改善缓存局部性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/kyutai-labs/pocket-tts">GitHub - kyutai-labs/pocket-tts: A TTS that fits in your CPU (and pocket) · GitHub</a></li>
<li><a href="https://grokipedia.com/page/Pocket_TTS">Pocket TTS</a></li>
<li><a href="https://github.com/ggml-org/ggml/pull/940">Add conv_transpose_1d_gemm by smeso · Pull Request #940 · ggml-org/ggml</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#text-to-speech`, `#performance`, `#machine-learning`, `#open-source`

---

<a id="item-5"></a>
## [DeepSeek V4 Pro 0813 登陆 OpenRouter，低成本高性能报告涌现](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 7.0/10

DeepSeek V4 Pro 0813 已发布，现在可以通过 OpenRouter 访问。早期用户反馈称赞其极低价格下的强劲性能，有用户花约 12.50 美元处理 20 亿 token，缓存命中率为 50%。 该发布进一步拉低了大型语言模型的成本/性能边界，使接近前沿的能力能以预算价格获得。这可能会加速开发者在原本依赖更昂贵替代品的情况下转而采用 DeepSeek 模型。 OpenRouter 的页面本身信息很少，但 DeepSeek 官方提供了 API 文档与基准。社区报告称在分布式物理引擎/交通模拟器上测试取得了显著改进，且没有引入新问题。

hackernews · explosion-s · Aug 12, 16:04

**背景**: DeepSeek 是一家以开源权重模型闻名的中国 AI 公司；其 R1 聊天机器人在 2025 年 1 月登上美国应用商店榜首而备受关注。V4 系列包含 Flash 和 Pro 变体，其中 Pro-Max 被称为目前最好的开源模型。OpenRouter 是一个 API 平台，可将请求路由到来自多个提供商的 400 多个 LLM，并按 token 透明计费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(product)">DeepSeek (product)</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek -ai/ DeepSeek - V 4 - Pro · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenRouter">OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，但多基于务实的成本/性能考量。一位开发者称在物理引擎负载上约 12.50 美元/20 亿 token 就取得了显著改进；其他人将其与 Kimi-K3、GLM-5.2 等性价比模型相提并论，同时指出 Opus 5 这类顶级模型对多数任务过于多余。也有用户指出 OpenRouter 页面缺少官方链接和基准，建议改用官方 API 文档。

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#cost-performance`, `#model release`

---

<a id="item-6"></a>
## [Chrome 解码小尺寸 JPEG 时产生伪影，与 Firefox 不同](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 7.0/10

开发者调查发现，Chrome 在缩小 JPEG 图片时会以较低分辨率进行解码，仅处理部分数据，导致微小图片出现视觉伪影。Firefox 则先完整解码再缩放，因此画面更清晰。 这种跨浏览器渲染差异影响依赖一致图标显示的 Web 开发者和 Electron 应用维护者。它提醒人们 JPEG 不适合用于小型 UI 元素，而浏览器的优化捷径可能破坏视觉保真度。 差异源于 Chrome 在缩小图片时采用部分 DCT 解码，这种近似方法会引入模糊或振铃效应。作者指出 JPEG 适用于照片而非图标，并建议使用与显示尺寸匹配的图片资源。

hackernews · gutechh · Aug 12, 14:00

**背景**: JPEG 压缩依赖于离散余弦变换（DCT），它将图像拆分为频率分量并通过丢弃高频数据来减小文件大小。当浏览器缩小图片时，可以选择先完整解压再重采样，也可以只解码低频率系数以直接生成小尺寸输出，后者是一种优化。Chrome 出于性能考虑选择了后者，但这会在小图片上产生可见伪影；Firefox 目前先完整解码再缩放，因此两个浏览器渲染的小 JPEG 经常不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Discrete_cosine_transform">Discrete cosine transform - Wikipedia</a></li>
<li><a href="https://cs.stanford.edu/people/eroberts/courses/soco/projects/data-compression/lossy/jpeg/dct.htm">Lossy Data Compression: JPEG</a></li>

</ul>
</details>

**社区讨论**: 评论区基本认可这一发现：有人提到在 Electron 中遇到类似的 PNG 渲染问题，也有人强调真正的解决办法是使用尺寸合适的图片。一位 Firefox 贡献者提供了关于低分辨率解码的进行中工作的链接；还有用户指出 Chrome 和 Firefox 使用不同的缩放算法，这可能比解码路径本身更能解释所见差异。另有人询问 Firefox 是完整渲染还是部分渲染，希望看到更全面的对比。

**标签**: `#browser rendering`, `#web development`, `#image scaling`, `#Chrome`, `#Firefox`

---

<a id="item-7"></a>
## [高尔斯分析 LLM 擅长哪些数学问题](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/) ⭐️ 7.0/10

菲尔兹奖得主蒂莫西·高尔斯发表博文，探讨大语言模型擅长哪些类型的数学，并以测试时扩展（test-time scaling）和采样而非原始基准分数来评估其表现。他还提出了识别真正达到人类水平的定理证明的标准，例如那些令人惊讶但事后看来优美而自然的证明。 这篇分析的重要性在于，它重新框定了 AI 社区评估 LLM 数学能力的方式，将注意力从基准准确率转向真正推动进步的算力密集型策略。它还引发了关于 AI 如何在数学研究中发挥作用这一战略性问题，而人类水平的证明在该领域一直是一个长期里程碑。 高尔斯的论述围绕测试时扩展和采样展开——即生成大量候选解并加以筛选，就像谷歌 AlphaCode 生成数百万个候选程序那样。他认为，识别人类水平的定理证明将涉及那些难以偶然发现、但事后看来优美而自然的证明。

hackernews · ColinWright · Aug 12, 10:04

**背景**: 测试时扩展是指在推理阶段分配额外的计算资源，例如让模型“思考”更久或采样大量候选输出，以提升问题求解能力。近期综述显示，这类方法在数学和编程等强推理任务上取得了突破。LLM 在寻找反例方面表现出特长，但在需要战术灵活性和战略监督的形式化定理证明上往往力不从心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://testtimescaling.github.io/">What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2503.24235">[2503.24235] A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?</a></li>
<li><a href="https://arxiv.org/html/2506.17104">Towards Advanced Mathematical Reasoning for LLMs via First-Order...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认同高尔斯的分析框架：有人指出该文本质上是在讨论测试时扩展，并引用 AlphaCode 在 2022 年仅靠普通采样取得的成功；还有人赞同其识别人类水平证明的标准。另有评论者分享了 AI 在数学领域成果的列表链接，推测 AI 对寻找反例的偏好，并质疑 AI 在处理并发代码困难的情况下能否应对时序逻辑。

**标签**: `#AI`, `#mathematics`, `#LLMs`, `#test-time-scaling`, `#theorem-proving`

---

<a id="item-8"></a>
## [Woxi：用 Rust 重写的开源 Wolfram 语言解释器](https://woxi.ad-si.com/) ⭐️ 7.0/10

Woxi 是一个用 Rust 编写的开源 Wolfram 语言解释器，并附带使用 iced 构建的类 Mathematica 图形界面 Woxi Studio。它还提供命令行、Jupyter 内核、Python 包、npm 包和 WASM 模块等多种运行方式。 Woxi 提供了一个免费、开源的 Wolfram 内核替代方案，毫秒级启动速度使其适合脚本和嵌入式场景，并能在浏览器中运行。如果项目持续成熟，可能会减少部分符号计算工作流对昂贵的 Mathematica 授权许可的依赖。 项目通过约 26,000 个单元测试和约 900 个 .wls 脚本快照测试来保证语言兼容性。目前作者专注于修复边界情况、提升性能和发展社区，Woxi 尚未完全替代 Mathematica。

hackernews · adius · Aug 12, 10:06

**背景**: Wolfram 语言是 Stephen Wolfram 开发的、基于知识库的符号编程语言，代码由内核执行，Mathematica 是最为人所知的前端。符号计算又称计算机代数，它以精确的符号形式处理数学表达式，而不是数值近似。虽然已有 Sage、Maxima、SymPy 等开源替代品，Woxi 的目标是用 Rust 提供一个快速、集成且可嵌入的重实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wolfram.com/language/elementary-introduction/2nd-ed/what-is-the-wolfram-language.html">What Is the Wolfram Language : Elementary Introduction to the...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computer_algebra">Computer algebra - Wikipedia</a></li>
<li><a href="https://www.socratica.com/pages/wolfram-language">Wolfram Language</a></li>

</ul>
</details>

**社区讨论**: 评论总体积极：有用户验证 Woxi Studio 能显示多元微积分可视化，还有用户在自己的测试中发现 Woxi 比 Sympy、Xcas 和 Maxima 更能给出预期答案，并因此对项重写语言产生兴趣。也有评论提出保留意见，包括缺少 % 变量和乱序执行等便利功能、希望增加控制系统模块，以及指出这其实是六个月前报道过的重复发布。

**标签**: `#wolfram-language`, `#rust`, `#open-source`, `#symbolic-computation`, `#mathematica`

---

<a id="item-9"></a>
## [研究者借投机解码窃取专有大模型的推理轨迹](https://www.latent.space/p/ainews-how-to-steal-a-reasoning-trace) ⭐️ 7.0/10

Latent Space 通讯报道了一种新演示的攻击方法，可从专有 LLM API 窃取隐藏的推理轨迹。论文《Stealing Reasoning Traces from Proprietary LLM APIs》中描述的方法，将前沿模型生成的加密推理轨迹注入同一厂商不受严格保护的兄弟模型，迫使该模型以明文形式输出轨迹，而无需对原模型进行越狱。 此事之所以重要，是因为推理轨迹是专有 AI 实验室最有价值且保护最严密的资产之一，而该攻击绕过了 Anthropic、OpenAI 和 Google 的反蒸馏防护。它把一种标准的推理优化技术——投机解码——变成了蒸馏侧信道，对 AI 安全、知识产权保护和竞争优势都有直接影响。 该攻击包含四种不同的攻击向量，可绕过反蒸馏机制，并在 Anthropic、OpenAI 和 Google 的模型上演示了提取。根据 Simon Willison 的解读，攻击者可将前沿模型生成的轨迹重放到较弱的兄弟模型中，并以明文形式逐字恢复。

rss · Latent Space · Aug 12, 07:11

**背景**: 推理模型会产生隐藏的思维链，即推理轨迹；提供商对其加密，部分是为了保护专有技术并防止蒸馏。投机解码是一种广泛使用的推理优化技术：一个小型草稿模型先提出 token，再由较大的目标模型验证，从而在不改变输出质量的前提下加快生成速度。标题中化用莎翁名句（“玫瑰换个名字依然芬芳”）暗示：当投机解码被这样滥用时，它实际上就是一种蒸馏。此前 DistillSpec 等工作也表明，投机解码与知识蒸馏在 LLM 推理和压缩研究中密切相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://www.alphaxiv.org/abs/2608.09867">Stealing Reasoning Traces from Proprietary LLM APIs | alphaXiv</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI security`, `#reasoning traces`, `#speculative decoding`, `#model distillation`, `#proprietary AI`

---

<a id="item-10"></a>
## [WhatsApp 宣布推出兼顾端到端加密与可验证性的诈骗警报功能](https://engineering.fb.com/2026/08/12/security/how-were-building-scam-alert-whatsapp/) ⭐️ 7.0/10

Meta 工程博客宣布，WhatsApp 正在早期开发一项“诈骗警报”功能，可在检测诈骗的同时保留端到端加密和可验证性保证。该系统由用户控制、可关闭，仅当模型认为某条消息可能有诈骗风险时才会触发警报。 这件事很重要，因为它应对了即时通讯应用中日益增长的 AI 生成和社会工程诈骗威胁，同时不损害端到端加密这一核心隐私承诺。如果成功，它可能为加密平台如何在用户安全与隐私之间取得平衡树立先例。 该功能由用户控制且可关闭，仅当模型认为某条消息很可能属于诈骗时才会发出警报，并在设计上遵循端到端加密的核心保证。这篇文章属于早期预览，因此实现细节和发布计划尚未完全公布。

rss · Meta Engineering · Aug 12, 13:00

**背景**: 端到端加密确保只有发送者和接收者能阅读消息，这意味着服务提供商无法为了检测诈骗而查看内容。可验证性保证是一种密码学属性，允许用户在不必透露底层私密数据的情况下，确认某些操作或判断是正确的。在消息传递场景中，这能够让诈骗警报系统证明检测模型确实对消息执行了检测，同时保持消息内容私密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://engineering.fb.com/2026/08/12/security/how-were-building-scam-alert-whatsapp/">How We’re Building Scam Alert on WhatsApp With End - to - End ...</a></li>

</ul>
</details>

**标签**: `#security`, `#WhatsApp`, `#end-to-end encryption`, `#scam detection`, `#Meta`

---