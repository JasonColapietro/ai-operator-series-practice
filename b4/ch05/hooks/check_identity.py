"""PreToolUse guard: before a gh command that posts, comments or merges,
ask GitHub which account it will act as. Exit 2 blocks. Practice file, fiction.

The AI Operator Series, Book 4, Chapter 5 (Listing 5.1). Python standard library only.
Put your own GitHub login in EXPECTED. Hook it up the way Book 3, chapter 8 hooks
its guards: PreToolUse, matcher "Bash", "if": "Bash(gh *)", "onFailure": "block".
"""
import json
import shlex
import subprocess
import sys

EXPECTED = "YOUR-GITHUB-LOGIN"  # the account your name is on
WRITES = {("pr", "create"), ("pr", "comment"), ("pr", "review"), ("pr", "merge"),
          ("issue", "create"), ("issue", "comment"), ("release", "create")}

command = json.load(sys.stdin).get("tool_input", {}).get("command", "")
try:
    words = shlex.split(command)
except ValueError:
    words = command.split()
writes = any(w.rsplit("/", 1)[-1] == "gh" and tuple(words[i + 1:i + 3]) in WRITES
             for i, w in enumerate(words))
if not writes:
    sys.exit(0)  # reading is fine as any account

try:
    who = subprocess.run(["gh", "api", "user", "--jq", ".login"], capture_output=True,
                         text=True, timeout=20, stdin=subprocess.DEVNULL).stdout.strip()
except (OSError, subprocess.TimeoutExpired):
    who = ""
if who.lower() != EXPECTED.lower():
    print(f"Blocked: this command would act on GitHub as '{who or 'unknown'}', "
          f"not as {EXPECTED}. Run gh auth switch to the right account, check "
          "for a GH_TOKEN or GITHUB_TOKEN in the environment, then try again.",
          file=sys.stderr)
    sys.exit(2)
