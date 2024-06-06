class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def sonido(self):
        pass 

class Perro(Animal):
    def sonido(self):
        return f'el perro hace ¡Guau, Guau!'
    
class Gato(Animal):
    def sonido(self):
        return 'el gato hace ¡Miau!'
    
animal1 = Perro('Alfa')
print(f'{animal1.nombre}, {animal1.sonido()}')

animal2 = Gato('Gary')
print(f'{animal2.nombre}, {animal2.sonido()}')

print()

'''
EXTRA
'''

class Empleados:
    def __init__(self, id, nombre) -> None:
        self.nombre = nombre
        self.id = id

    def deber(self):
        print('Trabajar')

class Gerente(Empleados):
    def __init__(self, id, nombre, empleados) -> None:
        super().__init__(id, nombre)
        self.empleados = empleados

    def deber(self):
        print('Gerente')

    def get_info(self):
        print(f'el gerente {self.nombre} con el id {self.id} tiene {self.empleados} empledos')

class Gerente_Proyecto(Empleados):
    def __init__(self, id, nombre, empleados) -> None:
        super().__init__(id, nombre)
        self.empleados = empleados

    def deber(self):
        print('Gerente de proyectos')

    def get_info(self):
        print(f'el gerente de proyectos {self.nombre} con el id {self.id} tiene {self.empleados} empledos')

class Programador(Empleados):
    def __init__(self, id, nombre, empleados=0) -> None:
        super().__init__(id, nombre)
        self.empleados = empleados

    def deber(self):
        print('Programar')

    def get_info(self):
        print(f'el programador {self.nombre} con el id {self.id} tiene {self.empleados} empleados')


empleado1 = Gerente(1, 'Javier', 5)
print(empleado1.id)
empleado1.deber()
print(empleado1.empleados)
print(empleado1.nombre)
empleado1.get_info()

print()

empleado2 = Gerente_Proyecto(2, 'Milei', 6)
print(empleado2.id)
empleado2.deber()
print(empleado2.empleados)
print(empleado2.nombre)
empleado2.get_info()

print()

empleado3 = Programador(3, 'Sergio')
print(empleado3.id)
empleado3.deber()
print(empleado3.empleados)
print(empleado3.nombre)
empleado3.get_info()
