from scipy.ndimage import imread

from waterfall.cover.picture import RGBCover


def read_picture(filepath):
    imarray = imread(filepath)
    if imarray.shape[2] == 3:
        return RGBCover(imarray)
