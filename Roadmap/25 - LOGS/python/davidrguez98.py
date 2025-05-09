""" /*
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
 */ """

#EJERCICIO

import logging

logging.debug("Esto es un mensaje de debug")
logging.info("Esto es un mensaje de información")
logging.warning("Esto es un mensaje de warning")
logging.error("Esto es un mensaje de error")
logging.critical("Esto es un mensaje critico")

#DIFICULTAD EXTRA

logging.basicConfig(level=logging.INFO, format="\n%(levelname)s: %(message)s")

class TaskManager:

    def __init__(self):
        self.tasks = {}

    def new_task(self, name: str, description: str):
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"La tarea {name} ha sido añadida.")
        elif name in self.tasks:
                logging.error(f"La tarea {name} ya estaba añadida a la lista de tareas.")
        else:
            print("La tarea no ha podido ser creada.")
            logging.debug(f"Error al añadir la tarea {name}.")

    def delete_task(self, name):
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"La tarea {name} ha sido eliminada")
        elif name not in self.tasks:
                logging.error(f"La tarea {name} no existe.")
        else:
            print("La tarea no ha podido ser eliminada.")
            logging.debug(f"Error al eliminar la tarea {name}.")

    def list_tasks(self):
        if self.tasks:
            print("\nLISTADO DE TAREAS:\n")
            for name, description in self.tasks.items():
                print(f"{name}: {description}")
        else:
            print("La lista de tarea no ha podido ser mostrada.")
            logging.debug(f"Error al visualizar la lista de tareas.")


task_manager = TaskManager()
task_manager.new_task("Pan", "Comprar una barra de pan integral")
task_manager.new_task("Pan", "Comprar una barra de pan integral")
task_manager.new_task("Ejercicio", "Hacer 30 minutos de yoga")
task_manager.new_task("Estudio", "Repasar conceptos básicos de React")
task_manager.new_task("Trabajo", "Enviar el informe mensual al supervisor")
task_manager.new_task("Cita médica", "Pedir cita para revisión anual")
task_manager.new_task("Tomates", "Comprar 6 tomates")
task_manager.list_tasks()
task_manager.delete_task("Estudio")
task_manager.delete_task("Cebolla")
task_manager.list_tasks()