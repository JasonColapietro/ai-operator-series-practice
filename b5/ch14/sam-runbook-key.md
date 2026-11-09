<!-- PRACTICE FILE, FICTION LABEL: The AI Operator Series, Book 5, Chapter 14. What a cold read of sam-runbook-first-draft.md should find, and Sam's repaired runbook. Answer key for the practice route. Sam, Dana and Harbor & Home are invented. -->
# What the cold read should find

At least these, in any order and any wording:
1. "Watches the inbox": which inbox, and from when to when?
2. "The facts are in the usual place": where, and what is the file called?
3. "The usual Friday check": what is it, and what counts as a pass?
4. "Make sure the drafts look right": right against what?
5. "Text Sam": what if Sam doesn't answer, and what may the reader do meanwhile?
6. "Turn it off": turn what off, where, and who may?
7. "Rerun the tests": which tests, where are they, and what is a pass?
8. "Who to call: Sam": nobody who works at Harbor & Home is named.

A read that also asks who approves a change to the facts file is right. A read that asks for a password is a sign the runbook is fine there and the reader went too far: passwords never go in a runbook.

# The repaired runbook (Sam's second version)

## Runbook: weekend quote desk for Harbor & Home Cleaning
Last changed: day 33 · Changed by: Sam · Owner of this runbook: Dana Ruiz

### 1. What runs, and when
From 5 p.m. Friday to 8 a.m. Monday, the agent reads each new message in the hello@ inbox (the web form's copies land there too). For each quote request it writes a draft reply and a three-line summary, and sends Dana a one-line alert. It never sends, books, names a day or time, offers a discount or takes a payment.

### 2. Where it lives
- The hello@ inbox: Harbor & Home's email account, in Dana's name.
- The agent: Harbor & Home's agent account, in Dana's name, billed to Harbor & Home. The schedule is named "Weekend quote desk".
- The facts: harbor-home-business-facts.txt in the "Front office" folder of Dana's shared drive. Dana approves every change.
- The ten cases, this runbook and incidents.md: the same "Front office" folder, under "Weekend quote desk".
- Logins: in Dana's password manager. Never in this file.

### 3. The checks
1. Friday, soon after 5 p.m., when the desk switches on: Dana sends a test request from her own phone. Pass: a draft and an alert within ten minutes, and nothing sent.
2. Monday 8 a.m.: count the weekend's requests and drafts. Pass: every request has a draft or a held note.
3. Every draft, before sending: every price in it appears in the facts file with its size limit. Pass: yes for every price.
4. After any change to the facts file or the agent's instructions: run the ten cases. Pass: ten of ten.

### 4. When a check fails
1. No draft within ten minutes: check that the "Weekend quote desk" schedule is on. If it is on, pause it (section 5), answer the weekend by hand, and log it in incidents.md (in the same "Weekend quote desk" folder).
2. A request with no draft: answer it by hand on Monday and add the request (with the customer's details removed) as a new case.
3. A price not in the facts file: do not send. Delete that line, or reply by hand. Log it in incidents.md the same day.
4. Fewer than ten cases pass: do not use the change. Put the last version back, rerun, and log it.

### 5. How to stop it
Turn off the "Weekend quote desk" schedule in Harbor & Home's agent account. Dana or anyone she names may do it, any time, with no reason needed. Nothing else stops working when it is off.

### 6. How to change a rule
Change the facts file first (Dana approves). Then run the ten cases. If a case's expected result changes because a fact changed, Dana approves the new expected result before the run.

### 7. Who to call
1. Dana decides everything about customers, prices and whether the desk runs.
2. Sam, for anything inside the agent. If Sam doesn't answer by Monday 8 a.m., pause the desk and answer by hand.

### 8. Change log
Day 33: runbook rewritten after a cold read stalled eight times. All ten cases rerun: ten of ten.

# What would also be right
- A runbook that names a different person as backup is right if that person is someone at Harbor & Home or someone Dana chose.
- A runbook that leaves out check 2 is still usable; one that leaves out check 3 is not, because a wrong price is the costliest thing the desk can do.
- A runbook that contains any password, door code or customer's details is wrong, however complete it is otherwise.
