"""
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
"""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    #filename="test.log", filemode="w",      # Crea un archivo.log con los diferentes mensajes o logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

logger.debug('Este es un mensaje de depuración (DEBUG)')
logger.info('Este es un mensaje informativo (INFO)')
logger.warning('Este es un mensaje de advertencia (WARNING)')
logger.error('Este es un mensaje de error (ERROR)')   # Usado normalmente en try/catch
logger.critical('Este es un mensaje crítico (CRITICAL)')


#############------------------------------------ EXTRA ------------------------------ #####################

import random

class TaskManager:

    def __init__(self):
        self.tasks = {}
        logger.info("Gestor de Tareas inicializado.")

    def add_task(self):
        name = input("Ingrese el nombre de la tarea: ")
        description = input("Ingrese la descripcion de la tarea: ")
        if name in self.tasks:
            logger.warning(f"Intento de añadir una tarea ya existente: {name}")
            return
        execution_time = random.randint(1, 5)
        self.tasks[name] = {
            "description": description,
            "execution_time": execution_time
        }
        logger.info(f"Tarea '{name}' añadida.")
        logger.debug(f"Tiempo de ejecucion de la tarea: '{name}': {execution_time} segundos.")

    def delete_task(self):
        name = input("Ingrese el nombre de la tarea a eliminar: ")        
        if name not in self.tasks:
            logger.warning(f"Intento de eliminar una tarea inexistente: {name}")
            return
        del self.tasks[name]        
        logger.info(f"Tarea '{name}' eliminada.")

    def list_tasks(self):
        if not self.tasks:
            logger.info("No hay tareas para listar")
            return
        for name, info in self.tasks.items():
            print(f"Tarea: {name} - Descripcion: {info['description']} - Tiempo de ejecucion: {info['execution_time']} segundos")
            logger.info(f"Tiempo de ejecucion de la tarea '{name}' es {info['execution_time']} segundos.")

manager = TaskManager()

while True:
    print("\nGestor de Tareas")
    print("1. Añadir tarea")
    print("2. Eliminar tarea")
    print("3. Listar tareas")
    print("4. Salir")
    choice = input("Seleccione una opción: ")
    if choice == '1':
        manager.add_task()
    elif choice == '2':
        manager.delete_task()
    elif choice == '3':
        manager.list_tasks()
    elif choice == '4':
        break
    else:
        print("Opción no válida, por favor intente nuevamente.")