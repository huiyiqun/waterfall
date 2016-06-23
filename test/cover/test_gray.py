import unittest
import numpy as np

from waterfall.cover.picture import GrayCover


class TestRGBCover(unittest.TestCase):
    def setUp(self):
        self.cover = GrayCover(
            np.random.randint(0, 255, 4 * 4).reshape(4, 4))

    def test_read_phase(self):
        for f in self.cover.phases:
            self.assertTupleEqual(getattr(self.cover, f).shape, (4, 4))

    def test_rebuild_cover(self):
        backup = dict()
        for f in self.cover.phases:
            backup[f] = getattr(self.cover, f)

        rebuilt = GrayCover.from_phases(**backup)
        self.assertTupleEqual(rebuilt._data.shape, self.cover._data.shape)
        self.assertListEqual(
            list(rebuilt._data.flatten()), list(self.cover._data.flatten()))
