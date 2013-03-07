from ctypes import *
from ctypes.util import find_library

from xcb import Connection

libx = cdll.LoadLibrary(find_library('X11-xcb'))

class Display(Structure):
    pass

create_window = libx.XOpenDisplay
create_window.argtypes = [c_char_p]
create_window.restype = POINTER(Display)

close_window = libx.XCloseDisplay
close_window.argtypes = [POINTER(Display)]
close_window.restype = c_int

get_xcb_connection = libx.XGetXCBConnection
get_xcb_connection.argtypes = [POINTER(Display)]
get_xcb_connection.restype = POINTER(Connection)
