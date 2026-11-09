"""Tests for scripts/reconcile.py. Practice file, fiction.

The AI Operator Series, Book 3, Chapter 4. Run from the folder that holds tests/:
    python3 -m unittest discover -s tests
"""
import sys
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import reconcile  # noqa: E402


def dep(day, payer, amount):
    return {"line": 0, "date": date(2027, 3, day), "payer": payer,
            "key": reconcile.name_key(payer), "amount": Decimal(amount)}


def inv(number, day, client, amount):
    return {"invoice": number, "date": date(2027, 3, day), "client": client,
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

    def test_deposit_with_no_invoice_is_reported(self):
        _, unmatched, _ = reconcile.reconcile(
            [dep(19, "TRANSFER IN M OYELARAN", "95.00")],
            [inv("INV-1", 18, "Brooks, D.", "190.00")])
        self.assertEqual(len(unmatched), 1)

    def test_payment_in_two_parts(self):
        matches, unmatched, _ = reconcile.reconcile(
            [dep(17, "TRANSFER IN R PATEL", "142.50"), dep(18, "TRANSFER IN R PATEL", "142.50")],
            [inv("INV-2", 17, "Patel, R.", "285.00")])
        self.assertEqual(unmatched, [])
        self.assertEqual(matches[0][0][0]["invoice"], "INV-2")

    def test_one_deposit_two_invoices(self):
        matches, unmatched, _ = reconcile.reconcile(
            [dep(17, "TRANSFER IN LINDQVIST RENTALS LLC", "460.00")],
            [inv("INV-3", 16, "Lindqvist Rentals LLC (Unit A)", "320.00"),
             inv("INV-4", 16, "Lindqvist Rentals LLC (Unit B)", "140.00")])
        self.assertEqual(unmatched, [])
        self.assertEqual(sorted(i["invoice"] for i in matches[0][0]), ["INV-3", "INV-4"])


if __name__ == "__main__":
    unittest.main()
