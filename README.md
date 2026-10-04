<a href="https://dotfei.github.io/Learn-From-Failure/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/DOTfei/Learn-From-Failure@main/assets/banner-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.jsdelivr.net/gh/DOTfei/Learn-From-Failure@main/assets/banner-light.svg">
    <img alt="Learn From Failure — a sourced knowledge base of corporate failure case studies, organized by failure mechanism, not industry. Click to browse the site." src="https://cdn.jsdelivr.net/gh/DOTfei/Learn-From-Failure@main/assets/banner-light.svg" width="100%">
  </picture>
</a>

English | [简体中文](README.zh-CN.md)

An experimental, AI-assisted learning Skill based on public corporate failure cases.
Maintainers have no business-operation or consulting experience, and the Skill's practical
effectiveness has not yet been demonstrated. Answers should show source links beside claims,
distinguish facts from interpretations, explain limits and suggest one small check.
AI ideas are untested; this is not professional advice. Older cases have not yet received a
claim-by-claim evidence review. See [LEGAL.md](LEGAL.md) for source-use restrictions.

See the [assistant self-review (Chinese)](skill-self-review.zh-CN.md) for fictional requests,
replies and limits. It is not a real-user effectiveness study. The optional
[interview and FAQ trial templates (Chinese)](templates/faq-pilot/interview.zh-CN.md)
support future private research.

[![Validate case files](https://github.com/DOTfei/Learn-From-Failure/actions/workflows/validate.yml/badge.svg)](https://github.com/DOTfei/Learn-From-Failure/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/DOTfei/Learn-From-Failure?style=social)](https://github.com/DOTfei/Learn-From-Failure/stargazers)
[![Cases](https://img.shields.io/badge/cases-38-9a3b2f)](cases/_index.md)

**A library of real, sourced corporate failure case studies — usable with any AI tool, or with no AI tool at all.**

Ask "does my company have any of the failure patterns that killed [Company X]?" and get an
answer grounded in what actually happened — not generic business-book advice.

---

## TL;DR

- **Have an AI tool?** Point it at this repo and ask about your company. See [Platform support](#platform-support).
- **Don't want to use AI?** Just browse the cases yourself at **[dotfei.github.io/Learn-From-Failure](https://dotfei.github.io/Learn-From-Failure/)**.
- **Want a quick self-check?** Use [CHECKLIST.md](CHECKLIST.md) — no AI needed.
- **Know a case that should be added?** [Suggest it here](https://github.com/DOTfei/Learn-From-Failure/issues/new/choose) — no writing required.

---

## What's in here

Every case follows the same four-part structure:

1. **What happened** — the facts, briefly.
2. **Root causes** — the real reason, not just "they went bankrupt."
3. **Warning signs** — what was visible *before* the collapse.
4. **Questions this raises** — the same questions, rewritten so you can ask them about *your* company.

Cases are tagged by **failure mechanism**, not industry — fraud, governance, cash burn,
disruption denial, product-market fit, scaling too fast, culture — because most of these
patterns aren't specific to one industry. See the full tagged list in [`cases/_index.md`](cases/_index.md).

## Why this exists

Most "startup failure lessons" content is a listicle you skim once and forget. This is built to
be used *conversationally*: describe your situation, and get pointed at the 3-6 cases that match
the actual mechanism of your risk — plus the exact questions that, in hindsight, would have
caught the problem at the real company.

**You don't have to ask for it, either.** If you're just talking through a normal business
decision — cutting costs, expanding fast, a hiring plan — and it strongly matches a known
failure pattern, the AI will flag it on its own: *"Before that — [Company] did almost exactly
this and here's what happened."* You still get the warning even if checking against failure
cases wasn't what you were asking about.

## See it in action

> **You:** We're a 12-person SaaS startup. We just closed a seed round and plan to grow from 12
> to 35 people in the next two months — before our renewal numbers next quarter come in. Our
> investors want to see "aggressive growth" in the deck. Is this a mistake?
>
> **Illustrative response (not a real user outcome):** Webvan disclosed facility order volumes
> below profitability levels in its [2000 annual report, filed April 2, 2001](https://www.sec.gov/Archives/edgar/data/1092657/000101287001001485/0001012870-01-001485.txt).
> A possible analogy is committing capacity before demand supports it; that is our interpretation,
> not proof that your hiring plan is wrong. SaaS hiring differs from grocery distribution:
> margins, paid backlog and how costs can be changed matter. Your renewal outlook is still missing.
>
> One untested check: compare the proposed team's committed cost with contracted revenue under
> a weaker-renewal scenario you choose. A paid backlog covering the added cost would weaken
> this concern. This is a learning question, not a demonstrated way to reduce failure rates.

Try it with your own situation, or read the full write-up in [`dist/learn-from-failure-bundle.md`](dist/learn-from-failure-bundle.md).

## Platform support

The content is plain Markdown, so there's no lock-in to one AI vendor:

| If you use... | Do this |
|---|---|
| **Claude Code** | Install as a plugin (`.claude-plugin/plugin.json`), or copy `.claude/skills/learn-from-failure/` into your own project. |
| **Cursor, Windsurf, OpenAI Codex CLI, Amp, Continue, or anything that reads [AGENTS.md](https://agents.md)** | Clone the repo and point your tool at it — `AGENTS.md` has the full instructions. |
| **ChatGPT Custom GPT, Gemini Gem, or any tool with a "knowledge upload"** | Upload [`dist/learn-from-failure-bundle.md`](dist/learn-from-failure-bundle.md) — one file with everything, sources included. |
| **A raw API call, or any chatbot with no file upload** | Paste the contents of the same bundle file into your prompt or system message. |
| **No AI tool at all** | Browse **[dotfei.github.io/Learn-From-Failure](https://dotfei.github.io/Learn-From-Failure/)** — searchable, filterable, nothing to install. |

Everything above reads from the same files in `cases/`. Nothing is copy-pasted by hand, so the
different versions can't drift out of sync — the bundle and the website are both regenerated by
scripts that CI checks on every change.

## How to read these cases

- **This is a reflection tool, not a prediction engine.** Many companies show one or two of
  these same warning signs and turn out fine (survivorship bias is real). A match means "worth
  investigating" — not "you will fail."
- **Check the sources.** Every case has a `## Sources` section. Verify a number before repeating
  it publicly. Found a mistake? [Report it](https://github.com/DOTfei/Learn-From-Failure/issues/new?template=case-error.yml).
- **Don't paste in confidential company info.** If you're analyzing your own company with an AI
  tool, keep that in your own private chat — don't commit it here. New cases should only cover
  companies with real public reporting (news, court filings, Wikipedia, etc.).
- **This is commentary, not a legal claim of guilt.** Allegations, indictments, and civil/
  regulatory findings are described as such — not as criminal convictions — unless a court
  actually convicted someone. See [LEGAL.md](LEGAL.md) for the full explanation and how to
  request a correction.

## Self-audit checklist (no AI needed)

[CHECKLIST.md](CHECKLIST.md) ([简体中文](CHECKLIST.zh-CN.md)) is a static list of every case's
"Questions this raises," grouped by failure mechanism — good for a quarterly review without
needing a conversation.

## Contributing

Three ways, from easiest to most involved:

1. **Just tell us.** [Suggest a case](https://github.com/DOTfei/Learn-From-Failure/issues/new?template=new-case.yml), [add a source](https://github.com/DOTfei/Learn-From-Failure/issues/new?template=add-source.yml), or [report an error](https://github.com/DOTfei/Learn-From-Failure/issues/new?template=case-error.yml) — fill in a form, no writing or Markdown required.
2. **Edit on GitHub.** Open any file in `cases/`, click the ✏️ pencil icon, make your change, and submit. GitHub creates the pull request for you — no local setup needed.
3. **Write a full case locally.** See [CONTRIBUTING.md](CONTRIBUTING.md) for the format and required sections.

## Project structure

```
AGENTS.md                 — instructions for AI tools other than Claude Code
.claude/skills/            — the Claude Code Skill (delegates to AGENTS.md)
.cursor/rules/              — the Cursor rule (also delegates to AGENTS.md)
cases/
  _index.md                — tagged index of every case
  _template.md               — template for adding a new case
  <company>.md               — one file per case, each with sources
  contrasts/                  — cases where a company faced the same pressure and adapted well
scripts/                   — regenerates the bundle and the website from cases/
dist/                      — single-file bundle for tools with no file access
docs/                      — the searchable website (GitHub Pages)
CHECKLIST.md               — static self-audit checklist
CHANGELOG.md               — what's changed, release by release
CODE_OF_CONDUCT.md         — expectations for contributors and discussion
LEGAL.md                   — sourcing standards, trademarks, corrections
```

## Language

Case files are written in English so the `## Sources` links map cleanly to the English-language
reporting they cite. That doesn't mean the conversation has to be in English — ask in Chinese
(or any language) and the analysis will come back translated. `README.zh-CN.md` and
`CHECKLIST.zh-CN.md` are ready-made Chinese references if you'd rather read them directly.

## License & legal

MIT — see [LICENSE](LICENSE). Case write-ups are original analysis of publicly reported facts,
not a copy of any single source; check the linked sources for authoritative detail. See
[LEGAL.md](LEGAL.md) for how this project handles trademarks, allegations vs. convictions, and
correction requests.
