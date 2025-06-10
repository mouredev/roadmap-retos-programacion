'''
/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la 
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
 */
'''
#https://docs.python.org/3/library/logging.html
import logging
#https://docs.python.org/3/library/logging.html#logging.basicConfig
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message') #https://docs.python.org/3/library/logging.html#logging.debug
logging.info('This is an info message') #https://docs.python.org/3/library/logging.html#logging.info
logging.warning('This is a warning message') #https://docs.python.org/3/library/logging.html#logging.warning
logging.error('This is an error message') #https://docs.python.org/3/library/logging.html#logging.error
logging.critical('This is a critical message') #https://docs.python.org/3/library/logging.html#logging.critical

#DIFICULTAD EXTRA, GESTION DE TAREAS
import time
class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f'{self.nombre} - {self.descripcion}'

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        logging.info(f'Tarea añadida: {tarea}')
        self.tareas.append(tarea)

    def eliminar_tarea(self, nombre):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                self.tareas.remove(tarea)
                logging.info(f'Tarea eliminada: {tarea}')
                break

gestor = GestorTareas()
logging.info('Gestor de tareas creado')
time.sleep(2)
tarea1 = Tarea('Tarea 1', 'Salir a correr')
gestor.agregar_tarea(tarea1)
time.sleep(1)
tarea2 = Tarea('Tarea 2', 'Terminar mi sitio web')
gestor.agregar_tarea(tarea2)
time.sleep(1)
tarea3 = Tarea('Tarea 3', 'Estudiar Python')
gestor.agregar_tarea(tarea3)
time.sleep(2)
logging.info('Tareas añadidas')
time.sleep(1)
logging.info('Eliminando tareas')
time.sleep(2)
gestor.eliminar_tarea('Tarea 2')
time.sleep(1)
gestor.eliminar_tarea('Tarea 1')
time.sleep(1)
gestor.eliminar_tarea('Tarea 3')
time.sleep(1)