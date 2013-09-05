
import sys
import os

data_dir = os.path.join(sys.prefix, "share/pyxtrlock")

def panic(message, exit_code=1):
    """Print an error message to stderr and exit"""
    print(message, file=sys.stderr)
    sys.exit(exit_code)
