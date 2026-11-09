"""Status line for Claude Code: model, branch, context used, last reconcile run.

Practice file, The AI Operator Series, Book 3, Chapter 11. Harbor & Home and
everything in reports/ are fiction. Python standard library only.
Claude Code sends session JSON on stdin; whatever this prints is the line.
"""
import json
import subprocess
import sys
from pathlib import Path

try:
    session = json.load(sys.stdin)
except ValueError:
    session = {}

model = (session.get("model") or {}).get("display_name", "?")
root = Path((session.get("workspace") or {}).get("project_dir") or ".")
used = (session.get("context_window") or {}).get("used_percentage")
context = f"{used:.0f}% context" if isinstance(used, (int, float)) else "context ?"

try:
    branch = subprocess.run(
        ["git", "-C", str(root), "branch", "--show-current"],
        capture_output=True, text=True, timeout=2,
    ).stdout.strip() or "no branch"
except (OSError, subprocess.SubprocessError):
    branch = "no git"

last = root / "reports" / "last-run.json"
try:
    run = json.loads(last.read_text(encoding="utf-8"))
    result = "ok" if run.get("exit_code") == 0 else "check it"
    reconcile = f"reconcile {run.get('date', '?')} {result}"
except (OSError, ValueError, AttributeError):
    reconcile = "reconcile: no run yet"

print(f"{model} | {branch} | {context} | {reconcile}")
