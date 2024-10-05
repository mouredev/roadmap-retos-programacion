import logging
import time
"""
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.

"""


# CONFIGURACIÓN
logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s - %(levelname)s - %(message)s")

# NIVELES DE SEVERIDAD
logging.debug("Este es un mensaje de debug")
logging.info("Este es un mensaje de info")
logging.warning("Este es un mensaje de warning")
logging.error("Este es un mensaje de error")
logging.critical("Este es un mensaje critical")


"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
 */

"""


class TaskManager:

    def __init__(self) -> None:
        self.task = {}

    def _print_time_(function):
        def count_time(*args):
            start_time = time.time()
            result = function(*args)
            end_time = time.time()
            logging.debug(f"Tiempo de ejecución {end_time-start_time:.6f} segundos.")
            return result
        return count_time
        
    @_print_time_
    def add_task(self, name, description):
        if name in self.task.keys():
            logging.error(f"Se ha intentado agregar la tarea {name} que ya existía")
        else: 
            self.task[name] = description
            logging.info(f"La tarea {name} se ha añadido exitosamente")
        logging.info(f"Hay {len(self.task)} tareas almacenadas")
        end_time = time.time()

    @_print_time_
    def show_task(self):
        if not self.task: 
            logging.warning("No había tareas para mostrar")
        else: 
            for key, value in self.task.items():
                print(f"Task: {key} - Description: {value}")
            logging.info(f"Se han mostrado correctamente {len(self.task)} tareas")

    @_print_time_
    def delete_task(self, name):
        if name in self.task.keys():
            del self.task[name]
            logging.info(f"La tarea {name} se ha eliminado exitosamente")
        else: 
            logging.error("Se ha intentado eliminar una tarea que no existe")
        logging.info(f"Hay {len(self.task)} tareas almacenadas")


    


manager = TaskManager()
manager.add_task("programacion", "ejercicios")
manager.add_task("programacion", "ejercicios")
manager.add_task("Machine learning", "ejercicios")
manager.add_task("Python", "ejercicios")
manager.add_task("estadistica", "ejercicios")
manager.show_task()
manager.delete_task("maths")
manager.delete_task("estadistica")
manager.delete_task("programacion")
manager.show_task()