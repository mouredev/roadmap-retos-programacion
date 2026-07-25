#Ejercicio 9: Herencia

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
# Crear instancias de Perro y Gato
mi_perro = Perro("Rex", 5)
mi_gato = Gato("Michi", 3)

# Mostrar los sonidos que hacen
print(f"{mi_perro.nombre} dice: {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} dice: {mi_gato.hacer_sonido()}")


# DIFICULTAD EXTRA (opcional):

class empleado:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def funciones(self):
        pass

    def empleados_info(self):
        return f"Nombre: {self.nombre}, ID: {self.identificacion}, Funciones: {self.funciones()}"


class gerente(empleado):
    def funciones(self):
        return "Gestiona el equipo y toma decisiones estratégicas."
    
class desarrollador(empleado):
    def funciones(self):
        return "Escribe y mantiene el código del software."
    
class diseñador(empleado):
    def funciones(self):
        return "Crea diseños visuales y experiencia de usuario."
    
# Crear instancias de cada tipo de empleado
gerente1 = gerente("Ana", 101)
desarrollador1 = desarrollador("Luis", 102)
diseñador1 = diseñador("Marta", 103)
# Mostrar la información de cada empleado
print(gerente1.empleados_info())
print(desarrollador1.empleados_info())
print(diseñador1.empleados_info())