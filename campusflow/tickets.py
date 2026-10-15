from campusflow.validation import (
    validate_affected_users,
    validate_category,
    validate_title,
    validate_urgency,
)
CATEGORIES = ["Network", "Hardware", "Software", "Other"]
STATUSES = ["open", "in_progress", "resolved"]
PRIORITIES = ["low", "medium", "high", "critical"]

def calculate_priority(urgency, affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"

    elif urgency == "high" or affected_users >= 10:
        return "high"

    elif urgency == "medium" or affected_users >= 3:
        return "medium"

    else:
        return "low"

def validate_ticket(title, category, urgency, affected_users):
    """Validate ticket input before creating or changing a ticket.

    Returns normalised ticket values.
    Raises ValueError if any input is invalid.
    """
    validated_title = validate_title(title)
    validated_category = validate_category(category)
    validated_urgency = validate_urgency(urgency)
    validated_affected_users = validate_affected_users(affected_users)

    return (
        validated_title,
        validated_category,
        validated_urgency,
        validated_affected_users,
    )
def create_ticket(title, category, urgency, affected_users, ticket_id):
    title, category, urgency, affected_users = validate_ticket(
        title, category, urgency, affected_users
    )

    ticket = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": calculate_priority(urgency, affected_users),
        "status": "open",
        "assigned_to": None,
        "notes": []
    }

    return ticket
def generate_ticket_id(tickets):
    numbers = []

    for ticket in tickets:
        number = int(ticket["id"][1:])
        numbers.append(number)

    if numbers:
        next_number = max(numbers) + 1
    else:
        next_number = 1

    return f"T{next_number:03d}" 

def list_tickets(tickets):
    return tickets       

def view_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    return None    

def find_ticket(tickets, ticket_id):
    """Return the ticket with the given ID, or None if it does not exist."""
    if not isinstance(ticket_id, str):
        return None

    for ticket in tickets:
        if ticket.get("id") == ticket_id:
            return ticket

    return None