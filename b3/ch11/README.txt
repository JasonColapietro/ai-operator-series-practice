PRACTICE FILES, FICTION. The AI Operator Series, Book 3, Chapter 11, Pack It, Share It, Mod It.
Harbor & Home Cleaning, Dana Ruiz, Sam Rivera and every customer, price and date in these files are invented. The JSON files are real configuration and were checked as printed.

For "Try this: Ship harbor-ops"
plugin/.claude-plugin/plugin.json        Listing 11.1, top half. Copy to plugins/harbor-ops/.claude-plugin/plugin.json and put your own name in place of "Your Name".
marketplace/.claude-plugin/marketplace.json   Listing 11.1, bottom half. Copy to .claude-plugin/marketplace.json at the repo root and put your own name in place of "Your Name".
plugin/hooks/hooks.json                  Listing 11.2. Chapter 8's hooks block with every path changed to ${CLAUDE_PLUGIN_ROOT}. Copy to plugins/harbor-ops/hooks/hooks.json, then delete the "hooks" block from .claude/settings.json so each hook runs once. On Windows, change each "python3" to "py", and keep chapter 8's copy-check hook in .claude/settings.json (it guards the repo, not the plugin).
claude/settings-marketplace.json         Listing 11.3. Merge these two keys into the repo's .claude/settings.json (keep the permissions from chapter 3). Change YOUR-NAME to your GitHub name.

For "Try this: Score it and show it"
eval-scenarios.md                        Ten scenarios to give the eval interview.
statusline.py                            Listing 11.4. Copy to ~/.claude/statusline.py, and keep a copy in scripts/statusline.py in the repo.
claude/settings-statusline.json          The statusLine block for ~/.claude/settings.json. On Windows, use "py" and forward slashes in the path.
statusline-prompt.txt                    The prompt card, if you'd rather /statusline wrote the script.
last-run.example.json                    The shape of reports/last-run.json. Chapter 14's nightly run writes this file for real.

Checked on a Mac, November 6, 2026: claude plugin validate --strict passes on the plugin and the marketplace (Claude Code 2.1.319); claude plugin marketplace add and claude plugin install work from a local copy, with a scratch config folder, at user scope and with --scope local; Codex CLI 0.164.0 adds the same marketplace and installs harbor-ops; statusline.py prints the line in Figure 11.2 from the example JSON (Python 3.14).
Nothing here turns on a plugin, hook or setting in any tool until you copy a file into place yourself.
