import copy
import unittest

from campusflow.tickets import (
    calculate_priority,
    create_ticket,
    find_ticket,
    generate_ticket_id,
    list_tickets,
    validate_ticket,
    view_ticket,
)

class TestPriority(unittest.TestCase):

    def test_critical_priority(self):
        result = calculate_priority("high", 12)
        self.assertEqual(result, "critical")

    def test_high_priority(self):
        result = calculate_priority("high", 2)
        self.assertEqual(result, "high")

    def test_medium_priority(self):
        result = calculate_priority("low", 4)
        self.assertEqual(result, "medium")

    def test_low_priority(self):
        result = calculate_priority("low", 1)
        self.assertEqual(result, "low")

    def test_priority_boundary_3_users(self):
        result = calculate_priority("low", 3)
        self.assertEqual(result, "medium")

    def test_priority_boundary_10_users(self):
        result = calculate_priority("high", 10)
        self.assertEqual(result, "critical")


class TestTicketCreation(unittest.TestCase):

    def test_valid_ticket(self):
        ticket = create_ticket(
            "Internet problem",
            "Network",
            "high",
            12,
            "T001"
        )

        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")

    def test_invalid_title(self):
        with self.assertRaises(ValueError):
            validate_ticket("", "Network", "high", 5)

    def test_whitespace_only_title(self):
        with self.assertRaises(ValueError):
            validate_ticket("   ", "Network", "high", 5)

    def test_invalid_users(self):
        with self.assertRaises(ValueError):
            validate_ticket("Internet", "Network", "high", 0)

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            validate_ticket("WiFi problem", "Food", "high", 5)

    def test_invalid_urgency(self):
        with self.assertRaises(ValueError):
            validate_ticket("WiFi problem", "Network", "extreme", 5)

    def test_generate_ticket_id(self):
        tickets = [
            {"id": "T001"},
            {"id": "T002"}
        ]

        result = generate_ticket_id(tickets)
        self.assertEqual(result, "T003")

    def test_generate_ticket_id_empty(self):
        result = generate_ticket_id([])
        self.assertEqual(result, "T001")
    
def test_created_ticket_has_empty_notes_list(self):
    ticket = create_ticket(
        "Wi-Fi not working",
        "Network",
        "high",
        12,
        "T001"
    )

    self.assertEqual(ticket["notes"], [])


def test_validate_ticket_normalises_category_and_urgency(self):
    result = validate_ticket(
        "  Wi-Fi issue  ",
        " network ",
        " HIGH ",
        10
    )

    self.assertEqual(
        result,
        ("Wi-Fi issue", "Network", "high", 10)
    )


def test_validate_ticket_rejects_boolean_affected_users(self):
    with self.assertRaises(ValueError):
        validate_ticket(
            "Wi-Fi issue",
            "Network",
            "high",
            True
        )


def test_validate_ticket_rejects_invalid_category(self):
    with self.assertRaises(ValueError):
        validate_ticket(
            "Wi-Fi issue",
            "Maintenance",
            "high",
            10
        )


class TestTicketViewing(unittest.TestCase):

    def test_list_tickets(self):
        tickets = [
            {"id": "T001"},
            {"id": "T002"}
        ]

        result = list_tickets(tickets)
        self.assertEqual(len(result), 2)

    def test_view_existing_ticket(self):
        tickets = [
            {"id": "T001", "title": "Internet problem"},
            {"id": "T002", "title": "Computer problem"}
        ]

        result = view_ticket(tickets, "T002")
        self.assertEqual(result["title"], "Computer problem")

    def test_view_missing_ticket(self):
        tickets = [
            {"id": "T001", "title": "Internet problem"}
        ]

        result = view_ticket(tickets, "T999")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()

class TestFindTicket(unittest.TestCase):
    def setUp(self):
        self.tickets = [
            {
                "id": "T001",
                "title": "Wi-Fi not working",
                "category": "Network",
                "urgency": "high",
                "affected_users": 12,
                "priority": "critical",
                "status": "open",
                "assigned_to": None,
                "notes": []
            },
            {
                "id": "T002",
                "title": "Laptop will not start",
                "category": "Hardware",
                "urgency": "medium",
                "affected_users": 2,
                "priority": "low",
                "status": "open",
                "assigned_to": None,
                "notes": []
            }
        ]

    def test_returns_matching_ticket(self):
        ticket = find_ticket(self.tickets, "T002")

        self.assertIsNotNone(ticket)
        self.assertEqual(ticket["id"], "T002")

    def test_returns_none_for_unknown_ticket(self):
        self.assertIsNone(find_ticket(self.tickets, "T999"))

    def test_returns_none_for_non_string_id(self):
        self.assertIsNone(find_ticket(self.tickets, 1))

    def test_does_not_modify_ticket_collection(self):
        before = copy.deepcopy(self.tickets)

        find_ticket(self.tickets, "T001")

        self.assertEqual(self.tickets, before)

def find_ticket(tickets, ticket_id):
    """Return the ticket with the given ID, or None if it does not exist."""
    if not isinstance(ticket_id, str):
        return None

    for ticket in tickets:
        if ticket.get("id") == ticket_id:
            return ticket

    return None