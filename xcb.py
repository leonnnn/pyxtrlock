#!/usr/bin/env python3

from ctypes import *

class xcb_connection(Structure):
    pass

class xcb_setup(Structure):
    pass

xcb_window = c_uint32
xcb_colormap = c_uint32
xcb_visualid = c_uint32

class xcb_screen(Structure):
    _fields_ = [
        ("root", xcb_window),
        ("default_colormap", xcb_colormap),
        ("white_pixel", c_uint32),
        ("black_pixel", c_uint32),
        ("current_input_masks", c_uint32),
        ("width_in_pixels", c_uint16),
        ("height_in_pixels", c_uint16),
        ("width_in_millimeters", c_uint16),
        ("height_in_millimeters", c_uint16),
        ("min_installed_maps", c_uint16),
        ("max_installed_maps", c_uint16),
        ("root_visual", xcb_visualid),
        ("backing_stores", c_uint8),
        ("save_unders", c_uint8),
        ("root_depth", c_uint8),
        ("allowed_depths_len", c_uint8)
    ]

class xcb_screen_iterator(Structure):
    _fields_ = [
        ("data", POINTER(xcb_screen)),
        ("rem", c_int),
        ("index", c_int)
    ]


screen_num = c_int()

libxcb = cdll.LoadLibrary('/usr/lib64/libxcb.so')
print(libxcb)

libxcb.xcb_connect.restype = POINTER(xcb_connection)
conn = libxcb.xcb_connect(None, byref(screen_num))

print('screen {}'.format(screen_num))

libxcb.xcb_get_setup.restype = POINTER(xcb_setup)
setup = libxcb.xcb_get_setup(conn)

libxcb.xcb_setup_roots_iterator.restype = xcb_screen_iterator
iter_ = libxcb.xcb_setup_roots_iterator(setup)

while screen_num.value:
    libxcb.xcb_screen_next(byref(iter_))
    screen_num.value -= 1

screen = iter_.data.contents
print(screen.white_pixel)
print(screen.width_in_pixels)
print(screen.height_in_pixels)

libxcb.xcb_disconnect(conn)
