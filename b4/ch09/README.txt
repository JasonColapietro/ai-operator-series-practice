PRACTICE FILES, FICTION. The AI Operator Series, Book 4, Chapter 9, Set Your Terms Once.
Harbor & Home Cleaning, Dana Ruiz, Sam Rivera and everything about them in this folder are invented,
and so are the website, its address (harborhome.example.com), its photo gallery and its February
rebuild. Nothing here turns on a plugin, hook or setting in any tool.

For "Try this: Decide, then license your library"
sam-library-inventory.txt      What Sam's library repo holds, folder by folder, and where each part came from.
sam-LICENSE.txt                Listing 9.1, Sam's library/LICENSE, the same text the chapter prints.
terms-template.md              The blank terms.md from "Save this".

For "Try this: Publish your terms and check the bots"
harbor-home-site-notes.txt         What's on Harbor & Home's site, and Dana's answers to the five kinds of use.
harbor-home-robots-inherited.txt   The robots.txt Sam found (the staging template that went live).
harbor-home-robots-first-fix.txt   Sam's first fix, with the planted mistake from the Sam's step.
harbor-home-robots-final.txt       The file after Dana decided. Read it after you write your own.
harbor-home-terms-page.txt         The terms page the chapter prints, as a model.
robots-check-prompt.txt            The prompt card.
check_bots.py                      Reads a robots.txt (file or web address) and prints each bot's status.
                                   Python standard library only:  python3 check_bots.py harbor-home-robots-inherited.txt
answer-key.txt                     Every result the "It worked if" lines accept.

What check_bots.py should print for the three files (checked 2026-11-06 with Python 3.14):
  inherited    every bot blocked
  first fix    the five search crawlers allowed; GPTBot, ClaudeBot, CCBot, Google-Extended blocked;
               ChatGPT-User, Claude-User, Perplexity-User and SomeOtherBot blocked by the old * group
  final        only GPTBot, ClaudeBot and CCBot blocked; everything else allowed, Google-Extended included

Given a web address, check_bots.py follows redirects the way crawlers do. If the site answers "not found"
(HTTP 404 or 410), it has no robots.txt, and every bot comes out allowed. Any other failure prints
"unverified" for every bot (rechecked 2026-11-07 against a local test server).

Bot names are as of November 2026. Check each company's crawler page before you copy a name.
