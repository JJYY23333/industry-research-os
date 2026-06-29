# Industry Research OS Skills

一组用于行业研究与机会分析的 Codex skills。目标不是让 Codex 只写一篇一次性报告，而是把行业信息沉淀成可持续更新、可检索、可复用的 Markdown 研究系统。

## 包含的 Skills

### 1. Industry Research OS

`industry-research-os` 用于结构化行业研究。

适合场景：

- 陌生行业快速入门
- 产业链和玩家地图梳理
- 商业模式、供应链、单位经济模型分析
- 行业趋势、用户场景、机会清单整理
- 生成 Obsidian 可用的行业研究知识库
- 周期性行业情报周报

使用示例：

```text
Use $industry-research-os to analyze the internet grocery industry in China and create a Markdown research database.
```

```text
帮我做新能源汽车产业分析，并沉淀成 Obsidian 可用的行业研究库。
```

### 2. Industry Opportunity Analysis

`industry-opportunity-analysis` 用于行业机会分析和验证优先级排序。

它会把一个目标行业拆成机会管道：先确认你的行业、工作性质、兴趣方向和想要的结果，再梳理行业地图、用户痛点、竞品缺口、产品和内容需求，用评分模型筛出最值得验证的机会，并输出 7/14/30 天验证计划。

适合场景：

- 找产品机会
- 找内容机会
- 找细分人群切入点
- 拆解竞品弱点
- 判断一个行业是否值得进入
- 对多个机会做评分和优先级排序
- 输出机会卡片、验证实验和行动路线图
- 从咨询公司、创业者、投资人、产品经理、销售或运营等不同视角切换分析口径
- 每次分析都新建文件夹保存结果，并在结尾提炼行业现状、痛点和机会

使用示例：

```text
Use $industry-opportunity-analysis to analyze the US pet supplements industry and produce ranked opportunity cards with validation tests.
```

```text
用 $industry-opportunity-analysis 分析美国宠物营养品行业，找出适合小团队验证的前 10 个机会。
```

```text
帮我分析跨境电商 SaaS 的行业机会，输出机会评分表、Top 机会卡片和 30 天验证计划。
```

## 安装

把需要的 skill 复制到 Codex skills 目录：

```bash
cp -R skills/industry-research-os ~/.codex/skills/
cp -R skills/industry-opportunity-analysis ~/.codex/skills/
```

然后新开一个 Codex 会话，或刷新 skill 列表。

## 目录结构

```text
skills/
├── industry-research-os/
│   ├── SKILL.md
│   ├── agents/
│   ├── references/
│   └── scripts/
└── industry-opportunity-analysis/
    ├── SKILL.md
    ├── agents/
    └── references/
```

## Industry Opportunity Analysis 输出内容

这个 skill 的核心交付物包括：

- 行业机会分析摘要
- 用户痛点地图
- 竞品缺口地图
- 产品和 offer 地图
- 关键词和内容机会地图
- 商业模式机会地图
- Top 机会卡片
- 机会评分表
- No-go / 低优先级机会清单
- 7/14/30 天验证计划
- 周期性监控模板

标准工作区结构：

```text
<industry-opportunity-os>/
├── README.md
├── 00-scope.md
├── 01-industry-overview.md
├── 02-user-pain-points/
├── 03-competitors/
├── 04-products-offers/
├── 05-keywords-content/
├── 06-business-models/
├── 07-opportunity-cards/
├── 08-scorecard.md
├── 09-validation-plan.md
├── 10-monitoring/
├── 11-key-points.md
└── sources.md
```

## 机会评分模型

`industry-opportunity-analysis` 会从以下维度给机会打分：

- 痛点强度
- 需求证据
- 竞争缺口
- 渠道可达性
- 变现能力
- 执行匹配度
- 验证速度
- 趋势支撑

它不会只因为市场规模大就推荐机会。一个机会必须同时说明：

- 谁是用户和买单方
- 解决什么高频或高价值痛点
- 为什么现有方案不够好
- 可以通过什么渠道触达
- 如何变现
- 最便宜的验证实验是什么
- 成功标准和放弃条件是什么

## 推荐使用方式

如果你只是想理解一个行业，先用：

```text
Use $industry-research-os ...
```

如果你已经有一个行业方向，想判断哪里值得切入，直接用：

```text
Use $industry-opportunity-analysis ...
```

如果你要做完整研究，可以组合使用：

```text
先用 $industry-research-os 建立行业研究库，再用 $industry-opportunity-analysis 基于研究库输出机会评分和验证计划。
```

## License

MIT
