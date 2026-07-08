---
name: learn-from-failure
description: Analyze a user's company/business situation against a knowledge base of real corporate failure case studies to spot matching failure patterns and warning signs before they repeat. Use when the user explicitly asks to review their business/decision against past failures, asks "will this fail," "what are we missing," "is this a red flag," or wants to add a new case. ALSO use proactively (without being asked) whenever the user describes an ordinary business decision — pricing, hiring/firing, fundraising, expansion, a board/investor matter, a cost cut, a pivot — that strongly and specifically matches a known failure mechanism in this knowledge base; surface a brief warning citing the case even if the user didn't ask for failure analysis.
---

# Learn From Failure

The full instructions for this skill live in **`AGENTS.md`** at the repo root (i.e.
`../../../AGENTS.md` relative to this file). That file uses the tool-agnostic
[AGENTS.md](https://agents.md) convention so the same instructions work across Claude Code,
Cursor, Windsurf, and other agentic tools without duplication — read it now and follow it.

Everything below is Claude-Code-specific context that `AGENTS.md` doesn't need to know about.

## Claude-Code-specific notes

- The `cases/` folder referenced throughout `AGENTS.md` is at the project root, i.e.
  `../../../cases/` relative to this file.
- When this Skill is invoked, you already have file-read access to the repo, so the "If you
  can't read files directly" fallback section in `AGENTS.md` doesn't apply to you — always read
  the actual case files rather than asking the user to paste `dist/learn-from-failure-bundle.md`.
- If you're maintaining this repo and change the workflow logic, edit `AGENTS.md` (the shared
  source of truth) rather than duplicating changes here. Only add content to this file that is
  genuinely Claude-Code-specific.
