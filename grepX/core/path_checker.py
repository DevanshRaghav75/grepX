import sys

def compatible_path(path):

    if sys.platform.lower().startswith('win'):
        return path.replace('/', '\\')
    return path