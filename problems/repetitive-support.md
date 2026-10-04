# Repetitive support questions — one problem pilot

Status: untested learning suggestion, reviewed October 3, 2026. This is not a failure case,
success formula, product endorsement or validated AI intervention. Maintainers have no
business-operation or consulting experience. No real support tickets or customer outcomes
were collected in this pilot.

## When to use this note

Use when a user explicitly asks how to handle repeated, low-risk support questions or whether
AI could help. First establish whether the questions really repeat, whether approved answers
exist and how much handling time they take. Do not infer a problem from company size or a
founder's workload alone. No historical failure case needs to be forced into the answer.

## Research lead, not evidence

[Starter Story's Userdesk research entrance](https://www.starterstory.com/userdesk-breakdown)
was surfaced through search on October 3, 2026. It has not been established here as an original
founder interview. No article body, revenue figure, founder quote, customer count or claimed
time saving is imported. The founder's original account and measured outcomes remain pending.
The documents below are a separate process reference, not corroboration of Userdesk's story.

## What the original sources actually support

GitLab's own support handbook treats repeated reply text as a reason to examine the upstream
process, and recommends documentation links and filling documentation gaps.
[GitLab, How to Respond to Tickets, last modified June 9, 2026](https://handbook.gitlab.com/handbook/support/workflows/how-to-respond-to-tickets/)

GitLab's AI guidance requires staff to write customer replies from their own investigation,
use AI for refinement rather than complete authorship, verify output, and check data
classification before selecting a tool.
[GitLab, Using AI in Support, last modified July 17, 2026](https://handbook.gitlab.com/handbook/support/ai/using-ai-in-support/)

These are published operating requirements from one organization, not independently observed
compliance or measured results. Two pages from GitLab are not two independent success studies.
They do not establish how common this problem is in small businesses, Userdesk's results,
or that AI performs better than ordinary FAQ search.

## Our interpretation and important differences

A repeated question might mean an answer is hard to find, onboarding is unclear, or the
product itself needs fixing. Adding a chatbot could hide that cause. GitLab's technical-support
context, staffing and data controls may differ substantially from a small shop or service team.
Customer-specific problems are not made safe or repeatable merely by similar wording.

## Non-AI option first

For one question category, improve the relevant FAQ or onboarding instruction and maintain
an approved quick reply pointing to it. This is a candidate baseline, not a proven improvement.
If manual lookup is already quick, or answers change frequently, AI may add no useful value.

## AI option — our untested proposal, not GitLab's workflow

Use AI internally to find a candidate answer in the business's approved FAQ and return its
exact source link and applicable version. A staff member verifies the match and writes the
customer response; optionally use AI to polish that human draft without adding new facts.
If no source supports an answer, return "no supported answer" and route to a person.
Do not auto-send replies, invent links, make refund promises or change accounts.

Inputs: a maintained, rights-cleared FAQ, relevant version/date, the question category and
an authorized human reviewer. Start with synthetic questions and public or deliberately
created answers. Real ticket use requires the user's permission and a suitable private,
approved environment with retention/access controls. Do not put tickets in this repository
or upload names, credentials, attachments or private records to an unapproved tool.

## When not to apply this pilot

Do not use this experiment for payments/refunds, identity or account access, legal/medical
advice, security incidents or situations needing individual investigation. Missing or stale
approved documentation is a reason to fix the source first, not let AI guess. An AI tool being
approved by GitLab does not mean it is approved for another company's customer data.

## One small check

Hypothesis: answer discovery, not missing knowledge or product defects, is the bottleneck.
In the user's private environment, compare FAQ/quick-reply lookup with AI-assisted lookup
for one low-risk category on a small, user-chosen set of questions. Include paraphrases and
questions with no documented answer. Use the same approved sources for both methods and
alternate which method is tried first to reduce familiarity effects.

Record total handling time, including prompting, review and corrections, alongside unsupported
answers, wrong versions and escalation decisions. Have a human check answers against the
approved source, not against the model's explanation. The user sets acceptable time/quality
criteria before testing. Stop for unsafe disclosures or unauthorized actions.

If most questions lack approved answers, or reviewed AI lookup is no faster or less accurate
than the baseline, the hypothesis weakens: keep the simpler workflow or repair documentation.
No percentage saving is promised. A small local trial would not prove general effectiveness.

## Content walkthrough — synthetic, not an effectiveness test

Assumed test FAQ, created for this exercise: public opening hours are 09:00–17:00 Monday–Friday;
no refund rules or account-access instructions are supplied. These are fictional, not facts
about GitLab, Userdesk or a real business.

- "When do you open on Friday?" — candidate answer may point to the approved hours entry;
  the staff member verifies and writes the reply. Do not invent a public URL for a synthetic FAQ.
- "Can I get a refund after 30 days?" — no supported answer; escalate, no invented policy.
- "Here is my password; reset my account." — outside scope; do not request/store credentials
  or perform an account action. Use the business's authorized identity process.

Manual result: the written rules distinguish supported lookup, absent evidence and sensitive
requests. No executable assistant was benchmarked and no timing or accuracy results exist.
The research process found usable process documentation, but the founder-story evidence chain
is incomplete; do not scale this into a success-case collection on that basis.

## Source and reuse record

Checked October 3, 2026:

- **GitLab, How to Respond to Tickets:** link above. Read the canned-response/process section,
  documentation section and last-modified footer; not all handbook pages or linked studies.
  Initial publication date unknown; June 9, 2026 is the page's modification date.
- **GitLab, Using AI in Support:** link above. Read data classification, reply-formatting and
  best-practice sections plus footer; not every linked tool policy. Initial publication date
  unknown; July 17, 2026 is its modification date. Supports stated rules, not their effectiveness.
- **Starter Story:** research URL only; search metadata read, article not imported or treated
  as an interview transcript. Publication date not independently verified. Checked
  [Starter Story terms](https://www.starterstory.com/terms) content/republication provisions
  and [HubSpot website terms](https://legal.hubspot.com/website-terms-of-use) sections 1–2.
  No permission for public Skill reuse established. Do not import its stories or databases.
- **GitLab rights/access:** read [handbook repository license](https://gitlab.com/gitlab-com/content-sites/handbook/-/raw/main/LICENSE)
  and [website terms](https://handbook.gitlab.com/handbook/legal/policies/website-terms-of-use/)
  sections 2–3. Repository license covers software and associated documentation, with third-party
  exceptions; website terms recognize applicable content-licensing permissions. This note uses
  brief original factual descriptions and links, not reproduced handbook prose, prompts,
  diagrams, customer records or third-party components. No blanket rights clearance is claimed.
  No source logos or endorsement claims are used. Recheck permissions before larger reuse.
