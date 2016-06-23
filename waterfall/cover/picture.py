import numpy as np

from waterfall.cover import Cover


class PictureCover(Cover):
    def __init__(self, imarray):
        super().__init__()
        self._data = imarray


class RGBCover(PictureCover):
    phases = ['R', 'G', 'B']

    @property
    def R(self):
        return self._data[:, :, 0]

    @property
    def G(self):
        return self._data[:, :, 1]

    @property
    def B(self):
        return self._data[:, :, 2]

    @classmethod
    def from_phases(cls, R, G, B):
        return cls(np.dstack((R, G, B)))


class GrayCover(PictureCover):
    phases = ['gray']

    @property
    def gray(self):
        return self._data

    @classmethod
    def from_phases(cls, gray):
        return cls(gray)
