# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * LOGS
# -----------------------------------
# Mas info: https://medium.com/@sachinsoni600517/logging-in-python-a-step-by-step-tutorial-086a617f4eaa

import logging
import time

"""
 * EJERCICIO #1:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
"""

# Para registrar mensajes en diferentes niveles.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 1. DEBUG
logging.debug('depuración')
    
# 2. INFORMACIÓN:
logging.info('informativo')

# 3. ADVERTENCIA:
logging.warning('Ddvertencia')

# 4. ERRORES:
logging.error('Error')
logging.critical('Error crítico')

"""
 * EJERCICIO #2:
* Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
* y listar dichas tareas.
* - Añadir: recibe nombre y descripción.
* - Eliminar: por nombre de la tarea.
* Implementa diferentes mensajes de log que muestren información según la 
* tarea ejecutada (a tu elección).
* Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
"""

class Program():
    def __init__(self):
        self.tasks: dict = {}
        logging.debug('Se inició instancia de la clase.')
    
    def _show_time(func: object):
        def wraper(*args):
            start_time: float = time.time()
            func(*args)
            end_time: float = time.time()
            logging.debug(f"Tiempo de ejecución: {(end_time - start_time):.21f} segundos.")

        return wraper

    @_show_time
    def add(self, name: str, description: str):
        self.tasks[name] = description
        logging.info('Se agregó una tarea.')

    @_show_time
    def delete(self, name: str):
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Tarea '{name}' eliminada.")
        else:
            print()
            logging.warning(f"No se encontró la tarea '{name}'.")

    @_show_time
    def show_list(self):
        logging.info('Lista de tareas')
        for task, des in self.tasks.items():
            print(f"{task} -- {des}")
        
print("\nEJERCICIO #2")

tasks = Program()

tasks.add("a", ".1")
tasks.add("b", "2")
tasks.add("c", "3")

tasks.delete("a")
tasks.show_list()

tasks.delete("a")

