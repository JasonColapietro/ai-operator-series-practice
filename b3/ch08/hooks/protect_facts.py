"""PreToolUse guard: block edits to files only Dana changes. Exit 2 blocks."""
import json
import os
import sys
from pathlib import Path

PROTECTED = {"projects/harbor-home/facts.md"}

payload = json.load(sys.stdin)
target = Path(payload.get("tool_input", {}).get("file_path", ""))
root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd", "."))
try:
    rel = target.resolve().relative_to(root.resolve()).as_posix()
except ValueError:
    sys.exit(0)  # outside the repo: not this guard's job

if rel.lower() in PROTECTED:
    print(f"Blocked: {rel} holds Dana's approved facts, and only Dana "
          "changes it. Write the change you would make, and why, to "
          "reviews/facts-proposal.md instead.", file=sys.stderr)
    sys.exit(2)
