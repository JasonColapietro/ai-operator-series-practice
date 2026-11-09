<!-- PRACTICE FILE, FICTION. The AI Operator Series, Book 3, Chapter 15. Listing 15.2: paste these two entries at the bottom of incidents.md, newest last. Below this line it matches the chapter word for word. -->

## 2027-06-16: "pushed" was a commit on the laptop
What happened: the agent's report said a fix to the checker
was pushed. GitHub's page for main didn't have it; the
commit sat on a local branch. Pushed by hand, then checked.
Rule: write "pushed" only with the commit's short id, read
from GitHub's page for main after the push.
Lives in: AGENTS.md, How to report.

## 2027-06-21: the Monday report had last week's deposits
What happened: the night job published a report dated June 21
built from the June 7 to 11 exports. Sunday's download had
failed, the old files kept their "latest" names, and every
check passed. Dana caught it. Rerun from the right files.
Rule: a report names the first and last deposit date it
read. A Monday report with a deposit dated before last
Monday is stale and is not published.
Lives in: AGENTS.md, rule 7; checks/compare_report.py, run
by the night job before it publishes.
