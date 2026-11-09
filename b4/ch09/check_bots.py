# PRACTICE FILE. The AI Operator Series, Book 4, Chapter 9, Set Your Terms Once.
# Any business or person named in this folder is fiction.
#
# check_bots.py: read a robots.txt and print what it tells each crawler.
# Uses Python's standard library only. Nothing to install.
#
#   python3 check_bots.py harbor-home-robots-inherited.txt
#   python3 check_bots.py https://yourdomain.com/robots.txt
#   python3 check_bots.py https://yourdomain.com/robots.txt /services/
#
# The first argument is a file on disk or a web address. The optional second
# argument is the page to test (default: the home page, /).
#
# What it can and can't tell you:
#   It reads the file the way a crawler that follows robots.txt is asked to.
#   It can't tell you whether a crawler obeys the file, or whether a firewall
#   or bot protection turns a crawler away before it reads anything.
#   If the file can't be fetched, every bot is "unverified", never "allowed".
#   The one exception is "not found" (HTTP 404 or 410): the site has no
#   robots.txt, the standard treats that as no rules, and every bot is allowed.
#   Web addresses follow redirects, the way crawlers do.
#   Python's parser uses the first rule that matches a page; the standard
#   (RFC 9309) uses the longest. For files with one Allow or Disallow per
#   group, like the ones in this chapter, the two agree.

import sys
import urllib.error
import urllib.request
import urllib.robotparser

# Names as of November 2026. Check each company's crawler page before relying on them.
BOTS = [
    ("OAI-SearchBot", "OpenAI, search"),
    ("ChatGPT-User", "OpenAI, when a person asks"),
    ("GPTBot", "OpenAI, training"),
    ("Claude-SearchBot", "Anthropic, search"),
    ("Claude-User", "Anthropic, when a person asks"),
    ("ClaudeBot", "Anthropic, training"),
    ("PerplexityBot", "Perplexity, search"),
    ("Perplexity-User", "Perplexity, when a person asks"),
    ("Googlebot", "Google, Search incl. AI Overviews and AI Mode"),
    ("Google-Extended", "Google, Gemini training and grounding (a token)"),
    ("Bingbot", "Microsoft, Bing and Copilot"),
    ("CCBot", "Common Crawl, public archive"),
    ("SomeOtherBot", "any crawler the file doesn't name"),
]


def read_source(source):
    """Return (text, problem). problem is None when the file was read."""
    if source.startswith(("http://", "https://")):
        request = urllib.request.Request(source, headers={"User-Agent": "check_bots.py (practice)"})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.read().decode("utf-8", errors="replace"), None
        except urllib.error.HTTPError as error:
            if error.code in (404, 410):
                # No robots.txt at all. RFC 9309 treats a missing file as no rules.
                return "", None
            return None, f"the server answered HTTP {error.code}"
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            return None, f"the fetch failed ({error})"
    try:
        with open(source, encoding="utf-8") as handle:
            return handle.read(), None
    except OSError as error:
        return None, f"the file couldn't be opened ({error})"


def main():
    if len(sys.argv) < 2:
        print("usage: python3 check_bots.py <robots.txt file or URL> [page path]")
        return 2
    source = sys.argv[1]
    page = sys.argv[2] if len(sys.argv) > 2 else "/"
    text, problem = read_source(source)
    print(f"robots.txt: {source}")
    print(f"page tested: {page}")
    print()
    if problem:
        for name, role in BOTS:
            print(f"  {name:<17} unverified   {role}")
        print()
        print(f"Unverified because {problem}. Open the address in a browser and look.")
        return 1
    parser = urllib.robotparser.RobotFileParser()
    parser.parse(text.splitlines())
    for name, role in BOTS:
        status = "allowed" if parser.can_fetch(name, page) else "blocked"
        print(f"  {name:<17} {status:<12} {role}")
    print()
    if not text.strip():
        print("No rules found (the file is empty, or the site has none), so nothing restricts any bot.")
    print("Allowed or blocked describes what the file asks. It doesn't show what a crawler does.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
