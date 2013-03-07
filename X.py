from ctypes import *
from ctypes.util import find_library

from xcb import Connection, Window

libx = cdll.LoadLibrary(find_library('X11-xcb'))

class Display(Structure):
    pass


Time = c_ulong
Bool = c_int

class KeyEvent(Structure):
    _fields_ = [
        ("type", c_int),
        ("serial", c_ulong),
        ("send_event", Bool),
        ("display", POINTER(Display)),
        ("window", Window),
        ("root", Window),
        ("subwindow", Window),
        ("time", Time),
        ("x", c_int),
        ("y", c_int),
        ("x_root", c_int),
        ("y_root", c_int),
        ("state", c_uint),
        ("key_code", c_uint),
        ("same_screen", Bool)
    ]

Keysym = c_uint32
Status = c_uint32


# XXX evil :)
# Should really use opaque structs for type safety
IM = POINTER(c_uint32)
IC = POINTER(c_uint32)

create_window = libx.XOpenDisplay
create_window.argtypes = [c_char_p]
create_window.restype = POINTER(Display)

close_window = libx.XCloseDisplay
close_window.argtypes = [POINTER(Display)]
close_window.restype = c_int

get_xcb_connection = libx.XGetXCBConnection
get_xcb_connection.argtypes = [POINTER(Display)]
get_xcb_connection.restype = POINTER(Connection)

open_IM = libx.XOpenIM
open_IM.argtypes = [
    POINTER(Display),   # display
    c_void_p, c_void_p, c_void_p
]
open_IM.restype = IM

create_IC = libx.XCreateIC
create_IC.argtypes = [
    IM,     # input method
    c_char_p,   # inputStyle
    c_uint32,
    c_void_p
]
create_IC.restype = IC

N_INPUT_STYLE = b"inputStyle"
IM_PRE_EDIT_NOTHING = 0x0008
IM_STATUS_NOTHING = 0x0400

set_ic_focus = libx.XSetICFocus
set_ic_focus.argtypes = [IC]
set_ic_focus.restype = None

utf8_lookup_string = libx.Xutf8LookupString
utf8_lookup_string.argtypes = [
    IC,
    POINTER(KeyEvent),
    POINTER(c_char),
    c_int,  # len
    POINTER(Keysym),
    POINTER(Status)
]
utf8_lookup_string.restype = c_int

BUFFER_OVERFLOW = -1
LOOKUP_NONE = 1
LOOKUP_CHARS = 2
LOOKUP_KEYSYM = 3
LOOKUP_BOTH = 4
