"""Run after build_bundle.py: ensure every source reaches the portable bundle intact."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
bundle = (root / 'dist/learn-from-failure-bundle.md').read_text()
sources = [root / 'AGENTS.md', root / 'LEGAL.md', root / 'CHECKLIST.md']
sources += [p for p in (root / 'cases').rglob('*.md') if p.name != '_template.md']
sources += list((root / 'problems').glob('*.md'))
for source in sources:
    assert source.read_text() in bundle, f'Missing or stale source: {source}'
print('OK — shared instructions, legal rules and case sources are in the bundle.')
