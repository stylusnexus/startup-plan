# AGENTS.md

## What this repo is

The Startup Plan: a short written guide for people starting to build software with AI coding agents (Claude Code, Codex, Cursor). It is one web page (`index.html`, published on GitHub Pages) plus two copy-paste prompts (`prompts/`). It covers a six-step working loop, the four mistakes that cost us the most time, and a first week of moves. It points readers to [full-starter](https://github.com/stylusnexus/full-starter) (a template to fork) and [agent-plugins](https://github.com/stylusnexus/agent-plugins) (skills to install).

## Who it is for

Anyone about to build with an AI coding agent who wants a working method first, or whose agent says "done" and they don't trust it. Don't assume the reader is an engineer.

## What it is not

- Not software. There is nothing to install.
- Not a course or the full guide. It is kept short on purpose.
- Not research. It is one team's experience, not a study or a benchmark.
- Not tied to one tool. Some examples use Claude Code file names; the loop applies to any coding agent.

Don't expand it into any of those. Add detail by linking out, not by growing the page.

## Editing rules

- `index.html` is one self-contained file. No build step, no dependencies.
- Each prompt lives in two places: a file under `prompts/` and a copy in a `<pre>` on the page. Change both, then run `python3 scripts/check-sync.py`. It must exit 0.
- The two longer source guides are private. Never link to them from this public repo.
- Check the page at a phone width (about 390px) after layout edits; it must not scroll sideways.
- Write as "we at Stylus Nexus", not "I".
- The repo is MIT licensed. Don't add content that isn't ours to license.
