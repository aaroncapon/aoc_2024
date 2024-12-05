"""
Day 3
"""

import re

import aocd


def problem_one(data: str) -> int:
    """problem one"""

    return sum(
        (int(x[0]) * int(x[1]) for x in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data))
    )


def problem_two(data: str) -> int:
    """problem two"""

    ret_val: int = 0

    ignore: bool = False
    for val in re.findall(r"(mul)\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", data):
        if "mul" in val[0] and ignore is False:
            ret_val += int(val[1]) * int(val[2])
        elif "do" in val[3]:
            ignore = False
        elif "don't" in val[4]:
            ignore = True

    return ret_val


def run() -> None:
    """Print day02 answers"""

    data: str = aocd.get_data(day=3, year=2024)

    print(f"Answer one: {problem_one(data)}")
    print(f"Answer two: {problem_two(data)}")
