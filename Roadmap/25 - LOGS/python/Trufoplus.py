###############################################################################
###     EJERCICIO
###############################################################################
import logging
from datetime import datetime

# Configuracion basica de un logginf
logging.basicConfig(
    #filename='my_log.log',          # Nombre del archivo de log, si no lo especificas se mostrara por consola 
    filemode='w',                   # Modo fe apertura del archivo
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  #Formato del mesaje
    datefmt='%d/%m/%Y %H:%M:%S',    # Formato de la fecha
    level=logging.DEBUG             # Nivel de severidad minimo
    )


# Uso del logging

logging.debug('Esto es un mensaje de depuración')
logging.info('Esto es un mensaje informativo')
logging.warning('Esto es una advertencia')
logging.error('Esto es un mensaje de error')
logging.critical('Esto es un mensaje crítico')
# Para separar los ejerccios en la consola
print()
print()
print()
###############################################################################
###     DIFICULTAD EXTRA
###############################################################################
class TaskManagement():
    """
    Programa de gestion de tareas
    """
    def __init__(self):
        self.tasks = {}
        logging.info("Inicialización del programa de gestión de tareas")

    def add_task(self, name: str, description: str):
        start_time = datetime.now()
        if name in self.tasks:
            logging.warning(f"La tarea '{name}' ya existe. No se puede agregar de nuevo.")
            return
        self.tasks[name] = description
        logging.info(f"Tarea '{name}' añadida con éxito.")
        logging.debug(f"Descripción: {description}")
        end_time = datetime.now()
        logging.info(f"Tiempo de ejecución para añadir tarea: {end_time - start_time}")

    def delete_task(self, name: str):
        start_time = datetime.now()
        if name not in self.tasks:
            logging.error(f"La tarea '{name}' no existe. No se puede eliminar.")
            return
        del self.tasks[name]
        logging.info(f"Tarea '{name}' eliminada con éxito.")
        end_time = datetime.now()
        logging.info(f"Tiempo de ejecución para eliminar tarea: {end_time - start_time}")
    
    def __str__(self):
        print("\nLISTA DE TAREAS: ")
        return "\n".join([f"{name}: {desc}" for name, desc in self.tasks.items()])
    

# Probando el codigo
mis_tareas = TaskManagement()
mis_tareas.add_task('Tarea_1', 'Limpiar el polvo')
mis_tareas.add_task('Tarea_2', 'Limpiar los baños')
mis_tareas.add_task('Tarea_2', 'Limpiar los baños')
print(mis_tareas)
mis_tareas.delete_task('Tarea_1')
mis_tareas.add_task('Tarea_3', 'Limpiar la cocina')
print(mis_tareas)
mis_tareas.delete_task('Tarea_4')