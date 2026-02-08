# EJERCICIO:
# Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
# un ejemplo con cada nivel de "severidad" disponible.
import logging
from typing import Dict
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato del mensaje
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug("Esto es un mensaje de debug")
logging.info("Esto es un mensaje de info")
logging.warning("Esto es un mensaje de warning")
logging.error("Esto es un mensaje de error")
logging.critical("Esto es un mensaje de critical")

#
# DIFICULTAD EXTRA (opcional):
# Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
# y listar dichas tareas.
# - Añadir: recibe nombre y descripción.
# - Eliminar: por nombre de la tarea.
# Implementa diferentes mensajes de log que muestren información según la
# tarea ejecutada (a tu elección).
# Utiliza el log para visualizar el tiempo de ejecución de cada tarea.

def medir_tiempo(func):
    """Decorador para medir el tiempo de ejecución de una función."""
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        inicio = time.time()

        resultado = func(*args, **kwargs)

        tiempo_ejecucion = (time.time() - inicio) * 1000
        logger.info(f"{func.__name__} se ejecuto en {tiempo_ejecucion:.2f} milisegundos")

        return resultado
    return wrapper


class GestorTareas:
    def __init__(self):
        self.tareas: Dict[str, str] = {} # Diccionario para almacenar las tareas
        self.logger = logging.getLogger(__name__)

    @medir_tiempo
    def add_task(self, name: str, descripcion: str):
        self.logger.debug(f"Intentando añadir tarea: {name}")
        name = name.lower().strip()
        descripcion = descripcion.lower().strip()
        if name in self.tareas:
            self.logger.warning(f"Tarea ya existe: {name}. Sobreescribiendo tarea")
            del self.tareas[name]
        
        self.tareas[name] = descripcion
        
        self.logger.info(f"Tarea añadida: {name}")
        self.logger.debug(f"Total de tareas: {len(self.tareas)}")
    
    @medir_tiempo
    def delete_task(self, name: str):
        self.logger.debug(f"Intentando eliminar tarea: '{name}'")
        name = name.lower().strip()

        if name not in self.tareas:
            self.logger.error(f"No se puede eliminar. La tarea '{name}' no existe")
            return
        
        del self.tareas[name]
        
        self.logger.info(f"Tarea '{name}' eliminada correctamente")
        self.logger.debug(f"Tareas restantes: {len(self.tareas)}")

    @medir_tiempo
    def listar_tareas(self):
        self.logger.info("=== Listando tareas ===")
        
        if not self.tareas:
            self.logger.warning("No hay tareas en el sistema")
            return
        
        self.logger.debug(f"Se encontraron {len(self.tareas)} tareas")
        
        for name, descripcion in self.tareas.items():
            print(f"- {name}: {descripcion}")
            self.logger.debug(f"Tarea listada: {name}")
        



def main():
    gestor = GestorTareas()


    print("\n=== Añadiendo tareas ===")
    gestor.add_task("Estudiar Python", "Repasar logging y decoradores")
    gestor.add_task("Hacer ejercicio", "30 minutos de cardio")
    gestor.add_task("Leer libro", "Continuar con Clean Code")
    gestor.add_task("Estudiar Python", "Nueva descripción")

    
    print("\n=== Listando tareas ===")
    gestor.listar_tareas()
    
    print("\n=== Eliminando tarea ===")
    gestor.delete_task("Hacer ejercicio")
    gestor.delete_task("Leer")
    
    print("\n=== Intentando eliminar tarea inexistente ===")
    gestor.delete_task("Tarea que no existe")
    
    print("\n=== Listando tareas actualizadas ===")
    gestor.listar_tareas()
    
    print("\n=== Añadiendo tarea duplicada ===")
    gestor.add_task("Estudiar Python", "Nueva descripción")

if __name__ == "__main__":
    main()