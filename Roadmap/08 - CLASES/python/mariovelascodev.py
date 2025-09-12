#Creación de una clase
class Person:
    def __init__(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
    def information(self):
        print(f"Nombre: {self.name}")
        print(f"Apellidos: {self.surname}")
        print(f"Edad: {self.age}")
        print(f"Email: {self.email}")

#Instanciamos la clase y le añadimos los parámetros y mostramos la información
persona_1 = Person("Mario", "Velasco", 34, "mario@mario.com")
persona_1.information()

#Modificamos algún atributo
persona_1.email = "correo@nocorreo.com"
print(f"El correo a sido cambiado a: {persona_1.email}")


#EXTRA

class Pila:
    def __init__(self):
        self.pila = []
    def agregar(self, param):
        self.pila.append(param)
    def eliminar(self):
        return f"Se ha eliminado: {self.pila.pop()}"
    def numero_elementos(self):
        return f"El número de elementos de la pila es: {len(self.pila)}"
    def contenido(self):
        return f"El contenido de la pila es: {self.pila}"

print("\nClase Pila")        
pila = Pila()
pila.agregar(34)
pila.agregar(2)
pila.agregar(200)
pila.agregar(98)
print(pila.contenido())
print(pila.numero_elementos())
print(pila.eliminar())
print(pila.contenido())
print(pila.numero_elementos())

class Cola:
    def __init__(self):
        self.cola = []
    def agregar(self, param):
        self.cola.append(param)
    def eliminar(self):
        return f"Se ha eliminado: {self.cola.pop(0)}"
    def numero_elementos(self):
        return f"El número de elementos de la cola es: {len(self.cola)}"
    def contenido(self):
        return f"El contenido de la cola es: {self.cola}"

print("\nClase Cola")    
cola = Cola()
cola.agregar(34)
cola.agregar(2)
cola.agregar(200)
cola.agregar(98)
print(cola.contenido())
print(cola.numero_elementos())
print(cola.eliminar())
print(cola.contenido())
print(cola.numero_elementos())