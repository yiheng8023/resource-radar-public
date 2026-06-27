from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "NOTICE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".gitattributes",
    ".gitignore",
    ".github/workflows/validate.yml",
    "schemas/resource.schema.json",
    "policies/scoring.json",
    "policies/lifecycle.json",
    "policies/domain-taxonomy.json",
    "data/demo/resources.json",
    "docs/public-private-boundary.md",
    "docs/design-basis.md",
    "docs/source-policy.md",
    "docs/universal-taxonomy.md",
    "docs/relationship-map.md",
    "docs/automation-boundary.md",
    "outputs/demo-report.md",
    "outputs/demo-report.json",
]

PRIVATE_ONLY_TERMS = [
    "ghp_",
    "github_pat_",
    "oauth token",
    "cookie value",
    "private key",
    "c:\\users\\",
    "/users/",
    "appdata",
    "browser profile",
    "session cookie",
]

ALLOWED_LANES = {
    "tool",
    "reference",
    "learning",
    "bookmark_seed",
    "skill_candidate",
    "dataset",
    "workflow",
    "standard",
}


def fail(message: str) -> None:
    raise SystemExit(f"verification failed: {message}")


def read_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def verify_required_files() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(f"missing required file: {rel}")


def verify_language_links() -> None:
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    if "English | [简体中文](README.zh-CN.md)" not in english:
        fail("README.md language switch is missing")
    if "[English](README.md) | 简体中文" not in chinese:
        fail("README.zh-CN.md language switch is missing")
    english_lower = english.lower()
    for phrase in [
        "agent-neutral",
        "tool-neutral",
        "private candidate pool",
        "stars as optional and weak",
        "downstream targets",
        "system context",
        "open-resource-governance/docs/system-topology.md",
        "public-safe resource structure, scoring/lifecycle examples",
    ]:
        if phrase not in english_lower:
            fail(f"README.md missing phrase: {phrase}")
    for phrase in [
        "系统位置",
        "open-resource-governance/docs/system-topology.md",
        "公开安全资源结构",
    ]:
        if phrase not in chinese:
            fail(f"README.zh-CN.md missing phrase: {phrase}")


def verify_policy_versions() -> None:
    for rel in ["policies/scoring.json", "policies/lifecycle.json", "data/demo/resources.json"]:
        if read_json(rel).get("schema_version") != 1:
            fail(f"{rel} schema_version must be 1")
    if read_json("policies/domain-taxonomy.json").get("schema_version") != "0.1.0":
        fail("policies/domain-taxonomy.json schema_version must be 0.1.0")


def verify_domain_taxonomy() -> set[str]:
    data = read_json("policies/domain-taxonomy.json")
    seen: set[str] = set()
    orders: set[int] = set()
    for item in data.get("domains", []):
        for key in ["id", "order", "display_name", "zh_name", "description"]:
            if key not in item:
                fail(f"domain taxonomy item missing {key}")
        if item["id"] in seen:
            fail(f"duplicate domain id: {item['id']}")
        if item["order"] in orders:
            fail(f"duplicate domain order: {item['order']}")
        seen.add(item["id"])
        orders.add(item["order"])
    if len(seen) < 20:
        fail("domain taxonomy must include the 18 main domains plus reserved fallback/archive domains")
    for required in ["90_low_trust_fallback_resources", "99_archive"]:
        if required not in seen:
            fail(f"domain taxonomy missing reserved domain: {required}")
    return seen


def verify_resources() -> None:
    data = read_json("data/demo/resources.json")
    domain_ids = verify_domain_taxonomy()
    ids = set()
    for item in data.get("resources", []):
        for key in [
            "id",
            "name",
            "url",
            "category",
            "source_type",
            "trust_tier",
            "visibility",
            "downstream_lanes",
            "license_review",
            "signals",
        ]:
            if key not in item:
                fail(f"resource missing {key}: {item.get('id', '<unknown>')}")
        if item["id"] in ids:
            fail(f"duplicate resource id: {item['id']}")
        ids.add(item["id"])
        parsed = urlparse(item["url"])
        if parsed.scheme != "https" or not parsed.netloc:
            fail(f"resource url must be public https: {item['id']}")
        if item["category"] not in domain_ids:
            fail(f"resource category is not in domain taxonomy: {item['id']} -> {item['category']}")
        if item["visibility"] != "public":
            fail(f"resource visibility must be public: {item['id']}")
        lanes = set(item["downstream_lanes"])
        if not lanes or lanes - ALLOWED_LANES:
            fail(f"invalid downstream lanes for {item['id']}")
        if item["license_review"].get("status") not in {"clear", "needs_manual_review", "not_applicable"}:
            fail(f"invalid license status for {item['id']}")
        signals = item["signals"]
        for signal in ["authority", "documentation", "freshness", "maintenance", "downstream_fit", "private_risk"]:
            value = signals.get(signal)
            if not isinstance(value, int) or value < 0 or value > 5:
                fail(f"invalid signal {signal} for {item['id']}")


def verify_public_safety_text() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel == "scripts/verify.py":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for term in PRIVATE_ONLY_TERMS:
            if term in text:
                fail(f"private-only term found in {rel}: {term}")


def verify_generated_outputs() -> None:
    subprocess.run(
        [sys.executable, "-B", str(ROOT / "scripts" / "run_demo.py"), "--check"],
        cwd=ROOT,
        check=True,
    )


def main() -> None:
    verify_required_files()
    verify_language_links()
    verify_policy_versions()
    verify_resources()
    verify_public_safety_text()
    verify_generated_outputs()
    print("resource-radar-public verification passed")


if __name__ == "__main__":
    main()
