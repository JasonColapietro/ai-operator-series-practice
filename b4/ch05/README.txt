PRACTICE FILES, FICTION. The AI Operator Series, Book 4, Chapter 5, Receipts, Not Claims.
Everything named in these files is invented: Harbor & Home Cleaning, Dana Ruiz, Sam Rivera, Mrs. Patel,
every document, date and line of website copy. Prices, the service area and the guarantee live in
practice/shared/harbor-home-business-facts.txt, their one home; nothing here repeats them.

For "Try this: Five receipts by tonight"
harbor-home-claims.txt     Seven lines from Dana's website and what Sam found to back them. The practice input.
receipts-answer-key.txt    Which five can go public, what goes on the gaps list, what to strike. Read it after you try.
templates/index.md         The evidence room's index: claim, artifact, who issued it, date checked.
templates/gaps.md          What you say but can't show yet. Never published.
templates/public.md        The receipts page source: five items, each with a link and a checked date.
templates/README.md        The note for receipts/: what the scheduled job does and who reads it.

For "Identity before your agents act" (needs Book 3's setup: a repo, Claude Code, the GitHub CLI)
hooks/check_identity.py    Listing 5.1. Blocks gh commands that create, comment, review, merge or release
                           unless GitHub says you're signed in as EXPECTED. Python standard library only.
hooks/settings-snippet.json  The PreToolUse entry for .claude/settings.json, in Book 3 chapter 8's shape.

For "Try this: Let one receipt keep itself"
scripts/append_receipt.py  Listing 5.2. Runs the tests in tests/, reads the current commit, and appends one
                           dated line to receipts/log.md. Publishes nothing. Run from the repo root.
stale-check-task.txt       The no-code route: a weekly Claude scheduled task that flags receipts whose
                           checked date is more than 90 days old. Pro plan or higher.

Checked 2026-11-06 on macOS with Python 3.14:
- append_receipt.py, run on a copy of practice/b3/ch04/finished/ with a stand-in for git (this
  workflow does not run git), printed "- 2026-11-06: checker tests, 6 run, all passed, at commit 4f2c9ab"
  and exited 0. With a failing test it printed "1 run, FAILED" and exited 1. With no tests/ folder it
  stopped with a message and exited 1. Run it once in a real repo before you schedule it.
- check_identity.py, fed sample payloads with a stand-in for gh: read-only commands passed (exit 0);
  pr comment, issue create (after cd ... &&), pr merge and release create under the wrong account were
  blocked (exit 2); a gh that printed nothing was blocked too. Not run on Windows or Linux.
Nothing here turns on a plugin, hook or setting in any tool you open it with until you copy it into place.
