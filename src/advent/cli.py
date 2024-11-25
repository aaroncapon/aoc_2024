"""
Entry point for CLI.
"""

import sys

from advent import main


def cli() -> None:
    """
    CLI entry point.
    """

    sys.exit(main.run(**vars(main.parse_args())))
