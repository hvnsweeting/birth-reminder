import os

def fix_path(filename):
    #because this app run with crontab, it must be use abs path
    filepath = os.path.realpath(__file__)
    path = os.path.dirname(filepath)
    fixed = os.path.join(path, filename)
    return fixed
