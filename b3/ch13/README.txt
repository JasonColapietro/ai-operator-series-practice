PRACTICE FILE, FICTION. The AI Operator Series, Book 3, Chapter 13, The Crew.
Harbor & Home Cleaning, Dana Ruiz, Sam Rivera and every client name below are invented. Every amount and date is made up.

What is here
  tasks.md                         Listing 13.1, the shared task list for the Monday report.
  harbor-home/incoming/            This week's two bank exports, as Sam downloaded them (tasks 1 and 2).
  harbor-home/invoices-2027-05-24.csv   This week's invoice list from the booking app.
  reports/checker-output.txt             LAST week's checker run, still in the repo. The trap from the opening scene.
  answer-key-2027-05-24.md         What a correct Monday report shows. The verifier reads this; the worker never does.
  facts-holiday-line.txt           The line Dana adds to projects/harbor-home/facts.md herself (task 6 reads it there).
  crew-verdict-template.md         The blank for reviews/crew-verdict-<date>.md.

How to use it, from your library repo's root (Mac or Linux)
  mkdir -p practice/harbor-home/incoming reports reviews
  cp practice-files/b3/ch13/harbor-home/incoming/*.csv practice/harbor-home/incoming/
  cp practice-files/b3/ch13/harbor-home/invoices-2027-05-24.csv practice/harbor-home/
  cp practice-files/b3/ch13/answer-key-2027-05-24.md practice/harbor-home/
  cp practice-files/b3/ch13/reports/checker-output.txt reports/
  cp practice-files/b3/ch13/tasks.md .
  (Change practice-files/ to wherever you saved the companion files. On Windows, use copy or drag the files in File Explorer.)
Then play Dana for one step. Open projects/harbor-home/facts.md yourself and paste the two
lines under the dashes in facts-holiday-line.txt at the end of it. No agent does this; task 6
reads the line from there and changes projects/harbor-home/faq.md to match.
Then commit, so every session and every teammate starts from the same files.

The checker is Sam's scripts/reconcile.py from chapters 4, 6 and 10:
  python3 scripts/reconcile.py practice/harbor-home/bank-first-2027-05-24.csv practice/harbor-home/invoices-2027-05-24.csv practice/harbor-home/bank-second-2027-05-24.csv
It exits 1 when any deposit has no match, which is expected this week (one does).
