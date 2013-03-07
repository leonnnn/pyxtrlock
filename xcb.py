#!/usr/bin/env python3

from ctypes import *
from ctypes.util import find_library


class Connection(Structure):
    pass


class Setup(Structure):
    pass


Window = c_uint32
Colormap = c_uint32
VisualID = c_uint32


class Screen(Structure):
    _fields_ = [
        ("root", Window),
        ("default_colormap", Colormap),
        ("white_pixel", c_uint32),
        ("black_pixel", c_uint32),
        ("current_input_masks", c_uint32),
        ("width_in_pixels", c_uint16),
        ("height_in_pixels", c_uint16),
        ("width_in_millimeters", c_uint16),
        ("height_in_millimeters", c_uint16),
        ("min_installed_maps", c_uint16),
        ("max_installed_maps", c_uint16),
        ("root_visual", VisualID),
        ("backing_stores", c_uint8),
        ("save_unders", c_uint8),
        ("root_depth", c_uint8),
        ("allowed_depths_len", c_uint8)
    ]


class ScreenIterator(Structure):
    _fields_ = [
        ("data", POINTER(Screen)),
        ("rem", c_int),
        ("index", c_int)
    ]


class GetWindowAttributesReply(Structure):
    _fields_ = [
        ("response_type", c_uint8),
        ("backing_store", c_uint8),
        ("sequence", c_uint16),
        ("length", c_uint32),
        ("visual", VisualID),
        ("_class", c_uint16),
        ("bit_gravity", c_uint8),
        ("win_gravity", c_uint8),
        ("backing_planes", c_uint32),
        ("backing_pixel", c_uint32),
        ("save_under", c_uint8),
        ("map_is_installed", c_uint8),
        ("map_state", c_uint8),
        ("override_redirect", c_uint8),
        ("colormap", Colormap),
        ("all_event_masks", c_uint32),
        ("your_event_masks", c_uint32),
        ("do_not_propagate_mask", c_uint16),
        ("pad0", c_uint8 * 2)
    ]


class VoidCookie(Structure):
    _fields_ = [
        ("sequence", c_uint)
    ]


# TODO?
class ImageFormat(c_int):
    pass


class ImageOrder(c_int):
    pass

Pixmap = c_uint32

COPY_FROM_PARENT = c_uint8(0)
WINDOW_CLASS_INPUT_ONLY = c_uint16(2)
CW_OVERRIDE_REDIRECT = c_uint32(512)

EVENT_MASK_KEY_PRESS = 1
EVENT_MASK_RELEASE_PRESS = 2

libxcb = cdll.LoadLibrary(find_library('xcb'))
libxcb_screensaver = cdll.LoadLibrary(find_library('xcb-screensaver'))
libxcb_image = cdll.LoadLibrary(find_library('xcb-image'))

connect = libxcb.xcb_connect
connect.argtypes = [c_char_p, POINTER(c_int)]
connect.restype = POINTER(Connection)

disconnect = libxcb.xcb_disconnect
disconnect.argtypes = [POINTER(Connection)]
disconnect.restype = None

get_setup = libxcb.xcb_get_setup
get_setup.argtypes = [POINTER(Connection)]
get_setup.restype = POINTER(Setup)

setup_roots_iterator = libxcb.xcb_setup_roots_iterator
setup_roots_iterator.argtypes = [POINTER(Setup)]
setup_roots_iterator.restype = ScreenIterator

screen_next = libxcb.xcb_screen_next
screen_next.argtypes = [POINTER(ScreenIterator)]
screen_next.restype = None

generate_id = libxcb.xcb_generate_id
generate_id.argtypes = [POINTER(Connection)]
generate_id.restype = Window

create_window = libxcb.xcb_create_window
create_window.argtypes = [
    POINTER(Connection), c_uint8, Window, Window, c_int16, c_int16,
    c_uint16, c_uint16, c_uint16, c_uint16, VisualID, c_uint32,
    POINTER(GetWindowAttributesReply)
]
create_window.restype = VoidCookie

screensaver_select_input = libxcb_screensaver.xcb_screensaver_select_input
screensaver_select_input.argtypes = [
    POINTER(Connection),
    Window,
    c_uint32
]
screensaver_select_input.restype = VoidCookie

image_create_pixmap_from_bitmap_data = \
    libxcb_image.xcb_create_pixmap_from_bitmap_data
image_create_pixmap_from_bitmap_data.restype = Pixmap
image_create_pixmap_from_bitmap_data.argtypes = [
    POINTER(Connection),     # connection
    Window,    # drawable
    c_char_p,    # data
    c_uint32,   # width
    c_uint32,   # height
    c_uint32,   # depth
    c_uint32,   # fg
    c_uint32,   # bg
    POINTER(c_uint8)   # XXX graphics context
]
