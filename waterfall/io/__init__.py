import magic

from waterfall.io.video import read_video


def read(filepath):
    mime = magic.from_file(filepath, mime=True)
    type, subtype = mime.split('/')

    if type == 'video':
        return read_video(filepath)
