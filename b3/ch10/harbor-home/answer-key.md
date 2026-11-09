# Answer key: deposits, Monday March 29 to Friday April 9, 2027

Practice file, fiction. The AI Operator Series, Book 3, Chapter 10. Harbor & Home Cleaning, Dana Ruiz, Sam Rivera and every client, invoice and amount are invented. Worked from the three files in this folder and Sana Haddad's email of March 31; the totals were added by script.

## Files
- bank-first-2027-03-29.csv: 10 deposits. Card settlements are month first (03/29/2027), transfers year first (2027-03-31).
- bank-second-2027-03-29.csv: 3 deposits. Dates are day first, so 01/04/2027 is April 1, and the amount column is "Amount (USD)".
- invoices-2027-03-29.csv: 12 open invoices. INV-2048 and INV-2050 carry over from the week of March 15.
- Deposits total $1,982.50. Invoices total $1,982.50.

## Which deposit pays which invoice
| Invoice | Client | Amount | Paid by |
|---|---|---|---|
| INV-2048 | Brooks, D. | $190.00 | first bank, 2027-03-29, $190.00 |
| INV-2050 | Haddad, S. | $260.00 | in two parts: first bank, 2027-03-31, $140.00, and second bank, 2027-04-01, $120.00 |
| INV-2061 | Alvarez, M. | $126.00 | first bank, 2027-03-29 |
| INV-2062 | Chen, L. | $148.50 | first bank, 2027-03-30 |
| INV-2063 | Haddad, S. | $140.00 | first bank, 2027-04-05, $140.00 |
| INV-2064 | Okonjo, F. | $175.00 | first bank, 2027-03-31 |
| INV-2065 | Nguyen, T. | $260.00 | second bank, 2027-04-02 |
| INV-2066 | Sullivan, K. | $126.00 | first bank, 2027-04-02 |
| INV-2067 | Alvarez, M. | $126.00 | first bank, 2027-04-05 |
| INV-2068 | Patel, R. | $165.00 | first bank, 2027-04-06 |
| INV-2069 | Becker, W. | $140.00 | second bank, 2027-04-07 |
| INV-2070 | Sullivan, K. | $126.00 | first bank, 2027-04-09 |

## The planted case
Sana Haddad has two open invoices: the deep clean from March 19 (INV-2050, $260.00) and a standard clean on March 30 (INV-2063, $140.00). She paid the deep clean in two parts on either side of the month end, $140.00 on March 31 and $120.00 on April 1, and paid the standard clean on April 5. Her email of March 31 says so.

The bank files alone can't settle this. The March 31 deposit has the same name and amount as INV-2063, so a checker that takes the first invoice that fits will match it there and then pair April 1 with April 5 for the deep clean. Every deposit matches and the totals agree, yet two of the three Haddad matches are wrong. In a March-only run, the same checker marks INV-2063 paid and lists INV-2050 as having no deposit, so Dana's month-end list would ask Ms. Haddad for $260.00 she has started to pay.

A right answer either matches the Haddad deposits as in the table above, using the email, or lists all three under "For Dana" because one client has two open invoices the deposits could pay. Both count.

## Everything else
Every other deposit pays exactly one invoice with the same name and amount. No deposit is left over and no invoice is left unpaid at the end of the two weeks.
