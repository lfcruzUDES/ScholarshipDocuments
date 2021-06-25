import unittest

import shipdoc.settings as settings
from googleapi.base_api import ServiceAPI
from googleapi.gss import GSS


class TestGoogleModule(unittest.TestCase):

    def test_base_class(self):
        service = ServiceAPI(
            settings.SECRETG,
            settings.DRIVE_SCOPES
        )

        self.assertTrue('serviceapi' in str(service).lower())

    def test_GSS_get_data(self):
        gss = GSS(
            settings.SECRETG,
            settings.SS_SCOPES,
            '1PSLlhh40ZLIz1utHmKsX1Q0mtahgTLvhbJvr09z8o-A',
            settings.RANGE_NAME
        )

        rows = gss.get_data();

        self.assertTrue(len(rows) == 29)
