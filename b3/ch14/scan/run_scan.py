"""Ask the locked questions, keep every raw answer, stop on an empty one.
Practice file, fiction (The AI Operator Series, Book 3, Chapter 14, Listing 14.1).
Usage, from the repo root: python3 scan/run_scan.py [ENGINE ...] [HOW_MANY_QUESTIONS]
"""
import json, re, subprocess, sys, tempfile
from datetime import datetime
from pathlib import Path

SCAN = Path(__file__).resolve().parent
RUNS = 3          # every question, three times per engine
TIMEOUT = 600     # seconds to wait for one answer
ENGINES = {       # one adapter per engine; the question is added last
    "claude": ["claude", "-p", "--safe-mode", "--output-format", "text", "--permission-mode",
               "dontAsk", "--allowedTools", "WebSearch,WebFetch", "--max-budget-usd", "1"],
    "codex": ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only",
              "-c", 'web_search="live"'],
    "practice": [sys.executable, str(SCAN / "practice_engine.py")],
}

args = sys.argv[1:]
limit = int(args.pop()) if args and args[-1].isdigit() else None
engines = args or ["claude", "codex"]
text = (SCAN / "prompts.md").read_text(encoding="utf-8")
questions = re.findall(r"^(Q\d\d)\. (.+)$", text, re.M)[:limit]
names = [n.strip() for n in (SCAN / "names.txt").read_text(encoding="utf-8").splitlines()
         if n.strip() and not n.startswith("#")]
stamp = datetime.now().strftime("%Y-%m-%dT%H%M%S")
blank = tempfile.mkdtemp()  # an empty folder, so no file from this repo reaches the engine

for engine in engines:
    for qid, question in questions:
        for run in range(1, RUNS + 1):
            raw = SCAN / "raw" / stamp / f"{engine}-{qid}-r{run}.txt"
            raw.parent.mkdir(parents=True, exist_ok=True)
            try:
                done = subprocess.run(ENGINES[engine] + [question], cwd=blank, stdin=subprocess.DEVNULL,
                                      capture_output=True, text=True, timeout=TIMEOUT)
                answer, code, err = done.stdout.strip(), done.returncode, done.stderr
            except subprocess.TimeoutExpired:
                answer, code, err = "", "timeout", ""
            raw.write_text(answer, encoding="utf-8")       # on disk before anything else happens
            raw.with_suffix(".err.txt").write_text(err, encoding="utf-8")
            status = "empty" if not answer else "answered" if code == 0 else "blocked"
            named = [n for n in names if n.lower() in answer.lower()] if status == "answered" else []
            row = {"stamp": stamp, "engine": engine, "question": qid, "run": run, "status": status,
                   "named": named, "planned": len(questions) * RUNS,
                   "raw": raw.relative_to(SCAN.parent).as_posix()}
            with open(SCAN / "results.jsonl", "a", encoding="utf-8") as results:
                results.write(json.dumps(row) + "\n")          # append, never rewrite
            if status == "empty":
                sys.exit(f"ENGINE FAILURE: {engine} returned nothing for {qid}, run {run}. "
                         f"Read {raw.with_suffix('.err.txt').name}. Run stopped; this is not a miss.")
print(f"Scan {stamp} finished: {len(engines)} engine(s), {len(questions)} question(s), {RUNS} runs each.")
