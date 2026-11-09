# Ten eval scenarios for harbor-ops

Practice file, fiction. The AI Operator Series, Book 3, Chapter 11. Harbor & Home Cleaning, Dana Ruiz, Sam Rivera and every customer named here are invented. Give these to `claude plugin eval init` when its interview asks what the plugin should and shouldn't do. Each line says what a person types and what a good run does. Write your own expected results before you run anything, the way chapter 7's trigger test did.

| # | The request | What a good run does |
|---|---|---|
| 1 | "Draft a reply to Laura Bettencourt's email in the inbox." | Loads harbor-reply. The 2,000 sq ft deep-clean price and the Monday date are [CHECK] markers; the vacuum gets a plain yes. |
| 2 | "A customer asks what a standard clean costs for 1,200 sq ft. Draft the reply." | Loads harbor-reply. Quotes the "from" price in facts.md with the square footage it covers. |
| 3 | "Our supply vendor wants net-15 invoice terms. Draft a reply." | Loads no skill. Supplier mail is Dana's. |
| 4 | "Someone applied for weekend shifts. Write back." | Loads no skill. Job-applicant mail is Dana's. |
| 5 | "Write Dana's Monday numbers summary from this week's export." | Loads weekly-numbers. |
| 6 | "Match this week's deposits to the open invoices." | Loads neither skill. weekly-numbers is not for invoices; this is the checker's job. |
| 7 | "Make the price wording consistent in projects/harbor-home/facts.md." | The guard blocks the edit and the agent writes a proposal to reviews/ instead. |
| 8 | "Use the reviewer agent on scripts/reconcile.py." | The reviewer reads and reports. No file changes. |
| 9 | "Rename amt to amount_due in scripts/reconcile.py." | Loads no skill. The edited file comes back formatted. |
| 10 | "Quote a deep clean for a 1,800 sq ft house, like the one in Dana's old email." | Loads harbor-reply. The price is a [CHECK]; the old $285 from voice.md is never reused. |

Scenarios 7 to 9 test the hooks and the reviewer. A case the eval can't set up on its own machine (an inbox file, a facts file) needs its files in the case folder; let the interview tell you what it can build, and drop a scenario rather than fake one.
