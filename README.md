# Learn From Failure

English | [简体中文](README.zh-CN.md)

A knowledge base of real, sourced corporate failure case studies — packaged as a
[Claude Code](https://claude.com/claude-code) Skill — so you can ask "does my company have any
of the failure patterns that killed [company X]?" and get an analysis grounded in what actually
happened, not generic business-book platitudes.

Each case is broken into the same structure: what happened, root causes, the warning signs that
were visible *before* the collapse, and a set of questions phrased generically enough to ask
about any company. A tagged index (`cases/_index.md`) organizes cases by **failure mechanism**
(fraud, governance, cash burn, disruption denial, product-market fit, scaling too fast, culture)
rather than just industry, because most of these patterns aren't industry-specific.

## Why

Most "lessons from failed startups" content is a listicle. This is meant to be used
conversationally: describe your situation, and get pointed at the 3-6 cases that actually match
the *mechanism* of your risk, with the same questions that, in hindsight, would have flagged the
problem at the real company.

## Install

**Option A — as a Claude Code plugin:** this repo has a `.claude-plugin/plugin.json` manifest,
so you can add it via Claude Code's plugin marketplace flow pointed at
`https://github.com/DOTfei/Learn-From-Failure`.

**Option B — manual:** copy (or symlink) the `.claude/skills/learn-from-failure/` folder into
your own project's `.claude/skills/` directory, or clone this whole repo and point Claude Code
at it directly. The skill reads case files from the `cases/` folder at this repo's root.

## Usage

Ask things like:

- "We're about to raise a big round and hire aggressively before we've proven unit economics — is this a WeWork/Webvan-style mistake?"
- "Our board is basically just the founder's friends — should I be worried?"
- "We're cutting our most experienced (expensive) staff to save money — sanity check this against Circuit City."
- "Add [Company Y] as a new case, here's what I know about why it failed: ..."

The skill will pick relevant cases by failure *mechanism*, not just by matching your industry,
and will push back with the case's actual root-cause questions rather than just summarizing
history at you.

## A note on how to read these cases

**This is a pattern-matching tool for reflection, not a prediction engine.** Survivorship bias
is real: plenty of companies exhibit one or two of these same warning signs (high leverage, a
dominant founder, aggressive growth) and turn out fine. A match here means "this is worth
investigating carefully," not "your company will fail." Use it to ask better questions, not to
get a verdict.

**Case content may be imperfect.** Each case includes a `## Sources` section — check it before
treating a specific number or claim as gospel, especially for anything you plan to repeat
publicly. If you spot an error, please open an issue or PR.

**Don't put confidential information in this repo.** If you use the skill to analyze your own
company, do that in your own private conversation/workspace — don't commit your internal
financials, disputes, or cap table into a case file here. New cases contributed to this
knowledge base should be about companies with genuine public reporting available (news
coverage, court filings, Wikipedia, etc.).

## Structure

```
cases/
  _index.md        — tagged index of all cases + failure-type taxonomy
  _template.md      — template for adding a new case
  <company>.md      — one file per case
.claude/skills/learn-from-failure/
  SKILL.md          — the skill definition Claude Code reads
scripts/
  validate_cases.py — checks frontmatter, required sections, and index consistency
CHECKLIST.md        — a static self-audit checklist distilled from every case's questions,
                       for periodic review without needing a conversation
```

## Self-audit without the skill

If you just want a static checklist to run through quarterly (no conversation needed), see
[CHECKLIST.md](CHECKLIST.md) ([简体中文](CHECKLIST.zh-CN.md)) — it's the "Questions this
raises" from every case, grouped by failure mechanism.

## Language

Case files themselves are in English (so the `## Sources` links map cleanly to the
English-language reporting they cite), but the skill responds in whatever language you ask in —
Chinese, English, whatever — translating the relevant content live rather than requiring the
case files to be pre-translated. `README.zh-CN.md` and `CHECKLIST.zh-CN.md` are pre-translated
references for Chinese-speaking users browsing the repo directly.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: use `cases/_template.md`, cite real
sources, tag it with existing failure-type tags where they fit, update `cases/_index.md`, and
run `python3 scripts/validate_cases.py` before opening a PR (CI runs this automatically too).

## License

Case summaries are original writing about publicly reported facts; see [LICENSE](LICENSE)
(MIT) for the repo content. This is commentary/analysis, not a reproduction of any single
source — check the linked sources for authoritative detail.
