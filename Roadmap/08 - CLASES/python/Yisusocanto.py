class Traductor:

    apellido = None

    def __init__(self, name: str, edad: int, idioma: list):
        self.name = name
        self.edad = edad
        self.idioma = idioma

    def print(self):
        print(f"Nombre: {self.name} / apellido: {self.apellido} / Edad: {self.edad} / idioma: {self.idioma}") 


mi_traductor = Traductor("Jesus", 20, ["español", "ingles", "frances"])
mi_traductor.print()
mi_traductor.apellido = "ocanto"
mi_traductor.print()
mi_traductor.idioma.pop(0)
mi_traductor.print()


#extra
#
class Pila:

    def __init__(self, contenido: list):
        self.contenido = contenido

    def print(self):
        print(f"contenido de la pila: {self.contenido}")

    def agregar(self, elemento):
        self.contenido.append(elemento)

    def quitar(self):
        self.contenido.pop()    



mi_pila = Pila(["manzana"])
mi_pila.print()
mi_pila.agregar("pera")
mi_pila.print()
mi_pila.quitar()
mi_pila.print()


class Cola:

    def __init__(self, contenido: list):
        self.contenido = contenido

    def print(self):
        print(f"contenido de la cola: {self.contenido}")

    def agregar(self, elemento):
        self.contenido.append(elemento)

    def quitar(self):
        self.contenido.pop(0)    



mi_cola = Cola(["manzana"])
mi_cola.print()
mi_cola.agregar("pera")
mi_cola.print()
mi_cola.quitar()
mi_cola.print()