"""A pretend engine for practice runs. Practice file, fiction.
The AI Operator Series, Book 3, Chapter 14. It answers each locked question
with the matching file in practice-answers/, which is invented text, not a real
AI answer. Empty one of those files to test the scan's empty-answer alarm.
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
question = sys.argv[-1]
text = (HERE / "prompts.md").read_text(encoding="utf-8")
for qid, locked in re.findall(r"^(Q\d\d)\. (.+)$", text, re.M):
    if locked == question:
        print((HERE / "practice-answers" / f"{qid}.txt").read_text(encoding="utf-8").strip())
        break
