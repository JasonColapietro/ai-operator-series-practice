"""Append one dated receipt line to receipts/log.md. Practice file, fiction.

The AI Operator Series, Book 4, Chapter 5 (Listing 5.2). Python standard library only.
Run it from the root of your library repo, the folder that holds tests/:
    python3 scripts/append_receipt.py      (on Windows: py scripts/append_receipt.py)

It runs the test suite, reads the current commit, and adds one line to the private log.
It changes nothing else, sends nothing and publishes nothing. A person reads the log
and copies a line to the public page by hand. Exit code 1 means the tests failed.
"""
import datetime
import subprocess
import sys
from pathlib import Path

LOG = Path("receipts/log.md")


def run(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True, stdin=subprocess.DEVNULL)


if not Path("tests").is_dir():
    sys.exit("No tests/ folder here. Run this from the root of your library repo.")

tests = run(sys.executable, "-m", "unittest", "discover", "-s", "tests")
ran_lines = [ln for ln in tests.stderr.splitlines() if ln.startswith("Ran ")]
ran = ran_lines[-1].split()[1] if ran_lines else "0"
passed = tests.returncode == 0 and ran != "0"
commit = run("git", "rev-parse", "--short", "HEAD").stdout.strip() or "no commit yet"
today = datetime.date.today().isoformat()

line = (f"- {today}: checker tests, {ran} run, "
        f"{'all passed' if passed else 'FAILED'}, at commit {commit}\n")
LOG.parent.mkdir(exist_ok=True)
with LOG.open("a", encoding="utf-8") as log:
    log.write(line)
print(line, end="")
sys.exit(0 if passed else 1)
