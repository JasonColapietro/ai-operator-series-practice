PRACTICE FILES, FICTION. The AI Operator Series, Book 2, Chapter 14, On a Schedule, Under Review.
Everything named in these files is invented: Harbor & Home Cleaning, Dana Ruiz, Sam Rivera, the crews, every client and business, and every address, date, price and booking. The prices and rules exist so you can check a summary against them, not to quote.
Files marked "copied unchanged" come from the Claude AI Made Practical practice pack. Text files carry a short header and a line of dashes above the words they hold. The CSV files carry no header, because a header row would change the rows the lessons count; this README is their fiction label.

For "Try this: A Monday that stops on stale input"
week-schedule-feb-8-12.csv     Harbor & Home's bookings for Monday, February 8 to Friday, February 12, 2027. 26 jobs. Fiction. Made from the pack's wf24-input-week-schedule.csv: every date moved 14 weeks later (dates inside the notes too), every job ID moved up by 341, and one client renamed. Nothing else changed, so the pack's planted problems are all still there.
week-schedule-feb-1-5.csv      The week before, February 1 to 5, 2027. 17 jobs. The stale file. Made the same way from the pack's wf24-input-stale-schedule.csv.
monday-summary-task.txt        Listing 14.1, the scheduled task, filled in for the practice route.
test-run-line.txt              The line that sets the run date for a test, so the freshness check sees Monday, February 8, 2027.
monday-summary-key.txt         What a correct run gets right on each file and on each run date. Computed by script from the two CSV files; it matches the pack's answer key with the new dates and IDs.
Also used: practice/shared/harbor-home-business-facts.txt, or your library/projects/harbor-home/facts.md from chapter 4. The task reads it as facts.md from the same folder as the schedule file.

Run dates: with the freshness check in place, a run gives the full summary of the February 8 to 12 file only when its run date is Monday, February 8, 2027, or a day from February 2 to 7. On every other date both files get the one-line reply, which is the check working. Use the test line to choose the date.

For "Try this: Your first thirty-minute review"
harbor-home-jobs-oct-5-9.csv   Harbor & Home's jobs export for Monday, October 5 to Friday, October 9, 2026. 28 rows. Fiction. Copied unchanged (the pack calls it wf23-input-jobs-oct5-9.csv). It is the week before chapter 3's practice week, chosen because its numbers are already known.
dana-notes-oct-5-9.txt         Dana's notes for that week, with her "ideas / someday" list. Copied unchanged below the header.
weekly-review-sep-28-oct-2.txt The review Dana wrote for the week before. It goes in the Project's files as last week's review. Copied unchanged below the header.
weekly-review-prompt.txt       Listing 14.3, the weekly review request. Copied from the pack with one change: the third slot names weekly-review-sep-28-oct-2.txt.
weekly-review-repair.txt       The repair for a review whose numbers don't match the export. Copied unchanged.
weekly-review-key.txt          What a correct review gets right. Numbers recomputed by script; they match the pack's key. Its price-check paragraph accepts both readings of the $25 size step.

For "Save this"
monday-summary-template.txt    The layout for library/schedules/monday-summary.md. Matches the chapter's listing word for word below its header.
weekly-review-template.txt     The layout for library/reviews/weekly-YYYY-MM-DD.md.

Nothing here turns on a plugin, hook or setting in any tool you open it with.
