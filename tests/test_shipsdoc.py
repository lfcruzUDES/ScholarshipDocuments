import unittest

from shipdoc.scholarship_docs import ScholarshipDocs


class TestScholarshipDocs(unittest.TestCase):

    def test_process(self):
        ship = ScholarshipDocs(
            range_name='Respuestas!A2:I5'
        )

        ship.process()
