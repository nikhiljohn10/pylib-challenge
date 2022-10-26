import os
import unittest
from file_db import Database

TEST_DB_FILE = "test_database.db"


class DatabaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db = Database(TEST_DB_FILE)

    def tearDown(self) -> None:
        del self.db
        if os.path.exists(TEST_DB_FILE):
            os.remove(TEST_DB_FILE)

    def test_db(self):
        self.db = Database(TEST_DB_FILE)
        with self.assertRaises(KeyError):
            self.db.read("test_key")
        self.db.write("test_key", "test_value")
        self.assertEqual(self.db.read("test_key"), "test_value")
        self.db.delete("test_key")
        with self.assertRaises(KeyError):
            self.db.read("test_key")
