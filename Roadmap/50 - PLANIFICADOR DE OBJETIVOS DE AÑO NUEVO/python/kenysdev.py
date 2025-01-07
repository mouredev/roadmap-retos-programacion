# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# #50 PLANIFICADOR DE OBJETIVOS DE AÑO NUEVO
# ------------------------------------
"""
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
"""

import os
from calendar import month_name as calendar_months
from datetime import datetime

class ObjectivePlanner:
    def __init__(self):
        self.goals = []
        self.months = list(calendar_months)[1:]
        self.pending_monthly = {}
        
    def add(self):
        if len(self.goals) >= 10:
            print("\nMáximo de 10 objetivos alcanzado.")
            return

        try:
            goal = {
                'name': input("Meta: ").strip(),
                'quantity': int(input("Cantidad: ")),
                'units': input("Unidades: ").strip(),
                'months': min(int(input("Plazo (en meses): ")), 12)
            }
            
            if all(goal.values()):
                goal_id = len(self.goals)
                self.goals.append(goal)
                monthly, extra = divmod(goal['quantity'], goal['months'])
                self.pending_monthly[goal_id] = [monthly + (1 if m < extra else 0) 
                                               for m in range(goal['months'])]
                print("\nObjetivo añadido exitosamente.")
            else:
                print("\nDatos inválidos.")
                
        except ValueError:
            print("\nError: Ingrese valores numéricos válidos.")

    def calculate_plan(self):
        if not self.goals:
            return None

        plan = {}
        for goal_id, goal in enumerate(self.goals):
            monthly_quantities = self.pending_monthly[goal_id]
            
            for month, quantity in enumerate(monthly_quantities):
                if quantity > 0:
                    month_name = self.months[month]
                    plan.setdefault(month_name, []).append(
                        f"[ ] {goal['name']} ({quantity} "
                        f"{goal['units']}/mes). Total: {goal['quantity']}."
                    )
        
        return {month: tasks for month, tasks in plan.items() if tasks}

    def save_plan(self, plan):
        if not plan:
            print("\nNo hay planificación para guardar.")
            return

        filename = f"plan_{datetime.now():%Y%m%d_%H%M}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for month, tasks in plan.items():
                    f.write(f"{month}:\n")
                    for task in tasks:
                        f.write(f"  {task}\n")
                    
                    f.write("\n")
                    
            print(f"\nPlan guardado en {filename}.")
            
        except IOError:
            print("\nError al guardar el archivo.")

    def display_plan(self):
        if plan := self.calculate_plan():
            for month, tasks in plan.items():
                print(f"\n{month}:")
                print('\n'.join(f"  {task}" for task in tasks))

    def run(self):
        os.system("cls" if os.name == "nt" else "clear")
        menu = {
            "1": lambda: self.add(),
            "2": lambda: self.display_plan(),
            "3": lambda: self.save_plan(self.calculate_plan()),
            "4": lambda: exit("\n¡Adiós!")
        }
        
        while True:
            print("\nGestor de Objetivos:")
            print("1. Añadir objetivo")
            print("2. Calcular plan detallado")
            print("3. Guardar planificación")
            print("4. Salir")
            
            if action := menu.get(input("\nSeleccione una opción: ").strip()):
                action()
            else:
                print("\nOpción inválida.")

if __name__ == "__main__":
    ObjectivePlanner().run()
