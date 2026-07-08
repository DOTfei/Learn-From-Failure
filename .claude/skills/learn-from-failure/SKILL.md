---
name: learn-from-failure
description: Analyze a user's company/business situation against a knowledge base of real corporate failure case studies to spot matching failure patterns and warning signs before they repeat. Use when the user asks to review their business/company/startup/decision against past failures, asks "will this fail," "what are we missing," "is this a red flag," or explicitly invokes /learn-from-failure. Also use when the user wants to add a new failure case to the knowledge base.
---

# Learn From Failure

A knowledge base of real, well-documented company failures (`../../../cases/`, relative to
this file — i.e. the `cases/` folder at the project root), each broken into: what happened,
root causes, visible warning signs, and generalized questions. This skill uses that knowledge
base to analyze the user's own company/situation and flag matching failure patterns.

## How to run this skill

1. **Read `cases/_index.md` first.** It lists every case with its industry and failure-type
   tags (fraud_and_ethics, governance_and_leadership, financial_management, disruption_denial,
   product_market_fit, scaling_too_fast, culture_and_talent), plus a one-line description of
   each tag. Use it to decide which case files are actually relevant — don't read all case
   files for every question.

2. **Understand what the user is asking about.** If it's vague ("look at my company"), ask
   briefly: what's the business, and what specifically are they worried about (cash, a big
   decision, a competitor, growth pace, a co-founder/investor issue, etc.)? Don't over-ask —
   one round of clarification is enough if the intent is reasonably clear.

3. **Select 3-6 relevant cases**, not by industry match alone but by *mechanism* match — a
   SaaS founder over-hiring on hype maps better to WeWork/Katerra/Webvan (scaling_too_fast)
   than to Kodak (disruption_denial). Read the "Root causes" and "Questions this raises"
   sections of the selected case files in `cases/`.

4. **Analyze, don't just summarize.** For each pattern that plausibly applies:
   - Name the case and the specific mechanism that failed (not just "they went bankrupt").
   - Map it concretely to what the user described — use their numbers/decisions/wording, not
     generic restatements.
   - Ask the "Questions this raises" from the case file directly to the user, adapted to their
     situation, so they self-diagnose rather than just being told.
   - Be honest when a pattern does NOT clearly apply — false-positive pattern-matching erodes
     trust in the tool. It's fine to say "none of the classic patterns fit this well, but here's
     the closest partial match and why it's not a full match."

5. **End with a short, concrete list** — the 2-4 highest-signal risks, phrased as things to
   check or decide this week/month, not a lecture on corporate history.

6. **If a matched case has a contrast file** (see `cases/contrasts/`, e.g. `netflix-pivot.md`
   contrasts with `blockbuster.md`), consider surfacing it too — it shows what a company that
   faced the *same* pressure but responded well actually did differently, which is often more
   actionable than only hearing about the failure.

## Adding a new case to the knowledge base

When the user wants to add a new failure case (their own past venture, a case they read about,
etc.), use `cases/_template.md` as the structure. Required frontmatter: `slug`, `company`,
`industry`, `founded`, `failed`, `failure_types` (use existing tags from `cases/_index.md`
where they fit, add a new tag only if genuinely none fit), `severity`. Required sections: What
happened, Root causes, Warning signs, Questions this raises for another company (phrased
generically so it pattern-matches to other companies, not just this one), and a **Sources**
section with links to the reporting used (Wikipedia, major news, court filings, etc.) — if you
can't find at least one independent source for a claim, don't include that claim. Use WebSearch
to verify facts/figures rather than relying on memory. After adding the file, update the table
and, if a new tag was introduced, the taxonomy section in `cases/_index.md`.

If the user wants to add a case about their *own* company/venture (not independently
verifiable via public sources), that's fine — just skip the Sources section and don't mark it
as if it were a citable public case; keep it in a clearly separate area if the repo maintainer
wants public cases and private ones kept apart.

## Language

Case files (`cases/*.md`) are written in English so that the cited `## Sources` map cleanly to
the English-language reporting they're drawn from. **This does not mean the conversation has to
be in English.** Respond to the user in whatever language they're writing in (e.g. reply fully
in 简体中文 if the user writes in Simplified Chinese) — translate the relevant "Root causes" /
"Warning signs" / "Questions" content into that language as you present it, rather than quoting
the English verbatim. Keep company names, and it's fine to keep one short English source title
in parentheses if useful for searching later, but the analysis itself should read naturally in
the user's language. `README.zh-CN.md` and `CHECKLIST.zh-CN.md` are pre-translated references
you can point a Chinese-speaking user to.

## Notes

- This is pattern-matching for reflection, not a verdict. Never tell the user their company
  "will fail" — frame findings as risks/questions worth taking seriously given precedent.
  Survivorship bias applies: many companies show one or two of these warning signs and are
  fine. A match is a prompt to investigate, not a diagnosis.
- If the user's business is in an industry not well represented in the case base (e.g. a local
  service business), still apply the mechanism-level patterns (cash burn, founder control,
  disruption denial, cost-cutting the wrong thing) — most of these transcend industry, which is
  why `cases/_index.md` organizes by failure mechanism, not just industry.
- Privacy: the user may share sensitive internal details (financials, cap table, disputes) to
  get a good analysis. Don't suggest committing that detail into this repo's case files or
  anywhere it could become public — keep company-specific analysis in the conversation, not in
  files intended for the shared knowledge base.
