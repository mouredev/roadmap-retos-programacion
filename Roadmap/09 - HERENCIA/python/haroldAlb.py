# EJERCICIO #
class Animal():
    def __init__(self, nombre, patas, pelo):
        self.__nombre = nombre
        self.__patas = patas
        self.__pelo = pelo
        
    def moverse(self):
        return f"{self.__nombre} se está moviendo... "
    
    def sonido(self):
        pass

class Perro(Animal):
    def __init__(self, nombre, patas, pelo, cola):
        super().__init__(nombre, patas, pelo)
        self.__cola = cola

    def sonido(self):
        print("Guau, guau!!!")

class Gato(Animal):
    def __init__(self, nombre, patas, pelo, uñas):
        super().__init__(nombre, patas, pelo)
        self.__uñas = uñas

    def sonido(self):
        print("Miaaaaaaw!!!")

def sonido_animal(Animal):
    Animal.sonido()

# EXTRA #
class Empleado:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.empleados = []

    def añadir_empleado(self, empleado):
        self.empleados.append(empleado)

    def imprimir_empleados(self):
        print(f"Empleados a cargo de {self.nombre}")
        for empleado in self.empleados:
            print(empleado.nombre)
        

class Gerente(Empleado):
    def coordinar(self):
        print(f"{self.nombre} está coordinanado todos los proyectos de la empresa.")

class GerenteProyecto(Empleado):
    def __init__(self, id, nombre, proyecto: str):
        super().__init__(id, nombre)
        self.proyecto = proyecto

    def coordinar_proyecto(self):
        print(f"{self.nombre} está coordinando su proyecto.")

class   Programador(Empleado):
    def __init__(self, id, nombre, lenguaje: str):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje

    def programar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}")

    def añadir_empleado(self, empleado: Empleado): # Al parámetro le estamos especificando que debe ser de la clase Empleado y heredará todo lo de este
        print(f"Los programadores no tienen empleados a su cargo. {empleado.nombre} no se añadirá.") # Ahora al poner el parámetro y un atributo de la super clase nos saldrá el nombre que hayamos puesto al hacer la instancia del objeto

if __name__ == "__main__":

    # EJERCICIO #
    print("#"*15 + " EJERCICIO " + "#"*15)

    perro = Perro("Kiwi", 4, "Corto", "Larga")
    gato = Gato("Kiko", 3, "largo", True)
    sonido_animal(perro)
    sonido_animal(gato)

    # EXTRA #
    print("#"*15 + " EXTRA " + "#"*15)

    gerente = Gerente(1, "Mario")
    ger_proyec1 = GerenteProyecto(2, "Olga", "Proyecto1")
    ger_proyec2 = GerenteProyecto(3, "Harold", "Proyecto2")
    prog1 = Programador(4, "Ana", "Python")
    prog2 = Programador(5, "Cloe", "labView")
    prog3 = Programador(6, "Samanta", "C#")
    prog4 = Programador(7, "Julia", "HTML")

    gerente.coordinar()
    ger_proyec1.coordinar_proyecto()
    ger_proyec2.coordinar_proyecto()
    prog1.programar()
    prog2.programar()
    prog3.programar()
    prog4.programar()


    gerente.añadir_empleado(ger_proyec1)
    gerente.añadir_empleado(ger_proyec2)
    ger_proyec1.añadir_empleado(prog1)
    ger_proyec1.añadir_empleado(prog2)
    ger_proyec2.añadir_empleado(prog3)
    ger_proyec2.añadir_empleado(prog4)
    prog1.añadir_empleado(prog4) # En vez de ejecutar el método de la super clase Empleado, hará el método de la clase hija Programador

    gerente.imprimir_empleados()
    ger_proyec1.imprimir_empleados()
    ger_proyec2.imprimir_empleados()
    prog1.imprimir_empleados() # no se imprimira ningún nombre
   
