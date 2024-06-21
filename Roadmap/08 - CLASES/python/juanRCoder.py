
# CLASES, estructura de datos abstrata, que permite el encapsulamiento de datos y comportamientos.

# Sintaxis
class Animal:
    default_name = 'perro'  # Atributo de clase

    def __init__(self, name=None):  # Constructor, inicializa atributos de instancia
        if not name:
            self.name = Animal.default_name  # Accediendo al atributo de clase
        else:
            self.name = name  # Atributo de instancia

    def greet(self):  # Método de instancia
        print(f'Hola {self.name}')

    def default(self):  # Método de instancia que accede directamente al atributo de clase
        print(Animal.default_name)

    @classmethod
    def method(cls):  # Método de clase
        print(cls.default_name)  # Accediendo al atributo de clase mediante cls



perro = Animal('Scott') # Crear un objeto a partir de la clase
perro.greet()   # accediendo al metodo de instancia 'greet'
# Hola Scott
perro.method() # accediendo al metodo de clase 'method'
# perro
print(perro.default_name) # imprimiedo el atributo de la clase
# perro
