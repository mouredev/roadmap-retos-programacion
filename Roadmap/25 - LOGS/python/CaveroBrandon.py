""""EJERCICIO:
Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
un ejemplo con cada nivel de "severidad" disponible."""

import logging
import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logging.debug('Detailed information, typically of interest only when diagnosing problems.')
logging.info('Confirmation that things are working as expected.')
logging.warning('An indication that something unexpected happened, or indicative of some problem in the near future'
                ' (e.g. ‘disk space low’). The software is still working as expected.')
logging.error('Due to a more serious problem, the software has not been able to perform some function.')
logging.critical('A serious error, indicating that the program itself may be unable to continue running.')

"""DIFICULTAD EXTRA (opcional):
Crea un programa ficticio de gestión de tareas que permita añadir, eliminar y listar dichas tareas.
- Añadir: recibe nombre y descripción.
- Eliminar: por nombre de la tarea.
Implementa diferentes mensajes de log que muestren información según la tarea ejecutada (a tu elección).
Utiliza el log para visualizar el tiempo de ejecución de cada tarea."""


class TaskManager:
    def __init__(self):
        self.tasks = {'Some': '123', 'other': '133'}

    def add_task(self, name: str, description: str):
        start_time = time.time()
        try:
            self.tasks[name] = description
            logging.info(f'New task successfully added: {name}')
        except Exception as e:
            logging.error(f'Error adding a new task: {e}')
        end_time = time.time()
        self.execution_time(start_time, end_time)

    def list_tasks(self):
        start_time = time.time()
        logging.info(f'The available tasks are:')
        try:
            for task, description in self.tasks.items():
                logging.info(f'{task}: {description}')
            logging.info('Task list was successfully printed')
        except Exception as e:
            logging.error(f'Error: {e}')
        end_time = time.time()
        self.execution_time(start_time, end_time)

    def remove_task(self, name: str):
        start_time = time.time()
        if name not in self.tasks:
            logging.info(f'The task "{name}" was not found in the task list')
            return
        else:
            del self.tasks[name]
            logging.info(f'The task "{name}" was successfully removed from the task list')
        end_time = time.time()
        self.execution_time(start_time, end_time)

    def execution_time(self, start_time, end_time):
        logging.debug(f'Execution time: {end_time - start_time:.6f} seconds')


def select_option():
    try:
        logging.info('Enter an option: ')
        option = int(input())
        if option == 1:
            logging.info('***** TASK LIST *****')
            task_manager.list_tasks()
            show_menu()
        elif option == 2:
            logging.info('***** ADD A NEW TASK *****')
            logging.info('Enter the task name: ')
            name = input()
            logging.info('Enter the task description: ')
            description = input()
            task_manager.add_task(name=name, description=description)
            show_menu()
        elif option == 3:
            logging.info('***** REMOVE A TASK *****')
            logging.info('Enter the task name to remove: ')
            name = input()
            task_manager.remove_task(name=name)
            show_menu()
        elif option == 4:
            logging.info('Program terminated')
        else:
            logging.warning('Incorrect option was entered')
            show_menu()
    except ValueError:
        logging.warning('Incorrect value entered, try again')
        show_menu()


def show_menu():
    logging.info('********** MENU ************')
    logging.info('1. Show available tasks')
    logging.info('2. Add new task')
    logging.info('3. Remove task')
    logging.info('4. Exit')
    select_option()


task_manager = TaskManager()
show_menu()
