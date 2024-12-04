"""
Day 2
"""

import aocd


def is_valid(in_list: list[int]) -> bool:
    """is the line valid"""

    zipped = list(zip(in_list, in_list[1:]))
    if any(abs(x - y) > 3 for x, y in zipped):
        return False
    if all(x < y for x, y in zipped) or all(x > y for x, y in zipped):
        return True

    return False


def problem_one(data: list[str]) -> int:
    """problem one"""

    return sum((1 for x in data if is_valid([int(x) for x in x.split()])))


def problem_two(data: list[str]) -> int:
    """problem two"""

    ret_val: int = 0

    for vals in data:
        vals_ints: list[int] = [int(x) for x in vals.split()]
        if is_valid(vals_ints):
            ret_val += 1
            continue
        for pos in range(len(vals_ints)):
            limited_list: list[int] = vals_ints[:]
            limited_list.pop(pos)
            if is_valid(limited_list):
                ret_val += 1
                break

    return ret_val


def run() -> None:
    """Print day02 answers"""

    data: list[str] = aocd.get_data(day=2, year=2024).split("\n")

    print(f"Answer one: {problem_one(data)}")
    print(f"Answer two: {problem_two(data)}")
