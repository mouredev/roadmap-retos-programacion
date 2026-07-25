#25 { Retos para Programadores } LOGS 

# Bibliography reference
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
* EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.

 """

log = print
log('Retos para Programadores #25')

import logging
import time

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define logging functions
def log_debug(message):
    logging.debug(f"DEBUG: {message}")

def log_info(message):
    logging.info(f"INFO: {message}")

def log_warning(message):
    logging.warning(f"WARNING: {message}")

def log_error(message):
    logging.error(f"ERROR: {message}")

def log_critical(message):
    logging.critical(f"CRITICAL: {message}")

# Example usage of logging
log_info("Retosparaprogramadores #25.") # 2024-12-25 11:54:13,185 - INFO - INFO: Retosparaprogramadores #25.
log_debug("This is a debug message.") # 2024-12-25 11:54:13,186 - DEBUG - DEBUG: This is a debug message.
log_info("This is an informational message.") # 2024-12-25 11:54:13,186 - INFO - INFO: This is an informational message.
log_warning("This is a warning message.") # 2024-12-25 11:54:13,186 - WARNING - WARNING: This is a warning message.
log_error("This is an error message.") # 2024-12-25 11:54:13,186 - ERROR - ERROR: This is an error message.
log_critical("This is a critical message.") # 2024-12-25 11:54:13,186 - CRITICAL - CRITICAL: This is a critical message.

# Task Manager class
class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, description):
        start_time = time.time()
        if name in self.tasks:
            log_warning(f"The task '{name}' already exists.")
            self.prompt_edit_task(name)
            return
        self.tasks[name] = description
        log_info(f"Task added: {name} - {description}")
        end_time = time.time()
        log_debug(f"Execution time for adding task: {(end_time - start_time):.2f} seconds")

    def prompt_edit_task(self, name):
        answer = input(f"The task '{name}' already exists. Do you want to edit it? (yes/no): ")
        if answer.lower() == 'yes':
            new_description = input('Enter the new description: ')
            self.edit_task(name, new_description)
        else:
            log_info(f"No changes made to the task '{name}'.")

    def edit_task(self, name, new_description):
        start_time = time.time()
        if name not in self.tasks:
            log_error(f"Could not edit the task '{name}' because it does not exist.")
            return
        self.tasks[name] = new_description
        log_info(f"Task edited: {name} - New Description: {new_description}")
        end_time = time.time()
        log_debug(f"Execution time for editing task: {(end_time - start_time):.2f} seconds")

    def remove_task(self, name):
        start_time = time.time()
        if name not in self.tasks:
            log_error(f"Could not remove the task '{name}' because it does not exist.")
            return
        del self.tasks[name]
        log_info(f"Task removed: {name}")
        end_time = time.time()
        log_debug(f"Execution time for removing task: {(end_time - start_time):.2f} seconds")

    def list_tasks(self):
        start_time = time.time()
        if not self.tasks:
            log_warning("No tasks to display.")
            return
        log_info("Task list:")
        for name, description in self.tasks.items():
            log_info(f"- {name}: {description}")
        end_time = time.time()
        log_debug(f"Execution time for listing tasks: {(end_time - start_time):.2f} seconds")

# Example usage of TaskManager
manager = TaskManager()
manager.add_task("Implement User Authentication", "Develop a user authentication system that allows users to register, log in, and log out securely.")
manager.add_task("Fix Bug in Feature Resize window", "Fix Bug in Feature Resize window")
manager.add_task("Write Unit Tests", "Write Unit Tests - Create tests for the user authentication module using Jest.")
manager.add_task("Refactor Code for Module Lang_translation", "Refactor Code for Module Lang_translation - Simplify the logic and remove redundant code.")
manager.add_task("Deploy Application to Production", "Deploy Application to Production - Set up CI/CD pipeline and deploy the latest build.")
manager.list_tasks()
manager.remove_task("Implement User Authentication")
manager.edit_task("Fix Bug in Feature Resize window", "Fix Bug in Feature Resize window - Resolve the issue causing the application to crash on submission.")
manager.list_tasks()

# Output:
"""  
2024-12-25 11:54:13,187 - INFO - INFO: Task added: Implement User Authentication - Develop a user authentication system that allows users to register, log in, and log out securely.
2024-12-25 11:54:13,187 - DEBUG - DEBUG: Execution time for adding task: 0.00 seconds
2024-12-25 11:54:13,187 - INFO - INFO: Task added: Fix Bug in Feature Resize window - Fix Bug in Feature Resize window
2024-12-25 11:54:13,187 - DEBUG - DEBUG: Execution time for adding task: 0.00 seconds
2024-12-25 11:54:13,188 - INFO - INFO: Task added: Write Unit Tests - Write Unit Tests - Create tests for the user authentication module using Jest.
2024-12-25 11:54:13,188 - DEBUG - DEBUG: Execution time for adding task: 0.00 seconds
2024-12-25 11:54:13,188 - INFO - INFO: Task added: Refactor Code for Module Lang_translation - Refactor Code for Module Lang_translation - Simplify the logic and remove redundant code.
2024-12-25 11:54:13,188 - DEBUG - DEBUG: Execution time for adding task: 0.00 seconds
2024-12-25 11:54:13,188 - INFO - INFO: Task added: Deploy Application to Production - Deploy Application to Production - Set up CI/CD pipeline and deploy the latest build.
2024-12-25 11:54:13,188 - DEBUG - DEBUG: Execution time for adding task: 0.00 seconds
2024-12-25 11:54:13,189 - INFO - INFO: Task list:
2024-12-25 11:54:13,189 - INFO - INFO: - Implement User Authentication: Develop a user authentication system that allows users to register, log in, and log out securely.
2024-12-25 11:54:13,189 - INFO - INFO: - Fix Bug in Feature Resize window: Fix Bug in Feature Resize window
2024-12-25 11:54:13,189 - INFO - INFO: - Write Unit Tests: Write Unit Tests - Create tests for the user authentication module using Jest.
2024-12-25 11:54:13,189 - INFO - INFO: - Refactor Code for Module Lang_translation: Refactor Code for Module Lang_translation - Simplify the logic and remove redundant code.
2024-12-25 11:54:13,189 - INFO - INFO: - Deploy Application to Production: Deploy Application to Production - Set up CI/CD pipeline and deploy the latest build.
2024-12-25 11:54:13,191 - DEBUG - DEBUG: Execution time for listing tasks: 0.00 seconds
2024-12-25 11:54:13,191 - INFO - INFO: Task removed: Implement User Authentication
2024-12-25 11:54:13,191 - DEBUG - DEBUG: Execution time for removing task: 0.00 seconds
2024-12-25 11:54:13,191 - INFO - INFO: Task edited: Fix Bug in Feature Resize window - New Description: Fix Bug in Feature Resize window - Resolve the issue causing the application to crash on submission.
2024-12-25 11:54:13,191 - DEBUG - DEBUG: Execution time for editing task: 0.00 seconds
2024-12-25 11:54:13,191 - INFO - INFO: Task list:
2024-12-25 11:54:13,191 - INFO - INFO: - Fix Bug in Feature Resize window: Fix Bug in Feature Resize window - Resolve the issue causing the application to crash on submission.
2024-12-25 11:54:13,192 - INFO - INFO: - Write Unit Tests: Write Unit Tests - Create tests for the user authentication module using Jest.
2024-12-25 11:54:13,192 - INFO - INFO: - Refactor Code for Module Lang_translation: Refactor Code for Module Lang_translation - Simplify the logic and remove redundant code.
2024-12-25 11:54:13,192 - INFO - INFO: - Deploy Application to Production: Deploy Application to Production - Set up CI/CD pipeline and deploy the latest build.
2024-12-25 11:54:13,192 - DEBUG - DEBUG: Execution time for listing tasks: 0.00 seconds 

"""
