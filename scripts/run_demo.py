from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESOURCES_PATH = ROOT / "data" / "demo" / "resources.json"
SCORING_PATH = ROOT / "policies" / "scoring.json"
LIFECYCLE_PATH = ROOT / "policies" / "lifecycle.json"
OUTPUT_MD = ROOT / "outputs" / "demo-report.md"
OUTPUT_JSON = ROOT / "outputs" / "demo-report.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def score_resource(resource: dict, weights: dict) -> int:
    signals = resource["signals"]
    raw = (
        signals["authority"] * weights["authority"]
        + signals["documentation"] * weights["documentation"]
        + signals["freshness"] * weights["freshness"]
        + signals["maintenance"] * weights["maintenance"]
        + signals["downstream_fit"] * weights["downstream_fit"]
        + (5 - signals["private_risk"]) * weights["private_risk_inverse"]
    )
    return round((raw / 5) * 100)


def classify(score: int, license_status: str, lifecycle: dict) -> str:
    for rule in lifecycle["rules"]:
        if score >= rule["minimum_score"] and license_status in rule["requires_license_status"]:
            return rule["state"]
    return "candidate"


def build_report() -> tuple[str, dict]:
    resources = load_json(RESOURCES_PATH)["resources"]
    scoring = load_json(SCORING_PATH)
    lifecycle = load_json(LIFECYCLE_PATH)
    weights = scoring["weights"]

    rows = []
    for resource in sorted(resources, key=lambda item: item["id"]):
        score = score_resource(resource, weights)
        state = classify(score, resource["license_review"]["status"], lifecycle)
        rows.append(
            {
                "id": resource["id"],
                "name": resource["name"],
                "url": resource["url"],
                "category": resource["category"],
                "source_type": resource["source_type"],
                "trust_tier": resource["trust_tier"],
                "downstream_lanes": resource["downstream_lanes"],
                "license_status": resource["license_review"]["status"],
                "score": score,
                "state": state,
            }
        )

    report_json = {
        "schema_version": 1,
        "generated_from": [
            "data/demo/resources.json",
            "policies/scoring.json",
            "policies/lifecycle.json",
        ],
        "resource_count": len(rows),
        "resources": rows,
    }

    lines = [
        "# Resource Radar Demo Report",
        "",
        "This deterministic report is generated from public-safe demo fixtures.",
        "",
        f"Resource count: {len(rows)}",
        "",
        "| ID | Name | Category | Type | Trust | Score | State | Lanes |",
        "| --- | --- | --- | --- | --- | ---: | --- | --- |",
    ]
    for row in rows:
        lanes = ", ".join(row["downstream_lanes"])
        lines.append(
            f"| `{row['id']}` | [{row['name']}]({row['url']}) | {row['category']} | "
            f"{row['source_type']} | {row['trust_tier']} | {row['score']} | {row['state']} | {lanes} |"
        )

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Scores are review aids, not automatic promotion decisions.",
            "- `needs_manual_review` license status blocks blind downstream import.",
            "- This demo does not call external services or mutate accounts.",
            "",
        ]
    )

    return "\n".join(lines), report_json


def write_outputs(markdown: str, report_json: dict) -> None:
    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD.write_text(markdown, encoding="utf-8", newline="\n")
    OUTPUT_JSON.write_text(
        json.dumps(report_json, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def check_outputs(markdown: str, report_json: dict) -> None:
    expected_json = json.dumps(report_json, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if not OUTPUT_MD.is_file() or OUTPUT_MD.read_text(encoding="utf-8") != markdown:
        raise SystemExit("demo report markdown is out of date; run python -B scripts/run_demo.py")
    if not OUTPUT_JSON.is_file() or OUTPUT_JSON.read_text(encoding="utf-8") != expected_json:
        raise SystemExit("demo report json is out of date; run python -B scripts/run_demo.py")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check generated outputs without writing")
    args = parser.parse_args()
    markdown, report_json = build_report()
    if args.check:
        check_outputs(markdown, report_json)
        print("demo report is up to date")
    else:
        write_outputs(markdown, report_json)
        print("generated demo report")


if __name__ == "__main__":
    main()
