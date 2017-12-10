
import sys


def panic(*message_parts, exit_code=1):
    """Print an error message to stderr and exit"""
    print("pyxtrlock:", *message_parts, file=sys.stderr)
    sys.exit(exit_code)
