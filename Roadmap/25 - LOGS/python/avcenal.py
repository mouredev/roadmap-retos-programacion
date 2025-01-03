import logging

"""
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
"""
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s -- %(levelname)s: %(message)s",
                    datefmt="%d/%m/%Y - %H:%M:%S",
                    handlers=[logging.StreamHandler()])

logging.debug("Info para hacer debugging")
logging.info("Todo funciona correctamente")
logging.warning("Ha pasado algo inesperado o está a punto de ocurrir algo")
logging.error("Error, no se ha podido realizar la acción")
logging.critical("Error grave, posiblemente el programa no pueda continuar")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea. DECORADORES??
"""
from time import sleep
import time

def task_number_decorator(function):
    def original_function(tasks:list):
        result = function(tasks)
        logging.debug(f"Número de tareas: {len(tasks)}")
        return result
    return original_function

def time_decorator(function):
    def original_function(*args):
        start_time = time.time()
        result = function(*args)
        end_time = time.time()
        print(f"La ejecución ha tardado {end_time - start_time:.6} segundos")
        print("\n")
        sleep(1)
        return result
    return original_function

@time_decorator
@task_number_decorator
def add_task(tasks:list):
    task:dict = {"name":"","description":""}
    task["name"] = input("Dime el nombre para esta tarea: ")
    for element in tasks: #busco si la tarea ya existe en el sistema
        if element["name"] == task["name"]:
            logging.warning("La tarea ya existe en el sistema")#si existe lanzo un logging.error
            break
    else: #si no existe añado la descripción y continúa la ejecución
        task["description"] = input("Y ahora la descripción: ")
        tasks.append(task)
        logging.info(f"Tarea {task["name"]} guardada en el sistema.")
    return tasks

@time_decorator
@task_number_decorator
def erase_task(tasks:list):
    if len(tasks) == 0:
        logging.warning(f"No hay tareas registradas en el sistema.")
    else:
        name:str = input("Dime el nombre de la tarea que quieres borrar: ")
        for element in tasks:
            if element["name"] == name:
                tasks.remove(element)
                logging.error(f"-- La tarea {name} ha sido borrada del sistema.")
                break
        else:
            logging.error(f"La tarea {name} no existe en el sistema.")
    return tasks

@time_decorator
def list_tasks(tasks):
    if len(tasks) == 0:
        logging.warning("No hay tareas registradas en el sistema")
    else:
        print("Estas son las tareas que hay en el sistema:")
        for element in tasks:
            print(f" - Nombre: {element["name"]}\n - Descripción: {element["description"]}\n")


print("\n\nTe doy la bienvenida al progranma de gestión de tareas")
tasks = list() #uso una lista aunque lo suyo sería usar un archivo externo para el log
#esta lista va a contener diccionarios con los elementos name y description.
while True:
    option = input("Por favor elije una de las opciones:\n - Añadir tarea(A)\n - Listar tareas(L)\n - Eliminar tarea(E)\n - Salir(S)\nTu opción --->").upper()
    if option == "A":
        add_task(tasks)
    elif option == "E":
        erase_task(tasks)
    elif option == "L":
        list_tasks(tasks)
    elif option == "S":
        print("Gracias por usar el sistema. Hasta pronto.")
        sleep(1)
        break
    else:
        print("La opción no es correcta\n")
        sleep(1)
