# Changelog

This project moves fast in small increments; this is a high-level summary, not every commit.
See the [commit history](https://github.com/DOTfei/Learn-From-Failure/commits/main/) for full detail.

## 2026-10-04 — assistant self-review

- Applied the project Skill to fictional business and support requests, retaining replies,
  source-reading scopes and self-assessment in `skill-self-review.zh-CN.md`.
  This is a manual assistant self-review, not an independent benchmark or real-team study.
- Replaced the unsupported proactive-warning example with a directly linked, scoped Webvan
  disclosure, analogy limits and one check. Real-user effectiveness remains unverified.

## 2026-10-03 — one problem pilot

- Added a Chinese recruitment and interview workflow under `templates/faq-pilot/`:
  recent-event questions, existing-workflow and counterevidence prompts, a blank private-note
  form, and conditions for moving into the FAQ trial. No outreach sent or interview results claimed.
- Saved reusable Chinese field-run instructions and a blank 20-run CSV under
  `templates/faq-pilot/`, outside the bundle's problem-note inputs. Method order is prefilled
  for 10 paired questions. Completed records must remain in the team's private environment.
  No real-team run or measured results are claimed; this compares support workflows, not
  the overall Skill's effectiveness.
- Added `problems/repetitive-support.md`: explicit-request-only support learning note with
  original-source process references, a non-AI baseline, untested AI option and one small check.
  Starter Story's Userdesk entrance remains an unverified research lead; no article or metrics
  imported and no founder-story verification or measured effectiveness claimed.
- Linked the note from shared Skill instructions and index, without counting it as a corporate
  failure or success case. Skill-creator guidance kept routing narrow and the reference separate.
- Reused the bundle builder and preservation check for problem notes, with matching CI paths.
  Website functionality and case data are unchanged. Walkthrough uses fictional questions only.
- Existing case/bundle checks, deterministic rebuild and unchanged-site checks passed.
  Skill metadata passed basic local checks; skill-creator's full validator could not run because
  PyYAML is absent in both available Python runtimes. No dependency installed for this pilot.

## 2026-10-02 — scoped evidence review

- Webvan: replaced unsupported fundraising, rollout and motive claims with a limited annual-report
  summary and SEC outcome reference; removed the unsupported product-market-fit classification.
- WeWork: separated the September 2019 IPO withdrawal request from the November 2023 Chapter 11
  announcement. Identified the readable registration draft as confidential at submission;
  public-release timing was not verified. Removed absolute governance/profitability judgments
  and the unsupported scaling classification.
- Katerra: withdrew unsupported figures and allegations, removed the fraud tag and marked research
  pending. Removed Skill-example, taxonomy and bilingual checklist recommendations; kept research entrances.
- Added source dates, reading scopes, analogy limits and one untested check per entry. Updated the
  bilingual hiring illustration to show evidence and uncertainty, not a real-user success story.
- Source-use review used SEC policy; blocked court entrances and incomplete rights checks are
  explicitly recorded, not bypassed. No restricted datasets, copied articles or new features added.
- Rebuilt the portable bundle and site data. Validation checks structure and preservation, not
  factual truth, legal clearance or effectiveness. Manual hiring/lease/multi-line walkthroughs are
  documented in `evidence-review-walkthrough.md`; they are content/rule checks, not user studies.

## 2026-07

- Added a Chinese (中文) UI toggle to the case-browser website (`docs/index.html`) — interface
  chrome translates live, case content stays English (sourced from English-language reporting).
- Added 5 Southeast/South Asian cases: BYJU'S (India), eFishery (Indonesia), Propzy (Vietnam),
  TaniHub (Indonesia), Kaodim (Malaysia) — bringing geographic coverage to 12 countries.
- Added `LEGAL.md` and a validator check distinguishing criminal convictions from unresolved
  charges/allegations, after catching two cases that had overstated legal status.
- Added 7 cases for geographic/mechanism diversity: Evergrande (China), Wirecard (Germany),
  Satyam (India), Steinhoff (South Africa), HIH Insurance (Australia), Odebrecht (Brazil), and
  Boeing 737 MAX — which introduced a new failure-mechanism tag, `safety_and_quality`.
- Added proactive-warning behavior: the AI now volunteers a relevant case even when the user
  didn't explicitly ask for a failure-pattern review, if there's a strong mechanism match.
- Added `AGENTS.md` (tool-agnostic instructions), a single-file bundle
  (`dist/learn-from-failure-bundle.md`) for platforms without file access, and the searchable
  static site (`docs/`) on GitHub Pages — making the knowledge base usable from any AI tool, or
  none at all.
- Added GitHub issue templates for suggesting a case, adding a source, and reporting an error.
- Added a project banner, bilingual (中文) documentation, and a self-audit checklist
  (`CHECKLIST.md`) usable without any AI tool.

## 2026-07 (initial release)

- Initial release: 25 sourced corporate failure case studies as a Claude Code Skill, tagged by
  failure mechanism (fraud, governance, financial management, disruption denial,
  product-market fit, scaling too fast, culture) rather than industry.
