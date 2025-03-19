import logging
import time

# Configurar el logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Ejemplos de mensajes de logging en diferentes niveles de severidad
logging.debug('Este es un mensaje de depuración.')
logging.info('Este es un mensaje informativo.')
logging.warning('Este es un mensaje de advertencia.')
logging.error('Este es un mensaje de error.')
logging.critical('Este es un mensaje crítico.')

### Ejercicio Extra ###

class TaskManager:
    
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        start_time = time.time()
        self.tasks.append({'name': name, 'description': description})
        logging.info(f'Task added: {name}')
        logging.debug(f'Time taken to add task: {time.time() - start_time} seconds')

    def remove_task(self, name):
        start_time = time.time()
        for task in self.tasks:
            if task['name'] == name:
                self.tasks.remove(task)
                logging.info(f'Task remove: {name}')
                logging.debug(f'Time taken to remove task: {time.time() - start_time} seconds')
                return
            
        logging.warninig(f'Task not found: {name}')
        logging.debug(f'Time taken to attempt to remove task: {time.time() - start_time} seconds')

    def list_tasks(self):
        start_time = time.time()
        for task in self.tasks:
            print(f"Task: {task['name']}, Description: {task['description']}")
        logging.info(f'Listed {len(self.tasks)} tasks')
        logging.debug(f'Time taken to list tasks: {time.time() - start_time} seconds')


manager = TaskManager()
manager.add_task('Task 1', 'Study Python')
manager.add_task('Task 2', 'Study JavaScript')
manager.add_task('Task 3', 'Study Java')
manager.list_tasks()
manager.remove_task('Task 1')
manager.list_tasks()


