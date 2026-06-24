# Industry Research OS

Industry Research OS is a Codex skill for structured industry analysis.

It helps Codex turn market research into a durable Markdown knowledge base instead of a one-off report. Use it for industry analysis, sector research, player mapping, business model analysis, supply chain analysis, unit economics, opportunity discovery, and recurring industry intelligence reports.

## 中文说明

Industry Research OS 是一个用于结构化产业分析的 Codex skill。

它的目标不是让 Codex 只输出一篇一次性行业报告，而是把产业研究沉淀成一套可以持续更新、检索和复用的 Markdown 知识库。适合用于产业分析、行业分析、陌生市场研究、玩家分析、商业模式拆解、供应链分析、单位经济模型分析、机会发现，以及周期性的行业情报周报。

### 它会生成什么

这个 skill 会引导 Codex 创建一套适合导入 Obsidian 的行业研究目录：

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

### 安装

把 skill 文件夹复制到 Codex 的 skills 目录：

```bash
cp -R skills/industry-research-os ~/.codex/skills/
```

然后新开一个 Codex 会话，或刷新 skill 列表。

### 使用示例

```text
Use $industry-research-os to analyze the internet grocery industry in China and create a Markdown research database.
```

```text
帮我做新能源汽车产业分析，并沉淀成 Obsidian 可用的行业研究库。
```

```text
用产业分析框架研究跨境电商 SaaS，输出玩家、商业模式、供应链、单位经济模型和机会清单。
```

### Skill 内容

- `skills/industry-research-os/SKILL.md`：触发描述和主工作流。
- `skills/industry-research-os/references/field-rules.md`：行业研究文档的固定字段规则。
- `skills/industry-research-os/references/output-contracts.md`：行业研究库的目录结构约定。
- `skills/industry-research-os/references/research-quality-rules.md`：来源等级、事实/判断/假设标注规则。
- `skills/industry-research-os/scripts/init_industry_workspace.py`：初始化行业研究库。
- `skills/industry-research-os/scripts/validate_industry_workspace.py`：校验行业研究库结构。
- `skills/industry-research-os/assets/templates/`：Markdown 模板。

## What It Produces

The skill guides Codex to create an Obsidian-friendly research workspace:

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

## Install

Copy the skill folder into your Codex skills directory:

```bash
cp -R skills/industry-research-os ~/.codex/skills/
```

Then start a new Codex session or refresh your skill list.

## Usage

Example prompts:

```text
Use $industry-research-os to analyze the internet grocery industry in China and create a Markdown research database.
```

```text
帮我做新能源汽车产业分析，并沉淀成 Obsidian 可用的行业研究库。
```

```text
用产业分析框架研究跨境电商 SaaS，输出玩家、商业模式、供应链、单位经济模型和机会清单。
```

## Skill Contents

- `skills/industry-research-os/SKILL.md`: trigger description and main workflow.
- `skills/industry-research-os/references/field-rules.md`: stable field rules for research documents.
- `skills/industry-research-os/references/output-contracts.md`: expected workspace structure.
- `skills/industry-research-os/references/research-quality-rules.md`: source grading and claim discipline.
- `skills/industry-research-os/scripts/init_industry_workspace.py`: initialize a research workspace.
- `skills/industry-research-os/scripts/validate_industry_workspace.py`: validate a research workspace.
- `skills/industry-research-os/assets/templates/`: Markdown templates.

## License

MIT
