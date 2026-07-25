class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladar(self):
        print(f'{self.nombre} dice: ¡Guau!')

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad} años.')


class PerroGuardian(Perro):
    def vigilar(self):
        print(f'{self.nombre} esta vigilando la casa.')


perro1 = Perro('Rex', 3)
perro2 = Perro('Luna', 7)
guardian = PerroGuardian('Thor', 10)

perro1.ladar()
perro2.mostrar_info()
guardian.vigilar()

# Extra

class Pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def anadir(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self):
        if self.esta_vacia():
            raise IndexError('Esta vacio')
        return self.elementos.pop()
    
    def tamano(self):
        return len(self.elementos)
    
    def imprimir(self):
        print('Contenido:', self.elementos)

pila = Pila()
pila.anadir(1)
pila.anadir(2)
pila.anadir(3)
pila.imprimir()
pila.eliminar()
pila.imprimir()
print('Tamaño: ', pila.tamano())

class Cola:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def anadir(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self):
        if self.esta_vacia():
            raise IndexError('Esta vacio')
        return self.elementos.pop(0)
    
    def tamano(self):
        return len(self.elementos)
    
    def imprimir(self):
        print('Contenido:', self.elementos)

cola = Cola()
cola.anadir(1)
cola.anadir(2)
cola.anadir(3)
cola.imprimir()
cola.eliminar()
cola.imprimir()
print('Tamaño: ', cola.tamano())