---
name: industry-research-os
description: Build structured industry and sector research systems. Use when Codex needs to do产业分析, 行业分析, 陌生行业研究, market mapping, competitor/player analysis, business model analysis, supply chain analysis, unit economics analysis, opportunity discovery, or recurring industry intelligence reports. Also use when the user asks to turn research into an Obsidian-ready Markdown database or knowledge base instead of a one-off report.
---

# Industry Research OS

Use this skill to turn industry research into a durable Markdown research database, not a one-off answer.

## Workflow

1. Clarify the research scope if missing:
   - industry
   - region
   - time range
   - research goal
   - output location
2. Create an industry workspace with `scripts/init_industry_workspace.py` when the user wants files.
3. Read `references/field-rules.md` before writing research documents.
4. Read `references/output-contracts.md` when creating or validating the folder structure.
5. For current industry facts, search for recent primary or high-quality sources before making claims.
6. Build the research database in this order:
   - overview
   - players
   - business models
   - supply chain
   - unit economics
   - users and scenarios
   - trends
   - opportunities
   - sources
7. Distinguish every important claim as fact, judgment, hypothesis, or to-verify.
8. Validate the workspace with `scripts/validate_industry_workspace.py`.

## Source Discipline

Prefer sources in this order:

1. Company annual reports, SEC/HKEX filings, company announcements, regulatory documents.
2. Securities reports, official media, industry associations, research institutes.
3. Media reports, industry articles, interviews, encyclopedic references.
4. Personal judgment, social discussion, unverified clues.

Use low-grade sources for leads, not as the only support for important numbers.

## Output Rules

- Write Markdown files with stable fields from `references/field-rules.md`.
- Keep each file focused on one object: one player, one business model, one trend, or one opportunity.
- Put source links in `sources.md` and repeat the most relevant sources in each document.
- Record uncertainty explicitly instead of smoothing it away.
- Do not mix platform, self-operated front warehouse, store-warehouse, and community group-buying models without first separating them.

## Scripts

Initialize a workspace:

```bash
python scripts/init_industry_workspace.py --industry "互联网买菜" --region "中国大陆" --time-range "2024-2026" --output ./互联网买菜
```

Validate a workspace:

```bash
python scripts/validate_industry_workspace.py ./互联网买菜
```

