#!/usr/bin/python3
import unittest  # For unit testing framework
import MySQLdb  # For MySQL database interaction
from models import storage  # Import storage object to interact with the models
from models.state import State  # Import the State model to test

class TestState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up MySQL connection and data for testing"""
        cls.db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        cls.cursor = cls.db.cursor()
        cls.cursor.execute("DELETE FROM states")  # Clear any existing data in the table

    @classmethod
    def tearDownClass(cls):
        """Close the cursor and database connection"""
        cls.cursor.close()
        cls.db.close()

    def test_create_state(self):
        """Test the creation of a new state"""
        # Get the current count of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Create a new state object
        state = State(name="California")
        state.save()

        # Check if a new state was added to the database
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        # Assert that the state count has increased by 1
        self.assertEqual(final_count, initial_count + 1)

