import unittest
from os import environ
from Exec import Executor


class Test_Executor(unittest.TestCase):
    """ Test of Executor class. """

    def setUp(self):
        self.EXEC = Executor()

    def test_evironment(self):
        self.assertTrue(bool(environ['BASE_PATH']))
        self.assertTrue(bool(environ['SECRETG']))
        self.assertTrue(bool(environ['SPREADSHEET_ID']))
        self.assertTrue(bool(environ['SHEET_NAME']))
        self.assertTrue(bool(environ['RANGE_NAME']))
        self.assertTrue(bool(environ['SS_SCOPES']))


if __name__ == "__main__":
    unittest.main()
