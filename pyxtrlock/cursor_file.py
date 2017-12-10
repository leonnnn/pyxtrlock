
import json
import base64


INTEGER_ATTRIBUTES = ["width", "height", "x_hot", "y_hot"]
COLOR_ATTRIBUTES = ["bg_color", "fg_color"]
BINARY_ATTRIBUTES = ["fg_bitmap", "bg_bitmap"]

MAX_CURSOR_SIZE = 512


def _check_size(w, h, data):
    pitch = (w + 7) // 8
    size = pitch * h
    if len(data) < size:
        raise ValueError("invalid cursor file: bitmap data is too small")


def save_cursor(cursor, f):
    res = {}
    for attr in INTEGER_ATTRIBUTES:
        if not (isinstance(cursor[attr], int) and
                0 <= cursor[attr] <= MAX_CURSOR_SIZE):
            raise ValueError("{} must be integer".format(attr))
        res[attr] = cursor[attr]

    for attr in COLOR_ATTRIBUTES:
        if not (len(cursor[attr]) == 3 and
                all(isinstance(comp, int) and 0 <= comp <= 255
                    for comp in cursor[attr])):
            raise ValueError("invalid color specification")
        res[attr] = cursor[attr]

    _check_size(cursor["width"], cursor["height"], cursor["fg_bitmap"])
    _check_size(cursor["width"], cursor["height"], cursor["bg_bitmap"])

    for attr in BINARY_ATTRIBUTES:
        res[attr] = base64.b64encode(cursor[attr]).decode("ascii")

    json.dump(res, f, sort_keys=True)


def load_cursor(f):
    cursor = json.load(f)
    res = {}

    for attr in INTEGER_ATTRIBUTES:
        if not (isinstance(cursor[attr], int) and
                0 <= cursor[attr] <= MAX_CURSOR_SIZE):
            raise ValueError("{} must be integer".format(attr))
        res[attr] = cursor[attr]

    for attr in COLOR_ATTRIBUTES:
        if not (len(cursor[attr]) == 3 and
                all(isinstance(comp, int) and 0 <= comp <= 255
                    for comp in cursor[attr])):
            raise ValueError("invalid color specification")
        res[attr] = tuple(cursor[attr])

    for attr in BINARY_ATTRIBUTES:
        res[attr] = base64.b64decode(cursor[attr])

    _check_size(res["width"], res["height"], res["fg_bitmap"])
    _check_size(res["width"], res["height"], res["bg_bitmap"])

    return res
