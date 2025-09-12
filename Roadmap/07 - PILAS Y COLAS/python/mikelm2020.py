# operaciones: introduce - introducir  recover - recuperar


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


def web_navigation():
    navigation = Stack()

    while True:
        action_of_navigate = input(
            "Escribe la URL o las palabras atras, adelante o salir"
        )

        if action_of_navigate == "adelante":
            pass
        elif action_of_navigate == "atras":
            if not navigation.is_empty():
                if navigation.size() > 1:
                    page = navigation.recover()
                else:
                    page = navigation.items[0]
        elif action_of_navigate == "salir":
            break
        else:
            navigation.introduce(action_of_navigate)
            page = navigation.items

        if not navigation.is_empty():
            print(f"Estas en {page}")


def shared_printing():
    printing_queue = Queue()

    while True:
        action = input("Añade un documento o escribe imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if not printing_queue.is_empty():
                print(f"Imprimiendo el documento {printing_queue.recover()}")
        else:
            printing_queue.introduce(action)

        print(f"La cola de impresión restante es: {printing_queue.items}")


if __name__ == "__main__":
    # web_navigation()
    shared_printing()
