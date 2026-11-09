"""Tests for scripts/reconcile.py. Practice file, fiction.

The AI Operator Series, Book 3, Chapter 10. Sam's twelve tests at the start of
the chapter: the ones written in chapter 4 and after, plus chapter 6's three for
the second bank and its fixture, tests/fixtures/second-bank-sample.csv (twelve
made-up rows; row 9 matches no invoice on purpose). Run from the repo root:
    python3 -m unittest discover -s tests
"""
import sys
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))
import reconcile  # noqa: E402


def dep(day, payer, amount, month=3):
    return {"line": 0, "date": date(2027, month, day), "payer": payer,
            "key": reconcile.name_key(payer), "amount": Decimal(amount)}


def inv(number, day, client, amount, month=3):
    return {"invoice": number, "date": date(2027, month, day), "client": client,
            "key": reconcile.name_key(client), "amount": Decimal(amount)}


class ReconcileTest(unittest.TestCase):
    def test_reads_both_date_formats(self):
        self.assertEqual(reconcile.parse_date("03/15/2027"), date(2027, 3, 15))
        self.assertEqual(reconcile.parse_date("2027-03-17"), date(2027, 3, 17))

    def test_unknown_date_is_an_error_not_a_skip(self):
        with self.assertRaises(ValueError):
            reconcile.parse_date("17 Mar 2027")

    def test_names_match_in_either_order(self):
        self.assertEqual(reconcile.name_key("TRANSFER IN R PATEL"), reconcile.name_key("Patel, R."))

    def test_names_must_match_not_only_amounts(self):
        matches, unmatched, _ = reconcile.reconcile(
            [dep(9, "TRANSFER IN ALDEN R", "148.50")], [inv("INV-1", 2, "Harmon, J.", "148.50")])
        self.assertEqual(matches, [])
        self.assertEqual(len(unmatched), 1)

    def test_deposit_with_no_invoice_is_reported(self):
        _, unmatched, _ = reconcile.reconcile(
            [dep(19, "TRANSFER IN M OYELARAN", "95.00")],
            [inv("INV-2", 18, "Brooks, D.", "190.00")])
        self.assertEqual(len(unmatched), 1)

    def test_deposit_before_its_invoice_does_not_match(self):
        matches, _, still_open = reconcile.reconcile(
            [dep(10, "CARD SETTLEMENT CHEN L", "148.50")], [inv("INV-3", 12, "Chen, L.", "148.50")])
        self.assertEqual(matches, [])
        self.assertEqual([i["invoice"] for i in still_open], ["INV-3"])

    def test_invoice_with_no_deposit_stays_open(self):
        _, _, still_open = reconcile.reconcile([], [inv("INV-4", 18, "Brooks, D.", "190.00")])
        self.assertEqual([i["invoice"] for i in still_open], ["INV-4"])

    def test_payment_in_two_parts(self):
        matches, unmatched, _ = reconcile.reconcile(
            [dep(17, "TRANSFER IN R PATEL", "142.50"), dep(18, "TRANSFER IN R PATEL", "142.50")],
            [inv("INV-5", 17, "Patel, R.", "285.00")])
        self.assertEqual(unmatched, [])
        self.assertEqual(matches[0][0][0]["invoice"], "INV-5")

    def test_one_deposit_two_invoices(self):
        matches, unmatched, _ = reconcile.reconcile(
            [dep(17, "TRANSFER IN LINDQVIST RENTALS LLC", "460.00")],
            [inv("INV-6", 16, "Lindqvist Rentals LLC (Unit A)", "320.00"),
             inv("INV-7", 16, "Lindqvist Rentals LLC (Unit B)", "140.00")])
        self.assertEqual(unmatched, [])
        self.assertEqual(sorted(i["invoice"] for i in matches[0][0]), ["INV-6", "INV-7"])

    def test_second_bank_writes_day_first(self):
        self.assertEqual(reconcile.parse_date("25/03/2027", reconcile.SECOND_BANK_FORMATS),
                         date(2027, 3, 25))
        self.assertEqual(reconcile.parse_date("05/03/2027", reconcile.SECOND_BANK_FORMATS),
                         date(2027, 3, 5))

    def test_second_bank_amount_column(self):
        rows = reconcile.load_deposits(HERE / "fixtures" / "second-bank-sample.csv", second_bank=True)
        self.assertEqual(len(rows), 12)
        self.assertEqual(rows[0]["amount"], Decimal("126.00"))

    def test_second_bank_fixture_row_9_is_unmatched(self):
        rows = reconcile.load_deposits(HERE / "fixtures" / "second-bank-sample.csv", second_bank=True)
        invoices = [inv(f"INV-{n}", r["date"].day, r["payer"].replace("TRANSFER IN ", ""), r["amount"])
                    for n, r in enumerate(rows, start=10) if n != 18]
        _, unmatched, _ = reconcile.reconcile(rows, invoices)
        self.assertEqual([(d["line"], d["payer"]) for d in unmatched], [(10, "TRANSFER IN VOSS K")])


if __name__ == "__main__":
    unittest.main()
