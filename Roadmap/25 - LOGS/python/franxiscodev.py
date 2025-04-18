'''
LOGS
'''
import logging
import time

# niveles de severidad
# cuando paso a producción level=logging.ERROR
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("Esto es un mensaje de DEBUG")
logging.info("Esto es un mensajito de INFO")
# solo imprime por default warning error critical
logging.warning("mensaje de WARNING")
logging.error("cuidado cuidado ERROR")
logging.critical("esto es grave CRITICAL")

'''
Extra
'''


class TaskManager:

    def __init__(self) -> None:
        self.tasks = {}
        # print(type(self.tasks))

    def _medir_tiempo(funcion):
        """Decorador para medir el tiempo de ejecución de una función."""

        def wrapper(self, *args, **kwargs):
            inicio = time.time()
            resultado = funcion(self, *args, **kwargs)
            tiempo_ejecucion = time.time() - inicio
            logging.info(
                f"TIEMPO ejecución {funcion.__name__}: {tiempo_ejecucion:.6f} segundos")
            return resultado
        return wrapper

    @_medir_tiempo
    def add_task(self, name: str, description: str):
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Tarea agregada ok: {name}")
        else:
            logging.warning(
                f"Se ha intentado agregar una tarea existente: {name}")
        logging.debug(f"Número de tareas actuales: {len(self.tasks)}")

    @_medir_tiempo
    def delete_task(self, name: str):
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Tarea eliminada ok: {name}")
        else:
            logging.error(
                f"Se ha intentado eliminar una tarea NO existente: {name} 💥")
        logging.debug(f"Número de tareas actuales: {len(self.tasks)}")

    @_medir_tiempo
    def list_tasks(self):
        if self.tasks:
            # print(self.tasks)
            logging.info("Imprimir Lista de tareas")
            for name, description in self.tasks.items():
                print(f"{name} - {description}")
        else:
            logging.info("No hay tareas para mostrar")


print("-- Tareas --")
task_manager = TaskManager()
task_manager.add_task("Panecillos", "Comprar pancitos para picoteo")
task_manager.add_task("Python", "Estudiar con picoteo")

task_manager.list_tasks()
task_manager.delete_task("Python")
task_manager.list_tasks()

task_manager.add_task("Panecillos", "Comprar +")
