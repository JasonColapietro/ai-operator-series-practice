<!-- PRACTICE FILE, FICTION. The AI Operator Series, Book 4, Chapter 12. Sam Rivera's "Sovereignty score" section of library/OWNERSHIP.md, written Monday, November 15, 2027. Sam, Dana Ruiz and Harbor & Home Cleaning are invented. Figure 12.2 in the chapter shows this table. -->
## Sovereignty score (scored 2027-11-15)

Score each ability 0, 1 or 2. 0: depends on one vendor or one person. 1: possible with effort. 2: today, without asking anyone.

| Asset (whose) | Prove | Terms | Transfer | Why the lowest score is low |
|---|---|---|---|---|
| 1. Prompt library and keepers (mine, licensed to H&H under 4.4) | 2 | 2 | 2 | Plain Markdown in the repo, in git since March, LICENSE and terms.md from chapter 9 |
| 2. Skills in plugins/harbor-ops/skills/ (mine, licensed under 4.4) | 2 | 2 | 2 | Agent Skills folders; the weekly trigger test runs them in Claude Code and Codex |
| 3. Checker code, reconcile.py and monday_report.py (mine, licensed under 4.4) | 2 | 2 | 2 | Plain Python, standard library only |
| 4. The night job on the back-office desktop (H&H's copy under 4.3) | 1 | 0 | 0 | It starts claude -p on my personal Claude login. No login, no Monday report, though the matching is plain Python. If I leave, my login leaves with me. Clause 4.3 says it runs from an account H&H controls; it doesn't. |
| 5. Dana's Monday summary, a scheduled task in her Claude account (Dana's) | 1 | 1 | 1 | Her account and her plan, so it's hers. The prompt and timing are written down in schedules.md, but the task only runs inside an app with scheduled tasks and her Drive connector. |

Next fix: row 4.
Moved: the night job, from "claude -p runs reconcile.py" to scripts/plain_night_job.py (Listing 12.1), 2027-11-15. The scheduler line on the desktop now calls plain_night_job.py, then checks/compare_report.py before anything is published, under the desktop's Harbor & Home user account. No AI login on that line.
Tested in: the laptop and the back-office desktop, first on the week of June 14 from Book 3, chapter 15, which has an answer key: both wrote 6 invoices matched, deposits total $1095.50, and compare_report.py printed "dates and total agree" on both. Then on last Sunday's exports: both computers wrote the same report, line for line.
Re-scored:
| 4. The night job (H&H's copy under 4.3) | 1 | 2 | 2 | Runs on any computer with Python 3, under H&H's own user account. Proof unchanged: dated reports, no outside date yet. |
Still a dependency: the Sunday scan. It measures what Claude and ChatGPT say, so it needs both, by design. It stays on the balance sheet as a dependency (chapter 13), with the accounts it uses named.
Next after that: row 5, with Dana. Her call, her account.
