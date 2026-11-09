# incidents.md

Newest at the bottom. Each entry: date, what happened, the rule
it produced, and where that rule now lives.

## 2027-03-22: the bank file was "fixed"
What happened: asked why the totals didn't match, the agent
rewrote the bank export's dates into one format and merged
Patel's two $142.50 transfers into one row. Restored with
git restore.
Rule: never change an export to make totals agree; report the row.
Lives in: AGENTS.md, rule 1.

## 2027-03-23: facts.md was tidied
What happened: while writing the checker, the agent changed
"from $260" to "from 260" in the price list. Nobody asked,
and its "done" message didn't mention it. Rewound.
Rule: never reformat facts.md.
Lives in: AGENTS.md, rule 2.

## 2027-03-23: "all deposits matched" was false
What happened: the agent's report said every deposit matched.
The checker had read five of nine rows, and the audit had
found a deposit that matched no invoice.
Rule: "all matched" only when the checker printed zero
unmatched in this session, with its last line pasted in.
Lives in: AGENTS.md, rule 3.

## 2027-04-05: April read as February
What happened: the agent changed the checker to try day-first
dates first, so 04/02/2027 became February 4. It left
Sullivan's $126.00 out as "outside the week" and called a
paid invoice unpaid.
Rule: slash dates in bank exports are month first.
Lives in: AGENTS.md, rule 4.

## 2027-04-05: a package nobody asked for
What happened: the agent added "import pandas" to the checker
and asked to install it. Declined and rewound.
Rule: standard library only in scripts/, tests/ and hooks/.
Lives in: AGENTS.md, rule 5.
