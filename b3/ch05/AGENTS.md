# AGENTS.md: the Harbor & Home library

## What this repo is
Sam Rivera's working library for Harbor & Home Cleaning, a
cleaning business in Portland, Maine, owned by Dana Ruiz.
It holds Dana's approved facts, saved prompts, skills, and
scripts/reconcile.py, which matches each bank deposit to
the invoice it pays. Dana's matching rules (one transfer
for two invoices, one invoice paid in two parts) are dated
in briefs/reconcile.md. Practice data only; names are fiction.

## Read-only paths
- projects/harbor-home/ is Dana's. Read it; never edit it.
- practice/ and every bank or invoice export are evidence.
  Read them; never edit them.
- Prices and policies live only in projects/harbor-home/facts.md.
  Point to that file. Never copy a price into another file.

## How to run and test
- Python 3, standard library only (see rule 5).
- Checker: python3 scripts/reconcile.py BANK_CSV INVOICES_CSV
- Tests, from the repo root: python3 -m unittest discover -s tests
  (Windows: py -m unittest discover -s tests). Run them
  before you report.

## Rules from incidents
Each rule has a date, the rule, and where it stops.
The story behind each one is in incidents.md.
1. 2027-03-22. Never change an export to make totals agree.
   Report the row, its line number and the mismatch instead.
   Stops at: copies you make under tests/fixtures/, which you
   may create and edit.
2. 2027-03-23. Never reformat, tidy or "fix" facts.md.
   If a fact looks wrong, say so in your report.
   Stops at: nothing in this repo. Dana edits it by hand.
3. 2027-03-23. Write "all deposits matched" only when the
   checker printed zero unmatched deposits in this session.
   Paste the checker's last line into your report.
   Stops at: tasks that never run the checker.
4. 2027-04-05. Bank exports mix two date formats. Slash dates
   are month first: 04/02/2027 is April 2. Dashed dates are
   year-month-day: 2027-04-02 is April 2. A date that fits
   neither: stop and report the row.
   Stops at: other files. Check a new file's format first.
5. 2027-04-05. Use only Python's standard library in scripts/,
   tests/ and hooks/. Never install or import another package.
   If a job seems to need one, stop and say why.
   Stops at: tools Sam runs by hand outside this repo.

## How to report
End every task with these four parts:
- Files changed: each one, with a one-line reason.
- Commands run, with the test result as printed.
- Deposits with no invoice: date, amount and line number,
  or "none".
- Anything you are unsure of, marked UNSURE.
Never commit or push unless the task says to.
