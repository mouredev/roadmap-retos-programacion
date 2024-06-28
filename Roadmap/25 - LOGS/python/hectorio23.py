# Autor: Héctor Adán 
# GitHub: https://github.com/hectorio23 
import logging
import time


#################################################
################# EJERCICIO #####################
#################################################

# Configuración básica del logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Ejemplos de mensajes con cada nivel de severidad
logging.debug("Este es un mensaje de depuración.")
logging.info("Este es un mensaje informativo.")
logging.warning("Este es un mensaje de advertencia.")
logging.error("Este es un mensaje de error.")
logging.critical("Este es un mensaje crítico.")



#################################################
############## EJERCICIO EXTRA ##################
#################################################

# Configuración del logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Lista para almacenar las tareas
tareas = []

def add_task(nombre, descripcion):
    start_time = time.time()
    logging.info(f"Añadiendo tarea: {nombre}")
    tarea = {"nombre": nombre, "descripcion": descripcion}
    tareas.append(tarea)
    logging.debug(f"Tareas actuales: {tareas}")
    end_time = time.time()
    logging.info(f"Tarea añadida en {end_time - start_time} segundos")

def delete_task(nombre):
    start_time = time.time()
    logging.info(f"Eliminando tarea: {nombre}")
    global tareas
    tareas = [tarea for tarea in tareas if tarea["nombre"] != nombre]
    logging.debug(f"Tareas actuales: {tareas}")
    end_time = time.time()
    logging.info(f"Tarea eliminada en {end_time - start_time} segundos")

def show_tasks():
    logging.info("Listando todas las tareas")
    for tarea in tareas:
        logging.info(f"Tarea: {tarea['nombre']}, Descripción: {tarea['descripcion']}")
    if not tareas:
        logging.warning("No hay tareas para listar")

# Ejemplo de uso del programa de gestión de tareas
add_task("Comprar pan", "Ir a la panadería y comprar una barra de pan")
add_task("Estudiar Python", "Completar el ejercicio de logging en Python")
show_tasks()
delete_task("Comprar pan")
show_tasks()
