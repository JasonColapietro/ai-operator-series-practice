"""Tests for scripts/monday_report.py. Practice file, fiction.

The AI Operator Series, Book 3, Chapter 12. Lane B's tests. The sample lines are
the checker's output for the practice week of March 22, 2027. Run from the repo root:
    python3 -m unittest discover -s tests
"""
import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import monday_report  # noqa: E402

SAMPLE = """\
PAID  INV-2051  ALVAREZ M  $126.00 on 2027-03-22
PAID  INV-2054  PHAM D  $165.00 on 2027-03-25
NO MATCH  2027-03-26  LAROCHE B  $95.00
NO DEPOSIT YET  INV-2048  BROOKS D  $190.00
2 invoices matched, 1 deposits with no match, 1 invoices with no deposit yet. Deposits total $386.00.
""".splitlines()


class MondayReportTest(unittest.TestCase):
    def test_lists_what_dana_decides(self):
        report = monday_report.build_report(SAMPLE, date(2027, 3, 22))
        self.assertIn("week of Monday 2027-03-22", report)
        self.assertIn("- 2027-03-26  LAROCHE B  $95.00", report)
        self.assertIn("- INV-2048  BROOKS D  $190.00", report)

    def test_keeps_the_checker_summary_word_for_word(self):
        report = monday_report.build_report(SAMPLE, date(2027, 3, 22))
        self.assertIn(SAMPLE[-1], report)

    def test_refuses_without_the_summary_line(self):
        with self.assertRaises(ValueError):
            monday_report.build_report(SAMPLE[:-1], date(2027, 3, 22))

    def test_refuses_a_stopped_run(self):
        stopped = ["STOPPED  bank-second.csv: no rows below the header. Nothing was matched."]
        with self.assertRaises(ValueError):
            monday_report.build_report(stopped, date(2027, 3, 22))


if __name__ == "__main__":
    unittest.main()
