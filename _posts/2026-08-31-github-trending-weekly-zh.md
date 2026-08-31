---
layout: default
title: "GitHub 热门项目周报: 2026-W36"
date: 2026-08-31
lang: zh
category: github-weekly
period: 2026-W36
---

> GitHub 热门项目周报（2026-W36）：统计窗口约为最近 168 小时，自 2026-08-24 起。

本期收录 18 个项目。主要语言分布：Python(6)、TypeScript(3)、Rust(3)、JavaScript(2)、Shell(1)、CSS(1)、C++(1)。每个项目均包含中文解释、适用场景和基于仓库元数据推断的运行原理。

---

## 快速目录

1. [freestylefly/awesome-gpt-image-2](#item-1) ⭐ 25903 · JavaScript
2. [anthropics/claude-plugins-community](#item-2) ⭐ 2940 · Python
3. [omacom/omarchy](#item-3) ⭐ 35685 · Shell
4. [tt-a1i/archify](#item-4) ⭐ 35777 · JavaScript
5. [apache/maka](#item-5) ⭐ 4242 · TypeScript
6. [AprilNEA/OpenLogi](#item-6) ⭐ 17963 · Rust
7. [MadsLorentzen/ai-job-search](#item-7) ⭐ 38660 · Python
8. [tashfeenahmed/freellmapi](#item-8) ⭐ 22993 · TypeScript
9. [openai/codex](#item-9) ⭐ 120210 · Rust
10. [anthropics/claude-plugins-official](#item-10) ⭐ 35644 · Python
11. [rohitg00/ai-engineering-from-scratch](#item-11) ⭐ 51378 · Python
12. [cursor/plugins](#item-12) ⭐ 6299 · TypeScript
13. [tinyhumansai/openhuman](#item-13) ⭐ 39059 · Rust
14. [ConardLi/garden-skills](#item-14) ⭐ 11817 · CSS
15. [google/googletest](#item-15) ⭐ 39394 · C++
16. [Alishahryar1/free-claude-code](#item-16) ⭐ 52023 · Python
17. [VoltAgent/awesome-agent-skills](#item-17) ⭐ 33416
18. [K-Dense-AI/scientific-agent-skills](#item-18) ⭐ 39773 · Python

---

<a id="item-1"></a>
## 1. [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

**它是什么**：这是一个面向 GPT-Image2 的工业级提示词（Prompt）引擎和模板库，基于 530+ 个实际案例逆向工程，提炼出 20+ 套可用模板和可复用的 Skills。

**解决什么问题**：它解决了 AI 图像生成中提示词编写依赖经验、效率低且难以复用的问题，尤其适合需要高质量、批量化或自动化图像生成的开发者和设计师场景。

**大致运行原理**：根据仓库描述和 topics，它通过收集大量案例并逆向分析提示词结构，整理成标准化的模板库，同时将经验沉淀为可调用的 'Skills'。语言为 JavaScript，可能围绕这些模板提供脚本或集成到 agents 与工作流自动化中，但具体机制未在元数据中详细说明，仅基于描述推测。

**为什么值得关注**：该项目拥有 25k+ stars 和 2.5k forks，社区关注度极高，且描述为'持续更新中'，说明活跃度和实用性受到认可。适合关注 AI 图像生成、提示词工程、以及自动化工作流的开发者或团队跟进学习。

**元信息**：JavaScript · ⭐ 25903 · Forks 2547

**Topics**：agents、ai-image-generation、chatgpt、dsh-plugin、gpt-image-2、image-prompts、prompt-as-code、prompt-engineering、skills、workflow-automation

**项目主页**：https://gpt-image2.canghe.ai

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-2"></a>
## 2. [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community)

**它是什么**：这是 Anthropic 官方维护的 Claude Cowork 和 Claude Code 社区插件市场仓库，作为一个只读镜像收录和展示社区插件。

**解决什么问题**：它解决用户难以发现和分发 Claude 相关插件的问题，为插件开发者和使用者提供一个集中入口和目录。应用场景包括寻找现成扩展、了解生态或提交自己的插件。

**大致运行原理**：根据仓库描述，它是一个只读镜像，插件提交实际发生在外部页面 clau.de/plugin-directory-submission，再由官方同步到这里。语言为 Python，推测仓库内可能包含用于生成或校验插件目录/元数据的脚本，但具体机制仅基于元数据推测，尚不确定。

**为什么值得关注**：该仓库已有 2940 星，说明 Claude 插件生态关注度很高。对 Claude Code/Cowork 的用户、插件开发者以及关注 Anthropic 生态的人都值得关注，因为它反映了官方认可的插件集散渠道。不过没有明确的时间信息，无法判断本周具体动态。

**元信息**：Python · ⭐ 2940 · Forks 237

**Topics**：未标注

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-3"></a>
## 3. [omacom/omarchy](https://github.com/omacom/omarchy)

**它是什么**：这是一个名为 Omarchy 的 Linux 项目，旨在提供美观、现代且“有主见”的 Linux 体验。

**解决什么问题**：它解决 Linux 用户在系统配置、外观定制和软件选择上的复杂性，通过预设的“有主见”配置提供开箱即用的现代桌面环境，降低定制门槛。

**大致运行原理**：从仓库描述和语言（Shell）推测，它可能通过 Shell 脚本实现自动化安装和配置，例如安装桌面环境、主题、应用及系统设置。由于仅基于元数据，具体技术机制可能是脚本驱动的定制化工具或可执行脚本集。

**为什么值得关注**：鉴于其高达 35685 颗星和 3680 个 fork，该项目正获得大量社区关注，可能是一个快速流行的 Linux 配置方案。适合追求美观与高效定制的 Linux 用户、开发者或爱好者关注。

**元信息**：Shell · ⭐ 35685 · Forks 3680

**Topics**：未标注

**项目主页**：https://omarchy.org

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-4"></a>
## 4. [tt-a1i/archify](https://github.com/tt-a1i/archify)

**它是什么**：这是一个 GitHub 热门项目。仓库描述为：Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.

**解决什么问题**：从仓库元数据看，它本周获得了较高关注，可能代表某个开发者工具、框架、库或应用方向正在升温。

**大致运行原理**：主要实现语言为 JavaScript，主题标签包括：agent-skills、architecture-as-code、architecture-diagram、claude-skill、code-visualization、codex、coding-agents、data-flow-diagram、deepseek-harness、developer-tools、diagram-as-code、diagrams、diagrams-as-code、dsh-plugin、mermaid-alternative、opencode、sequence-diagram、software-architecture、system-design、text-to-diagram。更准确的运行机制需要结合 README 和源码进一步分析。

**为什么值得关注**：建议关注其 README、示例、issue 和 release，判断是否适合纳入自己的工具链或技术观察列表。

**元信息**：JavaScript · ⭐ 35777 · Forks 2299

**Topics**：agent-skills、architecture-as-code、architecture-diagram、claude-skill、code-visualization、codex、coding-agents、data-flow-diagram、deepseek-harness、developer-tools、diagram-as-code、diagrams、diagrams-as-code、dsh-plugin、mermaid-alternative、opencode、sequence-diagram、software-architecture、system-design、text-to-diagram

**项目主页**：https://tt-a1i.github.io/archify/

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-5"></a>
## 5. [apache/maka](https://github.com/apache/maka)

**它是什么**：Apache Maka 是一个本地优先的 AI 代理工作空间，以追加日志方式记录代理运行时的所有事件。

**解决什么问题**：它解决 AI 代理运行过程中的可观测性与审计问题，帮助开发者调试和追踪模型消息、工具调用及权限决策，同时通过本地优先保护数据隐私。

**大致运行原理**：基于 TypeScript 构建，可能采用事件溯源机制将所有交互（如模型消息、工具结果、终止事件）持久化为追加式日志，并提供 CLI 和桌面（Electron）界面。具体实时同步和权限处理机制可能需从代码进一步确认。

**为什么值得关注**：作为 Apache 孵化项目，它代表了本地优先 AI 代理运行时的一种标准化探索，适合关注 AI 代理可靠性、可审计性和隐私控制的开发者与研究者关注。

**元信息**：TypeScript · ⭐ 4242 · Forks 392

**Topics**：agent-runtime、ai、ai-agent、apache、cli、desktop、electron、event-sourcing、incubator、llm、local-first、maka、tool-use、typescript

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-6"></a>
## 6. [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi)

**它是什么**：OpenLogi 是一款用 Rust 编写的、本地优先的罗技 Logitech Options+ 替代工具，通过 HID++ 协议控制罗技鼠标。

**解决什么问题**：它解决了罗技官方软件需要账户、可能含有遥测、以及用户希望本地控制鼠标按键/DPI/智能切换等需求，特别适合注重隐私或想摆脱官方工具的用户。

**大致运行原理**：根据元数据推测，它通过 Rust 实现 HID++ 协议通信，完成按键重映射、DPI 调节和 SmartShift 功能；可能使用 GPUI 构建界面，所有数据本地处理，无云端依赖。具体实现细节需从源码进一步确认。

**为什么值得关注**：该项目在 GitHub 上已获得约 1.8 万 Star，说明它正成为社区热点的本地优先输入设备工具。适合罗技鼠标用户、追求隐私的开发者，以及关注 Rust 桌面应用生态的人群关注。

**元信息**：Rust · ⭐ 17963 · Forks 524

**Topics**：dpi、gpui、hid、hidpp、local-first、logitech、logitech-mouse、logitech-options、mouse-remapping、mx-master、privacy、rust、smartshift

**项目主页**：https://openlogi.org

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-7"></a>
## 7. [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)

**它是什么**：一个基于 Claude Code 的 AI 求职应用框架，运行在本地机器上，用于自动化处理求职流程。

**解决什么问题**：解决求职过程中大量重复且耗时的工作，如筛选职位、定制简历、写求职信和面试准备，让求职者能更高效地申请工作并掌控整个过程。

**大致运行原理**：基于仓库描述和 topics 推测：它利用 Claude Code（AI 代理）来解析职位描述，并根据职位要求生成或调整简历（支持 LaTeX 格式）和求职信，同时提供面试准备功能。整个框架是自托管的，用户可以 fork 后自定义逻辑，使用 Python 作为主要语言。

**为什么值得关注**：该项目拥有极高的关注度（38.6k stars），说明 AI 辅助求职是当前热门需求。适合求职者、开发者以及关注 AI 代理应用的人群，可能代表了未来自动化求职工具的方向。

**元信息**：Python · ⭐ 38660 · Forks 13119

**Topics**：ai、ai-agents、career、claude-code、cover-letter、cv、interview-preparation、job-application、job-hunting、job-search、latex、resume

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-8"></a>
## 8. [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi)

**它是什么**：freellmapi 是一个聚合 34 个免费 LLM 提供商、635 个免费模型端点的统一 API 网关，对外提供单个 /v1 兼容端点。

**解决什么问题**：它解决了开发者在使用多个免费 LLM 服务时需要分别对接不同提供商、管理不同密钥和接口的麻烦，同时提供智能路由与自动故障转移，简化了免费模型的调用体验。

**大致运行原理**：基于元数据推测，该项目用 TypeScript 实现了一个代理服务，将请求统一转发到多个免费 LLM 提供商，并支持附加自定义 OpenAI 兼容端点；它可能通过智能路由选择可用模型，在失败时自动切换，并加密存储提供商密钥以保证安全。

**为什么值得关注**：该项目拥有 2.3 万星标，说明其免费聚合方案广受关注；适合需要低成本或零成本进行 AI 实验的个人开发者，尤其是希望快速对比和调用多个免费模型的人群。

**元信息**：TypeScript · ⭐ 22993 · Forks 3167

**Topics**：未标注

**项目主页**：https://freellmapi.co

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-9"></a>
## 9. [openai/codex](https://github.com/openai/codex)

**它是什么**：这是一个由 OpenAI 开发的轻量级编码代理，以命令行工具形式运行在终端中。

**解决什么问题**：它解决开发者在使用终端时希望获得自动化编程辅助的需求，可能用于代码生成、修改或执行常见开发任务，从而提升开发效率。

**大致运行原理**：该项目使用 Rust 语言编写，即采用编译型、高性能语言构建命令行应用。根据仓库描述，它运行在终端中，推测其可能通过交互式输入，结合 OpenAI 的后端模型（如 API）来理解和响应编码请求，但具体实现细节需查看源码确认。

**为什么值得关注**：该项目因来自 OpenAI 并拥有超过 12 万 Star 而备受关注，对于关注 AI 编程助手和终端效率工具的开发者值得关注。它可以作为了解 OpenAI 在轻量级编码代理方向设计思路的参考。

**元信息**：Rust · ⭐ 120210 · Forks 18364

**Topics**：未标注

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-10"></a>
## 10. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**它是什么**：Anthropic 官方维护的高质量 Claude Code 插件目录，集中展示和管理可用于 Claude Code 的插件资源。

**解决什么问题**：解决 Claude Code 用户发现、安装和管理高质量插件难的问题，提供一个官方认证的集中入口，避免用户在零散来源中寻找不可靠的插件。

**大致运行原理**：基于仓库描述和话题，这是一个以 Python 编写的元数据仓库，可能通过静态文件或脚本维护插件清单（例如以 JSON/目录形式），并结合 MCP（Model Context Protocol）和 skills 体系来定义插件能力。具体运行机制不明确，推测是通过版本管理、目录结构和文档站点（见 homepage）向用户提供插件索引和安装指引。

**为什么值得关注**：该仓库获得 35k+ stars，说明社区关注度极高；本周关注者可能是 Claude Code 用户、插件开发者以及希望了解 Anthropic 官方插件生态的人，可从中获取高质量插件并跟踪官方推荐趋势。

**元信息**：Python · ⭐ 35644 · Forks 3975

**Topics**：claude-code、mcp、skills

**项目主页**：https://code.claude.com/docs/en/plugins

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-11"></a>
## 11. [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)

**它是什么**：一个从零开始学习 AI 工程的开源课程/教程仓库，涵盖 LLM、智能体（agents）、MCP 等主题，主打“学习、构建、交付”的实践路线。

**解决什么问题**：它面向希望系统掌握 AI 工程（而非仅使用现成 API）的开发者，解决从理论到实际构建、部署 AI 应用之间缺乏完整路径的问题。

**大致运行原理**：基于元数据推测：仓库使用 Python 为主要语言，同时涉及 TypeScript 和 Rust，可能通过分步教程、代码示例和项目实战来演示从底层实现到系统集成的过程；主题包含 transformers、deep-learning、computer-vision、reinforcement-learning 等，表明内容覆盖多个 AI 子领域，并强调“from-scratch”的动手实现。

**为什么值得关注**：该项目拥有超过 51k star，说明其内容广受认可；对于想深入 AI 工程、学习 LLM 和智能体开发的开发者，它提供了一个高热度且实战导向的资源，适合本周作为学习或参考的起点。

**元信息**：Python · ⭐ 51378 · Forks 8897

**Topics**：agents、ai、ai-agents、ai-engineering、computer-vision、course、deep-learning、from-scratch、generative-ai、llm、machine-learning、mcp、nlp、python、reinforcement-learning、rust、swarm-intelligence、transformers、tutorial、typescript

**项目主页**：https://aiengineeringfromscratch.com

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-12"></a>
## 12. [cursor/plugins](https://github.com/cursor/plugins)

**它是什么**：Cursor 编辑器的官方插件规范与官方插件集合仓库，使用 TypeScript 编写。

**解决什么问题**：它解决 Cursor 编辑器生态中插件开发标准缺失的问题，为开发者提供统一的插件规范与官方示例，帮助扩展编辑器功能。

**大致运行原理**：基于元数据推测，该仓库定义插件接口规范（specification），并通过 TypeScript 实现官方插件，可能涉及加载机制、API 定义和事件系统。具体运行机制需查看源码确认，因为元数据未提供详细技术说明。

**为什么值得关注**：Cursor 作为 AI 编辑器广受关注，拥有 6.3k stars，该仓库是扩展 Cursor 能力的关键入口。插件开发者、希望定制编辑器的用户以及对 AI 编辑器生态感兴趣的人应关注。

**元信息**：TypeScript · ⭐ 6299 · Forks 509

**Topics**：未标注

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-13"></a>
## 13. [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)

**它是什么**：一个用 Rust 编写的个人 AI 超级智能系统，旨在成为用户的‘大脑’，管理本地优先的生活记忆，并编排多智能体与工作流。

**解决什么问题**：解决个人 AI 助手缺乏长期、私有记忆，难以协调多个智能体完成复杂任务，以及无法进行深度信息研究等问题；同时强调数据本地化以保护隐私。

**大致运行原理**：基于 Rust 构建，推测通过本地存储与向量检索维护个人记忆；使用协程或任务调度机制编排 agent 舰队与工作流；深度研究功能可能对接外部搜索、知识库或模型推理。具体机制需根据源码确认。

**为什么值得关注**：获得近 3.9 万星标，说明社区关注度极高，适合 AI 开发者、隐私敏感用户及个人知识管理工具爱好者关注；其本地优先 + 多代理编排的架构可能代表个人 AI 的一种发展趋势。

**元信息**：Rust · ⭐ 39059 · Forks 3837

**Topics**：未标注

**项目主页**：https://tinyhumans.ai/openhuman

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-14"></a>
## 14. [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills)

**它是什么**：ConardLi 维护的开源 AI Skills 集合，用于为 AI 代理（如 Claude）提供网页设计、知识检索、图像生成等预制能力。

**解决什么问题**：它解决 AI 代理在特定任务上能力不足或需要重复配置的问题，提供可复用的技能模板，降低集成复杂前端、RAG 检索和图像生成的门槛。

**大致运行原理**：基于元数据推测，项目以“skills”机制组织资源，可能包含提示词、工作流和样式等；通过适配 Claude/agent 框架，结合 RAG （检索增强生成）和 gpt-image-2 实现知识查询与图像生成，语言统计为 CSS 可能表明其中包含大量网页设计相关样式或资产。具体运行机制需查看仓库说明确认。

**为什么值得关注**：该项目星标过万，是 AI 代理技能生态中的热门资源；适合希望增强 Claude 等代理能力、或关注 AI 与前端设计/知识管理结合的开发者。

**元信息**：CSS · ⭐ 11817 · Forks 1456

**Topics**：agent、claude、gpt-image-2、rag、skills、web-design

**项目主页**：https://github.com/ConardLi/garden-skills

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-15"></a>
## 15. [google/googletest](https://github.com/google/googletest)

**它是什么**：GoogleTest 是 Google 开源的 C++ 测试与模拟框架。

**解决什么问题**：它解决 C++ 单元测试和 mocking 的需求，为开发者提供编写、组织和运行测试的标准化工具。

**大致运行原理**：基于元数据推测：它是 C++ 编写的库，提供测试断言、测试固件和测试发现机制，并与构建系统集成。仓库描述表明它同时支持测试和 mocking，即可以通过框架生成模拟对象来验证交互。

**为什么值得关注**：它是 C++ 领域最主流的测试框架之一，拥有广泛使用和活跃维护，适合 C++ 开发者、测试工程师及采用 TDD 实践的团队关注。

**元信息**：C++ · ⭐ 39394 · Forks 10883

**Topics**：未标注

**项目主页**：https://google.github.io/googletest/

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-16"></a>
## 16. [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)

**它是什么**：这是一个用 Python 编写的开源项目，提供从终端、应用、IDE 或手机免费使用 Claude Code、Codex、Pi、OpenCode 等多种 AI 模型的统一入口，支持语音交互，并声明拥有 13 亿以上的免费令牌。

**解决什么问题**：它解决 AI 编程助手或大模型 API 使用成本高、访问受限的问题，让用户通过多种设备或界面免费调用主流 AI 模型，同时强调符合服务条款（ToS friendly）。

**大致运行原理**：根据元数据推测，该项目可能通过封装或整合多个免费 AI 服务的 API，提供一个类似 OpenClaw 的命令行或图形界面，从而统一调用不同模型。语言为 Python，可能利用异步请求和 WebSocket 等技术实现实时交互，并支持语音输入输出，但具体机制需阅读源码确认。

**为什么值得关注**：该项目已获得超过 5.2 万星标和 8 千余次 fork，说明社区关注度极高，可能成为免费访问多种 AI 模型的热门工具。对于开发者、AI 爱好者以及希望降低 AI 使用成本或探索多模型工作流的人群，值得关注其功能和更新。

**元信息**：Python · ⭐ 52023 · Forks 8378

**Topics**：未标注

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-17"></a>
## 17. [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)

**它是什么**：这是一个精选的AI代理技能（agent skills）合集，收录了1000多个来自官方开发团队和社区的技能，并声明兼容Claude Code、Codex、Gemini CLI、Cursor等主流AI编程工具，属于awesome-list类型的资源仓库。

**解决什么问题**：它解决了AI代理在特定任务中缺乏可复用技能的问题，避免用户从零开始编写或寻找分散的技能，使不同工具的用户能共享经过筛选的技能，提升代理的实际应用效果。

**大致运行原理**：基于元数据推测，该仓库本身可能不包含完整实现，而是以列表或索引形式组织各技能的链接与说明。这些技能可能以特定格式（如SKILL.md或插件）定义，供各AI代理通过提示、配置或插件机制加载；兼容多个工具可能意味着存在统一技能格式或适配层，但具体机制需查看仓库内容确认。

**为什么值得关注**：该项目目前已获得超过3.3万star，反映出AI代理技能生态受到广泛关注，适合使用Claude Code、Codex、Cursor等工具的开发者、AI应用工程师和关注Agent生态的研究者关注。它可能是发现最新技能和了解技能规范的重要入口，若您正构建或使用AI代理，值得留意其近期更新和社区贡献。

**元信息**：未标注语言 · ⭐ 33416 · Forks 3535

**Topics**：agent-skills、ai-agents、awesome、awesome-list、claude-code、claude-code-skills、claude-skills、codex-skills、cursor-skills、gemini-skills、opencode-skills、skills

**项目主页**：https://officialskills.sh/

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-18"></a>
## 18. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

**它是什么**：一个开源的科学任务技能库，可让任意 AI 代理获得科学家级别的数据处理与分析能力，支持多种主流 AI 编程工具。

**解决什么问题**：解决通用 AI 代理缺乏专业科学知识、无法可靠执行生物/化学/医学研究任务的问题，为科研人员提供开箱即用的验证过技能与跨库检索能力，覆盖药物发现、基因组学、蛋白质组学等场景。

**大致运行原理**：基于 Python 实现，遵循开放的 Agent Skills 标准，将科学工作流封装为可插拔技能模块，并通过 100+ 科学数据库接口提供数据访问与计算支持。机器人可调用这些技能完成数据查询、可视化和领域分析，但具体执行机制需参照代码库进一步确认（如是否依赖外部 API 或本地模型）。

**为什么值得关注**：该项目已获 39.7k star，被全球 19 万+科学家使用，是当前最活跃的 AI 科学工具库之一，值得需要将 AI 应用于科研的开发者、生物信息学家和药物研发人员关注。

**元信息**：Python · ⭐ 39773 · Forks 3701

**Topics**：agent-skills、ai-scientist、bioinformatics、chemoinformatics、claude、claude-skills、claudecode、clinical-research、computational-biology、data-analysis、drug-discovery、genomics、materials-science、metabolomics、proteomics、scientific-computing、scientific-visualization

**项目主页**：https://k-dense.ai

**来源**：GitHubTrendingRSS weekly feed

---
