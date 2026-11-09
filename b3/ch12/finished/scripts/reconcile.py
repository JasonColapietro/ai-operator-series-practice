"""Check bank deposits against invoices. Practice file, fiction.

The AI Operator Series, Book 3, Chapter 12. Lane A's finished checker: the
chapter 10 starting copy plus one change, read_rows(), which stops the run
with a plain message when an export is missing, empty or short a column.
If your chapter 10 review changed how deposits match, keep your version and
compare only read_rows() and the two places that call it.
Python standard library only.

Usage, from the repo root:
    python3 scripts/reconcile.py BANK.csv INVOICES.csv [SECOND_BANK.csv]
"""
import csv
import sys
from datetime import datetime
from decimal import Decimal

FIRST_BANK_FORMATS = ("%m/%d/%Y", "%Y-%m-%d")  # the first bank uses both
SECOND_BANK_FORMATS = ("%d/%m/%Y",)  # the second bank writes the day first


def parse_date(text, formats=FIRST_BANK_FORMATS):
    for fmt in formats:
        try:
            return datetime.strptime(text.strip(), fmt).date()
        except ValueError:
            pass
    raise ValueError(f"unknown date format: {text!r}")


def payer_key(description):
    """'CARD SETTLEMENT ALVAREZ M' or 'TRANSFER IN HADDAD S' -> the name."""
    text = description.upper()
    for prefix in ("CARD SETTLEMENT", "TRANSFER IN", "TRANSFER FROM"):
        text = text.replace(prefix, "")
    return text.strip()


def client_key(client):
    """'Alvarez, M.' -> 'ALVAREZ M'."""
    return " ".join(client.upper().replace(",", " ").replace(".", " ").split())


class ExportError(Exception):
    """An export the checker can't trust. The run stops instead of guessing."""


def read_rows(path, columns):
    """Return the rows of one export, or raise ExportError naming the file."""
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        raise ExportError(f"{path}: file not found") from None
    missing = [c for c in columns if c not in (reader.fieldnames or [])]
    if missing:
        raise ExportError(f"{path}: missing column {', '.join(missing)}")
    if not rows:
        raise ExportError(f"{path}: no rows below the header")
    return rows


def load_deposits(path, second_bank=False):
    formats = SECOND_BANK_FORMATS if second_bank else FIRST_BANK_FORMATS
    amount_column = "Amount (USD)" if second_bank else "amount"
    rows = read_rows(path, ("date", "description", amount_column))
    return [
        {"date": parse_date(r["date"], formats), "payer": payer_key(r["description"]),
         "amount": Decimal(r[amount_column])}
        for r in rows
    ]


def load_invoices(path):
    rows = read_rows(path, ("invoice_no", "invoice_date", "client", "amount"))
    return [
        {"invoice": r["invoice_no"], "date": parse_date(r["invoice_date"]),
         "client": client_key(r["client"]), "amount": Decimal(r["amount"])}
        for r in rows
    ]


def reconcile(deposits, invoices):
    """Return (matches, unmatched deposits, invoices with no deposit).

    Pass 1: a deposit matches an open invoice with the same client and amount,
    dated on or before the deposit. Pass 2: two leftover deposits from one
    client that add up to one open invoice pay it in two parts.
    """
    open_invoices = sorted(invoices, key=lambda i: i["date"])
    matches, left = [], []
    for dep in sorted(deposits, key=lambda d: d["date"]):
        hit = next((i for i in open_invoices if i["client"] == dep["payer"]
                    and i["amount"] == dep["amount"] and i["date"] <= dep["date"]), None)
        if hit:
            open_invoices.remove(hit)
            matches.append((hit["invoice"], [dep]))
        else:
            left.append(dep)
    unmatched = []
    while left:
        dep = left.pop(0)
        pair = next((other for other in left if other["payer"] == dep["payer"]), None)
        hit = None
        if pair:
            total = dep["amount"] + pair["amount"]
            hit = next((i for i in open_invoices if i["client"] == dep["payer"]
                        and i["amount"] == total and i["date"] <= dep["date"]), None)
        if hit:
            left.remove(pair)
            open_invoices.remove(hit)
            matches.append((hit["invoice"], [dep, pair]))
        else:
            unmatched.append(dep)
    return matches, unmatched, open_invoices


def main(argv):
    if len(argv) not in (3, 4):
        print(__doc__.strip().splitlines()[-1].strip())
        return 2
    try:
        deposits = load_deposits(argv[1])
        if len(argv) == 4:
            deposits += load_deposits(argv[3], second_bank=True)
        invoices = load_invoices(argv[2])
    except ExportError as problem:
        print(f"STOPPED  {problem}. Nothing was matched.")
        return 2
    matches, unmatched, unpaid = reconcile(deposits, invoices)
    for invoice, deps in sorted(matches):
        parts = " + ".join(f"${d['amount']} on {d['date']}" for d in deps)
        label = "PAID IN TWO PARTS" if len(deps) == 2 else "PAID"
        print(f"{label}  {invoice}  {deps[0]['payer']}  {parts}")
    for dep in unmatched:
        print(f"NO MATCH  {dep['date']}  {dep['payer']}  ${dep['amount']}")
    for inv in unpaid:
        print(f"NO DEPOSIT YET  {inv['invoice']}  {inv['client']}  ${inv['amount']}")
    total_in = sum(d["amount"] for d in deposits)
    print(f"{len(matches)} invoices matched, {len(unmatched)} deposits with no match, "
          f"{len(unpaid)} invoices with no deposit yet. Deposits total ${total_in}.")
    return 1 if unmatched else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
