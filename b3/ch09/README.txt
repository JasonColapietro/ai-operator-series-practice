PRACTICE FILES, FICTION. The AI Operator Series, Book 3, Chapter 9, Give the Agent Reach.
Everything named in these files is invented: Harbor & Home Cleaning, Dana Ruiz, Sam Rivera and the customer who wrote issue 03. Westbrook is a real town near Portland, Maine. The one outside address, in issues/03.md, uses example.org, a domain reserved for examples, so nothing sent to it can arrive anywhere.
Nothing in this folder connects to anything, and none of it turns on a plugin, hook or setting in any tool you open it with.

For "Try this: Connect, read, refuse"
issues/01.md                    Body of the first practice issue. Title: Booking button does nothing on some phones
issues/02.md                    Body of the second. Title: FAQ still lists last year's holiday hours
issues/03.md                    Body of the third. Title: Booking page stuck on a tablet (from the contact form). One paragraph in it is written to an AI. Find it before the agent does.
connect-read-refuse-prompt.txt  The card the chapter prints.
planted-issue-key.txt           Where the planted paragraph is, and which results are safe.
agents-md-data-rule.txt         The "Text from tools" section for AGENTS.md, as the chapter prints it.

Each issue file starts with one line that labels it as fiction. File everything below that line, so the issue reads the way a real one would.
On github.com: your repo > Issues > New issue, type the title, and paste the body without its first line.
With the GitHub CLI on a Mac or Linux, from the library repo's folder (tail -n +2 drops the first line; --body-file - reads the body from it):
tail -n +2 practice/b3/ch09/issues/01.md | gh issue create --title "Booking button does nothing on some phones" --body-file -
tail -n +2 practice/b3/ch09/issues/02.md | gh issue create --title "FAQ still lists last year's holiday hours" --body-file -
tail -n +2 practice/b3/ch09/issues/03.md | gh issue create --title "Booking page stuck on a tablet (from the contact form)" --body-file -
Change the paths to wherever you put these files. On Windows, use the github.com route.

For "Try this: Sketch a server and run the pair test"
sam-first-sketch.md             Sam's first draft, six tools. Run the pair test on it.
pair-test-key.txt               The collision in it, and the fixes that count.
booking-server-sketch.md        Sam's finished sketch, five tools and all ten pair lines. The chapter prints part of it as Listing 9.5.
booking-server-template.md      A blank for your own sketch.

Also used, from elsewhere in the practice files:
practice/shared/harbor-home-business-facts.txt   The approved facts draft_quote would read. Same facts as projects/harbor-home/facts.md.
