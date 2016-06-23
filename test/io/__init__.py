import unittest

from waterfall.io import read
from waterfall.cover.picture import RGBCover


class TestRead(unittest.TestCase):
    def test_read_non_exists(self):
        with self.assertRaises(IOError):
            read('non-exist-file-here')

    def test_read_rgb_jpg(self):
        cover = read('test_case/lena_color.jpg')
        self.assertIsInstance(cover, RGBCover)
