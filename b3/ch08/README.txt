PRACTICE FILES, FICTION. The AI Operator Series, Book 3, Chapter 8, Make "Whenever" Automatic.
Harbor & Home Cleaning, Dana Ruiz and Sam Rivera are invented, and so is every price in the facts file these hooks protect. The scripts themselves are real and run as printed.

For "Try this: Guard the facts file"
hooks/probe.py                 Listing 8.1. Appends every payload it receives to hooks/probe.jsonl and blocks nothing. Delete probe.jsonl when you are done; it holds file paths from your machine.
claude/settings-probe.json     The probe's hooks block, for steps 1 and 2. Add its "hooks" key to your repo's .claude/settings.json, beside the "permissions" key from chapter 3; don't replace the file. On Windows, change each "python3" to "py".
claude/settings-hooks.json     Listing 8.2, the hooks block for .claude/settings.json: the guard, the formatter and the commit log. It replaces the probe's "hooks" key and sits beside "permissions" the same way. On Windows, change each "python3" to "py".
hooks/protect_facts.py         Listing 8.3, the guard. Exit 2 blocks an edit to projects/harbor-home/facts.md.
hooks/format_py.py             Listing 8.4, the formatter. Strips trailing spaces, turns tabs into spaces and ends the file with one newline. Never blocks.
hooks/log_commit.py            Listing 8.5, the commit log. Adds one line per commit to the end of decisions.md.
decisions-starter.md           A starting decisions.md with the commit log heading last.
agents-md-hooks-section.txt    The section for AGENTS.md that says why each hook exists.

Also used, from elsewhere in the practice files:
practice/shared/harbor-home-business-facts.txt   Dana's facts. In the library repo it lives at projects/harbor-home/facts.md.

Every script uses only Python's standard library. Checked with Claude Code 2.1.318 and Python 3.14 on a Mac, November 6, 2026. Nothing here does anything until you copy the hooks block into a repo's .claude/settings.json and start a new session there.
