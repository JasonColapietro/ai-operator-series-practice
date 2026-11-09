PRACTICE FILES, FICTION. The AI Operator Series, Book 3, Chapter 15, Done Means Live.
Everything named in these files is invented: Harbor & Home Cleaning, Dana Ruiz, Sam Rivera, Jamie Morales and every other client, invoice number, amount and date. Portland, Maine is a real place. The prices follow practice/shared/harbor-home-business-facts.txt and replace nothing in it. The CSV files keep their header lines, and the report and the message carry no label of their own because they stand in for a job's real output; this README is their fiction label.

Copy into your library repo, from the repo root:
  harbor-home/  ->  practice/harbor-home/   (beside what earlier chapters put there; nothing here overwrites chapter 10's answer-key.md)
  reports/      ->  reports/
  checks/       ->  checks/

For "Try this: Check the morning report"
harbor-home/bank-latest.csv               The bank export the night job read: the week of June 7 to 11, 2027, still under the "latest" name.
harbor-home/invoices-latest.csv           The invoice list the job read, the same old week.
harbor-home/bank-week-2027-06-14.csv      The bank export the job should have read: June 14 to 18, 2027.
harbor-home/invoices-week-2027-06-14.csv  The invoice list for the same week.
harbor-home/answer-key-2027-06-14.md      The second source: which deposit pays which invoice, and the week's total.
reports/reconcile-2027-06-21.md           The report the job published. Below its title and file line it is the real output of Sam's scripts/reconcile.py (chapter 12's finished version, practice/b3/ch12/finished/scripts/reconcile.py) on the two "latest" files.
reports/last-run-message.txt              The job's final message.
checks/compare_report.py                  Listing 15.1. Prints a report's dates and total beside the week it should cover. Python standard library only.
check-prompt.txt                          The prompt card.
check-key.txt                             What a correct check finds, and every result the chapter accepts. Read it after your own check.

For "Save this"
incidents-rows.md                         Listing 15.2, Sam's two newest entries for incidents.md.
agents-md-rule.txt                        Listing 15.3, the new rule for AGENTS.md.

To run the check from the repo root after copying:
python3 checks/compare_report.py reports/reconcile-2027-06-21.md practice/harbor-home/answer-key-2027-06-14.md
(On Windows, type py instead of python3.) It exits 1 on the practice report.

To rerun the reconcile on the right week and check the rerun (Mac or Linux terminal):
{ echo "# Reconcile, Monday 2027-06-21"; echo; python3 scripts/reconcile.py practice/harbor-home/bank-week-2027-06-14.csv practice/harbor-home/invoices-week-2027-06-14.csv; } > reports/reconcile-2027-06-21-rerun.md
python3 checks/compare_report.py reports/reconcile-2027-06-21-rerun.md practice/harbor-home/answer-key-2027-06-14.md
The second line prints "dates and total agree" and exits 0. The check needs the title line, because it reads the Monday date from it.
In PowerShell (not yet run on Windows):
& { "# Reconcile, Monday 2027-06-21"; ""; py scripts/reconcile.py practice/harbor-home/bank-week-2027-06-14.csv practice/harbor-home/invoices-week-2027-06-14.csv } | Set-Content -Encoding utf8 reports/reconcile-2027-06-21-rerun.md
Or ask your agent to rerun the reconcile on the two week-of-2027-06-14 files and save the output under the same title line.

Checked 2026-11-06 on macOS with Python 3: exit 1 on the practice report (both problems with the key, one without), exit 0 on the rerun.

Nothing here turns on a plugin, hook or setting in any tool, and nothing in it connects to anything.
