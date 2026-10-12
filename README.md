# CampusFlow

CampusFlow is a Python 3 command-line application for managing campus support tickets. It supports ticket creation, validation, assignment, workflow management, priority queues, and summary reports.

## Team

- **Engineer A:** Bashir Hassan — ticket creation, validation, priority calculation, IDs, listing and viewing.
- **Engineer B:** Timothy Yusuf — ticket assignment, status transitions, reopening, queue and reporting.

## Requirements

Python 3 (standard library only). Run commands from the repository root.

## Run the interactive application

```bash
python3 main.py
```

Choose a menu number:

1. Create Ticket
2. List Tickets
3. View Ticket
4. Assign Ticket
5. Update Status
6. Reopen Ticket
7. Ticket Queue
8. Generate Report
9. Exit

Example workflow:

1. Choose **1**, enter a title, category (`Network`, `Hardware`, `Software`, `Other`), urgency (`low`, `medium`, `high`), and a positive integer for affected users. The application prints the new ticket ID, such as `T001`.
2. Choose **2** to list tickets or **3** to view a ticket by ID.
3. Choose **4** to assign `T001` to a staff member.
4. Choose **5** and set status to `in_progress`, then choose **5** again to set it to `resolved`.
5. Choose **6** to reopen a resolved ticket.
6. Choose **7** to see unresolved tickets sorted by priority.
7. Choose **8** to see ticket totals grouped by status and priority.

The workflow requires assignment before an open ticket can move to `in_progress`. Tickets must be `in_progress` before they can be resolved. A resolved ticket must be reopened explicitly.

## Ticket fields

Each ticket includes `id`, `title`, `category`, `urgency`, `affected_users`, `priority`, `status`, and `assigned_to`.

Priority is calculated from urgency and affected users: `critical`, `high`, `medium`, or `low`.

## Automated tests

```bash
python3 -m unittest discover -s tests -v
```

The tests cover ticket validation and creation, workflow management, reports, and interactive menu actions. Always run the suite again after making changes.

## Project structure

- `main.py` — interactive CLI entry point
- `campusflow/tickets.py` — ticket creation, validation and lookup
- `campusflow/workflow.py` — assignment, status transitions and queue
- `campusflow/reports.py` — summary reporting
- `tests/` — automated unit and CLI tests
- `docs/` — supporting project documentation

## Important limitation

Tickets are stored **in memory** during the CLI session. They are lost when the program exits. Persistent file or database storage is **not implemented** in this version; do not assume tickets survive a restart.

## Collaboration and review

The team used feature branches, pull requests, code reviews and automated tests. The final audited commit should be taken from the `main` branch **after** all reviewed changes are merged:

```bash
git switch main
git pull origin main
git rev-parse HEAD
```
