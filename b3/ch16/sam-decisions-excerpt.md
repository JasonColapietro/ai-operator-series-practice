# Decisions

<!-- PRACTICE FILE, FICTION. The AI Operator Series, Book 3, Chapter 16. The top of Sam's decisions.md after the first weekly agent review. The commit log heading from chapter 8 stays last; the hook appends below it. -->

## 2027-03-12: the first agent job is deposit reconciliation
Decided: the agent checks deposits against invoices and reports.
It never sends, books or edits an export.
Why: Sam spent about forty minutes on it every Monday, by hand.
Who decided: Dana.

## 2027-04-05: standard library only
Decided: scripts/, tests/ and hooks/ use Python's standard library.
Why: one script runs on Dana's office computer and Sam's laptop
with nothing to install.
Who decided: Sam.

## 2027-07-19: the trigger test runs after every plugin update
Decided: harbor-reply goes back under its own folder name. After
any plugin update, rerun the four trigger requests in both tools
before the next drafts.
Why: the 2027-07-07 release renamed the folder, the link Codex
reads pointed at nothing, and a draft quoted a deep-clean price
Dana never set. Nine days passed before anyone noticed.
Who decided: Sam, with Dana's OK.

## Commit log (written by a hook)
