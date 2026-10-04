#!/usr/bin/env python3
"""Concatenate the whole knowledge base into one file for platforms with no filesystem/browsing
access (ChatGPT Custom GPT knowledge, Gemini Gem knowledge, a system prompt for a raw API call,
etc.). Run: python3 scripts/build_bundle.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES_DIR = ROOT / "cases"
OUT_PATH = ROOT / "dist" / "learn-from-failure-bundle.md"

PREAMBLE = "# Learn From Failure — Bundled Knowledge Base\n\n"

def main() -> None:
    parts = [PREAMBLE, (ROOT / "AGENTS.md").read_text(), "\n\n---\n\n",
             (ROOT / "LEGAL.md").read_text(), "\n\n---\n\n"]

    index = CASES_DIR / "_index.md"
    parts.append(f"<!-- ==== cases/_index.md ==== -->\n\n{index.read_text()}\n\n---\n\n")

    checklist = ROOT / "CHECKLIST.md"
    if checklist.exists():
        parts.append(f"<!-- ==== CHECKLIST.md ==== -->\n\n{checklist.read_text()}\n\n---\n\n")

    case_files = sorted(
        p for p in CASES_DIR.glob("*.md")
        if p.name not in {"_template.md", "_index.md"} and not p.name.startswith(".")
    )
    for path in case_files:
        parts.append(f"<!-- ==== cases/{path.name} ==== -->\n\n{path.read_text()}\n\n---\n\n")

    contrasts_dir = CASES_DIR / "contrasts"
    if contrasts_dir.is_dir():
        for path in sorted(p for p in contrasts_dir.glob("*.md") if not p.name.startswith(".")):
            parts.append(
                f"<!-- ==== cases/contrasts/{path.name} ==== -->\n\n{path.read_text()}\n\n---\n\n"
            )

    for path in sorted((ROOT / "problems").glob("*.md")):
        parts.append(f"<!-- ==== problems/{path.name} ==== -->\n\n{path.read_text()}\n\n---\n\n")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("".join(parts))
    size_kb = OUT_PATH.stat().st_size / 1024
    print(f"Wrote {OUT_PATH} ({size_kb:.0f} KB, {len(case_files)} cases + "
          f"{len(list(contrasts_dir.glob('*.md'))) if contrasts_dir.is_dir() else 0} contrast file(s))")


if __name__ == "__main__":
    main()
