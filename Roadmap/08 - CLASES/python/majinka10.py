class Mascota:
    def __init__(self, edad, nombre) -> None:
        self.edad = edad
        self.nombre = nombre
    
    def printData(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")
    
    def modifyData(self, new_edad, new_nombre):
        self.edad = new_edad
        self.nombre = new_nombre

gato = Mascota(4, 'Mishi')
gato.printData()
gato.modifyData(6, 'Tom')
gato.printData()

# Ejercicio EXTRA
print("\nColas y Pilas con Clases\n")

class Cola:
    def __init__(self) -> None:
        self.array = []
    
    def addElement(self, element):
            self.array.append(element)

    def delElement(self):
        try:
            element = self.array.pop(0)
            return element
        except IndexError:
            return "La cola está vacía."

    def lenght(self):
        return len(self.array)
    
    def printContent(self):
        print(self.array)

print("Ejercicio con las Colas\n")
cola = Cola()
cola.addElement(2)
cola.printContent()
cola.addElement(3)
cola.printContent()
print(f"El tamaño de la cola es: {cola.lenght()}")
print(f"Elemento eliminado: {cola.delElement()}")
cola.printContent()

class Pila:
    def __init__(self) -> None:
        self.array = []
    
    def addElement(self, element):
            self.array.append(element)

    def delElement(self):
        try:
            element = self.array.pop(-1)
            return element
        except IndexError:
            return "La pila está vacía."

    def lenght(self):
        return len(self.array)
    
    def printContent(self):
        print(self.array)

print("\nEjercicio con las Pilas\n")
pila = Pila()
pila.addElement(2)
pila.printContent()
pila.addElement(3)
pila.printContent()
print(f"El tamaño de la pila es: {pila.lenght()}")
print(f"Elemento eliminado: {pila.delElement()}")
pila.printContent()    
print(f"Elemento eliminado: {pila.delElement()}")
print(f"{pila.delElement()}")