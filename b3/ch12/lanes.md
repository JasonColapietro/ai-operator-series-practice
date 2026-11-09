# Lanes: who owns what

One owner per area. A lane edits only its own files.
Anything under Shared changes in a task of its own, run by Sam.

## Lanes
- The checker. Owner: lane A.
  scripts/reconcile.py, tests/test_reconcile.py
- Dana's Monday report. Owner: lane B.
  scripts/monday_report.py, tests/test_monday_report.py

## Shared (no lane edits these)
- The lines the checker prints: PAID, NO MATCH,
  NO DEPOSIT YET, STOPPED and the summary line.
  Lane B reads them, so lane A keeps them as they are.
- AGENTS.md, CLAUDE.md and this file.
- projects/harbor-home/ (Dana's, read-only).
- practice/ and every export (evidence, read-only).
- The skills, hooks and plugins/harbor-ops/.

## Before a lane starts
- git fetch origin, then git status -sb.
- Its own worktree, cut from origin/main.
- Its own port, if it runs a server.

## Before a worktree is removed
- Its pull request shows as merged on GitHub.
- No process is working in it: lsof on a Mac or Linux,
  Handle on Windows. Check again right before the delete.
