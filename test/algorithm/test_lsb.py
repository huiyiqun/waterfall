import unittest
import numpy


from waterfall.algorithm.lsb import LSBAlgorithm


class TestLSBAlgorithm(unittest.TestCase):
    def setUp(self):
        self.lsb = LSBAlgorithm(3)
        self.origin_secret_space = numpy.random.randint(0, 255, 200)
        self.watermark = b'this is a algorithm'

    def test_embed_and_extract(self):
        self.embedded_secret_space = self.lsb.embed(
            self.origin_secret_space, self.watermark)

        self.extracted_watermark = self.lsb.extract(self.embedded_secret_space)
        self.assertEqual(
            self.watermark, self.extracted_watermark[:len(self.watermark)])
