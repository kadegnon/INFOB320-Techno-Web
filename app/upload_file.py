import os

ALLOW_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])


def allow_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOW_EXTENSIONS
