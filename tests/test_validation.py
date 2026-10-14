import unittest

from campusflow.validation import (
    validate_affected_users,
    validate_category,
    validate_title,
    validate_urgency,
    validate_staff_label,
)


class TestValidateAffectedUsers(unittest.TestCase):
    def test_accepts_positive_integer(self):
        self.assertEqual(validate_affected_users(1), 1)
        self.assertEqual(validate_affected_users(10), 10)

    def test_rejects_zero(self):
        with self.assertRaises(ValueError):
            validate_affected_users(0)

    def test_rejects_negative_integer(self):
        with self.assertRaises(ValueError):
            validate_affected_users(-1)

    def test_rejects_float(self):
        with self.assertRaises(ValueError):
            validate_affected_users(2.5)

    def test_rejects_string(self):
        with self.assertRaises(ValueError):
            validate_affected_users("10")

    def test_rejects_boolean_true(self):
        with self.assertRaises(ValueError):
            validate_affected_users(True)

    def test_rejects_boolean_false(self):
        with self.assertRaises(ValueError):
            validate_affected_users(False)

    def test_rejects_none(self):
        with self.assertRaises(ValueError):
            validate_affected_users(None)


if __name__ == "__main__":
    unittest.main()

class TestValidateTitle(unittest.TestCase):
    def test_accepts_normal_title(self):
        self.assertEqual(validate_title("Wi-Fi not working"), "Wi-Fi not working")

    def test_trims_surrounding_spaces(self):
        self.assertEqual(
            validate_title("   Laptop will not start   "),
            "Laptop will not start"
        )

    def test_rejects_empty_string(self):
        with self.assertRaises(ValueError):
            validate_title("")

    def test_rejects_whitespace_only_title(self):
        with self.assertRaises(ValueError):
            validate_title("     ")

    def test_rejects_none(self):
        with self.assertRaises(ValueError):
            validate_title(None)

    def test_rejects_integer(self):
        with self.assertRaises(ValueError):
            validate_title(123)

    def test_rejects_list(self):
        with self.assertRaises(ValueError):
            validate_title(["Wi-Fi issue"])

class TestValidateCategory(unittest.TestCase):
    def test_accepts_network(self):
        self.assertEqual(validate_category("Network"), "Network")

    def test_accepts_lowercase_category(self):
        self.assertEqual(validate_category("network"), "Network")

    def test_accepts_category_with_spaces(self):
        self.assertEqual(validate_category("  hardware  "), "Hardware")

    def test_accepts_mixed_case_category(self):
        self.assertEqual(validate_category("SoFtWaRe"), "Software")

    def test_accepts_other(self):
        self.assertEqual(validate_category("other"), "Other")

    def test_rejects_unknown_category(self):
        with self.assertRaises(ValueError):
            validate_category("Maintenance")

    def test_rejects_empty_category(self):
        with self.assertRaises(ValueError):
            validate_category("")

    def test_rejects_whitespace_only_category(self):
        with self.assertRaises(ValueError):
            validate_category("   ")

    def test_rejects_none(self):
        with self.assertRaises(ValueError):
            validate_category(None)

    def test_rejects_integer(self):
        with self.assertRaises(ValueError):
            validate_category(1)

class TestValidateUrgency(unittest.TestCase):
    def test_accepts_low(self):
        self.assertEqual(validate_urgency("low"), "low")

    def test_accepts_medium(self):
        self.assertEqual(validate_urgency("medium"), "medium")

    def test_accepts_high(self):
        self.assertEqual(validate_urgency("high"), "high")

    def test_accepts_uppercase_urgency(self):
        self.assertEqual(validate_urgency("HIGH"), "high")

    def test_accepts_urgency_with_spaces(self):
        self.assertEqual(validate_urgency("  medium  "), "medium")

    def test_accepts_mixed_case_urgency(self):
        self.assertEqual(validate_urgency("MeDiUm"), "medium")

    def test_rejects_unknown_urgency(self):
        with self.assertRaises(ValueError):
            validate_urgency("urgent")

    def test_rejects_empty_urgency(self):
        with self.assertRaises(ValueError):
            validate_urgency("")

    def test_rejects_whitespace_only_urgency(self):
        with self.assertRaises(ValueError):
            validate_urgency("   ")

    def test_rejects_none(self):
        with self.assertRaises(ValueError):
            validate_urgency(None)

    def test_rejects_integer(self):
        with self.assertRaises(ValueError):
            validate_urgency(3)
class TestValidateStaffLabel(unittest.TestCase):
    def test_accepts_normal_staff_label(self):
        self.assertEqual(validate_staff_label("Mentor A"), "Mentor A")

    def test_trims_surrounding_spaces(self):
        self.assertEqual(validate_staff_label("  IT Support  "), "IT Support")

    def test_rejects_empty_string(self):
        with self.assertRaises(ValueError):
            validate_staff_label("")

    def test_rejects_whitespace_only_label(self):
        with self.assertRaises(ValueError):
            validate_staff_label("     ")

    def test_rejects_none(self):
        with self.assertRaises(ValueError):
            validate_staff_label(None)

    def test_rejects_integer(self):
        with self.assertRaises(ValueError):
            validate_staff_label(123)

    def test_rejects_list(self):
        with self.assertRaises(ValueError):
            validate_staff_label(["Mentor A"])