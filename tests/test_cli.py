"""Integration tests for the interactive CampusFlow CLI."""
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from main import main


class TestInteractiveCLI(unittest.TestCase):
    def run_cli(self, inputs):
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as tempdir:
            data_file = Path(tempdir) / "tickets.json"
            from campusflow.storage import load_tickets, save_tickets
            with patch("builtins.input", side_effect=inputs), patch("sys.stdout", output), \
                 patch("main.load_tickets", side_effect=lambda: load_tickets(data_file)), \
                 patch("main.save_tickets", side_effect=lambda tickets: save_tickets(tickets, data_file)):
                main()
        return output.getvalue()

    def test_menu_exit(self):
        output = self.run_cli(["9"])
        self.assertIn("Create Ticket", output)
        self.assertIn("Goodbye!", output)

    def test_empty_list_and_report(self):
        output = self.run_cli(["2", "8", "9"])
        self.assertIn("No tickets available.", output)
        self.assertIn("'total': 0", output)

    def test_create_list_view_and_report(self):
        output = self.run_cli([
            "1", "Internet not working", "Network", "high", "12",
            "2", "3", "T001", "8", "9",
        ])
        self.assertIn("Ticket created successfully!", output)
        self.assertIn("'id': 'T001'", output)
        self.assertIn("'priority': 'critical'", output)
        self.assertIn("'total': 1", output)

    def test_assign_progress_resolve_reopen_queue(self):
        output = self.run_cli([
            "1", "Internet down", "Network", "high", "12",
            "4", "T001", "Timothy",
            "5", "T001", "in_progress",
            "7",
            "5", "T001", "resolved",
            "7",
            "6", "T001",
            "9",
        ])
        self.assertIn("Assigned:", output)
        self.assertIn("Updated:", output)
        self.assertIn("No unresolved tickets.", output)
        self.assertIn("Reopened:", output)

    def test_invalid_input_does_not_crash(self):
        output = self.run_cli([
            "0", "1", "Bad input", "Network", "high", "abc",
            "4", "T999", "Timothy", "9",
        ])
        self.assertIn("Invalid choice.", output)
        self.assertIn("Error:", output)
        self.assertIn("Goodbye!", output)


if __name__ == "__main__":
    unittest.main()
