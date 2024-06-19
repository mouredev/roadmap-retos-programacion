"""
 EJERCICIO:
 Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 un ejemplo con cada nivel de "severidad" disponible.

 DIFICULTAD EXTRA (opcional):
 Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 y listar dichas tareas.
 - Añadir: recibe nombre y descripción.
 - Eliminar: por nombre de la tarea.
 Implementa diferentes mensajes de log que muestren información según la
 tarea ejecutada (a tu elección).
 Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
"""
import logging
from os import remove
from time import sleep

print(f"{'#' * 47}")
print(f"##  Explicación  {'#' * 30}")
print(f"{'#' * 47}")

print(r"""
https://docs.python.org/es/3/howto/logging.html  <= en este link se haya una muy buena explicación de qué es y cuándo se usa "logging".

-----------------------------------------------------------------------------------------------------------------------------

Ejemplo de logging "sencillo":

    logger = logging.getLogger("reto_25_neslarra")
    logging.basicConfig(filename=logger.name + '.log', encoding='utf-8', filemode='a',
                        format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG,
                        datefmt='%Y-%b-%d %H:%M:%S')
    
    logger.debug('This message should go to the log file')
    logger.info('So should this') 
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
    logger.critical('Oopsie doopsie!!!')

-----------------------------------------------------------------------------------------------------------------------------

Ejemplo de logging desviando, formateando y filtrando eventos:

    def filter_console(reg):
        if reg.levelname in ("INFO", "DEBUG"):
            return True
        return False
    
    
    def filter_logfile(reg):
        if reg.levelname in ("WARNING", "ERROR", "CRITICAL"):
            return True
        return False
    
    
    log_format = logging.Formatter('%(asctime)s - %(levelname)s %(funcName)s (%(lineno)d) %(message)s', datefmt='%Y-%b-%d %H:%M:%S')
    logFile = 'reto_25_neslarra.log'
    
    file_handler = logging.FileHandler(logFile, encoding='utf-8')
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.WARNING)
    # file_handler.addFilter(filter_logfile)     # NO hace falta filtrar pque el level ya sólo toma WARNING, ERROR y CRITICAL <= SOLO EJEMPLO
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_format)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.addFilter(filter_console)
    
    logger = logging.getLogger('root')
    logger.setLevel(logging.DEBUG)
    
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    logger.debug('Se muestra SÓLO por consola')
    logger.info('Se muestra SÓLO por consola')
    logger.warning('Se muestra SÓLO por  fichero de log')
    logger.error('Se muestra SÓLO por  fichero de log')
    logger.critical('Se muestra SÓLO por  fichero de log')
    
    _ = input("Revisar el fichero de log => apretar cualquier tecla para borarrlo y salir.")
    logging.shutdown()
    remove(logFile)
""")

print(f"{'#' * 52}")
print(f"##  Dificultad Extra  {'#' * 30}")
print(f"{'#' * 52}\n")


class Task:

    logger = logging.getLogger("root")
    log_file = "reto_25_" + logger.name + '.log'
    logging.basicConfig(filename=log_file, encoding='utf-8', filemode='a',
                        format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG,
                        datefmt='%Y-%b-%d %H:%M:%S')

    def __init__(self, taskname: str):
        self.taskname = taskname
        Task.log_task(self.taskname)

    @classmethod
    def log_task(cls, taskname):
        cls.logger.info(taskname)

    @classmethod
    def log_shutdown(cls):
        logging.shutdown()
        remove(cls.log_file)


task1 = Task("Salir de la cama")
sleep(1)
task2 = Task("Ventilar")
sleep(1)
task3 = Task("Ordenar la habitación")
sleep(1)
task4 = Task("Bañarme")
sleep(1)
task5 = Task("Vestirme")
sleep(1)
task6 = Task("Desayunar")
sleep(1)
task7 = Task("Ponerme a trabajar")

_ = input("Revisar el fichero de log => apretar cualquier tecla para borarrlo y salir.")
Task.log_shutdown()
