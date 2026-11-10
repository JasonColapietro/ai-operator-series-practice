"""Exit 1 if a skill in .claude/skills/ differs from its source in .agents/skills/."""
import sys
from pathlib import Path

SOURCE = Path(".agents/skills")
COPY = Path(".claude/skills")


def files(root):
    return {p.relative_to(root).as_posix(): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


problems = []
for skill in sorted(p for p in SOURCE.iterdir() if p.is_dir()):
    copy = COPY / skill.name
    if not copy.is_dir():
        problems.append(f"missing copy: {copy.as_posix()}")
        continue
    source_files, copy_files = files(skill), files(copy)
    for name in sorted(source_files.keys() | copy_files.keys()):
        if source_files.get(name) != copy_files.get(name):
            problems.append(f"differs: {skill.name}/{name}")

print("\n".join(problems) or "skill copies match")
sys.exit(1 if problems else 0)
