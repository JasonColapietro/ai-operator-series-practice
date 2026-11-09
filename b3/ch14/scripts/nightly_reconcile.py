"""Run the reconcile with nobody watching, under a cap, and say plainly how it went.
Practice file, fiction (The AI Operator Series, Book 3, Chapter 14, Listing 14.2).
Usage, from the repo root: python3 scripts/nightly_reconcile.py
"""
import json, subprocess, sys
from datetime import date
from pathlib import Path

today = date.today().isoformat()
prompt = ("Run python3 scripts/reconcile.py on the newest bank and invoice files in "
          f"practice/harbor-home/ and save what it prints to reports/reconcile-{today}.md. "
          "Change nothing else.")
command = ["claude", "-p", prompt, "--output-format", "json", "--permission-mode", "dontAsk",
           "--allowedTools", "Bash(python3 scripts/reconcile.py *)", "Edit(./reports/**)",
           "--max-budget-usd", "2"]
Path("reports").mkdir(exist_ok=True)
try:
    done = subprocess.run(command, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=900)
    result = json.loads(done.stdout)
except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError) as problem:
    sys.exit(f"{today} FAILED: no result to read ({type(problem).__name__}). Run it by hand.")
report = Path(f"reports/reconcile-{today}.md")
problems = []
if result.get("is_error") or result.get("terminal_reason") != "completed":
    problems.append(f"run ended {result.get('subtype')} / {result.get('terminal_reason')}")
if result.get("permission_denials"):
    problems.append(f"{len(result['permission_denials'])} call(s) denied")
if not report.exists() or not report.read_text(encoding="utf-8").strip():
    problems.append(f"{report} is missing or empty")
cost = result.get("total_cost_usd", 0)
line = f"{today} {'REVIEW: ' + '; '.join(problems) if problems else 'OK'} (estimated ${cost:.2f} of $2 cap)"
result.update(date=today, exit_code=1 if problems else 0, summary=line)
Path("reports/last-run.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(line)
sys.exit(1 if problems else 0)
