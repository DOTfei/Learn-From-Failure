# Changelog

This project moves fast in small increments; this is a high-level summary, not every commit.
See the [commit history](https://github.com/DOTfei/Learn-From-Failure/commits/main/) for full detail.

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
