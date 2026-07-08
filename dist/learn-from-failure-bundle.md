# Learn From Failure — Bundled Knowledge Base

You are being given a knowledge base of real, sourced corporate failure case studies, organized
by *failure mechanism* (fraud & ethics, governance & leadership, financial management,
disruption denial, product-market fit, scaling too fast, culture & talent, safety & quality)
rather than industry.
Use it to analyze the user's own company/business situation and flag matching failure patterns.

## Two modes

Mode 1 - explicit review: the user directly asks you to check their business/decision against
failure cases. Do the full workflow below.

Mode 2 - proactive warning, unasked: the user is just talking through a normal business decision
(pricing, hiring/firing, fundraising, expansion, a cost cut, a pivot) with no mention of failure
analysis. If what they describe strongly and specifically matches one case's mechanism,
volunteer a short warning alongside your normal answer - one case, 1-2 sentences, e.g. "Before
that - [Company] did almost exactly this and here's what happened: ...". Only do this for a
genuinely strong match; if it's a loose/generic match, say nothing. Don't turn every answer into
a history lecture - this is a brief flag, not the full analysis, unless they ask for more.

## How to use this (mode 1 - the full workflow)

1. Check the index and taxonomy below to find cases matching the *mechanism* of what the user
   describes, not just their industry — e.g. a founder over-hiring on hype maps better to
   WeWork/Katerra/Webvan (scaling too fast) than to Kodak (disruption denial).
2. Select 3-6 relevant cases. For each: name the case and the specific mechanism that failed
   (not just "they went bankrupt"), map it concretely to what the user described using their own
   numbers/decisions/wording, and ask the case's "Questions this raises" directly, adapted to
   their situation — so they self-diagnose rather than being told.
3. Be honest when nothing matches well — false-positive pattern-matching erodes trust. It's fine
   to say "none of the classic patterns fit this well, but here's the closest partial match."
4. End with 2-4 concrete, highest-signal risks phrased as things to check or decide soon — not a
   history lecture.
5. This is pattern-matching for reflection, not a verdict, in EITHER mode. Survivorship bias applies: many
   companies show one or two of these warning signs and are fine. Never tell the user their
   company "will fail" — frame findings as risks worth investigating given precedent.
6. Respond in whatever language the user is writing in — translate the relevant content live
   rather than quoting the English below verbatim.
7. Don't ask the user to paste confidential internal details back into any public place; keep
   company-specific analysis in the conversation.

Everything from here down is the knowledge base itself: the tagged index, the self-audit
checklist, then every individual case file (including contrast cases), each with its sources.

---

<!-- ==== cases/_index.md ==== -->

# Failure Case Index

32 failure cases, tagged by failure_types for pattern matching. One company can span multiple tags.
Every case file has a `## Sources` section linking to the reporting/references used — check
those before citing a specific number or claim with confidence, and please add sources for
any new case you contribute.

| Case | Industry | Primary failure types |
|---|---|---|
| [enron](enron.md) | energy/finance (US) | fraud_and_ethics, governance_and_leadership, financial_management |
| [lehman-brothers](lehman-brothers.md) | finance (US) | financial_management, governance_and_leadership |
| [kodak](kodak.md) | manufacturing/tech (US) | disruption_denial, culture_and_talent |
| [blockbuster](blockbuster.md) | retail/media (US) | disruption_denial, product_market_fit |
| [nokia-mobile](nokia-mobile.md) | tech/hardware (Finland) | disruption_denial, culture_and_talent, governance_and_leadership |
| [theranos](theranos.md) | healthcare/tech (US) | fraud_and_ethics, governance_and_leadership, product_market_fit |
| [wework](wework.md) | real estate/tech (US) | governance_and_leadership, financial_management, scaling_too_fast |
| [quibi](quibi.md) | media/streaming (US) | product_market_fit, governance_and_leadership |
| [pets-com](pets-com.md) | e-commerce (US) | product_market_fit, financial_management, scaling_too_fast |
| [webvan](webvan.md) | e-commerce/logistics (US) | scaling_too_fast, financial_management, product_market_fit |
| [toys-r-us](toys-r-us.md) | retail (US) | financial_management, disruption_denial |
| [sears](sears.md) | retail (US) | financial_management, disruption_denial, culture_and_talent |
| [borders](borders.md) | retail (US) | disruption_denial, culture_and_talent |
| [juicero](juicero.md) | hardware (US) | product_market_fit, financial_management |
| [ftx](ftx.md) | crypto/finance (US/Bahamas) | fraud_and_ethics, governance_and_leadership, financial_management |
| [segway](segway.md) | hardware (US) | product_market_fit, governance_and_leadership |
| [myspace](myspace.md) | tech/social (US) | culture_and_talent, disruption_denial, product_market_fit |
| [circuit-city](circuit-city.md) | retail (US) | culture_and_talent, financial_management, disruption_denial |
| [blackberry](blackberry.md) | tech/hardware (Canada) | disruption_denial, culture_and_talent, governance_and_leadership |
| [yahoo](yahoo.md) | tech/internet (US) | governance_and_leadership, culture_and_talent, product_market_fit |
| [katerra](katerra.md) | construction/proptech (US) | scaling_too_fast, governance_and_leadership, financial_management, fraud_and_ethics |
| [fusionex](fusionex.md) | tech/data analytics (Malaysia) | governance_and_leadership, financial_management, fraud_and_ethics |
| [kenny-rogers-roasters](kenny-rogers-roasters.md) | restaurant/franchise (US) | scaling_too_fast, financial_management |
| [luckin-coffee](luckin-coffee.md) | retail/F&B (China) | fraud_and_ethics, governance_and_leadership, scaling_too_fast |
| [silicon-valley-bank](silicon-valley-bank.md) | finance/banking (US) | financial_management, governance_and_leadership |
| [evergrande](evergrande.md) | real estate (China) | financial_management, scaling_too_fast, governance_and_leadership |
| [wirecard](wirecard.md) | fintech/payments (Germany) | fraud_and_ethics, governance_and_leadership |
| [satyam](satyam.md) | IT services (India) | fraud_and_ethics, governance_and_leadership |
| [steinhoff](steinhoff.md) | retail conglomerate (South Africa) | fraud_and_ethics, governance_and_leadership |
| [boeing-737-max](boeing-737-max.md) | aerospace/manufacturing (US) | safety_and_quality, culture_and_talent, governance_and_leadership |
| [hih-insurance](hih-insurance.md) | insurance (Australia) | governance_and_leadership, financial_management, fraud_and_ethics |
| [odebrecht](odebrecht.md) | construction/engineering (Brazil) | fraud_and_ethics, governance_and_leadership |

## Failure type taxonomy

- **fraud_and_ethics** — faked results, hid losses, misused customer/investor funds (Enron, Theranos, FTX, Katerra, Fusionex, Luckin Coffee, Wirecard, Satyam, Steinhoff, HIH Insurance, Odebrecht)
- **governance_and_leadership** — no real checks on founder/CEO, board can't or won't push back, indecisive or conflicted leadership (WeWork, FTX, Yahoo, Nokia, BlackBerry, Katerra, Lehman, Fusionex, Silicon Valley Bank, Evergrande, Wirecard, Satyam, Steinhoff, Boeing 737 MAX, HIH Insurance, Odebrecht)
- **financial_management** — bad debt/leverage, negative unit economics, cash burn with no path to breakeven (Lehman, Toys R Us, Sears, Pets.com, Webvan, Juicero, Katerra, Fusionex, Silicon Valley Bank, Evergrande, HIH Insurance)
- **disruption_denial** — saw the shift coming (or invented it) and protected the legacy business instead (Kodak, Blockbuster, Nokia, Sears, Borders, BlackBerry, Toys R Us, Circuit City, MySpace)
- **product_market_fit** — built/scaled before proving anyone actually wanted it at that price/format (Quibi, Pets.com, Webvan, Juicero, Segway, Theranos, MySpace, Yahoo)
- **scaling_too_fast** — grew headcount/locations/capital deployment ahead of proven, repeatable unit economics (WeWork, Webvan, Pets.com, Katerra, Kenny Rogers Roasters, Luckin Coffee, Evergrande)
- **culture_and_talent** — internal culture suppressed dissent, punished honesty, or cost-cut away the thing that made the company win (Enron, Kodak, Nokia, Sears, Borders, Circuit City, MySpace, BlackBerry, Yahoo, Boeing 737 MAX)
- **safety_and_quality** — cut corners on product/service safety or quality to save cost or time (Boeing 737 MAX)

## Contrast cases (`cases/contrasts/`)

Not every company that saw a disruption coming failed to respond — it's worth reading the failure
next to the company that faced the *same* shift and adapted, to see what a real response looks
like versus a token one:

- [netflix-pivot](contrasts/netflix-pivot.md) — contrasts directly with [blockbuster](blockbuster.md): same disruption (DVD rental → streaming), opposite response.

These use a different, lighter frontmatter schema (no `severity`/`failed` fields) and are excluded from `scripts/validate_cases.py`, which only validates `cases/*.md`.

## Geographic coverage

Cases span the US, Canada, Finland, Germany, India, South Africa, China, Malaysia, Australia,
and Brazil — most of these failure mechanisms aren't specific to one country's business culture.
If you know a well-documented case from a region not yet covered here, see
[CONTRIBUTING.md](../CONTRIBUTING.md).

## Method & limitations

These are pattern-matching prompts for reflection, not predictions. Survivorship bias applies:
plenty of companies exhibited one or two of these warning signs and survived anyway. Treat a
match as "worth investigating," never as "this means we will fail." See the root disclaimer in
the repo [README](../README.md#how-to-read-these-cases).


---

<!-- ==== CHECKLIST.md ==== -->

# Self-Audit Checklist

English | [简体中文](CHECKLIST.zh-CN.md)

A distilled version of the "Questions this raises for another company" from every case in
`cases/`, grouped by failure mechanism. Meant for periodic self-review (quarterly board meeting,
before a big raise/hire/expansion decision) rather than a one-time chat with the skill. If you
answer "yes, that's a risk" to several items in one section, go read the linked cases for that
section in full — they'll be more specific than the checklist item.

None of these are pass/fail. They're prompts to investigate. See the
[method & limitations note](cases/_index.md#method--limitations) before treating any "yes" as a
verdict.

## Fraud & ethics
_See: [enron](cases/enron.md), [theranos](cases/theranos.md), [ftx](cases/ftx.md), [katerra](cases/katerra.md), [fusionex](cases/fusionex.md), [luckin-coffee](cases/luckin-coffee.md), [wirecard](cases/wirecard.md), [satyam](cases/satyam.md), [steinhoff](cases/steinhoff.md), [hih-insurance](cases/hih-insurance.md), [odebrecht](cases/odebrecht.md)_

- [ ] Can an outside expert independently verify our core technical/financial claim, or is it only internal say-so?
- [ ] Are we, our auditors, or our board financially incentivized to not look too closely at our own numbers?
- [ ] If a customer/client/investor asked for a full, honest audit tomorrow, could we produce clean records immediately?
- [ ] Do people who raise uncomfortable questions get heard, or get sidelined/fired?
- [ ] Is there any structure where funds held for someone else (customers, clients) could be used for our own operations, even informally?
- [ ] Is there pressure on any team to hit a growth/sales number that only makes sense if part of it is manufactured rather than real?
- [ ] Are the same handful of related counterparties or entities showing up across multiple of our transactions?
- [ ] Do we have an unusually high win-rate on competitive bids or deals that we've never honestly examined the reason for?

## Governance & leadership
_See: [wework](cases/wework.md), [ftx](cases/ftx.md), [yahoo](cases/yahoo.md), [nokia-mobile](cases/nokia-mobile.md), [blackberry](cases/blackberry.md), [lehman-brothers](cases/lehman-brothers.md), [fusionex](cases/fusionex.md), [evergrande](cases/evergrande.md), [wirecard](cases/wirecard.md), [satyam](cases/satyam.md), [steinhoff](cases/steinhoff.md), [hih-insurance](cases/hih-insurance.md), [odebrecht](cases/odebrecht.md)_

- [ ] Does any single individual have effectively unchecked control, and can the board actually say no to them?
- [ ] Are there transactions where a founder/executive personally benefits at the company's expense?
- [ ] Does our board have anyone who can meaningfully challenge leadership on substance, not just vision?
- [ ] Has our strategic direction changed multiple times recently without any version being given time to actually work?
- [ ] Is critical operational knowledge (passwords, contracts, key relationships) concentrated in one or two people who could walk away with it?
- [ ] When credible outside critics raise specific concerns, is our first instinct to investigate the claim or discredit the accuser?

## Financial management
_See: [lehman-brothers](cases/lehman-brothers.md), [toys-r-us](cases/toys-r-us.md), [sears](cases/sears.md), [pets-com](cases/pets-com.md), [webvan](cases/webvan.md), [juicero](cases/juicero.md), [katerra](cases/katerra.md), [silicon-valley-bank](cases/silicon-valley-bank.md), [evergrande](cases/evergrande.md), [hih-insurance](cases/hih-insurance.md)_

- [ ] If our single largest revenue source dropped 20-30% in value/volume, would we still be solvent?
- [ ] Does each unit/order we sell actually make money once fully-loaded costs are included — or are we hoping "scale will fix it"?
- [ ] If external funding dried up tomorrow, how many months could we survive?
- [ ] Is our debt load sized to what the business can service even under sustained competitive pressure?
- [ ] Are we pulling capital out of the business (dividends, buybacks, distributions) faster than we reinvest in what keeps customers coming back?
- [ ] Is a large share of our deposits/customers/revenue concentrated in one tightly networked community that could all move in the same direction at once?
- [ ] Are we using customer deposits/prepayments as working capital for something other than what they were paid for?
- [ ] Is there a real delay between a decision we make today and when its true cost becomes visible — and are we accounting for that lag?

## Disruption denial
_See: [kodak](cases/kodak.md), [blockbuster](cases/blockbuster.md), [nokia-mobile](cases/nokia-mobile.md), [sears](cases/sears.md), [borders](cases/borders.md), [blackberry](cases/blackberry.md), [circuit-city](cases/circuit-city.md)_

- [ ] Do we have an internal idea/prototype that threatens our main revenue line — and if so, who decided to shelve it, and why?
- [ ] Are we protecting this quarter's profit at the cost of being relevant in five years?
- [ ] Is a competitor winning on a dimension (price, convenience, simplicity) we've stopped prioritizing?
- [ ] Have we outsourced any capability to a partner who could become our biggest competitor once they've learned our business?
- [ ] Is any part of our revenue model something customers openly resent, and are we protecting it instead of fixing it?

## Product-market fit
_See: [quibi](cases/quibi.md), [pets-com](cases/pets-com.md), [webvan](cases/webvan.md), [juicero](cases/juicero.md), [segway](cases/segway.md), [theranos](cases/theranos.md), [myspace](cases/myspace.md)_

- [ ] Have we validated the core assumption behind our product with real, unpaid user behavior — or only with funding and press?
- [ ] Does our product have any organic/viral growth loop, or does every user require a paid acquisition dollar?
- [ ] Could our core value proposition be replicated by something drastically simpler or cheaper — have we actually tested that?
- [ ] Is our price point matched to the actual value/problem being solved for the everyday buyer?
- [ ] Is our confidence in demand based on real customer behavior, or on how impressive the technology/story seems to us and investors?

## Scaling too fast
_See: [wework](cases/wework.md), [webvan](cases/webvan.md), [pets-com](cases/pets-com.md), [katerra](cases/katerra.md), [kenny-rogers-roasters](cases/kenny-rogers-roasters.md), [luckin-coffee](cases/luckin-coffee.md), [evergrande](cases/evergrande.md)_

- [ ] Have we proven the model is profitable in one location/segment before replicating the fixed-cost investment elsewhere?
- [ ] Is our expansion pace set by what the data says is working, or by external/investor pressure to grow fast?
- [ ] Are we scaling into multiple new business lines simultaneously before proving profitability in even one?
- [ ] Do we have the operational capacity to actually integrate everything we've acquired or launched?

## Culture & talent
_See: [kodak](cases/kodak.md), [nokia-mobile](cases/nokia-mobile.md), [sears](cases/sears.md), [borders](cases/borders.md), [circuit-city](cases/circuit-city.md), [myspace](cases/myspace.md), [boeing-737-max](cases/boeing-737-max.md)_

- [ ] If we cut costs by removing our most experienced people, are we also cutting away the reason customers choose us?
- [ ] Do bad-news signals reach leadership honestly and quickly, or get softened on the way up?
- [ ] Is our organizational culture built around obsessing over the product/customer, or around extracting revenue from an existing asset?
- [ ] Would our best customers notice, and be upset, by a cost cut we're considering?
- [ ] Do employees privately raise safety/quality/ethical concerns that never surface through official channels?

## Safety & quality
_See: [boeing-737-max](cases/boeing-737-max.md)_

- [ ] Are we making a safety- or quality-related decision specifically to avoid a disclosure, approval, or training requirement — rather than to make the product genuinely safer or better?
- [ ] Does any critical system or process rely on a single point of failure that someone has already flagged as risky?
- [ ] Is our team effectively self-certifying its own safety/quality claims, with no truly independent check?
- [ ] Is competitor or schedule pressure driving a shortcut on safety or quality we wouldn't normally take?


---

<!-- ==== cases/blackberry.md ==== -->

---
slug: blackberry
company: BlackBerry (RIM)
industry: tech/hardware
founded: 1984
failed: 2013-2016 (exited hardware business)
failure_types: [disruption_denial, culture_and_talent, governance_and_leadership]
severity: acquired_in_distress
---

## What happened
BlackBerry dominated the smartphone market for enterprise/business users with its physical keyboard and secure email. After the iPhone (2007) and Android redefined smartphones around touchscreens and consumer apps, BlackBerry's co-CEOs publicly dismissed the iPhone as a fad and a security/battery-life risk, kept betting on keyboards and enterprise features, and lost its market position within a few years, eventually exiting hardware entirely.

## Root causes
- Leadership's deep confidence in what had made them successful (security, keyboard, enterprise IT relationships) blinded them to a redefinition of the category around consumer experience and apps.
- Dual co-CEO structure reportedly slowed decisive strategic response, with disagreement about how seriously to take the touchscreen threat.
- Underestimated how much the buying decision would shift from IT departments (BlackBerry's stronghold) to individual consumers (bring-your-own-device), which undercut their core distribution advantage.
- Software/app ecosystem investment lagged years behind competitors, so even later touchscreen models couldn't match the user experience.

## Warning signs (visible before the collapse)
- Public leadership statements dismissing a category-redefining competitor's product as inferior or a fad.
- Continued doubling down on the previous generation's winning formula (keyboard, enterprise security) after the market's buying criteria visibly shifted.
- The core distribution channel/buyer (corporate IT) starting to lose influence to a new one (individual consumers) without a strategic response.
- App/software ecosystem gap versus competitors widening every year without being treated as the central problem.

## Questions this raises for another company
- Are we dismissing a new competitor's approach because it's genuinely inferior, or because it threatens what we're good at?
- Is our core buyer/channel losing influence to a different decision-maker (e.g., IT to end-user), and are we adapting our go-to-market accordingly?
- Are we doubling down on our historical strength even as the market's criteria for winning changes?
- Does our leadership structure allow for fast, decisive strategic pivots, or does it produce delay through consensus-seeking?

## Sources
- [How BlackBerry Lost the Smartphone War — Medium](https://medium.com/@celestineriza/how-blackberry-lost-the-smartphone-war-fbc9d121412a)
- [BlackBerry's Collapse: How Security Phones Missed the Touchscreen Revolution — Headcount Coffee](https://www.headcountcoffee.com/blogs/corporate-legends-lost-empires/blackberry-s-collapse-how-security-phones-missed-the-touchscreen-revolution)


---

<!-- ==== cases/blockbuster.md ==== -->

---
slug: blockbuster
company: Blockbuster
industry: retail/media
founded: 1985
failed: 2010
failure_types: [disruption_denial, product_market_fit]
severity: bankruptcy
---

## What happened
Blockbuster passed on the chance to buy Netflix for $50M in 2000, dismissing DVD-by-mail/streaming as a niche. It kept optimizing its late-fee-driven, brick-and-mortar rental model until Netflix and Redbox made it irrelevant; Blockbuster filed for bankruptcy in 2010.

## Root causes
- Revenue model (late fees) actively conflicted with what customers actually wanted (convenience, no fees), so fixing the customer pain point meant cannibalizing existing profit.
- Leadership evaluated a disruptive competitor using the old business's metrics (store traffic, late-fee revenue) instead of the new model's trajectory.
- Late, half-hearted digital response (a rebranded "Total Access" and streaming attempt) came years after the market had already moved, and was hobbled by an unwillingness to fully abandon stores.
- Heavy fixed costs in physical real estate made the eventual pivot financially harder every year it was delayed.

## Warning signs (visible before the collapse)
- A core revenue stream that customers openly resent (late fees became a punchline).
- A direct, cheaper, more convenient competitor growing steadily while being publicly dismissed as "not a real threat."
- Internal digital initiatives launched underfunded, late, and clearly reactive rather than a genuine strategic bet.
- Store growth/optimization continuing even as foot traffic and rental volume trends started softening.

## Questions this raises for another company
- Is any part of our revenue model something customers resent, and are we protecting it instead of fixing it?
- Are we judging an upstart competitor by our own scoreboard instead of theirs?
- If we had to compete against a "better, cheaper, more convenient" version of ourselves starting today, could our current cost structure survive?
- Is our response to a new competitor a genuine bet, or a defensive press release?

## Sources
- [Blockbuster 'laughed us out of the room,' recalls Netflix cofounder — Fortune](https://fortune.com/2023/04/14/netflix-cofounder-marc-randolph-recalls-blockbuster-rejecting-chance-to-buy-it/)
- [Fact Check: Did Blockbuster Turn Down Chance to Buy Netflix for $50 Million — Newsweek](https://www.newsweek.com/fact-check-did-blockbuster-turn-down-chance-buy-netflix-50-million-1575557)


---

<!-- ==== cases/boeing-737-max.md ==== -->

---
slug: boeing-737-max
company: Boeing (737 MAX program)
industry: aerospace/manufacturing
founded: 1916 (737 MAX launched 2016)
failed: 2018-2019 (crashes and worldwide grounding)
failure_types: [safety_and_quality, culture_and_talent, governance_and_leadership]
severity: shutdown
---

## What happened
To compete quickly with Airbus's new fuel-efficient A320neo, Boeing rushed the 737 MAX to market by fitting larger engines onto its decades-old 737 airframe, which changed the plane's handling characteristics. To avoid costly pilot retraining and keep the plane certified as "just another 737," Boeing added a software system (MCAS) that automatically pushed the nose down based on a single angle-of-attack sensor, and did not disclose its existence to pilots. Two planes crashed within five months — Lion Air in October 2018 (189 dead) and Ethiopian Airlines in March 2019 (157 dead) — both traced to MCAS misfiring on faulty sensor data. The entire global fleet was grounded for about 20 months, costing Boeing over $20 billion.

## Root causes
- Commercial pressure to match a competitor's timeline and avoid pilot-retraining costs drove a design choice (hide a new flight-control system rather than disclose and train for it) that prioritized schedule and cost over a full safety case.
- MCAS relied on a single angle-of-attack sensor with no redundancy, despite engineers reportedly flagging the risk of relying on one sensor for a system with this much control authority.
- The FAA had delegated large parts of the safety certification process to Boeing itself (a self-certification model), removing an independent check exactly where one mattered most.
- Internal culture reportedly shifted over years toward emphasizing financial performance and shareholder returns, with safety/engineering concerns escalated less forcefully as a result — documented later in internal communications and congressional investigations.

## Warning signs (visible before the collapse)
- A safety-critical new system built to avoid disclosure/training requirements rather than to be independently and fully evaluated on its own merits.
- Single point of failure (one sensor) in a system with significant control authority over the aircraft, despite internal engineering concern about exactly this risk.
- A regulator relying on the manufacturer's own engineers to certify safety-critical systems, rather than independent verification.
- Internal communications later revealed employees privately joking about or expressing concern over the plane's safety and the certification process, while the company's public position remained confident.

## Questions this raises for another company
- Are we making a safety- or quality-critical design/process decision specifically to avoid a disclosure, training, or approval requirement, rather than to make the product actually safer?
- Does any critical system rely on a single point of failure that an engineer has already flagged as risky?
- Is our own team effectively self-certifying its own safety/quality claims, with no truly independent check?
- Do employees privately express safety or quality concerns that never surface in official channels or leadership's public confidence?
- Is schedule or cost pressure from a competitor's timeline driving a shortcut on safety or quality that we wouldn't take under normal circumstances?

## Sources
- [Boeing 737 MAX groundings — Wikipedia](https://en.wikipedia.org/wiki/Boeing_737_MAX_groundings)
- [The Boeing 737 MAX: Lessons for Engineering Ethics — PMC/National Institutes of Health](https://pmc.ncbi.nlm.nih.gov/articles/PMC7351545/)
- [Case Study: The $20 Billion Boeing 737 Max Disaster — Henrico Dolfing](https://www.henricodolfing.com/2024/08/case-study-19-20-billion-boeing-737-max.html)


---

<!-- ==== cases/borders.md ==== -->

---
slug: borders
company: Borders Group
industry: retail
founded: 1971
failed: 2011
failure_types: [disruption_denial, culture_and_talent]
severity: bankruptcy
---

## What happened
Borders outsourced its online bookselling entirely to Amazon in 2001, believing e-commerce was a distraction from its core physical-superstore strategy. It later tried to build its own e-commerce and e-reader capability far too late, entered digital music/DVD instead of doubling down on core books, and filed for bankruptcy in 2011, closing all stores.

## Root causes
- Handing its entire online channel to the very competitor (Amazon) that would go on to dominate the category eliminated any chance of building in-house digital capability when it still had time to.
- Strategic focus stayed on expanding physical superstore square footage even as reading and retail habits were visibly shifting online.
- Diversified into adjacent physical media (music, DVDs) at exactly the moment those categories were also being disrupted digitally, rather than investing in e-books/e-readers.
- Heavy real-estate lease obligations from the superstore expansion strategy became a fixed-cost anchor once sales began declining.

## Warning signs (visible before the collapse)
- Core strategic capability (e-commerce) contracted out to a direct competitor rather than built internally.
- Continued physical footprint expansion after signs that the category's growth was moving online.
- New investment directed at categories (physical music/DVD) already showing digital disruption elsewhere, rather than the company's own core digital gap.
- A widening gap versus a competitor (Amazon, then Kindle) building the exact capability the company had chosen to skip.

## Questions this raises for another company
- Have we outsourced any capability to a partner who could become our biggest competitor once they've learned our business?
- Are we still expanding in a direction (e.g., physical footprint) that the market has already started moving away from?
- Are we investing in adjacent categories facing the same disruption risk, instead of fixing our own core gap?
- Do our fixed obligations (leases, contracts) reduce our ability to pivot fast if the market shifts?

## Sources
- [Borders Collapse: How a Bookstore Giant Missed the Digital Shift — Headcount Coffee](https://www.headcountcoffee.com/blogs/corporate-legends-lost-empires/the-fall-of-borders-books-how-a-retail-giant-outsourced-itself-to-death)
- [Why Borders Failed While Barnes & Noble Survived — NPR](https://www.npr.org/2011/07/19/138514209/why-borders-failed-while-barnes-and-noble-survived)


---

<!-- ==== cases/circuit-city.md ==== -->

---
slug: circuit-city
company: Circuit City
industry: retail
founded: 1949
failed: 2009
failure_types: [culture_and_talent, financial_management, disruption_denial]
severity: bankruptcy
---

## What happened
In 2007, facing margin pressure, Circuit City fired around 3,400 of its most experienced (and highest-paid) sales associates and replaced them with cheaper, less experienced staff — a decision widely credited with gutting the knowledgeable customer service that had differentiated it from big-box rivals. Combined with underinvestment in stores and slow response to Best Buy and online retail, Circuit City filed for bankruptcy in 2008 and fully liquidated in 2009.

## Root causes
- Cost-cutting targeted the exact asset (experienced, knowledgeable sales staff) that created customer loyalty and differentiated the company from lower-cost competitors, trading short-term payroll savings for long-term customer experience damage.
- Chronic underinvestment in store environment and format modernization left stores looking dated relative to Best Buy's newer format.
- Leadership treated payroll as a pure cost line to optimize rather than as an investment tied to the core value proposition (expert help with electronics purchases).
- Slow, inconsistent strategic responses to a strengthening competitor (Best Buy) and to online retail's emergence.

## Warning signs (visible before the collapse)
- A cost-cutting decision that directly removed the thing customers said they valued most about the company.
- Employee morale and customer service quality visibly declining right after a "cost savings" initiative.
- Store format and experience falling visibly behind the primary competitor without a serious refresh plan.
- Financial performance treated as a payroll/cost problem rather than a value-proposition/differentiation problem.

## Questions this raises for another company
- If we cut costs by removing our most experienced people, are we also cutting away the reason customers choose us?
- Are we treating an underperformance problem as a cost issue when it might actually be a differentiation issue?
- Is our physical/product experience falling visibly behind a direct competitor's, and do we have a real refresh plan?
- Would our best customers notice, and be upset, if we made this cost cut?

## Sources
- [Circuit City Cuts 3,400 'Overpaid' Workers — Washington Post](https://www.washingtonpost.com/archive/business/2007/03/29/circuit-city-cuts-3400-overpaid-workers/a67a22c6-0416-4a50-9a40-398a0bf85a02/)
- [What Happened to Circuit City? — WhatJobs News](https://www.whatjobs.com/news/what-happened-to-circuit-city/)


---

<!-- ==== cases/enron.md ==== -->

---
slug: enron
company: Enron
industry: energy/finance
founded: 1985
failed: 2001
failure_types: [fraud_and_ethics, governance_and_leadership, financial_management]
severity: bankruptcy, fraud_conviction
---

## What happened
Enron used mark-to-market accounting and off-balance-sheet special purpose entities to hide billions in debt and fabricate profits. When the scheme unraveled in 2001, the company collapsed within weeks, wiping out $74B in shareholder value and employees' retirement savings.

## Root causes
- Compensation and culture rewarded reported earnings growth over real cash generation, so managers were incentivized to manufacture numbers rather than flag problems.
- Board and auditor (Arthur Andersen) were structurally conflicted — auditors also did lucrative consulting work for the client they were supposed to police.
- A "rank and yank" internal culture punished dissent and whistleblowing, so early warnings didn't reach the top.
- Complexity (thousands of subsidiaries/SPEs) was used deliberately to make the business impossible to scrutinize from outside.

## Warning signs (visible before the collapse)
- Reported earnings that consistently beat guidance despite an opaque, hard-to-explain business model.
- Heavy reliance on related-party transactions and entities run by the company's own CFO.
- Aggressive, publicly celebrated culture of "smartest guys in the room" — low tolerance for internal challenge.
- Auditor independence compromised by non-audit fees.

## Questions this raises for another company
- Are we (or our auditors/board) financially incentivized to not look too closely at our own numbers?
- Can any single executive explain our financial structure in plain language, or does it require specialists to untangle?
- Do people who raise uncomfortable questions get promoted, ignored, or pushed out?
- Would our reported growth still look believable if a skeptical outsider audited it line by line?

## Sources
- [Enron scandal — Wikipedia](https://en.wikipedia.org/wiki/Enron_scandal)
- [Enron scandal — Britannica](https://www.britannica.com/event/Enron-scandal)
- [Enron — FBI](https://www.fbi.gov/history/cases-and-criminals/enron)


---

<!-- ==== cases/evergrande.md ==== -->

---
slug: evergrande
company: China Evergrande Group
industry: real estate (China)
founded: 1996
failed: 2021 (default), 2024 (liquidation ordered)
failure_types: [financial_management, scaling_too_fast, governance_and_leadership]
severity: bankruptcy
---

## What happened
Evergrande grew into China's second-largest property developer by borrowing heavily to fund land purchases and construction across hundreds of projects in 200+ cities, while also expanding into unrelated businesses (electric vehicles, theme parks, a football club). When Chinese regulators introduced debt limits ("three red lines") in 2020, Evergrande couldn't refinance its way out of over $300 billion in liabilities. It defaulted on dollar bonds in December 2021 — the largest-ever dollar-bond default by an Asian company — and a Hong Kong court ordered its liquidation in January 2024.

## Root causes
- Business model depended on continuously raising new debt to fund new projects, using presale deposits from homebuyers on unfinished units as working capital — a structure that only works as long as growth (and new buyer deposits) never slows down.
- Diversified into capital-intensive, unrelated businesses (EVs, theme parks) using cash that a highly leveraged core business couldn't spare, spreading risk across ventures with no track record.
- Grew past all three of the regulator's own leverage thresholds (debt-to-cash, debt-to-equity, debt-to-assets) — the company's own numbers showed the danger before the external shock hit.
- When financing conditions tightened, there was no fallback: the whole structure assumed uninterrupted access to new capital forever.

## Warning signs (visible before the collapse)
- Debt ratios exceeding every one of a regulator's own published risk thresholds, for a company that size, for years.
- Presale/deposit-funded construction model with a large gap between homes sold (and paid for) and homes actually delivered.
- Rapid unrelated diversification (EVs, entertainment, sports) funded by a core business that was already highly leveraged.
- Heavy reliance on the assumption that credit markets and government policy would stay accommodating indefinitely.

## Questions this raises for another company
- Are we using customer deposits or prepayments as working capital for unrelated growth, rather than holding them against the specific obligation they were paid for?
- Do we know exactly where we sit against any leverage/risk thresholds a regulator, lender, or our own board has set — and are we already past them?
- Are we diversifying into ventures with no proven track record, funded by a core business that itself carries a lot of debt?
- Does our entire growth model assume that credit will always be available on the same terms it is today?

## Sources
- [Chinese property sector crisis (2020–present) — Wikipedia](https://en.wikipedia.org/wiki/Chinese_property_sector_crisis_(2020%E2%80%93present))
- [What is the Evergrande debt crisis and why does it matter for the global economy? — World Economic Forum](https://www.weforum.org/stories/2021/09/evergrande-debt-crisis-global-economy/)
- [China developer Evergrande: debt crisis, bond default and investor risks — CNBC](https://www.cnbc.com/2021/09/17/china-developer-evergrande-debt-crisis-bond-default-and-investor-risks.html)


---

<!-- ==== cases/ftx.md ==== -->

---
slug: ftx
company: FTX
industry: crypto/finance
founded: 2019
failed: 2022
failure_types: [fraud_and_ethics, governance_and_leadership, financial_management]
severity: bankruptcy, fraud_conviction
---

## What happened
FTX, a crypto exchange, secretly funneled billions of dollars of customer deposits to its affiliated trading firm Alameda Research to cover Alameda's losses and fund risky bets and lavish spending. When a liquidity crunch triggered a wave of withdrawals in November 2022, FTX couldn't return customer funds and collapsed within days; its founder was later convicted of fraud.

## Root causes
- No real separation between the exchange (holding customer funds) and its affiliated trading firm (Alameda) — customer deposits were used as trading capital, a fundamental breach of custodial responsibility.
- Governance was essentially nonexistent: no real board oversight, no CFO with independent authority, financial records reportedly tracked informally.
- Leadership operated with a "we're smarter than the rules" culture, treating basic financial controls as unnecessary friction.
- Extreme concentration of decision-making and asset control in one or two individuals with no independent checks.

## Warning signs (visible before the collapse)
- A company holding customer/client funds that also runs its own trading operation using related capital — a structural conflict of interest.
- Absence of conventional corporate controls (independent board, real CFO, audited financials) despite handling billions of dollars.
- Public reporting/rumors of extremely close financial ties between "separate" entities under common ownership.
- Culture that publicly downplayed the importance of conventional compliance/audit processes as old-fashioned.

## Questions this raises for another company
- Do we have any structure where funds held on behalf of customers/clients could be used for our own operations, even informally?
- Do we have real, independent financial oversight (board, CFO, audit), or does one person effectively control everything?
- Are we treating standard financial controls as bureaucratic friction rather than as protection against catastrophic failure?
- If customers/clients all asked for their money back tomorrow, could we actually return it?

## Sources
- [Bankruptcy of FTX — Wikipedia](https://en.wikipedia.org/wiki/Bankruptcy_of_FTX)
- [Samuel Bankman-Fried Sentenced to 25 Years — U.S. Department of Justice](https://www.justice.gov/archives/opa/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes)


---

<!-- ==== cases/fusionex.md ==== -->

---
slug: fusionex
company: Fusionex
industry: tech/data analytics
founded: 2005
failed: 2023-2024 (liquidation)
failure_types: [governance_and_leadership, financial_management, fraud_and_ethics]
severity: bankruptcy
---

## What happened
Fusionex, a Malaysian big-data analytics firm founded by Ivan Teh, grew from a London Stock Exchange listing (2013, oversubscribed 3x, raised RM500M) to being acquired by Hitachi for RM545M in 2020. In March 2023 Hitachi requested an internal audit; Fusionex management refused to hand over financial records, citing data-access restrictions. Months later the company announced layoffs, Ivan Teh demanded a USD150M emergency capital injection from Hitachi, and by December 2023 the company was in liquidation with the entire C-suite resigning abruptly without handing over documents, passwords, or records. Court-appointed liquidators later found evidence of business/client diversion to other entities before the collapse and an unpaid RM22.3M debt to Hitachi.

## Root causes
- Under new ownership (Hitachi), the founder-led management retained effective operational control and refused normal audit/oversight, so financial problems went undetected for over three years post-acquisition.
- Spending flowed to related third-party vendors for vague "technology fees" and "software development costs," inflating the burn rate without transparent justification.
- No real handover/succession plan existed — when leadership resigned, they left without documents, passwords, or records, suggesting governance had never been institutionalized beyond the founder.
- Liquidators found signs that parts of the business (client accounts, projects) may have been quietly diverted to other entities before the collapse.

## Warning signs (visible before the collapse)
- A parent/acquirer requesting a routine audit and being refused or stonewalled by the operating management it had bought.
- Sudden, unexplained demand for a large emergency capital injection with no clear accounting for prior spending.
- Heavy reliance on payments to related or opaque third-party vendors rather than transparent, itemized costs.
- Mass, abrupt C-suite resignations with no transition — a strong signal that leadership expected imminent exposure rather than a fixable problem.

## Questions this raises for another company
- If our parent company/board/investor asked for a full audit tomorrow, could we produce clean records immediately — or would there be resistance?
- Do we have significant spending flowing to vendors or entities connected to our own leadership, and is it itemized and justified?
- Is critical operational knowledge (passwords, contracts, financial records) concentrated in one or two people who could walk away and take it with them?
- Would a client or revenue stream just... disappear if leadership left tomorrow, because it was never really institutionalized?

## Sources
- [Fusionex: Rise and Collapse — The Runway Ventures](https://www.therunway.ventures/p/fusionex)
- [Fusionex liquidators probing alleged diversion of business to third parties — The Edge Malaysia](https://theedgemalaysia.com/node/710771)
- [Hitachi court petition to wind up Fusionex — Digital News Asia](https://www.digitalnewsasia.com/business/hitachi-court-petition-wind-fusionex-reveal-grim-picture-alleged-unethical-and)


---

<!-- ==== cases/hih-insurance.md ==== -->

---
slug: hih-insurance
company: HIH Insurance
industry: insurance (Australia)
founded: 1968
failed: 2001
failure_types: [governance_and_leadership, financial_management, fraud_and_ethics]
severity: bankruptcy, fraud_conviction
---

## What happened
HIH was Australia's second-largest general insurer before it was placed into provisional liquidation in March 2001, in what remains the largest corporate collapse in Australian history, with losses eventually estimated at up to A$5.3 billion. The company had systematically underpriced insurance risk to win market share, made a large acquisition (FAI Insurance) that turned out to be far weaker than represented, and used aggressive accounting to understate its liabilities (reserves it would eventually need to pay out on claims) for years. A board with plenty of relevant expertise nonetheless failed to challenge a dominant CEO, and several executives were later convicted of related offenses.

## Root causes
- Chronic underpricing of insurance policies to win business meant the company was collecting premiums that were, in aggregate, not enough to cover the claims they would eventually have to pay — a slow-motion insolvency that took years to surface because insurance claims are paid out long after premiums are collected.
- A major acquisition (FAI) was completed without adequately verifying the target's true financial condition, importing a much bigger reserving problem than disclosed.
- Aggressive/optimistic reserving (understating how much the company would eventually owe policyholders) flattered short-term profit at the direct expense of long-term solvency.
- Board included experienced insurance and accounting professionals, but deferred heavily to a dominant CEO and did not exercise independent challenge on the specific numbers that mattered most (reserve adequacy).

## Warning signs (visible before the collapse)
- Pricing that was persistently and noticeably below what competitors charged for comparable risk, sustained over years — profitable-looking growth that is actually accumulating future losses.
- A major acquisition completed on the acquirer's own optimistic assessment rather than independent, rigorous due diligence of the target's real financial position.
- A board with real technical expertise that nonetheless didn't independently push back on the CEO's numbers — expertise on paper doesn't guarantee genuine oversight in practice.
- A business model (insurance) where the true cost of decisions made today (how much risk to write, at what price) isn't visible for years — a structural reason to distrust short-term profit signals alone.

## Questions this raises for another company
- Are we winning business by pricing below what the underlying risk or cost actually justifies, and would we know if we were?
- Did we verify a major acquisition's true financial condition independently, or trust the numbers we were given going into the deal?
- Does our board have genuine technical expertise AND the independence to challenge leadership's specific numbers — or just the former?
- Is there a meaningful delay between a decision we make today and when its true cost becomes visible — and are we accounting for that lag, or just looking at today's profit?

## Sources
- [HIH Insurance — Wikipedia](https://en.wikipedia.org/wiki/HIH_Insurance)
- [Case Study on Corporate Governance Failures: The Collapse of HIH Insurance — MBA Knowledge Base](https://mbaknol.com/business-ethics/case-study-on-corporate-governance-failures-the-collapse-of-hih-insurance/)
- [HIH Insurance Group — Australia's biggest corporate collapse](https://www.hihsupport.com.au/hih-insurance-group/)


---

<!-- ==== cases/juicero.md ==== -->

---
slug: juicero
company: Juicero
industry: hardware/consumer tech
founded: 2013
failed: 2017
failure_types: [product_market_fit, financial_management]
severity: shutdown
---

## What happened
Juicero raised $120M to build a $400 Wi-Fi-connected juicer that squeezed proprietary produce packs (sold via subscription). Journalists discovered in 2017 that the packs could be squeezed by hand just as effectively (and faster) without the machine, destroying the product's core value proposition; the company shut down months later.

## Root causes
- Enormous engineering effort and capital went into a mechanically over-engineered solution to a problem (juicing a bag) that didn't require that much force or complexity — the machine was solving a problem more sophisticated than the actual task.
- Business model relied on razor/razor-blade lock-in (proprietary packs) for a product that could be trivially bypassed by hand, so the moat was illusory.
- Investors and leadership were reportedly seduced by the engineering sophistication and manufacturing precision, mistaking impressive engineering for customer value.
- No cheap/early real-world test (like literally asking "can this be done by hand?") was done before hundreds of millions were committed to hardware and manufacturing.

## Warning signs (visible before the collapse)
- A product whose core justification (a proprietary machine) could be trivially replicated by a simpler, cheaper alternative (human hands).
- Investment and press narrative focused heavily on engineering/manufacturing impressiveness rather than customer problem validation.
- High price point ($400 device + ongoing subscription) for a benefit (fresh juice) available more cheaply through many existing alternatives.
- Founders and investors reportedly aware internally that the packs could be hand-squeezed, but not treating it as an existential risk.

## Questions this raises for another company
- Could our core value proposition be replicated by something drastically simpler or cheaper — and if so, have we actually tested that?
- Are we impressed with our own engineering/production sophistication in a way that's substituting for real customer validation?
- Is our margin/business model dependent on a lock-in mechanism that's easy to bypass?
- Has anyone internally raised "a simpler alternative already does this" — and if so, what happened to that concern?

## Sources
- [Juicero — Wikipedia](https://en.wikipedia.org/wiki/Juicero)
- [The Downfall of Juicero: The Overhyped High-Tech Juicer — Codemotion](https://www.codemotion.com/magazine/dev-life/stories/the-downfall-of-juicero-the-overhyped-high-tech-juicer/)


---

<!-- ==== cases/katerra.md ==== -->

---
slug: katerra
company: Katerra
industry: construction/proptech
founded: 2015
failed: 2021
failure_types: [scaling_too_fast, governance_and_leadership, financial_management, fraud_and_ethics]
severity: bankruptcy
---

## What happened
Katerra raised over $2B (largely from SoftBank) with a vision to industrialize construction end-to-end — architecture, manufacturing, and building, all under one roof — expanding into dozens of business lines and acquiring numerous companies simultaneously. It struggled to integrate the acquisitions or make any single business line actually profitable, burned cash rapidly, and after falling short of projections reportedly presented its board with intentionally misstated financial reports. SoftBank gave a $200M rescue in late 2020, but once its own lender (Greensill) collapsed and no further cash came, Katerra filed for bankruptcy in June 2021.

## Root causes
- Attempted to vertically integrate and industrialize an entire complex industry (construction) all at once, rather than proving the model in one narrow segment first.
- Aggressive, investor-driven growth capital (large SoftBank checks) enabled scaling headcount, acquisitions, and factories far ahead of any proven, repeatable, profitable process.
- Integrating many disparate acquired companies and business lines simultaneously created enormous operational complexity that leadership could not manage effectively.
- Construction is a notoriously low-margin, execution-heavy, locally-regulated industry; the "move fast" software mentality applied here left little room for error and made mistakes very expensive (physical factories, real buildings).

## Warning signs (visible before the collapse)
- Enormous capital raised and deployed into rapid expansion across many business lines before unit economics were validated in any one of them.
- Growth funded primarily by a single large investor's conviction rather than by internally generated proof points.
- A string of leadership departures and reported cultural/operational instability accompanying the rapid scaling.
- An industry with structurally thin margins and high physical/regulatory execution risk being approached with a "blitzscale" software growth playbook.
- When results fell short of projections, financial reporting to the board was reportedly manipulated rather than the strategy being honestly reassessed.

## Questions this raises for another company
- Are we scaling into many new lines of business simultaneously before proving profitability in even one?
- Is our growth funded by conviction from one investor/backer rather than by our own internally validated economics?
- Does our industry have low margins and high execution risk that make "move fast and break things" a genuinely dangerous strategy?
- Do we have the operational capacity to actually integrate everything we've acquired or launched, or are we accumulating unmanaged complexity?
- When we miss our own projections, is the reporting to our board/investors honest, or softened/adjusted to look better than reality?

## Sources
- [SoftBank-Backed Katerra Files Bankruptcy With Billions in Debt — Bloomberg](https://www.bloomberg.com/news/articles/2021-06-07/softbank-backed-katerra-files-bankruptcy-with-billions-in-debt)
- [Katerra Bankruptcy: How SoftBank's American House of Cards Collapsed — Bloomberg Opinion](https://www.bloomberg.com/opinion/articles/2021-06-08/katerra-bankruptcy-how-softbank-s-american-house-of-cards-collapsed)
- [Softbank-backed Katerra's collapse is a failure of pattern-matching — Axios](https://www.axios.com/2021/06/08/katerra-bankruptcy-softbank)


---

<!-- ==== cases/kenny-rogers-roasters.md ==== -->

---
slug: kenny-rogers-roasters
company: Kenny Rogers Roasters (US operations)
industry: restaurant/franchise
founded: 1991
failed: 1998 (Chapter 11, US chain shrank from 425+ to near zero over the following decade)
failure_types: [scaling_too_fast, financial_management]
severity: bankruptcy
---

## What happened
Kenny Rogers Roasters, a rotisserie-chicken chain co-founded by singer Kenny Rogers, expanded rapidly to more than 425 restaurants in the U.S. by the mid-1990s. The pace of new-store openings outstripped the brand's ability to sustain per-store sales and manage the resulting overhead, and by March 1998 the company filed for Chapter 11 bankruptcy. It was sold to Nathan's Famous for a fraction of its former value, and the U.S. footprint kept shrinking to about 90 locations by the early 2000s and zero by 2011. (Separately, the brand was later relaunched in Asia by Malaysia's Berjaya Group and became a genuine success there — see below.)

## Root causes
- Store-count growth was treated as the primary success metric, without each new location proving it could sustain profitable sales on its own before the next batch was opened.
- Franchise/company-owned expansion added fixed overhead (leases, staffing, supply chain) faster than the brand's actual customer demand and repeat-visit rate could support.
- A single celebrity-driven brand concept saturated its addressable market (malls, shopping centers) faster than it could deepen loyalty in any one location.
- No clear signal was used to slow expansion — growth continued past the point where per-store economics were already softening.

## Warning signs (visible before the collapse)
- New location openings continuing at a fast pace while same-store sales or per-unit profitability weren't the headline metric being tracked or reported.
- Heavy reliance on a single differentiator (celebrity name, novelty of rotisserie concept) rather than deepening product/operations moat as competitors caught up.
- Growth funded in a way that assumed continued expansion, rather than treating each new store as needing to independently justify its own capital.

## Questions this raises for another company
- Are we opening new locations/hiring/expanding because the unit economics of our existing ones justify it, or because "more" is the current strategy by default?
- What's our actual per-location (or per-customer, per-branch) profitability trend, and is anyone tracking it as closely as total headcount/store count?
- Is our growth resting on one differentiator that a competitor or the market's novelty-fatigue could erode?
- Do we have a pre-agreed signal (e.g., three consecutive underperforming openings) that would make us pause expansion, or do we only find out in hindsight?

## A note on the "second life"
The same brand, under different ownership and market (Berjaya Group, Malaysia/Asia, starting 2008), succeeded with a more disciplined expansion pace and stronger repeat-customer fundamentals in a market where the concept was still novel. This is a useful reminder that the failure was about *execution pace and location economics*, not that "rotisserie chicken chains can't work" — the underlying concept was fine; the growth discipline wasn't there the first time.

## Sources
- [Kenny Rogers Roasters — Wikipedia](https://en.wikipedia.org/wiki/Kenny_Rogers_Roasters)
- [Whatever Happened to Kenny Rogers Roasters? — Reminisce](https://www.remindmagazine.com/article/34399/kenny-rogers-roasters-history-what-happened-to/)
- [The Untold Truth Of Kenny Rogers Roasters — Mashed](https://www.mashed.com/196806/the-untold-truth-of-kenny-rogers-roasters/)


---

<!-- ==== cases/kodak.md ==== -->

---
slug: kodak
company: Kodak
industry: manufacturing/tech
founded: 1888
failed: 2012
failure_types: [disruption_denial, culture_and_talent]
severity: bankruptcy
---

## What happened
Kodak's own engineer invented the first digital camera in 1975. The company shelved it to protect its enormously profitable film business, kept investing in film for another two decades, and filed for bankruptcy in 2012 once digital photography (and smartphones) made film nearly obsolete.

## Root causes
- The core business (film) was so profitable that any internal effort competing with it was starved of resources and support — a classic innovator's dilemma.
- Leadership treated digital as a threat to manage/delay rather than a future to lead, protecting near-term earnings over long-term relevance.
- Organizational identity was fused to "we are a chemical/film company," making it psychologically hard to bet the company on a different technology.
- By the time Kodak took digital seriously, competitors (Sony, Canon, later smartphone makers) had years of head start.

## Warning signs (visible before the collapse)
- Internal invention or evidence of a disruptive alternative that leadership actively deprioritized.
- Company messaging and investment continuing to emphasize the legacy product line long after market signals shifted.
- New technology initiatives housed in small, underfunded "innovation labs" disconnected from real budget or authority.
- Customers' adoption curve for the new technology visibly steepening while the company's product roadmap didn't change.

## Questions this raises for another company
- Do we have an internal idea or prototype that threatens our main revenue line — and if so, who decided to shelve it, and why?
- Are we protecting this quarter's profit at the cost of being relevant in five years?
- If a competitor built only the "threatening" alternative and nothing else, would they beat us within a decade?
- Is our innovation effort resourced like it matters, or is it a symbolic side project?

## Sources
- [Kodak — Wikipedia](https://en.wikipedia.org/wiki/Kodak)
- [How Kodak Failed — Forbes](https://www.forbes.com/sites/chunkamui/2012/01/18/how-kodak-failed/)
- [Kodak invented the first digital camera (and shelved it) — Slidebean](https://slidebean.com/story/first-kodak-digital-camera)


---

<!-- ==== cases/lehman-brothers.md ==== -->

---
slug: lehman-brothers
company: Lehman Brothers
industry: finance
founded: 1850
failed: 2008
failure_types: [financial_management, governance_and_leadership]
severity: bankruptcy
---

## What happened
Lehman leveraged itself over 30-to-1 to buy heavily into subprime mortgage-backed securities. When the housing market turned, the losses exceeded the firm's capital cushion and no buyer or bailout materialized; it filed the largest bankruptcy in U.S. history, triggering a global financial crisis.

## Root causes
- Extreme leverage meant a relatively small drop in asset values was enough to wipe out equity entirely.
- Concentrated bet on one asset class (real-estate-linked securities) with no meaningful hedge at the firm level.
- Risk management was subordinate to trading desks chasing short-term revenue and bonuses.
- Leadership dismissed internal risk warnings and doubled down on the same trade as the market started to crack.

## Warning signs (visible before the collapse)
- Leverage ratio far above peers, expanding even as the underlying market showed stress signals.
- Revenue increasingly concentrated in one product line rather than diversified.
- Internal risk officers reportedly overruled or sidelined by revenue-generating units.
- Competitors and short-sellers publicly questioning the marks on Lehman's real-estate book months before the collapse.

## Questions this raises for another company
- If our single largest revenue source dropped 20-30% in value, would we still be solvent?
- Does our risk/compliance function have the authority to actually stop a deal, or only to advise?
- Are we adding leverage or concentration because the fundamentals support it, or because it's working right now?
- When insiders or outsiders raise doubts about a core bet, do we investigate or dismiss them?

## Sources
- [Bankruptcy of Lehman Brothers — Wikipedia](https://en.wikipedia.org/wiki/Bankruptcy_of_Lehman_Brothers)
- [Why did Lehman Brothers fail? — Economics Observatory](https://www.economicsobservatory.com/why-did-lehman-brothers-fail)
- [Bankruptcy of Lehman Brothers — Britannica](https://www.britannica.com/event/bankruptcy-of-Lehman-Brothers)


---

<!-- ==== cases/luckin-coffee.md ==== -->

---
slug: luckin-coffee
company: Luckin Coffee
industry: retail/food & beverage (China)
founded: 2017
failed: 2020 (fraud exposed; delisted from Nasdaq; survived post-restructuring)
failure_types: [fraud_and_ethics, governance_and_leadership, scaling_too_fast]
severity: fraud_conviction
---

## What happened
Luckin Coffee, marketed as "the Starbucks of China," expanded to thousands of stores in a few years and went public on Nasdaq in 2019. To hit aggressive growth targets, employees used related-party transactions to fabricate more than $300M in retail sales through 2019, then inflated expenses by over $190M and altered accounting/bank records to hide it. An internal investigation admitted the fraud in April 2020; the stock fell over 75% in a single day, the company was delisted from Nasdaq, and it later paid a $180M SEC penalty plus a fine from Chinese regulators. (Note: unlike most cases here, Luckin itself survived — it restructured, replaced leadership, and later returned to profitability and even relisted over-the-counter, making it also a partial "recovery after fraud" story.)

## Root causes
- Extremely aggressive store-count and revenue growth targets, set to justify the IPO valuation and sustain investor narrative, created pressure that led employees to fabricate results rather than report a slower real growth rate.
- Related-party transactions were used specifically to manufacture the appearance of real customer sales, which is much harder for outside auditors to catch than simple bookkeeping errors.
- Growth was reported and celebrated well ahead of the unit economics (heavy subsidies/discounting to drive store traffic) actually working, creating a gap between the story and reality that eventually had to be closed one way or another.
- Weak internal controls at a fast-scaling company let a small group of employees fabricate a very large fraud before internal or external checks caught it.

## Warning signs (visible before the collapse)
- Store growth and reported revenue growth rates far outpacing what the underlying subsidized, low-margin unit economics could plausibly sustain.
- Short-seller reports (Muddy Waters published a detailed report in early 2020) alleging fabricated store traffic and sales data months before the company's own admission.
- Heavy discounting/subsidy-driven customer acquisition presented publicly as organic demand growth.
- A company scaling headcount, stores, and reported numbers faster than its internal financial controls could mature to handle the scale.

## Questions this raises for another company
- Are our growth numbers real customer demand, or partly the result of subsidies/discounting dressed up as organic growth in how we report them?
- Have we scaled reporting/financial controls at the same pace as we've scaled stores/headcount/revenue claims, or is oversight lagging behind growth?
- If a skeptical outside researcher (short-seller, journalist, auditor) dug into our unit-level data, would our growth story hold up?
- Is there pressure on any team to hit a growth number that only makes sense if some of it is manufactured rather than real?

## Sources
- [Luckin Coffee Agrees to Pay $180 Million Penalty to Settle Accounting Fraud Charges — SEC](https://www.sec.gov/newsroom/press-releases/2020-319)
- [Case Study: Luckin Coffee Accounting Fraud — Seven Pillars Institute](https://sevenpillarsinstitute.org/case-study-luckin-coffee-accounting-fraud/)
- [Luckin Coffee Inc. — SEC Litigation Release](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-24987)


---

<!-- ==== cases/myspace.md ==== -->

---
slug: myspace
company: MySpace
industry: tech/social media
founded: 2003
failed: 2011 (sold at massive loss after user exodus to Facebook)
failure_types: [culture_and_talent, disruption_denial, product_market_fit]
severity: acquired_in_distress
---

## What happened
MySpace was the dominant social network in the mid-2000s and was bought by News Corp for $580M in 2005. Under News Corp, the site prioritized advertising revenue and page-view-driven design (heavy, cluttered pages, aggressive ad placements) over user experience and product innovation, while Facebook shipped a cleaner, faster, more reliable product with a clearer growth model. Users migrated en masse, and MySpace was sold in 2011 for $35M.

## Root causes
- Owner (News Corp) prioritized short-term ad-revenue optimization over long-term product quality, engineering investment, and user experience.
- Slow, cluttered, bug-prone site experience (partly from ad-heavy design and technical debt) drove users toward a cleaner competitor as soon as one existed.
- Organizational culture was more "media company monetizing an asset" than "product/engineering company iterating for users," which put it at a structural disadvantage against a competitor built by engineers obsessed with product.
- Leadership and technical talent turnover after acquisition, weakening the ability to respond quickly to Facebook's rise.

## Warning signs (visible before the collapse)
- User-facing product quality (speed, reliability, clutter) visibly declining or stagnating while revenue metrics were still framed as healthy.
- Advertising/monetization decisions made with limited apparent input from product/user-experience considerations.
- A key competitive dimension (product speed and cleanliness) being ceded to a rising direct competitor without a serious response.
- Talent and engineering culture shifting away from product obsession after being acquired by a media-first parent.

## Questions this raises for another company
- Are we optimizing near-term monetization in ways that are visibly degrading the core user/customer experience?
- Is our organizational culture built around obsessing over the product, or around extracting revenue from an existing asset?
- Is a competitor winning on a dimension (speed, simplicity, reliability) we've stopped prioritizing?
- Did an acquisition or ownership change shift our incentives away from what originally made us win?

## Sources
- [What Happened to Myspace? — EM360Tech](https://em360tech.com/tech-articles/what-happened-myspace-fall-worlds-first-social-media-giant)
- [Chart: The Rise and Fall of MySpace — Statista](https://www.statista.com/chart/26176/estimated-number-of-myspace-users-at-key-milestones/)


---

<!-- ==== cases/nokia-mobile.md ==== -->

---
slug: nokia-mobile
company: Nokia (mobile phones division)
industry: tech/hardware
founded: 1865 (mobile division dominant 1998-2011)
failed: 2013 (sold to Microsoft)
failure_types: [disruption_denial, culture_and_talent, governance_and_leadership]
severity: acquired_in_distress
---

## What happened
Nokia was the world's dominant phone maker when the iPhone launched in 2007. It kept betting on its aging Symbian OS and hardware-first culture instead of a modern software/app-ecosystem approach, lost the smartphone race to Apple and Android within a few years, and sold its handset business to Microsoft in 2013 at a fraction of its former value.

## Root causes
- Deep hardware-engineering culture undervalued software and platform/ecosystem thinking, which is what actually won the smartphone era.
- Internal fear-based management (documented later as a culture of middle managers hiding bad news from leadership) delayed an honest reckoning with how far behind Symbian was.
- Organizational silos meant software and hardware teams didn't collaborate well enough to ship a competitive touch/app experience quickly.
- Decision paralysis: evaluated multiple OS strategies (Symbian, MeeGo, eventually Windows Phone) without committing decisively to one fast enough.

## Warning signs (visible before the collapse)
- A new entrant (Apple) redefining the product category (touchscreen + app store) while the incumbent's roadmap stayed hardware-spec focused.
- Middle managers reportedly softening bad news about product delays and competitive gaps before it reached the top.
- Multiple parallel, competing internal strategies for the same problem (three OS bets at once) signaling lack of a clear decision.
- Developer and app ecosystem growing rapidly around competitors while the incumbent's platform stayed closed/underinvested.

## Questions this raises for another company
- Is our core competency (e.g. hardware) actually what the market will pay for next, or is the value shifting to something we're weaker at (e.g. software/platform)?
- Do bad-news signals reach leadership honestly and quickly, or get softened on the way up?
- Are we running multiple competing strategies at once because we're hedging, or because we can't decide?
- Are we measuring ourselves against the old definition of the product category, or the new one a competitor just created?

## Sources
- [Case Study: Strategic Backstory of Nokia's Rise and Fall — The CDO TIMES](https://cdotimes.com/2025/08/13/case-study-strategic-backstory-nokias-rise-and-fall/)
- [Microsoft, Nokia, and the burning platform — VentureBeat](https://venturebeat.com/mobile/microsoft-nokia-and-the-burning-platform-a-final-look-at-the-failed-windows-phone-alliance/)
- [How Microsoft flushed $7.6 billion down the drain when it bought Nokia — TechSpot](https://www.techspot.com/news/102922-decade-later-how-microsoft-flushed-76-billion-down.html)


---

<!-- ==== cases/odebrecht.md ==== -->

---
slug: odebrecht
company: Odebrecht S.A.
industry: construction/engineering (Brazil)
founded: 1944
failed: 2016 (guilty plea), ongoing restructuring/rebrand
failure_types: [fraud_and_ethics, governance_and_leadership]
severity: fraud_conviction
---

## What happened
Odebrecht, Latin America's largest construction and engineering conglomerate, ran a dedicated internal division ("Division of Structured Operations," effectively a bribery department with its own budget, staff, and even encrypted software) that paid roughly $788 million in bribes across a dozen countries between 2001 and 2016 to win public infrastructure contracts. The scheme was exposed through Brazil's "Operation Car Wash" investigation. Odebrecht pleaded guilty to U.S. and Brazilian charges in 2016 in what was then the largest foreign-bribery settlement ever prosecuted (over $2.6 billion in fines), its CEO was jailed, and the resulting political fallout toppled or implicated presidents and senior officials in multiple Latin American countries.

## Root causes
- Bribery was not a rogue individual's misconduct but an institutionalized, budgeted internal function with its own staff, software, and operating procedures — corruption was built into the business model for winning contracts, not an occasional lapse.
- Heavy reliance on government infrastructure contracts created a direct incentive to influence the officials awarding them, and the company built durable, repeatable relationships to do so across many countries.
- Success bred scale: as the bribery apparatus worked in one country, it was systematized and exported to others, compounding both the financial exposure and the number of jurisdictions eventually investigating.
- Weak or captured oversight in the countries where contracts were awarded meant the scheme could run for over a decade before a single investigation (in this case, aimed initially at money laundering, not Odebrecht itself) unraveled it.

## Warning signs (visible before the collapse)
- An unusually high win-rate on competitively bid government contracts across many countries over a long period.
- A dedicated internal unit or function whose actual purpose is opaque even to much of the rest of the organization, operating with its own budget and tools.
- Business heavily dependent on relationships with government decision-makers in jurisdictions with weaker transparency or anti-corruption enforcement.
- Rapid replication of a "successful" approach to winning contracts from one country to many, without anyone asking why it worked so consistently.

## Questions this raises for another company
- If we win an unusually high share of competitive government or institutional bids, have we honestly examined why?
- Do we have any internal function whose real purpose isn't transparent to the rest of the organization, even at a senior level?
- Is a large share of our revenue dependent on relationships with a small number of government or institutional decision-makers?
- Are we replicating an approach that "works" in one market into new markets without scrutinizing why it's been so effective?

## Sources
- [Odebrecht — Wikipedia](https://en.wikipedia.org/wiki/Odebrecht)
- [Bribery Division: What is Odebrecht? Who is Involved? — ICIJ](https://www.icij.org/investigations/bribery-division/bribery-division-what-is-odebrecht-who-is-involved/)
- [Petrobras scandal — Britannica](https://www.britannica.com/event/Petrobras-scandal)


---

<!-- ==== cases/pets-com.md ==== -->

---
slug: pets-com
company: Pets.com
industry: e-commerce/retail
founded: 1998
failed: 2000
failure_types: [product_market_fit, financial_management, scaling_too_fast]
severity: shutdown
---

## What happened
Pets.com sold pet supplies online, spending heavily on brand advertising (including a Super Bowl ad) while selling heavy, low-margin products (like bags of dog food) at a loss to acquire market share, on the theory that scale would eventually produce profit. It burned through its IPO proceeds within nine months and shut down in the 2000 dot-com crash.

## Root causes
- Unit economics were negative from day one — shipping heavy, bulky items cheaply while discounting the products themselves meant the company lost money on every order, with no credible plan for when that would change.
- Spent disproportionately on brand marketing (mascot, Super Bowl ad) relative to actual demonstrated repeat demand or margin.
- Business plan depended on capital markets staying open indefinitely to fund ongoing losses ("grow now, profit later") rather than on the business becoming self-sustaining.
- No differentiated advantage (technology, logistics, or exclusive supply) over the eventual winners in the category, who solved logistics economics before scaling.

## Warning signs (visible before the collapse)
- Marketing spend far exceeding revenue, with brand awareness treated as equivalent to a viable business.
- Product economics (cost to acquire, ship, and discount goods) that lose money per unit sold, with growth making losses larger, not smaller.
- Funding strategy dependent on continuing to raise money in a hot market rather than approaching break-even.
- Little to no structural moat (proprietary logistics, exclusive supply, technology) versus competitors or the category incumbent.

## Questions this raises for another company
- Does each unit/order we sell lose or make money once fully loaded costs are included — and are we sure "scale will fix it," or just hoping?
- Is our marketing spend building demonstrated repeat demand, or just brand awareness disconnected from unit economics?
- If external funding dried up tomorrow, how many months could we survive?
- What structural advantage do we have that a well-funded copycat couldn't replicate?

## Sources
- [Pets.com — Wikipedia](https://en.wikipedia.org/wiki/Pets.com)
- [Pets.com — Museum of Failure](https://museumoffailure.com/exhibition/pets-com)


---

<!-- ==== cases/quibi.md ==== -->

---
slug: quibi
company: Quibi
industry: media/streaming
founded: 2018
failed: 2020
failure_types: [product_market_fit, governance_and_leadership]
severity: shutdown
---

## What happened
Quibi raised $1.75B to launch a mobile-only, short-form ($5-10 min episodes), premium-produced streaming service, betting on "quick bites" of Hollywood-quality content for commuters. It launched in April 2020 — just as COVID lockdowns eliminated commuting — lacked a shareable/social hook, had no TV app at launch, and shut down after only six months.

## Root causes
- The core assumption (people want premium content in mobile-only, short segments, specifically for commute/in-between moments) was never validated with real users before committing over a billion dollars.
- No mechanism for organic growth: no social sharing, no free tier, no TV-screen support, so it had to buy every single user through paid marketing.
- Leadership team came from traditional Hollywood/entertainment backgrounds with limited experience in consumer tech product growth loops.
- Launched into a macro environment (pandemic lockdowns) that invalidated the core use case, with no ability to adapt the product quickly.

## Warning signs (visible before the collapse)
- Enormous funding and top-tier content deals secured before any real evidence of consumer demand for the format.
- Product missing basic expected features at launch (no casting to TV, no easy sharing) in a category where those are baseline.
- Founders/leaders publicly confident and dismissive of early skepticism from tech press about the underlying premise.
- A single external shock (pandemic) able to invalidate the entire core use case, with no fallback positioning.

## Questions this raises for another company
- Have we validated the core assumption behind our product with real, unpaid user behavior — or only with funding and press?
- Does our product have any organic/viral growth loop, or does every single user require a paid acquisition dollar?
- Is our founding team's expertise matched to the actual skill the business needs (e.g., content vs. consumer growth)?
- What single external event would invalidate our core use case, and do we have any plan if it happens?

## Sources
- [Quibi shuts down: Why the $1.75 billion streaming app failed — Yahoo Finance](https://finance.yahoo.com/news/quibi-shuts-down-why-the-175-billion-streaming-app-failed-104534579.html)
- [7 Reasons Quibi Failed Despite Raising $1.8B — Failory](https://www.failory.com/cemetery/quibi)


---

<!-- ==== cases/satyam.md ==== -->

---
slug: satyam
company: Satyam Computer Services
industry: IT services (India)
founded: 1987
failed: 2009
failure_types: [fraud_and_ethics, governance_and_leadership]
severity: fraud_conviction
---

## What happened
Satyam was one of India's largest IT outsourcing companies. In January 2009, founder-chairman Ramalinga Raju confessed in a letter to the board that he had fabricated the company's accounts for years — inflating revenue, profit, and cash balances by roughly $1.5 billion, including over $1 billion in cash and bank balances that simply did not exist. The fraud was reportedly used to secure bank loans that were then diverted into unrelated real-estate ventures, and unraveled when a related property deal collapsed and drew scrutiny. It became known as "India's Enron."

## Root causes
- Founder held concentrated control over both the company and the diversion of its funds into personal/family real-estate ventures, with no internal check strong enough to catch or stop it.
- Fabricated financials were used as collateral to secure real loans from real banks — turning an accounting fraud into an actual cash diversion, not just a paper exercise.
- Board included qualified, independent-seeming directors, but a related-party transaction (an attempted $1.6B acquisition of two Raju-family-linked firms) was nearly approved before shareholder backlash forced its reversal — showing the board's scrutiny was more form than function.
- The fraud was sustained for years by continuously growing the fabrication to stay ahead of scrutiny, a treadmill that only stops when external conditions (here, a property market downturn) force a reckoning.

## Warning signs (visible before the collapse)
- A board approving (however briefly) a large related-party acquisition benefiting the founder's own family, with governance processes that looked adequate on paper.
- Reported cash and bank balances large enough that basic third-party verification (bank confirmations) should have been routine — and evidently wasn't rigorous enough.
- Fraud reportedly tied to and dependent on an unrelated market (real estate) staying strong — when that market turned, the whole scheme was exposed.
- A founder whose personal financial dealings were closely intertwined with the company's balance sheet.

## Questions this raises for another company
- Could our founder or a small group of insiders move company funds into their own ventures without the board or auditors independently verifying it?
- Are our reported cash balances actually confirmed directly with our banks by an independent party, or only reported internally?
- Is any part of our company's financial health quietly dependent on an unrelated market or venture staying strong?
- Does our board actually block related-party transactions that benefit insiders, or does it approve them and rely on after-the-fact shareholder pressure to reverse mistakes?

## Sources
- [Satyam scandal — Wikipedia](https://en.wikipedia.org/wiki/Satyam_scandal)
- [Founder Of Indian IT Giant Satyam Gets 7 Years For Fraud — NPR](https://www.npr.org/sections/thetwo-way/2015/04/09/398503322/founder-of-indian-it-giant-satyam-gets-7-years-in-fraud)
- [Satyam Scandal: Inside India's Enron — Transparently.ai](https://www.transparently.ai/blog/satyam-scandal-indias-enron)


---

<!-- ==== cases/sears.md ==== -->

---
slug: sears
company: Sears
industry: retail
founded: 1892
failed: 2018
failure_types: [financial_management, disruption_denial, culture_and_talent]
severity: bankruptcy
---

## What happened
Once America's largest retailer, Sears was merged with Kmart in 2005 under hedge-fund manager Eddie Lampert, who ran the company on an internal "competing business units" model that pitted divisions against each other for resources, while extracting value through real-estate spinoffs (Seritage) and stock buybacks instead of reinvesting in stores. The company filed for bankruptcy in 2018 after a decade of store closures and eroding sales.

## Root causes
- Internal structure that made divisions compete for capital like independent hedge-fund-style units undermined companywide cooperation (e.g., appliances and apparel units wouldn't collaborate on customer experience).
- Capital was extracted (real estate spin-off, buybacks, dividends to the controlling investor's funds) rather than reinvested in stores, e-commerce, or brand relevance.
- Chronic underinvestment in store maintenance and online capability let the shopping experience visibly decay for over a decade while competitors modernized.
- Leadership philosophy (rooted in market-based internal competition) was arguably better suited to financial engineering than to operating a large, complex retail brand needing unified strategy.

## Warning signs (visible before the collapse)
- Visible, ongoing decline in store conditions and customer experience without correction over many years.
- Structural moves that pulled value out of the operating company (real estate spin-offs, buybacks) even as core retail performance worsened.
- Persistent, publicly documented internal conflict between business units instead of coordinated strategy.
- Store closures and sales declines treated as manageable for years past the point competitors had already adapted.

## Questions this raises for another company
- Are we pulling capital out of the core business (dividends, spin-offs, buybacks) faster than we're reinvesting in what keeps customers coming back?
- Does our internal structure encourage departments to compete against each other more than to serve the customer together?
- Have we let visible quality/experience decline for "too long" because no single decision felt like the fatal one?
- Is our leadership's core skill set matched to running the operating business, or better suited to financial restructuring?

## Sources
- [Eddie Lampert Shattered Sears, Sullied His Reputation, and Lost Billions — Institutional Investor](https://www.institutionalinvestor.com/article/2bsxn8l0u5yr6zhelmhog/corner-office/eddie-lampert-shattered-sears-sullied-his-reputation-and-lost-billions-of-dollars-or-did-he)
- [Sears sues former CEO Eddie Lampert for alleged 'thefts' of billions — CNBC](https://www.cnbc.com/2019/04/18/sears-sues-eddie-lampert-steven-mnuchin-others-for-alleged-thefts.html)


---

<!-- ==== cases/segway.md ==== -->

---
slug: segway
company: Segway
industry: hardware/transportation
founded: 1999
failed: 2020 (discontinued flagship product)
failure_types: [product_market_fit, governance_and_leadership]
severity: shutdown
---

## What happened
Segway launched in 2001-2002 amid enormous hype (predicted by some backers to "reinvent" city transportation), priced its personal transporter at nearly $5,000, and sold only around 140,000 units in almost two decades — a fraction of early projections. Regulatory uncertainty (banned from sidewalks/roads in many places because it fit no existing vehicle category), the high price, and no clear use case relative to walking/biking/cars kept demand niche; cheaper electric scooters (Bird, Lime) finished the job after 2017, and the company discontinued the original product line in 2020.

## Root causes
- Product-market fit was assumed rather than tested: the company and investors believed the technology was so impressive that a market would obviously follow, without validating who would actually buy it and why.
- High price point ($5,000) put it far outside impulse-purchase range for what was, functionally, a walking/biking replacement — a hard sell for most consumers.
- No resolved regulatory framework (sidewalk vs. road use) at launch, creating real friction and uncertainty for the exact everyday use case being pitched.
- Marketing hype set expectations (revolutionizing transportation) far beyond what the product could realistically deliver for an individual buyer's daily life.

## Warning signs (visible before the collapse)
- Massive pre-launch hype and secrecy building expectations disconnected from any demonstrated consumer demand.
- A price point badly mismatched to the everyday problem the product solved.
- Unresolved basic regulatory/practical questions (where can you legally use it) at the moment of launch.
- Sales dramatically below internal projections in the first years, without the underlying strategy being revisited.

## Questions this raises for another company
- Is our confidence in demand based on real customer behavior, or on how impressive the technology seems to us and investors?
- Is our price point matched to the actual value/problem being solved for the everyday buyer?
- Are there unresolved external factors (regulatory, infrastructure, compatibility) that our own core use case depends on?
- When early sales badly miss projections, do we revisit the strategy, or just wait for the market to "catch up"?

## Sources
- [Why Did Segway Fail? — FourWeekMBA](https://fourweekmba.com/what-happened-to-segway/)
- [The Demise Of The Segway Is A Cautionary Tale For Technological Optimists — Forbes](https://www.forbes.com/sites/michaellynch/2020/06/29/the-demise-of-the-segway-is-a-cautionary-tale-for-technological-optimists/)


---

<!-- ==== cases/silicon-valley-bank.md ==== -->

---
slug: silicon-valley-bank
company: Silicon Valley Bank (SVB)
industry: finance/banking
founded: 1983
failed: 2023
failure_types: [financial_management, governance_and_leadership]
severity: bankruptcy
---

## What happened
SVB, the primary bank for much of the U.S. venture-backed startup ecosystem, invested heavily in long-term bonds during 2021's low-rate environment. As the Federal Reserve raised interest rates through 2022, the market value of those bonds fell, creating over $15B in unrealized losses by end of 2022, while SVB had also let its interest-rate hedges lapse. When SVB announced a $1.8B loss from selling securities and an emergency capital raise on March 8, 2023, prominent venture investors publicly urged portfolio companies to pull their money; depositors withdrew $42 billion in a single day, and regulators shut the bank down on March 10 — the second-largest U.S. bank failure in history.

## Root causes
- Concentrated deposit base (largely tech startups and VC funds) meant depositor behavior was correlated — when one influential voice said "pull your money," a huge share of depositors acted in the same direction at the same time, unlike a diversified retail bank.
- Interest-rate risk was mismanaged: large bond purchases were made assuming rates would stay low, and hedges that would have protected against rate increases were reportedly removed to boost near-term reported earnings.
- Very large deposit balances (many well above the $250K FDIC insurance limit) gave depositors a strong individual incentive to be first to withdraw at the first sign of trouble, accelerating the run.
- Risk management and governance did not scale with the bank's rapid growth in the 2020-2021 period — growth was prioritized over building the controls appropriate to the bank's new size and concentration.

## Warning signs (visible before the collapse)
- A rapidly growing balance sheet increasingly concentrated in long-duration securities exposed to interest-rate risk, in a rising-rate environment.
- A depositor base heavily concentrated in one industry/network (tech/VC) with a documented tendency to communicate and act collectively.
- Large unrealized losses on a "hold to maturity" bond portfolio that would only become "realized" losses if the bank were forced to sell early — a bet that assumed it would never need to.
- Removal or lapsing of hedges specifically in the period when the underlying risk (rate increases) was already visibly materializing.

## Questions this raises for another company
- Is a large share of our deposits/assets concentrated with one type of customer or a tightly networked community that could move in the same direction at the same time?
- Have we taken on a financial position (rates, currency, commodity) assuming a trend continues, without a real hedge, or did we remove a hedge to make near-term numbers look better?
- What fraction of our depositors/customers/revenue sit above whatever protection or insurance threshold exists, giving them a strong individual incentive to move first in a crisis?
- Has our risk management and governance actually kept pace with how fast we've grown, or is it still sized for an earlier, smaller version of the company?

## Sources
- [Collapse of Silicon Valley Bank — Wikipedia](https://en.wikipedia.org/wiki/Collapse_of_Silicon_Valley_Bank)
- [The Collapse Of Silicon Valley Bank — NPR Planet Money](https://www.npr.org/sections/money/2023/03/14/1163200179/the-collapse-of-silicon-valley-bank)
- [Material Loss Review of Silicon Valley Bank — Federal Reserve OIG](https://oig.federalreserve.gov/reports/board-material-loss-review-silicon-valley-bank-sep2023.pdf)


---

<!-- ==== cases/steinhoff.md ==== -->

---
slug: steinhoff
company: Steinhoff International
industry: retail/furniture conglomerate (South Africa)
founded: 1964
failed: 2017
failure_types: [fraud_and_ethics, governance_and_leadership]
severity: fraud_charges_pending
---

## What happened
Steinhoff, a South African-founded, Europe-listed global furniture and retail conglomerate (owner of brands like Conforama and Mattress Firm), collapsed in December 2017 when its auditors refused to sign off on its accounts and CEO Markus Jooste resigned the same evening. An investigation later found roughly €6.5 billion in fictitious or irregular transactions with a network of off-balance-sheet entities over nearly a decade. The share price fell more than 95% within days, wiping out over $13 billion for investors including South African pension funds, and triggering lawsuits across three continents. Jooste was never criminally tried: South Africa's financial regulator (FSCA) fined him R475 million for publishing false/misleading statements in March 2024, and he died by apparent suicide the next day, shortly before he was due to face separate criminal charges and an arrest warrant from German prosecutors. No individual has been criminally convicted in the case as of this writing; the regulatory and civil proceedings above are administrative/civil findings, not criminal convictions.

## Root causes
- Used a network of related off-balance-sheet entities to book fictitious profits and hide losses from real acquisitions, inflating the company's apparent growth from its aggressive acquisition strategy.
- Rapid, debt-funded, cross-border acquisition spree (Europe, US, Africa, Australia) created enough complexity that consolidated financial statements were extremely hard for outsiders — and apparently even some insiders — to scrutinize.
- Long-tenured relationships between the CEO and the network of transaction counterparties meant conflicts of interest weren't flagged through normal channels.
- Auditor turnover/pressure dynamics meant red flags accumulated for years before an audit firm finally refused to sign off, at which point the exposure was already enormous.

## Warning signs (visible before the collapse)
- An acquisition pace and geographic spread fast enough that even sophisticated investors and analysts struggled to fully understand the consolidated business.
- Profit growth that consistently outpaced what organic performance in the underlying retail brands could plausibly explain.
- A concentrated, long-standing network of transaction counterparties tied to leadership, used repeatedly across deals.
- Auditors reportedly raising concerns for a period before ultimately refusing to sign off — a gap between "still auditing" and "confident in the numbers."

## Questions this raises for another company
- Have we grown so fast through acquisition that even our own board or investors can't fully explain how the consolidated numbers add up?
- Are the same handful of counterparties or related entities showing up across multiple of our transactions?
- Is our reported profit growth consistently outrunning what the underlying operating businesses could organically produce?
- If our auditor privately had doubts for a year before finally acting, would we have any independent way of finding out sooner?

## Sources
- [Steinhoff International — Wikipedia](https://en.wikipedia.org/wiki/Steinhoff_International)
- [A Look into the Accounting Fraud Case at Steinhoff International — Arcadia](https://www.byarcadia.org/post/a-look-into-accounting-fraud-case-at-steinhoff-international)
- [More Violations Uncovered in Steinhoff Scandal — OCCRP](https://www.occrp.org/en/news/more-violations-uncovered-in-steinhoff-scandal)
- [Ex-Steinhoff CEO Jooste's Death Came After Arrest Warrant Issued — Bloomberg](https://www.bloomberg.com/news/articles/2024-03-22/ex-steinhoff-ceo-jooste-death-came-after-arrest-warrant-issued)
- [Ex-Steinhoff CEO Markus Jooste Dies Day After He's Fined $25 Million — Bloomberg](https://www.bloomberg.com/news/articles/2024-03-21/former-steinhoff-ceo-markus-jooste-dies-in-south-africa)

*Markus Jooste died before any criminal trial and was never convicted; the account above reflects regulatory/civil findings and reporting, not a criminal conviction.*


---

<!-- ==== cases/theranos.md ==== -->

---
slug: theranos
company: Theranos
industry: healthcare/tech
founded: 2003
failed: 2018
failure_types: [fraud_and_ethics, governance_and_leadership, product_market_fit]
severity: shutdown, fraud_conviction
---

## What happened
Theranos claimed its Edison device could run hundreds of accurate blood tests from a single finger-prick, raising over $700M at a $9B valuation. The technology never worked as claimed — most tests were secretly run on modified third-party machines or produced unreliable results — and the fraud was exposed by investigative journalism in 2015, leading to shutdown and criminal convictions.

## Root causes
- Founder built a culture of extreme secrecy ("stealth mode" taken to an extreme) that prevented normal scientific peer review or scrutiny of whether the core technology actually worked.
- Board was stacked with prestigious but non-technical members (former statesmen, generals) who could not meaningfully evaluate the science.
- Aggressive PR and fundraising ran years ahead of product reality — the story was sold before the technology existed.
- Internal dissent was suppressed: employees who raised accuracy/safety concerns were threatened with legal action or fired.

## Warning signs (visible before the collapse)
- Zero peer-reviewed publications or independent validation of a claimed medical breakthrough, despite years of operation.
- A board with impressive names but no relevant technical expertise to challenge the founder.
- Extreme secrecy even with employees, and heavy NDAs/legal threats used against internal skeptics.
- Product claims dramatically outpacing any public, verifiable demonstration.

## Questions this raises for another company
- Can an outside expert independently verify our core technical claim, or do we only have internal say-so?
- Does our board have anyone who can actually challenge the founder/CEO on the technical substance, not just the vision?
- Are we more focused on the story we tell investors than on what the product can currently, verifiably do?
- Do employees who raise safety, quality, or accuracy concerns get heard, or get managed out?

## Sources
- [Theranos — Wikipedia](https://en.wikipedia.org/wiki/Theranos)
- [Elizabeth Holmes — Wikipedia](https://en.wikipedia.org/wiki/Elizabeth_Holmes)
- [Fake It Till You Fail: Elizabeth Holmes and the Theranos Story — Darden](https://ideas.darden.virginia.edu/theranos-darden-case)


---

<!-- ==== cases/toys-r-us.md ==== -->

---
slug: toys-r-us
company: Toys "R" Us
industry: retail
founded: 1948
failed: 2017 (bankruptcy), 2018 (liquidation)
failure_types: [financial_management, disruption_denial]
severity: bankruptcy
---

## What happened
In 2005, private equity firms took Toys "R" Us private in a $6.6B leveraged buyout, loading the company with roughly $5B in debt. The company had to pay $400-500M/year in interest alone, leaving little capital to modernize stores or compete with Amazon and Walmart online; it filed for bankruptcy in 2017 and liquidated in 2018, closing all U.S. stores.

## Root causes
- The leveraged buyout structure transferred the acquirers' debt onto the company itself, consuming cash flow that should have funded e-commerce and store investment.
- Heavy interest payments left the business unable to compete on price or online convenience against Amazon and Walmart during the exact years e-commerce was taking off.
- Store experience and digital investment stagnated for over a decade while the debt burden persisted, widening the gap with competitors.
- Ownership structure prioritized financial engineering (extracting value via the buyout) over long-term operating health of the underlying business.

## Warning signs (visible before the collapse)
- Debt load and required interest payments disproportionate to the company's cash-generating ability, especially in a capital-intensive retail category.
- Visible underinvestment in stores and online capability relative to direct competitors over many years.
- Ownership incentives (PE sponsors) misaligned with long-term competitiveness versus near/medium-term financial extraction.
- A widening gap between the company's customer experience and where the market (online shopping) was clearly heading.

## Questions this raises for another company
- Is our debt load sized to what the business can service even if a competitor undercuts us for several years?
- Are we underinvesting in the capability (e.g., digital/online) that we know is where our category is heading?
- Do our owners'/investors' incentives align with the long-term health of the operating business, or with near-term financial extraction?
- If our interest/debt payments doubled overnight, could we still invest in staying competitive?

## Sources
- [Toys "R" Us Collapse: How Private Equity Loaded It With Debt — Headcount Coffee](https://www.headcountcoffee.com/blogs/corporate-legends-lost-empires/how-private-equity-destroyed-toys-r-us-the-real-story-behind-the-bankruptcy)
- [Private Equity: Looting "R" Us — The American Prospect](https://prospect.org/2018/03/20/private-equity-looting-r-us/)


---

<!-- ==== cases/webvan.md ==== -->

---
slug: webvan
company: Webvan
industry: e-commerce/grocery/logistics
founded: 1996
failed: 2001
failure_types: [scaling_too_fast, financial_management, product_market_fit]
severity: bankruptcy
---

## What happened
Webvan raised over $800M to build a nationwide online grocery delivery network, constructing massive custom automated warehouses in city after city before demand in any single market was proven. It expanded to 10+ cities in under two years, never came close to the warehouse utilization needed to break even, and went bankrupt in 2001.

## Root causes
- Committed hundreds of millions to fixed infrastructure (custom automated warehouses) sized for demand that didn't yet exist, in market after market, without proving the model in one city first.
- Grocery delivery has structurally thin margins and heavy logistics costs; the automation was meant to fix this but required near-full warehouse utilization that never materialized.
- Expansion pace was driven by investor/market pressure to grow fast and "own the category" rather than by validated unit economics in existing markets.
- Executive team had limited grocery/logistics operating experience relative to the operational complexity being attempted.

## Warning signs (visible before the collapse)
- Massive capital expenditure on infrastructure before the core business model was proven profitable even in one location.
- Aggressive multi-city rollout timeline set by growth targets/investor expectations rather than operating data.
- Persistently low warehouse utilization rates reported well below the level needed for the automation investment to pay off.
- Thin-margin category (grocery) being treated with venture-scale growth assumptions borrowed from software.

## Questions this raises for another company
- Have we proven the model is profitable in one location/segment before replicating the fixed-cost investment elsewhere?
- Is our expansion pace set by what the data says is working, or by external pressure to grow fast?
- Does our industry have inherently thin margins that require near-perfect operational execution — and do we have the operating expertise for that, not just capital?
- What is our actual utilization/efficiency rate against the level needed to break even, and is it trending toward or away from that?

## Sources
- [Webvan — Wikipedia](https://en.wikipedia.org/wiki/Webvan)
- [Four Lessons Amazon Learned From Webvan's Flop — Forbes](https://www.forbes.com/sites/petercohan/2013/06/17/four-lessons-amazon-learned-from-webvans-flop/)


---

<!-- ==== cases/wework.md ==== -->

---
slug: wework
company: WeWork
industry: real estate/tech
founded: 2010
failed: 2019 (failed IPO, forced restructuring); Chapter 11 in 2023
failure_types: [governance_and_leadership, financial_management, scaling_too_fast]
severity: bankruptcy
---

## What happened
WeWork signed long-term leases on office space and rented it out short-term, marketing itself as a tech "community" company to justify a software-like valuation ($47B) despite being fundamentally a leveraged real-estate business. Its 2019 IPO filing exposed massive losses, self-dealing by founder Adam Neumann, and no path to profitability; the IPO collapsed, Neumann was ousted, and the company eventually filed for bankruptcy in 2023.

## Root causes
- Fundamental mismatch between the actual business model (long-term lease liabilities funding short-term rental income — a risky duration mismatch) and how it was marketed and valued (as high-margin tech).
- Founder held outsized, unchecked control (super-voting shares, a compliant board) enabling self-dealing: leasing his own properties to the company, trademarking "We" and selling it back to the company.
- Growth-at-all-costs culture prioritized signing new locations over unit economics of existing ones.
- No governance check translated enthusiasm/vision into financial discipline before the S-1 filing forced public scrutiny.

## Warning signs (visible before the collapse)
- A charismatic founder with concentrated voting control and a board that rarely pushed back.
- Business fundamentals (heavy fixed lease liabilities vs. variable short-term revenue) inconsistent with the growth-stock valuation multiple being claimed.
- Related-party transactions benefiting the founder personally at the company's expense.
- Massive, widening losses treated as a temporary/acceptable cost of "growth" with no credible path to profitability shown.

## Questions this raises for another company
- Are we valuing/pitching ourselves based on the industry we resemble in spirit, or the one whose economics we actually have (fixed costs, margins, liabilities)?
- Does any single individual have effectively unchecked control, and is the board able to say no to them?
- Are there transactions where a founder/executive personally benefits at the company's expense?
- Is our growth being funded sustainably, or by continuously raising more money to cover structurally negative unit economics?

## Sources
- [What exactly happened to WeWork? — The Corporate Governance Institute](https://www.thecorporategovernanceinstitute.com/insights/case-studies/what-exactly-happened-to-wework/)
- [The WeWork Collapse: Governance Failures, Founder Control & Lessons Learned — Directors Institute](https://www.directors-institute.com/post/the-wework-collapse-governance-failures-founder-control-lessons-learned)


---

<!-- ==== cases/wirecard.md ==== -->

---
slug: wirecard
company: Wirecard AG
industry: fintech/payments (Germany)
founded: 1999
failed: 2020
failure_types: [fraud_and_ethics, governance_and_leadership]
severity: bankruptcy, fraud_charges_pending
---

## What happened
Wirecard was a German payment-processing company that grew into a DAX-30 blue chip, at one point worth more than Deutsche Bank. Much of its reported profit came from transactions and a claimed €1.9 billion in cash held in trustee accounts at two Philippine banks that, when auditor EY finally refused to sign off on the 2019 accounts, were found not to exist. The company filed for insolvency in June 2020. Former CEO Markus Braun was arrested and has been on criminal trial since late 2022 — as of the trial's most recent extension (to end of 2025), no verdict has been delivered, and Braun denies the charges, blaming other former executives. Former COO Jan Marsalek fled the country and remains an internationally wanted fugitive. In a *separate civil case*, a German court ordered Braun and two other former executives to pay €140 million in damages for breach of fiduciary duty.

## Root causes
- A large share of reported revenue and profit came from third-party partner businesses in opaque jurisdictions that were never independently verified in a way that could catch fabrication.
- The auditor (EY) signed off on the same fabricated figures for over a decade before finally refusing — long-tenured auditor relationships did not translate into genuine scrutiny.
- The German financial regulator (BaFin) reportedly investigated journalists and short-sellers who raised fraud allegations, rather than investigating the company itself, delaying the reckoning by years.
- National pride in a homegrown fintech champion (competing narrative to Silicon Valley) made institutional actors reluctant to challenge the company's numbers.

## Warning signs (visible before the collapse)
- Investigative journalism (Financial Times) and short-sellers publishing detailed, specific fraud allegations years before the collapse, initially dismissed by the company and regulator alike.
- A large share of profit concentrated in unverifiable "third-party acquirer" partnerships in jurisdictions with weak transparency.
- Regulatory response to fraud allegations directed at the accusers (journalists, short-sellers) rather than the company being accused.
- A single long-tenured auditor relationship with no apparent escalation of scrutiny despite years of accumulating red flags.

## Questions this raises for another company
- Is a large share of our reported profit concentrated in relationships or jurisdictions that are hard for an outside auditor to independently verify?
- Has the same auditor signed off on our numbers for many years — and would a fresh set of eyes actually catch something they've stopped looking for?
- When credible outside critics (journalists, short-sellers, analysts) raise specific fraud allegations, is our first instinct to investigate the claim or to discredit the accuser?
- Are we, or our regulators, treating a company as "too important to be fraudulent" because of what it represents (national champion, hot sector) rather than what its numbers actually show?

## Sources
- [Wirecard scandal — Wikipedia](https://en.wikipedia.org/wiki/Wirecard_scandal)
- [Wirecard's collapse reveals cracks at the heart of Germany, Inc — CNN Business](https://www.cnn.com/2020/06/27/tech/wirecard-germany)
- [Wirecard Was Germany's Fintech Star—Now $2 Billion Is Missing — Forbes](https://www.forbes.com/sites/isabeltogoh/2020/06/23/wirecard-was-germanys-fintech-star-now-2-billion-is-missing-and-its-ceo-has-been-arrested/)
- [German court extends Wirecard trial to end 2025 — no judgement date — Reuters via Yahoo Finance](https://finance.yahoo.com/news/german-court-extends-wirecard-trial-094222992.html)
- [Ex-Wirecard CEO Braun sentenced to pay damages to insolvency administrator (civil case) — MarketScreener](https://www.marketscreener.com/quote/stock/WIRECARD-AG-129712707/news/Ex-Wirecard-CEO-Braun-sentenced-to-pay-damages-to-insolvency-administrator-47809931/)

*Criminal charges against Markus Braun are unproven allegations; he denies wrongdoing and is presumed innocent unless and until convicted.*


---

<!-- ==== cases/yahoo.md ==== -->

---
slug: yahoo
company: Yahoo
industry: tech/internet
founded: 1994
failed: 2017 (core business sold to Verizon for a fraction of past valuation)
failure_types: [governance_and_leadership, culture_and_talent, product_market_fit]
severity: acquired_in_distress
---

## What happened
Yahoo was one of the earliest and biggest internet portals, at one point worth over $125B. It passed on acquiring Google (twice, for as little as $1M then later $3B) and later passed on acquiring Facebook for $1B, while cycling through six CEOs in under a decade with shifting, inconsistent strategies (portal vs. search vs. media vs. content). It also rejected a $44.6B acquisition offer from Microsoft in 2008 and later suffered massive undisclosed data breaches. Its core business was eventually sold to Verizon in 2016-2017 for about $4.8B — a fraction of its peak value.

## Root causes
- Chronic strategic indecision — repeated CEO turnover meant the company kept restarting its strategy (search vs. content vs. portal) before any direction had time to work.
- Missed or declined the two most consequential acquisition opportunities in internet history (Google, Facebook) due to internal disagreement about long-term value versus short-term price.
- Organizational culture became risk-averse and bureaucratic as the company grew, slowing product decisions relative to more nimble competitors (Google, later Facebook).
- Security/infrastructure investment lagged, leading to breaches that further damaged trust and valuation right before the sale.

## Warning signs (visible before the collapse)
- Frequent CEO/leadership changes each bringing a different strategic direction, with no time for any one bet to prove out.
- Declining a clearly promising acquisition target primarily over price negotiation rather than long-term strategic value.
- Slower product shipping cadence and more internal process relative to smaller, faster-moving competitors in the same space.
- Security or infrastructure debt accumulating without proportional investment, eventually surfacing as a major incident.

## Questions this raises for another company
- Has our strategic direction changed multiple times recently without any version being given time to actually work?
- Are we letting a good acquisition or partnership slip away over a price disagreement, without weighing the long-term strategic cost of a competitor getting it instead?
- Are we becoming slower and more process-heavy than the smaller competitors now nipping at our core business?
- Is there infrastructure or security debt we're deferring that could become a headline-level failure?

## Sources
- [Yahoo Sells To Verizon In Saddest $5 Billion Deal In Tech History — Forbes](https://www.forbes.com/sites/briansolomon/2016/07/25/yahoo-sells-to-verizon-for-5-billion-marissa-mayer/)
- [The rise and fall (OK — mostly fall) of Yahoo — freeCodeCamp](https://www.freecodecamp.org/news/the-rise-and-fall-mostly-fall-of-yahoo-ddbceb44670c)


---

<!-- ==== cases/contrasts/netflix-pivot.md ==== -->

---
slug: netflix-pivot
company: Netflix
industry: media/streaming
founded: 1997
avoided_failure_by: pivoting from DVD-by-mail to streaming ahead of the market forcing it
contrasts_with: blockbuster
failure_types_avoided: [disruption_denial]
---

## What happened
Netflix built its early business on DVD-by-mail — the same category Blockbuster dominated in stores. Rather than defending that model once bandwidth and technology made streaming viable, Netflix invested roughly $40M into streaming infrastructure starting in 2007, deliberately built the capability that would eventually cannibalize its own core DVD business, integrated into consumer devices early, and later moved into original content. It kept the DVD-by-mail service running in parallel for over a decade (shipping its final disc in September 2023) rather than an abrupt cutover, but streaming was clearly the resourced, strategic priority from early on.

## Why this worked where Blockbuster's non-response failed
- Leadership treated the disruptive alternative (streaming) as the future to lead, not a niche to dismiss — the opposite of Blockbuster CEO Jim Keyes calling Netflix "not even on the radar" as late as 2008.
- Netflix was willing to cannibalize its own profitable core business (DVD rental) on purpose, before being forced to by a competitor or collapsing demand.
- Existing data/infrastructure from the DVD business (customer preferences, recommendation data) was reused as a real asset for the new business, not thrown away.
- The transition was resourced like a real bet — real capital, real engineering investment — not a symbolic side project.

## What this suggests to check in your own company
- When we see a cheaper/simpler alternative to our core product emerging, do we resource a real internal response, or a token one?
- Are we willing to let a new internal initiative compete with (and eventually shrink) our most profitable current business, if the market is clearly moving that way?
- Are we using the data/customer relationships from our current business as an asset for the pivot, rather than starting over?
- Is our transition plan resourced at a level that could actually win, or just enough to say we "have a strategy" for it?

## Sources
- [Netflix vs. Blockbuster: The Streaming Pivot — MBA Strategy Case Study](https://www.visimade.com/p/netflix-vs-blockbuster-the-streaming-pivot-mba-strategy-case-study)
- [Netflix Case Study: From Late Fees to Streaming Dominance — World Economic Magazine](https://worldecomag.com/netflix-case-study-from-late-fees-2-dominance/)
- See also [cases/blockbuster.md](../blockbuster.md) for the failure side of this same disruption.


---

