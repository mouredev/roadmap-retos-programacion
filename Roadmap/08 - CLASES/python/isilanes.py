from abc import ABC, abstractmethod
from typing import TypeVar


T = TypeVar("T")


class Dog:

    def __init__(self, name: str, age: int = 1):
        self.name = name
        self.age = age

    def __str__(self):
        if self.age == 1:
            return f"El cachorrito {self.name} tiene un añito"

        if self.age < 5:
            return f"El cachorro {self.name} tiene {self.age} años"

        return f"{self.name} tiene {self.age} años"


class Collection(ABC):

    def __init__(self, content: list[T] | None = None):
        self.content: list[T] = content or []

    def add(self, element: T) -> None:
        """
        Add 'element' to the collection.

        Args:
            element (T):
                Element to add to the collection.

        Return:
            Nothing.
        """
        self.content.append(element)

    @abstractmethod
    def extract(self) -> T:
        """
        Remove (and return) next element in the collection, according
        to the rules of the specific collection (FILO/LIFO for Stack,
        FIFO for Queue).

        Args:
            None.

        Returns:
            The extracted element.
        """

    @property
    def size(self) -> int:
        """
        Return the size of the collection, as the count of elements in it.
        """
        return len(self.content)

    def __str__(self) -> str:
        return str(self.content)


class Stack(Collection):

    def extract(self) -> T:
        return self.content.pop()


class Queue(Collection):

    def extract(self) -> T:
        return self.content.pop(0)


def extra():
    stack = Stack([1, 2, 3])
    print(f"\nContenido inicial de la pila: {stack}")
    print(f"Extraemos un elemento (el {stack.extract()})")
    print(f"Contenido de la pila actualizado: {stack}")
    print(f"Ahora la pila tiene tamaño {stack.size}")
    print("Añadimos un elemento a la pila (el 4)")
    stack.add(4)
    print(f"Contenido de la pila actualizado: {stack}")

    queue = Queue(["a", "b", "c"])
    print(f"\nContenido inicial de la cola: {queue}")
    print(f"Extraemos un elemento (la '{queue.extract()}')")
    print(f"Contenido de la cola actualizado: {queue}")
    print(f"Ahora la cola tiene tamaño {queue.size}")
    print("Añadimos un elemento a la cola (la 'd')")
    queue.add("d")
    print(f"Contenido de la cola actualizado: {queue}")


def main():
    dog = Dog(name="Pluto")
    print(dog)
    dog.age = 3
    print(dog)
    dog.age = 10
    print(dog)


if __name__ == "__main__":
    main()
    extra()
