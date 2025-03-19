import os

MONTHS = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]


def show_menu():
    print("\nPlanificador de objetivos:")
    print("1. Añadir objetivo")
    print("2. Calcular el plan detallado")
    print("3. Guardar la planificación")
    print("4. Salir")


class Goal:

    def __init__(self, goal_name: str, amount: int, units: str, limit: int):
        self.goal_name = goal_name
        self.amount = amount
        self.units = units
        self.limit = limit


def request_goal() -> Goal:

    goal_name = input("Meta: ")

    while True:
        try:
            amount = int(input("Cantidad: "))
            if amount <= 0:
                print("La cantidad debe ser un número positivo.")
                continue
            break
        except:
            print("Por favor, introduce un número entero válido.")

    units = input("Unidades: ")

    while True:
        try:
            limit = int(input("Plazo en meses (máximo 12): "))
            if limit <= 0 or limit > len(MONTHS):
                print("El plazo debe ser un número entre 1 y 12 (meses).")
                continue
            break
        except:
            print("Por favor, introduce un número entre 1 y 12 (meses).")

    return Goal(goal_name, amount, units, limit)


def calculate_detailed_plan(goals: list[Goal]) -> dict:

    plan = {month: [] for month in range(1, len(MONTHS) + 1)}

    for goal in goals:
        month_amount = goal.amount / goal.limit

        for month in range(1, goal.limit + 1):
            plan[month].append(
                Goal(goal.goal_name, round(month_amount, 2), goal.units, goal.amount))

    return plan


def show_detailed_plan(plan: dict):

    for month in range(1, len(MONTHS) + 1):

        if not plan[month]:
            # No hay objetivos en este mes
            break

        print(f"\n{MONTHS[month - 1]}: ")

        for index, goal in enumerate(plan[month], start=1):
            print(
                f"[ ] {index}. {goal.goal_name} ({
                    goal.amount} {goal.units}/mes). Total: {goal.limit}.")


def save_detailed_plan(plan: dict):

    file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "plan.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Plan detallado\n")

        for month in range(1, len(MONTHS) + 1):

            if not plan[month]:
                # No hay objetivos en este mes
                break

            file.write(f"\n{MONTHS[month - 1]}:\n")

            for index, goal in enumerate(plan[month], start=1):
                file.write(
                    f"[ ] {index}. {goal.goal_name} ({
                        goal.amount} {goal.units}/mes). Total: {goal.limit}.\n")

    print(f"Plan guardado con éxito en {file_path}")


goals = []

while True:

    show_menu()

    option = input("Elige una opción: ")

    if option == "1":
        if len(goals) >= 10:
            print("Has alcanzado el número máximo de objetivos (10).")
        else:
            goal = request_goal()
            goals.append(goal)
            print("Objetivo añadido con éxito.")

    elif option == "2":
        if len(goals) == 0:
            print("No hay objetivos añadidos.")
        else:
            plan = calculate_detailed_plan(goals)
            show_detailed_plan(plan)

    elif option == "3":
        if len(goals) == 0:
            print("No hay objetivos para guardar.")
        else:
            plan = calculate_detailed_plan(goals)
            save_detailed_plan(plan)

    elif option == "4":
        print("Saliendo del planificador.")
        break
    else:
        print("Opción inválida. Elige una opción entre 1 y 4.")
