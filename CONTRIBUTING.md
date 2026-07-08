# Contributing a case

1. Copy `cases/_template.md` to `cases/<company-slug>.md`.
2. Fill in the frontmatter:
   - `slug`, `company`, `industry`, `founded`, `failed`, `severity`
   - `failure_types`: reuse tags from the taxonomy in `cases/_index.md`
     (`fraud_and_ethics`, `governance_and_leadership`, `financial_management`,
     `disruption_denial`, `product_market_fit`, `scaling_too_fast`, `culture_and_talent`)
     wherever they genuinely fit. Only introduce a new tag if none of the existing ones
     describe the core mechanism — and if you do, add it to the taxonomy section too.
3. Write the four required sections:
   - **What happened** — 2-5 sentences, facts only, no editorializing.
   - **Root causes** — the deep cause, not just the symptom ("filed for bankruptcy" is not a
     root cause).
   - **Warning signs** — things an outside observer could plausibly have noticed *before* the
     collapse, not things only obvious in hindsight.
   - **Questions this raises for another company** — phrase these generically, as if asking
     them of any company, not just this one. This is the part the skill actually surfaces to
     users, so it matters most.
4. Add a **Sources** section with links to independent reporting (news, Wikipedia, court
   filings, regulatory findings, etc.). If you can't source a specific figure or claim, either
   find a source or leave it out — don't guess.
5. Add a row to the table in `cases/_index.md`, and update the taxonomy section if you added a
   new tag.
6. Run `python3 scripts/build_bundle.py` and commit the resulting change to
   `dist/learn-from-failure-bundle.md`. This file is a single-file copy of the whole knowledge
   base for platforms with no repo/file access (ChatGPT Custom GPT, Gemini Gem, raw API calls —
   see README → Platform support). CI checks it's up to date and will fail your PR if you forget.
7. Run `python3 scripts/build_site.py` and commit the resulting change to `docs/data.json` —
   this feeds the GitHub Pages case browser at `docs/index.html`. CI checks this stays in sync
   too.
8. Run `python3 scripts/validate_cases.py` — CI runs this too, but it's faster to catch issues
   locally.

If you're updating shared workflow logic (not adding a case), edit `AGENTS.md` at the repo
root — it's the single source of truth read by Claude Code (`SKILL.md` delegates to it), Cursor
(`.cursor/rules/learn-from-failure.mdc` delegates to it), and other AGENTS.md-aware tools. Don't
fork the logic into multiple files.

## What makes a good case

- A real company, publicly reported on, with enough detail to identify a specific *mechanism*
  of failure (not just "it went bankrupt").
- A failure with lessons that generalize — the "Questions" section should be usable by a reader
  in a completely different industry.

## What doesn't belong here

- Unverified claims, rumors, or takes with no source.
- Your own company's private/confidential situation — analyze that in conversation with the
  skill, don't commit it as a public case file.
- Cases that are really just "the market changed and there was nothing anyone could have done"
  — if there's no meaningful warning sign or decision point, it's not a useful case for this
  format.
