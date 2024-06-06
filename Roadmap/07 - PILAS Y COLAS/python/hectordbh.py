"""EJERCICIO
"""
# stacks - LIFO
class Stack():
    """Clase pila para trabajar LIFO
    """
    def __init__(self):
        self.items = []

    def isempty(self):
        """Método para verificar si la pila está vacía
        """
        if not self.items:
            print("La pila está vacía")
        else:
            print("Hay elementos en la pila")

    def push(self, item):
        """Método para añadir un elemento a la pila
        """
        self.items.append(item)
        print("Se ha añadido el elemento a la pila")

    def pop(self):
        """Método que elimina de la pila el último elemento introducido
        """
        print(f"El elemento {self.items.pop()} se ha eliminado")

    def top(self):
        """Método que devuelve el elemento más alto de la pila
        """
        print(self.items[len(self.items)-1])

    def size(self):
        """Método que devuelve el tamaño de la pila
        """
        print(f"La pila contiene: {self.items} y su longitud es: {len(self.items)}")

# queue - FIFO
class Queue():
    """Clase cola para trabajar Queue
    """
    def __init__(self):
        self.items = []

    def isempty(self):
        """Método para verificar si la cola está vacía
        """
        if not self.items:
            print("La cola está vacía")
        else:
            print("Hay elementos en la cola")

    def enqueue(self, item):
        """Método para añadir un elemento a la cola
        """
        self.items.insert(0, item)
        print("Se ha añadido el elemento a la cola")

    def dequeue(self):
        """Método que elimina de la cola el primer elemento introducido
        """
        print(f"El elemento {self.items.pop()} se ha eliminado")

    def size(self):
        """Método que devuelve el tamaño de la cola
        """
        print(f"La cola contiene: {self.items} y su longitud es: {len(self.items)}")

# ---------------------- PRUEBAS LIFO -----------------------
pila = Stack()
pila.isempty()
pila.push("primero")
pila.size()
pila.push("segundo")
pila.size()
pila.pop()
pila.size()

# ---------------------- PRUEBAS FIFO -----------------------
cola = Queue()
cola.isempty()
cola.enqueue("Héctor")
cola.size()
cola.enqueue("Pedro")
cola.size()
cola.dequeue()
cola.size()

# ---------------------- DIFICULTAD EXTRA -------------------
class WebNav():
    """Clase para manejar adelante/atrás en un navegador
    """
    def __init__(self):
        self.stack = []
        self.history = ["www.google.es", "www.rae.es", "www.apple.com"]

    def method(self, ins):
        """Método para indicar si avanzamos o retrocedemos

        Args:
            ins (str): adelante/atras

        Returns:
            str: elemento más top en la tabla
        """
        if ins == "adelante":
            if len(self.stack) == len(self.history):
                web = str(input("Introduce una web: "))
                self.push(web)
            else:
                self.push()
            return self.top()
        if ins == "atras":
            if len(self.stack) <= 1:
                if len(self.stack) == 1:
                    self.pop()
                print("No tienes historial que recuperar")
            else:
                self.pop()
                return self.top()

    def push(self, item = ""):
        """Método para añadir un elemento a la pila
        """
        if item != "":
            self.history.append(item)
        self.stack.append("forward")

    def pop(self):
        """Método que elimina de la pila el último elemento introducido
        """
        return self.stack.pop()

    def top(self):
        """Método que devuelve el elemento más alto de la pila
        """
        print(self.history[len(self.stack)-1])

# ---------------------- PRUEBAS NAVEGACIÓN -----------------
nav = WebNav()
print(nav.history)
nav.method("adelante")
nav.method("adelante")
nav.method("adelante")
nav.method("atras")
nav.method("atras")
nav.method("atras")

class Impress():
    """Clase para manejar la cola de impresión de un dispositivo
    """
    def __init__(self):
        self.items = []

    def isempty(self):
        """Método para verificar si la cola de impresión está vacía
        """
        if not self.items:
            print("La cola de impresión está vacía")
        else:
            print("Hay elementos en la cola de impresión")

    def enqueue(self, item):
        """Método para añadir un elemento a la cola de impresión
        """
        self.items.insert(0, item)
        print("Se ha añadido el elemento a la cola de impresión")

    def dequeue(self):
        """Método que elimina de la cola el primer elemento introducido
        """
        print(f"El elemento {self.items.pop()} se ha impreso")

    def size(self):
        """Método que devuelve el tamaño de la cola
        """
        print(f"Documentos en la cola de impresión: {self.items}")

# ---------------------- PRUEBAS COLA DE IMPRESIÓN ----------
imp = Impress()
imp.isempty()
imp.enqueue("Archivo1")
imp.isempty()
imp.enqueue("Archivo2")
imp.size()
imp.dequeue()
imp.size()
