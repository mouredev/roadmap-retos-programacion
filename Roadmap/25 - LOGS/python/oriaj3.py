""" 
25 - LOGS
Autor de la solución: Oriaj3

Teoría:
Los logs son mensajes que se utilizan para registrar información sobre la ejecución de un programa.
Los logs son útiles para depurar errores, monitorizar el comportamiento de una aplicación y registrar
la actividad del sistema.

En Python, se puede utilizar el módulo "logging" para añadir logs a un programa. El módulo "logging"
proporciona una interfaz flexible y fácil de usar para registrar mensajes de log en diferentes niveles
de severidad.

Los niveles de severidad de los logs son:
- DEBUG: Mensajes detallados para depurar problemas.
- INFO: Mensajes informativos sobre la ejecución del programa.
- WARNING: Mensajes de advertencia sobre posibles problemas.
- ERROR: Mensajes de error que indican un problema en la ejecución del programa.
- CRITICAL: Mensajes críticos que indican un fallo grave en el programa.

Ejemplo:
import logging

# Configurar el logger
logging.basicConfig(level=logging.DEBUG)

# Registrar mensajes de log
logging.debug("Este es un mensaje de debug")
logging.info("Este es un mensaje informativo")
logging.warning("Este es un mensaje de advertencia")
logging.error("Este es un mensaje de error")
logging.critical("Este es un mensaje crítico")
"""

"""
/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
"""
import logging

#Añadir tiempo a los mensajes
logging.basicConfig(format='%(asctime)s [%(levelname)s]  %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG, handlers = [logging.StreamHandler()])

logging.debug("Este es un mensaje de debug")
logging.info("Este es un mensaje informativo")
logging.warning("Este es un mensaje de advertencia")
logging.error("Este es un mensaje de error")
logging.critical("Este es un mensaje crítico")


"""
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



class gestor_tareas:
    tareas = []
    
    def anadir(self, nombre, descripcion):
        self.tareas.append([nombre, descripcion])
        logging.info(f"Se ha añadido la tarea: {nombre}")
        
    def eliminar(self, nombre):
        encontrado = False
        for tarea in self.tareas:
            if tarea[0] == nombre:
                self.tareas.remove(tarea)
                logging.info(f"Se ha eliminado la tarea: {nombre}")    
                encontrado = True
                break
        if not encontrado:
            logging.warning(f"No se ha encontrado la tarea: {nombre}")
            
                
    def listar(self):
        if len(self.tareas) == 0:
            logging.warning("No hay tareas para mostrar")
            return
        for tarea in self.tareas:
            print(f"Nombre: {tarea[0]} - Descripción: {tarea[1]}")
    

# Crear un gestor de tareas
gestor = gestor_tareas()
gestor.listar()

gestor.anadir("Tarea1", "Descripción de la tarea 1")
gestor.anadir("Tarea2", "Descripción de la tarea 2")
gestor.listar()

gestor.eliminar("Tarea1")
gestor.eliminar("Tarea3")
