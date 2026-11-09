<!-- PRACTICE FILE, FICTION LABEL: The AI Operator Series, Book 5, Chapter 12. The first entry in clients/harbor-home/incidents.md, in Book 3's entry shape (date, what happened, rule, where the rule lives). Sam and Harbor & Home are invented. -->
# Incidents: Harbor & Home

## Build day, before week 1: the price check passed a broken copy
What happened: the playbook's price check, written for the FAQ page, was still pointed at faq.md alone. Run on a copy with a planted $300 price in a quote draft, it printed PASS. Nothing reached Dana or a customer.
Rule: every check reads the whole delivery folder, and a check that reads no files stops with "CANNOT CHECK". Every check must fail a planted copy before it is trusted.
Lives in: playbooks/staffing-quote-desk/checks/check_delivery.py; AGENTS.md, "Before you report done".
