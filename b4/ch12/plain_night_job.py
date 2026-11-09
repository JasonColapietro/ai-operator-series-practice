"""The night job with no agent in it. Practice file, fiction.
The AI Operator Series, Book 4, Chapter 12, Listing 12.1.

Book 3's night job asked Claude Code to run scripts/reconcile.py and save what it
printed. The matching was plain Python all along, so this version runs the checker
itself. It needs Python 3 and nothing else: no AI account, no login, no network.

Usage, from the repo root (on Windows, py instead of python3):
    python3 scripts/plain_night_job.py BANK.csv INVOICES.csv [YYYY-MM-DD]
The date names the Monday the report is for; it defaults to today.
Writes reports/reconcile-<date>.md with the title line Book 3's
checks/compare_report.py reads. Exits 1, with a plain message, if the checker fails.
Python standard library only.
"""
import subprocess
import sys
from datetime import date
from pathlib import Path

if len(sys.argv) not in (3, 4):
    sys.exit("Usage: python3 scripts/plain_night_job.py BANK.csv INVOICES.csv [YYYY-MM-DD]")
bank, invoices = sys.argv[1], sys.argv[2]
monday = sys.argv[3] if len(sys.argv) == 4 else date.today().isoformat()
date.fromisoformat(monday)  # stops here on a malformed date

try:
    done = subprocess.run([sys.executable, "scripts/reconcile.py", bank, invoices],
                          stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=300)
except subprocess.TimeoutExpired:
    sys.exit(f"{monday} FAILED: reconcile.py ran past five minutes. Run it by hand.")
if done.returncode != 0 or not done.stdout.strip():
    said = (done.stderr.strip() or done.stdout.strip()).splitlines()[-1:] or ["no output"]
    sys.exit(f"{monday} FAILED: reconcile.py exited {done.returncode}: {said[0]}")

report = Path(f"reports/reconcile-{monday}.md")
report.parent.mkdir(exist_ok=True)
report.write_text(f"# Reconcile, Monday {monday}\n\nFiles: {bank}, {invoices}\n\n"
                  f"```text\n{done.stdout.rstrip()}\n```\n", encoding="utf-8")
print(f"{monday} OK: wrote {report}")
