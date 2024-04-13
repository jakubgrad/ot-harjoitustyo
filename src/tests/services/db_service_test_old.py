import unittest
import os
from services.db_service import DbService


class TestDbService(unittest.TestCase):
    def setUp(self):
        self.db_service = DbService()
        self.db_path = "src/db/house_app.db"

    def test_creates_databases_once_initialized(self):
        self.assertEqual(os.path.exists(self.db_path), True)
