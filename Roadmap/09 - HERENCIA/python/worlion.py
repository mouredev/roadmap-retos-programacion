"""
    HERENCIA EN PYTHON
"""
# Clase animal (superclase)
class Animal:
    nombre = ""
    sonido = ""
    icono = ""
    
    def __init__(self, nombre = "", sonido="", icono = "❓") -> None:
        self.nombre = nombre
        self.sonido = sonido
        self.icono = icono

    def hacer_sonido(self):
        print(f"el {self.nombre} hace: {self.sonido} {self.icono}")        

# Clase perro (subclase)
class Perro(Animal):
    def __init__(self) -> None:
        super().__init__("Perro", "guau!", "🐶")
        
# Clase gato (subclase)
class Gato(Animal):
    def __init__(self) -> None:
        super().__init__("Gato", "miau!", "🐱")
        
myDog = Perro()
myDog.hacer_sonido()
        
myCat = Gato()
myCat.hacer_sonido()

"""
DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")
pass
