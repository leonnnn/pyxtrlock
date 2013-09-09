from ctypes import *
from pyxtrlock.utils import check_and_load_library

class XCBError(Exception):
    """
    Raised on XCBErrors
    """


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


class Cookie(Structure):
    _fields_ = [
        ("sequence", c_uint)
    ]

VoidCookie = Cookie
AllocNamedColorCookie = Cookie
AllocColorCookie = Cookie
GrabKeyboardCookie = Cookie
GrabPointerCookie = Cookie


# TODO?
class ImageFormat(c_int):
    pass


class ImageOrder(c_int):
    pass


class AllocNamedColorReply(Structure):
    _fields_ = [
        ("response_type", c_uint8),
        ("pad0", c_uint8),
        ("sequence", c_uint16),
        ("length", c_uint32),
        ("pixel", c_uint32),
        ("exact_red", c_uint16),
        ("exact_green", c_uint16),
        ("exact_blue", c_uint16),
        ("visual_red", c_uint16),
        ("visual_green", c_uint16),
        ("visual_blue", c_uint16)
    ]

class AllocColorReply(Structure):
    _fields_ = [
        ("response_type", c_uint8),
        ("pad0", c_uint8),
        ("sequence", c_uint16),
        ("length", c_uint32),
        ("red", c_uint16),
        ("green", c_uint16),
        ("blue", c_uint16),
        ("pad1", c_uint8 * 2),
        ("pixel", c_uint32),
    ]


class GenericError(Structure):
    _fields_ = [
        ("response_type", c_uint8),
        ("error_code", c_uint8),
        ("sequence", c_uint16),
        ("resource_id", c_uint32),
        ("minor_code", c_uint16),
        ("major_code", c_uint8),
        ("pad0", c_uint8),
        ("pad", c_uint32 * 5),
        ("full_sequence", c_uint32)
    ]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__,
                               ','.join(field + '=' + str(getattr(self, field))
                                        for field, _ in self._fields_))


class GenericID(c_uint32):
    pass


class GrabReply(Structure):
    _fields_ = [
        ("response_type", c_uint8),
        ("status", c_uint8),
        ("sequence", c_uint16),
        ("length", c_uint32)
    ]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__,
                               ','.join(str(getattr(self, field))
                                        for field, _ in self._fields_))

class GenericEvent(Structure):
    _fields_ = [
        ("response_type", c_uint8),
        ("pad0", c_uint8),
        ("sequence", c_uint16),
        ("pad", c_uint32 * 7),
        ("full_sequence", c_uint32)
    ]

Keycode = c_uint8
Timestamp = c_uint32

class KeyPressEvent(Structure):
    _fields_ = [
        ("response_type", c_uint8),
        ("detail", Keycode),
        ("sequence", c_uint16),
        ("time", Timestamp),
        ("root", Window),
        ("event", Window),
        ("child", Window),
        ("root_x", c_int16),
        ("root_y", c_int16),
        ("event_x", c_int16),
        ("event_y", c_int16),
        ("state", c_uint16),
        ("same_screen", c_uint8),
        ("pad0", c_uint8)
    ]



GrabKeyboardReply = GrabReply
GrabPointerReply = GrabReply


Pixmap = GenericID
Cursor = GenericID

COPY_FROM_PARENT = 0
WINDOW_CLASS_INPUT_ONLY = 2
CW_OVERRIDE_REDIRECT = 512
CW_EVENT_MASK = 2048

EVENT_MASK_KEY_PRESS = 1
EVENT_MASK_KEY_RELEASE = 2

CURRENT_TIME = 0
GRAB_MODE_ASYNC = 1

WINDOW_NONE = 0

KEY_PRESS = 2

libxcb = check_and_load_library('xcb')
libxcb_image = check_and_load_library('xcb-image')
libc = check_and_load_library('c')

connect = libxcb.xcb_connect
connect.argtypes = [c_char_p, POINTER(c_int)]
connect.restype = POINTER(Connection)

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
generate_id.restype = GenericID

create_window = libxcb.xcb_create_window
create_window.argtypes = [
    POINTER(Connection),    # connection
    c_uint8,    # depth
    Window,     # wid
    Window,     # parent
    c_int16,    # x
    c_int16,    # y
    c_uint16,   # width
    c_uint16,   # height
    c_uint16,   # border_width
    c_uint16,   # _class
    VisualID,   # visual
    c_uint32,   # value_mask
    POINTER(c_uint32)   # value_lis
]
create_window.restype = VoidCookie

alloc_named_color = libxcb.xcb_alloc_named_color
alloc_named_color.argtypes = [
    POINTER(Connection),    # connection
    Colormap,   # cmap
    c_uint16,   # name len
    c_char_p    # name
]
alloc_named_color.restype = AllocNamedColorCookie

alloc_color = libxcb.xcb_alloc_color
alloc_color.argtypes = [
    POINTER(Connection),    # connection
    Colormap,   # cmap
    c_uint16,   # r
    c_uint16,   # g
    c_uint16    # b
]
alloc_color.restype = AllocColorCookie

alloc_named_color_reply = libxcb.xcb_alloc_named_color_reply
alloc_named_color_reply.argtypes = [
    POINTER(Connection),    # connection
    AllocNamedColorCookie,  # cookie
    POINTER(POINTER(GenericError))  # e
]
alloc_named_color_reply.restype = POINTER(AllocNamedColorReply)

alloc_color_reply = libxcb.xcb_alloc_color_reply
alloc_color_reply.argtypes = [
    POINTER(Connection),    # connection
    AllocColorCookie,  # cookie
    POINTER(POINTER(GenericError))  # e
]
alloc_color_reply.restype = POINTER(AllocColorReply)


def alloc_named_color_sync(conn, colormap, color_string):
    """Synchronously allocate a named color

    Wrapper function for xcb_alloc_named_color and alloc_named_color_reply.

    Raises ``XCBError`` on errors.
    """
    if isinstance(color_string, str):
        color_string = color_string.encode('us-ascii')

    cookie = alloc_named_color(conn, colormap, len(color_string),
                               color_string)
    error_p = POINTER(GenericError)()
    res = alloc_named_color_reply(conn, cookie, byref(error_p))
    if error_p:
        raise XCBError(error_p.contents)

    ret = (res.contents.visual_red, res.contents.visual_green,
           res.contents.visual_blue)
    free(res)
    return ret

def alloc_color_sync(conn, colormap, r, g, b):
    """Synchronously allocate a color

    Wrapper function for xcb_alloc_color and alloc_color_reply.

    The (r, g, b) triple is in the range 0 to 255 (as opposed to
    the X protocol using the 0 to 2^16-1 range).

    Raises ``XCBError`` on xcb errors and value errors for invalid
    values of r, g, b.
    """
    if r < 0 or b < 0 or g < 0:
        raise ValueError
    if r > 255 or b > 255 or g > 255:
        raise ValueError

    r <<= 8; g <<= 8; b <<= 8

    cookie = alloc_color(conn, colormap, r, g, b)
    error_p = POINTER(GenericError)()
    res = alloc_color_reply(conn, cookie, byref(error_p))
    if error_p:
        raise XCBERror(error_p.contents)

    ret = (res.contents.red, res.contents.blue, res.contents.green)
    free(res)
    return ret

request_check = libxcb.xcb_request_check
request_check.argtypes = [POINTER(Connection), VoidCookie]
request_check.restype = POINTER(GenericError)

create_cursor_checked = libxcb.xcb_create_cursor_checked
create_cursor_checked.argtypes = [
    POINTER(Connection),    # connection
    Cursor,     # cursor
    Pixmap,     # source
    Pixmap,     # mask
    c_uint16,   # fore_red
    c_uint16,   # fore_green
    c_uint16,   # fore_blue
    c_uint16,   # back_red
    c_uint16,   # back_green
    c_uint16,   # back_blue
    c_uint16,   # x
    c_uint16    # y
]
create_cursor_checked.restype = VoidCookie


def create_cursor_sync(conn, source, mask, fg, bg, x, y):
    """
    Synchronously create a cursor, including error checks.

    Raises ``XCBError`` on failure. Otherwise returns ``Cursor``.
    """
    cursor = generate_id(conn)
    cookie = create_cursor_checked(conn, cursor, source, mask,
                                   fg[0], fg[1], fg[2], bg[0],
                                   bg[1], bg[2], x, y)
    error = request_check(conn, cookie)
    if error:
        raise XCBError(error.contents)

    return cursor

map_window = libxcb.xcb_map_window
map_window.argtypes = [POINTER(Connection), Window]
map_window.restype = VoidCookie

flush = libxcb.xcb_flush
flush.argtypes = [POINTER(Connection)]
flush.restype = c_int

grab_keyboard = libxcb.xcb_grab_keyboard
grab_keyboard.argtypes = [
    POINTER(Connection),    # connection
    c_uint8,    # owner_events
    Window,     # grab_window
    Timestamp,  # time
    c_uint8,    # pointer_mode
    c_uint8     # keyboard_mode
]
grab_keyboard.restype = GrabKeyboardCookie

grab_keyboard_reply = libxcb.xcb_grab_keyboard_reply
grab_keyboard_reply.argtypes = [
    POINTER(Connection),    # connection
    GrabKeyboardCookie,     # cookie,
    POINTER(POINTER(GenericError))  # e
]
grab_keyboard_reply.restype = POINTER(GrabKeyboardReply)


def grab_keyboard_sync(conn, owner_events, grab_window, time, ptr_mode,
                       kbd_mode):
    """
    Synchronously grab the keyboard.

    Wrapper function for grab_pointer and grab_pointer_reply. Returns
    the status field from the reply. Raises ``XCBError`` on error.
    """
    owner_events = 1 if owner_events else 0

    cookie = grab_keyboard(conn, owner_events, grab_window, time, ptr_mode,
                           kbd_mode)
    error_p = POINTER(GenericError)()
    kbd_grab = grab_keyboard_reply(conn, cookie, byref(error_p))

    if error_p:
        raise XCBError(error_p.contents)
    status = kbd_grab.contents.status
    free(kbd_grab)
    return status


grab_pointer = libxcb.xcb_grab_pointer
grab_pointer.argtypes = [
    POINTER(Connection),    # connection
    c_uint8,    # owner_events
    Window,     # grab_window
    c_uint16,   # event_mask
    c_uint8,    # pointer_mode
    c_uint8,    # keyboard_mode
    Window,     # confine_to
    Cursor,     # cursor
    Timestamp  # time
]
grab_pointer.restype = GrabPointerCookie

grab_pointer_reply = libxcb.xcb_grab_pointer_reply
grab_pointer_reply.argtypes = [
    POINTER(Connection),    # connection
    GrabPointerCookie,     # cookie,
    POINTER(POINTER(GenericError))  # e
]
grab_pointer_reply.restype = POINTER(GrabPointerReply)

# constants to interpret grab results
GrabSuccess = 0
AlreadyGrabbed = 1
GrabInvalidTime = 2
GrabNotViewable = 3
GrabFrozen = 4

def grab_pointer_sync(conn, owner_events, window, event_mask, ptr_mode,
                      kbd_mode, confine_to, cursor, timestamp):
    """
    Synchronously grab the pointing device.

    Wrapper function for ``grab_pointer`` and ``grab_pointer_reply``.
    Raises ``XCBError`` on error. Otherwise returns the result of
    ``grab_pointer_reply``
    """
    owner_events = 1 if owner_events else 0
    cookie = grab_pointer(conn, owner_events, window, event_mask, ptr_mode,
                          kbd_mode, confine_to, cursor, timestamp)
    error_p = POINTER(GenericError)()
    ptr_grab = grab_pointer_reply(conn, cookie, byref(error_p))
    if error_p:
        raise XCBError(error_p.contents)
    status = ptr_grab.contents.status
    free(ptr_grab)
    return status

wait_for_event_ = libxcb.xcb_wait_for_event
wait_for_event_.argtypes = [POINTER(Connection)]
wait_for_event_.restype = POINTER(GenericEvent)

free = libc.free
free.argtypes = [c_void_p]
free.restype = None

class FreeWrapper(object):

    def __init__(self, pointer):
        self.pointer = pointer

    def __enter__(self):
        return self.pointer

    def __exit__(self, etype, evalue, traceback):
        free(self.pointer)


def wait_for_event(conn):
    return FreeWrapper(wait_for_event_(conn))

# xcb_image
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
