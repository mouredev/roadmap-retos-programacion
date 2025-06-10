import logging

# -- exercise
logging.basicConfig(level=logging.DEBUG)

# Log messages with different severity levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


# -- extra challenge
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        task = {"name": name, "description": description}
        self.tasks.append(task)
        logging.info(f"Task '{name}' added")

    def delete_task(self, name):
        for task in self.tasks:
            if task["name"] == name:
                self.tasks.remove(task)
                logging.info(f"Task '{name}' deleted")
                break
        else:
            logging.warning(f"Task '{name}' not found")

    def list_tasks(self):
        for task in self.tasks:
            logging.info(f"Task: {task['name']}, Description: {task['description']}")


task_manager = TaskManager()

task_manager.add_task("Task 1", "Description 1")
task_manager.add_task("Task 2", "Description 2")

task_manager.delete_task("Task 1")

task_manager.list_tasks()
