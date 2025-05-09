"""
/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 */
"""
# Logging
import logging

# Creando mi propio Log
log = logging.getLogger("Mi Log")
log.setLevel(level=logging.DEBUG) # Lo pongo en modo DEBUG para que capture todos los mensajes

formato = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

archivo = logging.FileHandler(filename="mi_log.log",mode="a")
consola = logging.StreamHandler()

archivo.setFormatter(formato)
consola.setFormatter(formato)

log.addHandler(archivo)
log.addHandler(consola)

# Pruebas
log.debug("Esto es un mensaje de depuración")
log.info("Esto es un mensaje informativo")
log.warning("Esto es una advertencia")
log.error("Esto es un mensaje de error")
log.critical("Esto es un mensaje critico")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * x Añadir: recibe nombre y descripción.
 * x Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la 
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
"""

class Tarea:
    _lista_tareas = {}
    def agregar(self,nombre,descripcion):
        self._lista_tareas[nombre] = descripcion
        log.info(f"{nombre} añadido")

    def borrar(self,nombre):
        if nombre in self._lista_tareas:
            del self._lista_tareas[nombre]
            log.info(f"{nombre} eliminado")

    def mostrar(self):
        print()
        log.info("Mostrando Lista Actual:")
        for nombre, descripcion in self._lista_tareas.items():
            log.info(f"{nombre}\n{descripcion}")    
        log.info(f"Lista mostrada")

# Pruebas
hoy = Tarea()
hoy.agregar("Programar","Hacer este ejercicio")
hoy.agregar("Comer","Pizza Barbacoa")
hoy.agregar("Dormir","Recuperar fuerzas")

hoy.mostrar()
hoy.borrar("Comer")
hoy.mostrar()