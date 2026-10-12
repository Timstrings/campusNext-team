"""Persist CampusFlow tickets in a JSON file."""
import json
from pathlib import Path

DEFAULT_PATH = Path("tickets.json")
REQUIRED_FIELDS = {"id", "title", "category", "urgency", "affected_users", "priority", "status", "assigned_to"}


def load_tickets(path=DEFAULT_PATH):
    """Load tickets; return an empty list when no data file exists."""
    file_path = Path(path)
    if not file_path.exists():
        return []
    try:
        with file_path.open("r", encoding="utf-8") as file:
            tickets = json.load(file)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ValueError(f"Invalid ticket JSON in {file_path}") from error
    if not isinstance(tickets, list) or any(
        not isinstance(ticket, dict) or not REQUIRED_FIELDS.issubset(ticket)
        for ticket in tickets
    ):
        raise ValueError(f"Invalid ticket data in {file_path}")
    return tickets


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
