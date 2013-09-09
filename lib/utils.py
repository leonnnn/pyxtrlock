from ctypes import cdll
from ctypes.util import find_library

def check_and_load_library(libname):
    handle = find_library(libname)
    if handle is None:
        raise ImportError("unable to find system library: {}".format(
            libname))
    return cdll.LoadLibrary(handle)
