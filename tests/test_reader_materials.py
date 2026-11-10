"""Exercise the standalone starter, copied skills, scan arithmetic and delivery review.

Run from the practice set root: python3 -m unittest discover -s tests -v
All changes made by these tests stay inside temporary directories.
"""
import collections
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_script(script, *args, cwd=None):
    return subprocess.run(
        [sys.executable, str(script), *map(str, args)], cwd=cwd,
        capture_output=True, text=True, timeout=20,
    )


class ReaderMaterialsTests(unittest.TestCase):
    def test_every_chapter_has_reader_instructions(self):
        for book, chapters in [(1, 15), (2, 15), (3, 16), (4, 14), (5, 15)]:
            for chapter in range(1, chapters + 1):
                path = ROOT / f'b{book}/ch{chapter:02d}/README.txt'
                with self.subTest(chapter=str(path.relative_to(ROOT))):
                    self.assertTrue(path.is_file())
                    self.assertTrue(path.read_text().strip())

    def test_standalone_library_has_every_reply_skill_input(self):
        # Follow the revised copy-and-rename steps as a reader starting at Book 3.
        with tempfile.TemporaryDirectory() as folder:
            library = Path(folder)
            project = library / 'projects/harbor-home'
            project.mkdir(parents=True)
            (library / 'skills').mkdir()
            (library / 'briefs').mkdir()
            shutil.copyfile(ROOT / 'shared/harbor-home-business-facts.txt', project / 'facts.md')
            for name in ['instructions.md', 'brief.md', 'voice.md']:
                shutil.copyfile(ROOT / 'b2/ch04' / name, project / name)
            shutil.copytree(ROOT / 'b2/ch11/weekly-numbers', library / 'skills/weekly-numbers')
            shutil.copyfile(ROOT / 'b2/ch15/dana-first-agent-job.txt', library / 'everything-else.md')
            shutil.copyfile(ROOT / 'b3/ch01/sam-reconcile-brief.txt', library / 'briefs/reconcile.md')
            shutil.copyfile(ROOT / 'b2/front/keeper-1-reply-from-approved-facts.txt', library / 'keepers.md')
            self.assertEqual((project / 'facts.md').read_bytes(), (ROOT / 'shared/harbor-home-business-facts.txt').read_bytes())
            self.assertIn('HARBOR & HOME CLEANING: PROJECT BRIEF', (project / 'brief.md').read_text())
            self.assertIn('Keeper #1', (library / 'keepers.md').read_text())
            self.assertTrue((library / 'skills/weekly-numbers/SKILL.md').is_file())
            self.assertTrue((library / 'briefs/reconcile.md').is_file())
            self.assertIn('voice sample', (project / 'instructions.md').read_text().lower())
            self.assertIn('price or a date from its sample emails', (ROOT / 'b3/ch07/harbor-reply/SKILL.md').read_text())

    def test_windows_copy_checker_detects_missing_and_drifted_skill(self):
        script = ROOT / 'b3/ch07/check_skill_copies.py'
        with tempfile.TemporaryDirectory() as folder:
            library = Path(folder)
            source = library / '.agents/skills/harbor-reply'
            source.parent.mkdir(parents=True)
            shutil.copytree(ROOT / 'b3/ch07/harbor-reply', source)
            missing = run_script(script, cwd=library)
            self.assertEqual(missing.returncode, 1)
            self.assertIn('missing copy', missing.stdout)
            copied = library / '.claude/skills/harbor-reply'
            copied.parent.mkdir(parents=True)
            shutil.copytree(source, copied)
            same = run_script(script, cwd=library)
            self.assertEqual(same.returncode, 0, same.stderr)
            (copied / 'SKILL.md').write_text('drifted copy\n')
            drift = run_script(script, cwd=library)
            self.assertEqual(drift.returncode, 1)
            self.assertIn('differs: harbor-reply/SKILL.md', drift.stdout)

    def test_reviewer_protects_actual_evidence_directory(self):
        text = (ROOT / 'b3/ch10/claude/agents/reviewer.md').read_text()
        self.assertIn('5. No line in scripts/ writes to practice/ or projects/.', text)
        self.assertNotIn('writes to incoming/', text)
        self.assertIn('.claude/agents/reviewer.md', (ROOT / 'b3/ch10/codex/agents/reviewer.toml').read_text())

    def test_delivery_pattern_examples_and_empty_input(self):
        script = ROOT / 'b5/ch12/checks/check_delivery.py'
        facts = ROOT / 'shared/harbor-home-business-facts.txt'
        for case, expected in [('delivery', 0), ('broken-price', 1), ('broken-saturday', 1), ('checks', 2)]:
            with self.subTest(case=case):
                result = run_script(script, facts, ROOT / 'b5/ch12' / case)
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                if expected == 0:
                    self.assertIn('0 pattern findings. Owner review required.', result.stdout)

    def test_zero_pattern_findings_never_omit_owner_review(self):
        # A dollar string can exist in the facts yet be wrong for the service;
        # natural-language availability can fall outside a pattern match.
        script = ROOT / 'b5/ch12/checks/check_delivery.py'
        facts = ROOT / 'shared/harbor-home-business-facts.txt'
        for name in ['wrong-service-price.md', 'unapproved-day.md']:
            with self.subTest(case=name):
                result = run_script(script, facts, ROOT / 'b5/ch12/owner-review-cases' / name)
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stdout.strip(), 'PASS: 1 file(s) read, 0 pattern findings. Owner review required.')
        self.assertIn('Owner review (name, time, prices with service/size checked', (ROOT / 'b5/ch12/evidence-template.md').read_text())

    def test_figure_6_3_key_arithmetic_and_coverage(self):
        key = (ROOT / 'b5/ch06/scorecard-key.md').read_text()
        rows = []
        for line in key.splitlines():
            if re.match(r'^\| Q\d+ \|', line):
                rows.append([x.strip() for x in line.strip('|').split('|')])
        self.assertEqual(len(rows), 10)
        totals = collections.Counter(mark for row in rows for mark in row[3:])
        self.assertEqual(totals, {'N': 12, 'X': 17, '0': 7, 'E': 3, 'B': 1})
        for subset, named, answered in [(rows[:7], 3, 25), (rows[7:], 9, 11)]:
            marks = [mark for row in subset for mark in row[3:]]
            self.assertEqual(marks.count('N'), named)
            self.assertEqual(sum(x not in ('E', 'B') for x in marks), answered)
        for engine, expected in enumerate([(4, 10), (3, 9), (2, 8), (3, 9)], 3):
            marks = [row[engine] for row in rows]
            self.assertEqual((marks.count('N'), sum(x not in ('E', 'B') for x in marks)), expected)


if __name__ == '__main__':
    unittest.main()
