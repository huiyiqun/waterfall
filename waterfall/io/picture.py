from scipy.ndimage import imread

from waterfall.cover.picture import RGBCover, GrayCover


def read_picture(filepath):
    imarray = imread(filepath)
    if len(imarray.shape) == 2:
        return GrayCover(imarray)
    elif len(imarray.shape) == 3 and imarray.shape[2] == 3:
        return RGBCover(imarray)
