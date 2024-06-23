"""
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
"""

import logging

# Logging configuration
logging.basicConfig(level=logging.DEBUG,
                    filename='example.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )

# Examples of each level of severity
logging.debug('This is a DEBUG message')
logging.info('This is a INFO message')
logging.warning('This is a WARNING message')
logging.error('This is a ERROR message')
logging.critical('This is a CRITICAL message')

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la 
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
"""

class Task:
    def __init__(self, name, description, finalized=False, final_date=None):
        self.name = name
        self.description = description
        self.finalized = finalized
        self.final_date = final_date
        

class Task_manager():

    def __init__(self):
        self.tasks = []  # List to store tasks as dictionaries


    def add_task(self, task: Task):
        self.tasks.append(
            {
                'name': task.name,
                'description': task.description,
                'finalized': task.finalized,
                'final_date': task.final_date
             }
             )
        logging.info(f'Task added.')


    def delete_task(self, name: str):
        for task in self.tasks:
            if task['name'] == name:
                self.tasks.remove(task)
                logging.info(f'Task deleted.')
                return
        logging.warning(f'Task was not fouded.')


    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def change_to_finalized(self, name: str):
        for task in self.tasks:
            if task['name'] == name:
                task['finalized'] = True
                logging.info(f'Task finalized.')
                return
        logging.warning(f'Task was not fouded.')

task1 = Task('Task1', 'Description of task 1')
task2 = Task('Task2', 'Description of task 2', final_date='2024-06-23')

task_manager = Task_manager()
task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.list_tasks()
task_manager.delete_task('Task1') # Task deleted
task_manager.list_tasks()
task_manager.delete_task('Task3') # Task not found
task_manager.change_to_finalized('Task2')

task_manager.list_tasks()