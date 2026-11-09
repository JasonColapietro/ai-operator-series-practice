"""Write the morning card for the newest scan. Practice file, fiction.
The AI Operator Series, Book 3, Chapter 14 (the morning card, Figure 14.3).
Usage, from the repo root: python3 scan/report.py
"""
import json
from pathlib import Path

SCAN = Path(__file__).resolve().parent
rows = [json.loads(line) for line in open(SCAN / "results.jsonl", encoding="utf-8") if line.strip()]
stamp = rows[-1]["stamp"]
rows = [r for r in rows if r["stamp"] == stamp]
stopped = any(r["status"] == "empty" for r in rows)
lines = [f"# Scan {stamp}", "", f"Raw answers: scan/raw/{stamp}/", ""]
for engine in dict.fromkeys(r["engine"] for r in rows):
    mine = [r for r in rows if r["engine"] == engine]
    count = {s: sum(r["status"] == s for r in mine) for s in ("answered", "blocked", "empty")}
    named = sum(bool(r["named"]) for r in mine if r["status"] == "answered")
    planned = mine[0]["planned"]
    rate = (f"{named} of {count['answered']} answers ({named / count['answered']:.0%})"
            if count["answered"] and not stopped else "not scored")
    lines += [f"## {engine}",
              f"- Named us: {rate}",
              f"- Coverage: {count['answered']} of {planned} planned ({count['answered'] / planned:.0%})",
              f"- Blocked: {count['blocked']}  Empty: {count['empty']}", ""]
if stopped:
    lines.append("RUN STOPPED ON AN EMPTY ANSWER. Fix the engine and run the whole scan again.")
(SCAN / "reports").mkdir(exist_ok=True)
(SCAN / "reports" / f"scan-{stamp}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
