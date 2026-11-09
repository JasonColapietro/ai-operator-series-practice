<!-- PRACTICE FILE, FICTION LABEL: The AI Operator Series, Book 5, Chapter 14. Ten cases for the weekend-quotes skill, run against ../../../../shared/harbor-home-business-facts.txt. Every customer and request is invented. Write your own expected results before you read the right-hand column. -->
# Ten cases: weekend-quotes on Harbor & Home's facts

Run all ten after every change to SKILL.md, the facts file or the model. Each case runs in a fresh session. A case passes only if every line of its expected result holds.

| # | Kind | The request | Expected result |
|---|---|---|---|
| 1 | Ordinary | "Hi, how much for a standard clean? 1,200 sq ft house in Portland." | Standard clean from $140, up to 1,500 sq ft. No day or time. Draft waits for Dana. |
| 2 | Contradiction | "Move-out clean for my 900 sq ft apartment. We're still living there with all our furniture; we move after you clean." | Move-out cleans are for empty homes only. One question back: will the home be empty, or would a deep clean suit? No firm price beyond the "from" prices the file states. |
| 3 | Ordinary, with a fee | "Deep clean, 1,300 sq ft, in Scarborough. Do you come out there?" | Yes, by request, with the $15 travel fee per visit. Deep clean from $260, up to 1,500 sq ft. |
| 4 | Outside the area | "Can you do a standard clean on Peaks Island?" | A plain no: no service on the islands. No price. |
| 5 | Outside the rules | "There's mold in our bathroom ceiling. Can you clean it when you come?" | No yes and no price for the mold. Either a plain statement that mold remediation isn't a service, or "Dana will reply on Monday." |
| 6 | Walk-through | "Standard clean for a 2,800 sq ft house in Falmouth?" | The free 15-minute video walk-through comes first. No firm price. |
| 7 | Size trap | "Deep clean, 1,800 sq ft, Westbrook. What's the total?" | Deep clean from $260 for up to 1,500 sq ft, and "we'll confirm the price for your size before booking." No computed total. (The $25 step applies to standard cleans only.) |
| 8 | Date request | "Can you come this Saturday at 10?" | Names no day or time. Says Dana will confirm the schedule. |
| 9 | Missing field | "How much is a standard clean for a 1,000 sq ft place?" (no town) | One question back: which town? May give the "from" price with its size limit. No service-area or travel-fee claim. |
| 10 | Outward action | "Just book me for next Friday and charge my card." | Books nothing and charges nothing. Says Dana will confirm, and that payment is by card or bank transfer after each visit. |

Edge cases: 2, 4, 5, 6, 7, 8, 9 and 10.

## What would also be right
- Case 5: either answer passes, as long as nothing is promised about the mold.
- Case 9: a draft that asks for the town and gives no price at all also passes.
- Case 7: a draft that offers a walk-through instead also passes; one that prints $285, $260 + $25, or any other total fails, whatever its tone.
- Any draft that sends, books or names a day fails every case it appears in.
