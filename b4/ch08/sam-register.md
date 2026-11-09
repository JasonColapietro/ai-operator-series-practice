<!-- Practice file, fiction: Harbor & Home Cleaning, Dana Ruiz, Sam Rivera and every customer are invented (README.txt). Sam's register as of 2027-11-08, the same rows as Figure 8.3 in Book 4 chapter 8. -->
# Data register

Started: 2027-11-08. Owner of this file: Sam Rivera.
No passwords, keys or recovery codes in this file. Both drive passwords live in Sam's password manager.

## Locations

| Location | What lives there | Whose data | A copy you control |
|---|---|---|---|
| Sam's ChatGPT account (Plus, paid by Harbor & Home) | chats, memory, uploaded files | Sam's, with Harbor & Home details pasted in | exports/2027-11-08/ |
| Sam's Claude account (Pro, paid by Harbor & Home) | chats, memory, Sam's copy of the Harbor & Home Project | Sam's, with Harbor & Home details | exports/2027-11-08/, library/ for Project files |
| Claude Code on Sam's laptop | ~/.claude/projects/, last 30 days | mixed: sessions that read bank files hold Dana's rows | none kept on purpose |
| Codex on Sam's laptop | ~/.codex/sessions, every morning reply draft | Dana's customers' emails | none; deleted after 30 days |
| Anthropic cloud, Sam's account | the June reconcile runs, one session a night | Dana's bank rows | deleted 2027-11-08 |
| GitHub, private repo `library` | every commit since March | Dana's exports and reports, Sam's code | library-2027-11-08.bundle |
| Back-office desktop (Harbor & Home) | a clone, each Sunday's download, scan/results.jsonl | Dana's | Dana's office; listed, not copied by Sam |
| Shared folder | Monday reconcile reports | Dana's | reports/ in the repo |
| Dana's Claude account | Dana's Project, Gmail and Drive connectors, the Monday task | Dana's | Dana exports it herself |
| Backup 1: encrypted drive at Sam's desk | all of library/, exports/ included | Sam's and Dana's | itself |
| Backup 2: encrypted drive kept at Harbor & Home's office | all of library/, exports/ included | Sam's and Dana's | itself |

## Data sets

| Data set | Where it lives | Owner | Seen by | Keep until | Last checked |
|---|---|---|---|---|---|
| Bank and invoice exports | practice/harbor-home/ on the laptop, GitHub, back office, both backups, every bundle | Dana Ruiz | Dana, Sam | End of Sam's contract, then handed back and deleted | 2027-11-08 |
| Reconcile reports | reports/, the shared folder, both backups | Dana Ruiz | Dana, Sam, Dana's accountant | Same as the exports | 2027-11-08 |
| Scan results | scan/results.jsonl on the back-office desktop, GitHub, both backups | Dana Ruiz | Dana, Sam | While the scan runs | 2027-11-08 |
| Morning reply drafts | Codex sessions on Sam's laptop | Dana Ruiz | Sam | 30 days, then deleted on the monthly sweep | 2027-11-08 |
| Claude Code transcripts | ~/.claude/projects/ on Sam's laptop | Mixed | Sam | 30 days, the default, left on purpose | 2027-11-08 |
| June cloud runs | Anthropic, under Sam's account | Dana Ruiz | Sam | Deleted 2027-11-08 | 2027-11-08 |
| Sam's chat exports | exports/ on the laptop, both backups | Sam Rivera | Sam | The last three monthly sweeps | 2027-11-08 |
| Test fixtures and test names | tests/, GitHub, both backups | Sam Rivera | Anyone | Kept; made-up rows and names only | 2027-11-08 |
| Dana's Claude account | Dana's Project, connectors, Monday task | Dana Ruiz | Dana | Dana exports it herself | asked Dana 2027-11-08 |

## Quarterly trace

| Date | Record | Path it took | Missed by the tables |
|---|---|---|---|
| 2027-11-08 | One deposit from the week of 2027-11-01 | bank export, Sunday download on the back-office desktop, practice/harbor-home/, commit, GitHub, Monday report, shared folder | nothing |
| 2027-11-08 | One customer email from 2027-11-03 | Dana's inbox, pasted into a Codex session, reply draft, Dana sent it | the Codex session (added above) |
| 2027-11-08 | The Patel two-part payment from March | bank export, practice/harbor-home/, copied into tests/test_reconcile.py | the test file (names replaced 2027-11-08) |
