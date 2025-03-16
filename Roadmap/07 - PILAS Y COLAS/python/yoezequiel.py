class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("La pila está vacía")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("La pila está vacía")

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("La cola está vacía")

    def size(self):
        return len(self.items)


def navegador():
    historial = Stack()
    actual = ""

    while True:
        comando = input("Ingrese 'adelante', 'atrás' o el nombre de una página web: ")

        if comando == "adelante":
            if not historial.is_empty():
                actual = historial.pop()
                print("Navegando adelante a:", actual)
            else:
                print("No hay más páginas hacia adelante")
        elif comando == "atrás":
            if actual != "":
                historial.push(actual)
                print("Navegando atrás desde:", actual)
                actual = ""
            else:
                print("No hay más páginas hacia atrás")
        else:
            if actual != "":
                historial.push(actual)
            actual = comando
            print("Navegando a:", actual)


navegador()


def navegador():
    historial = Stack()
    actual = ""

    while True:
        comando = input("Ingrese 'adelante', 'atrás' o el nombre de una página web: ")

        if comando == "adelante":
            if not historial.is_empty():
                actual = historial.pop()
                print("Navegando adelante a:", actual)
            else:
                print("No hay más páginas hacia adelante")
        elif comando == "atrás":
            if actual != "":
                historial.push(actual)
                print("Navegando atrás desde:", actual)
                actual = ""
            else:
                print("No hay más páginas hacia atrás")
        else:
            if actual != "":
                historial.push(actual)
            actual = comando
            print("Navegando a:", actual)


navegador()


def impresora():
    documentos = Queue()

    while True:
        comando = input("Ingrese 'imprimir' o el nombre de un documento: ")

        if comando == "imprimir":
            if not documentos.is_empty():
                print("Imprimiendo:", documentos.dequeue())
            else:
                print("No hay documentos en la cola para imprimir")
        else:
            documentos.enqueue(comando)
            print("Documento agregado a la cola:", comando)


impresora()
