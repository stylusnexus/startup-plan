# The Startup Plan

The loop, the failures already made, and where to fork or install. A practical playbook for shipping software with AI coding agents, consolidated from two longer guides — [Shipping with Agents](https://github.com/stylusnexus/shipping-with-agents) and [Testing with Agents](https://github.com/stylusnexus/testing-with-agents).

**Read it:** https://stylusnexus.github.io/startup-plan/

By [Stylus Nexus](https://github.com/stylusnexus).

## What's here

- **The loop** — think, plan, build, verify, review, ship, with the distinctions that actually matter (think diverges, plan commits; verify is mechanical, review needs judgment)
- **Four failures** — the mega-agent, the mega-CLAUDE.md, ephemeral knowledge, gut-feel prompting, and the one instinct behind all four
- **First moves** — concrete, this-week actions
- **Where to go next** — fork [full-starter](https://github.com/stylusnexus/full-starter) for a complete repo, or install skills directly from [agent-plugins](https://github.com/stylusnexus/agent-plugins) into a project you already have

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
