"""
    Classes...
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class Employee:
    """Employee class"""

    _first_name: str
    _last_name: str
    _salary: int

    def set_first_name(self, first_name: str):
        """Set a new first name"""
        self._first_name = first_name
        return self

    def set_last_name(self, last_name: str):
        """Set a new last name"""
        self._last_name = last_name
        return self

    def set_salary(self, salary: str):
        """Set a new salary"""
        self._salary = salary
        return self

    def get_first_name(self) -> str:
        """Return first name"""
        return self._first_name

    def get_last_name(self) -> str:
        """Return last name"""
        return self._last_name

    def get_salary(self) -> str:
        """Return salary"""
        return self._salary

    def print_attributes(self):
        """Print attributes values"""
        print(f'\nFirst name --> "{self._first_name}"')
        print(f'Last name --> "{self._last_name}"')
        print(f"Salary --> {self._salary}")
        return self


print("Classes in Python...\n")

print(
    '''from dataclasses import dataclass
from typing import Any


@dataclass
class Employee:
    """Employee class"""

    _first_name: str
    _last_name: str
    _salary: int

    def set_first_name(self, first_name: str):
        """Set a new first name"""
        self._first_name = first_name
        return self

    def set_last_name(self, last_name: str):
        """Set a new last name"""
        self._last_name = last_name
        return self

    def set_salary(self, salary: str):
        """Set a new salary"""
        self._salary = salary
        return self

    def get_first_name(self) -> str:
        """Return first name"""
        return self._first_name

    def get_last_name(self) -> str:
        """Return last name"""
        return self._last_name

    def get_salary(self) -> str:
        """Return salary"""
        return self._salary

    def print_attributes(self):
        """Print attributes values"""
        print(f'\\nFirst name --> \\"{self._first_name}\\"')
        print(f'Last name --> \\"{self._last_name}\\"')
        print(f"Salary --> {self._salary}")
        return self'''
)

print('\nemployee = Employee("Lucas", "Hoz", 2300)')

my_employee = Employee("Lucas", "Hoz", 2300)

print("\nEmployee attributes...")
my_employee.print_attributes()

my_employee.set_first_name("Nahuel")
print('\nemployee.set_first_name("Nahuel")')

print("\nEmployee attributes...")
my_employee.print_attributes()

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")


# Stack exercise...
class Stack:
    """Stack class"""

    def __init__(self, stack: list[Any]) -> None:
        if stack is None:
            stack = []
        stack_length: int = len(stack)

        self._last_element: Any | None = stack[-1] if (stack_length > 0) else None
        self._length: int = stack_length
        self._stack: list[Any] = stack

    def get_stack(self) -> list[Any]:
        """Return stack"""
        return self._stack

    def get_length(self) -> int:
        """Return length"""
        return self._length

    def get_last_element(self) -> Any | None:
        """Return last element"""
        return self._last_element

    def append_element(self, element: any):
        """Append element at the end"""
        self._stack.append(element)
        self._last_element = element
        self._length = len(self._stack)
        return self

    def delete_last_element(self):
        """Delete last element"""
        self._stack.pop()
        self._length = len(self._stack)
        self._last_element = self._stack[-1] if (self._length > 0) else None
        return self

    def print_attributes(self):
        """Print attributes values"""
        print(f"\nLast element --> {self._last_element}")
        print(f"Length --> {self._length}")
        print(f"Stack --> {self._stack}")
        return self


my_stack = Stack(["Lucas", "Nahuel"])
my_stack.append_element("Buenos Aires")

print("\nStack attributes...")
my_stack.print_attributes()

my_stack.delete_last_element().delete_last_element()

print("\nStack attributes...")
my_stack.print_attributes()

my_stack.delete_last_element()

print("\nStack attributes...")
my_stack.print_attributes()


# Queue exercise...
class Queue:
    """Queue class"""

    def __init__(self, queue: list[Any]) -> None:
        if queue is None:
            queue = []
        queue_length: int = len(queue)

        self._length: int = queue_length
        self._queue: list[Any] = queue
        self._first_element: Any | None = queue[0] if queue_length > 0 else None

    def get_length(self) -> int:
        """Return length"""
        return self._length

    def get_queue(self) -> list[Any]:
        """Return queue"""
        return self._queue

    def get_first_element(self) -> Any:
        """Return first element"""
        return self._first_element

    def append_element(self, element: Any):
        """Append element at the end"""
        self._queue.append(element)
        self._length = len(self._queue)
        return self

    def delete_first_element(self):
        """Delete first element"""
        self._queue = self._queue[1:]
        self._length = len(self._queue)
        self._first_element = self._queue[0] if (self._length > 0) else None
        return self

    def print_attributes(self):
        """Print attributes values"""
        print(f"\nLength --> {self._length}")
        print(f"Queue --> {self._queue}")
        print(f"First element --> {self._first_element}")
        return self


my_queue = Queue(["Estados Unidos", "Miami"])

my_queue.append_element("Beach")

print("\nQueue attributes...")
my_queue.print_attributes()

my_queue.delete_first_element().delete_first_element()

print("\nQueue attributes...")
my_queue.print_attributes()

my_queue.delete_first_element()

print("\nQueue attributes...")
my_queue.print_attributes()
