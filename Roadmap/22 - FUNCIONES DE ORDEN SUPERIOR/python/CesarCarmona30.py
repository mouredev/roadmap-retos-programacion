from functools import reduce
from datetime import datetime

from numpy import number

def apply_func(func, arg):
  return func(arg)

print(apply_func(len, "omnia mea mecum porto"))

def apply_multiplier(n):
  def multiplier(x):
    return x * n
  return multiplier

multiplier = apply_multiplier(2)
print(multiplier(5))
print(apply_multiplier(3)(2))

def apply_double(n):
  return n * 2

numbers = [1, 2, 3, 4, 5]

print(list(map(apply_double, numbers)))

def is_even(n):
  return n % 2 == 0

print(list(filter(is_even, numbers)))

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

def sum_values(x, y):
  return x + y

print(reduce(sum_values, numbers))


'''
  EXTRA
'''

students = [
  {"name": "Cesar", "birthdate": "30-07-2004", "grades": [10, 10, 10, 9, 9, 6]},
  {"name": "Alex", "birthdate": "06-04-2002", "grades": [10, 9, 9, 8, 10, 7]},
  {"name": "Diego", "birthdate": "10-01-2003", "grades": [8, 7, 10, 9, 6, 6]},
]

def average(grades):
  return sum(grades) / len(grades)

print(
  list(map(lambda student: {
    "name": student["name"],
    "average": average(student["grades"])}, students)
  )
)

print(
  list(
    map(lambda student:
        student["name"],
        filter(lambda student: average(student["grades"]) >= 9, students)
        )
  )
)

print(sorted(students, key=lambda student: datetime.strptime(
  student["birthdate"], "%d-%m-%Y")))

print(max(map(lambda student: max(student["grades"]), students)))