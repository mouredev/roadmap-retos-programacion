# 50 - Planificador de objetivos de Año Nuevo
import os
from enum import Enum

class Month(Enum):
    ENERO = 1
    FEBRERO = 2
    MARZO = 3
    ABRIL = 4
    MAYO = 5
    JUNIO = 6
    JULIO = 7
    AGOSTO = 8
    SEPTIEMBRE = 9
    OCTUBRE = 10
    NOVIEMBRE = 11
    DICIEMBRE = 12

class Goals:
    def __init__(self):
        self.goal: str = None
        self.count = 0
        self.unit: str = None
        self.time_frame: int = 0
        self.calculated_goal = {Month(x).name: "" for x in range(1,13)}
        # {goal} ({.calculated_goal[month]} {.unit}/mes). Total: {.count}

    def create(self):
        valid_data = True
        print("Creador de objetivos: ")
        goal = input("Meta: ")
        count = input("Cantidad: ")
        unit = input("Unidad de medida: ")
        time_frame = input("Plazo en meses (máximo 12): ")

        if not count.isdigit() or int(count) < 0:
            print("\nLa cantidad debe ser un numero entero mayor que 0")
            valid_data = False
        if not time_frame.isdigit() or int(time_frame) < 0:
            print("\nEl plazo debe ser un numero entero mayor que 0")
            valid_data = False
            if int(time_frame) > 12:
                print("\nEl plazo maximo es de 12 meses")
                valid_data = False
        if valid_data:
            self.goal = goal
            self.count = int(count)
            self.unit = unit
            self.time_frame = int(time_frame)
        else:
            print("\nError: no se pudo crear el objetivo")        


    def calculate(self):
        media = self.count/self.time_frame
        media = round(media,2)
        for i in range(1,self.time_frame+1):
            self.calculated_goal[Month(i).name] = media


class Planner:
    def __init__(self):
        self.goals = []
        self.planner_text = {Month(x+1).name:[] for x in range(12)}
    
    def add_goal(self):
        if len(self.goals) < 10:
            goal = Goals()
            try:
                goal.create()
                goal.calculate()
                self.goals.append(goal)
            except Exception as e:
                print(f"\nError en la creacción de la meta")
        else:
            print("\nError: Solo se puede tener un maximo de 10 objetivos!")
            return

    def calculate_planner(self):
        if not self.goals:
            print("\nError: No se ha agregado ningun objetivo.")
            return
        
        self.planner_text = {Month(x+1).name:[] for x in range(12)}
        for goal in self.goals:
            for x in range(1,13):
                if goal.calculated_goal[Month(x).name]:
                    text = f"{goal.goal} ({goal.calculated_goal[Month(x).name]} {goal.unit}/mes). Total: {goal.count}"
                    self.planner_text[Month(x).name].append(text)
        
    def show_planner(self):
        if not self.goals:
            return
        print("\nImprimiendo plan detallado:")
        for month, texts_list in self.planner_text.items():
            if not self.planner_text[month]:
                continue
            print(f"\n{month}:")
            for index, text in enumerate(texts_list):
                print(f"[ ] {index+1}. {text}")

    def save_planner(self):
        if not self.goals:
            print("\nError: No se ha agregado ningun objetivo.")
            return
        
        file_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "plan.txt")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Plan detallado\n")
            for month, texts_list in self.planner_text.items():
                if not self.planner_text[month]:
                    continue
                f.write(f"\n{month}:")
                for index, text in enumerate(texts_list):
                    f.write(f"[ ] {index+1}. {text}\n")
        print(f"\nDocumento generado con exito en la ruta {file_path}!")

planner_2025 = Planner()


def show_menu():
    print("\nPlanificador de objetivos:")
    print("1. Añadir objetivo")
    print("2. Calcular plan detallado")
    print("3. Guardar la planificación")
    print("4. Salir")

while True:

    show_menu()

    option = input("Elige una opción: ")

    match option:
        case "1":
            planner_2025.add_goal()
        case "2":
            planner_2025.calculate_planner()
            planner_2025.show_planner()
        case "3":
            planner_2025.calculate_planner()
            planner_2025.save_planner()
        case "4":
            print("Saliendo del planificador...")
            break
        case _:
            print("Valor invalido.")