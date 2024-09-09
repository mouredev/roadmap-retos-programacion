# #08 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
# Definición de la clase Persona
class Persona:
    # Inicializador con atributos nombre y edad
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    # Método para imprimir los atributos
    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}")

# Crear una instancia de la clase Persona
persona1 = Persona("Jesus Antonio", 30, "Programador")

persona1.imprimir_informacion()



"""
EXTRA
"""
# Pendientes