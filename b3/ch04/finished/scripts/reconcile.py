"""Check bank deposits against invoices. Practice file, fiction.

The AI Operator Series, Book 3, Chapter 4. One finished version of the checker,
for comparing with yours. Yours will differ; the answer key says which results
count as right. Python standard library only.

Usage, from the repo root:
    python3 scripts/reconcile.py BANK.csv INVOICES.csv
"""
import csv
import re
import sys
from datetime import datetime
from decimal import Decimal

DATE_FORMATS = ("%m/%d/%Y", "%Y-%m-%d")  # the bank export uses both
BANK_WORDS = ("CARD SETTLEMENT", "TRANSFER IN", "TRANSFER FROM")


def parse_date(text):
    """Read either date format. Never skip a row: an unknown format is an error."""
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text.strip(), fmt).date()
        except ValueError:
            pass
    raise ValueError(f"unknown date format: {text!r}")


def name_key(name):
    """A name as a set of words, so 'R PATEL' and 'Patel, R.' agree.

    Bank wording and anything in parentheses, such as '(Unit A)', are dropped.
    """
    name = re.sub(r"\(.*?\)", " ", name.upper())
    for words in BANK_WORDS:
        name = name.replace(words, " ")
    return frozenset(re.sub(r"[^A-Z0-9 ]", " ", name).split())


def load_deposits(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [
            {"line": n, "date": parse_date(r["date"]), "payer": r["description"],
             "key": name_key(r["description"]), "amount": Decimal(r["amount"])}
            for n, r in enumerate(csv.DictReader(f), start=2)
        ]


def load_invoices(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [
            {"invoice": r["invoice_no"], "date": parse_date(r["invoice_date"]),
             "client": r["client"], "key": name_key(r["client"]),
             "amount": Decimal(r["amount"])}
            for r in csv.DictReader(f)
        ]


def reconcile(deposits, invoices):
    """Return (matches, unmatched deposits, invoices still open).

    A deposit matches an open invoice with the same payer and amount, dated on or
    before the deposit. Then two rules from Dana's job: two deposits from one
    payer that add up to one invoice are one payment in two parts, and one
    deposit that equals two of a payer's open invoices pays both.
    """
    open_inv = sorted(invoices, key=lambda i: i["date"])
    matches, left = [], []

    def fits(inv, dep):
        return inv["key"] == dep["key"] and inv["date"] <= dep["date"]

    for dep in sorted(deposits, key=lambda d: d["date"]):
        hit = next((i for i in open_inv if fits(i, dep) and i["amount"] == dep["amount"]), None)
        if hit:
            open_inv.remove(hit)
            matches.append(([hit], [dep]))
        else:
            left.append(dep)

    unmatched = []
    while left:
        dep = left.pop(0)
        pair = next((d for d in left if d["key"] == dep["key"]), None)
        hit = pair and next((i for i in open_inv if fits(i, dep)
                             and i["amount"] == dep["amount"] + pair["amount"]), None)
        if hit:
            left.remove(pair)
            open_inv.remove(hit)
            matches.append(([hit], [dep, pair]))
            continue
        mine = [i for i in open_inv if fits(i, dep)]
        two = next(((a, b) for k, a in enumerate(mine) for b in mine[k + 1:]
                    if a["amount"] + b["amount"] == dep["amount"]), None)
        if two:
            for i in two:
                open_inv.remove(i)
            matches.append((list(two), [dep]))
            continue
        unmatched.append(dep)
    return matches, unmatched, open_inv


def main(argv):
    if len(argv) != 3:
        print("usage: python3 scripts/reconcile.py BANK.csv INVOICES.csv")
        return 2
    matches, unmatched, still_open = reconcile(load_deposits(argv[1]), load_invoices(argv[2]))
    for invs, deps in matches:
        if len(deps) == 2:
            parts = " + ".join(f"${d['amount']} on {d['date']}" for d in deps)
            print(f"PAID IN TWO PARTS  {invs[0]['invoice']}  {invs[0]['client']}  {parts}")
        if len(invs) == 2:
            print(f"ONE DEPOSIT, TWO INVOICES  ${deps[0]['amount']} on {deps[0]['date']}  "
                  f"pays {invs[0]['invoice']} and {invs[1]['invoice']}")
    for dep in unmatched:
        print(f"NO MATCH  line {dep['line']}  {dep['date']}  {dep['payer']}  ${dep['amount']}")
    for inv in still_open:
        print(f"NO DEPOSIT YET  {inv['invoice']}  {inv['client']}  ${inv['amount']}")
    n = len(unmatched)
    print(f"{len(deposits_used(matches))} deposits matched, {n} deposit{'' if n == 1 else 's'} with no match")
    return 1 if unmatched else 0


def deposits_used(matches):
    return [d for _, deps in matches for d in deps]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
