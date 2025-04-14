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

#Configuramos el logger
logger = logging.getLogger("task_list")
logger.setLevel(logging.DEBUG)

consoloe_handler = logging.StreamHandler()
consoloe_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("task_list_log.log", "w")
file_handler.setLevel(logging.DEBUG)

formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formater)
file_handler.setFormatter(formater)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.propagate = False

print("Bienvenido a tu lista de tareas.")
tasks = {}
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
                print("Añadir tarea")
                name = input("Introduce el nombre de la tarea: ").lower()
                description = input("Introduce la descripción: ")
                tasks[name] = description
                logger.info(f"Añadida tarea {name}")
            case 2:
                print("Eliminar tarea")
                name = input("Introduce el nombre de la tareaa eliminar: ").lower()
                del tasks[name]
                logger.info(f"Eliminada tarea {name}")
            case 3:
                print("Tareas")
                for name, task in tasks.items():
                    print(name)
                    print(f"\t{task}")
                logger.info(f"Se listaron las tareas - Número de tareas listadas {len(tasks)}")
            case 4:
                print("Adios")
                logger.info("Se cerro la aplicación")
                break
    except ValueError as e:
        print("Introduce una opción valida.")
        logger.info(f"El usuario introdujo una opción invalida: {type(e)} - {e}")
        continue

    except KeyError as e:
        print("No hay ninguna tarea con ese nombre.")
        logger.info(f"El usuario introdujo una tarea inexistente: {type(e)} - {e}")

    except Exception as e:
        logger.error(f"Error critico: {type(e)} - {e}")
        
