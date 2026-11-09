"""Print a Monday report's deposit dates and total beside the week it should cover.
Practice file, fiction. The AI Operator Series, Book 3, Chapter 15.

Usage, from the repo root:
    python3 checks/compare_report.py REPORT.md [ANSWER_KEY.md]
Exits 1 if any deposit falls outside last Monday to Sunday, if the total
differs from the answer key, or if it can't find what it needs to check.
Python standard library only.
"""
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path


def find(pattern, text, what):
    match = re.search(pattern, text)
    if not match:
        sys.exit(f"cannot check: no {what} found, so the result is unknown")
    return match.group(1)


report = Path(sys.argv[1])
text = report.read_text(encoding="utf-8")
when = datetime.fromtimestamp(report.stat().st_mtime)
day = date.fromisoformat(find(r"Monday (\d{4}-\d{2}-\d{2})", text, "Monday date in the title"))
start, end = day - timedelta(days=7), day - timedelta(days=1)
dates = sorted(date.fromisoformat(d) for d in re.findall(r" on (\d{4}-\d{2}-\d{2})", text))
total = find(r"Deposits total \$([\d,]+\.\d\d)", text, "deposits total").replace(",", "")

problems = []
print(f"report:   {report.as_posix()}, modified {when:%Y-%m-%d %H:%M}")
print(f"covers:   {start} to {end}")
if dates:
    print(f"deposits: {len(dates)}, dated {dates[0]} to {dates[-1]}")
    if dates[0] < start or dates[-1] > end:
        problems.append("deposits outside the week: stale or wrong export")
else:
    problems.append("no deposits listed")
print(f"total:    ${total}")
if len(sys.argv) > 2:
    key = Path(sys.argv[2]).read_text(encoding="utf-8")
    want = find(r"Deposits total \$([\d,]+\.\d\d)", key, "total in the answer key").replace(",", "")
    print(f"key:      ${want}  ({Path(sys.argv[2]).name})")
    if want != total:
        problems.append("total differs from the answer key")

print("\n".join(problems) or "dates and total agree")
sys.exit(1 if problems else 0)
