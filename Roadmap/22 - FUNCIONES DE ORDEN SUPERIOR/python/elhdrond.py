from datetime import datetime
from functools import reduce

"""
    HIGHER-ORDER FUNCTIONS
"""


# Function as argument


def apply_func(func, x):
    return func(x)


print(apply_func(len, "Elhdrond"))


# Function as return value


def apply_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier


multiplier = apply_multiplier(2)
print(multiplier(5))
print(apply_multiplier(3)(2))


"""
    SYSTEM HIGHER-ORDER FUNCTIONS
"""

numbers = [1, 3, 4, 2, 5]


# map()


def apply_double(n):
    return n * 2


print(list(map(apply_double, numbers)))


# filter()


def is_even(n):
    return n % 2 == 0


print(list(filter(is_even, numbers)))


# sorted()

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce()


def sum_values(x, y):
    return x + y


print(reduce(sum_values, numbers))

"""
    EXTRA EXERCISE
"""

students = [
    {
        "name": "Luke Skywalker",
        "birthdate": "24-05-1977",
        "grades": [9.5, 8.0, 7.5, 10.0],
    },
    {"name": "Leia Organa", "birthdate": "25-05-1977", "grades": [9.0, 9.5, 8.5, 9.8]},
    {"name": "Han Solo", "birthdate": "29-07-1944", "grades": [6.5, 7.0, 5.5, 8.0]},
    {
        "name": "Rey Skywalker",
        "birthdate": "15-12-1999",
        "grades": [9.2, 9.8, 10.0, 9.5],
    },
    {"name": "Finn", "birthdate": "11-01-1995", "grades": [7.0, 6.5, 8.0, 7.5]},
]


def validate_grades(grades: list[float]) -> list[float]:
    return [g for g in grades if 0 <= g <= 10]


def average(grades: list[float]) -> float:
    valid = validate_grades(grades)
    return sum(valid) / len(valid) if valid else 0.0


# Average grades per student
print("Average grades:")
print(
    list(
        map(
            lambda s: {"name": s["name"], "average": round(average(s["grades"]), 2)},
            students,
        )
    )
)

# Top students (average >= 9)
print("\nTop students (average >= 9):")
print(
    list(
        map(
            lambda s: s["name"],
            filter(lambda s: average(s["grades"]) >= 9, students),
        )
    )
)

# Students sorted by age (youngest first)
print("\nStudents sorted by age (youngest first):")
print(
    list(
        map(
            lambda s: s["name"],
            sorted(
                students,
                key=lambda s: datetime.strptime(s["birthdate"], "%d-%m-%Y"),
                reverse=True,
            ),
        )
    )
)

# Highest grade across all students
print("\nHighest grade overall:")
print(max(map(lambda s: max(validate_grades(s["grades"])), students)))
