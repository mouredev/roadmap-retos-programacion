import logging
import time
"""
Ejercicio
"""

logging.basicConfig(level=logging.DEBUG, 
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.StreamHandler()]
                    )

logging.debug("Esto es un mensaje de DEBUG")
logging.info("Esto es un mensaje de INFO")
logging.warning("Esto es un mensaje de WARNING")
logging.error("Esto es un mensaje de ERROR")
logging.critical("Esto es un mensaje de CRITICAL")


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

    
class TaskManager:
    
    def __init__(self) -> None:
        self.tasks = {}
    
    def add_task(self, name: str, description: str):
        star_time = time.time()
        if name not in self.tasks:
           self.tasks[name] = description
           logging.info(f"Tarea añadida: {name}") 
        else:
            logging.warning(f"Se ha intentado añadir una tarea existente {name}")
        end_time = time.time()
        print(end_time - star_time)
    def delete_task(self, name: str):
        star_time = time.time()
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Tarea eliminada: {name}")
        else:
            logging.error(f"Se ha intentando eliminar una tarea que no existe: {name}")
        end_time = time.time() 
        print(end_time - star_time) 
    def list_task(self):
        star_time = time.time()
        if self.tasks:
            logging.info(f"Se va a imprimir la lista de tareas")
            for name, description in self.tasks.items():
                print(f"{name} - {description}")
        else:
            logging.error("Lista de tareas inexistente")
        end_time = time.time()  
        print(end_time - star_time)
         
task_manager = TaskManager()
task_manager.list_task()
task_manager.add_task("Pan", "Comprar 5 barras de pan")
task_manager.add_task("Python", "Estudiar python")
task_manager.add_task("Python", "Estudiar python")
task_manager.list_task()
task_manager.delete_task("Python")
task_manager.list_task()