---
name: weekly-numbers
description: "Summarize one week of Harbor & Home jobs from the booking app export (CSV). Use for the Monday numbers or a weekly jobs summary. Not for invoices, quotes or customer email."
---

# Weekly numbers

One week of Harbor & Home's jobs export, turned into a summary Dana can read in two minutes before the crews go out.

## Do not use this skill for
- Invoices, quotes, payroll or taxes.
- Customer email, even when it is about a bill.
- More than one week at a time. Ask for one week's export instead.

## What you need
1. The week's jobs export, as a CSV file.
2. The approved price list: the business facts file, attached or in the Project. If there is none, say so, skip every price check, and do the rest.

## Counting rules
1. Compute every figure from the rows with code. Never estimate.
2. A job is completed only when its status says Completed.
3. Lockout and Late cancel rows are charges, not jobs. Their price goes into money billed, each on a line of its own.
4. Two rows that match in every column are one job exported twice. Count it once and name its job ID.
5. If a column's meaning is unclear, read columns.md in this folder. If you still have to assume, say what you assumed.

## The summary, in this order
1. Three to five sentences on the week, with the key numbers.
2. Completed jobs and money billed by service type, with a total row, the charge lines under it, and the job IDs under each total.
3. By day: jobs scheduled, jobs completed, money billed.
4. Unpaid: job ID, client and amount for each, then the total.
5. Money billed per crew hour, from completed jobs with hours filled in. Name any job left out.
6. Check these: every row whose price doesn't match the price list, has a blank value or looks off, with the job ID, what you found and what the price list says.

## Pass or fail, before you answer
1. Completed jobs by service, plus the charge lines, equal money billed.
2. Paid plus unpaid equal money billed.
3. No job ID appears twice in any list.
4. Every figure that is neither in the file nor a total of listed rows ends with "(my addition)".
If any check fails, recount from the file. Never hand over a summary that fails one.

## Never
- Change, delete or merge a row, even one that looks wrong. Report it in Check these.
- Call a price an overcharge when the price list doesn't cover that size or service. Write "cannot confirm from the price list".
- Flag small-office prices. They are quoted after a walk-through.
- Send, post or share the summary. Dana decides who sees it.

## Last line
End every summary with this line, word for word:
Counted with the weekly-numbers skill, version 1.
