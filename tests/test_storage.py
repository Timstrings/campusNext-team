"""Tests for persistent JSON ticket storage."""
import json
import tempfile
import unittest
from pathlib import Path

from campusflow.storage import load_tickets, save_tickets
from campusflow.tickets import create_ticket


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.path = Path(self.tempdir.name) / "tickets.json"

    def tearDown(self):
        self.tempdir.cleanup()

    def test_missing_file_returns_empty_list(self):
        self.assertEqual(load_tickets(self.path), [])

    def test_save_and_reload_ticket(self):
        ticket = create_ticket("Internet down", "Network", "high", 12, "T001")
        save_tickets([ticket], self.path)
        self.assertEqual(load_tickets(self.path), [ticket])

    def test_empty_list_persists(self):
        save_tickets([], self.path)
        self.assertEqual(load_tickets(self.path), [])

    def test_updates_persist(self):
        ticket = create_ticket("Internet down", "Network", "high", 12, "T001")
        save_tickets([ticket], self.path)
        ticket["status"] = "resolved"
        save_tickets([ticket], self.path)
        self.assertEqual(load_tickets(self.path)[0]["status"], "resolved")

    def test_corrupt_json_raises_value_error(self):
        self.path.write_text("{not-json", encoding="utf-8")
        with self.assertRaises(ValueError):
            load_tickets(self.path)

    def test_invalid_json_structure_raises_value_error(self):
        self.path.write_text(json.dumps({"tickets": []}), encoding="utf-8")
        with self.assertRaises(ValueError):
            load_tickets(self.path)

    def test_invalid_ticket_shape_raises_value_error(self):
        self.path.write_text(json.dumps([{"id": "T001"}]), encoding="utf-8")
        with self.assertRaises(ValueError):
            load_tickets(self.path)

    def test_non_list_save_rejected(self):
        with self.assertRaises(ValueError):
            save_tickets({"id": "T001"}, self.path)


if __name__ == "__main__":
    unittest.main()
