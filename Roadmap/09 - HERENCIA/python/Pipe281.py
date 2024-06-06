class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def mostrar_datos(self):
        txt = "{0}, {1}"
        return txt.format(self.nombre,self.sonido)

class perro(Animal):
    pass    

class gato(Animal):
    pass  

perro1 = perro("Perro", "Guau Guau")
print(perro1.mostrar_datos())

gato1 = gato("Gato", "Miau Miau")
print(gato1.mostrar_datos())