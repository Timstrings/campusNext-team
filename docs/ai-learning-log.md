# AI Learning and Verification Log

## Purpose
This document records how AI assistance was used in the CampusFlow project, how suggestions were verified, and what the team learned. It distinguishes recorded work from checks still requiring human confirmation.

## Recorded AI-assisted activities

| Activity | AI assistance | Human verification or evidence | Learning |
|---|---|---|---|
| Understanding the assessment | Explained the division of ticket creation, workflow, tests, documentation, and audit requirements in Hausa | Team divided work between Engineer A (Bashir Hassan) and Engineer B (Timothy Yusuf); individual authorship and review should be verified in Git history | Translate requirements into independently testable tasks |
| Ticket management | Explained validation, priority calculation, ticket IDs, and expected outputs | Ticket creation, listing, and lookup were manually exercised in the CLI with ticket `T001` | Validate inputs before creating ticket dictionaries |
| Workflow | Explained assignment, `open` → `in_progress` → `resolved`, reopening, and queue behavior | CLI manually demonstrated assignment to Timothy, status changes, empty resolved queue, and reopening | Enforce allowed status transitions |
| Interactive audit fix | Suggested and wrote an interactive CLI to replace the demonstration-only `main.py` | User manually ran menu choices 1, 2, 3, 4, 5, 6, 7, 8 and shared successful outputs in chat | A library of functions is not the same as a usable CLI |
| Error handling | Helped interpret a nonexistent ticket ID error (`T0001` instead of `T001`) | CLI displayed an error and returned to the menu without crashing | Reject invalid IDs gracefully |
| JSON persistence | Suggested `json.load`/`json.dump`, startup loading, saving after changes, and isolated storage tests | Added code and tests in the audit branch; **automated execution and restart verification are still pending** | Persist state separately from business logic |
| Documentation | Helped clarify README instructions, limitations, and design decisions | Documentation changes are visible in the pull request; **team review is pending** | Documentation must match implemented behavior |

## Example: AI suggestion and verification

**Problem:** The mentor's manual audit could not exercise features because `python3 main.py` printed a demo ticket instead of offering a menu.

**Suggestion:** Provide a numbered interactive CLI for creating, listing, viewing, assigning, updating, reopening, queueing, and reporting tickets.

**Verification:** The user ran the CLI and shared successful output for creating ticket `T001`, assigning it to Timothy, moving it to `in_progress` and `resolved`, excluding it from the unresolved queue, reopening it, and generating a report showing one open critical ticket.

**Limitation:** This manual walkthrough does not prove that every invalid input, storage failure, or automated test passes. Run the complete suite before final submission.

## Verification checklist for the team

- [x] Manual interactive creation/list/view/assign/status/queue/reopen/report walkthrough shared
- [ ] Run `python3 -m unittest discover -s tests -v` against the latest audit branch and record the actual result
- [ ] Restart `python3 main.py` and verify tickets persist in `tickets.json`
- [ ] Review Git commits and PRs to confirm each member's actual code and tests
- [ ] Have both team members read and approve this log
- [ ] Record the final tested commit SHA and merge details

## Integrity note

This is a draft assembled from the recorded AI-assisted work and user-shared manual outputs. It does **not** claim that every team member performed each activity or that unrun tests passed. Add each engineer's own reflections and exact evidence before submitting.
