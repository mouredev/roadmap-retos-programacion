# CLASES

# CLASE CON INICIALIZADOR, ATRIBUTOS Y UNA FUNCIÓN QUE LOS IMPRIMA
class Perro:
    def __init__(self, nombre, raza, sexo, edad) -> None:
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
    
    def imprimir(self):
        print(f"{self.nombre} es un {self.raza}, es {self.sexo} y tiene {self.edad} años de edad.")
    
    def actualizar_datos(self, nuevo_nombre, nueva_raza, nuevo_sexo, nueva_edad):
        self.nombre = nuevo_nombre
        self.raza = nueva_raza
        self.edad = nueva_edad
        self.sexo = nuevo_sexo
        
perro = Perro("Duke", "Golden Retriever", "macho", 2)
perro.imprimir()

perro.actualizar_datos("Floppy", "Chihuahua", "hembra", 3)
perro.imprimir()



# EJERCICIO - DIFICULTAD EXTRA

# PILA
class PilaCartas:
    def __init__(self) -> None:
        self.pila = []

    def agregar(self, carta):
        self.pila.append(carta)
    
    def quitar(self):
        if self.pila:
            last = self.pila.pop()
            print(f"Se quitó la carta: {last}")
        else:
            print("La pila esta vacía, no se puede quitar más cartas")

    def imprimir(self):
        print(f"Las cartas de la pila son: {self.pila}")

carta = PilaCartas()

carta.agregar("Rey de corazón")
carta.agregar("As de corazón")
carta.agregar("Trebol de espadas")
carta.imprimir()

carta.quitar()
carta.imprimir()


# COLA
class ColaCajero:
    def __init__(self) -> None:
        self.cola = []

    def agregar(self, persona):
        self.cola.append(persona)
    
    def quitar(self):
        if self.cola:
            first = self.cola.pop(0)
            print(f"{first} ingresó al cajero")
        else:
            print("La cola esta vacía")

    def imprimir(self):
        print(f"Las personas en la cola son: {self.cola}")

cola = ColaCajero()

cola.agregar("Juan")
cola.agregar("Ana")
cola.agregar("Pedro")
cola.imprimir()

cola.quitar()
cola.imprimir()