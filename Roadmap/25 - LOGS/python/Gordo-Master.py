### Logs ###

import logging
import time

"""
Ejercicio
"""

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s ",
    handlers=[logging.StreamHandler()]
)

# logging.debug("Esto es un mensaje de DEBUG")
# logging.info("Esto es un mensaje de INFO")
# logging.warning("Esto es un mensaje de WARNING")
# logging.error("Esto es un mensaje de ERROR")
# logging.critical("Esto es un mensaje de ERROR")

"""
Extra
"""


class TaskManager:

    def __init__(self) -> None:
        self.tasks = {}

    def duration(func):
        def time_laps(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            logging.debug(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")
            return result
        return time_laps

    @duration
    def add_task(self, name: str, description: str):
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Tarea añadida: {name}.")
        else:
            logging.warning(f"Se a intentado añadir una tarea que ya existe: {name}.")
        logging.debug(f"Numero de tareas: {len(self.tasks)}")

    @duration
    def delete_task(self, name: str):
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Se ha eliminado la tarea: {name}.")
        else:
            logging.error(f"Se ha intentado eliminar una tarea que no existe: {name}.")
        logging.debug(f"Numero de tareas: {len(self.tasks)}")


    @duration    
    def list_tasks(self):
        if self.tasks:
            logging.info(f"Se va a imprimir la lista de tareas.")
            for name, description in self.tasks.items():
                print (f"{name} - {description}")
        else:
            logging.info(f"No hay tareas para mostrar.")

task_manager = TaskManager()
task_manager.list_tasks()
task_manager.add_task("Pan", "Comprar 5 barras de pan")
task_manager.add_task("Python", "Estudiar Python")
task_manager.list_tasks()
task_manager.delete_task("Python")
task_manager.list_tasks()
task_manager.add_task("Pan", "Comprar 5 barras de pan")
task_manager.delete_task("Python")

