from campusflow.tickets import find_ticket
from campusflow.validation import (
    validate_note_message,
    validate_staff_label,
)


def next_note_id(ticket):
    """Return the next available note ID for a ticket."""
    existing_ids = []

    for note in ticket.get("notes", []):
        existing_ids.append(note["note_id"])

    number = 1

    while f"N{number:03d}" in existing_ids:
        number += 1

    return f"N{number:03d}"


def add_note(tickets, ticket_id, author, message):
    """Add a validated follow-up note to an open or in-progress ticket.

    Returns a result dictionary. A rejected note does not change the
    ticket collection or consume a note ID.
    """
    ticket = find_ticket(tickets, ticket_id)

    if ticket is None:
        return {
            "ok": False,
            "error": "Ticket not found."
        }

    if ticket["status"] not in ("open", "in_progress"):
        return {
            "ok": False,
            "error": "A resolved ticket cannot receive a new note until it is reopened."
        }

    try:
        validated_author = validate_staff_label(author)
        validated_message = validate_note_message(message)
    except ValueError as error:
        return {
            "ok": False,
            "error": str(error)
        }

    note = {
        "note_id": next_note_id(ticket),
        "author": validated_author,
        "message": validated_message
    }

    ticket["notes"].append(note)

    return {
        "ok": True,
        "ticket": ticket,
        "note": note
    }


def view_notes(tickets, ticket_id):
    """Return all notes for a ticket in note-ID order."""
    ticket = find_ticket(tickets, ticket_id)

    if ticket is None:
        return {
            "ok": False,
            "error": "Ticket not found."
        }

    notes = sorted(ticket.get("notes", []), key=lambda note: note["note_id"])

    return {
        "ok": True,
        "ticket": ticket,
        "notes": notes
    }