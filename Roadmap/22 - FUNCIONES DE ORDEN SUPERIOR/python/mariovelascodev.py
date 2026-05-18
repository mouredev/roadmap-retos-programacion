from datetime import datetime

def low_speak(text):
    return text.lower()

def communication(func):
    text = func("¡Hola Python!")
    print(text)

communication(low_speak)

def sum_values(value1, value2, f_add_one):
    return f_add_one(value1 + value2)

def add_one(value):
    return value + 1

print(sum_values(3, 4, add_one))

def hight_speak():
    def communication(text):
        return text.upper()
    return communication

blow = hight_speak()
print(blow("¡Hola Python!"))
print(hight_speak()("Hola mundo"))


#Extra
students = [
    {"name":"mario", "birthdate":"07-02-1990", "grades":[7,6,8,9]},
    {"name":"lucia", "birthdate":"06-08-1989", "grades":[8,4.9,6,7]},
    {"name":"tomas", "birthdate":"23-01-1995", "grades":[9.5,9,9,9]}
]

#Promedio calificaciones
def grade_average(grades):
    return sum(grades) / len(grades)

grades_average = list(map(lambda student:{
    "name": student["name"],
    "grade_average": grade_average(student["grades"])
}, students))

print(grades_average)

#Mejores estudiantes
best_student = list(map(lambda student:
    student["name"],
    filter(lambda student: grade_average(student["grades"]) >= 9, students)
))

print(best_student)

#Nacimiento
arrange_birthdate = sorted(students, key=lambda student: datetime.strptime(
    student["birthdate"], "%d-%m-%Y"), reverse=True)

print(arrange_birthdate)

#Mayor calificación
best_grade = max(map(lambda student: max(student["grades"]), students))

print(best_grade)