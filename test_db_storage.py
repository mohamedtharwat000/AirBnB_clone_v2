#!/usr/bin/python3
"""unittest for DBStorage"""
import unittest
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


class TestDBStorage(unittest.TestCase):
    """ """

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_attributes(self):
        self.assertTrue(isinstance(self.storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))
