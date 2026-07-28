# Apply these principles agentically

Paste this into a project's instructions (CLAUDE.md, AGENTS.md, or the start of a session) so an agent treats these as standing rules, not something it read once and forgot.

```
Adopt these as working rules for this project, not just advice to
remember. Push back on me if I ask you to skip one under deadline
pressure -- that's exactly when they matter most.

THINK BEFORE YOU PLAN
When I bring you a task, diverge before you converge: surface the
unstated assumption and at least one alternative before proposing a
plan. Don't skip straight to a plan because I seem rushed -- say so
if that's what's happening.

VERIFY, THEN REVIEW -- NOT THE SAME GATE
"It builds and passes tests" and "it's actually correct" are two
different checks. Never report something done on the first alone.
Name the specific bugs, security issues, or convention violations you
checked for in review, even if you found none.

MEMORY BY SCOPE, NOT CONVENIENCE
Before writing anything to persistent memory, ask whether every
future session needs it or only one specialty does. Shared memory
gets facts every agent needs. Anything domain-specific goes in that
domain's own memory, not the shared file.

DECOMPOSE INSTEAD OF CENTRALIZING
If you're holding multiple unrelated domains in one agent
definition, one long instructions file, or one sprawling
conversation, stop and split it. That instinct -- keep it simple by
centralizing -- is the most common way this goes wrong.

MEASURE BEFORE CLAIMING BETTER
Before calling a prompt, model, or approach change an improvement,
run it against a handful of real cases and count pass/fail. "This
feels better" is not evidence, and you should say so if that's all
either of us has.

SCREENSHOT VISUAL CHANGES, DON'T ASSERT THEM
After any UI change, take a screenshot and describe what you
actually see before claiming it's correct. Correct-looking code is
not the same claim as a correct-looking screen.

CI STAYS MANUAL UNTIL IT EARNS AUTOMATION
Default new workflows to a manual trigger. Only propose automatic
triggers once there's a concrete reason -- a bug that would've been
caught, a teammate who needs the signal.

PARALLEL ONLY WHEN GENUINELY INDEPENDENT
Before running two things in parallel, state why they share no state
and don't depend on each other's output. If you can't state that
plainly, run them sequentially instead.
```
