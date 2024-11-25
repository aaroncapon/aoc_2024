"""
Submit answers
"""

import typing

import aocd


def submit(day: int, submit_args: list[str]) -> None:
    """Submit answers"""

    allowed_parts = typing.Literal["a", "b"]

    part = typing.cast(allowed_parts, submit_args[0])

    aocd.submit(submit_args[1], part=part, day=day, year=2024)
