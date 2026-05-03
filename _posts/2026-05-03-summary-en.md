---
layout: default
title: "Horizon Summary: 2026-05-03 (EN)"
date: 2026-05-03
lang: en
---

> From 21 items, 7 important content pieces were selected

---

1. [DeepSeek V4 Preview Open-Sourced with Strong Agent Abilities](#item-1) ⭐️ 9.0/10
2. [Mercury's experience with a 2-million-line Haskell codebase](#item-2) ⭐️ 8.0/10
3. [VideoLAN Releases dav2d: Fast Open-Source AV2 Decoder](#item-3) ⭐️ 8.0/10
4. [Developer’s Six-Year Journey Building Custom Maps for watchOS](#item-4) ⭐️ 8.0/10
5. [VS Code Inserted 'Co-Authored-by Copilot' into Commits Even When AI Disabled](#item-5) ⭐️ 8.0/10
6. [NASA's O2O Laser Sends 484 GB from Moon at 260 Mbps](#item-6) ⭐️ 8.0/10
7. [iPhone Runs 400B Parameter Model via SSD Streaming](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Preview Open-Sourced with Strong Agent Abilities](https://t.me/zaihuapd/41185) ⭐️ 9.0/10

DeepSeek released the preview version of DeepSeek-V4 as open-source, featuring two variants: DeepSeek-V4-Pro, which significantly improves agentic abilities and outperforms all evaluated open-source models in math, STEM, and competitive coding; and DeepSeek-V4-Flash, a smaller, faster, and cheaper model with still-strong reasoning and agent capabilities. This release pushes open-source LLMs closer to top proprietary models in agentic tasks, potentially reshaping the landscape for autonomous AI agents and making high-performance agentic AI more accessible and affordable for developers. DeepSeek-V4-Pro outperforms all open-source models on agent-related benchmarks and approaches '御三家' (GPT, Claude, Gemini) performance. V4-Flash uses smaller parameters and activation for faster, more economical inference, while a 'Flash-Max' variant offers near-Pro reasoning with larger thinking budget.

telegram · zaihuapd · May 3, 02:21

**Background**: Agentic AI refers to AI systems with autonomy to take actions and make decisions, going beyond simple assistance. '御三家' in the Chinese AI community denotes the three leading proprietary LLM families: GPT (OpenAI), Claude (Anthropic), and Gemini (Google). DeepSeek-V4 follows earlier open-source models like DeepSeek-V3 and R1, continuing the trend of open-weight models challenging proprietary systems. DeepSeek-V4-Pro is designed for high-precision tasks requiring deep reasoning, while DeepSeek-V4-Flash targets low-latency, high-throughput applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.grammarly.com/agentic-ai">What is Agentic AI ? | Agentic AI 101</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1944892815285924215">Gemini、Claude、GPT御三家模型的个人体会和建议 - 知乎</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-deepseek-v4-flash-and-v4-pro-in-microsoft-foundry/4515174">Introducing DeepSeek V4 Flash and V4 Pro in Microsoft Foundry | Microsoft Community Hub</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#LLM`, `#Open Source`, `#AI Agents`, `#Model Release`

---

<a id="item-2"></a>
## [Mercury's experience with a 2-million-line Haskell codebase](https://blog.haskell.org/a-couple-million-lines-of-haskell/) ⭐️ 8.0/10

Mercury published a detailed post on maintaining over two million lines of Haskell in production, highlighting how strong typing prevents errors but also noting readability and productivity challenges. This case study provides rare evidence of Haskell's viability at scale in a high-stakes fintech environment, informing decisions for organizations evaluating functional programming languages. The codebase comprises two million lines, with types used to enforce critical business invariants, but the post cautions that excessive type modeling can lead to high-touch refactors and maintenance burdens.

hackernews · unignorant · May 3, 00:01

**Background**: Haskell is a statically typed, purely functional programming language renowned for its powerful type system and ability to encode invariants. Mercury is a financial technology company offering banking services, known for its engineering culture and use of Haskell in production. Functional programming emphasizes immutable data and pure functions, contrasting with imperative styles.

**Discussion**: Commenters generally acknowledged Haskell's type safety benefits but raised concerns about readability, overuse of types leading to rigid codebases, and lower productivity compared to languages like Rust. Some also noted that style issues like single-letter variable names plague Haskell codebases.

**Tags**: `#Haskell`, `#production engineering`, `#functional programming`, `#maintainability`, `#case study`

---

<a id="item-3"></a>
## [VideoLAN Releases dav2d: Fast Open-Source AV2 Decoder](https://code.videolan.org/videolan/dav2d) ⭐️ 8.0/10

VideoLAN has published dav2d, a new open-source AV2 video decoder designed to be the fastest and most portable implementation, targeting multiple CPU architectures including x86, ARM, and RISC-V. AV2 promises significant bitrate savings over AV1, and an efficient CPU decoder like dav2d can jumpstart ecosystem adoption before hardware decoders become available, mirroring the crucial role dav1d played for AV1. The dav2d codebase is currently focused on correctness, with planned assembly optimizations for x86, ARM, and RISC-V; the AV2 specification is still in draft status, but demos have been shown at CES 2026.

hackernews · dabinat · May 2, 17:32

**Background**: AV1 is a royalty-free video codec developed by the Alliance for Open Media, widely used by platforms like YouTube and Netflix. AV2 is its next-generation successor, aiming for up to 30% better compression. The dav1d decoder, written in hand-tuned assembly, was instrumental in enabling efficient AV1 playback on devices without hardware support. dav2d follows the same philosophy to accelerate AV2 adoption.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Dav2d-Open-Source-AV2-Decode">VideoLAN Publishes Dav2d For Open-Source AV2 Decoder</a></li>
<li><a href="https://videocardz.com/newz/videolan-publishes-dav2d-an-early-cpu-decoder-for-av2-video-codec">VideoLAN publishes dav2d, an early CPU decoder for AV2 video ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/AV2_(video_coding_format)">AV2 (video coding format)</a></li>

</ul>
</details>

**Discussion**: Commenters note that dav2d is described as the fastest AV2 decoder, and recall the transformative impact of dav1d on AV1 adoption. Some ask technical questions about usage (e.g., converting H.264 to AV2), while others mention the AV2 spec schedule has slipped past the original late-2025 target, remaining in draft as of May 2026.

**Tags**: `#AV2`, `#video codec`, `#dav2d`, `#open source`, `#multimedia`

---

<a id="item-4"></a>
## [Developer’s Six-Year Journey Building Custom Maps for watchOS](https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/) ⭐️ 8.0/10

A developer chronicled a six-year effort perfecting a custom mapping app for watchOS, featuring unique cartographic data with hiking trails not found in Apple Maps. This highlights the gap in Apple’s first-party outdoor mapping features and demonstrates how third-party innovation can answer the needs of niche users, offering valuable lessons for wearable app development. The app uses pre-rendered image tiles created by a hired cartographer, providing rich detail but requiring separate downloads for zoom levels and orientation, unlike Apple Maps’ dynamic rendering.

hackernews · valzevul · May 2, 21:14

**Background**: watchOS is the operating system for Apple Watch. Apple Maps offers limited hiking trail and topography information, even on the adventure-oriented Watch Ultra. Third-party apps can fill this void with custom cartography and specialized features.

**Discussion**: Commenters expressed frustration over Apple’s lack of hiking maps, confusion about the app’s pricing model, and admiration for the technical achievement. Some appreciated the custom design and nostalgic anecdotes, while others noted the absence of basic features like GPX import.

**Tags**: `#watchOS`, `#Apple Watch`, `#maps`, `#software development`, `#hiking`

---

<a id="item-5"></a>
## [VS Code Inserted 'Co-Authored-by Copilot' into Commits Even When AI Disabled](https://github.com/microsoft/vscode/pull/310226) ⭐️ 8.0/10

In pull request #310226, VS Code changed the default setting for 'git.addAICoAuthor' to 'all', causing 'Co-Authored-by: Copilot' to be appended automatically to commit messages, even when AI features were disabled and Copilot was not used. This undermines developer trust by falsifying authorship in version control history, a critical record for legal and ethical accountability, and reveals a pattern of prioritizing AI promotion over user consent. The configuration schema default was changed but the runtime fallback in repository.ts still called 'off', creating inconsistency. The Copilot bot's review warning about this was ignored, and setting 'disableAIFeatures' did not prevent the behavior.

hackernews · indrora · May 2, 19:57

**Background**: In Git, 'Co-authored-by' is a standard commit trailer used to credit multiple contributors. Misusing it without explicit user action misrepresents commit provenance. VS Code is a widely used code editor that integrates AI features via GitHub Copilot.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors">Creating a commit with multiple authors - GitHub Docs</a></li>
<li><a href="https://stackoverflow.com/questions/58525836/git-magic-keywords-in-commit-messages-signed-off-by-co-authored-by-fixes">github - Git magic keywords in commit messages (Signed-off-by...)</a></li>

</ul>
</details>

**Discussion**: The community overwhelmingly condemned the change as a breach of trust and an ethical violation. Commenters stressed that falsifying commit authors for marketing stats is unacceptable, and noted the Copilot bot's own warning was ignored. The approving developer apologized, but skepticism remains.

**Tags**: `#AI`, `#ethics`, `#version-control`, `#developer-tools`, `#Microsoft`

---

<a id="item-6"></a>
## [NASA's O2O Laser Sends 484 GB from Moon at 260 Mbps](https://dailygalaxy.com/2026/05/nasa-just-beamed-484-gigabytes-from-moon/) ⭐️ 8.0/10

During the Artemis II mission, NASA's O2O laser communication system successfully transmitted 484 gigabytes of data from the Moon at a downlink speed of 260 megabits per second, demonstrating a major leap in space communication bandwidth. This breakthrough enables near-real-time analysis of high-definition lunar imagery and supports smooth public video feeds, laying the groundwork for high-bandwidth communications on future lunar and Mars missions. The system was developed by MIT Lincoln Laboratory, with ground stations at NASA’s Jet Propulsion Laboratory, White Sands Complex, and the Australian National University’s Mount Stromlo Observatory; it once received 26 gigabytes in under an hour.

telegram · zaihuapd · May 3, 00:50

**Background**: Free-space optical communication uses infrared laser beams instead of radio waves, offering much higher data rates due to higher frequencies. NASA has been testing laser communications since 2013, including the Laser Communications Relay Demonstration (LCRD). The Orion Artemis II Optical Communications System (O2O) is the first operational laser system for a crewed lunar mission, overcoming challenges such as precise pointing and atmospheric interference.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artemis_II">Artemis II - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Free-space_optical_communication">Free-space optical communication</a></li>

</ul>
</details>

**Tags**: `#space exploration`, `#laser communication`, `#NASA`, `#Artemis`, `#optical communications`

---

<a id="item-7"></a>
## [iPhone Runs 400B Parameter Model via SSD Streaming](https://x.com/anemll/status/2035901335984611412) ⭐️ 8.0/10

The ANEMLL project has demonstrated an iPhone 17 Pro running a 400-billion-parameter Mixture-of-Experts model. By streaming expert weights from the SSD, the model consumes only 5.5 GB of memory at a speed of 0.6 tokens per second. This proves that extremely large models can run on mobile devices using storage as virtual memory, opening the door to advanced on-device AI without constant cloud connectivity. The model uses a Mixture-of-Experts architecture, where only a fraction of parameters are active per token; the Flash-MoE engine manages expert loading from the iPhone's NVMe SSD. The inference speed of 0.6 tokens per second is too slow for real-time interaction.

telegram · zaihuapd · May 3, 10:57

**Background**: Mixture-of-Experts (MoE) models achieve high parameter counts by partitioning into multiple 'experts', activating only a relevant subset per input, reducing compute. Still, storing all weights typically needs large RAM. Here, weights are streamed on-demand from the iPhone's fast NVMe SSD, drastically cutting memory use at the cost of speed.

<details><summary>References</summary>
<ul>
<li><a href="https://agent-wars.com/news/2026-03-24-iphone-17-pro-runs-a-400b-parameter-llm-via-ssd-streaming">iPhone 17 Pro Runs a 400B Parameter LLM via Flash Streaming</a></li>
<li><a href="https://github.com/tonbistudio/moe-ssd-streaming-windows">GitHub - tonbistudio/moe- ssd - streaming -windows: Running a 32 GB...</a></li>

</ul>
</details>

**Tags**: `#edge-computing`, `#large-language-models`, `#mobile-inference`, `#Flash-MoE`, `#iPhone`

---