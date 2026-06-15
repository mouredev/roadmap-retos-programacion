'''
Ejercicio:
Explora el concepto de "logging" en tu lenguaje. Configuralo y muestra un ejemplo con cada nivel de severidad posible.
'''

import logging

# Creamos el logger
logger = logging.getLogger(__name__)

# Configuramos el logging para que todo se guarde en el archivo 'example.log' y su nivel de severidad sea DEBUG.
logging.basicConfig(encoding = 'utf-8', level = logging.DEBUG)

logger.debug('Este es el mas bajo de los niveles. Se usa para informacion detallada, tipicamente solo durante el diagnostico de problemas')
logger.info('Este es el penultimo mas bajo de los niveles, confirma de que las cosas estan funcionando como se esperaba.')
logger.warning('Este es el nivel por defecto, indica que algo inesperado sucedio.')
logger.error('Debido a un problema mas grave, el software no ha sido capaz de realizar alguna funcion')
logger.critical('Un grave error, que indica que el programa en si mismo puede ser incapaz de seguir funcionando.')

'''
Dificultad extra:
Crea un programa ficticio de gestion de tareas que permita agregar, eliminar y listar dicha tareas.
    * Agregar: recibe nombre y descripcion
    * Eliminar: por nombre de la tarea

Implementa diferentes mensajes de log que muestren informacion segun la tarea ejecutada

Utiliza un log para visualizar el tiempo de ejecucion de cada tarea
'''
tareas = []

'''
Creamos un decorador que:
Mida la hora antes de ejecutar
mida la hora depsues
imprima el tiempo en log
'''

import time

def tiempos(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_total = (fin - inicio)
        logger.info(f"La ejecucion de {func.__name__} duro {tiempo_total:.4f}")
        return resultado
    return wrapper

@tiempos
def agregar_tarea(nombre: str, descripcion: str):
    tarea = {}
    try:
        tarea["nombre"] = nombre
        tarea["descripcion"] = descripcion
        
        tareas.append(tarea)
        logger.info("Tarea creada con exito!")
    except Exception as e:
        logger.warning(f"Ha ocurrido un error inesperado: {e}")

@tiempos
def eliminar_tarea(nombre: str):
    try:
        for tarea in tareas:
            if tarea["nombre"] == nombre:
                tareas.remove(tarea)
                logger.info("Tarea eliminada con exito!")
    except Exception as e:
        logger.warning(f"Ha ocurrido un error inesperado: {e}") 

@tiempos
def mostrar_tareas():
    try:
        for tarea in tareas:
            print(f"*Nombre: {tarea['nombre']}, Descripcion: {tarea['descripcion']}")
        logger.info("Tareas listadas con exito!")
    except Exception as e:
        logger.warning(f"Ha ocurrido un error inesperado: {e}")


agregar_tarea("Hacer codigo", "Terminar este codigo")
agregar_tarea("Hacer el cuarto", "Organizar mi cuarto y tender la cama.")
eliminar_tarea("Hacer codigo")
mostrar_tareas()