# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga
"""
/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
"""

""" Logging

Es un modulo poderoso para el seguimiento de eventos. Tiene diferentes niveles de
severidad para los eventos.
"""
import logging

# Configuración básica, se establece el nivel, el formato, y se indica que los logs
# se envíen a la consola
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # filename = "app.log" Opcionalmente se puede guardar en un archivo

# Niveles de severida
logging.debug("Este es un mensaje de debug")
logging.info("Este es un mensaje de información")
logging.warning("Este es un mensaje de advertencia")
logging.error("Este es un mensaje de error")
logging.critical("Este es un mensaje crítico")

# Logger personalizado

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Creamos un handler para la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formato personalizado
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Anadir handler al logger
logger.addHandler(console_handler)

# Registrar mensajes
logger.debug("Este es un mensaje de debug")
logger.info("Informacion importante")

"""
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
"""
import logging
import time
from typing import Dict

# Configuración básica del logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()]
)

class TaskManager:
    def __init__(self):
        self.tasks: Dict[str, str] = {}
        self._logger = logging.getLogger("TaskManagerLogger")
        self._logger.info("Se ha creado una instancia de la clase")

    @staticmethod
    def _log_execution_time(func):
        def wrapper(*args):
            start_time: float = time.time()
            logging.info(f"Iniciando {func.__name__}...")
            result = func(*args)
            duration = time.time() - start_time
            logging.info(f"{func.__name__} ejecutada en {duration:.8f}")
            return result
        return wrapper
        

    @_log_execution_time
    def add_task(self, task_name:str, task_description:str) -> bool:
        if task_name not in self.tasks: 
            self.tasks.update({task_name: task_description})
            self._logger.info(f"Tarea {task_name} agregada satisfactoriamente")
            return True
        else:
            self._logger.warning(f'La tarea {task_name} ya existe!')
            return False

    @_log_execution_time
    def remove_task(self, task_name) -> bool:
        if task_name in self.tasks:
            self.tasks.pop(task_name)
            self._logger.info(f"Tarea {task_name} eliminada con éxito")
            return True
        else:
            self._logger.warning(f"Tarea {task_name} no encontrada")
            return False

    @property
    @_log_execution_time
    def list_tasks(self) -> None:
        if not self.tasks:
            self._logger.info("No hay tareas registradas")
            return
        for key, value in self.tasks.items():
            print(f"{key}: {value}")
        self._logger.info(f"Tareas listada con éxito")


if __name__ == "__main__":

    print(f"Ejecutando el programa {TaskManager.__name__}")
    t1 = TaskManager()
    # Agregando tareas
    t1.add_task("Tarea 1", "Esta es la tarea 1")
    t1.add_task("Tarea 2", "Esta es la tarea 2")
    t1.add_task("Tarea 3", "Esta es la tarea 3")

    # Listando tareas
    t1.list_tasks

    t1.add_task("Tarea 1", "Esta es una nueva tarea 1")
    t1.list_tasks
    # Eliminando tareas
    t1.remove_task("Tarea 1")
    t1.remove_task("Tarea 1")