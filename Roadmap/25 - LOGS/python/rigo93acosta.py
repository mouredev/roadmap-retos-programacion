'''
/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la 
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
 */
'''

'''
Ejercicio
'''

import logging
import time

# # logging.basicConfig(level=logging.DEBUG, 
# #                     format="%(asctime)s - %(levelname)s - %(message)s",
# #                     handlers=[logging.StreamHandler()])

logging.basicConfig(level=logging.DEBUG, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


'''
Extra
'''
def print_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        logging.debug(f"Execution time: {end_time - start_time:.2e} seconds")
    return wrapper

class TaskManager:

    def __init__(self) -> None:
        self.tasks = {}
    
    @print_time
    def add_task(self, name: str, description: str) -> None:
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Task {name} added")
        else:
            logging.warning(f"Task {name} already exists")

        logging.debug(f"Total tasks: {len(self.tasks)}")

    @print_time
    def remove_task(self, name: str) -> None:
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Task {name} removed")
        else:
            logging.error(f"Task {name} not found")

        logging.debug(f"Total tasks: {len(self.tasks)}")
    
    @print_time
    def list_tasks(self) -> None:
        if self.tasks:
            logging.info("Listing tasks")
            for name, description in self.tasks.items():
                print(f"{name}: {description}")
        else:
            logging.warning("No tasks to list")

task_manager = TaskManager()
task_manager.list_tasks()
task_manager.add_task("Python", "Estudiar Python")
task_manager.add_task("C", "Estudiar C")
task_manager.add_task("Python", "Estudiar Python")
task_manager.add_task("C++", "Estudiar C++")
task_manager.add_task("Java", "Estudiar Java")
task_manager.list_tasks()
task_manager.remove_task("Python")
task_manager.remove_task("C++")
task_manager.list_tasks()