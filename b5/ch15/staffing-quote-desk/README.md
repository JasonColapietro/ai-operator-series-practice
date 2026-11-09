<!-- PRACTICE FILE, FICTION LABEL: The AI Operator Series, Book 5, Chapter 15. Sam Rivera's weekend quote desk playbook packaged as a plugin. Sam, Dana Ruiz, Harbor & Home Cleaning and Marcus Lee Design are invented. -->
# Weekend quote desk

Drafts a reply to every evening and weekend quote request from the owner's own approved facts file, with a three-line summary for the owner. The owner approves every reply before it goes. Nothing in this plugin sends, books, confirms or charges.

## What's inside
- `skills/weekend-quotes/`: the drafting skill from chapter 14, with its `license` line and `LICENSE.txt`, `references/facts-file.md` (where each client's facts live and what they must state), `evals/` (the ten cases) and `runbook-template.md`.
- `LICENSE.md`: the terms for everything in this folder.

## Install
1. Put the business's approved facts file in the client's own drive, and write its exact location in the client's runbook.
2. Install the plugin in the client's own account, never yours, from a marketplace repo that holds only this plugin. In Claude Code, after the client adds that marketplace: `claude plugin install staffing-quote-desk@<marketplace-name>` (Book 3, chapter 11).
3. Fill `runbook-template.md` for the client, then run all ten cases in a fresh session before the first live weekend.

## Before you change it
Raise the version in `.claude-plugin/plugin.json`, run the ten cases, then publish.
