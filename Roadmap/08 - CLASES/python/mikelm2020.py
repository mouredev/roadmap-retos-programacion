# Clases
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total


# Extra
class Stack:
    def __init__(self):
        # Crea una pila vacía
        self.items = []

    def introduce(self, element):
        # Agrega el elemento element a la pila
        self.items.append(element)

    def recover(self):
        # Devuelve el elemento tope y lo elimina
        # Si la pila está vacía levanta una excepción
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def is_empty(self):
        # Devuelve True si la pila esta vacía
        return self.items == []

    def size(self):
        return len(self.items)

    def content(self):
        return print(self.items)


class Queue:
    def __init__(self):
        # Crea una cola vacía
        self.items = []

    def introduce(self, element):
        # Agrega el elemento element a la cola
        self.items.append(element)

    def recover(self):
        # Devuelve el primer elemento y lo elimina
        # Si la cola está vacía levanta una excepción
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def is_empty(self):
        # Devuelve True si la cola esta vacía
        return self.items == []

    def size(self):
        return len(self.items)

    def content(self):
        return print(self.items)


if __name__ == "__main__":
    store = Store("Test")
    store2 = Store("Amazon")
    store2.add_item("Keyboard", 100)

    stack = Stack()
    for number in range(1, 10):
        stack.introduce(number)
    stack.recover()
    stack.content()
    print(f"El tamaño de la pila es:  {stack.size()}")

    queue = Queue()
    for number in range(1, 10):
        queue.introduce(number)
    queue.recover()
    queue.content()
    print(f"El tamaño de la cola es:  {queue.size()}")
