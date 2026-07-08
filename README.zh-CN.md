# Learn From Failure（从失败中学习）

[English](README.md) | 简体中文

一个由真实、可查证来源支撑的企业失败案例知识库 —— **不绑定任何单一 AI 平台**，让你可以问
"我的公司有没有当年拖垮某某公司的那些失败模式？"，得到的分析是基于真实发生过的事情，而不是
泛泛而谈的商业鸡汤。

知识库本身就是纯 Markdown 文件，没有平台锁定：[Claude Code](https://claude.com/claude-code)
有原生 Skill；Cursor、Windsurf、OpenAI Codex CLI、Amp、Continue 等大多数 agentic 编程工具
通过通用的 `AGENTS.md` 规范读取同一份指令；没有文件访问能力的纯对话工具（ChatGPT、Gemini、
直接调 API）可以用打包成单文件的版本。详见下面的"平台支持"。不想用任何 AI 工具？
**直接浏览 [dotfei.github.io/Learn-From-Failure](https://dotfei.github.io/Learn-From-Failure/)**
——可搜索、可按失败机制筛选，不需要安装任何东西。

每个案例都用同样的结构拆解：发生了什么、根本原因、崩溃前就已经存在的警示信号，以及一组
可以套用在任何公司身上的通用问题。带标签的索引（`cases/_index.md`）按**失败机制**分类
（造假、治理失控、财务管理不当、拒绝转型、产品市场不匹配、扩张过快、文化/人才问题），
而不只是按行业分类 —— 因为这些模式大多不局限于某个行业。

## 为什么做这个

市面上大多数"创业失败教训"内容都是清单体文章。这个项目是设计给对话式使用的：描述你的
处境，Claude 会挑出真正在**失败机制**上和你相似的 3-6 个案例，并抛出当年如果有人问过、
本可以提前发现问题的那些具体问题。

## 平台支持

| 你用的工具 | 怎么用这个仓库 |
|---|---|
| **Claude Code** | 通过 `.claude-plugin/plugin.json` 清单当插件安装（在插件市场流程里指向 `https://github.com/DOTfei/Learn-From-Failure`），或者把 `.claude/skills/learn-from-failure/` 文件夹复制/软链接到你自己项目的 `.claude/skills/` 目录下。 |
| **Cursor、Windsurf、OpenAI Codex CLI、Amp、Continue，或任何支持 [AGENTS.md](https://agents.md) 规范的工具** | 克隆这个仓库（或作为参考/submodule 引入），让你的工具指向它 —— 仓库根目录的 `AGENTS.md` 有完整指令。Cursor 用户还有 `.cursor/rules/learn-from-failure.mdc`，内容指向同一份 `AGENTS.md`。 |
| **ChatGPT Custom GPT、Gemini Gem，或任何支持上传"知识文件"但不能访问仓库的工具** | 上传 `dist/learn-from-failure-bundle.md` —— 一份包含指令、索引、清单和所有带来源案例的单文件，由 `scripts/build_bundle.py` 生成。 |
| **直接调 API（OpenAI、Anthropic 等），完全没有工具能力** | 把 `dist/learn-from-failure-bundle.md` 的内容粘贴进（或作为）system prompt / context。纯 Markdown，不需要特殊解析。 |
| **其他没有文件上传功能的聊天工具** | 直接把 `dist/learn-from-failure-bundle.md` 里相关的部分（比如索引 + 3-4 个案例）复制粘贴进对话框。 |
| **不用任何 AI 工具，只想读案例** | 浏览 [dotfei.github.io/Learn-From-Failure](https://dotfei.github.io/Learn-From-Failure/) —— 一个可搜索、可筛选的静态网站（`docs/`，由 `scripts/build_site.py` 生成），不需要安装任何东西也不需要 AI。 |

以上方式读取的都是 `cases/` 里同一份源文件 —— 没有手动重复维护多份内容，所以知识库
不会在不同平台之间出现不一致。`dist/learn-from-failure-bundle.md` 和 `docs/data.json`
都由 CI 校验的脚本自动生成（见"贡献"部分）。

## 使用方式

直接用中文问，Claude 会用中文回答（案例原文是英文写的，方便对照英文信源，但分析对话本身
会翻译成你使用的语言）。比如可以问：

- "我们准备融一大笔钱，还没验证清楚单位经济模型就要激进招人扩张，这是不是在重复 WeWork / Webvan 的错误？"
- "我们董事会基本上都是创始人的朋友，这样有风险吗？"
- "我们为了省钱在裁最有经验（也最贵）的员工，拿 Circuit City 的案例帮我 sanity check 一下。"
- "帮我把 [某公司] 加进案例库，这是我了解到的它失败的原因：……"

### 一次真实分析长什么样

> **你：** 我们是个 12 人的 SaaS 创业公司，刚拿到种子轮，计划两个月内从 12 人扩到 35 人——
> 销售、客服、再加几个工程师——赶在下个季度续费数据出来之前。投资人想在 deck 里看到"激进
> 增长"。这样做是不是有问题？
>
> **Claude：** 这跟 `scaling_too_fast`（扩张过快）这个机制很像，而且比起 WeWork 更接近
> [Webvan](cases/webvan.md) 和 [Kenny Rogers Roasters](cases/kenny-rogers-roasters.md) 的
> 情况——规模小很多，但核心错误一样：**在还没验证一个关键指标（续费率）之前，先把固定成本
> （人头）投进去了**。Webvan 在证明模式能在一个城市跑通之前，先建了 10 亿美元的仓库产能；
> 你现在是在还不知道现有客户会不会续费之前，先把团队扩大三倍。
>
> 把这两个案例的问题套到你身上：
> 1. 如果下个季度的续费数据不理想，35 人的团队你还养得起吗，还是说这个招聘计划只有在续费
>    数据乐观的情况下才成立？
> 2. 招聘节奏是现有客户数据支撑的，还是为了让 deck 看起来"激进增长"好看？Webvan 的扩张
>    节奏是投资人期待推着走的，不是一个城市一个城市验证盈利后才推进的。
> 3. 这 23 个新增岗位里，有多少是可逆的（合同工、按月签），有多少是不管下季度数据如何都
>    锁死的固定成本？
>
> 这不是说不能招人——而是说这两个案例给出的建议是招聘的**顺序**（先看到续费信号再招，而
> 不是反过来），而不是反对增长本身。

Skill 会按失败**机制**而不是单纯按行业来匹配案例，并且会直接抛出案例里那些真正的根因
问题让你自查，而不是只给你讲一遍历史。

## 关于怎么理解这些案例

**这是一个用于自我反思的模式匹配工具，不是预测引擎。** 幸存者偏差是真实存在的：很多公司
同样有高杠杆、强势创始人、激进扩张这些警示信号，最后活得好好的。这里的"匹配"意味着
"这件事值得认真调查一下"，而不是"你的公司一定会失败"。用它来问出更好的问题，而不是
拿它下结论。

**案例内容不保证完全准确。** 每个案例都有 `## Sources` 区块 —— 在你打算把某个具体数字或
说法当作确凿事实之前，请先核对来源，尤其是打算公开引用的场合。如果发现错误，欢迎提 issue
或 PR。

**不要把机密信息放进这个仓库。** 如果你用这个 skill 分析自己的公司，请在自己私有的对话/
工作空间里进行 —— 不要把内部财务数据、纠纷、股权结构这类信息提交成案例文件。贡献到这个
知识库的新案例，应该是有真实公开报道支撑的公司（新闻报道、法院文件、维基百科等）。

## 目录结构

```
AGENTS.md                       — 平台无关的通用指令（Cursor、Windsurf、Codex CLI、Amp 等）
.claude/skills/learn-from-failure/
  SKILL.md                       — Claude Code Skill，逻辑委托给 AGENTS.md
.cursor/rules/
  learn-from-failure.mdc         — Cursor 规则，同样委托给 AGENTS.md
cases/
  _index.md                      — 所有案例的标签索引 + 失败类型分类体系
  _template.md                    — 新增案例用的模板
  <company>.md                    — 每个案例一个文件（英文原文，附来源链接）
  contrasts/                      — "对照案例"：同样的冲击下，应对得当的公司
scripts/
  validate_cases.py              — 检查 frontmatter、必需章节、索引一致性
  build_bundle.py                — 重新生成 dist/learn-from-failure-bundle.md
  build_site.py                  — 重新生成 docs/data.json（GitHub Pages 案例浏览器用）
dist/
  learn-from-failure-bundle.md   — 给没有仓库/文件访问能力的工具用的单文件打包版本
docs/
  index.html, data.json          — 可搜索的静态案例浏览器，通过 GitHub Pages 提供服务
CHECKLIST.md / CHECKLIST.zh-CN.md — 从所有案例的"问题"提炼出的静态自查清单
```

## 不用 Skill 也能自查

如果只是想要一份可以每季度过一遍的静态清单（不需要对话），参考
[CHECKLIST.zh-CN.md](CHECKLIST.zh-CN.md) —— 这是把所有案例的"值得追问的问题"按失败机制
分类整理出来的。

## 贡献

参考 [CONTRIBUTING.md](CONTRIBUTING.md)（英文）。简单说：用 `cases/_template.md` 做模板，
引用真实来源，用现有的失败类型标签打标（没有合适的再新增），更新 `cases/_index.md`，提交
PR 前跑一下 `python3 scripts/validate_cases.py`（CI 也会自动跑）。也欢迎贡献案例的中文
翻译，或者贡献马来西亚/中国/其他地区的失败案例 —— 目前案例以欧美大公司为主，地区和规模
多样性是接下来想加强的方向。

## 语言支持说明

案例正文目前只有英文（方便和引用来源的英文报道对照）。但 Skill 在对话中会**用你提问的
语言回答**并翻译相关内容，不需要等到案例文件本身被翻译完才能用中文提问。本文件和
`CHECKLIST.zh-CN.md` 是预先翻译好的参考资料。

## License

案例内容是基于公开报道事实的原创归纳分析；仓库代码/文档使用 MIT 协议，见
[LICENSE](LICENSE)。这是评论/分析性质的内容，不是任何单一来源的复制 —— 具体细节请查阅
每个案例的来源链接。
