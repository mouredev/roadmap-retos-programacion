"""ejercicio"""

class Animal:

    def __init__(self,nombre):
        self.nombre=nombre

    def sonido(self):
        print("x")


class Perro(Animal):


    def sonido(self):
        print("guau")



class Gato(Animal):


    def sonido(self):
        print("Miau")


def sonidoA(animal: Animal):
    animal.sonido()

    

animal =Animal("animal")

sonidoA(animal)

perro=Perro("maya")
sonidoA(perro)

gato=Gato("nala")
sonidoA(gato)


class Empleado:

    def __init__(self,id,nombre) :
        self.id=id
        self.nombre=nombre
        self.trabajadores=[]

    def añadirEmpleados(self,trabajador):
        self.trabajadores.append(trabajador)
    
    def imprimirEmpleados(self):
        for trabajador in self.trabajadores:
            print(trabajador.nombre)   

class Gerente(Empleado):
    
    def coorProyectos(self):
        print(f"el {self.nombre} esta cordinando los proyectos")


class Gerente_Poryectos(Empleado):
    def __init__(self, id, nombre,proyectos):
        super().__init__(id, nombre)
        self.proyectos = proyectos

    
    def coorProyecto(self):
        print(f" el {self.nombre} esta cordinando el proyecto {self.proyectos} ")

class Programadores(Empleado):
    def __init__(self, id, nombre,lenguajes):
        super().__init__(id, nombre)
        self.lenguajes=lenguajes

    def lenguaje(self):
        print(f"el {self.nombre} utiliza {self.lenguajes} como lenguajes de programación")

    def añadirEmpleados(self,trabajadores:Empleado):
        print(f"el programador no tiene trabajadores a su cargo {trabajadores.nombre} no sera añadido")






gerente=Gerente(1,"chema")
gerenteP=Gerente_Poryectos(2,"antonio","app")
gerenteP2=Gerente_Poryectos(3,"pepe","web")
miProgramador=Programadores(4,"devChema","python")
miProgramador2=Programadores(4,"Mouredev","java")

gerente.añadirEmpleados(gerenteP)
gerente.añadirEmpleados(gerenteP2)
gerenteP2.añadirEmpleados(miProgramador)

miProgramador.añadirEmpleados(miProgramador2)

miProgramador.lenguaje()

gerente.coorProyectos()
gerenteP.coorProyecto()

gerente.imprimirEmpleados()
gerenteP2.imprimirEmpleados()

miProgramador.imprimirEmpleados()## en este no va tener salida


