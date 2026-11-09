# Weekly agent review, 2027-07-19

<!-- PRACTICE FILE, FICTION. The AI Operator Series, Book 3, Chapter 16. Sam Rivera's first weekly agent review for Harbor & Home Cleaning. Every name, date, cost and result is invented. -->

Next week's one change: rerun the trigger test after every plugin update, before the next drafts.

## 1. What ran (0 to 15)
| Job | Last report | Result | Cost |
|---|---|---|---|
| Nightly reconcile | reports/last-run.json, 2027-07-19 | 1 deposit unmatched (named) | under the $2 cap every night |
| Weekly scan | scan/reports/scan-2027-07-18T020000.md | 10 questions, 3 runs, 2 engines; 0 empty answers | under its cap |
| Reply drafts (Codex, mornings) | no report | none | not tracked |

Outputs I read myself:
- Drafts for Ortiz, Kowalski, Pham: Ortiz quotes a firm price for a 2,200 sq ft deep clean. No [CHECK]. Kowalski and Pham fine.
- Scan reports 2027-07-11 and 2027-07-18: coverage line present for both engines; each run's folder in scan/raw/ has 60 answer files (each with its .err.txt beside it).
- Known-answer run: reconcile on chapter 10's week in practice/harbor-home/, compared with answer-key.md. Matches the key, including both Haddad parts on INV-2050.

## 2. Drift (15 to 30)
Trigger test (expected / Claude Code / Codex):
- Inbox request / harbor-reply: harbor-reply / no skill
- Supplier invoice terms / none: none / none
- Rename amt / none: none / none
- Monday numbers / weekly-numbers: weekly-numbers / weekly-numbers
New rows in incidents.md:
- none since 2027-06-21. Added one today: the reply skill missing in Codex for nine days.
Spend against last week: flat.

## 3. What changes (30 to 45)
Versions: written from claude --version and codex --version.
Release notes that touch my setup: nothing on skills, hooks or headless runs this week.
Logins and tokens near expiry: GitHub token for the MCP server expires 2027-07-26. Make a new one this week. (The token itself lives in my password manager, never here.)
/doctor and codex doctor: clean.
Plugin updates since last week: harbor-ops released and updated 2027-07-07. The release renamed the reply skill's folder, and the link in .agents/skills/ that Codex reads pointed at nothing. This is the drift.

## 4. Decisions (45 to 60)
The decision: harbor-reply goes back under its own folder name, and the trigger test runs after every plugin update. In decisions.md.
Parked: the reply drafts have no report. Give them one next week if the hour runs long again.
