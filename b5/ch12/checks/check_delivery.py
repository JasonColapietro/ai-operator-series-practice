# PRACTICE FILE, FICTION LABEL: The AI Operator Series, Book 5, Chapter 12, Deliver With Agents.
# Listing 12.1. Scans customer-facing files for price, appointment and promise patterns.
# Harbor & Home Cleaning, Dana Ruiz and Sam Rivera are invented. Python standard library only.
#
# Usage: python3 check_delivery.py FACTS_FILE PATH [PATH ...]
#   PATH may be a file or a folder. Folders are read for every .md and .txt file inside them.
# Exit 0: no pattern findings; owner review is required. Exit 1: pattern findings.
# Exit 2: nothing was read, so nothing was checked.
import re
import sys
from pathlib import Path

WEEKDAYS = "Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday"
RULES = [
    # 1. A price the facts file does not state.
    ("price", re.compile(r"\$\d[\d,]*(?:\.\d\d)?")),
    # 2. A day or time offered as if it were booked.
    ("appointment", re.compile(r"\b\d{1,2}(?::\d\d)?\s?(?:a\.m\.|p\.m\.|am\b|pm\b)"
                               rf"|\b(?:this|next) (?:{WEEKDAYS})\b|\b(?:{WEEKDAYS}) at\b"
                               r"|\bconfirmed\b|\byou're (?:all set|booked)\b|\bsee you\b", re.I)),
    # 3. A reply-time or availability promise nobody approved.
    ("promise", re.compile(r"\bwithin (?:\w+ ){0,2}(?:minute|hour|day)s?\b|24/7|around the clock"
                           r"|\bright away\b|\bsame[- ]day\b|\bimmediately\b", re.I)),
]


def money(s):
    return s.replace("$", "").replace(",", "").removesuffix(".00")


def main(argv):
    if len(argv) < 3:
        print(__doc__ or "usage: check_delivery.py FACTS_FILE PATH [PATH ...]")
        return 2
    facts = Path(argv[1]).read_text(encoding="utf-8")
    facts_lower = facts.lower()
    approved_prices = {money(m) for m in RULES[0][1].findall(facts)}

    files = []
    for p in map(Path, argv[2:]):
        if p.is_dir():
            files += sorted(f for f in p.rglob("*") if f.suffix in (".md", ".txt"))
        elif p.is_file():
            files.append(p)
    if not files:
        print("CANNOT CHECK, no .md or .txt files found in", " ".join(argv[2:]))
        return 2

    findings = []
    for f in files:
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith(("#", "<!--")):
                continue  # headings and file labels are notes to the reader, not customer text
            for kind, rx in RULES:
                for m in rx.finditer(line):
                    hit = m.group(0)
                    if kind == "price" and money(hit) in approved_prices:
                        continue
                    if kind == "promise" and hit.lower() in facts_lower:
                        continue
                    findings.append(f"{f}:{n}  {kind}  \"{hit}\"")

    if findings:
        print("\n".join(findings))
        print(f"FAIL: {len(findings)} finding(s) in {len(files)} file(s) read")
        return 1
    print(f"PASS: {len(files)} file(s) read, 0 pattern findings. Owner review required.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
