#!/usr/bin/python3

import pickle
import sys

data = None
for arg in sys.argv[1:]:
    with open(arg, "rb") as f:
        data = pickle.load(f, encoding='latin1')
    if data is not None:
        data["fg_bitmap"] = bytes(data["fg_bitmap"], encoding='latin1')
        data["bg_bitmap"] = bytes(data["bg_bitmap"], encoding='latin1')
        with open(arg, "wb") as f:
            pickle.dump(data, f)
