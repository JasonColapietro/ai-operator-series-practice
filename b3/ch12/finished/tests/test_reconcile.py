"""Tests for scripts/reconcile.py. Practice file, fiction.

The AI Operator Series, Book 3, Chapter 12. The chapter 10 starting tests plus
lane A's three: an empty export, a missing column and a missing file each stop
the run with a message that names the file. Run from the repo root:
    python3 -m unittest discover -s tests
"""
import sys
import tempfile
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import reconcile  # noqa: E402


def dep(day, payer, amount, month=3):
    return {"date": date(2027, month, day), "payer": payer, "amount": Decimal(amount)}


def inv(number, day, client, amount, month=3):
    return {"invoice": number, "date": date(2027, month, day), "client": client,
            "amount": Decimal(amount)}


class ReconcileTest(unittest.TestCase):
    def test_both_date_formats(self):
        self.assertEqual(reconcile.parse_date("03/02/2027"), date(2027, 3, 2))
        self.assertEqual(reconcile.parse_date("2027-03-03"), date(2027, 3, 3))

    def test_second_bank_writes_day_first(self):
        self.assertEqual(reconcile.parse_date("25/03/2027", reconcile.SECOND_BANK_FORMATS),
                         date(2027, 3, 25))

    def test_names_must_match_not_only_amounts(self):
        invoices = [inv("H-1", 2, "HARMON J", "148.50")]
        matches, unmatched, unpaid = reconcile.reconcile([dep(9, "ALDEN R", "148.50")], invoices)
        self.assertEqual(matches, [])
        self.assertEqual([d["payer"] for d in unmatched], ["ALDEN R"])

    def test_payment_in_two_parts(self):
        invoices = [inv("H-2", 3, "PIERCE D", "320.00")]
        deposits = [dep(4, "PIERCE D", "160.00"), dep(5, "PIERCE D", "160.00")]
        matches, unmatched, unpaid = reconcile.reconcile(deposits, invoices)
        self.assertEqual([m[0] for m in matches], ["H-2"])
        self.assertEqual(unmatched, [])

    def test_client_names_normalized(self):
        self.assertEqual(reconcile.client_key("Alvarez, M."), "ALVAREZ M")
        self.assertEqual(reconcile.payer_key("TRANSFER IN HADDAD S"), "HADDAD S")


class ExportGuardTest(unittest.TestCase):
    def write(self, text):
        f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
        f.write(text)
        f.close()
        self.addCleanup(Path(f.name).unlink)
        return f.name

    def test_empty_export_stops_the_run(self):
        path = self.write("date,description,Amount (USD)\n")
        with self.assertRaisesRegex(reconcile.ExportError, "no rows below the header"):
            reconcile.load_deposits(path, second_bank=True)

    def test_missing_column_is_named(self):
        path = self.write("invoice,invoice_date,client,amount\nINV-1,2027-03-22,\"Moreau, J.\",140.00\n")
        with self.assertRaisesRegex(reconcile.ExportError, "missing column invoice_no"):
            reconcile.load_invoices(path)

    def test_missing_file_is_named(self):
        with self.assertRaisesRegex(reconcile.ExportError, "file not found"):
            reconcile.load_deposits("no-such-export.csv")


if __name__ == "__main__":
    unittest.main()
