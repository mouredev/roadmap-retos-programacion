# 25 - LOGS

"""
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
"""

import logging  # El logging es prácticamente un depurador de código
import os
import time

logging.basicConfig(
    encoding='utf-8',
    format="%(levelname)s == %(message)s",
    level=logging.DEBUG
)

# Por defecto el level es Warning
logging.debug("Este es un mensaje de debug")
logging.critical("Este es un mensaje crítico")
logging.error("Este es un mensaje de error")
logging.info("Este es un mensaje de info")
logging.warning("Este es un mensaje de advertencia")


class GestorDeTareas:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.datos_json = {}
        return cls._instancia

    def añadir_datos(self, nombre: str, descripcion: str):
        self.datos_json[nombre] = descripcion
        logging.info("Los datos fueron añadidos correctamente")

    def mostrar_datos(self):
        if self.datos_json:
            for nombre, descripcion in self.datos_json.items():
                logging.info(f"{nombre}: {descripcion}")
        else:
            logging.info("No hay tareas para mostrar")

    def eliminar_datos(self):
        tarea = input("Escribe el nombre de la tarea a eliminar: ")

        if tarea in self.datos_json:
            self.datos_json.pop(tarea)
            logging.info("La tarea ha sido eliminada")
        else:
            logging.warning(f"No hay tarea que se llame: {tarea}")


def añadir_datos() -> tuple:
    nombre = input("Escribe el nombre de la tarea: ")
    descripcion = input("Escribe una descripción breve de la tarea: ")
    logging.info("Todo ha salido perfectamente")
    return nombre, descripcion


def limpiar_pantalla():
    os.system('cls')


while True:
    logging.debug("Inicialización del gestor de tareas")
    time.sleep(0.3)
    logging.debug("Añade las tareas")

    gestor_de_tareas = GestorDeTareas()
    logging.info("""
                 1. Ver tareas
                 2. Añadir tarea
                 3. Eliminar tarea
                 """)

    try:
        opcion = int(input("Elige según el índice: "))
    except ValueError:
        logging.error("La opción tiene que ser un número")
        continue

    if opcion == 1:
        logging.info("Se mostrarán las tareas")
        gestor_de_tareas.mostrar_datos()
        input("Toque 'Enter' para continuar: ")
        limpiar_pantalla()

    elif opcion == 2:
        logging.info("Se añadirá una tarea")
        tarea = añadir_datos()
        nombre, descripcion = tarea
        gestor_de_tareas.añadir_datos(nombre, descripcion)
        time.sleep(1)
        limpiar_pantalla()

    elif opcion == 3:
        logging.info("Se eliminará una tarea")
        gestor_de_tareas.eliminar_datos()
        time.sleep(1)
        limpiar_pantalla()

    else:
        logging.warning("El número que seleccionaste no es una opción")
