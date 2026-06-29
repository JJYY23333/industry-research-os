# Opportunity Scoring Model

Use this file before ranking opportunities. Score from 1 to 5 unless stated otherwise.

## Opportunity Card

Each opportunity must include:

- `name`
- `type`: product, service, content, channel, pricing, business model, regulatory, infrastructure
- `target_user`
- `pain_or_demand`
- `evidence`
- `current_alternatives`
- `competitor_gap`
- `proposed_offer`
- `acquisition_channel`
- `monetization_logic`
- `riskiest_assumption`
- `validation_test`
- `success_threshold`
- `kill_condition`
- `score`
- `confidence`: high, medium, low
- `sources`

## Core Scores

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Pain intensity | Mild preference | Frequent annoyance | Urgent, expensive, repeated pain |
| Demand evidence | Anecdotes only | Repeated search/social/review signals | Clear paid demand or strong purchase intent |
| Competition gap | Dominant solutions cover it well | Some gaps visible | Existing options are weak, costly, confusing, or poorly distributed |
| Channel access | No clear path to users | One plausible channel | Clear reachable channel with repeatable content/SEO/community/partner path |
| Monetization | Unclear willingness to pay | Plausible payment model | Existing spend or obvious budget owner |
| Execution fit | Outside user's capabilities | Requires learning/partners | Fits user's assets, skills, budget, and timeline |
| Speed to validate | >90 days | 30-60 days | 7-14 days |
| Trend support | Declining or stagnant | Stable | Strengthening due to platform, behavior, regulation, or tech shift |

## Adjustments

Subtract 1-2 points when:

- The buyer and user are different and the buying process is unclear.
- The opportunity depends on a platform that may block, ban, or commoditize it.
- The market is attractive only because of broad TAM claims.
- Required data, licenses, suppliers, or trust signals are not accessible.
- The first validation test is expensive or slow.

Add 1 point when:

- Negative reviews show repeated willingness to switch.
- Small competitors are growing despite weak products or poor content.
- Search intent is commercial and existing pages are low quality.
- Users already pay for awkward workarounds.
- The user has a proprietary channel, data source, audience, supplier, or execution edge.

## Ranking Formula

Use weighted judgment, not a blind average:

```text
priority = pain + demand + channel + monetization + execution_fit + speed_to_validate + trend_support - competition_risk
```

Then revise the rank by confidence:

- `high`: supported by multiple reliable sources or direct market signals.
- `medium`: supported by repeated secondary signals, but direct payment or conversion evidence is missing.
- `low`: plausible hypothesis that requires early validation before serious work.

## No-Go Signals

Flag as no-go or low priority when:

- No specific buyer can be named.
- The user pain is real but not paid.
- Acquisition depends entirely on paid ads with unknown economics.
- The product is easy to copy and has no channel advantage.
- The opportunity requires regulatory, medical, financial, or legal claims that the user cannot substantiate.
- The validation path cannot produce a useful signal within the user's timeframe.

## Validation Test Menu

| Test | Best for | Signal |
|---|---|---|
| Interview sprint | Pain and workflow discovery | Repeated language, urgent moments, existing workarounds |
| Landing page smoke test | Offer and message validation | Conversion rate, email signups, demo requests |
| Paid search test | Commercial demand | CTR, CPC, conversion intent, keyword economics |
| SEO/content batch | Content opportunity | Impressions, saves, comments, long-tail traction |
| Concierge MVP | Service/product feasibility | Paid pilots, time saved, retention intent |
| Competitor review mining | Product gap discovery | Repeated complaints and switching triggers |
| Community post test | Audience resonance | Comments with use cases, DMs, requests for details |

