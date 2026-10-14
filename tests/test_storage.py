"""Tests for persistent JSON ticket storage."""
import json
import tempfile
import unittest
from pathlib import Path

from campusflow.storage import load_tickets, save_tickets
from campusflow.tickets import create_ticket


class TestNotesStorage(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "tickets.json"

        self.tickets = [
            {
                "id": "T001",
                "title": "Wi-Fi not working",
                "category": "Network",
                "urgency": "high",
                "affected_users": 12,
                "priority": "critical",
                "status": "open",
                "assigned_to": "IT Support",
                "notes": [
                    {
                        "note_id": "N001",
                        "author": "Mentor A",
                        "message": "Wi-Fi router reboot attempted"
                    }
                ]
            }
        ]

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_notes_survive_save_and_reload(self):
        save_tickets(self.tickets, self.path)
        loaded = load_tickets(self.path)

        self.assertEqual(loaded, self.tickets)
        self.assertEqual(loaded[0]["notes"][0]["note_id"], "N001")

    def test_old_ticket_without_notes_is_given_empty_notes(self):
        old_ticket = {
            "id": "T001",
            "title": "Wi-Fi not working",
            "category": "Network",
            "urgency": "high",
            "affected_users": 12,
            "priority": "critical",
            "status": "open",
            "assigned_to": None
        }

        save_tickets([old_ticket], self.path)
        loaded = load_tickets(self.path)

        self.assertEqual(loaded[0]["notes"], [])

    def test_duplicate_ticket_id_is_rejected(self):
        duplicate_tickets = [
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
                "id": "T001",
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

        save_tickets(duplicate_tickets, self.path)

        with self.assertRaises(ValueError):
            load_tickets(self.path)

    def test_malformed_note_is_rejected(self):
        self.tickets[0]["notes"] = [
            {
                "note_id": "N001",
                "author": "Mentor A"
            }
        ]

        save_tickets(self.tickets, self.path)

        with self.assertRaises(ValueError):
            load_tickets(self.path)

    def test_duplicate_note_id_is_rejected(self):
        self.tickets[0]["notes"] = [
            {
                "note_id": "N001",
                "author": "Mentor A",
                "message": "Router reboot attempted"
            },
            {
                "note_id": "N001",
                "author": "Mentor B",
                "message": "Investigating switch ports"
            }
        ]

        save_tickets(self.tickets, self.path)

        with self.assertRaises(ValueError):
            load_tickets(self.path)