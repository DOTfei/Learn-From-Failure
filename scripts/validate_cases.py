#!/usr/bin/env python3
"""Validate case files: required frontmatter, required sections, index consistency."""
import re
import sys
from pathlib import Path

CASES_DIR = Path(__file__).resolve().parent.parent / "cases"
REQUIRED_FRONTMATTER = ["slug", "company", "industry", "founded", "failed", "failure_types", "severity"]
REQUIRED_SECTIONS = [
    "## What happened",
    "## Root causes",
    "## Warning signs",
    "## Questions this raises for another company",
]
KNOWN_TAGS = {
    "fraud_and_ethics",
    "governance_and_leadership",
    "financial_management",
    "disruption_denial",
    "product_market_fit",
    "scaling_too_fast",
    "culture_and_talent",
    "safety_and_quality",
}
SKIP = {"_template.md", "_index.md"}


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm


def main() -> int:
    errors = []
    case_files = sorted(
        p for p in CASES_DIR.glob("*.md")
        if p.name not in SKIP and not p.name.startswith(".")
    )

    if not case_files:
        print("No case files found.")
        return 1

    index_text = (CASES_DIR / "_index.md").read_text()

    for path in case_files:
        text = path.read_text()
        fm = parse_frontmatter(text)
        for field in REQUIRED_FRONTMATTER:
            if field not in fm or not fm[field]:
                errors.append(f"{path.name}: missing frontmatter field '{field}'")

        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{path.name}: missing required section '{section}'")

        if "## Sources" not in text:
            errors.append(f"{path.name}: missing '## Sources' section (add at least one reference, "
                           f"or explicitly note this is a private/unsourced case)")

        raw_tags = fm.get("failure_types", "")
        tags = [t.strip() for t in raw_tags.strip("[]").split(",") if t.strip()]
        if not tags:
            errors.append(f"{path.name}: failure_types is empty")
        unknown = [t for t in tags if t not in KNOWN_TAGS]
        if unknown:
            errors.append(
                f"{path.name}: unrecognized failure_types tag(s) {unknown} — "
                f"add them to the taxonomy in cases/_index.md if intentional, "
                f"or fix a typo"
            )

        if path.name not in index_text:
            errors.append(f"{path.name}: not linked from cases/_index.md")

        # Legal-accuracy guard: "fraud_conviction" asserts a court found someone guilty.
        # If the body never actually says so, this is very likely describing an unresolved
        # allegation/indictment/civil finding instead — a meaningful factual (and defamation-risk)
        # difference. This is a heuristic, not proof of correctness either way; a human should
        # still sanity-check any case involving a real person's guilt.
        severity = fm.get("severity", "")
        if "fraud_conviction" in severity:
            body_lower = text.lower()
            conviction_words = ["convicted", "guilty", "conviction", "sentenced"]
            if not any(w in body_lower for w in conviction_words):
                errors.append(
                    f"{path.name}: severity includes 'fraud_conviction' but the body doesn't "
                    f"contain a word like 'convicted'/'sentenced'/'guilty' — double check this "
                    f"is an actual criminal conviction, not just charges/an indictment/a civil "
                    f"or regulatory finding (use 'fraud_charges_pending' if so, and say plainly "
                    f"in the text that it's unresolved)"
                )

    contrasts_dir = CASES_DIR / "contrasts"
    contrast_files = (
        sorted(p for p in contrasts_dir.glob("*.md") if not p.name.startswith("."))
        if contrasts_dir.is_dir() else []
    )
    for path in contrast_files:
        text = path.read_text()
        fm = parse_frontmatter(text)
        for field in ("slug", "company", "contrasts_with"):
            if field not in fm or not fm[field]:
                errors.append(f"contrasts/{path.name}: missing frontmatter field '{field}'")
        if "## Sources" not in text:
            errors.append(f"contrasts/{path.name}: missing '## Sources' section")

    if errors:
        print(f"Found {len(errors)} issue(s):\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK — {len(case_files)} case files and {len(contrast_files)} contrast file(s) validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
