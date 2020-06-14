import re
import unittest

from hocron.line_pattern import LinePattern


class TestLinePattern(unittest.TestCase):

    def test_line_pattern(self):
        line_pattern = LinePattern(['EUR', re.compile('\d\d\.\d\d')])  # noqa 
        matched_words = line_pattern.match(['EUR', '45.12'])

        self.assertTrue(matched_words)
        self.assertEquals(
            matched_words,
            ['EUR', '45.12']
        )
