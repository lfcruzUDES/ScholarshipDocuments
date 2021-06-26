import unittest

from shipdoc.scholarship_docs import ScholarshipDocs


class TestScholarshipDocs(unittest.TestCase):

    def test_process(self):
        ship = ScholarshipDocs(
            ss_id='1PSLlhh40ZLIz1utHmKsX1Q0mtahgTLvhbJvr09z8o-A',
            range_name='Respuestas!A2:I5'
        )

        ship.process()
