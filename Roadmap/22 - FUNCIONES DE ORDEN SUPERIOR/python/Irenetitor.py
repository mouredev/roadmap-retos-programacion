from functools import reduce
from datetime import datetime

#Exercise

def winner(name):
    return f"The winner is {name}"

def candidate_winner(name, func):     #Passing a function as an argument
    return func(name)

print(candidate_winner("Samuel", winner))



def division(n):
    def operation(x):
        return n // x         #Returning a function
    return operation

half = division(12)

print(half(2))
print(division(16)(4))


#------------------------------
#Built-in Higher-Order Functions

nums = [1, 2, 3, 4]

result = map(lambda x: x * 2, nums)    #map(function, iterable)
print(list(result))


nums = [2, 3, 4, 6, 7, 9, 12]

odds = filter(lambda x: x % 3 == 0, nums)     #filter(function, iterable)
print(list(odds))


nums = [3, 6, 8, 5]

total = reduce(lambda a, b: a + b, nums)      #reduce(function, iterable)
print(total)

sorted(["Irene", "Alex", "Michael"], key=len)  #sorted() (if you pass a function)

#Extra Exercise

students = [
    {"name": "Lola", "birthday": "23-05-1997", "grades": [7, 4.7, 6, 9]},
    {"name": "Rose", "birthday": "06-07-1993", "grades": [6, 5.7, 7.7, 3.9]},
    {"name": "Valentino", "birthday": "12-02-1995", "grades": [8.3, 6.7, 4.8, 10]},
    {"name": "Irene", "birthday": "12-02-1995", "grades": [8.3, 9.7, 9.8, 10]},
    {"name": "Galileo", "birthday": "12-02-1995", "grades": [6, 8.9, 7.8, 9.6]},
    {"name": "Kate", "birthday": "12-02-1995", "grades": [9, 7, 10, 10]}
]

def average(grades):
    return sum(grades) / len(grades)

#Average
print(
    list(map(lambda student: {
        "name": student["name"],
        "average": average(student["grades"])}, students)
    )
)

#Best students
print(
    list(
        map(lambda student: 
            student["name"],
            filter(lambda student: average(student["grades"]) >= 9, students)
            )
        )
    )

#List of students from youngest to oldest
print(
    list(
        map(lambda student: 
            student["name"],
            sorted(students, key=lambda student: datetime.strptime(
            student["birthday"], "%d-%m-%Y"), reverse=True)))
)

#Highest grade

print(
    max(map(lambda student: max(student["grades"]), students))
)