"""
Day 4
"""

import aocd
import numpy
import numpy.typing as npt


def problem_one(data: npt.NDArray[numpy.str_]) -> int:
    """problem one"""

    to_find: tuple[str, str] = ("XMAS", "SAMX")

    num_xmas: int = 0
    i_max: int = data.shape[0] - 3
    j_max: int = data.shape[1] - 3
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if i < i_max:
                if "".join(data[i : i + 4, j : j + 1].flatten()) in to_find:
                    num_xmas += 1
            if j < j_max:
                if "".join(data[i : i + 1, j : j + 4].flatten()) in to_find:
                    num_xmas += 1
            if i < i_max and j < j_max:
                square: npt.NDArray[numpy.str_] = data[i : i + 4, j : j + 4]
                if "".join(square.diagonal().flatten()) in to_find:
                    num_xmas += 1
                if "".join(numpy.flipud(square).diagonal().flatten()) in to_find:
                    num_xmas += 1

    return num_xmas


def problem_two(data: npt.NDArray[numpy.str_]) -> int:
    """problem two"""

    to_find: tuple[str, str] = ("MAS", "SAM")

    num_mas: int = 0
    for i in range(data.shape[0] - 2):
        for j in range(data.shape[1] - 2):
            diag1 = "".join(data[i : i + 3, j : j + 3].diagonal().flatten())
            diag2 = "".join(
                numpy.flipud(data[i : i + 3, j : j + 3]).diagonal().flatten()
            )
            if diag1 in to_find and diag2 in to_find:
                num_mas += 1

    return num_mas


def run() -> None:
    """Print day02 answers"""

    data: npt.NDArray[numpy.str_] = numpy.array(
        [list(x) for x in aocd.get_data(day=4, year=2024).split()], dtype=str
    )

    print(f"Answer one: {problem_one(data)}")
    print(f"Answer two: {problem_two(data)}")
