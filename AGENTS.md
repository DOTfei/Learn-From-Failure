# Learn From Failure — Agent Instructions

This file follows the [AGENTS.md](https://agents.md) convention read by most coding/agentic AI
tools (Cursor, Windsurf, OpenAI Codex CLI, Amp, Continue, Claude Code, etc.). If your tool
doesn't auto-discover this file, paste its contents into your system prompt / custom
instructions, or point the tool at this repo.

This repo is a knowledge base of sourced corporate failure case studies, organized by *failure
mechanism* rather than industry, meant to be used conversationally: a user describes their
company/decision, and you analyze it against real precedent.

Claude Code users: see `.claude/skills/learn-from-failure/SKILL.md` for the equivalent Skill
form of these same instructions (auto-loaded, no setup needed).

## When to use this

When the user asks you to review their business/company/startup/decision against past
failures, asks "will this fail," "what are we missing," "is this a red flag," references this
repo, or wants to add a new case to the knowledge base.

## How to run this

1. **Read `cases/_index.md` first.** It lists every case with its industry and failure-type
   tags (`fraud_and_ethics`, `governance_and_leadership`, `financial_management`,
   `disruption_denial`, `product_market_fit`, `scaling_too_fast`, `culture_and_talent`), plus a
   one-line description of each tag. Use it to decide which case files are actually relevant —
   don't read every case file for every question.

2. **Understand what the user is asking about.** If it's vague ("look at my company"), ask
   briefly: what's the business, and what specifically are they worried about (cash, a big
   decision, a competitor, growth pace, a co-founder/investor issue, etc.)? One round of
   clarification is usually enough.

3. **Select 3-6 relevant cases**, not by industry match alone but by *mechanism* match — a SaaS
   founder over-hiring on hype maps better to WeWork/Katerra/Webvan (`scaling_too_fast`) than to
   Kodak (`disruption_denial`). Read the "Root causes" and "Questions this raises" sections of
   the selected files in `cases/`.

4. **Analyze, don't just summarize.** For each pattern that plausibly applies:
   - Name the case and the specific mechanism that failed (not just "they went bankrupt").
   - Map it concretely to what the user described — use their numbers/decisions/wording, not
     generic restatements.
   - Ask the "Questions this raises" from the case file directly, adapted to their situation, so
     they self-diagnose rather than just being told.
   - Be honest when a pattern does NOT clearly apply — false-positive pattern-matching erodes
     trust. It's fine to say "none of the classic patterns fit this well, but here's the closest
     partial match and why it's not a full match."

5. **End with a short, concrete list** — the 2-4 highest-signal risks, phrased as things to
   check or decide this week/month, not a lecture on corporate history.

6. **Surface contrast cases when relevant** (`cases/contrasts/`, e.g. `netflix-pivot.md`
   contrasts with `blockbuster.md`) — a company that faced the *same* pressure and responded
   well is often more actionable to hear about than only the failure.

## Adding a new case

Use `cases/_template.md` as the structure. Required frontmatter: `slug`, `company`, `industry`,
`founded`, `failed`, `failure_types` (reuse tags from `cases/_index.md` where they fit),
`severity`. Required sections: What happened, Root causes, Warning signs, Questions this raises
for another company (phrased generically), and a **Sources** section with links to independent
reporting — don't include a claim you can't source. If your tool has web search/browsing, use
it to verify facts rather than relying on training data. After adding the file, update the table
and taxonomy in `cases/_index.md`.

## Language

Case files are written in English so `## Sources` links map cleanly to the English-language
reporting they cite. Respond to the user in whatever language they're writing in — translate the
relevant content live rather than quoting English verbatim. `README.zh-CN.md` and
`CHECKLIST.zh-CN.md` are pre-translated references for Chinese-speaking users.

## Notes

- This is pattern-matching for reflection, not a verdict. Never tell the user their company
  "will fail" — frame findings as risks/questions worth taking seriously given precedent.
  Survivorship bias applies: many companies show one or two of these warning signs and are
  fine. A match is a prompt to investigate, not a diagnosis.
- If the user's business is in an industry not well represented here (e.g. a local service
  business), still apply the mechanism-level patterns — most transcend industry, which is why
  `cases/_index.md` organizes by failure mechanism, not just industry.
- Privacy: the user may share sensitive internal details to get a good analysis. Don't suggest
  committing that detail into this repo's case files — keep company-specific analysis in the
  conversation, not in files intended for the shared knowledge base.

## If you can't read files directly

If your environment doesn't support reading repo files (e.g. a plain chat interface with no
file/browsing tool), ask the user to paste in `dist/learn-from-failure-bundle.md` — a single
concatenated file containing the full index, checklist, and all cases, meant to be pasted as
context or uploaded as a knowledge file (see `README.md` → "Platform support").
