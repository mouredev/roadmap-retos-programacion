""" #08 CLASES """

from collections import deque

# ----------------- CONOCIENDO CLASES -----------------

# Creacion de una clase


class Transporte:
    # Creacion de atributos globales
    ruedas = True

    # Creacion del constructor
    def __init__(self, conductor):
        self.conductor = conductor

    # Creacion del destructor
    def __delattr__(self):
        print("Transporte dado de baja")

    # Creacion de metodos especializados para la clase
    def avanzar(self):
        if self.ruedas:
            print(f"{self.conductor} comenzará a avanzar")

    def frenar(self):
        print(f"{self.conductor} comenzará a frenar")


# automovil = Transporte("Allan")
# automovil.avanzar()

# ------------------------ EJERCICIO EXTRA --------------------------

# -------- CLASE PILA ---------
print("-------- CLASE PILA ---------")


class Pila:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        print("-> add_item() en acción")
        self.items.append(item)

    def remove_last_item(self):
        print("-> remove_last_item() en acción")
        if not self.items:
            print("sin elementos")
        else:
            item_removed = self.items.pop()
            print(f"Elemento eliminado: {item_removed}")

    def show_items(self):
        print("-> show_items() en acción: ")
        if not self.items:
            print("sin elementos")
        else:
            for item in self.items:
                print(item, end=" - ")
            print("")


pila = Pila()
pila.add_item("Hola")
pila.add_item("Mundo")
pila.show_items()
pila.remove_last_item()
pila.show_items()


# -------- CLASE COLA ---------

print("-------- CLASE COLA ---------")


class Cola:
    def __init__(self):
        self.items = deque()

    def add_item(self, item):
        print("-> add_item() en acción")
        self.items.append(item)

    def remove_first_item(self):
        print("-> remove_fisrt_item() en acción")
        if not self.items:
            print("sin elementos")
        else:
            item_removed = self.items.popleft()
            print(f"Elemento atendido: {item_removed}")

    def show_items(self):
        print("-> show_items() en acción")
        if not self.items:
            print("sin elementos")
        else:
            for item in self.items:
                print(item, end=" - ")
            print("")


cola = Cola()
cola.add_item("Persona 1")
cola.add_item("Persona 2")
cola.add_item("Persona 3")
cola.show_items()
cola.remove_first_item()
cola.show_items()
