from datetime import datetime

def processOperation(a, b, operation):
    return operation(a, b)

def addition(a, b):
    return a + b

print(processOperation(4, 10, addition))

### Ejercicio Extra ###

students = [
    {"name": "Isaac", "birthdate": "2001-10-21", "notes": [10, 10, 10]},
    {"name": "Marco", "birthdate": "2001-05-02", "notes": [6, 8.9, 7.6]},
    {"name": "Felix", "birthdate": "2001-06-11", "notes": [9.2, 9.8, 10]},
    {"name": "Jenni", "birthdate": "2001-03-28", "notes": [8.5, 8.9, 7]},
    {"name": "Karen", "birthdate": "2001-01-13", "notes": [8.2, 8.8, 8]},
]

print(students)

def average(notes):
    return sum(notes) / len(notes)

averages = list(map(lambda student: {
    "name": student["name"],
    "average": round(average(student["notes"]), 1)
}, students))
print(averages)

best_students = list(filter(lambda student: student["average"] >= 9, averages))
print(best_students)

ordered_students = sorted(students, key=lambda student: datetime.strptime(student["birthdate"], "%Y-%m-%d"), reverse=True)
for student in ordered_students:
    print(f"{student["name"]}, {student["birthdate"]}")

best_average = max(averages, key=lambda student: student["average"])
print(best_average)