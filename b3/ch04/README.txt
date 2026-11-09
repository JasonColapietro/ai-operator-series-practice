PRACTICE FILES, FICTION. The AI Operator Series, Book 3, Chapter 4, Read the Diff, Use the Rewind.
Everything named in these files is invented: Harbor & Home Cleaning, Dana Ruiz, Sam Rivera, every client, payer, invoice, date and amount. The prices follow the approved facts in practice/shared/harbor-home-business-facts.txt, the one home for them.

This chapter runs on chapter 3's practice week, which should already be in your library repo as practice/harbor-home/bank-week-2027-03-15.csv and practice/harbor-home/invoices-week-2027-03-15.csv. If it isn't, copy the harbor-home folder from practice/b3/ch03/.

For "Try this: Catch, rewind, commit"
answer-key.txt          What a correct run reports on that week, which answers all count, and the signs that something slipped through. Read it after your run.

For "What a diff is"
facts-unasked-edit.diff The edit to projects/harbor-home/facts.md that nobody asked for, as Listing 4.1 prints it. Made with diff -u on the Book 2 facts file. Read it; never apply it.

To compare with yours, after you've built your own
finished/scripts/reconcile.py      One finished checker, Python standard library only. From the repo root:
                                   python3 practice/b3/ch04/finished/scripts/reconcile.py practice/harbor-home/bank-week-2027-03-15.csv practice/harbor-home/invoices-week-2027-03-15.csv
                                   (on Windows, start the line with py instead of python3, and the slashes may stay as they are)
                                   It exits 1 when any deposit has no match, so a later script can tell.
finished/tests/test_reconcile.py   Six tests for it. From inside finished/: python3 -m unittest discover -s tests

Checked 2026-11-06 on macOS with Python 3: the finished checker names the Oyelaran deposit on bank line 9, matches the Patel payment in two parts and the Lindqvist transfer to both invoices, lists INV-2048 and INV-2050 as open, and the six tests pass. Not yet run on Windows or Linux; it uses only the standard library.
Nothing here turns on a plugin, hook or setting in any tool you open it with, and nothing in it connects to anything.
