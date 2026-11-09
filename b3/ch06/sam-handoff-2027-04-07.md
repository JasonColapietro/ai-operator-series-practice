<!-- FICTION. Sam's handoff, handoffs/2027-04-07-claude-second-bank.md, Book 3 chapter 6, Listing 6.2. -->
# Handoff: second bank format (Claude Code)

## Target
library/, the private repo. The deposit checker,
scripts/reconcile.py.

## Branch and remote
main. Pushed to origin on 2027-04-07.

## Files changed
- scripts/reconcile.py: reads the second bank's export.
- tests/test_reconcile.py: three new tests.
- tests/fixtures/second-bank-sample.csv: 12 rows, fiction.
- AGENTS.md: the day-first rule for the second bank.
- incidents.md: one dated row for the lost decision.

## Commands run
python3 -m unittest discover -s tests (12 tests, all pass)

## Verified (and how)
Tests pass. The run names row 9 of the fixture, the
planted deposit, as unmatched. Not checked: any real
export.

## Status
The checker reads both banks' exports. It has not run
on real files.

## Blockers and caveats
- The second bank writes dates day first. Row 7 of its
  export reads 25/03/2027. The rule is in AGENTS.md.
- The 18/03/2027 transfer pays two invoices billed to two
  different clients. The checker lists it as unmatched.
  How to count it is Dana's call.
- Tuesday's commit is named "wip". This note says what
  it holds.

## Exact next step
Run the checker on Monday's two bank exports and the
invoice list. Save the unmatched list to reports/ for
Dana. Change no matching rule.
