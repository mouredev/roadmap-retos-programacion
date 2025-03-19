""" ---------------------- EJERCICIO -------------------- """
class Triangle():
    """Clase de ejemplo
    """
    def __init__(self, base, altura):
        """Método que inicia las propiedades

        Args:
            base (float): base del triángulo
            altura (float): altura del triángulo
        """
        self.base = base
        self.altura = altura

    @property
    def area(self):
        """Método para calcular su área
        """
        area = (self.base*self.altura)/2
        return area

    def __str__(self):
        """Método que imprime el objeto creado
        """
        return f"El área del triángulo es {self.area}"

# ----------------- PRUEBAS CLASE TRIANGLE() -------------- #
triangulo = Triangle(5, 3)
print(triangulo)

triangulo2 = Triangle(2.5, 4)
print(triangulo2)

# ---------------------- DIFICULTAD EXTRA ----------------- #
# Pila
class Stack():
    """Clase pila para el embarco y desembarco de
    pasajeros en un avión - LIFO
    """
    def __init__(self):
        self.stack = []

    def add(self, passenger):
        """Embarcar pasajeros

        Args:
            passenger (str): pasajeroXX

        Returns:
            str: pasajeroXX a bordo
            Acción de añadir a la lista
        """
        print(f"\nPasajero: {passenger} a bordo")
        return self.stack.append(passenger)

    def out(self):
        """Desembarcar pasajero

        Returns:
            str: pasajeroXX ha desembarcado
            Acción de eliminar de la lista el último elemento
        """
        while len(self.stack) > 0:
            print(f"Parajero: {self.stack[-1]} ha desembarcado")
            return self.stack.pop()
        print("Ya no hay pasajeros a bordo")

    def quantity(self):
        """Cantidad de pasajeros a bordo
        """
        passengers = len(self.stack)
        print(f"El número de pasajeros a bordo es: {passengers}")

    def listview(self):
        """Ver la lista de pasajeros

        Returns:
            list: lista de pasajeros
        """
        print("\nLISTA DE PASAJEROS")
        print(self.stack)

# -------------------- PRUEBAS CLASE STACK() -------------- #
def pruebas_stack():
    """Función para probar la clase Stack()
    """
    embarco = Stack()
    embarco.add("pasajero01")
    embarco.quantity()
    embarco.add("pasajero02")
    embarco.quantity()
    embarco.listview()
    embarco.out()
    embarco.quantity()
    embarco.listview()
    embarco.out()
    embarco.quantity()
    embarco.listview()
    embarco.out()
    embarco.add("pasajero03")
    embarco.listview()

pruebas_stack()

# Cola
class Queue():
    """Clase cola para atención presencial en oficina
    """
    def __init__(self):
        self.queue = []

    def arrived(self, name):
        """Llegar a la cola

        Args:
            name (str): nombre de la persona
        
        Returns:
            str: (nombre), su turno es: (número)
            Acción de incluir en la cola a una persona
        """
        self.queue.append(name)
        print(f"{name}, su turno es: {len(self.queue)}")

    def gone(self):
        """Atención al ciudadano y eliminación de la cola

        Returns:
            str: (nombre) ha sido atendido
            Acción de quitar de la cola el primer registro
        """
        while len(self.queue) > 0:
            print(f"{self.queue[0]} ha sido atendido")
            return self.queue.pop(0)
        print("La cola está vacía")

    def size(self):
        """Conocer la cantidad de personas que están esperando
        
        Returns:
            str: El tamaño de la cola actual es de (número) personas
        """
        if len(self.queue) == 0:
            print("La cola está vacía")
        else:
            print(f"El tamaño de la cola actual es de {len(self.queue)} personas")

    def names(self):
        """Obtener los integrantes de la lista

        Returns:
            str: integrantes de la lista
        """
        print("\nINTEGRANTES DE LA LISTA")
        if len(self.queue) == 0:
            print("No hay integrantes")
        else:
            for item in self.queue:
                print(item)

# -------------------- PRUEBAS CLASE QUEUE() -------------- #

def pruebas_queue():
    """Función para probar la clase Queue()
    """
    cola = Queue()
    cola.size()
    cola.arrived("Héctor")
    cola.size()
    cola.names()
    cola.arrived("Juan")
    cola.size()
    cola.names()
    cola.gone()
    cola.size()
    cola.names()
    cola.gone()
    cola.size()
    cola.names()

pruebas_queue()
