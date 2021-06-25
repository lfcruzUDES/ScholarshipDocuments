import unittest
from os import environ
from Exec import Executor


class Test_Executor(unittest.TestCase):
    """ Test of Executor class. """

    def setUp(self):
        self.EXEC = Executor()


if __name__ == "__main__":
    unittest.main()
