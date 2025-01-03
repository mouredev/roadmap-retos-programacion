"""
EJERCICIO:
Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
un ejemplo con cada nivel de "severidad" disponible.

DIFICULTAD EXTRA(opcional):
Crea un programa ficticio de gestión de tareas que permita añadir, 
eliminar y listar dichas tareas.
- Añadir: recibe nombre y descripción.
- Eliminar: por nombre de la tarea.
Implementa diferentes mensajes de log que muestren información según
la tarea ejecutada (a tu elección).
Utiliza el log apra visualizar el tiempo de ejecución de cada tarea.

by adra-dev
"""

"""
Loggin:
Registrar información relevante durante la ejecución de un programa 
es una buena práctica como desarrollador cuando buscas obtener un 
mejor entendimiento de tu código. Esta práctica es llamada  logging, 
y es una herramienta muy útil para ti como desarrollador, esta te 
puede ayudar a descubrir escenarios que tal vez no hayas tenido en 
cuenta.

Estos registros son llamados logs, y pueden servir como un par extra 
de ojos que constantemente están mirando al flujo de tu aplicación. 
Los logs pueden guardar información, como qué  usuarios o IP 
accedieron a la aplicación. Si ocurre un error, entonces los logs 
pueden proporcionar más información que un seguimiento de pila, ya 
que indican el estado del programa antes del error y la línea de 
código en la que se produjo.

Python provee a un sistema de logins como parte de su librería estándar. 
documentacion: "https://realpython.com/python-logging/" 

Severidad:
Existen  5 niveles de logs por default, en orden de severidad 
creciente serían: DEBUG, INFO, WARNING, ERROR, CRITICAL.

"""

import logging
import time 

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers= [logging.StreamHandler()])

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


"""
Extra
"""

class TaskManager:

    def __init__(self) -> None:
        self.tasks = {}

    def addTask(self, name: str, description: str):
        start_time = time.time()
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Tarea agregada: {name}.")
        else:
            logging.warning(f"Se ha intentando agregar una tarea que ya existe: {name}.")
        logging.debug(f"Numero de tareas {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def deleteTask(self, name: str):
        start_time = time.time()
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Se ha eliminado la tarea: {name}.")
        else:
            logging.error(
                f"Se a intentando eliminar una tarea que no existe: {name}.")
        logging.debug(f"Numero de tareas {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def list_tasks(self):
        start_time = time.time()
        if self.tasks:
            logging.info(f"Se va imprimir la lista de tareas")
            for name, description in self.tasks.items():
                print(f"{name} - {description}")
        else:
            logging.info("No hay tareas para mostrar")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def _print_time(self, start_time, end_time):
        logging.debug(
            f"Tiempo de ejecucion: {end_time - start_time:.6f} segundos.")


task_manager = TaskManager()
task_manager.list_tasks()
task_manager.addTask("Pan", "Comprar 5 barras de pan")
task_manager.addTask("Python", "Estudiar Python")
task_manager.list_tasks()
task_manager.deleteTask("Python")
task_manager.list_tasks()
task_manager.addTask("Pan", "Comprar 5 barras de pan")
task_manager.deleteTask("Python")