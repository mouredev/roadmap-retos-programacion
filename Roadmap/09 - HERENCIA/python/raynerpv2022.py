# // /*
# //  * EJERCICIO:
# //  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
# //  * implemente una superclase Animal y un par de subclases Perro y Gato,
# //  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
# //  *





class Animal:
    
    def __init__(self, nombre) -> None:
        self.nombre = nombre


class Delfin (Animal):
     
    def __init__(self,  ruido, nombre) -> None:
        super().__init__(nombre)
        self.ruido = ruido

    def sonido(self):
        print(f"Me llamo {self.nombre}, y hago {self.ruido}")

class Tiburon (Animal):
    def __init__(self,  ruido, nombre) -> None:
        super().__init__(nombre)
        self.ruido = ruido

    def sonido(self):
        print(f"Me llamo {self.nombre}, y hago {self.ruido}")


Tibu = Tiburon("GHGHGHGHGHGHG", "tiburcio")
Tonina= Delfin("jijijijjjiijjjiji", "Toninota")
Tibu.sonido()
Tonina.sonido()


# //  * DIFICULTAD EXTRA (opcional):
# //  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
# //  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
# //  * Cada empleado tiene un identificador y un nombre.
# //  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
# //  * actividad, y almacenan los empleados a su cargo.
# //  */

class Empleado:
    def __init__(self,id,nombre) -> None:
        self.id = id
        self.nombre = nombre
        self.empleados_acargo = []

    def addE(self, empleado):
        self.empleados_acargo.append(empleado)

    def mostrarE(self):
        print(f"Empleados A CArgo de {self.nombre}")
        for i in self.empleados_acargo:
            print (i.nombre)
     

class Gerente( Empleado):
    def __init__(self, id, nombre) -> None:
        super().__init__(id, nombre)
        
    def gerenciar(self):
        print(f"NOmbre : {self.nombre}  ID {self.id} ------ Empleados a Cargo : {len(self.empleados_acargo)}, Coordina todos los Proyectos")


    
class GerenteP (Empleado)  :
    def __init__(self, id, nombre, proyecto) -> None:
        super().__init__(id, nombre)
        self.empleados_acargo = [] 
        self.proyecto = proyecto

    def gerenciar(self):
        print(f"NOmbre : {self.nombre}  ID {self.id} ------ Empleados a Cargo : {len(self.empleados_acargo)}, Coordina el proyecto {self.proyecto} ")

    def addE(self, empleado: Empleado):
        self.empleados_acargo.append(empleado)

    


class Programador(Empleado):
    def __init__(self, id, nombre, language) -> None:
        super().__init__(id, nombre)
        self.language = language

    def programar(self):
        print(f"NOmbre : {self.nombre}  ID {self.id} ------ programa en {self.language}")
    def addE(self, empleado):
        print("No puede Tener empleados a su cargo")


P1 = Programador(99,"Paco", ["Python","C#"])
P2 = Programador(98,"Kuko",["GO", "C++"])
GP1 = GerenteP(22,"Cucurella","Web TOR")
G1 = Gerente(111,"Gerente Manolo")
G1.addE(GP1)
GP1.addE(P1)
GP1.addE(P2)

G1.gerenciar()
GP1.gerenciar()
P1.programar()
P2.programar()
G1.mostrarE()
GP1.mostrarE()
P1.addE(P2)


