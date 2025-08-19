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

from abc import ABC, abstractmethod


    

class Resolution:
    def __init__(self, goal: str, amount: int, units: str, deadline:int) -> None:
        self.goal = goal
        self.amount = amount
        self.units = units
        self.deadline = deadline


class ResolutionsManager:
    def __init__(self) -> None:
        self.resolutions = []

    def add_resolution(self, resolution: Resolution) -> bool:
        if len(self.resolutions) > 9:
            return False
        
        self.resolutions.append(resolution)
        return True
        

class UIService:

    def display_menu(self) -> int:

        print("Planificador de objetivos.")
        print("1.- Agregar proposito")
        print("2.- Calcular plan detallado.")
        print("3.- Guardar plan")
        print("4.- Salir")

        selection = 0
        while selection not in range(1,5): 
            selection = input("Introduce una opción correcta: ")
            if not selection.isdigit():
                continue
            selection = int(selection)
        return int(selection)
    

class MenuAction(ABC):
    @abstractmethod
    def execute(self):
        pass

class AddResolutionAction(MenuAction):
    def __init__(self, resolutions_manager : ResolutionsManager) -> None:
        self.resolutions_manager = resolutions_manager

    def execute(self):
        goal = input("Proposito: ")

        while True:
            amount = input("Cantidad: ")
            if not amount.isdigit():
                print("Debes introducir un número")
                continue
            amount = int(amount)
            break

        units = input("Unidad:")
        while True:
            deadline = input("Plazo (meses): ")
            if not deadline.isdigit():
                print("Debes introducir un número")
                continue
            deadline = int(deadline)
            break

        resolution = Resolution(goal, amount, units, deadline)

        if resolutions_manager.add_resolution(resolution):
            print("Proposito añadido correctamente.")
        else:
            print("Ya has añadido el máximo de propositos.")

class CalculatePlanActionn(MenuAction):
    def __init__(self, resolutions_manager : ResolutionsManager) -> None:
        self.resolutions_manager = resolutions_manager

    def execute(self):

        months = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre",

        }

        for i in range(1,13):
            print()
            print(months[i])
            for resolution in resolutions_manager.resolutions:
                if resolution.deadline >= i:
                    print(f"\t{i}. {resolution.goal} ({resolution.amount / resolution.deadline} {resolution.units}/mes. Total {resolution.amount})")

class SavePlanAction(MenuAction):
    def __init__(self, resolutions_manager : ResolutionsManager) -> None:
        self.resolutions_manager = resolutions_manager

    def execute(self):
        pass


class ResolutionPlanner:
    def __init__(self, ui_service: UIService, resolutions_manager: ResolutionsManager ) -> None:
        self.ui_service = ui_service
        self.resolutions_manager = resolutions_manager

        self.menu_actions = {
            1: AddResolutionAction(resolutions_manager),
            2: CalculatePlanActionn(resolutions_manager),
            3: SavePlanAction(resolutions_manager)
        }

    def run(self):
        while True:
            selection = self.ui_service.display_menu()

            if selection == 4:
                break
            
            action = self.menu_actions.get(selection)
            if action:
                action.execute()
            else:
                print("Opción no valida.")

ui_service = UIService()
resolutions_manager = ResolutionsManager()
resolution_planner = ResolutionPlanner(ui_service, resolutions_manager)

resolution_planner.run()