import os


class InvalidFileExtension(Exception):
    pass


ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg"}


def allowed_file(filename):
    return os.path.splitext(filename)[-1].lower() in ALLOWED_EXTENSIONS
