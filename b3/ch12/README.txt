PRACTICE FILES, FICTION. The AI Operator Series, Book 3, Chapter 12, Many Agents, One Repo.
Everything named in these files is invented: Harbor & Home Cleaning, Dana Ruiz, Sam Rivera, every client, deposit, invoice, number and date. Portland, Maine is a real place. The CSV files and the two library files can't carry a fiction line without changing how they work, so this README is their label.

For "Try this: Two lanes, one merge"
harbor-home/bank-first-2027-03-22.csv            The first bank's deposits for the week of Monday, March 22, 2027. Month-first and year-first dates, as chapter 5's rule 4 says.
harbor-home/bank-second-2027-03-22.csv           The second bank's deposits for the same week. Day first, with the "Amount (USD)" column, as chapter 6 found.
harbor-home/invoices-2027-03-22.csv              The booking app's open invoices for the week.
harbor-home/bank-second-2027-03-22-empty.csv     The second bank's export as it came down one Monday: the header and nothing else. For lane A.
harbor-home/invoices-2027-03-22-renamed.csv      The invoice list after the booking app renamed a column. For lane A.
Copy the harbor-home/ files into practice/harbor-home/ in your library repo, commit them, and push before you start either lane. A worktree holds only what is committed.
prompt-lane-a.txt, prompt-lane-b.txt             The chapter's two prompt cards, word for word below their headers.
answer-key.txt                                   What a correct run shows, and every answer that counts. Read it after your run.

For "Save this"
lanes.md                Listing 12.1, word for word. Save it as docs/lanes.md.
worktreeinclude.txt     The one-line .worktreeinclude from the chapter. Save it as .worktreeinclude at the repo root. Rename it; the leading dot matters.
Your .gitignore already has the .claude/worktrees/ line from chapter 2 (practice/b3/ch02/gitignore.txt).

To compare with yours, after you've built your own
finished/scripts/reconcile.py        Lane A's result. It starts from the chapter 10 starting copy of the checker (practice/b3/ch10/sam/scripts/reconcile.py). If your chapter 10 review changed how deposits match, keep your version and compare only read_rows() and the code that calls it.
finished/tests/test_reconcile.py     The chapter 10 starting tests plus lane A's three.
finished/scripts/monday_report.py    Lane B's result.
finished/tests/test_monday_report.py Lane B's four tests.
From inside finished/:  python3 -m unittest discover -s tests   (Windows: py -m unittest discover -s tests)
To run both together from a folder holding scripts/ and harbor-home/:
  python3 scripts/reconcile.py harbor-home/bank-first-2027-03-22.csv harbor-home/invoices-2027-03-22.csv harbor-home/bank-second-2027-03-22.csv | python3 scripts/monday_report.py 2027-03-22

Checked 2026-11-06 on macOS with Python 3: the 12 tests pass; the good week writes reports/monday-2027-03-22.md; the empty second-bank file stops the checker with exit 2, and the report script repeats the checker's STOPPED line (a pipe would otherwise hide it), writes nothing and exits 1; the renamed column stops the checker and names invoice_no. Not yet run on Windows or Linux; it uses only the standard library.
Nothing here turns on a plugin, hook or setting in any tool you open it with, and nothing in it connects to anything.
