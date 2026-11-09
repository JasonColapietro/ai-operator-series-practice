"""PostToolUse after git commit: add the commit to the log in decisions.md."""
import os
import subprocess
import sys
from pathlib import Path

sys.stdin.read()  # the payload; this hook only needs the newest commit
root = Path(os.environ.get("CLAUDE_PROJECT_DIR", "."))
result = subprocess.run(["git", "log", "-1", "--format=%h|%cs|%s"],
                        cwd=root, capture_output=True, text=True)
if result.returncode != 0 or not result.stdout.strip():
    sys.exit(0)

short_hash, date, subject = result.stdout.strip().split("|", 2)
log = root / "decisions.md"
if log.exists() and short_hash in log.read_text(encoding="utf-8"):
    sys.exit(0)  # already logged, for example after a failed commit
with log.open("a", encoding="utf-8") as f:
    f.write(f"- {date} commit {short_hash}: {subject}\n")
