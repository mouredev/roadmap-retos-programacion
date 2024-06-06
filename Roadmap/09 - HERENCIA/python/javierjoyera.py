class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def emitir_sonido(self):
        raise NotImplementedError("La Subclase debe implementar este método")
    
'''
La herencia se define al pasar la superclase como parametro a la definicion de la subclase.

La superclase Animal tiene un metodo emitir_sonido que no hace nada, pero que debe ser implementado por las subclases.
'''

##Subclases
class Perro(Animal):
    def emitir_sonido(self):
        return ("%s dice: Guau" % self.nombre)
    
class Gato(Animal):
    def emitir_sonido(self):
        return ("%s dice: Miau" % self.nombre)
    
my_dog = Perro("Bruno")
my_cat = Gato("Garfield")

print(my_dog.emitir_sonido())
print(my_cat.emitir_sonido())

## Ejercicio OPCIONAL

class Empleado: 
    def __init__(self, id_empleado, nombre):
        self.id_empleado = id_empleado
        self.nombre = nombre
    
    def __str__(self):
        return "El id del empleado %s es %s" % (self.nombre, self.id_empleado)
    
    def mostrar_informacion(self):
        print(self)


#Subclase Gerente
class Gerente(Empleado):
    def __init__(self, id_empleado, nombre):
        super().__init__(id_empleado, nombre)
        self.empleados_a_cargo = []

    def agregar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Empleados a cargo:")
        for empleado in self.empleados_a_cargo:
            print("- %s" % empleado)

#Subclase Gerente de proyectos
class GerenteProyectos(Gerente):
    def __init__(self, id_empleado, nombre):
        super().__init__(id_empleado, nombre)
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Proyectos a cargo:")
        for proyecto in self.proyectos:
            print("- %s" % proyecto)

class Programador(Empleado):
    def __init__(self, id_empleado, nombre, lenguajes):
        super().__init__(id_empleado, nombre)
        self.lenguajes = lenguajes

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Lenguajes:")
        for lenguaje in self.lenguajes:
            print("- %s" % lenguaje)

#creación de Empleados
gerente_1 = GerenteProyectos(1, "Lorena")
gerente_proyecto_1 = GerenteProyectos(2, "Pedro")
gerente_proyecto_2 = GerenteProyectos(3, "Maria")

programador_1 = Programador(4, "Juan", ["Python", "Java"])
programador_2 = Programador(5, "Carlos", ["Python", "C++"])
programador_3 = Programador(6, "Ana", ["Python", "C++"])

gerente_1.agregar_empleado(gerente_proyecto_1)
gerente_1.agregar_empleado(gerente_proyecto_2)

gerente_proyecto_1.agregar_empleado(programador_1)
gerente_proyecto_1.agregar_empleado(programador_2)

gerente_proyecto_2.agregar_empleado(programador_3)

gerente_proyecto_1.agregar_proyecto("Proyecto 1")
gerente_proyecto_1.agregar_proyecto("Proyecto 2")
gerente_proyecto_2.agregar_proyecto("Proyecto 3")

print("Información del Gerente")
print("-----------------------------")
gerente_1.mostrar_informacion()
print("-----------------------------")
print("Información del Gerente de Proyectos 1")
print("-----------------------------")
gerente_proyecto_1.mostrar_informacion()
print("-----------------------------")
print("Información del Gerente de Proyectos 2")
print("-----------------------------")
gerente_proyecto_2.mostrar_informacion()
print("-----------------------------")
print("Información del Programador 1")
print("-----------------------------")
programador_1.mostrar_informacion()
print("-----------------------------")
print("Información del Programador 2")
print("-----------------------------")
programador_2.mostrar_informacion()
print("-----------------------------")
print("Información del Programador 3")
print("-----------------------------")
programador_3.mostrar_informacion()