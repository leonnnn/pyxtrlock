
import json
import base64


INTEGER_ATTRIBUTES = ["width", "height", "x_hot", "y_hot"]
COLOR_ATTRIBUTES = ["bg_color", "fg_color"]
BINARY_ATTRIBUTES = ["fg_bitmap", "bg_bitmap"]


def save_cursor(cursor, f):
    res = {}
    for attr in INTEGER_ATTRIBUTES:
        if not isinstance(cursor[attr], int):
            raise ValueError("{} must be integer".format(attr))
        res[attr] = cursor[attr]

    for attr in COLOR_ATTRIBUTES:
        if not (len(cursor[attr]) == 3 and
                all(isinstance(comp, int) and 0 <= comp <= 255
                    for comp in cursor[attr])):
            raise ValueError("invalid color specification")
        res[attr] = cursor[attr]

    for attr in BINARY_ATTRIBUTES:
        res[attr] = base64.b64encode(cursor[attr]).decode("ascii")
    json.dump(res, f, sort_keys=True)


def load_cursor(f):
    cursor = json.load(f)
    res = {}

    for attr in INTEGER_ATTRIBUTES:
        if not isinstance(cursor[attr], int):
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

    return res
