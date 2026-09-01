---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> From 133 items, 5 important content pieces were selected

---

1. [美伊在霍尔木兹海峡交火，为数周来首次](#item-1) ⭐️ 9.0/10
2. [谷歌从 Chrome 应用商店移除 MV2 扩展，包括 uBlock Origin](#item-2) ⭐️ 8.0/10
3. [研究人员借助文件攻击攻破 Claude Code 自动模式](#item-3) ⭐️ 8.0/10
4. [uv 通过 BLAKE3 哈希实现 wheel 缓存按文件去重](#item-4) ⭐️ 8.0/10
5. [OpenAI 广告业务年化收入达 10 亿美元，全球扩展](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [美伊在霍尔木兹海峡交火，为数周来首次](https://www.bbc.co.uk/news/articles/cx2z72x5z1po?at_medium=RSS&at_campaign=rss) ⭐️ 9.0/10

美国袭击了霍尔木兹海峡拉拉克岛上的伊朗火箭发射器，造成两人死亡，此前美方发现伊朗计划布设新水雷。作为回应，伊朗袭击了美军在约旦和阿联酋的基地。 这是美国自 7 月下旬以来首次对伊朗发动已知袭击，标志着这一关键石油运输通道的紧张局势升级。此次交火可能影响全球石油市场和地区安全。 拉拉克岛袭击造成两人死亡、两人受伤。美国中央司令部表示，在探测到伊朗计划向海峡布设新水雷后，于周日深夜发起打击，伊朗随后袭击了美军在约旦和阿联酋的基地。

rss · BBC World News · Aug 31, 13:47

**背景**: 霍尔木兹海峡是全球石油运输要道，战前约占全球海运石油供应量的五分之一。美方多次袭击伊朗导弹发射器和雷达，试图削弱伊朗对该水道的控制。特朗普上周声称美国海军首次清除了海峡中的水雷，伊朗否认这一说法。

**标签**: `#geopolitics`, `#Iran`, `#United States`, `#oil markets`, `#Strait of Hormuz`

---

<a id="item-2"></a>
## [谷歌从 Chrome 应用商店移除 MV2 扩展，包括 uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

谷歌已正式从 Chrome 网上应用商店移除 Manifest V2 (MV2) 扩展，包括 uBlock Origin。这是谷歌 MV2 弃用时间线的一个里程碑，升级到 Chrome 139 及更高版本的用户将无法再使用 MV2 扩展。 这是浏览器扩展生态中的一个重要执行里程碑，影响到数百万依赖 uBlock Origin 和其他 MV2 广告拦截器的用户。它引发安全和迁移方面的担忧，尤其是对非技术用户而言，他们在没有有效广告拦截的情况下更容易受到恶意广告的侵害。 根据谷歌官方时间表，Manifest V2 扩展在升级到 Chrome 139 及更高版本后将停止工作。uBlock Origin 使用 webRequest API 实时拦截和阻止网络请求，因此它无法在功能不受限制的情况下简单迁移到 Manifest V3。

hackernews · twapi · Aug 31, 21:10

**背景**: Manifest V2 (MV2) 是 Chrome 之前的扩展框架，而 Manifest V3 (MV3) 是较新的框架，它限制某些 API（包括 webRequest API）以提升安全性和性能。uBlock Origin 是一款免费开源的广告拦截器，在 Chrome 上有超过 2900 万活跃用户，在 Firefox 上有 1060 万，是 Firefox 上最受欢迎的扩展。谷歌多年前就宣布了 MV2 弃用计划，因此从 Chrome 网上应用商店移除这些扩展是一次计划中的过渡，而非意外。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline">Manifest V2 support timeline | Chrome for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">UBlock Origin</a></li>
<li><a href="https://chromeunboxed.com/manifest-v2-is-officially-dead-as-the-chrome-web-store-permanently-purges-legacy-extensions/">Manifest V2 is officially dead as the Chrome Web Store...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论普遍鼓励改用 Firefox，多位用户提到 uBlock Origin 在 Firefox 上表现最佳。一些人强调广告拦截现在已成为安全问题，尤其是对容易点击恶意广告的老年等弱势用户而言。其他人则对谷歌对网络的单方面控制表示不满，并表示会继续使用 Firefox。

**标签**: `#Chrome`, `#Manifest V2`, `#uBlock Origin`, `#ad blocking`, `#browser ecosystem`

---

<a id="item-3"></a>
## [研究人员借助文件攻击攻破 Claude Code 自动模式](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) ⭐️ 8.0/10

Embrace The Red 上发布的这项安全研究展示了一条针对 Claude Code 自动模式的具体攻击链，利用模型可预测的工具调用习惯和 Python 模块解析机制来劫持执行。攻击通过在被攻击者控制的目录中构造文件，遮蔽 Python 标准库模块实现。 该发现表明，即便是自动模式这样的权限管控功能，也只会对工具调用进行分类，而无法防御通过文件层面影响实际执行代码的攻击。对于越来越依赖自主 AI 代理的开发者来说，这一点至关重要，因为一个看似无害的文件可能在完全不触发安全检查的情况下悄然劫持代理行为。 该攻击专门利用 Claude 习惯性调用诸如 python -c 等熟悉工具的特点，并结合 Python 的模块解析顺序，使解压目录中的恶意 struct.py 能够遮蔽标准库。Anthropic 的自动模式虽然使用分类器阻止不可逆或破坏性操作，但该攻击暴露出一个盲区：代理本身被诱导执行了受攻击者影响的代码。

hackernews · Recursing · Aug 31, 07:49

**背景**: Claude Code 是 Anthropic 推出的代理式编程工具，自动模式（2026 年 3 月推出，后来成为默认选项）允许 Claude 在安全分类器保护下自行做出权限决定。Python 会按 sys.path 中的目录顺序搜索模块，如果攻击者能在解释器扫描的目录中放置一个与标准库同名的文件，该文件就可能被优先导入。这与 Python 依赖混淆和库劫持攻击类似，因此业界越来越推荐在基础设施层面将代理执行环境进行沙箱隔离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude by Anthropic</a></li>
<li><a href="https://www.hackingarticles.in/linux-privilege-escalation-python-library-hijacking/">Linux Privilege Escalation: Python Library Hijacking</a></li>
<li><a href="https://beyondscale.tech/blog/ai-agent-sandboxing-enterprise-security-guide">AI Agent Sandboxing: Enterprise Security Guide 2026</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为这项攻击设计巧妙，有人指出 python -c 对 Claude 而言是“承重墙”式工具，因此行为可预测。也有人反对将其称为提示注入，认为这更像是一种针对 Claude 的特洛伊木马；另一些人则强调真正的缓解措施是让代理在沙箱中运行，并关闭不必要的网络访问。

**标签**: `#AI security`, `#prompt injection`, `#Claude Code`, `#LLM agents`, `#sandboxing`

---

<a id="item-4"></a>
## [uv 通过 BLAKE3 哈希实现 wheel 缓存按文件去重](https://github.com/astral-sh/uv/pull/21327) ⭐️ 8.0/10

Astral 的 uv 项目合并了一个 PR，将 wheel 缓存重构为按 BLAKE3 哈希存储每个文件，从而在缓存的 wheel 之间实现文件级去重。这一变化通过消除重复文件改善了缓存完整性和磁盘占用。 uv 是使用最广泛的 Python 包管理器之一，其缓存设计是热安装如此之快的关键原因。这一架构变化通过减小缓存体积、防止数据损坏影响了数百万开发者，也为包管理器采用内容寻址存储开创了先例。 该 PR 使用 BLAKE3（一种快速且可高度并行的加密哈希）来命名和校验缓存文件。一条社区评论指出，实测的权衡是缓存体积约减少 10%，但性能约下降 4%，实现复杂度也随之增加。

hackernews · tosh · Aug 31, 06:03

**背景**: uv 是一个用 Rust 编写的 Python 包和项目管理器，能够非常快速地解析和安装依赖。wheel 是 Python 的预构建发行包；uv 缓存解压后的 wheel，并通过硬链接将其链接到环境中，这比 pip 每次解压缓存归档的方式更快。BLAKE3 是一种专为高速和并行化设计的加密哈希函数，非常适合内容寻址存储和完整性校验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/uv/">uv is an extremely fast Python package and project manager , written...</a></li>
<li><a href="https://github.com/astral-sh/uv">astral-sh/ uv : An extremely fast Python package and project manager ...</a></li>
<li><a href="https://github.com/BLAKE3-team/BLAKE3">GitHub - BLAKE3 -team/ BLAKE3 : the official Rust and C...</a></li>

</ul>
</details>

**社区讨论**: pip 维护者 @notatallshaw 指出，uv 的缓存是其热安装速度优势的主要来源，但也提到缺少如为下载功能重现精确发行版等特性。其他用户称赞 uv 对 Python 开发的影响，而 @CivBase 质疑约 10% 的缓存体积压缩是否值得约 4% 的速度下降和额外的复杂度。@TacticalCoder 热情地称赞 BLAKE3，并分享了他在类似去重/完整性工具中使用它的个人经验。

**标签**: `#uv`, `#python`, `#package-management`, `#caching`, `#deduplication`

---

<a id="item-5"></a>
## [OpenAI 广告业务年化收入达 10 亿美元，全球扩展](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads) ⭐️ 7.0/10

OpenAI 宣布，ChatGPT 广告业务的年化收入运行率已达到 10 亿美元，并正在全球扩张，以支持免费和低成本的 AI 访问。这标志着该公司首次公开其广告业务的收入里程碑。 这一里程碑表明 OpenAI 的商业模式正转向通过广告来补贴免费用户，可能重塑 AI 市场格局。它可以让更多人免费使用 ChatGPT，同时也促使竞争对手探索类似的变现方式。 年化收入运行率是将近期广告收入推算为全年数据的前瞻性估计，而非实际全年收入。OpenAI 此前宣布在 ChatGPT 中测试广告，并强调清晰标注、答案独立性、隐私保护和用户控制等措施。

rss · OpenAI News · Aug 31, 04:00

**背景**: 年化收入运行率是一种财务指标，将公司当前某个较短时期的收入折算为全年等值，前提是当前情况持续不变。OpenAI 此前开始测试在 ChatGPT 中投放广告以支持免费访问，并逐步加入广告标识和用户控制功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/testing-ads-in-chatgpt/">Testing ads in ChatGPT - OpenAI</a></li>
<li><a href="https://corporatefinanceinstitute.com/resources/accounting/revenue-run-rate/">Revenue Run Rate - Definition, Calculation, Examples</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT Ads`, `#Advertising`, `#AI Business Model`, `#Revenue`

---