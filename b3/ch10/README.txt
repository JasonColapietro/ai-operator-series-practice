PRACTICE FILES, FICTION. The AI Operator Series, Book 3, Chapter 10, A Second Context Window.
Everything named in these files is invented: Harbor & Home Cleaning, Dana Ruiz, Sam Rivera, Sana Haddad and every other client, invoice number, amount and date. The prices follow practice/shared/harbor-home-business-facts.txt and replace nothing in it. The one email address uses example.org, a domain reserved for examples.

Copy harbor-home/ into your library repo as practice/harbor-home/ (add these files beside what chapters 3 and 5 put there; the reviewer names its three files, so the older weeks don't get in its way). If you have no checker of your own, copy sam/scripts/reconcile.py, sam/tests/ (the test file and its fixtures/ folder) and sam/reports/reconcile-2027-04-12.md to scripts/, tests/ and reports/ at the repo root. Then commit the copies, so git status is clean before the review starts. The CSV files keep their header lines; this README is their fiction label.

For "Try this: Delegate one review"
claude/agents/reviewer.md              Listing 10.1. Copy it to .claude/agents/reviewer.md.
codex/agents/reviewer.toml             Listing 10.2, the same reviewer for Codex. Copy it to .codex/agents/reviewer.toml.
review-prompt.txt                      The prompt card.
review-key.txt                         What a good review finds, and every result the chapter accepts. Read it after your own check.
review-template.md                     The blank for reviews/reconcile-review-<date>.md.
harbor-home/bank-first-2027-03-29.csv  The first bank's deposits, Monday March 29 to Friday April 9, 2027.
harbor-home/bank-second-2027-03-29.csv The second bank's deposits for the same two weeks. Dates are day first.
harbor-home/invoices-2027-03-29.csv    The booking app's open invoices for the two weeks, with two carried over from March 15 to 19.
harbor-home/haddad-email-2027-03-31.txt  The customer email that settles the planted case.
harbor-home/answer-key.md              Which deposit pays which invoice, and why one client is the hard case.
sam/                                   Sam's checker, tests and saved report at the start of the chapter: chapter 4's finished checker plus chapter 6's second-bank reader, its twelve tests and their fixture (tests/fixtures/second-bank-sample.csv). The checker has one blind spot on purpose. Its twelve tests pass.

To run Sam's checker from the repo root after copying:
python3 scripts/reconcile.py practice/harbor-home/bank-first-2027-03-29.csv practice/harbor-home/invoices-2027-03-29.csv practice/harbor-home/bank-second-2027-03-29.csv

Nothing here turns on a plugin, hook or setting in any tool until you copy a file into place yourself.
