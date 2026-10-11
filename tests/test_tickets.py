import unittest

from campusflow.tickets import (
    calculate_priority,
    validate_ticket,
    create_ticket,
    generate_ticket_id,
    list_tickets,
    view_ticket
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