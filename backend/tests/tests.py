import unittest
from app.models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    def test_valid_user(self):
        user = User(user_id="12345")
        self.assertEqual(user.user_id, "12345")
        self.assertIsInstance(user.created_at, datetime)
    
    def test_invalid_id_empty(self):
        with self.assertRaises(ValueError) as context:
            user = User(user_id=None)
        self.assertIn("User ID cannot be empty", str(context.exception))
    
    def test_invalid_id_too_long(self):
        with self.assertRaises(ValueError) as context:
            user = User(user_id="123456789101112")
        self.assertIn("User ID cannot be longer than 10 characters", str(context.exception))
    
    def test_invalid_id_not_string(self):
        with self.assertRaises(ValueError) as context:
            user = User(user_id=1234)
        self.assertIn("User ID must be a string", str(context.exception))

if __name__ == '__main__':
    unittest.main()