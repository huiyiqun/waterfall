from waterfall.cover import Cover


class PictureCover(Cover):
    pass


class RGBCover(PictureCover):
    def __init__(self, imarray):
        super().__init__()
        self._data = imarray

    @property
    def R(self):
        return self._data[:, :, 0]

    @property
    def G(self):
        return self._data[:, :, 1]

    @property
    def B(self):
        return self._data[:, :, 2]
