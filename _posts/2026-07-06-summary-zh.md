---
layout: default
title: "Horizon Summary: 2026-07-06 (ZH)"
date: 2026-07-06
lang: zh
---

> From 75 items, 6 important content pieces were selected

---

1. [哈梅内伊葬礼开始，接班人缺席](#item-1) ⭐️ 10.0/10
2. [Rust 1.96.1 补丁修复关键安全漏洞](#item-2) ⭐️ 9.0/10
3. [欧盟理事会快速通过聊天控制 1.0，强制消息扫描](#item-3) ⭐️ 9.0/10
4. [俄罗斯弹道导弹在北约峰会前夕袭击基辅致 7 死](#item-4) ⭐️ 9.0/10
5. [llama.cpp b9876 修复 MoE 模型使用张量并行与 CPU 卸载时的崩溃](#item-5) ⭐️ 8.0/10
6. [Flipper Zero 转向最少社区互动，引发用户强烈不满](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [哈梅内伊葬礼开始，接班人缺席](https://www.nytimes.com/2026/07/04/world/middleeast/iran-funeral-supreme-leader-ali-khamenei.html) ⭐️ 10.0/10

伊朗最高领袖阿里·哈梅内伊的葬礼仪式已在德黑兰开始，他于 2 月 28 日在美国与以色列的空袭中身亡。其指定接班人穆杰塔巴·哈梅内伊在仪式期间仍未公开露面。 这一事件标志着伊朗面临关键的领导层过渡，可能对国内治理、核政策以及地区代理人冲突产生重大影响。新最高领袖的缺席引发了对其稳定性和继承公信力的质疑。 葬礼因持续战争而推迟，据报道祈祷大厅内有人呼吁杀死唐纳德·特朗普。穆杰塔巴·哈梅内伊的三位兄弟站在棺椁旁，但他本人未公开露面。

rss · NYTimes World · Jul 5, 09:19

**背景**: 阿亚图拉·阿里·哈梅内伊自 1989 年起担任伊朗最高领袖，掌握国家最高权力。其统治以权力集中、国内镇压以及遍布中东的武装代理人网络为特征。他在 2 月美以打击中身亡，留下了权力真空。

**标签**: `#geopolitics`, `#Iran`, `#Middle East`, `#succession`, `#proxy conflict`

---

<a id="item-2"></a>
## [Rust 1.96.1 补丁修复关键安全漏洞](https://github.com/rust-lang/rust/releases/tag/1.96.1) ⭐️ 9.0/10

Rust 1.96.1 是一个补丁版本，修复了 Cargo 的 libssh2 依赖中的多个 CVE（CVE-2025-15661、CVE-2026-55199、CVE-2026-55200），修复了 rustc 的 MIR 优化中的误编译问题，以及修复了 Cargo 中超时/重试行为的问题。 这些安全修复对整个 Rust 生态系统至关重要，因为 Cargo 是主要的包管理器，其依赖中的漏洞可能危及软件供应链安全。误编译修复也确保了优化代码的正确性，提高了可靠性。 libssh2 补丁解决了三个 CVE：CVE-2025-15661、CVE-2026-55199 和 CVE-2026-55200。MIR 优化修复纠正了一个可能导致错误机器码的误编译问题。超时/重试修复提高了 Cargo 在网络问题下的可靠性。

github · rustbot · Jul 5, 23:50

**背景**: MIR（中间层 IR）是 Rust 编译器在代码生成前用于优化的中间表示。MIR 优化可以提高性能并减少编译时间。libssh2 是一个实现 SSH2 协议的客户端 C 库，Cargo 使用它进行安全网络操作，如通过 git 获取依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://libssh2.org/">libssh 2</a></li>
<li><a href="https://rustc-dev-guide.rust-lang.org/mir/optimizations.html">MIR optimizations - Rust Compiler Development Guide</a></li>

</ul>
</details>

**标签**: `#security`, `#rust`, `#cargo`, `#compilation`, `#patching`

---

<a id="item-3"></a>
## [欧盟理事会快速通过聊天控制 1.0，强制消息扫描](https://www.heise.de/en/news/Chat-Control-1-0-EU-Council-forces-messenger-scans-via-fast-track-11353659.html) ⭐️ 9.0/10

欧盟理事会快速通过了聊天控制 1.0 法规，要求消息提供商扫描用户聊天内容以查找儿童性虐待材料（CSAM），这恢复了之前已到期的临时豁免。 此举强制对私人通信进行大规模监控，引发严重的隐私和加密担忧，并为削弱欧盟范围内的端到端加密开创先例，可能影响全球数百万用户和消息平台。 聊天控制 1.0 是对未加密消息的自愿扫描机制，但其快速通道通过绕过了议会的全面审查。更具争议的聊天控制 2.0（针对端到端加密服务）仍在单独讨论中。

hackernews · stavros · Jul 5, 11:44

**背景**: 聊天控制是指欧盟旨在检测和报告在线通信中儿童性虐待材料的法规。聊天控制 1.0 最初于 2021 年作为临时豁免通过，允许提供商自愿扫描未加密消息。该法规于 2024 年春季到期，但理事会现在寻求通过快速通道恢复它。批评者认为，这种扫描（尤其是客户端扫描）在技术上存在缺陷，会产生高误报率，并破坏隐私和加密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.heise.de/en/news/Chat-Control-1-0-EU-Council-forces-messenger-scans-via-fast-track-11353659.html">Chat Control 1.0: EU Council forces messenger scans via fast-track | heise online</a></li>
<li><a href="https://thecybersecguru.com/news/eu-chat-control-2026-guide/">EU Chat Control Is Back - And This Time It Might Actually Pass | The CyberSec Guru</a></li>

</ul>
</details>

**社区讨论**: 社区评论大多持批评态度，用户认为支持该措施的政客要么是无知要么是腐败。一些人区分了聊天控制 1.0（针对未加密消息）和更危险的 2.0（针对端到端加密），但仍谴责快速通道流程是监控的后门。

**标签**: `#EU policy`, `#chat control`, `#encryption`, `#privacy`, `#regulation`

---

<a id="item-4"></a>
## [俄罗斯弹道导弹在北约峰会前夕袭击基辅致 7 死](https://www.nytimes.com/2026/07/05/world/europe/kyiv-ukraine-russia-attack-nato.html) ⭐️ 9.0/10

2026 年 7 月 5 日，俄罗斯向乌克兰首都基辅发射弹道导弹，造成至少 7 人死亡，这是不到一周内的第二次重大袭击。 此次袭击发生在关键北约峰会前夕，被视为蓄意的升级信号，可能重塑联盟战略、增加国防开支，并加剧更广泛冲突的风险。 袭击使用了弹道导弹，且此次攻击紧随本周早些时候的类似大规模打击，表明在西方领导人齐聚之际，对首都的攻击是持续性的。

rss · NYTimes World · Jul 6, 02:52

**背景**: 自 2022 年 2 月俄罗斯全面入侵以来，乌克兰屡遭导弹袭击。原计划讨论对乌进一步军事援助和安全保障的北约峰会，如今笼罩在这直接挑衅的阴影之下。

**标签**: `#Geopolitical Risk`, `#Russia-Ukraine War`, `#NATO`, `#Security`, `#Missile Attack`

---

<a id="item-5"></a>
## [llama.cpp b9876 修复 MoE 模型使用张量并行与 CPU 卸载时的崩溃](https://github.com/ggml-org/llama.cpp/releases/tag/b9876) ⭐️ 8.0/10

llama.cpp 的 b9876 版本修复了一个关键崩溃问题，该问题在使用张量并行与 CPU 卸载的 MoE 专家时发生，具体原因是 MoE 路由器的输出张量非连续，触发了错误的断言。 此修复提高了在异构硬件（GPU + CPU）上运行大型 MoE 模型的可靠性，这是将模型扩展到 GPU 内存限制之外的常见配置。张量并行结合 CPU 卸载在生产推理中越来越常用，因此这个崩溃修复直接惠及许多部署。 该 bug 是由 `ggml_backend_meta_buffer_{get,set}_tensor` 中的 `GGML_ASSERT(ggml_is_contiguous(tensor))` 断言在检查分割状态之前运行导致的。MoE 路由器的输出张量是镜像的（GGML_BACKEND_SPLIT_AXIS_MIRRORED）且非连续；通过将分割状态查找移动到断言之上，修复允许镜像情况继续执行而不会触发错误断言。

github · github-actions[bot] · Jul 5, 18:29

**背景**: 混合专家（MoE）是一种神经网络架构，每个输入令牌只激活部分参数，从而在较低计算成本下实现更大模型。张量并行将模型层分割到多个设备（如 GPU）上，以降低每设备内存。CPU 卸载将模型部分（如 MoE 专家）移至 CPU 内存，进一步减轻 GPU 内存压力，但需要谨慎处理张量布局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.plainenglish.io/how-mixture-of-experts-moe-language-models-work-342b0db571c8">How Mixture of Experts ( MoE ) Language Models Work?</a></li>
<li><a href="https://lightning.ai/docs/pytorch/stable/advanced/model_parallel/tp.html">Tensor Parallelism — PyTorch Lightning 2.6.1 documentation</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#bug-fix`, `#MoE`, `#tensor-parallelism`, `#open-source`

---

<a id="item-6"></a>
## [Flipper Zero 转向最少社区互动，引发用户强烈不满](https://blog.flipper.net/future-of-flipper-zero-development/) ⭐️ 7.0/10

Flipper Zero 宣布战略调整，将最小化直接社区互动，固件维护聚焦于核心稳定性，实际上结束了社区驱动的活跃开发。 此举疏远了曾推动 Flipper Zero 流行的热情用户群体，可能促使开发者转向 Momentum 或 Extreme 等替代固件，损害生态系统的长期健康。 公司表示不会再进行实时社区互动，却讽刺地宣布了 AMA 活动；用户指出官方固件此前删除了合法的渗透测试工具，并在 Discord 上禁言讨论替代固件。

hackernews · croes · Jul 5, 18:22

**背景**: Flipper Zero 是一款便携式安全测试多功能工具，通过 Kickstarter 众筹，界面设有虚拟宠物海豚。其开源固件拥有庞大的爱好者社区，他们开发应用和修改。该设备能够读取、复制和模拟 RFID、NFC、无线电遥控等。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flipper_Zero">Flipper Zero</a></li>
<li><a href="https://grokipedia.com/page/Flipper_Zero">Flipper Zero</a></li>

</ul>
</details>

**社区讨论**: 用户表达了强烈失望，一位用户称他们在官方固件删除渗透测试工具并禁言替代固件讨论后已放弃官方固件。另一位批评者称这一转变是“最低限度维持生存”，并指出结束社区互动却宣布 AMA 的讽刺之处。

**标签**: `#flipper-zero`, `#firmware`, `#community`, `#hardware-security`, `#development`

---