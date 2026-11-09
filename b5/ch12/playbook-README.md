<!-- PRACTICE FILE, FICTION LABEL: The AI Operator Series, Book 5, Chapter 12. Sam's library/playbooks/staffing-quote-desk/README.md, the list of what the delivery kit holds. Copy the shape for each offer. Sam Rivera and Harbor & Home are invented. -->
# Playbook: weekend quote desk

The kit every quote-desk client starts from. Copy it into the client's own repo or Project; never work in this folder.
Offer: ../../offers/staffing-quote-desk.md. Standard: ../../service-standard.md.

| File | What it is | Came from |
|---|---|---|
| AGENTS.md | The agent's rules, including the outward-action rule. CLAUDE.md imports it. | Book 3, chapter 5 |
| CLAUDE.md | One line, `@AGENTS.md`, so Claude Code reads the same rules. | Book 3, chapter 5 |
| brief-template.md | The brief: audiences, what to build, Acceptance lines, what waits for the owner. | Book 2, chapter 13 |
| skills/quote-reply/SKILL.md | Drafts a reply from the client's approved facts only. | Book 3, chapter 7 |
| checks/check_delivery.py | Prices, appointments and promises against the facts file. Exit 2 when it reads nothing. | This chapter, Listing 12.1 |
| fixtures/ | Broken copies with one planted flaw each. Every check must fail at least one. | This chapter |
| evals/cases.md | Twelve test requests and what a right draft does with each. | This chapter |
| hooks/ | The guard that blocks sending and publishing. | Book 3, chapter 8 |
| handoff-template.md | What was built, where it runs, how to change it, what wasn't checked. | This chapter |
| report-template.md | The monthly report. | Chapter 13 |

Each client gets a folder of its own, clients/<client>/, with evidence/ and incidents.md (chapter 14 adds runbook.md), and its own worktree or Project with a written owner. One client's facts never sit in another client's room.
