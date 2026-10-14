import copy
import unittest

from campusflow.notes import add_note, next_note_id, view_notes


def make_ticket(status="open", notes=None):
    return {
        "id": "T001",
        "title": "Wi-Fi not working",
        "category": "Network",
        "urgency": "high",
        "affected_users": 12,
        "priority": "critical",
        "status": status,
        "assigned_to": "IT Support",
        "notes": notes if notes is not None else []
    }


class TestAddNote(unittest.TestCase):
    def setUp(self):
        self.tickets = [make_ticket()]

    def test_adds_valid_note_to_open_ticket(self):
        result = add_note(
            self.tickets,
            "T001",
            "Mentor A",
            "Wi-Fi router reboot attempted"
        )

        self.assertTrue(result["ok"])
        self.assertEqual(len(self.tickets[0]["notes"]), 1)
        self.assertEqual(self.tickets[0]["notes"][0]["note_id"], "N001")
        self.assertEqual(self.tickets[0]["notes"][0]["author"], "Mentor A")

    def test_second_note_uses_next_id(self):
        add_note(self.tickets, "T001", "Mentor A", "Router reboot attempted")
        result = add_note(self.tickets, "T001", "Mentor B", "Investigating switch ports")

        self.assertTrue(result["ok"])
        self.assertEqual(result["note"]["note_id"], "N002")

    def test_rejects_note_on_resolved_ticket(self):
        self.tickets = [make_ticket(status="resolved")]
        before = copy.deepcopy(self.tickets)

        result = add_note(
            self.tickets,
            "T001",
            "Mentor A",
            "Wi-Fi router reboot attempted"
        )

        self.assertFalse(result["ok"])
        self.assertEqual(self.tickets, before)

    def test_rejects_blank_author_without_consuming_id(self):
        before = copy.deepcopy(self.tickets)

        result = add_note(
            self.tickets,
            "T001",
            "   ",
            "Wi-Fi router reboot attempted"
        )

        self.assertFalse(result["ok"])
        self.assertEqual(self.tickets, before)
        self.assertEqual(next_note_id(self.tickets[0]), "N001")

    def test_rejects_short_message_without_consuming_id(self):
        before = copy.deepcopy(self.tickets)

        result = add_note(
            self.tickets,
            "T001",
            "Mentor A",
            "1234"
        )

        self.assertFalse(result["ok"])
        self.assertEqual(self.tickets, before)
        self.assertEqual(next_note_id(self.tickets[0]), "N001")

    def test_rejects_unknown_ticket(self):
        result = add_note(
            self.tickets,
            "T999",
            "Mentor A",
            "Wi-Fi router reboot attempted"
        )

        self.assertFalse(result["ok"])
        self.assertEqual(result["error"], "Ticket not found.")

    def test_allows_note_after_reopen(self):
        self.tickets = [make_ticket(status="resolved")]

        rejected = add_note(
            self.tickets,
            "T001",
            "Mentor A",
            "Wi-Fi router reboot attempted"
        )

        self.tickets[0]["status"] = "open"

        accepted = add_note(
            self.tickets,
            "T001",
            "Mentor A",
            "Wi-Fi router reboot attempted"
        )

        self.assertFalse(rejected["ok"])
        self.assertTrue(accepted["ok"])
        self.assertEqual(accepted["note"]["note_id"], "N001")


class TestViewNotes(unittest.TestCase):
    def test_returns_notes_in_id_order(self):
        ticket = make_ticket(
            notes=[
                {"note_id": "N002", "author": "Mentor B", "message": "Investigating switch ports"},
                {"note_id": "N001", "author": "Mentor A", "message": "Router reboot attempted"}
            ]
        )

        result = view_notes([ticket], "T001")

        self.assertTrue(result["ok"])
        self.assertEqual(
            [note["note_id"] for note in result["notes"]],
            ["N001", "N002"]
        )

    def test_returns_empty_notes_for_new_ticket(self):
        result = view_notes([make_ticket()], "T001")

        self.assertTrue(result["ok"])
        self.assertEqual(result["notes"], [])

    def test_rejects_unknown_ticket(self):
        result = view_notes([make_ticket()], "T999")

        self.assertFalse(result["ok"])
        self.assertEqual(result["error"], "Ticket not found.")


if __name__ == "__main__":
    unittest.main()