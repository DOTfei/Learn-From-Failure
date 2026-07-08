#!/usr/bin/env python3
"""Build docs/data.json for the GitHub Pages case browser (docs/index.html).

No external dependencies — this repo's case files follow a strict, simple Markdown subset
(headers, bullet lists, bold, links, paragraphs), so a small hand-rolled renderer is enough and
keeps the whole site dependency-free and buildable with plain python3.

Run: python3 scripts/build_site.py
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES_DIR = ROOT / "cases"
OUT_PATH = ROOT / "docs" / "data.json"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm, m.group(2)


def render_inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    return text


def render_body(body: str) -> str:
    lines = body.strip("\n").splitlines()
    html_parts = []
    list_buffer = []
    para_buffer = []

    def flush_list():
        if list_buffer:
            items = "".join(f"<li>{render_inline(i)}</li>" for i in list_buffer)
            html_parts.append(f"<ul>{items}</ul>")
            list_buffer.clear()

    def flush_para():
        if para_buffer:
            html_parts.append(f"<p>{render_inline(' '.join(para_buffer))}</p>")
            para_buffer.clear()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_list()
            flush_para()
            continue
        header_match = re.match(r"^(#{2,3})\s+(.*)$", stripped)
        if header_match:
            flush_list()
            flush_para()
            level = 4 if len(header_match.group(1)) == 2 else 5
            html_parts.append(f"<h{level}>{render_inline(header_match.group(2))}</h{level}>")
            continue
        bullet_match = re.match(r"^-\s+(.*)$", stripped)
        if bullet_match:
            flush_para()
            list_buffer.append(bullet_match.group(1))
            continue
        flush_list()
        para_buffer.append(stripped)

    flush_list()
    flush_para()
    return "".join(html_parts)


def load_case(path: Path, is_contrast: bool = False) -> dict:
    fm, body = parse_frontmatter(path.read_text())
    raw_tags = fm.get("failure_types") or fm.get("failure_types_avoided", "")
    tags = [t.strip() for t in raw_tags.strip("[]").split(",") if t.strip()]
    return {
        "slug": fm.get("slug", path.stem),
        "company": fm.get("company", path.stem),
        "industry": fm.get("industry", ""),
        "founded": fm.get("founded", ""),
        "failed": fm.get("failed", ""),
        "severity": fm.get("severity", ""),
        "tags": tags,
        "is_contrast": is_contrast,
        "contrasts_with": fm.get("contrasts_with", ""),
        "html": render_body(body),
    }


def main() -> None:
    cases = []
    for path in sorted(CASES_DIR.glob("*.md")):
        if path.name in {"_template.md", "_index.md"} or path.name.startswith("."):
            continue
        cases.append(load_case(path))

    contrasts_dir = CASES_DIR / "contrasts"
    if contrasts_dir.is_dir():
        for path in sorted(contrasts_dir.glob("*.md")):
            if path.name.startswith("."):
                continue
            cases.append(load_case(path, is_contrast=True))

    all_tags = sorted({t for c in cases for t in c["tags"]})

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps({"cases": cases, "tags": all_tags}, indent=1, ensure_ascii=False))
    print(f"Wrote {OUT_PATH} ({len(cases)} cases, {len(all_tags)} tags)")


if __name__ == "__main__":
    main()
