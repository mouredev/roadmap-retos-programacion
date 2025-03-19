from abc import ABC, abstractmethod
from collections import deque
from typing import Collection


class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.__name = name
        self.__surname = surname
        self.__age = age

    def full_info(self) -> str:
        return f"{self.__name} {self.__surname} - {self.__age} years"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def surname(self) -> str:
        return self.__surname

    @property
    def age(self) -> int:
        return self.__age

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @age.setter
    def age(self, age: int) -> None:
        self.__age = age

    @surname.setter
    def surname(self, surname: str) -> None:
        self.__surname = surname

    def __str__(self) -> str:
        name, surname, age = self.__name, self.__surname, self.__age
        return f"Person({name=} {surname=} {age=})"


def create_person(name: str, surname: str, age: int) -> Person:
    return Person(name, surname, age)


class Structure[T](ABC):
    @abstractmethod
    def push(self, element: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @property
    @abstractmethod
    def elements(self) -> Collection[T]:
        pass

    def __str__(self) -> str:
        return str(self.elements)

    @property
    def is_empty(self) -> bool:
        return len(self.elements) == 0

    @property
    def length(self) -> int:
        return len(self.elements)


class Queue[T](Structure[T]):
    def __init__(self) -> None:
        self.__elements: deque[T] = deque()

    def push(self, element: T) -> None:
        self.__elements += [element]

    def pop(self) -> T:
        return self.__elements.popleft()

    @property
    def elements(self) -> deque[T]:
        return self.__elements


class Stack[T](Structure[T]):
    def __init__(self) -> None:
        self.__elements: list[T] = []

    def push(self, element: T) -> None:
        self.__elements += [element]

    def pop(self) -> T:
        return self.elements.pop()

    @property
    def elements(self) -> list[T]:
        return self.__elements


def main() -> None:
    kevin = create_person(name="kevin", surname="dueñas", age=23)
    print(kevin.full_info())
    print(kevin)

    kevin.surname = "asael"
    kevin.age = 24
    print(kevin)
    print(kevin.full_info())

    # Generic queue
    queue = Queue[int]()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.elements)
    print(queue.pop())
    print(queue)
    print(queue.is_empty)
    print(queue.length)

    # Generic stack
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.elements)
    print(stack)
    print(stack.pop())

    print(stack.elements)
    print(stack)
    print(stack.is_empty)
    print(stack.length)


if __name__ == "__main__":
    main()
