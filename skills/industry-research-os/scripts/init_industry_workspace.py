#!/usr/bin/env python3
import argparse
import json
from datetime import date
from pathlib import Path


DIRS = [
    "02-players",
    "03-business-models",
    "04-supply-chain",
    "05-unit-economics",
    "06-users-and-scenarios",
    "07-trends",
    "08-opportunities",
    "09-weekly-intelligence",
]


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize an industry research workspace.")
    parser.add_argument("--industry", required=True)
    parser.add_argument("--region", default="")
    parser.add_argument("--time-range", default="")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path(args.output)
    root.mkdir(parents=True, exist_ok=True)
    for dirname in DIRS:
        (root / dirname).mkdir(exist_ok=True)

    today = date.today().isoformat()
    meta = {
        "industry": args.industry,
        "region": args.region,
        "time_range": args.time_range,
        "last_update": today,
        "status": "draft",
        "completed_sections": [],
        "open_questions": [],
        "source_grades": {"A": 0, "B": 0, "C": 0, "D": 0},
    }
    write_if_missing(root / "research_state.json", json.dumps(meta, ensure_ascii=False, indent=2) + "\n")

    header = (
        f"行业：{args.industry}\n"
        f"地区：{args.region}\n"
        f"时间范围：{args.time_range}\n"
        f"最后更新：{today}\n"
    )
    write_if_missing(
        root / "README.md",
        f"# {args.industry}行业研究库\n\n{header}\n这个目录用于沉淀结构化产业分析资料。\n",
    )
    write_if_missing(
        root / "00-overview.md",
        f"# {args.industry}行业总览\n\n类型：行业总览\n{header}状态：草稿\n置信度：\n一句话结论：\n\n## 核心事实\n\n-\n\n## 分析判断\n\n-\n\n## 关键指标\n\n-\n\n## 相关玩家\n\n-\n\n## 风险与不确定性\n\n-\n\n## 待验证问题\n\n-\n\n## 来源\n\n-\n",
    )
    write_if_missing(
        root / "sources.md",
        f"# 来源索引\n\n类型：来源索引\n{header}状态：草稿\n置信度：\n一句话结论：\n\n## A 级来源\n\n-\n\n## B 级来源\n\n-\n\n## C 级来源\n\n-\n\n## D 级来源\n\n-\n\n## 来源\n\n-\n",
    )
    write_if_missing(
        root / "09-weekly-intelligence" / "模板.md",
        f"# 周报模板\n\n类型：周报模板\n{header}状态：草稿\n置信度：\n一句话结论：\n\n## 本周摘要\n\n-\n\n## 新事实\n\n| 日期 | 事实 | 来源等级 | 来源 |\n| --- | --- | --- | --- |\n|  |  |  |  |\n\n## 玩家变化\n\n## 商业模式变化\n\n## 风险事件\n\n## 机会变化\n\n## 下周动作\n\n-\n\n## 来源\n\n-\n",
    )
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
