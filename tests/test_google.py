import pathlib
import shutil
import unittest
import uuid

import shipdoc.settings as settings
from googleapi.base_api import ServiceAPI
from googleapi.gdrive import Drive
from googleapi.gss import GSS


class TestGoogleModule(unittest.TestCase):
    test_directory = pathlib.Path(__file__).parent / 'data_test'

    def setUp(self):
        if not self.test_directory.exists():
            self.test_directory.mkdir()

    def test_base_class(self):
        """ Test base class for Google APIs """
        service = ServiceAPI(
            settings.SECRETG,
            settings.DRIVE_SCOPES
        )

        self.assertTrue('serviceapi' in str(service).lower())

    def test_GSS_get_data(self):
        """ Test GSS API """

        gss = GSS(
            settings.SECRETG,
            settings.SS_SCOPES,
            ss_id='1PSLlhh40ZLIz1utHmKsX1Q0mtahgTLvhbJvr09z8o-A',
            range_name='Respuestas!A2:I30'
        )

        rows = gss.get_data();

        self.assertTrue(len(rows) == 29)

    def test_GSS_append(self):
        """ Append data to Sheet. """
        ss_id = '1F74_8k_nQUGArmUtBXD8WPC5l3skWatUn9GiifqwJ7k'
        range_name = 'index'

        gss = GSS.create(
            settings.SECRETG,
            settings.SS_SCOPES,
            ss_id,
            range_name
        )

        values = [
            [
                uuid.uuid4().hex,
                uuid.uuid4().hex,
                uuid.uuid4().hex,
                uuid.uuid4().hex,
            ]
        ]

        result = gss.append(values)

        self.assertTrue(len(values[0]), result)


    def test_Drive_download_file(self):
        drive = Drive(
            settings.SECRETG,
            settings.DRIVE_SCOPES,
        )

        target_file = self.test_directory / f'{uuid.uuid4().hex}.pdf'

        drive.download_file(
            '11nYW0IjB-iqESGy37qDswr0YvOJ8nThI',
            target_file
        )

        self.assertTrue(target_file.exists())

    def test_upload_file(self):
        drive = Drive(
            settings.SECRETG,
            settings.DRIVE_SCOPES,
        )

        target_file = self.test_directory / f'{uuid.uuid4().hex}.pdf'

        drive.download_file(
            '11nYW0IjB-iqESGy37qDswr0YvOJ8nThI',
            target_file
        )

        doc = drive.upload_file(
            'TEST_DOCUMENT.pdf',
            target_file,
            folders=['1Aar9k5d185Nb3N9bwLK_Yw_bnGp-dlYc']
        )

        print(doc)

    def tearDown(self):
        if self.test_directory.exists():
            shutil.rmtree(self.test_directory)
