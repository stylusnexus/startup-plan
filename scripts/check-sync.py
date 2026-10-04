#!/usr/bin/env python3
"""Check that each prompt on index.html matches its file under prompts/.

The prompts live in two places: a plain file (so people can curl it) and a
<pre> on the page (so people can copy it). They must stay identical.
Usage: python3 scripts/check-sync.py   (exit 1 on any difference)
"""
import html
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
page = (root / "index.html").read_text()

PROMPTS = {
    "validation-gate-prompt": "prompts/validation-gate.md",
    "agentic-principles-prompt": "prompts/agentic-principles.md",
}

failed = 0
for pre_id, rel in PROMPTS.items():
    m = re.search(rf'<pre id="{pre_id}"[^>]*>(.*?)</pre>', page, re.S)
    f = re.search(r"```\n(.*?)\n```", (root / rel).read_text(), re.S)
    if not m or not f:
        print(f"✗ {rel}: could not find the prompt block (page id {pre_id})")
        failed += 1
        continue
    on_page = html.unescape(m.group(1)).strip()
    in_file = f.group(1).strip()
    if on_page == in_file:
        print(f"✓ {rel} matches index.html")
    else:
        print(f"✗ {rel} differs from index.html#{pre_id}")
        failed += 1

sys.exit(1 if failed else 0)
