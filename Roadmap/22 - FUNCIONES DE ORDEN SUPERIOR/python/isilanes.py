from datetime import datetime


def main():
    print("===== MAIN =====")

    def add(a: int, b: int) -> int:
        return a + b

    def subtract(a: int, b: int) -> int:
        return a - b

    def higher_order_selector(operation: str) -> callable:
        return {
            "plus": add,
            "minus": subtract,
        }.get(operation, lambda a, b: None)

    func = higher_order_selector("plus")
    assert func(1, 1) == 2
    func = higher_order_selector("minus")
    assert func(3, 4) == -1
    func = higher_order_selector("petecander")
    assert func(3, 4) is None
    print("Función main() completada con éxito.")


def extra():
    print("\n===== EXTRA =====")

    class Student:
        def __init__(self, name: str, birth: datetime, grades: list[int]):
            self.name = name
            self.birth = birth
            self.grades = grades

        def __str__(self) -> str:
            return f"{self.name}: birth_date={self.birth}, grades={self.grades}"

    def average(values: list[float]) -> float | None:
        return sum(values)/len(values) if values else None

    students = [
        Student(name="John", birth=datetime(2000, 1, 1), grades=[10, 10, 9]),
        Student(name="Amelie", birth=datetime(1999, 12, 1), grades=[10, 10, 9.5]),
        Student(name="Brais", birth=datetime(1750, 2, 1), grades=[1, 1, 9.8]),
        Student(name="isilanes", birth=datetime(666, 12, 31), grades=[]),
    ]

    def grade_averages(student_list: list[Student]) -> None:
        print("Estudiantes ordenados for nombre y notas, de forma ascendente (yo no hago las reglas):")

        data = [(s.name, average(s.grades), s) for s in student_list if s.grades]

        for fields in sorted(data):
            print(*fields)

    def best_students(student_list: list[Student]) -> None:
        print("Mejores estudiantes (no se especifica que ordenados):")

        data = [s.name for s in student_list if average(s.grades) and average(s.grades) >= 9]

        for line in data:
            print(line)

    def students_by_age(student_list: list[Student]) -> None:
        print("Estudiantes por edad:")

        data = [(s.birth, s) for s in student_list if s.birth]

        for _, s in sorted(data, reverse=True):
            print(s)

    def highest_grade(student_list: list[Student]) -> None:
        print("Mayor calificación (no se pide saber de quién es, y no se especifica que sea la media):")

        max_grade = 0
        for student in student_list:
            if not student.grades:
                continue
            max_grade = max(max_grade, max(student.grades))

        print(max_grade)

    def higher_order_callback_selector(operation: str) -> callable:
        f = {
            "promedio": grade_averages,
            "mejores": best_students,
            "nacimiento": students_by_age,
            "mayor_calificación": highest_grade,
        }.get(operation)

        if f is None:
            raise ValueError(f"Operation '{operation}' is not valid.")

        return f

    for action in ("promedio", "mejores", "nacimiento", "mayor_calificación"):
        higher_order_callback_selector(action)(students)

    print("Función extra() completada con éxito.")


if __name__ == "__main__":
    main()
    extra()
