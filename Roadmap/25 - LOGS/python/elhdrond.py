import logging
import time

"""
LOGS
"""

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

logging.debug("Detailed diagnostic information, useful during development.")
logging.info("Application started successfully.")
logging.warning("Disk space is running low — consider cleaning up old files.")
logging.error("Failed to connect to the database.")
logging.critical("System is out of memory. Shutting down.")


"""
    EXTRA EXERCISE
"""


class TaskManager:
    def __init__(self) -> None:
        self.tasks = {}

    def add_task(self, name: str, description: str):
        start_time = time.time()
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Task added: {name}.")
        else:
            logging.warning(f"Task already exists: {name}.")
        logging.debug(f"Total tasks: {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def delete_task(self, name: str):
        start_time = time.time()
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Task deleted: {name}.")
        else:
            logging.error(f"Task not found: {name}.")
        logging.debug(f"Total tasks: {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def list_tasks(self):
        start_time = time.time()
        if self.tasks:
            logging.info("Listing all tasks.")
            for name, description in self.tasks.items():
                print(f"{name} - {description}")
        else:
            logging.info("No tasks to display.")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def _print_time(self, start_time, end_time):
        logging.debug(f"Execution time: {end_time - start_time:.6f} seconds.")


task_manager = TaskManager()
task_manager.list_tasks()
task_manager.add_task("Deploy API", "Deploy the new API version to production")
task_manager.add_task("Write Tests", "Add unit tests for the payment module")
task_manager.add_task("Code Review", "Review open pull requests on GitHub")
task_manager.list_tasks()
task_manager.delete_task("Write Tests")
task_manager.list_tasks()
task_manager.add_task("Deploy API", "Deploy the new API version to production")
task_manager.delete_task("Fix Bug")
