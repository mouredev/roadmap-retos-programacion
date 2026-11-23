class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def sonido(self):
        pass

    def describeme(self):
        print(f'Hola soy un animal de tipo {type(self).__name__}')

class Perro(Animal):
    def sonido(self):
        print("¡Wof!")

class Gato(Animal):
    def sonido(self):
        print('¡Miau!')

mi_perro = Perro('mamifero', 5)
mi_perro.sonido()

mi_gato = Gato('mamifero', 4)
mi_gato.sonido()

'''
EXTRA
'''

class Empleado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class Gerente(Empleado):
    def __init__(self, id, nombre, empleados_acargo):
        super().__init__(id, nombre)
        self.empleados_acargo = empleados_acargo

    def contratar(self):
        pass

    def despesdir(self):
        pass

class Gerente_de_proyectos(Empleado):
    def __init__(self, id, nombre, empleados_acargo):
        super().__init__(id, nombre)
        self.empleados_acargo = empleados_acargo

    def contratar(self):
        pass
    
    def despesdir(self):
        pass

class Programador(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def programar(self):
        print('hola mundo')