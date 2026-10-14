"""Persist CampusFlow tickets in a JSON file."""
import json
from pathlib import Path

DEFAULT_PATH = Path("tickets.json")

REQUIRED_FIELDS = {
    "id",
    "title",
    "category",
    "urgency",
    "affected_users",
    "priority",
    "status",
    "assigned_to",
}

VALID_CATEGORIES = {"Network", "Hardware", "Software", "Other"}
VALID_URGENCIES = {"low", "medium", "high"}
VALID_PRIORITIES = {"low", "medium", "high", "critical"}
VALID_STATUSES = {"open", "in_progress", "resolved"}

REQUIRED_NOTE_FIELDS = {"note_id", "author", "message"}


def validate_note(note, ticket_id):
    """Validate one follow-up note attached to a ticket."""
    if not isinstance(note, dict):
        raise ValueError(f"Ticket {ticket_id} has an invalid note.")

    if not REQUIRED_NOTE_FIELDS.issubset(note):
        raise ValueError(f"Ticket {ticket_id} has a note with missing fields.")

    if not isinstance(note["note_id"], str) or not note["note_id"].strip():
        raise ValueError(f"Ticket {ticket_id} has an invalid note ID.")

    if not isinstance(note["author"], str) or not note["author"].strip():
        raise ValueError(f"Ticket {ticket_id} has an invalid note author.")

    if not isinstance(note["message"], str) or not note["message"].strip():
        raise ValueError(f"Ticket {ticket_id} has an invalid note message.")


def validate_ticket_record(ticket):
    """Validate one decoded ticket record before it enters memory."""
    ticket_id = ticket.get("id", "unknown")

    if not isinstance(ticket_id, str) or not ticket_id.strip():
        raise ValueError("Ticket ID must be a non-empty string.")

    if not isinstance(ticket["title"], str) or not ticket["title"].strip():
        raise ValueError(f"Ticket {ticket_id} has an invalid title.")

    if ticket["category"] not in VALID_CATEGORIES:
        raise ValueError(f"Ticket {ticket_id} has an invalid category.")

    if ticket["urgency"] not in VALID_URGENCIES:
        raise ValueError(f"Ticket {ticket_id} has an invalid urgency.")

    affected_users = ticket["affected_users"]

    if isinstance(affected_users, bool) or not isinstance(affected_users, int):
        raise ValueError(f"Ticket {ticket_id} has invalid affected users.")

    if affected_users <= 0:
        raise ValueError(f"Ticket {ticket_id} has invalid affected users.")

    if ticket["priority"] not in VALID_PRIORITIES:
        raise ValueError(f"Ticket {ticket_id} has an invalid priority.")

    if ticket["status"] not in VALID_STATUSES:
        raise ValueError(f"Ticket {ticket_id} has an invalid status.")

    assigned_to = ticket["assigned_to"]

    if assigned_to is not None and (
        not isinstance(assigned_to, str) or not assigned_to.strip()
    ):
        raise ValueError(f"Ticket {ticket_id} has an invalid assignment.")

    notes = ticket.get("notes", [])

    if not isinstance(notes, list):
        raise ValueError(f"Ticket {ticket_id} notes must be a list.")

    note_ids = []

    for note in notes:
        validate_note(note, ticket_id)

        note_id = note["note_id"]

        if note_id in note_ids:
            raise ValueError(
                f"Ticket {ticket_id} has duplicate note ID {note_id}."
            )

        note_ids.append(note_id)

    # Support older CampusFlow files by adding an empty notes list.
    ticket["notes"] = notes


def validate_ticket_collection(tickets):
    """Validate every ticket and reject duplicate ticket IDs."""
    if not isinstance(tickets, list):
        raise ValueError("Tickets must be a list.")

    ticket_ids = []

    for ticket in tickets:
        if not isinstance(ticket, dict):
            raise ValueError("Each ticket must be a dictionary.")

        if not REQUIRED_FIELDS.issubset(ticket):
            raise ValueError("A ticket is missing required fields.")

        ticket_id = ticket["id"]

        if ticket_id in ticket_ids:
            raise ValueError(f"Duplicate ticket ID found: {ticket_id}")

        ticket_ids.append(ticket_id)
        validate_ticket_record(ticket)

    return tickets


def load_tickets(path=DEFAULT_PATH):
    """Load and fully validate tickets; return an empty list if no file exists."""
    file_path = Path(path)

    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            tickets = json.load(file)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ValueError(f"Invalid ticket JSON in {file_path}") from error

    return validate_ticket_collection(tickets)


def save_tickets(tickets, path=DEFAULT_PATH):
    """Save ticket data as readable JSON, replacing the previous snapshot."""
    if not isinstance(tickets, list):
        raise ValueError("Tickets must be a list")

    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    temporary_path = file_path.with_name(file_path.name + ".tmp")

    with temporary_path.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=2, ensure_ascii=False)
        file.write("\n")

    temporary_path.replace(file_path)