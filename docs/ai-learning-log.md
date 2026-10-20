# AI Learning and Verification Log

## Current project: CampusFlow Next

| Role | Full name |
|---|---|
| Engineer A | Timothy Yusuf |
| Engineer B | Fredrick Ogbodo |

## Project history

The original CampusFlow project was developed by:

- Engineer A — Bashir Hassan.
- Engineer B — Timothy Yusuf.

For the current CampusFlow Next project, Timothy Yusuf works as
Engineer A and Fredrick Ogbodo works as Engineer B.

These are separate team arrangements. Original contributions should remain
accurately credited in the project history. Current roles do not change
the authorship of earlier work.

## Purpose

This document records how AI assistance supported development,
troubleshooting, documentation, and learning in CampusFlow Next.

It distinguishes between:

- Work and results recorded in the development conversation.
- Contributions reported by the team.
- Checks still requiring confirmation against the submitted revision.

AI-generated suggestions are not treated as verified simply because they
were provided. The engineers remain responsible for understanding,
reviewing, and testing the changes they use.

## Current responsibilities and contributions

### Engineer A — Timothy Yusuf

Current project focus: ticket validation, structured notes, workflow
reliability, and JSON storage.

The development conversation records work concerning:

- Validation of ticket information and note inputs.
- Structured follow-up notes and note IDs.
- Assignment and ticket-status rules.
- Reopening resolved tickets.
- Safe loading and saving of ticket data.
- Duplicate ticket and note ID checks.
- Ticket and note ID continuity after reloading.
- Tests for validation, notes, workflow, and storage.

Exact authorship and the extent of each contribution should be supported
by the relevant commits, pull requests, and Timothy's own explanation.

### Engineer B — Fredrick Ogbodo

The team reports that Fredrick worked on:

- `main.py` and the interactive command-line interface.
- `campusflow/search.py` for ticket search and filtering.
- `campusflow/reports.py` for ticket summaries.
- `campusflow/understanding_check.py` for the Engineering Understanding
  Check.
- The Add Follow-up Note menu integration.
- The View Ticket Notes menu integration.

The note-menu work concerns prompts, calls to note functions, and display
of results. It does not by itself establish authorship of the underlying
note-validation or storage implementation.

Supporting commits, pull requests, tests, and Fredrick's own explanation
should be added before submission.

## Recorded AI-assisted learning activities

| Activity | AI assistance | Recorded verification or limitation | Learning |
|---|---|---|---|
| Understanding project requirements | Helped explain responsibilities, testing expectations, documentation, and audit requirements | The current team arrangement has been clarified as Timothy Yusuf — Engineer A and Fredrick Ogbodo — Engineer B | Separate current responsibilities from original project history |
| Ticket validation and structured notes | Explained validation rules, note IDs, rejected actions, and expected behaviour | Earlier shared test output included passing validation and note tests; results must be rechecked against the submitted revision | Validate input before changing application state |
| Workflow troubleshooting | Helped interpret the message “Only resolved tickets can be reopened” | Shared CLI output showed that requests using `OPEn` and `OPEN` reached the reopening rule and were rejected | Input normalisation and permitted workflow transitions are separate concerns |
| Search troubleshooting | Explained title searches, optional filters, and the sorting prompt | Shared CLI output showed searches returning “No matching tickets”; the actual ticket title and status were not supplied, so a search defect was not confirmed | Check actual data and active filters before diagnosing a defect |
| Status input normalisation | Suggested using `.strip().lower()` when reading a new status | The supplied `main.py` contains this input-normalisation code; a fresh test result for the final revision is still required | Normalise input at the interface without bypassing workflow rules |
| Lowercase status display | Suggested using `ticket['status'].lower()` in `show_ticket()` | The code change was proposed; the final displayed output and test result were not supplied | Display formatting does not change stored values or search behaviour |
| JSON persistence | Discussed startup loading, saving after changes, and persistence tests | Earlier shared test output included passing save/reload and ID-continuity tests; manual restart verification for the final revision remains to be recorded | Persistence requires explicit verification, not just a successful in-memory operation |
| Documentation | Helped revise the README and learning log | Terminal output confirmed that `docs/ai-learning-log.md` and `docs/design-decisions.md` were tracked locally at the time checked | Documentation must distinguish reported work, verified evidence, and pending checks |

## Learning cycle 1: Workflow errors and status input

### Observation

The user entered `OPEn` and `OPEN` while changing the status of ticket
`T001`. The application returned:

    Error: Only resolved tickets can be reopened.

### AI explanation and suggestion

AI explained that converting text to lowercase does not change whether
a transition is allowed.

It suggested normalising the status input with:

    new_status = input(
        "New status (open/in_progress/resolved): "
    ).strip().lower()

### Recorded evidence

The supplied `main.py` contains this normalisation.

Its `open` branch calls `reopen_ticket()`. This explains why an `open`
request can still be rejected by the reopening rule.

The shared output did not establish the ticket's exact current status.

### Learning

Recognising the user's input and allowing the requested state transition
are different responsibilities.

A fix should address the observed cause rather than remove a valid
workflow restriction.

### Remaining verification

- Test uppercase and mixed-case status inputs.
- Confirm valid transitions still succeed.
- Confirm invalid transitions leave ticket state unchanged.
- Record the tested commit SHA and actual results.

## Learning cycle 2: Search filters and note text

### Observation

A follow-up note was added to `T001`. The user then searched using
network-related title text and received:

    No matching tickets.

The user also entered `T001` at the sorting question during one attempt.

### AI explanation

AI explained that:

- The search prompt asks for title text, not note text.
- Category, status, and priority restrict the search.
- The sorting prompt expects a yes/no response, not a ticket ID.
- A ticket's actual title and status should be checked before diagnosing
  the result.

### Recorded evidence

The supplied `search_view()` passes the entered title, category, status,
and priority to `search_tickets()`.

The sorting prompt checks whether its response is `y`.

The implementation of `search_tickets()` and the actual saved ticket
data were not supplied during this troubleshooting exchange, so the
cause of the missing match was not independently established.

### Learning

Search troubleshooting should begin with known data and a simple query.
Add filters one at a time and compare expected and actual results.

A “No matching tickets” message is not, by itself, proof of a defect.

### Remaining verification

- Create or identify a ticket with a known title and status.
- Search using a short part of that title with other filters blank.
- Add category, status, and priority filters individually.
- Record expected and actual results.
- Verify search does not mutate the ticket collection.

## Automated test evidence

An earlier user-shared terminal run reported:

    python3 -m unittest discover -s tests -v

    Ran 124 tests in 0.064s

    OK

This is evidence for the checkout used in that run.

The conversation did not associate that result with a full commit SHA.
It must not be presented as proof that every later revision passes.

### Final submitted revision

- Full commit SHA: To be recorded.
- Test command: `python3 -m unittest discover -s tests -v`
- Date run: To be recorded.
- Number of tests: To be recorded.
- Failures, errors, and skips: To be recorded.
- Actual result: To be recorded.

## Individual reflections

Each engineer should write or confirm their own reflection.

### Timothy Yusuf — Engineer A

- A specific problem I investigated:
- AI suggestion I accepted, modified, or rejected:
- How I checked the suggestion:
- What I learned:
- Supporting commit, PR, test, or manual evidence:

### Fredrick Ogbodo — Engineer B

- A specific problem I investigated:
- AI suggestion I accepted, modified, or rejected:
- How I checked the suggestion:
- What I learned:
- Supporting commit, PR, test, or manual evidence:

## Final verification checklist

- [x] Current team roles clarified.
- [x] Earlier terminal output showing 124 passing tests recorded.
- [x] Local tracking of the AI learning log and design-decisions document confirmed.
- [ ] Verify contribution statements against Git history and pull requests.
- [ ] Complete and confirm each engineer's individual reflection.
- [ ] Test the CLI against the exact submitted revision.
- [ ] Verify note entry and note viewing.
- [ ] Verify tickets and notes survive saving and restarting.
- [ ] Verify search using known ticket data.
- [ ] Verify status normalisation and permitted workflow transitions.
- [ ] Run the complete test suite against the submitted revision.
- [ ] Record the final tested commit SHA and test results.
- [ ] Record both engineers' actual PR links and review evidence.
- [ ] Have Timothy Yusuf review and approve this log.
- [ ] Have Fredrick Ogbodo review and approve this log.

## Integrity note

This log combines the team's clarification of roles, user-shared terminal
output, supplied code, and recorded AI-assisted troubleshooting.

It does not claim that both engineers performed every recorded action,
that suggested changes were always applied, or that later revisions
passed tests without a recorded run.

Preserve accurate credit for the original CampusFlow work by Bashir Hassan
and Timothy Yusuf. Record current CampusFlow Next contributions under
Timothy Yusuf — Engineer A and Fredrick Ogbodo — Engineer B, supported by
actual project evidence.