#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


REQUIRED_PATHS = [
    "README.md",
    "00-overview.md",
    "sources.md",
    "02-players",
    "03-business-models",
    "04-supply-chain",
    "05-unit-economics",
    "06-users-and-scenarios",
    "07-trends",
    "08-opportunities",
    "09-weekly-intelligence",
]

REQUIRED_COMMON_FIELDS = [
    "类型：",
    "行业：",
    "地区：",
    "时间范围：",
    "最后更新：",
    "状态：",
    "置信度：",
    "一句话结论：",
    "## 来源",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an industry research workspace.")
    parser.add_argument("workspace")
    args = parser.parse_args()

    root = Path(args.workspace)
    errors = []

    if not root.exists():
        errors.append(f"workspace does not exist: {root}")
    else:
        for item in REQUIRED_PATHS:
            if not (root / item).exists():
                errors.append(f"missing required path: {item}")

        state = root / "research_state.json"
        if state.exists():
            try:
                json.loads(state.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"invalid research_state.json: {exc}")

        for md in root.rglob("*.md"):
            text = md.read_text(encoding="utf-8")
            if md.name == "README.md":
                continue
            missing = [field for field in REQUIRED_COMMON_FIELDS if field not in text]
            if missing:
                errors.append(f"{md.relative_to(root)} missing fields: {', '.join(missing)}")

    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

