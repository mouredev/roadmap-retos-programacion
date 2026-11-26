'''
Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
* un ejemplo con cada nivel de "severidad" disponible.
'''

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Este es un mensaje de depuración (DEBUG)')
logging.info('Este es un mensaje informativo (INFO)')
logging.warning('Este es un mensaje de advertencia (WARNING)')
logging.error('Este es un mensaje de error (ERROR)')
logging.critical('Este es un mensaje crítico (CRITICAL)')
logging.log(logging.DEBUG, 'Este es un mensaje de depuración usando log()')
logging.log(logging.INFO, 'Este es un mensaje informativo usando log()')
logging.log(logging.WARNING, 'Este es un mensaje de advertencia usando log()')
logging.log(logging.ERROR, 'Este es un mensaje de error usando log()')
logging.log(logging.CRITICAL, 'Este es un mensaje crítico usando log()')

'''
DIFICULTAD EXTRA (opcional):
* Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
* y listar dichas tareas.
* - Añadir: recibe nombre y descripción.
* - Eliminar: por nombre de la tarea.
* Implementa diferentes mensajes de log que muestren información según la
* tarea ejecutada (a tu elección).
* Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
'''

import time

tasks = {}

def add_task(name, description):
    start_time = time.time()
    logging.info(f'Añadiendo tarea: {name}')
    # Simulación de añadir tarea
    tasks[name] = description
    logging.debug(f'Descripción de la tarea: {description}')
    end_time = time.time()
    logging.info(f'Tarea "{name}" añadida correctamente en {end_time - start_time:.2f} segundos.')


def remove_task(name):
    start_time = time.time()
    logging.info(f'Eliminando tarea: {name}')
    # Simulación de eliminar tarea
    if name in tasks:
        del tasks[name]
    else:
        logging.error(f'Tarea "{name}" no encontrada.')
        return    
    end_time = time.time()
    logging.warning(f'Tarea "{name}" eliminada correctamente en {end_time - start_time:.6f} segundos.')

def list_tasks(tasks):
    start_time = time.time()
    logging.info('Listando todas las tareas:')
    for name, description in tasks.items():
        print(f'Tarea: {name}, Descripción: {description}')
    end_time = time.time()
    logging.info(f'Tareas listadas correctamente en {end_time - start_time:.6f} segundos.')

# Ejemplo de uso
add_task('Comprar leche', 'Ir al supermercado y comprar leche.')
add_task('Estudiar Python', 'Dedicar 2 horas a practicar Python.')
list_tasks(tasks)
remove_task('Comprar leche')
list_tasks(tasks)
remove_task('Hacer ejercicio')  # Intento de eliminar una tarea que no existe
remove_task('Comprar leche')  
