import unittest

from shipdoc.beneficiaries import Beneficiaries


class TestBeneficiaries(unittest.TestCase):

    def test_start_connection(self):
        Beneficiaries()

    def test_run(self):
        beneficiaries = Beneficiaries()
        beneficiaries.run()
