<!-- PRACTICE FILE, FICTION. The AI Operator Series, Book 3, Chapter 13, The Crew. Harbor & Home Cleaning, Dana Ruiz and Sam Rivera are invented. Listing 13.1 prints everything below this line. -->
# Monday report, May 24, 2027

Lead: plans, assigns, updates this file. Does no task itself.
Worker: one task at a time, in the order below. Touches only the
file its task writes.
Verifier: a fresh session that did none of the work.
Status words: todo, doing, done, blocked.

| # | Task | Owner | Waits for | Writes | Status |
|---|---|---|---|---|---|
| 1 | Bring in the first bank's export | worker | none | practice/harbor-home/bank-first-2027-05-24.csv | todo |
| 2 | Bring in the second bank's export | worker | none | practice/harbor-home/bank-second-2027-05-24.csv | todo |
| 3 | Run the checker on this week's three files | worker | 1, 2 | reports/checker-output.txt | todo |
| 4 | Write Dana's Monday report | worker | 3 | reports/monday-2027-05-24.md | todo |
| 5 | Check the report against the answer key | verifier | 4 | reviews/verify-2027-05-24.md | todo |
| 6 | Update the holiday-hours answer from facts.md | worker | none | projects/harbor-home/faq.md | todo |

Rules
- Tasks 1 and 2: the export is in practice/harbor-home/incoming/.
  Check it holds only May 17 to 21, 2027, then move it to Writes.
- Task 3: the first line of checker-output.txt says the run date and the
  deposit dates it covers.
- Task 4: stop if the first line of checker-output.txt is not today's run.
- Task 5: report findings only. Never fix the report.
- Task 6: Dana reads the new answer before it goes on the website.
