# 09 - Herencias

# Clase padre
class Animal:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        print('Algun sonido')

    def presentarse(self):
        print(f'Hola, soy {self.nombre}, y tengo {self.edad} años.')

# Clase Hija
class Perro(Animal):

    def __init__(self, nombre, edad, raza):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, edad)
        self.raza = raza

    # Sobrescribimos el metodo sonido
    def sonido(self):
        print('¡Guau, guau!')

    # Agregamos un metodo especifico del Perrro
    def perseguir_cola(self):
        print(f'{self.nombre} esta persiguiendo su cola')

class Gato(Animal):
    
    def __init__(self, nombre, edad, color):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, edad)
        self.color = color

    # Sobrescribimos el metodo sonido
    def sonido(self):
        print('Miau')

    # Agregamos un metodo especifico del Gato
    def dormir(self):
        print(f'{self.nombre} esta durmiendo.')


mi_perro = Perro('Max', 3, 'Pug')
mi_perro.presentarse()
mi_perro.sonido()
mi_perro.perseguir_cola()

mi_gato = Gato('Luna', 2, 'Negro')
mi_gato.presentarse()
mi_gato.sonido()
mi_gato.dormir()


# Extra

class Empleado:

    def __init__(self, id, nombre, cargo):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.empleados = []

    def presentarse(self):
        print(f'Hola, mi nombre es {self.nombre} y mi cargo es {self.cargo}')

    def agregar_empleado(self, empleados):
        self.empleados.append(empleados)

    def listar_empleados(self):
        if len(self.empleados) >= 1:
            print(f'{self.nombre} tiene a cargo {len(self.empleados)} empleados.')
        else:
            print(f'{self.nombre} no tiene empleados a cargo.')


class Gerente(Empleado):

    def __init__(self, id, nombre, cargo):
        super().__init__(id, nombre, cargo)

    def planifica(self):
        print(f'Como {self.cargo}, estoy planificando los objetivos del proximo año')


class GerenteProyecto(Empleado):
    
    def __init__(self, id, nombre, cargo):
        super().__init__(id, nombre, cargo)

    def ejecuta(self):
        print(f'Como {self.cargo}, estoy ejecutando los objetivos de este año')


class Programador(Empleado):

    def __init__(self, id, nombre, cargo):
        super().__init__(id, nombre, cargo)

    def desarrolla(self):
        print(f'Como {self.cargo}, estoy desarrollando un programa para alcanzar los objetivos.')

    
gerente_1 = Gerente(1, 'Jorge', 'Gerente')
gerente_1.presentarse()
gerente_1.planifica()

gerente_proyecto_1 = GerenteProyecto(2, 'Felipe', 'Gerente de Proyectos')
gerente_proyecto_1.presentarse()
gerente_proyecto_1.ejecuta()

programador_1 = Programador(3, 'Raul', 'Programador')
programador_1.presentarse()
programador_1.desarrolla()

gerente_1.agregar_empleado(gerente_proyecto_1)
gerente_proyecto_1.agregar_empleado(programador_1)

gerente_1.listar_empleados()
gerente_proyecto_1.listar_empleados()
programador_1.listar_empleados()