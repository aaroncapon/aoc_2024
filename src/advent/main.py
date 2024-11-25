"""
Main
"""

import argparse
import importlib

import rich_argparse


def parse_args() -> argparse.Namespace:
    """Get CLI args"""

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Advent of code 2024",
        prog="advent",
        formatter_class=rich_argparse.RawDescriptionRichHelpFormatter,
    )

    parser.add_argument("day", help="Run code from specified day", type=int)

    parser.add_argument(
        "--submit",
        nargs=2,
        help="Sumbit your answer for the specified day. Specifiy level and answer. "
        "E.g., a 42",
        default=None,
    )

    return parser.parse_args()


def run(args: argparse.Namespace) -> int:
    """main"""

    which_day: str = f"{args.day:02d}"

    try:
        day = importlib.import_module("advent.day" + which_day)
        try:
            return int(day.run(args.submit))
        except Exception as error:  # pylint: disable=broad-exception-caught
            print(f"{error}")
            return 98
    except ModuleNotFoundError:
        print("ERROR: Day not yet implemented")
        return 1
    except Exception as error:  # pylint: disable=broad-exception-caught
        print(f"{error}")
        return 99


if __name__ == "__main__":
    run(parse_args())
