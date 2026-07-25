""" /*
 * EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 * 
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado 
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *   
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)
 */ """

import os

MONTHS = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def show_menu():

    print("\nPlanificador de objetivos")
    print("1. Añadir objetivo.")
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
            print("Introduce un número entero válido.")

    units = input("Unidades: ")

    while True:
        try:
            limit = int(input("Plazo en meses (máx. 12): "))
            if limit <= 0 or limit > len(MONTHS):
                print("El plazo debe ser de 1 a 12 meses.")
                continue
            break
        except:
            print("Introduce un número entre 1 y 12.")

    return Goal(goal_name, amount, units, limit)

def calculate_detailed_plan(goals: list[Goal]) -> dict:

    plan = {month: [] for month in range(1, len(MONTHS) + 1)}

    for goal in goals:

        month_amount = goal.amount / goal.limit

        for month in range(1, goal.limit + 1):

            plan[month].append(Goal(goal.goal_name, round(month_amount, 1), goal.units, goal.amount))

    return plan

def show_detailed_plan(plan: dict):

    for month in range(1, len(MONTHS) + 1):

        if not plan[month]:
            break
        
        print(f"\n{MONTHS[month - 1]}: ")

        for index, goal in enumerate(plan[month], start=1):
            print(f"[ ] {index}. {goal.goal_name} ({goal.amount} {goal.units}/mes). Total: {goal.limit}.")

def save_detailed_plan(plan: dict):

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plan.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Plan detallado")

        for month in range(1, len(MONTHS) + 1):

            if not plan[month]:
                break
            
            file.write(f"\n{MONTHS[month - 1]}:\n")

            for index, goal in enumerate(plan[month], start=1):
                file.write(f"[ ] {index}. {goal.goal_name} ({goal.amount} {goal.units}/mes). Total: {goal.limit}.\n")

    print(f"Plan guardado con éxito en {file_path}")




goals = []

while True:

    show_menu()

    option = input("\nElige una opción: ")

    if option == "1":
        if len(goals) >= 10:
            print("Has alcanzado el número máximo de objetivos (10).")
            continue
        else:
            goal = request_goal()
            goals.append(goal)
            print("Objetivo añadido correctamente.")
            continue

    if option == "2":
        if len(goals) == 0:
            print("No hay objetivos añadidos.")
            continue
        else:
            plan = calculate_detailed_plan(goals)
            show_detailed_plan(plan)
            continue

    if option == "3":
        if len(goals) == 0:
            print("No hay objetivos para guardar.")
            continue
        else:
            plan = calculate_detailed_plan(goals)
            save_detailed_plan(plan)

    if option == "4":
        print("Saliendo del planificador.")
        break
    else:
        print("Opción no válida. Elige una opción entre el 1 y 4.")
        
