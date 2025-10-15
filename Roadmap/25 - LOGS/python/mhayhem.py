#@Author Daniel Grande (Mhayhem)

# EJERCICIO:
# Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
# un ejemplo con cada nivel de "severidad" disponible.

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Esto es un mensaje de debuging.")
logging.info("Esto es un mensaje de información.")
logging.warning("Esto es un mensaje de advertencía.")
logging.error("Esto es un mensaje de error.")
logging.fatal("Esto es un mensaje crítico.")


# DIFICULTAD EXTRA (opcional):
# Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
# y listar dichas tareas.
# - Añadir: recibe nombre y descripción.
# - Eliminar: por nombre de la tarea.
# Implementa diferentes mensajes de log que muestren información según la 
# tarea ejecutada (a tu elección).
# Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 

import logging
from time import time 
from functools import wraps

class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

def calculate_time(func):
    @wraps(func)
    def timer(*args, **kwargs):
        star = time()
        result = func(*args, **kwargs)
        end = time()
        total_time = end - star
        logging.info(f"La función {func.__name__} se ejecuto en {total_time:.2f} s") 
        return result
    return timer

tasks = []

@calculate_time
def created_task(array: list) -> list:
    logging.info("inicializando Creador de tareas.")
    print("Tarea a crear.")
    name = input("Nombre:\n")
    description = input("Descripción:\n")
    if not name or not description:
        logging.warning("No se puede crear tareas sin nombre o sin descripción.")
    else:
        task = Task(name, description)
        array.append(task)
    return array

@calculate_time
def delete_task(array: list) -> list:
    logging.info("inicializando Eliminacion de tareas")
    del_task = input("Tarea a eliminar:\n")

    if del_task in tasks:
        logging.info(f"Tarea {del_task} sera eliminada.")
        array.pop(del_task)
    else:
        logging.error(f"La tarea: {del_task} no se encuentra. Cancelando eliminación.")
    return array

@calculate_time
def display_tasks(array) -> list:
    logging.info("Inicializando Listar tareas.")
    if not array:
        logging.error("No existen tareas")
    else:
        for i, task in enumerate(array):
            print(f"{i+ 1}: {task.name}")
        print(f"Listadas {len(array)}")
        
    return array

def task_manager(array):
    print("TASK MANAGER V 1.01")
    print("=" * 40)
    try:
        while True:
            print("1. Crear tarea.\n"
                "2. Eliminar tarea.\n"
                "3. Listar tareas.\n"
                "4. Salir.")
            option = int(input())
            match option:
                case 1:
                    created_task(array)
                    print("\n")
                case 2:
                    delete_task(array)
                    print("\n")
                case 3:
                    display_tasks(array)
                    print("\n")
                case 4:
                    logging.info("Saliendo del Task Manager")
                    break
                case _:
                    logging.warning("Opción inválida.\n")
    except ValueError as e:
        logging.critical(f"ERROR: {e}; Solo se aceptan números. Cerrando programa.")
    except KeyboardInterrupt as e:
        logging.critical(f"ERROR: {e}; El usuario interrumpió la ejecución. Cerrando programa.")

if __name__ == "__main__":
    task_manager(tasks)