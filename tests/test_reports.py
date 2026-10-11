
import unittest

from campusflow.reports import generate_report


class TestGenerateReport(unittest.TestCase):
    def setUp(self):
        self.tickets = [
            {
                "id": "T001",
                "status": "open",
                "priority": "critical",
            },
            {
                "id": "T002",
                "status": "in_progress",
                "priority": "high",
            },
            {
                "id": "T003",
                "status": "resolved",
                "priority": "high",
            },
            {
                "id": "T004",
                "status": "open",
                "priority": "low",
            },
        ]

    def test_total_tickets(self):
        report = generate_report(self.tickets)

        self.assertEqual(report["total"], 4)

    def test_status_breakdown(self):
        report = generate_report(self.tickets)

        self.assertEqual(
            report["by_status"],
            {
                "open": 2,
                "in_progress": 1,
                "resolved": 1,
            },
        )

    def test_priority_breakdown(self):
        report = generate_report(self.tickets)

        self.assertEqual(
            report["by_priority"],
            {
                "critical": 1,
                "high": 2,
                "medium": 0,
                "low": 1,
            },
        )

    def test_empty_ticket_list(self):
        report = generate_report([])

        self.assertEqual(report["total"], 0)
        self.assertEqual(sum(report["by_status"].values()), 0)
        self.assertEqual(sum(report["by_priority"].values()), 0)


if __name__ == "__main__":
    unittest.main()

