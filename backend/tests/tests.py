import unittest
from datetime import datetime
from app.models.user import User
from app.persist.connection import get_session, create_db_and_tables
from sqlmodel import Session, SQLModel, create_engine

class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine("sqlite:///:memory:")
        create_db_and_tables()

    def setUp(self):
        SQLModel.metadata.create_all(self.engine)
        self.session = Session(self.engine)

    def tearDown(self):
        self.session.close()
        SQLModel.metadata.drop_all(self.engine)

    def test_valid_user(self):
        user = User(name="test_user")
        self.assertEqual(user.name, "test_user")
        self.assertIsInstance(user.created_at, datetime)

    def test_invalid_name_too_long(self):
        with self.assertRaises(ValueError) as context:
            user = User(name="123456789101112")
        self.assertIn("Name cannot be longer than 10 characters", str(context.exception))
    
    def test_invalid_name_not_string(self):
        with self.assertRaises(ValueError) as context:
            user = User(name=1234)
        self.assertIn("Name must be a string", str(context.exception))

    def test_invalid_empty_name(self):
        with self.assertRaises(ValueError) as context:
            user = User(name="")
        self.assertIn("Name cannot be empty", str(context.exception))

    def test_database_operations(self):
        user = User(name="dbtest")
        self.session.add(user)
        self.session.commit()
        
        db_user = self.session.get(User, user.id)
        self.assertIsNotNone(db_user)
        self.assertEqual(db_user.name, "dbtest")
        self.assertIsInstance(db_user.created_at, datetime)

if __name__ == '__main__':
    unittest.main()