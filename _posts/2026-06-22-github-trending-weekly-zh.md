---
layout: default
title: "GitHub 热门项目周报: 2026-W26"
date: 2026-06-22
lang: zh
category: github-weekly
period: 2026-W26
---

> GitHub 热门项目周报（2026-W26）：统计窗口约为最近 168 小时，自 2026-06-15 起。

本期收录 19 个项目。主要语言分布：Python(6)、TypeScript(6)、Rust(3)、C(1)、JavaScript(1)、Shell(1)、Ruby(1)。每个项目均包含中文解释、适用场景和基于仓库元数据推断的运行原理。

---

## 快速目录

1. [DeusData/codebase-memory-mcp](#item-1) ⭐ 10663 · C
2. [chopratejas/headroom](#item-2) ⭐ 45177 · Python
3. [Panniantong/Agent-Reach](#item-3) ⭐ 37150 · Python
4. [iptv-org/iptv](#item-4) ⭐ 127225 · TypeScript
5. [n0-computer/iroh](#item-5) ⭐ 10474 · Rust
6. [google-research/timesfm](#item-6) ⭐ 24960 · Python
7. [NVIDIA/SkillSpector](#item-7) ⭐ 9132 · Python
8. [asgeirtj/system_prompts_leaks](#item-8) ⭐ 44649 · JavaScript
9. [calesthio/OpenMontage](#item-9) ⭐ 9517 · Python
10. [withastro/flue](#item-10) ⭐ 6329 · TypeScript
11. [addyosmani/agent-skills](#item-11) ⭐ 64942 · Shell
12. [Kong/insomnia](#item-12) ⭐ 39526 · TypeScript
13. [tursodatabase/turso](#item-13) ⭐ 20943 · Rust
14. [makeplane/plane](#item-14) ⭐ 52431 · TypeScript
15. [LMCache/LMCache](#item-15) ⭐ 9565 · Python
16. [meshery/meshery](#item-16) ⭐ 11232 · TypeScript
17. [chatwoot/chatwoot](#item-17) ⭐ 33163 · Ruby
18. [swc-project/swc](#item-18) ⭐ 34116 · Rust
19. [freeCodeCamp/freeCodeCamp](#item-19) ⭐ 450117 · TypeScript

---

<a id="item-1"></a>
## 1. [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

**它是什么**：一个高性能的代码智能 MCP 服务器，能够将代码库索引为持久化的知识图谱。

**解决什么问题**：解决大型代码库的上下文分析难题，通过亚毫秒级查询和极低 token 消耗，提升 AI 编码工具的效率和准确性。

**大致运行原理**：基于 C 语言实现，利用 tree-sitter 进行 AST 解析（支持 158 种语言），提取代码结构并存储为 Cypher 可查询的知识图谱，最终以 SQLite 持久化，实现毫秒级索引和查询。

**为什么值得关注**：本周获得超 10k 星标，且被 Aider、Claude Code、Cursor 等主流编码工具集成，适合需要高效代码理解和上下文管理的开发者关注。

**元信息**：C · ⭐ 10663 · Forks 804

**Topics**：aider、ast、claude-code、code-analysis、code-intelligence、codex、cursor、cypher、developer-tools、gemini-cli、graph-visualization、kilocode、knowledge-graph、mcp、mcp-server、model-context-protocol、opencode、sqlite、tree-sitter、windsurf

**项目主页**：https://deusdata.github.io/codebase-memory-mcp/

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-2"></a>
## 2. [chopratejas/headroom](https://github.com/chopratejas/headroom)

**它是什么**：Headroom 是一个开源工具，用于在将工具输出、日志、文件和 RAG 片段发送给大型语言模型（LLM）之前进行压缩，可减少 60-95% 的 token 消耗，同时保持答案质量。

**解决什么问题**：它解决了 LLM 调用中 token 成本高昂和上下文窗口限制的问题，特别适用于需要处理大量上下文（如 RAG 管道、代理日志、代码库扫描）的场景，通过压缩降低延迟和费用。

**大致运行原理**：基于元数据推测，Headroom 可能使用智能文本压缩算法（如摘要、关键信息提取或结构化压缩），并可作为 Python 库、代理或 MCP 服务器集成，在数据输入 LLM 前自动压缩。它支持 TypeScript 和 Python，可能通过模式识别或自定义规则优化压缩率。

**为什么值得关注**：本周关注它是因为该项目获得了 45k+ star 和 3k+ fork，表明社区高度认可其在 token 优化领域的创新价值；适合所有使用 LLM API 的开发者、RAG 系统构建者以及关注成本控制的研究人员。

**元信息**：Python · ⭐ 45177 · Forks 3146

**Topics**：agent、ai、anthropic、claude-code、compression、context-engineering、context-window、cursor、fastapi、langchain、llm、mcp、openai、prompt-engineering、proxy、python、rag、token-optimization、tokens、typescript

**项目主页**：https://headroom-docs.vercel.app/docs

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-3"></a>
## 3. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

**它是什么**：一个基于Python的命令行工具，为AI代理提供访问和搜索多个互联网平台（如Twitter、Reddit、YouTube等）的能力，无需支付API费用。

**解决什么问题**：解决AI代理需要实时访问互联网数据但受限于API费用或接口复杂性的问题，服务于需要集成多平台信息抓取的AI应用场景。

**大致运行原理**：根据元数据推测，它可能通过模拟浏览器请求或利用平台的非官方接口来抓取数据，提供统一的CLI接口供AI代理调用。支持MCP（可能指Model Context Protocol）等协议与LLM工具集成。

**为什么值得关注**：本周高星数（37150）表明社区关注度极高，适合AI开发者和希望低成本为AI代理添加网络搜索能力的人关注。

**元信息**：Python · ⭐ 37150 · Forks 2959

**Topics**：agent-infrastructure、ai-agent、ai-search、automation、bilibili、claude-code、cli、cursor、free-api、llm-tools、mcp、python、reddit-scraper、twitter-scraper、web-scraper、xiaohongshu、youtube-transcript

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-4"></a>
## 4. [iptv-org/iptv](https://github.com/iptv-org/iptv)

**它是什么**：一个收集全球公开可用的IPTV频道列表的开源项目。

**解决什么问题**：帮助用户免费获取全球电视直播频道，聚合来自互联网的公开IPTV流，并提供更新和维护的播放列表。

**大致运行原理**：使用TypeScript开发工具和脚本，自动抓取和整理来自不同来源的IPTV频道的M3U格式播放列表，基于元数据推测可能包括定期更新和验证链接可用性的机制。

**为什么值得关注**：拥有超过12万星标，是GitHub上最受欢迎的IPTV资源，适合电视爱好者、开源社区成员和希望节省电视费用的用户关注。

**元信息**：TypeScript · ⭐ 127225 · Forks 6987

**Topics**：iptv、m3u、playlist、streams、tv

**项目主页**：https://iptv-org.github.io

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-5"></a>
## 5. [n0-computer/iroh](https://github.com/n0-computer/iroh)

**它是什么**：Iroh 是一个基于 Rust 的模块化网络栈，旨在用“键”（keys）代替 IP 地址进行网络通信。

**解决什么问题**：它解决传统 IP 地址易变、不易记忆的问题，特别适用于 P2P 应用、实时通信和需要穿透 NAT/防火墙的场景，提供可靠的多路径连接。

**大致运行原理**：根据仓库描述和标签（如 QUIC、holepunching、p2p），推测其核心是通过 QUIC 协议提供加密传输，利用 NAT 打洞技术（holepunching）实现端到端直连，并支持多路径复用以增强稳定性；模块化设计使开发者可灵活组合网络组件。

**为什么值得关注**：本周关注该项目因其在 Rust 生态中提供创新的 P2P 网络解决方案，对构建去中心化应用、实时协作工具或需要稳定穿透内网的开发者极具吸引力；10474 颗星显示出社区高度认可和活跃度。

**元信息**：Rust · ⭐ 10474 · Forks 476

**Topics**：does-anyone-read-these、holepunching、memes、multipath、p2p、quic、realtime、rust、tags、tagsoftags

**项目主页**：https://iroh.computer

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-6"></a>
## 6. [google-research/timesfm](https://github.com/google-research/timesfm)

**它是什么**：TimesFM 是 Google Research 开发的预训练时间序列基础模型，专用于时间序列预测。

**解决什么问题**：它解决时间序列预测问题，应用场景包括金融、气象、能源等领域，帮助预测未来趋势或数值。

**大致运行原理**：基于元数据推测，该模型可能采用 decoder-only 的 Transformer 架构，在大规模时间序列数据上预训练，学习通用时间序列模式，然后通过微调适应具体预测任务。

**为什么值得关注**：该仓库拥有 24960 颗星，社区关注度极高，意味近期可能有重要更新或论文发布；适合数据科学家、金融分析师、物联网工程师等需要时间序列预测的人群关注。

**元信息**：Python · ⭐ 24960 · Forks 2375

**Topics**：未标注

**项目主页**：https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-7"></a>
## 7. [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)

**它是什么**：一个用于检测AI代理技能中安全漏洞、恶意模式和风险的开源扫描工具。

**解决什么问题**：解决AI代理技能（如插件、工具）可能引入的安全问题，帮助开发者和安全团队在部署前识别潜在威胁。

**大致运行原理**：基于Python实现，可能通过静态代码分析或行为模式匹配来扫描AI技能的定义或代码，识别已知漏洞特征和恶意模式。

**为什么值得关注**：本周获得超过9000颗星，受到AI安全社区高度关注；适合AI应用开发者、安全工程师和任何需要安全部署AI代理的团队关注。

**元信息**：Python · ⭐ 9132 · Forks 717

**Topics**：未标注

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-8"></a>
## 8. [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)

**它是什么**：一个定期更新并公开各大AI模型（如Claude、ChatGPT、Gemini等）系统提示词（system prompts）的开源项目。

**解决什么问题**：帮助研究人员和开发者了解商业AI模型的底层行为设定，用于提示工程、模型对比或合规分析。

**大致运行原理**：基于JavaScript（可能使用爬虫或API）从各个AI产品的公开交互中提取系统提示词，并整理成可浏览的仓库。具体技术细节未明确，但推测是通过分析网络请求或页面内容来获取。

**为什么值得关注**：该项目已有4.6万+星标，更新活跃，且覆盖主流AI模型（Claude、GPT、Gemini等），适合AI从业者、安全研究员和关注模型透明度的用户持续关注。

**元信息**：JavaScript · ⭐ 44649 · Forks 7362

**Topics**：ai、ai-agents、anthropic、awesome、chatbot、chatgpt、claude、claude-code、codex、deep-learning、education、gemini、generative-ai、google、llm、machine-learning、nlp、open-source、openai、prompt-engineering

**项目主页**：https://asgeirtj.github.io/system_prompts_leaks/

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-9"></a>
## 9. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

**它是什么**：OpenMontage 是一个开源的、基于 AI 智能体的视频制作系统，号称拥有 12 条管线、52 个工具和 500 多种智能体技能。

**解决什么问题**：它解决了从文本或图像生成高质量视频的复杂性问题，用户无需专业视频编辑技能，只需通过与 AI 编码助手（如 Claude、Copilot）交互即可完成视频制作。适用于内容创作者、开发者等需要快速创建视频的场景。

**大致运行原理**：基于元数据推测，项目使用 Python 实现，集成多种 AI 模型和工具（如 Flux、Stable Diffusion 进行图像生成，ElevenLabs 进行语音合成，FFmpeg 和 Remotion 进行视频渲染），通过智能体编排多个流水线（pipeline）和工具链，实现从脚本、图像、音频到最终视频的全自动生成。

**为什么值得关注**：本周值得关注是因为它拥有近万颗星和超过 1300 Fork，是首个开源且完全代理驱动的视频生产系统，适合对 AI 视频生成、自动化内容创作感兴趣的开发者或创作者关注。

**元信息**：Python · ⭐ 9517 · Forks 1353

**Topics**：agent、agentic-ai、ai、claude、copilot、cursor、elevenlabs、ffmpeg、flux、image-generation、open-source、openai、python、remotion、stable-diffusion、text-to-speech、text-to-video、video-generation、video-production

**项目主页**：https://github.com/calesthio/OpenMontage

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-10"></a>
## 10. [withastro/flue](https://github.com/withastro/flue)

**它是什么**：Flue是一个基于TypeScript的沙盒代理框架，用于构建隔离、可执行的代理环境。

**解决什么问题**：它解决在安全隔离的环境中运行不受信任的代码或代理的问题，防止恶意行为影响宿主系统，适用于需要执行AI代理、自动化脚本或第三方插件的场景。

**大致运行原理**：根据元数据推测，它利用TypeScript的类型安全性和沙盒机制（如VM隔离或浏览器iframe）来创建独立的代理执行环境，可能通过定义严格的接口和权限控制来管理代理行为。

**为什么值得关注**：该项目因与Astro团队关联且拥有超过6300星而备受关注，适合开发安全代理、AI应用或需要隔离执行环境的开发者关注。

**元信息**：TypeScript · ⭐ 6329 · Forks 355

**Topics**：未标注

**项目主页**：https://www.flueframework.com

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-11"></a>
## 11. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

**它是什么**：一个为AI编码代理（如Claude Code、Cursor）提供生产级工程技能的Shell脚本集合。

**解决什么问题**：解决AI编码代理在自动生成代码时缺乏工程实践（如测试、重构、安全）的问题，帮助它们产出更可靠、可维护的代码。

**大致运行原理**：基于元数据推测：通过Shell脚本和配置文件定义技能（如代码审查、性能分析），利用Agent Skills接口注入到AI代理的开发环境中，使其在编码时自动调用这些技能。

**为什么值得关注**：本周获得64.9k星，可能是AI编码代理领域的热门实践集合，适合使用Claude Code、Cursor等工具的开发者或对AI工程化感兴趣的团队关注。

**元信息**：Shell · ⭐ 64942 · Forks 7011

**Topics**：agent-skills、antigravity、antigravity-ide、claude-code、cursor、skills

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-12"></a>
## 12. [Kong/insomnia](https://github.com/Kong/insomnia)

**它是什么**：Insomnia 是一个开源的跨平台 API 客户端，支持 GraphQL、REST、WebSockets、SSE 和 gRPC 等多种协议，并提供云、本地和 Git 存储选项。

**解决什么问题**：它解决了开发者在调试、测试和设计 API 时需要一个统一工具的需求，特别是需要同时支持多种现代 API 协议（如 GraphQL 和 gRPC）的场景。

**大致运行原理**：基于 TypeScript 开发，使用 Electron 框架实现跨平台桌面应用；通过插件化架构支持多种协议和存储后端，用户可本地或通过云同步请求集合，并集成 Git 进行版本控制。

**为什么值得关注**：该项目拥有近 4 万星标，持续活跃开发，是 API 开发工具中的热门选择；适合全栈开发者、API 设计者及需要高效管理多种 API 请求的团队关注。

**元信息**：TypeScript · ⭐ 39526 · Forks 2338

**Topics**：api、api-client、api-design、curl、electron-app、graphql、grpc、http-client、rest-api、websockets

**项目主页**：https://insomnia.rest

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-13"></a>
## 13. [tursodatabase/turso](https://github.com/tursodatabase/turso)

**它是什么**：Turso 是一个与 SQLite 兼容的进程内 SQL 数据库，使用 Rust 语言实现。

**解决什么问题**：它旨在提供轻量级、嵌入式的数据库解决方案，兼容 SQLite 但可能针对边缘计算、浏览器环境或需要更高性能的场景进行优化。

**大致运行原理**：基于 Rust 构建，兼容 SQLite 的语法和存储格式；利用 WebAssembly 技术实现跨平台运行，可作为嵌入式数据库直接集成到应用中，无需独立服务器。

**为什么值得关注**：该项目拥有超过 2 万颗星，社区活跃度高，适合需要 SQLite 兼容性但希望探索新型部署方式的开发者，尤其是边缘计算或 WebAssembly 爱好者。

**元信息**：Rust · ⭐ 20943 · Forks 1070

**Topics**：database、embedded-database、sql、sqlite3、webassembly

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-14"></a>
## 14. [makeplane/plane](https://github.com/makeplane/plane)

**它是什么**：一个开源的现代项目管理平台，是 Jira、Linear、Monday 和 ClickUp 的替代品。

**解决什么问题**：解决团队在任务跟踪、冲刺管理、文档协作和问题分类等方面的需求，提供免费、可自托管的项目管理方案。

**大致运行原理**：基于元数据推测：前端使用 TypeScript（React + Vite）构建，后端使用 Python（Django）框架，数据存储依赖 PostgreSQL 和 Redis，支持 Docker 容器化部署。功能涵盖看板、甘特图、问题追踪、冲刺管理等。

**为什么值得关注**：该项目在 GitHub 上拥有超 5 万星标，社区活跃，适合寻求开源、可自托管且功能全面的项目管理工具的团队或个人开发者关注。

**元信息**：TypeScript · ⭐ 52431 · Forks 4658

**Topics**：boards、bug-tracker、django、docker、gantt、issue-tracker、jira、jira-alternative、kanban、linear、postgresql、product-management、project-management、project-planning、python、react、redis、typescipt、vite、work-management

**项目主页**：http://plane.so

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-15"></a>
## 15. [LMCache/LMCache](https://github.com/LMCache/LMCache)

**它是什么**：LMCache 是一个专为大语言模型设计的 KV 缓存层，旨在以最快的速度加速推理过程。

**解决什么问题**：解决大语言模型推理时因重复计算键值对（KV Cache）带来的延迟问题，尤其适用于长序列和批量推理场景。

**大致运行原理**：基于元数据推测，它通过缓存已计算的键值对，避免在后续解码步骤中重复计算，可能利用 CUDA/ROCm 后端进行高效内存管理与传输，并集成 vLLM 等推理框架。

**为什么值得关注**：本周值得关注因为该项目拥有近万颗星标，活跃度高，且覆盖 AMD 与 NVIDIA 硬件，对提升 LLM 推理速度和降低延迟有显著潜力，适合 AI 推理工程师和性能优化开发者。

**元信息**：Python · ⭐ 9565 · Forks 1367

**Topics**：amd、cuda、fast、inference、kv-cache、llm、pytorch、rocm、speed、vllm

**项目主页**：https://lmcache.ai/

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-16"></a>
## 16. [meshery/meshery](https://github.com/meshery/meshery)

**它是什么**：Meshery 是一个云原生管理器，提供可扩展的管理平面，用于操作和可视化 Kubernetes 及云基础设施。

**解决什么问题**：它解决多云和混合环境中基础设施管理复杂性的问题，服务于平台工程师和 DevOps 团队，帮助他们实现 GitOps、基础设施即代码和内部开发者平台。

**大致运行原理**：基于元数据推测：它采用前端 React.js（TypeScript）和后端 Go 语言构建，可能通过 Kubernetes Operator 与控制平面交互，利用 WebAssembly 扩展能力，并提供可视化界面（Kanvas）来管理和观测云原生资源。

**为什么值得关注**：Meshery 是一个活跃的 CNCF 项目，拥有超过 11k 星标，持续支持 GSoC 和 Hacktoberfest，适合关注云原生、平台工程和可视化管理的开发者关注本周动态。

**元信息**：TypeScript · ⭐ 11232 · Forks 3477

**Topics**：cloud-native、cncf、control-plane、docker、gitops、golang、gsoc、hacktoberfest、infrastructure-as-code、internal-developer-platform、kanvas、kubernetes、kubernetes-operator、management-plane、meshery、opa、platform-engineering、reactjs、visualization、webassembly

**项目主页**：https://meshery.io

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-17"></a>
## 17. [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)

**它是什么**：Chatwoot 是一个开源的全渠道客服平台，支持实时聊天、电子邮件支持和社交媒体集成，替代 Intercom、Zendesk 等商业工具。

**解决什么问题**：它解决企业与客户之间多渠道沟通的统一管理问题，适用于需要整合网站聊天、邮件、WhatsApp 等渠道的客户支持场景。

**大致运行原理**：基于元数据推测：项目使用 Ruby on Rails 框架，后端通过 ActionCable 实现实时消息推送；前端采用 Vue.js 构建响应式界面，集成 WebSocket 和 REST API；支持 Docker 部署，并针对 Heroku 优化，同时提供聊天小部件嵌入网站。

**为什么值得关注**：本周关注因为它是 GitHub 上最活跃的开源客服平台之一，拥有超过 3.3 万星标，持续更新且社区活跃；适合需要自托管客服系统、控制数据隐私或避免高昂商业许可费用的团队。

**元信息**：Ruby · ⭐ 33163 · Forks 7820

**Topics**：actioncable、chat-widget、conversation、customer-support、dashboard、design、docker、docker-image、heroku、intercom、javascript、livechat、opensource、rails、ruby、sass、vuejs、whatsapp、zendesk

**项目主页**：https://www.chatwoot.com/help-center

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-18"></a>
## 18. [swc-project/swc](https://github.com/swc-project/swc)

**它是什么**：SWC 是一个基于 Rust 的快速 Web 开发平台，主要用作 JavaScript/TypeScript 的编译器与打包工具。

**解决什么问题**：它解决 JavaScript/TypeScript 编译和打包速度慢的问题，特别是相比 Babel 等 JS 编写的工具，SWC 利用 Rust 实现高性能，适用于大型项目或对构建速度有要求的场景。

**大致运行原理**：基于仓库描述和 topics，SWC 使用 Rust 语言编写，实现 ECMAScript/TypeScript 解析器、编译器等功能。可能通过将源码解析为 AST，然后进行转换与代码生成，并利用 Rust 的并行与内存安全特性加速编译过程。具体机制需查看文档确认。

**为什么值得关注**：SWC 在 Rust 生态中备受关注，star 数高（34k+），适合前端开发者或关注构建工具性能优化的用户。近期可能持续优化兼容性或推出新特性（如 SWC 打包器），值得关注以提升项目构建效率。

**元信息**：Rust · ⭐ 34116 · Forks 1426

**Topics**：babel、compiler、ecmascript、ecmascript-parser、javascript、parser、rust、swc、typescript、typescript-compiler、typescript-parser

**项目主页**：https://swc.rs

**来源**：GitHubTrendingRSS weekly feed

---

<a id="item-19"></a>
## 19. [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)

**它是什么**：免费学习编程和计算机科学的开源平台及其课程体系。

**解决什么问题**：解决编程教育资源付费、封闭的问题，为任何人提供免费的、自定进度的编程课程和认证，尤其为非营利组织和教师提供支持。

**大致运行原理**：基于元数据推测：使用 TypeScript 构建，前端采用 React，可能结合 D3 进行数据可视化，后端使用 Node.js；整个平台包括交互式课程、项目挑战和社区协作，通过 GitHub 开源协作维护代码与课程内容。

**为什么值得关注**：拥有超过 45 万 Star 和 4.5 万 Fork，是 GitHub 上最活跃的教育项目之一；持续更新课程质量，每周有大量贡献者参与，适合想学习编程的初学者、希望贡献开源社区的开发者以及教育工作者关注。

**元信息**：TypeScript · ⭐ 450117 · Forks 45195

**Topics**：careers、certification、community、curriculum、d3、education、freecodecamp、javascript、learn-to-code、math、nodejs、nonprofits、programming、react、teachers

**项目主页**：https://contribute.freecodecamp.org

**来源**：GitHubTrendingRSS weekly feed

---
