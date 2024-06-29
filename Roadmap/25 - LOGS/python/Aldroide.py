"""
    Ejercicio: Explora el concepto de "logging" en tu lenguaje. configuralo
    y muestra un ejemplo con cada nivel de "severidad" disponible.
"""

import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.StreamHandler()])

logging.debug("Esto es un mensaje de DEBUG")
logging.info("Esto es un mensaje de INFO")
logging.warning("Esto es un mensaje de warning")
logging.error("Esto es un mensaje de ERROR")
logging.critical("Esto es un mensaje de CRITICAL")

"""
    Dificultad Extra (opcional):
    Crea un programa ficticio de gestión de tareas que permita añadir, eliminar 
    y listar dichas tareas.
    - Añadir: recibe nombre y descripción.
    - Eliminar: por nombre de la tarea.
    Implementa diferentes mensajes de log que muestren información según 
    la tarea ejecutada (a tu elección)
    Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
"""


class TaskManager:
    def __init__(self) -> None:
        self.tasks = {}

    def add_task(self, name: str, description: str):
        start_time = time.time()
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Tarea añadida: {name}.")
        else:
            logging.warning(f"Se ha intentado una tarea existente: {name}.")
        logging.debug(f"Número de tareas: {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def delete_task(self, name: str):
        start_time = time.time()
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"se ha eliminmado la tarea: {name}.")
        else:
            logging.warning(
                f"Se ha intentado eliminar una tarea que no existe {name}")
        logging.debug(f"Numero de tareas: {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def list_tasks(self):
        star_time = time.time()
        if self.tasks:
            logging.info(f"Se va aimprimir la lista de tareas.")
            for name, description in self.tasks.items():
                print(f"{name} - {description}")
        else:
            logging.info("No hay tareas que mostrar.")
        end_time = time.time()
        self._print_time(star_time, end_time)

    def _print_time(self, start_time, end_time):
        logging.debug(
            f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")


task_manager = TaskManager()
task_manager.list_tasks()
task_manager.add_task("Fotografía", "Revelar fotos de Lia")
task_manager.add_task("Python", "Estudiar Python para ciencia de datos")
task_manager.list_tasks()
task_manager.delete_task("Python")
task_manager.list_tasks()
task_manager.add_task("Historia", "Leer los hornos de Hitler")
task_manager.delete_task("Python")
