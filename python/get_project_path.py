import os, sys

from pathlib import Path


def get_project_path():
    return Path(os.path.dirname(os.path.realpath(sys.argv[0])))
