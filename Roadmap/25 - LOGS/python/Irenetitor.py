import logging
import time
from functools import wraps

#Exercise

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")


#Extra Exercise


logger = logging.getLogger(__name__)

#Decorator
def log_execution_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        logger.debug(
            f"Method '{func.__name__}' completed in {duration:.6f} seconds"
        )
        return result
    return inner


class TaskRegistry:
    def __init__(self):
        self._storage: dict[str, str] = {}

    @log_execution_time
    def create(self, title: str, details: str) -> None:
        if title in self._storage:
            logger.warning(f"Task '{title}' already exists.")
            return

        self._storage[title] = details
        logger.info(f"Task '{title}' successfully created.")
        logger.debug(f"Current task count: {len(self._storage)}")

    @log_execution_time
    def remove(self, title: str) -> None:
        if title not in self._storage:
            logger.error(f"Task '{title}' was not found.")
            return

        del self._storage[title]
        logger.info(f"Task '{title}' removed.")
        logger.debug(f"Current task count: {len(self._storage)}")

    @log_execution_time
    def show_all(self) -> None:
        if not self._storage:
            logger.info("Task list is empty.")
            return

        logger.info("Displaying registered tasks:")
        for title, details in self._storage.items():
            print(f"* {title} -> {details}")


if __name__ == "__main__":
    registry = TaskRegistry()

    registry.show_all()
    registry.create("Groceries", "Buy fruits and vegetables")
    registry.create("Workout", "30 minutes of cardio")
    registry.show_all()
    registry.remove("Workout")
    registry.show_all()
    registry.create("Groceries", "Duplicate test")
    registry.remove("Reading")
