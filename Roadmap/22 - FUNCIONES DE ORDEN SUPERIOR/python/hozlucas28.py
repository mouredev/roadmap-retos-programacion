# pylint: disable=pointless-string-statement,missing-function-docstring,missing-module-docstring

from typing import TypeVar, Callable, TypedDict
from datetime import date


"""
    Higher order functions (HOF)...
"""

print("Higher order functions (HOF)...")

T = TypeVar("T")


def to_filtered(*, array: list[T], func: Callable[[T], bool]) -> list[T]:
    sorted_array: list[T] = []

    for element in array:
        if func(element):
            sorted_array.append(element)

    return sorted_array


numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\n{numbers=}")

even_numbers: list[int] = to_filtered(
    array=numbers, func=lambda number: number % 2 == 0
)
print(f"\n{even_numbers=}")

odd_numbers: list[int] = to_filtered(array=numbers, func=lambda number: number % 2 != 0)
print(f"\n{odd_numbers=}")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)


"""
    Additional challenge...
"""

print("Additional challenge...\n")

Student = TypedDict(
    "Student",
    {
        "born_date": date,
        "name": str,
        "qualifications": list[float],
    },
)

type K = int | float


def get_average(*_numbers: K) -> K:
    total: K = _numbers[0]
    for number in _numbers[1:]:
        total += number

    return total / len(_numbers)


students: list[Student] = [
    {
        "born_date": date(year=2000, month=1, day=1),
        "name": "John Doe",
        "qualifications": [8.5, 9.0, 7.5],
    },
    {
        "born_date": date(year=1999, month=5, day=10),
        "name": "Jane Smith",
        "qualifications": [9.5, 9.5, 9.0],
    },
    {
        "born_date": date(year=2001, month=3, day=15),
        "name": "Michael Johnson",
        "qualifications": [7.0, 8.0, 6.5],
    },
    {
        "born_date": date(year=2002, month=7, day=20),
        "name": "Emily Davis",
        "qualifications": [9.0, 9.5, 8.5],
    },
    {
        "born_date": date(year=2000, month=9, day=5),
        "name": "David Wilson",
        "qualifications": [8.0, 7.5, 8.5],
    },
    {
        "born_date": date(year=1999, month=12, day=25),
        "name": "Olivia Martinez",
        "qualifications": [9.5, 9.0, 9.5],
    },
    {
        "born_date": date(year=2001, month=8, day=12),
        "name": "Sophia Anderson",
        "qualifications": [7.5, 8.5, 7.0],
    },
    {
        "born_date": date(year=2002, month=4, day=30),
        "name": "Daniel Thompson",
        "qualifications": [9.0, 8.0, 9.0],
    },
]

print("Students...\n")
for student in students:
    print(f"{student['name']} / {student['born_date']} / {student['qualifications']}")

students_with_name_and_average_qualification = list(
    map(
        lambda student: {
            "name": student["name"],
            "average_qualification": get_average(*student["qualifications"]),
        },
        students,
    )
)

print("\nStudents with name and average qualification...\n")
for student in students_with_name_and_average_qualification:
    print(f"{student['name']} / {student['average_qualification']:.2f}")

students_with_average_qualification_more_than_nine: list[Student] = to_filtered(
    array=students, func=lambda student: get_average(*student["qualifications"]) >= 9
)

print("\nStudents with an average qualification more than nine...\n")
for student in students_with_average_qualification_more_than_nine:
    print(f"{student['name']} / {student['born_date']} / {student['qualifications']}")


sorted_students_by_born_date: list[Student] = sorted(
    students, key=lambda student: student["born_date"], reverse=True
)

print("\nSorted students by born date (youngest to oldest)...\n")
for student in sorted_students_by_born_date:
    print(f"{student['name']} / {student['born_date']} / {student['qualifications']}")

students_with_name_and_best_qualification = list(
    map(
        lambda student: {
            "name": student["name"],
            "best_qualification": max(*student["qualifications"]),
        },
        students,
    )
)

print("\nStudents with name and best qualification...\n")
for student in students_with_name_and_best_qualification:
    print(f"{student['name']} / {student['best_qualification']}")
