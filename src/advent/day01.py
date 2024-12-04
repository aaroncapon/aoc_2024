"""
Day 1
"""

import aocd


def problem_one(list1: list[int], list2: list[int]) -> int:
    """problem one"""

    diff: int = 0

    list1 = sorted(list1)
    list2 = sorted(list2)

    for vals in zip(list1, list2):
        diff += abs(vals[0] - vals[1])

    return diff


def problem_two(list1: list[int], list2: list[int]) -> int:
    """problem two"""

    ret_val: int = 0

    for val1 in list1:
        ret_val += val1 * list2.count(val1)

    return ret_val


def run() -> None:
    """Print day01 answers"""

    data: list[str] = aocd.get_data(day=1, year=2024).split("\n")

    list1: list[int] = []
    list2: list[int] = []
    for value in data:
        vals = value.split()
        list1.append(int(vals[0]))
        list2.append(int(vals[1]))

    print(f"Answer one: {problem_one(list1, list2)}")
    print(f"Answer two: {problem_two(list1, list2)}")
