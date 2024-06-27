"""
*
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
import logging
import random

logging.basicConfig(format="%(process)d %(levelname)s %(message)s", level=logging.DEBUG)
logging.debug("esto es una depuracion")
logging.info("esto es una confirmacion") 
logging.warning("esto es una advertencia")
logging.error("esto es un mensaje de error")
logging.critical("esto es un mensaje critico")

#Extra

class GestionTareas:
    def __init__(self):
        self.tareas = {}
        

    
    def agg_tarea(self):
        name = input("Introduzca nombre: ")
        description = input("Introduzca breve descripcion de la tarea: ")
        if name in self.tareas:
            logging.error("La tarea ya existe")
        execution_time = random.randint(1,5)
        self.tareas[name]= {
            "description":description, 
            "execution_time":execution_time}
        logging.info("tarea agregada")
    
    def list_tareas(self):
        if not self.tareas:
            logging.error("La tarea no existe")
        for name, description  in self.tareas.items():
            logging.info(f"nombre de la tarea: {name}")
            logging.info(f"Descripcion: {description['description']}")
            logging.info(f"Tiempo de ejecucion: {description['execution_time']} segundos")
    
    def del_tareas(self):
        name = input("Introduzca nombre: ")
        if name not in self.tareas:
            logging.error("La tarea no existe")
        else:
            del self.tareas[name]
            logging.info(f"la tarea {name} fue eliminada")


        
task = GestionTareas()     
while True:
    print("--------->Gestor de Tareas<------------------")
    print("---->Elija una de las siguientes opciones<---")
    print("1. Agregar: ")
    print("2. Listar: ")
    print("3. Eliminar: ")
    print("4. Salir: ")

    option = int(input("Seleccione una opcion: "))

    if option == 1:
        task.agg_tarea()
    elif option == 2:
        task.list_tareas()
    elif option == 3:
        task.del_tareas()
    elif option == 4:
        print("Has elegido salir del programa, Hasta luego")
        break
    else:
        print("elija una de las opciones indicadas")
