"""
    #08 CLASES 
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad


person1 = Persona("Juan", 30)
person1.imprimir_informacion()
person1.set_nombre("Pedro")
person1.set_edad(25)
person1.imprimir_informacion()
print(person1.get_nombre())
print(person1.get_edad())

"""
  DIFICULTAD EXTRA
"""


class Pila:
    def __init__(self, pila):
        self.pila = pila

    def push(self, dato):
        self.pila.append(dato)

    def pop(self):
        return self.pila.pop()

    def imprimir(self):
        print(self.pila)


pila1 = Pila([])
pila1.push(1)
pila1.push(2)
pila1.push(3)
pila1.imprimir()
print(pila1.pop())
pila1.imprimir()


class Cola:
    def __init__(self, cola):
        self.cola = cola

    def enqueue(self, dato):
        self.cola.append(dato)

    def dequeue(self):
        return self.cola.pop(0)

    def imprimir(self):
        print(self.cola)


cola1 = Cola([])
cola1.enqueue(1)
cola1.enqueue(2)
cola1.enqueue(3)
cola1.imprimir()
print(cola1.dequeue())
cola1.imprimir()
