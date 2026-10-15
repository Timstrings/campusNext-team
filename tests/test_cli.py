"""Integration tests for the interactive CampusFlow Next CLI."""
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

            with (
                patch("builtins.input", side_effect=inputs),
                patch("sys.stdout", output),
                patch(
                    "main.load_tickets",
                    side_effect=lambda: load_tickets(data_file),
                ),
                patch(
                    "main.save_tickets",
                    side_effect=lambda tickets: save_tickets(
                        tickets, data_file
                    ),
                ),
            ):
                main()

        return output.getvalue()

    def test_menu_exit(self):
        output = self.run_cli(["11"])

        self.assertIn("CAMPUSFLOW NEXT", output)
        self.assertIn("Saved. Goodbye!", output)

    def test_empty_list_and_report(self):
        output = self.run_cli(["2", "6", "11"])

        self.assertIn("No tickets yet.", output)
        self.assertIn("Total tickets: 0", output)
        self.assertIn("Resolution: 0.0%", output)

    def test_create_list_view_and_report(self):
        output = self.run_cli([
            "1", "Internet not working", "Network", "high", "12",
            "2", "6", "11",
        ])

        self.assertIn("Created T001 with critical priority.", output)
        self.assertIn("T001 | Internet not working", output)
        self.assertIn("Total tickets: 1", output)
        self.assertIn("Resolution: 0.0%", output)

    def test_assign_progress_resolve_reopen_queue(self):
        output = self.run_cli([
            "1", "Internet down", "Network", "high", "12",
            "3", "T001", "Timothy",
            "4", "T001", "in_progress",
            "5",
            "4", "T001", "resolved",
            "5",
            "4", "T001", "open",
            "5",
            "6",
            "11",
        ])

        self.assertIn("Ticket assigned.", output)
        self.assertIn("Ticket status updated.", output)
        self.assertIn("T001 | Internet down", output)
        self.assertIn("Total tickets: 1", output)

    def test_ticket_survives_restart(self):
        from campusflow.storage import load_tickets, save_tickets

        with tempfile.TemporaryDirectory() as tempdir:
            data_file = Path(tempdir) / "tickets.json"
            output = io.StringIO()

            with (
                patch("main.load_tickets", side_effect=lambda: load_tickets(data_file)),
                patch("main.save_tickets", side_effect=lambda tickets: save_tickets(tickets, data_file)),
                patch("sys.stdout", output),
            ):
                with patch(
                    "builtins.input",
                    side_effect=[
                        "1", "Internet down", "Network", "high", "12", "11"
                    ],
                ):
                    main()

                with patch(
                    "builtins.input",
                    side_effect=["2", "11"],
                ):
                    main()

            self.assertIn("Created T001 with critical priority.", output.getvalue())
            self.assertIn("T001 | Internet down", output.getvalue())
            self.assertEqual(load_tickets(data_file)[0]["id"], "T001")

    def test_invalid_menu_choice_does_not_crash(self):
        output = self.run_cli(["0", "11"])

        self.assertIn("Please choose a number from 1 to 11.", output)
        self.assertIn("Saved. Goodbye!", output)

    def test_invalid_ticket_creation_does_not_crash(self):
        output = self.run_cli([
            "1", "Internet down", "Network", "high", "abc", "11"
        ])

        self.assertIn("Error:", output)
        self.assertIn("Saved. Goodbye!", output)

    def test_add_and_view_note(self):
        output = self.run_cli([
            "1", "Internet down", "Network", "high", "12",
            "8", "T001", "Mentor A", "Wi-Fi router reboot attempted",
            "9", "T001",
            "11",
        ])

        self.assertIn("Added note N001.", output)
        self.assertIn("N001 | Mentor A | Wi-Fi router reboot attempted", output)


if __name__ == "__main__":
    unittest.main()