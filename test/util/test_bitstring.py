import unittest

from waterfall.util.bitstring import Bitstring


class TestBitstring(unittest.TestCase):
    def setUp(self):
        self.bitstring = Bitstring([
            255, 1
        ])

    def test_len(self):
        self.assertEqual(len(self.bitstring), 16)

    def test_getitem(self):
        self.assertListEqual(
            [self.bitstring[i] for i in range(16)], [1] * 9 + [0] * 7)
        self.assertListEqual(
            [self.bitstring[-i-1] for i in range(16)], [0] * 7 + [1] * 9)

    def test_getslice(self):
        self.assertEqual(self.bitstring[0:8], 255)
        self.assertEqual(self.bitstring[1:9], 255)
        self.assertEqual(self.bitstring[2:10], 127)
        self.assertEqual(self.bitstring[0:16:2], 31)

    def test_setitem(self):
        self.bitstring[15] = 1
        self.assertListEqual(self.bitstring.bytes, [255, 129])

        self.bitstring[-1] = 0
        self.assertListEqual(self.bitstring.bytes, [255, 1])

        self.bitstring[0] = 0
        self.assertListEqual(self.bitstring.bytes, [254, 1])

        self.bitstring[-16] = 1
        self.assertListEqual(self.bitstring.bytes, [255, 1])

    def test_setslice(self):
        for i in range(256 * 256):
            self.bitstring[:] = i
            self.assertListEqual(self.bitstring.bytes, [i % 256, i // 256])

        self.bitstring[9:] = 0
        self.assertListEqual(self.bitstring.bytes, [255, 1])
