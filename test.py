
import unittest
from login import login


class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(
            login("admin", "1234"),
            "Login successful"
        )

    def test_wrong_password(self):
        self.assertEqual(
            login("admin", "1111"),
            "Invalid username or password"
        )

    def test_wrong_username(self):
        self.assertEqual(
            login("student", "1234"),
            "Invalid username or password"
        )

    def test_empty_username(self):
        with self.assertRaises(ValueError):
            login("", "1234")

    def test_empty_password(self):
        with self.assertRaises(ValueError):
            login("admin", "")


if __name__ == "__main__":
    unittest.main()
        
