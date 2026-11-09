PRACTICE FILES, FICTION. The AI Operator Series, Book 3, Chapter 14, The Night Shift.
Harbor & Home Cleaning, Dana Ruiz, Sam Rivera, Bramblecove Cleaning and Quillstone Maids are invented. Because Harbor & Home is fiction, a real AI engine will never name it: with real engines, these files teach the plumbing (coverage, empty answers, the morning card), and the named-us rate means something only when you scan your own business. The practice engine answers with invented text so you can test every part of the scan for free.

Copy scan/ and scripts/ into the root of your library repo. Nothing here turns on a plugin, hook or setting in any tool.

For "Try this: Tonight's run"
scripts/nightly_reconcile.py     Listing 14.2. Runs chapter 4's checker headless under a $2 cap and prints one verdict line.
scan/prompts.md                  The ten locked buyer questions for Harbor & Home (Q01 to Q10), with their tags.
scan/names.txt                   The declared names. An answer names the business only if one of these lines appears in it.
scan/run_scan.py                 Listing 14.1. Asks each question three times per engine and stops on an empty answer.
scan/report.py                   Writes the morning card to scan/reports/ and prints it.
scan/practice_engine.py          A pretend engine. It answers from practice-answers/, invented text, never a real AI answer.
scan/practice-answers/Q01.txt..  The pretend answers. Empty one to test the alarm (step 5), then copy it back from here.
schedules.txt                    Example schedule lines for cron, launchd and Task Scheduler, and the cloud task's prompt.

What the practice engine should give you on a full run (checked 2026-11-06):
  python3 scan/run_scan.py practice    then    python3 scan/report.py
  Named us: 12 of 30 answers (40%) · Coverage: 30 of 30 planned (100%) · Blocked: 0  Empty: 0
  Q01, Q04, Q07 and Q10 name the business. Q04 counts only because "Harbor and Home Cleaning" is in names.txt:
  delete that line and the same answers score 9 of 30 (30%).
With Q03.txt emptied, the run stops at Q03, run 1, with "ENGINE FAILURE", exit code 1, and the card reads
  "Named us: not scored" and "Coverage: 6 of 30 planned (20%)".

Runs, files and folders the scripts create (keep them out of the practice folders you copy from):
scan/raw/<stamp>/      one answer file and one .err.txt file per question, run and engine
scan/results.jsonl     one line per answer, appended, never rewritten
scan/reports/          one morning card per scan
reports/               reconcile-<date>.md and last-run.json from the nightly reconcile
