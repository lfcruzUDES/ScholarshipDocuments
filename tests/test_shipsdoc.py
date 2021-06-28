import unittest

from shipdoc.scholarship_docs import ScholarshipDocs


class TestScholarshipDocs(unittest.TestCase):

    def test_process_pdf4(self):
        ship = ScholarshipDocs()

        ship.process()

    # def test_process_magick(self):
    #     ship = ScholarshipDocs(mode='magick')

    #     ship.process()
