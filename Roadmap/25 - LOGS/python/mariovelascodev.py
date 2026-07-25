import logging
import time
#Ejercicio

#Configuración básica del logger
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)

#Registrar mensajes
logging.debug("Esto es un mensaje de depuración")
logging.info("Esto es un mensaje de información")
logging.warning("Esto es un mensaje de aviso")
logging.error("Esto es un mensaje de ERROR")
logging.critical("Esto es un mensaje de ERROR CRITICO")

print("\n-----------------\n")

#Extra
class TaskManager():
    def __init__(self) -> None:
        self.tasks = {}

    def elapsed_time(func):
        def wrapper(*args, **kwargs):
            start_task = time.time()
            c = func(*args, **kwargs)
            logging.debug(f"Tiempo transcurrido: {time.time() - start_task:.6f} segundos")
            return c
        return wrapper

    @elapsed_time
    def add_task(self, name, description):
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info("Tarea asignada")
        else:
            logging.warning(f"La tarea {name} existe")

    @elapsed_time
    def delete_task(self, name):
        if name in self.tasks:
            del self.tasks[name]
            logging.info("Tarea eliminada.")
        else:
            logging.warning(f"La tarea {name} no existe")

    @elapsed_time
    def show_tasks(self):
        print("Listado de tareas")
        for key, value in self.tasks.items():
            print(f"{key}: {value}")

task_manager = TaskManager()
task_manager.show_tasks()
task_manager.add_task("Python", "Estudiar Python")
task_manager.add_task("SQL", "Estudiar SQL")
task_manager.show_tasks()
task_manager.add_task("SQL", "Estudiar SQL")
task_manager.delete_task("Java")
task_manager.delete_task("Python")
