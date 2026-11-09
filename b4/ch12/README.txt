PRACTICE FILES, FICTION. The AI Operator Series, Book 4, Chapter 12, Sovereignty, Not Tenancy.
Sam Rivera, Dana Ruiz, Harbor & Home Cleaning and every customer, invoice and amount mentioned here are invented. Portland, Maine is a real place.

For "Try this: Score five assets"
score-template.md     The "Sovereignty score" section to paste into library/OWNERSHIP.md, with the scoring rule at the top.
score-prompt.txt      The prompt card, if you want a first draft of the scores from your own OWNERSHIP.md.
sams-score.md         Sam's section as written on Monday, November 15, 2027: five rows, then the night job re-scored after the move. Read it after your own try.
score-key.txt         What the exercise accepts on the practice route, row by row.

For "Try this: Move one dependency"
plain_night_job.py    Listing 12.1. The night job with no agent in it: it runs Book 3's scripts/reconcile.py directly and writes
                      reports/reconcile-<date>.md with the title line Book 3's checks/compare_report.py reads.
                      Python standard library only. Copy it to scripts/ in your library repo.

Copy into your library repo (or a new empty folder), from the practice set's root:
  b3/ch12/finished/scripts/   ->  scripts/                  (Book 3's finished checker, reconcile.py and monday_report.py; skip if your repo already has them)
  b3/ch15/harbor-home/        ->  practice/harbor-home/     (the week of June 14, 2027 and its answer key)
  b3/ch15/checks/             ->  checks/                   (compare_report.py, Book 3 Listing 15.1)
  b4/ch12/plain_night_job.py  ->  scripts/plain_night_job.py
If you copied Book 3 chapter 15's reports/ folder earlier, the first command below replaces its stale reports/reconcile-2027-06-21.md with a correct one. That's expected.

To run it, open a terminal in that folder and type:
python3 scripts/plain_night_job.py practice/harbor-home/bank-week-2027-06-14.csv practice/harbor-home/invoices-week-2027-06-14.csv 2027-06-21
python3 checks/compare_report.py reports/reconcile-2027-06-21.md practice/harbor-home/answer-key-2027-06-14.md
The first line prints "2027-06-21 OK: wrote reports/reconcile-2027-06-21.md" (on Windows the path shows a backslash). The second prints "dates and total agree" and exits 0.
On Windows, type py instead of python3. [VERIFY: run both lines on Windows 11 and Ubuntu at print]
Checked 2026-11-06 on macOS with Python 3.14 and Book 3's finished checker (practice/b3/ch12/finished/scripts/reconcile.py): six invoices matched, deposits total $1095.50, exit 0. With a missing bank file it prints "FAILED: reconcile.py exited 2" and the checker's own message, and exits 1.

Nothing here turns on a plugin, hook or setting in any tool, and nothing in it connects to anything.
