#/*
# * EJERCICIO:
# * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
# * implemente una superclase Animal y un par de subclases Perro y Gato,
# * junto con una función que sirva para imprimir el sonido que emite cada Animal.

class animal:
    nombre = ""
    especies = ""
    
    def add_nombre(self, nombre: str):
        self.nombre = nombre

    def sonido(self):
        pass

    def mensaje(self):
        print(f"El {self.especies} se llama {self.nombre}")
        print("Tu sonido es:")
        self.sonido()

class perro(animal):
    def __init__(self, especies = "perro"):
        self.especies = especies

    def sonido(self):
        print("woof woof")

class gato(animal):
    def __init__(self, especies = "gato"):
        self.especies = especies

    def sonido(self):
        print("meow meow")

perro = perro()
gato = gato()

perro.add_nombre("Aang")
gato.add_nombre("Katara")

perro.mensaje()
gato.mensaje()

# *
# * DIFICULTAD EXTRA (opcional):
# * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
# * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
# * Cada empleado tiene un identificador y un nombre.
# * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
# * actividad, y almacenan los empleados a su cargo.
# */

class empleado:
    def __init__(self, identificador: str, nombre: str):
        self.identificador = identificador
        self.nombre = nombre

class gerente(empleado):
    def oprimir_empleado(self, nombre_empleado):
        print(f"El {self.cargo} {self.nombre} oprimió al empleado {nombre_empleado}.")
    
    def declararse_en_quiebra(self):
        print(f"El {self.cargo} {self.nombre} se declaró en quiebra")

class gerente_de_proyecto(gerente):
    cargo = "Gerente de Proyecto"

    def ordenar_desarrollo(self):
        print(f"El {self.cargo} {self.nombre} ordenó el desarrollo de una nueva feature")

    def quejarse_del_proyecto(self, nombre_proyecto):
        print(f"El {self.cargo} {self.nombre} se quejó del proyecto {nombre_proyecto}.")

class programador(empleado):
    cargo = "Programador"
    features_desarrolladas = 0

    def desarrollar_feature(self, nombre_feature):
        print(f"El {self.cargo} {self.nombre} desarrolló el feature {nombre_feature}.")
        self.features_desarrolladas += 1

def dia_de_trabajo():
    gerente = gerente_de_proyecto(1, "Tom Nook")
    prog_1 = programador(2, "Timmy")
    prog_2 = programador(3, "Tommy")
    features = 0

    print("\n===== ANIMAL COSSING ENTERPRISE =====\n")
    print("Departamento de TI:")
    print(f" -> {gerente.cargo}: {gerente.nombre}")
    print(f" -> {prog_1.cargo}: {prog_1.nombre}")
    print(f" -> {prog_2.cargo}: {prog_2.nombre}")

    print("\n** Comenzó la jornada laboral **\n")

    try:
        features = int(input("¿Cuántos proyectos deberían realizarse hoy? "))
    except:
        print("\nLa cantidad de features no tiene sentido... :(")
        gerente.oprimir_empleado(prog_1.nombre)
        gerente.oprimir_empleado(prog_2.nombre)
        gerente.declararse_en_quiebra()
        return
    
    while features > 0:
        print("")
        gerente.ordenar_desarrollo()
        prog_1.desarrollar_feature("numero " + str(features+0.1))
        gerente.oprimir_empleado(prog_1.nombre)
        print("")

        gerente.ordenar_desarrollo()
        prog_2.desarrollar_feature("numero " + str(features+0.2))
        gerente.oprimir_empleado(prog_2.nombre)
        print("")

        gerente.quejarse_del_proyecto("numero " + str(features))
        features -= 1
    
    print("** La jornada laboral ha terminado **\n")
    gerente.declararse_en_quiebra()
    print("\n\n")

dia_de_trabajo()