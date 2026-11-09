<!-- Practice file, fiction label in README.txt. Copy to library/backups.md and delete this line. -->
# Backups

What gets copied: all of library/, including exports/ and the dated bundles in it.
Never in this file: passwords, keys or recovery codes. Write where each one lives instead.
Client data in these copies: see data/register.md, which lists both backups on every row they hold.

## Backup 1 (here)
Where: 
Encrypted with: 
Password lives in: 
Last copied: YYYY-MM-DD

## Backup 2 (off premises)
Where: 
Encrypted with: 
Password lives in: 
Who else can reach it: 
Last copied: YYYY-MM-DD

## Restore tests
One file from each backup, restored into a scratch folder and opened. For a bundle: git bundle verify, then git clone into the scratch folder and open one file.

| Date | Backup | File restored | Opened in | Result |
|---|---|---|---|---|
| | | | | |

## The monthly sweep
1. Request every account export on the register's Locations list.
2. Commit, then make and verify a dated bundle of each repo.
3. Download the exports within 24 hours into exports/YYYY-MM-DD/.
4. Copy library/ to both backups.
5. Restore one file from each and log it above.
