from datetime import datetime


class Student:
    name: str
    birthday: datetime
    marks: list[int]

    def __init__(self, name, birthday, marks):
        self.name = name
        self.birthday = birthday
        self.marks = marks


def operation(students: list[Student], operation):
    try:
        for student in students:
            check_marks(student.marks)

        return operation(students)
    except ValueError as e:
        return e


def average_grades(students):
    average_grades = dict()

    for student in students:
        marks = student.marks

        average = sum(marks) / len(marks)

        average_grades[f"{student.name}"] = average

    return average_grades


def best_students(students: list[Student]):
    average = average_grades(students)
    best_students = []

    for name, mark in average.items():
        if mark >= 9:
            best_students.append(name)

    return best_students


def order_by_birth(students: list[Student]):
    ordered_students = sorted(students, key=lambda student: student.birthday, reverse=True)
    ordered_students_list = []

    for student in ordered_students:
        ordered_students_list.append(student.name)

    return ordered_students_list


def get_highest_mark(students: list[Student]):
    highest_marks = max(student.marks for student in students)
    highest_mark = max(highest_marks)

    return highest_mark


def check_marks(marks: list[int]):
    for mark in marks:
        if not 0 <= mark <= 10:
            raise ValueError("Una calificación debe estar comprendida entre 0 y 10")


def main():
    student1 = Student("Pepe", datetime(1996, 3, 10), [10, 9, 8.75])
    student2 = Student("Ana", datetime(1996, 6, 12), [5, 4, 6])
    student3 = Student("Juan", datetime(1996, 5, 23), [8, 7, 3])

    print(operation([student1, student2, student3], average_grades))
    print(operation([student1, student2, student3], best_students))
    print(operation([student1, student2, student3], order_by_birth))
    print(operation([student1, student2, student3], get_highest_mark))


if __name__ == '__main__':
    main()
