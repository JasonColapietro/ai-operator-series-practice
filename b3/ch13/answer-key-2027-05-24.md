<!-- PRACTICE FILE, FICTION. The AI Operator Series, Book 3, Chapter 13, The Crew. Harbor & Home Cleaning, Dana Ruiz and Sam Rivera are invented. Computed by running Sam's checker (practice/b3/ch10/sam/scripts/reconcile.py) on this folder's three files with python3 -I on 2026-11-06. -->
# Answer key: the Monday report for May 24, 2027

Files: harbor-home/incoming/bank-first-2027-05-24.csv,
harbor-home/incoming/bank-second-2027-05-24.csv (dates written day
first) and harbor-home/invoices-2027-05-24.csv.
Deposits cover Monday, May 17 to Friday, May 21, 2027.

## Totals a correct report shows
- Deposits total: $1,644.50 (nine deposits, two banks)
- Invoices matched: 7 (using 8 of the 9 deposits)
- Deposits with no match: 1
- Invoices with no deposit yet: 1 (the checker's last line may call it
  open or still open)

## Lines a correct report names
- Paid in two parts: INV-2130, Haddad S., $150.00 on May 19 and
  $145.00 on May 21 ($295.00, a deep clean plus inside fridge).
- No match: Lindqvist R., $165.00 on May 21. No invoice this week
  carries that amount for that client. It is most likely INV-2118
  ($165.00, dated May 14) from last week's list, which this run did
  not read. Dana confirms; the report must not mark it paid.
- No deposit yet: INV-2132, Moreau J., $140.00, dated May 20.

## Signs the report used last week's run
- Deposits total $1,021.00, or 6 invoices matched.
- Any of Kowalski, Sato or Ferreira.
- No deposit with no match.
- The first line of checker-output.txt names 2027-05-17.

## What the verifier may accept
- Totals written as $1644.50 or $1,644.50.
- Names written as the bank prints them (LINDQVIST R) or as the
  invoices do (Lindqvist, R.).
- The open invoice called "no deposit yet", "open" or "still open".
- Any wording for the Lindqvist line, as long as it is left open
  for Dana and not counted as paid.
