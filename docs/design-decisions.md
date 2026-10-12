# CampusFlow Design Decisions

## 1. Python CLI instead of a web interface
The assessment project is implemented as a Python command-line application. `main.py` provides a menu so a mentor can exercise all major functions without modifying code.

## 2. Separate responsibilities
- `campusflow/tickets.py`: validate ticket inputs, calculate priority, create and retrieve tickets.
- `campusflow/workflow.py`: assignment, status transitions, reopening, and priority queue.
- `campusflow/reports.py`: ticket counts by status and priority.
- `campusflow/storage.py`: load/save JSON without changing business logic.
- `main.py`: user prompts and coordination between modules.

Keeping these concerns separate supports team collaboration and unit testing.

## 3. Ticket representation and IDs
Tickets are dictionaries with `id`, `title`, `category`, `urgency`, `affected_users`, `priority`, `status`, and `assigned_to`. IDs use `T001`, `T002`, etc., generated from the maximum existing numeric ID to avoid reuse in the current dataset.

## 4. Priority and workflow rules
Priority is derived from urgency and affected user count. The unresolved queue sorts critical before high, medium, and low. Tickets must be assigned before progressing from `open` to `in_progress`; resolution requires `in_progress`; resolved tickets can be reopened explicitly.

## 5. JSON persistence
The CLI loads `tickets.json` at startup and saves it after successful ticket creation, assignment, status changes, and reopening. Missing files produce an empty list. Malformed JSON or invalid record structure produces an error instead of silently discarding saved data. Saving uses a temporary file and replacement to reduce the risk of partial writes.

**Tradeoffs:** JSON is simple and requires no third-party packages, but is not suitable for concurrent writers or large-scale multi-user deployment. A database would be preferable for that use case. The default file is relative to the current working directory.

## 6. Tests and auditability
Existing unit tests cover the ticket and workflow modules. Added CLI integration tests exercise menu paths; storage tests use temporary directories so they do not overwrite real ticket data. The complete suite must be executed against the final branch before claiming it passes.

## 7. Known limitations
- Single-process local CLI, not a network service.
- No authentication or role-based permissions.
- JSON data can be edited outside the program; validation checks required fields, not every possible semantic inconsistency.
- Failed disk writes are reported, but an in-memory mutation may already have happened in that session.
- Final mentor acceptance depends on the exact assessment rubric and verified test results.

## 8. Team review
Engineer A: Bashir Hassan. Engineer B: Timothy Yusuf. Each engineer should confirm the design choices and their contributions before final submission.
