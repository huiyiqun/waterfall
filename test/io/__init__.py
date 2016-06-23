import unittest

from waterfall.io import read


class TestRead(unittest.TestCase):
    def test_non_exists(self):
        with self.assertRaises(IOError):
            read('non-exist-file-here')
