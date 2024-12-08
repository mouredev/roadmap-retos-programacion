"""
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
"""

# El concepto de “logging” en Python es muy útil para rastrear eventos que ocurren mientras se ejecuta un programa.
#  Python tiene un módulo incorporado llamado logging que permite registrar mensajes con diferentes niveles de severidad.

import logging

# Configuración básica del logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Ejemplos de mensajes con diferentes niveles de severidad
logging.debug('Este es un mensaje de depuración (debug)')
logging.info('Este es un mensaje informativo (info)')
logging.warning('Este es un mensaje de advertencia (warning)')
logging.error('Este es un mensaje de error (error)')
logging.critical('Este es un mensaje crítico (critical)')


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

import logging
import time

# Configuración básica del logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Lista para almacenar las tareas
tareas = []

def añadir_tarea(nombre, descripcion):
    inicio = time.time()
    tareas.append({'nombre': nombre, 'descripcion': descripcion})
    logging.info(f'Tarea añadida: {nombre}')
    fin = time.time()
    logging.debug(f'Tiempo de ejecución de añadir_tarea: {fin - inicio:.4f} segundos')

def eliminar_tarea(nombre):
    inicio = time.time()
    global tareas
    tareas = [tarea for tarea in tareas if tarea['nombre'] != nombre]
    logging.info(f'Tarea eliminada: {nombre}')
    fin = time.time()
    logging.debug(f'Tiempo de ejecución de eliminar_tarea: {fin - inicio:.4f} segundos')

def listar_tareas():
    inicio = time.time()
    if not tareas:
        logging.warning('No hay tareas para listar')
    else:
        for tarea in tareas:
            logging.info(f"Tarea: {tarea['nombre']}, Descripción: {tarea['descripcion']}")
    fin = time.time()
    logging.debug(f'Tiempo de ejecución de listar_tareas: {fin - inicio:.4f} segundos')

# Ejemplo de uso
añadir_tarea('Comprar pan', 'Comprar pan en la panadería')
añadir_tarea('Estudiar Python', 'Completar el ejercicio de logging')
listar_tareas()
eliminar_tarea('Comprar pan')
listar_tareas()
