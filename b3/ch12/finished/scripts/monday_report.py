"""Turn the checker's printed result into Dana's Monday report. Practice file, fiction.

The AI Operator Series, Book 3, Chapter 12. Lane B's finished script.
It reads the lines scripts/reconcile.py prints and writes reports/monday-<date>.md.
It refuses to write a report unless the checker's last line, the summary, is there.
Python standard library only.

Usage, from the repo root (on Windows, py instead of python3):
    python3 scripts/reconcile.py BANK.csv INVOICES.csv [SECOND_BANK.csv] | python3 scripts/monday_report.py YYYY-MM-DD
"""
import re
import sys
from datetime import date
from pathlib import Path

SUMMARY = re.compile(r"^\d+ invoices matched, \d+ deposits with no match, \d+ invoices with no deposit yet\.")


def build_report(checker_lines, monday):
    """Return the report as text, or raise ValueError if the checker did not finish."""
    lines = [l.rstrip() for l in checker_lines if l.strip()]
    if not lines or not SUMMARY.match(lines[-1]):
        raise ValueError("the checker's summary line is missing, so the run did not finish")
    paid = [l for l in lines if l.startswith("PAID")]
    no_match = [l[len("NO MATCH"):].strip() for l in lines if l.startswith("NO MATCH")]
    no_deposit = [l[len("NO DEPOSIT YET"):].strip() for l in lines if l.startswith("NO DEPOSIT YET")]
    out = [f"# Deposits and invoices, week of Monday {monday.isoformat()}", ""]
    out += ["## For Dana to decide", ""]
    out += ["Deposits with no invoice:"] + [f"- {l}" for l in no_match or ["none"]] + [""]
    out += ["Invoices with no deposit yet:"] + [f"- {l}" for l in no_deposit or ["none"]] + [""]
    out += ["## Paid", ""] + [f"- {l}" for l in paid or ["none"]] + [""]
    out += ["## The checker's own last line", "", lines[-1], ""]
    return "\n".join(out)


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[-1].strip())
        return 2
    try:
        monday = date.fromisoformat(argv[1])
    except ValueError:
        print(f"not a date: {argv[1]!r} (write it as YYYY-MM-DD)")
        return 2
    checker_lines = sys.stdin.read().splitlines()
    try:
        report = build_report(checker_lines, monday)
    except ValueError as problem:
        # In a pipe the checker's STOPPED line never reaches the screen, so pass it on.
        for line in checker_lines:
            if line.startswith("STOPPED"):
                print(line)
        print(f"No report written: {problem}.")
        return 1
    out = Path("reports") / f"monday-{monday.isoformat()}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(f"wrote {out.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
