"""
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
"""

# EJERCICIO:
import time
import logging

logging.debug("Mensaje a nivel debug.")
logging.info("Mensaje a nivel info.")
logging.warning("Mensaje a nivel warning.")
logging.error("Mensaje a nivel error.")
logging.critical("Mensaje a nivel critical.")

# DIFICULTAD EXTRA:
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, description):
        start_time = time.time()
        if name in self.tasks:
            logging.warning(f'La tarea "{name}" ya existe.')
        else:
            self.tasks[name] = description
            logging.info(f'Tarea "{name}" añadida.')
        end_time = time.time()
        logging.debug(f'Tiempo de ejecución para añadir tarea: {
                      end_time - start_time} segundos')

    def remove_task(self, name):
        start_time = time.time()
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f'Tarea "{name}" eliminada.')
        else:
            logging.warning(f'La tarea "{name}" no existe.')
        end_time = time.time()
        logging.debug(f'Tiempo de ejecución para eliminar tarea: {
                      end_time - start_time} segundos')

    def list_tasks(self):
        start_time = time.time()
        if not self.tasks:
            logging.info('No hay tareas disponibles.')
        else:
            for name, description in self.tasks.items():
                logging.info(f'Tarea: {name} - Descripción: {description}')
        end_time = time.time()
        logging.debug(f'Tiempo de ejecución para listar tareas: {
                      end_time - start_time} segundos')


if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Tarea 1", "Descripción de la Tarea 1")
    manager.add_task("Tarea 2", "Descripción de la Tarea 2")

    manager.list_tasks()

    manager.remove_task("Tarea 1")

    manager.list_tasks()
