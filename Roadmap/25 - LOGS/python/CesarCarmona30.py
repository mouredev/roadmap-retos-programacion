import logging
import time

'''
  EJERCICIO
'''

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

logging.debug('Esto es un mensaje de DEBUG')
logging.info('Esto es un mensaje de INFO')
logging.warning('Esto es un mensaje de WARNING')
logging.error('Esto es un mensaje de ERROR')
logging.critical('Esto es un mensaje de CRITICAL')

'''
  EXTRA
'''

class TaskManager:
  def __init__(self) -> None:
    self.tasks = {}

  def add_task(self, name, description):
    start_time = time.time()
    if name not in self.tasks:
      self.tasks[name] = description
      logging.info(f"Tarea añadida: {name}.")
    else:
      logging.warning(
        f"Se ha intentado añadir una tarea que ya existe: {name}.")
    logging.debug(f"Número de tareas: {len(self.tasks)}")
    end_time = time.time()
    self._print_time(start_time, end_time)

  def delete_task(self, name):
    start_time = time.time()
    if name in self.tasks:
      del self.tasks[name]
      logging.info(f"Se ha eliminado la tarea: {name}.")
    else:
      logging.error(
        f"Se ha intentado eliminar una tarea que no existe: {name}.")
    logging.debug(f"Número de tareas: {len(self.tasks)}")
    end_time = time.time()
    self._print_time(start_time, end_time)

  def list_tasks(self):
    start_time = time.time()
    if self.tasks:
      logging.info(f"Lista de tareas: ")
      for name, description in self.tasks.items():
        print(f"{name} - {description}")
    else:
      logging.info("No hay tareas para mostrar.")
    end_time = time.time()
    self._print_time(start_time, end_time)

  def _print_time(self, start_time, end_time):
    logging.debug(
      f"Tiempo de ejecución {end_time - start_time:.6f} seg." )
    
task_manager = TaskManager()
task_manager.list_tasks()
task_manager.add_task("Pan", "Comprar 5 barras de pan")
task_manager.add_task("Python", "Estudiar Python")
task_manager.list_tasks()
task_manager.delete_task("Python")
task_manager.list_tasks()
task_manager.add_task("Pan", "Comprar 5 barras de pan")
task_manager.delete_task("Python")