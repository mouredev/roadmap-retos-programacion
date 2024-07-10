# higher-order functions
import time
from datetime import datetime


def sum_nums(num_1: int, num_2: int) -> int:
    return num_1 + num_2


def higher_order_function(num_1: int, num_2: int, func):
    start = time.time()
    result = func(num_1, num_2)
    end = time.time()
    print(f"{func.__name__}({num_1}, {num_2}) = {result}. Function time: {end - start:.2f}")
    return result


print(higher_order_function(1, 2, sum_nums))

# EXTRA

students = [
    {
        "name": "ggilperez",
        "birthdate": "08-04-1993",
        "grades": [6, 7, 5, 8, 5, 9]
    },
    {
        "name": "mouredev",
        "birthdate": "29-04-1987",
        "grades": [9, 9, 9, 10, 8, 9]
    },
    {
        "name": "midudev",
        "birthdate": "13-07-1989",
        "grades": [8, 7, 9, 10, 8, 7]
    }
]


def average(grades: list[int]) -> float:
    return round(sum(grades) / len(grades), 2)


# Average
print(list(map(lambda x: {"name": x["name"], "average": average(x["grades"])}, students)))

# Best above 9
print([x["name"] for x in list(filter(lambda x: average(x["grades"]) >= 9, students))])

# Sort by birthdate
print(sorted(students, key=lambda x: datetime.strptime(x["birthdate"], "%d-%m-%Y"), reverse=True))

# Best grade
print(max(map(lambda x: max(x["grades"]), students)))