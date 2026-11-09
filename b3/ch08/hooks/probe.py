"""Probe hook: append what each event sends to hooks/probe.jsonl. Blocks nothing."""
import sys
from pathlib import Path

log = Path(__file__).with_name("probe.jsonl")
with log.open("a", encoding="utf-8") as f:
    f.write(sys.stdin.read().strip() + "\n")
