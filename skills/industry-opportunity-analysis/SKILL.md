---
name: industry-opportunity-analysis
description: Use when Codex needs to analyze industry opportunities, market white space, consulting entry points, product ideas, content opportunities, competitor gaps, user pain points, keyword/content demand, business model opportunities, opportunity scoring, validation plans, or an Obsidian-ready saved analysis for a target industry or sector.
---

# Industry Opportunity Analysis

Turn a target industry into an evidence-backed opportunity pipeline: researched, scored, prioritized, and ready for validation.

## Operating Rules

- Before any industry analysis output, run a short user confirmation step. Confirm the user's target industry, work nature or role, interest direction, and desired result. This matters because the same industry should be analyzed differently for a consultant, founder, investor, operator, salesperson, policymaker, or content creator.
- If the user already provided those details, restate them as assumptions and ask for confirmation before deep research or final analysis.
- Do not begin the substantive analysis until the user confirms the result direction. If the user only wants a quick answer and explicitly refuses clarification, state the assumed scope before continuing.
- Every analysis run must create a new folder and save the result there. Use the current working directory unless the user gives a path. Use a clear folder name based on the industry and date/time; if a folder already exists, create a unique suffix. If file creation is impossible, stop and explain the blocker.
- If the user wants current facts, search recent primary or high-quality sources before making claims.
- Mark important claims as `fact`, `judgment`, `hypothesis`, or `to-verify`.
- Prefer a ranked opportunity backlog over a broad report. Every opportunity must include evidence, assumptions, risks, and a next validation action.
- Separate product, content, channel, pricing, business model, and regulatory opportunities instead of merging them into one vague "market chance."

## Workflow

1. **Confirm the user's context**
   - Ask concise questions for any missing items:
     - Target industry or sector scope.
     - User's work nature or role, such as consulting, entrepreneurship, investment, product, sales, operations, policy, research, or content.
     - Interest direction, such as current state, pain points, opportunities, competitors, policy, product ideas, consulting services, or validation.
     - Desired result and output format, such as brief memo, consulting-style report, opportunity backlog, SOP, slides outline, or Obsidian-ready workspace.
   - If the user has already supplied details, summarize: `I will analyze <industry> from the perspective of <role/work nature>, focusing on <interest direction>, and produce <result>. Please confirm.` Wait for confirmation before continuing.

2. **Create the result workspace**
   - Create a new folder before writing the analysis.
   - If creating files, read `references/output-contracts.md` first.
   - Save scope confirmation and assumptions in `00-scope.md`.

3. **Frame the scope**
   - Define industry, market, customer segment, time horizon, user role, interest direction, decision goal, and expected result.
   - If the user is exploring, default to: `industry + region + 12-24 month opportunity horizon`, but still confirm before analysis.

4. **Build the quick industry map**
   - Capture industry definition, value chain, customer segments, main jobs-to-be-done, buying triggers, top players, channels, and constraints.
   - For current markets, collect sources and grade their reliability.

5. **Create the evidence databases**
   - User pain points: complaints, unmet needs, workaround behavior, willingness-to-pay clues.
   - Competitors: positioning, offers, pricing, channels, SEO/content structure, conversion path.
   - Products/offers: categories, features, price bands, reviews, repeat purchase drivers, negative reviews.
   - Keywords/content: demand intent, commercial value, platform fit, content formats, recurring topics.
   - Business models: revenue logic, CAC/LTV clues, supply chain dependency, margin drivers.

6. **Mine opportunities by lens**
   - Pain gap: strong repeated pain with weak existing solutions.
   - Segment gap: underserved user segment or use case.
   - Competitor gap: visible weakness in top players' products, content, SEO, pricing, or distribution.
   - Channel gap: demand exists on one platform but supply/competition is weak.
   - Content gap: high-interest questions or formats not well served.
   - Offer gap: better bundle, guarantee, onboarding, service layer, or price architecture.
   - Timing gap: regulation, technology, platform, supply chain, or cultural shift changes what is viable.

7. **Score and prioritize**
   - Read `references/scoring-model.md` before scoring.
   - Score each opportunity with explicit evidence and confidence.
   - Rank by validation priority, not excitement. Penalize opportunities with unclear buyer, weak channel, or untestable assumptions.

8. **Design validation**
   - Convert each top opportunity into a 7/14/30-day validation plan.
   - Specify the riskiest assumption, cheapest test, success threshold, required asset, expected signal, and kill condition.

9. **Package the output**
   - Deliver: executive summary, opportunity scorecard, top opportunity cards, no-go list, validation roadmap, source log, open questions.
   - Always create `11-key-points.md` with concise takeaways.
   - After saving files, end the chat response with the folder path and three distilled sections: `行业现状`, `关键痛点`, and `机会方向`.

## Output Discipline

- Do not claim an opportunity is attractive unless the buyer, pain, channel, and test are clear.
- Do not use market size as the primary reason to recommend an opportunity.
- Do not confuse content popularity with monetizable demand; tie content signals to buyer intent or acquisition strategy.
- Keep sources linked near the claims they support, and put the full list in `sources.md` when creating a workspace.
- Do not leave the result only in chat. The saved folder is part of the deliverable every time.
- Match the analysis lens to the confirmed user context. For example, a consulting company needs service packages, buyers, project entry points, delivery assets, and pricing logic; a founder needs MVPs, channels, validation tests, and execution risks.

## Reference Files

- `references/scoring-model.md`: scoring rubric, confidence rules, and opportunity card schema.
- `references/output-contracts.md`: Obsidian-ready folder structure and required deliverables.
