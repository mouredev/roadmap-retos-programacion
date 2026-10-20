#Las clases Perro y Gato heredan de Animal.
#La función sonido es polimórfica

class Animal():
    def __init__(self, nombre:str):
        self.nombre = nombre

    def sonido(self):
        pass    

class Perro(Animal):
    def sonido(self):
        print("¡Guau!")

class Gato(Animal):
    def sonido(self):
        print("¡Miau!")

Tobi = Perro("Tobi")
Tobi.sonido()
Micifu = Gato("Micifú")
Micifu.sonido()

'''
DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo
'''
class Empleado():
    def __init__(self, id: int, nombre:str):
        self.id = id
        self.nombre = nombre
        self.empleados = []

    def añadir(self, empleado):
        self.empleados.append(empleado)    

    def listar(self):
        for empleado in self.empleados:
            print(f"Soy {self.nombre} mi empleado es: {empleado.id} -> {empleado.nombre}") 


class Gerente(Empleado):
    def funcion(self):
        print(f"Soy el gerente {self.nombre} mi oficio es mandar en todo.")


class GerenteDeProyecto(Empleado):
    def __init__(self, id:int, nombre:str, proyecto:str):
        super().__init__(id, nombre)
        self.proyecto = proyecto
    def funcion(self):
        print(f"Soy el gerente de proyecto {self.nombre} mi oficio es encargarme del proyecto {self.proyecto}.")

class Programador(Empleado):
    def __init__(self, id:int, nombre:str, lenguaje:str):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje
    def funcion(self):
        print(f"Soy el programador {self.nombre} mi oficio es programar en {self.lenguaje}.")

    def añadir(self, empleado: Empleado):
            print(f"Un programador no puede tener empleados {empleado.nombre} no se añadirá")    
        

mi_gerente = Gerente(1, "MoureDev")
mi_gerente_de_proyecto1 = GerenteDeProyecto(2, "Brais", "Proyecto 1")
mi_gerente_de_proyecto2 = GerenteDeProyecto(3, "Moure", "Proyecto 2")
my_programador1 = Programador(4, "Kontrol", "Swift")
my_programador2 = Programador(5, "Ros", "Cobol")
my_programador3 = Programador(6, "Bushi", "Dart")
my_programador4 = Programador(7, "Nasos", "Python")   

mi_gerente.añadir(mi_gerente_de_proyecto1)
mi_gerente.añadir(mi_gerente_de_proyecto2)

mi_gerente_de_proyecto1.añadir(my_programador1)
mi_gerente_de_proyecto1.añadir(my_programador2)
mi_gerente_de_proyecto2.añadir(my_programador3)
mi_gerente_de_proyecto2.añadir(my_programador4)

my_programador1.añadir(my_programador2)

my_programador1.funcion()
mi_gerente_de_proyecto1.funcion()
mi_gerente.funcion()
mi_gerente.listar()
mi_gerente_de_proyecto1.listar()
my_programador1.listar()
mi_gerente_de_proyecto2.listar()      

