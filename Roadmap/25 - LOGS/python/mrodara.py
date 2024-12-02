### LOGS EN PYTHON

'''
El módulo logging en Python proporciona una forma flexible y potente de registrar mensajes en tus aplicaciones. 
Es especialmente útil para depurar, monitorear y registrar eventos importantes en aplicaciones pequeñas o grandes.
'''

# Permite monitorear eventos para niveles de registro, salidas de registro y formato.
import logging

# Configuración básica de logging con basicConfig
logging.basicConfig(level=logging.DEBUG)

# Mostramos ejemplos de todos los niveles
logging.debug('Este mensaje es de nivel DEBUG')
logging.info('Este mensaje es de nivel INFO')
logging.warning('Este mensaje es de nivel WARNING')
logging.error('Este mensaje es de nivel ERROR')
logging.critical('Este mensaje es de nivel CRITICAL')

# Podemos darle formato a los mensajes de log, por ejemplo para indicar fechas del mensaje
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

logging.info('Este mensaje es de nivel INFO')
logging.warning('Este mensaje es de nivel WARNING')
logging.error('Este mensaje es de nivel ERROR')


### EJERCICIO EXTRA
class Tareas():
    
    def __init__(self):
        self.tasks = []
        
    def list_tasks(self):
        
        if len(self.tasks) > 0:
            logging.info("Solictud listar tareas")
            print(list(self.tasks))
            logging.info("Fin Solictud listar tareas")
        else:
            logging.warning("Solicitud listar tareas")
            print("No hay tareas para mostrar")
            logging.warning("Fin Solicitud listar tareas")

    def add_task(self, name: str, description: str):
        logging.info("Solicitud agregar tarea")
        self.tasks.append({"name": name, "description": description})
        print(f"Tarea agregada: {name} - {description}")
        logging.info("Fin Solicitud agregar tarea")
        
    def delete_task(self, name: str):
        
        logging.warning("Inicio solicitud eliminar tarea")
        
        for task in self.tasks:
                      
            if task['name'].lower() == name.lower():
                    self.tasks.remove(task)
                    print(f"Tarea eliminada: {name}")
                    break
                        
        logging.warning("Fin solicitud eliminar tarea")


my_tasks = Tareas()

my_tasks.list_tasks()
my_tasks.add_task("Tarea 1", "Actualizar gestor de dependencias")
my_tasks.add_task("Tarea 2", "Instalar paquetes necesarios")
my_tasks.list_tasks()
my_tasks.delete_task("Tarea 2")
### FIN EJERCICIO EXTRA

### FIN LOGS EN PYTHON

