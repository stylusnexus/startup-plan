# The Startup Plan

A short written guide for people starting to build software with AI coding agents such as Claude Code, Codex, or Cursor. It lays out a six-step working loop, the four mistakes that cost us the most time, and what to do in your first week.

**Read it:** https://stylusnexus.github.io/startup-plan/

By [Stylus Nexus](https://github.com/stylusnexus).

## Use it when

- You're about to start a project with an AI coding agent and want a working method before you write code
- Your agent says "done" and you don't trust it
- You want standing rules you can paste into your project's instructions file (see the prompts below)

## What's here

- **The loop:** think, plan, build, verify, review, ship. Think widens the options and plan commits to one. Verify is a mechanical pass/fail; review needs judgment.
- **Four failures:** the mega-agent, the mega-CLAUDE.md, knowledge that lives only in a chat, and prompting by gut feel. One instinct sits behind all four.
- **First moves:** concrete things to do this week
- **Where to go next:** [full-starter](https://github.com/stylusnexus/full-starter) is a project template you fork to set the workflow up. [agent-plugins](https://github.com/stylusnexus/agent-plugins) holds skills you install into a project you already have.

## What this is NOT

- **Not software.** It's a web page and two prompt files. There's nothing to install.
- **Not a course or the full guide.** It's the short version of two longer guides we wrote for ourselves, kept short on purpose.
- **Not research.** It's one team's experience, not a study or a benchmark.
- **Not tied to one tool.** Some examples use Claude Code file names. The loop and the failures apply to any coding agent.

## Prompts

Both prompts on the page are also plain files, so you can grab one without opening a browser:

```bash
curl -s https://raw.githubusercontent.com/stylusnexus/startup-plan/main/prompts/validation-gate.md
curl -s https://raw.githubusercontent.com/stylusnexus/startup-plan/main/prompts/agentic-principles.md
```

- [`prompts/validation-gate.md`](prompts/validation-gate.md) — run before you scaffold anything, one time
- [`prompts/agentic-principles.md`](prompts/agentic-principles.md) — paste into CLAUDE.md / AGENTS.md as standing rules

## Editing

Single self-contained `index.html`, no build step, no dependencies. Served via GitHub Pages from `main`.

Each prompt lives in two places: a file under `prompts/` and a copy on the page. After editing either, run `python3 scripts/check-sync.py`. It fails if they differ.

## License

MIT. See [LICENSE](LICENSE). You can reuse the prompts and the page; keep the copyright notice.
