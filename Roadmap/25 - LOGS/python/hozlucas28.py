# pylint: disable=pointless-string-statement,missing-module-docstring,missing-class-docstring,missing-function-docstring

import logging

from time import time
from typing import TypedDict, Self


"""
    Logging...
"""

print("Logging...")

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s (%(levelname)s): %(message)s"
)

print("\nlogging.critical(msg=<MESSAGE>)...\n")
logging.critical(msg="Critical log message!")

print("\nlogging.debug(msg=<MESSAGE>)...\n")
logging.debug(msg="Debug log message!")

print("\nlogging.error(msg=<MESSAGE>)...\n")
logging.error(msg="Error log message!")

print("\nlogging.info(msg=<MESSAGE>)...\n")
logging.info(msg="Information log message!")

print("\nlogging.warning(msg=<MESSAGE>)...\n")
logging.warning(msg="Warning log message!")


print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)


"""
    Additional challenge...
"""

print("Additional challenge...")

type Description = str
type Title = str

Task = TypedDict(
    "Task",
    {
        "description": Description,
        "title": Title,
    },
)


class TaskManager:
    __debug: bool
    __tasks: list[Task]

    def __init__(
        self, *, initial_tasks: None | list[Task] = None, enableDebug=False
    ) -> None:
        self.__debug = enableDebug
        self.__tasks = [] if initial_tasks is None else initial_tasks

    def add_task(self, *, new_task: Task) -> Self:
        if self.__debug:
            print()
            logging.debug(msg="addTask (method) start execution...")
            start_time: float = time()

        self.__tasks.append(new_task)

        if self.__debug:
            logging.debug(msg="addTask (method) ends execution!")
            print(f"addTask: {time()-start_time} seconds")

        return self

    def delete_task_by_title(self, *, title: Title) -> Self:
        if self.__debug:
            print()
            start_time: float = time()
            logging.debug(msg="delete_task_by_title (method) start execution...")

        sanitized_tasks: list[Task] = []
        sanitized_title: str = title.strip().upper()

        for task in self.__tasks:
            if task["title"].strip().upper() != sanitized_title:
                sanitized_tasks.append(task)

        self.__tasks = sanitized_tasks

        if self.__debug:
            logging.debug(msg="delete_task_by_title (method) ends execution!")
            print(f"delete_task_by_title: {time()-start_time} seconds")

        return self

    def print_tasks(self) -> Self:
        if self.__debug:
            print()
            logging.debug(msg="print_tasks (method) start execution...")
            start_time: float = time()
            print()

        for task in self.__tasks:
            print(task)

        if self.__debug:
            print()
            logging.debug(msg="print_tasks (method) ends execution!")
            print(f"print_tasks: {time()-start_time} seconds")

        return self


task_manager: TaskManager = TaskManager(enableDebug=True)

EXIT_: bool = False

while not EXIT_:
    operation: str = input(
        "\nWrite an operation ('Add task', 'Delete task by title', 'Print tasks', or 'Exit'): "
    )

    sanitized_operation: str = operation.strip().upper()

    match sanitized_operation:
        case "ADD TASK":

            task_title: str = input("\nTask title: ")
            task_description: str = input("Task description: ")

            task_manager.add_task(
                new_task={
                    "title": task_title.strip(),
                    "description": task_description.strip(),
                }
            )

        case "DELETE TASK BY TITLE":
            task_title: str = input("\nTask title: ")

            task_manager.delete_task_by_title(title=task_title)

        case "PRINT TASKS":
            task_manager.print_tasks()

        case "EXIT":
            EXIT_ = True
            print("\nApplication closed!")

        case _:
            print("\nInvalid operation! Try again...")
