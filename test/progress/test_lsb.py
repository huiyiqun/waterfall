import unittest
from scipy.misc import imshow

from waterfall.io import read
from waterfall.transform.flatten import flatten
from waterfall.transform.select_phase import select_phase
from waterfall.algorithm.lsb import LSBAlgorithm


class TestLSBProgress(unittest.TestCase):
    def test_color(self):
        cover = read("./test_case/lena_color.jpg")
        lsb = LSBAlgorithm(3)
        watermark = b'Tsinghua University'

        secret_space = flatten(select_phase(cover, 'R'))

        embedded_cover = secret_space.revert(
            lsb.embed(secret_space, watermark))

        imshow(embedded_cover._data)

        extracted = lsb.extract(flatten(select_phase(embedded_cover, 'R')))

        self.assertEqual(watermark, extracted[:len(watermark)])

    def test_gray(self):
        cover = read("./test_case/lena_gray.jpg")
        lsb = LSBAlgorithm(3)
        watermark = b'Tsinghua University'

        secret_space = flatten(select_phase(cover, 'gray'))

        embedded_cover = secret_space.revert(
            lsb.embed(secret_space, watermark))

        imshow(embedded_cover._data)

        extracted = lsb.extract(flatten(select_phase(embedded_cover, 'gray')))

        self.assertEqual(watermark, extracted[:len(watermark)])
