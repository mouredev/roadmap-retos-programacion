"""
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
"""

# ─────────────────────────────────────────────────────────────────────────────────
#   Claves comunes del logging y sus tipos de formato
#
# | Clave            | Qué representa                         | Tipo     | Formato |
# |------------------|----------------------------------------|----------|---------|
# | asctime          | Fecha y hora (como texto)              | str      | %s      |
# | levelname        | Nivel del log (DEBUG, INFO, etc.)      | str      | %s      |
# | message          | El mensaje que escribes                | str      | %s      |
# | name             | Nombre del logger                      | str      | %s      |
# | filename         | Nombre del archivo                     | str      | %s      |
# | module           | Nombre del módulo (sin .py)            | str      | %s      |
# | pathname         | Ruta completa del archivo              | str      | %s      |
# | funcName         | Nombre de la función                   | str      | %s      |
# | processName      | Nombre del proceso                     | str      | %s      |
# | threadName       | Nombre del hilo                        | str      | %s      |
# | lineno           | Número de línea                        | int      | %d      |
# | process          | ID del proceso (PID)                   | int      | %d      |
# | thread           | ID del hilo                            | int      | %d      |
# | created          | Timestamp (segundos desde epoch)       | float    | %f      |
# | msecs            | Milisegundos de `asctime`              | float    | %f      |
# | relativeCreated  | Tiempo desde inicio del logging        | float    | %f      |
# ─────────────────────────────────────────────────────────────────────────────────

import logging
from logging.handlers import RotatingFileHandler

"""Configuracion básica. Cop logger raiz."""

logging.basicConfig(filename= 'mi_basic_log.log',filemode= 'a',level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')
#Se configura logger por defecto
logging.debug("Este es un mensaje de depuración (DEBUG).") #Se imprimen los mensajes segun la configuración
logging.info("Este es un mensaje informativo (INFO).")
logging.warning("Este es un mensaje de advertencia (WARNING).")
logging.error("Este es un mensaje de error (ERROR).")
logging.critical("Este es un mensaje crítico (CRITICAL).")



"""Configuracion con logger y handlers"""

#Se crea un logger. Si no le pongo nombre se considera tambien el raiz.
logger = logging.getLogger("mi_logguer") #Se le puede dar un nombre al crear y funcionan como jerarquia. logguer.sublogger.subsublogger
logger.setLevel(logging.DEBUG) # Si no lo configuro manualmente, por defecto se establece en Warning

# Configuración para la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Configuración para un archivo
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.DEBUG)

# Creo un formato
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Añadir los handlers al Logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.propagate = False

# Ahora, los logs se enviarán tanto a la consola como al archivo
logger.debug("Mensaje de debug.")
logger.info("Mensaje informativo.")



"""Configuracion de handler de fichero con rotación"""

logger1 = logging.getLogger("mi_logger_rotacion")
logger1.setLevel(logging.DEBUG)

file_handler_rot = RotatingFileHandler('rotate_log.log', mode='a', maxBytes= 1000, backupCount= 3)
file_handler_rot.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler_rot.setFormatter(formatter)
logger1.addHandler(file_handler_rot)
logger1.propagate = False # Evitas que el log se propague y llegue al raiz. Lo que imprime mensajes duplicados.
logger1.debug("Este es un mensaje de depuración (DEBUG).") #Se imprimen los mensajes segun la configuración
logger1.info("Este es un mensaje informativo (INFO).")
logger1.warning("Este es un mensaje de advertencia (WARNING).")
logger1.error("Este es un mensaje de error (ERROR).")
logger1.critical("Este es un mensaje crítico (CRITICAL).")



"""Configuracion de handler con jerarquia"""

# ----------------------------
# Configuración del logger raíz
# ----------------------------

logger_principal = logging.getLogger('mi_aplicacion')
logger_principal.setLevel(logging.DEBUG)

# Handler para consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Formato
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Añadimos el handler al logger principal
logger_principal.addHandler(console_handler)
logger_principal.propagate = False

# ----------------------------
# Simulación de modulo1
# ----------------------------

logger_modulo1 = logging.getLogger('mi_aplicacion.modulo1')

def ejecutar_modulo1():
    logger_modulo1.debug("Debug desde módulo 1")
    logger_modulo1.info("Info desde módulo 1")


# ----------------------------
# Simulación de modulo2
# ----------------------------

logger_modulo2 = logging.getLogger('mi_aplicacion.modulo2')

def ejecutar_modulo2():
    logger_modulo2.warning("Warning desde módulo 2")
    logger_modulo2.error("Error desde módulo 2")

# ----------------------------
# Ejecutamos todo
# ----------------------------

ejecutar_modulo1()
ejecutar_modulo2()



"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la 
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
"""

import time

#Creo un decorador para medir el tiempo de ejecucion de las tareas.
def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        logger.debug(f"Tiempo de ejecucion de {function.__name__}: {end - start:.10f} segundos")
        return result
    return wrapper



#Configuramos el logger
def setup_logger():
    logger = logging.getLogger("task_list")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler("task_list_log.log", "w")
    file_handler.setLevel(logging.DEBUG)

    formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formater)
    file_handler.setFormatter(formater)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.propagate = False
    return logger

logger = setup_logger()

class TaskManager():

    def __init__(self):
        self.tasks = {}

    @measure_time
    def insert_task(self):
        print("--Añadir tarea--")
        logger.debug("Opción Insert task")
        name = input("Introduce el nombre de la tarea: ").lower()
        if not name in self.tasks:
            description = input("Introduce la descripción: ")
            self.tasks[name] = description
            logger.info(f"Se introdujo correctamente la tarea: {name}")
            logger.debug(f"Número de tareas en la lista: {len(self.tasks)}")
        else:
            logger.error(f"La tarea {name} ya existe.")

    @measure_time
    def delete_task(self):
        print("--Eliminar tarea--")
        logger.debug("Opción Delete task")
        name = input("Introduce el nombre de la tareaa eliminar: ").lower()
        if name in self.tasks:
            del self.tasks[name]
            logger.info(f"Se borro la tarea {name} correctamente.")
            logger.debug(f"Número de tareas en la lista: {len(self.tasks)}")
        else:
            logger.error(f"La tarea {name} no esta en la lista.")

    @measure_time
    def list_tasks(self):
        logger.debug("Opción List tasks")
        if self.tasks:
            for name, task in self.tasks.items():
                print(f"{name}:{task}")
            logger.debug(f"Número de tareas en la lista: {len(self.tasks)}")
        else:
            logger.error(f"La lista esta vacía.")


print("Bienvenido a tu lista de tareas.")
task_manager = TaskManager()
while True:
    print("Menu:")
    print("\t1. Añadir tarea.")
    print("\t2. Eliminar tarea.")
    print("\t3. Listar tareas.")
    print("\t4. Salir.")
    try:
        option = int(input("Elige una opción: "))

        match option:
            case 1:
                task_manager.insert_task()
            case 2:
                task_manager.delete_task()
            case 3:
                task_manager.list_tasks()
            case 4:
                print("Adios")
                logger.debug("Se cerro la aplicación.")
                break
    except ValueError as e:
        logger.error(f"Has introducido una opcion invalida: {option}. Vuelve a intentarlo.")
        logger.debug(f"El usuario introdujo una opción invalida: {type(e)} - {e}")
        continue

    except Exception as e:
        logger.critical(f"Error critico: {type(e)} - {e}")
        
