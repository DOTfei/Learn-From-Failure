# Learn From Failure（从失败中学习）

[English](README.md) | 简体中文

**一个由真实、可查证来源支撑的企业失败案例知识库 —— 可以配合任何 AI 工具用，也可以完全不用 AI。**

问一句"我的公司有没有当年拖垮某某公司的那些失败模式？"，得到的回答是基于真实发生过的事情，
而不是泛泛而谈的商业鸡汤。

---

## 一分钟看懂

- **有 AI 工具？** 让它指向这个仓库，直接问你公司的情况。看下面的"平台支持"。
- **不想用 AI？** 直接浏览案例：**[dotfei.github.io/Learn-From-Failure](https://dotfei.github.io/Learn-From-Failure/)**
- **只想快速自查？** 用 [CHECKLIST.zh-CN.md](CHECKLIST.zh-CN.md)，不需要 AI。
- **知道一个该收录的案例？** [在这里提交](https://github.com/DOTfei/Learn-From-Failure/issues/new/choose)，不用自己写。

---

## 这里面有什么

每个案例都用同样的四段式拆解：

1. **发生了什么** —— 简短说明事实。
2. **根本原因** —— 真正的原因，不只是"倒闭了"这种表面结论。
3. **警示信号** —— 崩溃之前，其实就已经能看出来的迹象。
4. **值得追问的问题** —— 把同样的问题改写成可以套用在**你自己公司**身上的版本。

案例按**失败机制**打标签，不是按行业分类——造假、治理失控、财务管理不当、拒绝转型、产品
市场不匹配、扩张过快、文化/人才问题——因为这些模式大多不局限于某一个行业。完整标签列表见
[`cases/_index.md`](cases/_index.md)。

## 为什么做这个

市面上大多数"创业失败教训"内容都是看一遍就忘的清单体文章。这个项目是设计给**对话式使用**的：
描述你的处境，就能拿到真正在**失败机制**上和你相似的 3-6 个案例，以及当年如果有人问过、
本可以提前发现问题的那些具体问题。

**而且不用你专门开口问。** 就算你只是在聊一个普通的经营决定——裁员省钱、快速扩张、招聘
计划——只要这个决定明显符合某个已知的失败模式，AI 会主动提醒你："先说一句——[某某公司]
当年几乎做了一模一样的事，结果是……"哪怕你根本没打算对照失败案例，也会主动收到这个警告。

## 一次真实分析长什么样

> **你：** 我们是个 12 人的 SaaS 创业公司，刚拿到种子轮，计划两个月内从 12 人扩到 35 人——
> 赶在下个季度续费数据出来之前。投资人想在 deck 里看到"激进增长"。这样做是不是有问题？
>
> **Claude：** 这跟 `scaling_too_fast`（扩张过快）很像——比起 WeWork，更接近
> [Webvan](cases/webvan.md) 和 [Kenny Rogers Roasters](cases/kenny-rogers-roasters.md)。
> 规模小很多，但核心错误一样：**在还没验证一个关键指标（续费率）之前，先把固定成本
> （人头）投进去了**。Webvan 在证明模式能在一个城市跑通之前，先建了 10 亿美元的仓库产能。
>
> 把这两个案例的问题套到你身上：
> 1. 如果下个季度续费数据不理想，35 人的团队你还养得起吗？
> 2. 招聘节奏是现有客户数据支撑的，还是为了让 deck 好看？
> 3. 这 23 个新增岗位里，有多少是可逆的（合同工），有多少是锁死的固定成本？
>
> 这不是说不能招人——而是招聘的**顺序**：先看到信号，再招人。

可以直接拿你自己的情况试试，或者看完整案例内容：[`dist/learn-from-failure-bundle.md`](dist/learn-from-failure-bundle.md)。

## 平台支持

内容本身就是纯 Markdown 文件，没有平台锁定：

| 你用的工具 | 怎么用 |
|---|---|
| **Claude Code** | 当插件安装（`.claude-plugin/plugin.json`），或把 `.claude/skills/learn-from-failure/` 复制到你自己项目里。 |
| **Cursor、Windsurf、OpenAI Codex CLI、Amp、Continue，或任何支持 [AGENTS.md](https://agents.md) 的工具** | 克隆这个仓库，让工具指向它——`AGENTS.md` 有完整指令。 |
| **ChatGPT Custom GPT、Gemini Gem，或任何支持"上传知识文件"的工具** | 上传 [`dist/learn-from-failure-bundle.md`](dist/learn-from-failure-bundle.md)——一个文件，全部内容和来源都在里面。 |
| **直接调 API，或任何没有文件上传功能的聊天工具** | 把同一份打包文件的内容粘贴进对话或 system prompt。 |
| **不用任何 AI 工具** | 浏览 **[dotfei.github.io/Learn-From-Failure](https://dotfei.github.io/Learn-From-Failure/)**——可搜索、可筛选，不需要安装任何东西。 |

以上方式读取的都是 `cases/` 里同一份源文件，没有手动重复维护多份内容，所以不会出现
"网页版"和"AI 版"内容不一致的情况——打包文件和网站数据都由脚本自动生成，CI 会检查是否同步。

## 怎么理解这些案例

- **这是用于自我反思的工具，不是预测引擎。** 很多公司同样有高杠杆、强势创始人、激进扩张
  这些警示信号，最后活得好好的（幸存者偏差是真实存在的）。"匹配"意味着"值得认真调查一下"，
  不是"你的公司一定会失败"。
- **记得核对来源。** 每个案例都有 `## Sources` 区块，打算公开引用某个数字之前先核对一下。
  发现错误？[提交一个报错 issue](https://github.com/DOTfei/Learn-From-Failure/issues/new?template=case-error.yml)。
- **不要把机密信息放进这个仓库。** 用 AI 分析自己公司时，在自己私有的对话里进行——不要把
  内部财务、纠纷、股权结构这类信息提交成案例文件。新案例应该是有真实公开报道支撑的公司。

## 自查清单（不需要 AI）

[CHECKLIST.zh-CN.md](CHECKLIST.zh-CN.md)（[English](CHECKLIST.md)）是把所有案例的"值得
追问的问题"按失败机制整理成的静态清单，适合每季度过一遍，不需要对话。

## 贡献

三种方式，从简单到复杂：

1. **直接告诉我们。** [提交一个案例线索](https://github.com/DOTfei/Learn-From-Failure/issues/new?template=new-case.yml)、[补充一个来源](https://github.com/DOTfei/Learn-From-Failure/issues/new?template=add-source.yml)，或[报告一个错误](https://github.com/DOTfei/Learn-From-Failure/issues/new?template=case-error.yml)——填个表单就行，不用写 PR 或 Markdown。
2. **在 GitHub 网页上直接编辑。** 打开 `cases/` 里任意文件，点 ✏️ 铅笔图标，改完提交——GitHub 会自动帮你开 PR，不需要在本地装任何东西。
3. **自己在本地写一个完整案例。** 格式和必需章节见 [CONTRIBUTING.md](CONTRIBUTING.md)（英文）。

也欢迎贡献马来西亚/中国/其他地区的失败案例——目前案例以欧美大公司为主，地区多样性是接下来
想加强的方向。

## 目录结构

```
AGENTS.md                       — 给 Claude Code 以外的 AI 工具用的通用指令
.claude/skills/                  — Claude Code Skill（逻辑委托给 AGENTS.md）
.cursor/rules/                    — Cursor 规则（同样委托给 AGENTS.md）
cases/
  _index.md                      — 所有案例的标签索引
  _template.md                    — 新增案例用的模板
  <company>.md                    — 每个案例一个文件，附来源链接
  contrasts/                      — "对照案例"：同样的冲击下，应对得当的公司
scripts/                         — 从 cases/ 自动生成打包文件和网站
dist/                            — 给没有文件访问能力的工具用的单文件打包版本
docs/                            — 可搜索的网站（GitHub Pages）
CHECKLIST.md / CHECKLIST.zh-CN.md — 静态自查清单
```

## 语言说明

案例正文只有英文，方便和引用来源的英文报道对照。但这不代表对话也得用英文——用中文
（或任何语言）提问，分析结果会翻译过来。如果你想直接读中文，本文件和
`CHECKLIST.zh-CN.md` 是现成的中文参考资料。

## License

MIT 协议，见 [LICENSE](LICENSE)。案例内容是基于公开报道事实的原创归纳分析，不是任何
单一来源的复制——具体细节请查阅每个案例的来源链接。
