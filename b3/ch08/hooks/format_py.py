"""PostToolUse: tidy a Python file after an edit. Never blocks."""
import json
import sys
from pathlib import Path

target = Path(json.load(sys.stdin).get("tool_input", {}).get("file_path", ""))
if target.suffix != ".py" or not target.is_file():
    sys.exit(0)

raw = target.read_bytes()
newline = "\r\n" if b"\r\n" in raw else "\n"
lines = raw.decode("utf-8").splitlines()
tidy = newline.join(line.rstrip().expandtabs(4) for line in lines).rstrip()
tidy += newline
if tidy.encode("utf-8") != raw:
    target.write_bytes(tidy.encode("utf-8"))
