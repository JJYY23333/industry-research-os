# Output Contracts

## Workspace Structure

```text
<industry-name>/
├── README.md
├── 00-overview.md
├── 01-field-rules.md
├── 02-players/
├── 03-business-models/
├── 04-supply-chain/
├── 05-unit-economics/
├── 06-users-and-scenarios/
├── 07-trends/
├── 08-opportunities/
├── 09-weekly-intelligence/
└── sources.md
```

## Minimum First Pass

For a first-pass industry database, create at least:

- `README.md`
- `00-overview.md`
- `01-field-rules.md`
- `sources.md`
- 3-5 player files under `02-players/`
- 2-4 model files under `03-business-models/`
- `04-supply-chain/供应链地图.md`
- `05-unit-economics/单位经济模型.md`
- `06-users-and-scenarios/用户场景.md`
- `07-trends/趋势判断.md`
- `08-opportunities/机会清单.md`
- `09-weekly-intelligence/模板.md`

## Research State

When the workflow is long-running, create `research_state.json`:

```json
{
  "industry": "",
  "region": "",
  "time_range": "",
  "last_update": "",
  "status": "draft",
  "completed_sections": [],
  "open_questions": [],
  "source_grades": {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
  }
}
```

