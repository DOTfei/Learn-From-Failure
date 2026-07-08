# Legal notes

This isn't a substitute for advice from an actual lawyer — if you're relying on this project
commercially at scale, get a real legal review. This document explains the choices already made
to keep the project on solid ground, and what's still worth having a lawyer look at.

## What this project is (and isn't)

This is **commentary and analysis of publicly reported facts** about real companies, for
educational purposes. It is **not** legal, financial, or investment advice, and nothing here
should be read as a recommendation to buy, sell, invest in, or avoid any company, security, or
transaction. It does not evaluate any company that isn't already covered in `cases/`.

## Why this is generally safe ground, legally

- **Truth is a defense to defamation, and we cite sources.** Every case has a `## Sources`
  section linking to independent reporting, court records, regulatory filings, or company/
  government statements. Claims are attributed to that reporting, not asserted as our own
  original findings.
- **Company and brand names are used descriptively, not as an endorsement or in commerce.**
  Referring to a company by its real name to discuss and critique publicly known facts about it
  ("nominative fair use") is standard journalistic and commentary practice — this project does
  not use any company's name or mark to sell a competing product or imply affiliation with or
  endorsement by that company. All trademarks belong to their respective owners.
- **Allegations vs. convictions are treated as legally distinct, on purpose.** Being investigated,
  charged, sued, or fined by a regulator is not the same as being criminally convicted, and this
  project's `severity` field and case text are meant to say precisely which one applies (see
  `cases/_template.md`). `scripts/validate_cases.py` includes an automated check that flags any
  case claiming `fraud_conviction` in its frontmatter if the body doesn't actually document a
  conviction — this exists specifically to catch the mistake of asserting someone is guilty of a
  crime before a court has found that. If you ever spot a case that gets this wrong, please
  [report it](https://github.com/DOTfei/Learn-From-Failure/issues/new?template=case-error.yml)
  immediately — this is the single most important category of correction for this project.
- **Most subjects are already-resolved, court-adjudicated, or regulator-published matters** —
  bankruptcies, SEC/regulator settlements, and criminal convictions that are already public
  record — which is the lowest-risk category of factual reporting to reference.

## What contributors and users should keep in mind

- **Don't add unsourced claims.** [CONTRIBUTING.md](CONTRIBUTING.md) requires a source for every
  case; don't work around that by phrasing a guess as fact.
- **Don't assert a living or currently-operating person's guilt beyond what's actually been
  legally established.** Say "denies the charges," "trial ongoing," or "civil finding" rather
  than "convicted" or "guilty" unless a court has actually ruled that. See `cases/_template.md`.
- **Don't put your own company's confidential information into a public case file.** If you're
  using this project (via the Skill, AGENTS.md, or the bundle) to analyze your own business,
  keep that analysis in your own private conversation — don't commit it here.
- **If something about you or your company is inaccurate here**, [open a correction request](https://github.com/DOTfei/Learn-From-Failure/issues/new?template=case-error.yml).
  Corrections to factual claims are the top priority contribution type for this project — it has
  no interest in keeping inaccurate or unfair content live.

## License vs. this document

[LICENSE](LICENSE) (MIT) covers the code/scripts in this repo and disclaims warranty on them, in
the standard open-source sense. It does not and cannot immunize anyone from liability for false
statements of fact — that protection comes from accuracy and sourcing, not a software license,
which is why the practices above (not the license) are what actually keep this project safe to
publish and to contribute to.
