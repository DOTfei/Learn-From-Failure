# Failure Case Index

37 failure cases, tagged by failure_types for pattern matching. One company can span multiple tags.
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
| [byjus](byjus.md) | edtech (India) | scaling_too_fast, financial_management, governance_and_leadership |
| [efishery](efishery.md) | agritech/aquaculture (Indonesia) | fraud_and_ethics, governance_and_leadership, scaling_too_fast |
| [propzy](propzy.md) | proptech/real estate (Vietnam) | scaling_too_fast, financial_management, product_market_fit |
| [tanihub](tanihub.md) | agritech (Indonesia) | scaling_too_fast, financial_management, governance_and_leadership |
| [kaodim](kaodim.md) | services marketplace (Malaysia) | product_market_fit, disruption_denial |

## Failure type taxonomy

- **fraud_and_ethics** — faked results, hid losses, misused customer/investor funds (Enron, Theranos, FTX, Katerra, Fusionex, Luckin Coffee, Wirecard, Satyam, Steinhoff, HIH Insurance, Odebrecht, eFishery)
- **governance_and_leadership** — no real checks on founder/CEO, board can't or won't push back, indecisive or conflicted leadership (WeWork, FTX, Yahoo, Nokia, BlackBerry, Katerra, Lehman, Fusionex, Silicon Valley Bank, Evergrande, Wirecard, Satyam, Steinhoff, Boeing 737 MAX, HIH Insurance, Odebrecht, BYJU'S, eFishery, TaniHub)
- **financial_management** — bad debt/leverage, negative unit economics, cash burn with no path to breakeven (Lehman, Toys R Us, Sears, Pets.com, Webvan, Juicero, Katerra, Fusionex, Silicon Valley Bank, Evergrande, HIH Insurance, BYJU'S, Propzy, TaniHub)
- **disruption_denial** — saw the shift coming (or invented it) and protected the legacy business instead (Kodak, Blockbuster, Nokia, Sears, Borders, BlackBerry, Toys R Us, Circuit City, MySpace, Kaodim)
- **product_market_fit** — built/scaled before proving anyone actually wanted it at that price/format (Quibi, Pets.com, Webvan, Juicero, Segway, Theranos, MySpace, Yahoo, Propzy, Kaodim)
- **scaling_too_fast** — grew headcount/locations/capital deployment ahead of proven, repeatable unit economics (WeWork, Webvan, Pets.com, Katerra, Kenny Rogers Roasters, Luckin Coffee, Evergrande, BYJU'S, eFishery, Propzy, TaniHub)
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
Brazil, Indonesia, and Vietnam — most of these failure mechanisms aren't specific to one
country's business culture. If you know a well-documented case from a region not yet covered
here, see [CONTRIBUTING.md](../CONTRIBUTING.md).

## Method & limitations

These are pattern-matching prompts for reflection, not predictions. Survivorship bias applies:
plenty of companies exhibited one or two of these warning signs and survived anyway. Treat a
match as "worth investigating," never as "this means we will fail." See the root disclaimer in
the repo [README](../README.md#how-to-read-these-cases).
