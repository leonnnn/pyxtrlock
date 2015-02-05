#!/usr/bin/python3

import pickle

fg_bitmap = bytes([0x00])
bg_bitmap = bytes([0x00])

with open("lock.pickle", "wb") as f:
    pickle.dump({
        "width": 1,
        "height": 1,
        "x_hot": 1,
        "y_hot": 1,
        "fg_bitmap": fg_bitmap,
        "bg_bitmap": bg_bitmap,
        "color_mode": "named",
        "bg_color": "steelblue3",
        "fg_color": "grey25"
    }, f)
