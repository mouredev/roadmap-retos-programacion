# @Author: Daniel Grande (Mhayhem)

# EJERCICIO:
# El nuevo año está a punto de comenzar...
# ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
#
# Programa un gestor de objetivos con las siguientes características:
# - Permite añadir objetivos (máximo 10)
# - Calcular el plan detallado
# - Guardar la planificación
# 
# Cada entrada de un objetivo está formado por (con un ejemplo):
# - Meta: Leer libros
# - Cantidad: 12
# - Unidades: libros
# - Plazo (en meses): 12 (máximo 12)
#
# El cálculo del plan detallado generará la siguiente salida:
# - Un apartado para cada mes
# - Un listado de objetivos calculados a cumplir en cada mes
#   (ejemplo: si quiero leer 12 libros, dará como resultado 
#   uno al mes)
# - Cada objetivo debe poseer su nombre, la cantidad de
#   unidades a completar en cada mes y su total. Por ejemplo:
#
#   Enero:
#   [ ] 1. Leer libros (1 libro/mes). Total: 12.
#   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
#   Febrero:
#   [ ] 1. Leer libros (1 libro/mes). Total: 12.
#   ...
#   Diciembre:
#   [ ] 1. Leer libros (1 libro/mes). Total: 12.
#
# - Si la duración es menor a un año, finalizará en el mes
#   correspondiente.
#   
# Por último, el cálculo detallado debe poder exportarse a .txt
# (No subir el fichero)

months_name = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

class Goal:
    def __init__(self, goal: str, amount: int, units: str, deadline: int):
        self.goal = goal
        self.amount = amount
        self.units = units
        self.deadline = deadline
    
    def display_info(self, unit_month: int):
        return f"{self.goal} ({unit_month} {self.units}/ mes). Total {self.amount}"

months =  {month: [] for month in months_name}



def create_goal() -> object:
    goal_name = input("Objetivo: ")
    while True:
        try:
            amount = int(input("Cantidad (solo números): "))
            if amount > 0:
                break
            else:
                print("El número ha de ser positivo y mayor a cero.")
        except ValueError as e:
            print(f"ERROR: {e}")
    units = input("Unidades: ")
    while True:
        try:
            deadline = int(input("Plazo (maximo 12): "))
            if deadline > 0 and deadline < 13:
                break
            else:
                print("el número debe ser positivo y entre 1 y 12.")
        except ValueError as e:
            print(f"ERROR: {e}")
    
    goal = Goal(goal_name, amount, units, deadline)

    return goal

def calculate_monthly_unit(goal_object: object):
    unit_per_month = goal_object.amount // goal_object.deadline
    rest = goal_object.amount % goal_object.deadline
    
    return unit_per_month, rest

def add_goal_to_month(goal_object: object, unit: int, rest: int):
    limit = goal_object.deadline
    
    for index in range(limit):
        if rest > 0:
            months[months_name[index]].append((goal_object, unit + 1))
            rest -= 1
        else:
            months[months_name[index]].append((goal_object, unit))
        

def display():
    planning_text = ""
    for key, value in months.items():
        planning_text += f"{key}:\n"
        for item in value:
            planning_text += f"{item[0].display_info(item[1])}\n"
        planning_text += "\n"
    return planning_text

def save_planning():
    with open("planning.txt", "w") as file:
        file.write(display())


def main():
    total_goals = 0
    while True:
        print("1. Planificar objetivo.\n"
            "2. Mostrar Planificación\n"
            "3. Guardar.\n"
            "4. Salir")
        try:
            option = int(input())
            match option:
                case 1:
                    if total_goals < 10:
                        goal = create_goal()
                        unit, rest = calculate_monthly_unit(goal)
                        add_goal_to_month(goal, unit, rest)
                        total_goals += 1
                    else:
                        print("Se ha superado el maximo de 10 objetivos.")
                case 2:
                    print(display())
                case 3:
                    try:
                        save_planning()
                        print("Planificación guardada.")
                    except Exception as e:
                        print(f"ERROR: {e}")
                case 4:
                    print("Cerrando planificación.")
                    break
                case _:
                    print("Opción incorrecta.")
                    
        except ValueError as e:
            print(f"ERROR: {e}")

if __name__=="__main__":
    main()