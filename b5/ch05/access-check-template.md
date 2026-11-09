<!-- Practice file. The AI Operator Series, Book 5, Chapter 5. A blank for library/playbooks/visibility/access-check.md. Bot names as of November 2026; check each vendor's crawler page before you rely on one. -->
# Access check: [SITE]

Checked: [DATE]. Money pages checked: [URL PATHS].

## The rules file

| Bot | Role | Group it follows | Status | Reason |
|---|---|---|---|---|
| OAI-SearchBot | search | | | |
| ChatGPT-User | fetches for a person | | | |
| GPTBot | training | | | |
| Claude-SearchBot | search | | | |
| Claude-User | fetches for a person | | | |
| ClaudeBot | training | | | |
| PerplexityBot | search | | | |
| Perplexity-User | fetches for a person | | | |
| Googlebot | search (and Google's AI answers) | | | |
| Google-Extended | training token | | | |
| Bingbot | search (and Copilot) | | | |
| CCBot | public archive | | | |

Status is one of: allowed, blocked, unverified. Blocked on purpose? Say so, and name the decision (Book 4, chapter 9).

## What the bot receives

- Firewall or CDN bot protection: [setting name and state, or "unverified" and why]
- Raw source of [MONEY PAGE]: searched for "[A SENTENCE FROM THE PAGE]". Found / not found.
- Facts that live only in images or appear only after a click: [list]

## Discovery

- Sitemap listed in robots.txt: yes / no
- Money pages in the sitemap: [list what's missing]
- Stray noindex: [pages]
- Canonical points to: [URL, for each money page]

## Changes to make

1. [change] (who approves it: [name])
