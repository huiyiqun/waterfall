import magic

from waterfall.io.video import read_video
from waterfall.io.picture import read_picture


def read(filepath):
    mime = magic.from_file(filepath, mime=True).decode()
    type, subtype = mime.split('/')

    if type == 'video':
        cover = read_video(filepath)
    elif type == 'image':
        cover = read_picture(filepath)

    cover.mime = mime

    return cover
