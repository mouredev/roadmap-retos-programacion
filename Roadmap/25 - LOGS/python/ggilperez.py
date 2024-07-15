# Logs
import logging
import time

logging.basicConfig()  # By default warning level


def print_logs():
    logging.debug("This is a debug level log")
    logging.info("This is a info level log")
    logging.warning("This is a warning level log")
    logging.error("This is a error level log")
    logging.critical("This is a critical level log")

print_logs()

logging.getLogger().setLevel(logging.DEBUG)
print_logs()

# EXTRA

class TaskManager:

    def __init__(self):
        self.tasks = {}

    def add_task(self, name, description):
        start = time.time()
        if name not in self.tasks:
            logging.info(f"adding task {name}")
            self.tasks[name] = description
        else:
            logging.error(f"task {name} already exists")
        end = time.time()
        logging.debug(f"adding task time {end-start}s")

    def remove_tasks(self, name):
        start = time.time()
        if name in self.tasks:
            logging.info(f"removing task {name}")
            self.tasks.pop(name)
        else:
            logging.error(f"task {name} not found")
        end = time.time()
        logging.debug(f"removing task time {end-start}s")

    def list_tasks(self):
        start = time.time()
        for key, value in self.tasks.items():
            print(f"Task: {key}. Description: {value}")
        end = time.time()
        logging.debug(f"listing task time {end-start}s")


task_manager = TaskManager()
task_manager.add_task("SW Acolyte", "New episode wednesday")
task_manager.add_task("Do house", "Clean")
task_manager.list_tasks()
task_manager.remove_tasks("SW Acolyte")
task_manager.list_tasks()
task_manager.add_task("Acolyte", "Create review")
task_manager.remove_tasks("Do house")
