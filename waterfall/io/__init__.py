import magic

from waterfall.io.video import read_video
from waterfall.io.picture import read_picture


def read(filepath):
    mime = magic.from_file(filepath, mime=True)
    type, subtype = mime.split('/')

    if type == 'video':
        return read_video(filepath)
    elif type == 'image':
        return read_picture(filepath)
