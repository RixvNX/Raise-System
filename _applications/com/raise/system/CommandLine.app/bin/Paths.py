import os
import sys

def getPath() -> str:
    if hasattr(sys, 'frozen'):
        f_paths = os.path.dirname(sys.executable)
        # f_paths = f_paths[:-4]
        return f_paths
    paths = os.path.dirname(__file__)
    # paths = paths[:-4]
    return paths

def getSubPaths() -> str:
    __PATHER__ = getPath()
    __PATHER__ = __PATHER__.split("/")
    __PATHER__.pop(-1)
    return "/".join(__PATHER__)