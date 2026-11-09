<!-- PRACTICE FILE, FICTION. The AI Operator Series, Book 3, Chapter 9, Give the Agent Reach. Sam's finished sketch for a Harbor & Home booking server, as the chapter prints it in Listing 9.5 (the chapter prints the header and the tools table; this file also holds all ten pair lines). Harbor & Home Cleaning, Dana and Sam are invented. Nothing here is built; Appendix D builds it. -->
# Harbor & Home booking server: sketch

Job of the server: answer booking questions from approved facts
and the schedule. It drafts and holds. It never books, sends or
charges. Dana confirms every hold.

## Tools

| Tool | Use it when the request... | Reads | Writes |
|---|---|---|---|
| find_open_slots | asks when a crew can come, for a date or a range | schedule | nothing |
| get_customer_history | names a past customer and asks what they had | visit log | nothing |
| draft_quote | gives a service and a size and wants a price | facts.md | nothing |
| request_booking_hold | picks one slot and asks to keep it | schedule | a pending hold, 24 hours, Dana confirms |
| log_inquiry | is a booking question none of the others finishes | nothing | one line in the inquiry log |

Ask-gate: request_booking_hold and log_inquiry (they write).
Every call, by any tool, goes in the call log: date, tool,
inputs, result. The call log is where next month's tools come from.

## Pair test (from the request alone)

1. find_open_slots / get_customer_history: use A when the request is about the calendar ahead, B when it is about visits already done.
2. find_open_slots / draft_quote: use A when the request asks when, B when it asks how much.
3. find_open_slots / request_booking_hold: use A when no slot is chosen yet, B when the customer has named one slot.
4. find_open_slots / log_inquiry: use A when the request asks about dates, B when it asks about anything this server cannot finish.
5. get_customer_history / draft_quote: use A when the request names a past visit, B when it names a service and a size.
6. get_customer_history / request_booking_hold: use A when the request looks back, B when it reserves a future slot.
7. get_customer_history / log_inquiry: use A when the customer is on file and asks about the past, B for a question no tool answers.
8. draft_quote / request_booking_hold: use A when the request wants a price, B when it wants a slot kept.
9. draft_quote / log_inquiry: use A when service and size are given, B when the question is outside the price list (an office walk-through, a service we do not offer).
10. request_booking_hold / log_inquiry: use A when one slot is named, B when no tool can act on the request.

All ten pairs separate. No collisions.
