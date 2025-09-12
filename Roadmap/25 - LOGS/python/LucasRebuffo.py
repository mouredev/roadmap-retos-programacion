import logging
import time

""" Ejercicio """

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
""" 
logging.debug("Esto es un mensaje de DEBUG")
logging.info("Esto es un mensaje de INFORMACION")
logging.warning("Esto es un mensaje de AVISO")
logging.error("Esto es un mensaje de ERROR")
logging.critical("Esto es un mensaje CRITICO")
 """

""" EXTRA """


def time_exec_decorator(function):

    def time_exec(*args):
        start_time = time.time()
        c = function(*args)
        end_time = time.time()
        print(f"Execution time: {end_time-start_time:.6f}")
        return c

    return time_exec


class Gestor_de_Tareas:

    def __init__(self) -> None:
        self.tareas = {}

    @time_exec_decorator
    def agregar_tarea(self, name, description):

        if name not in self.tareas:
            self.tareas[name] = description
            logging.info(f"Tarea agregada: {name}")
        else:
            logging.warning(f"La tarea que se quiere agregar ya existe")
        logging.debug(f"Numero de tareas: {len(self.tareas)}")

    @time_exec_decorator
    def borrar_tarea(self, name):
        if name in self.tareas:
            del self.tareas[name]
            logging.info(f"Tarea borrada: {name}")
        else:
            logging.error(f"La tarea que se quiere borrar no existe")

    @time_exec_decorator
    def listar_tareas(self):
        if self.tareas:
            logging.info(f"Se imprimen la tareas")
            for name, description in self.tareas.items():
                print(f"{name} - {description}")
        else:
            logging.info(f"No hay tareas que mostrar")


gestor_de_tareas = Gestor_de_Tareas()
gestor_de_tareas.agregar_tarea("Estudiar Python", "Aprender conceptos bases")
gestor_de_tareas.agregar_tarea(
    "Estudiar curso fullstack", "Profundizar en la parte de backend"
)
gestor_de_tareas.listar_tareas()

gestor_de_tareas.borrar_tarea("Estudiar Python")

gestor_de_tareas.listar_tareas()
