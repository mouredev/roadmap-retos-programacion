"""
* EJERCICIO:
* Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
* implemente una superclase Animal y un par de subclases Perro y Gato,
* junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""

class Animal():
    def __init__(self, nombre: str, especie: str, peso: float, altura: int, familiares: list):
        
        self.nombre = nombre
        self.especie = especie
        self.peso = peso
        self.altura = altura
        self.familiares = familiares

    esta_adoptado: bool = False

    def mostrar_datos(self):
        print(f"Tu animal tiene estas características (Nombre: {self.nombre}, Especie: {self.especie}, Peso: {self.peso}, Altura en cms: {self.altura}, Padres: {self.familiares})")
    
    def adoptar(self):
        if self.esta_adoptado == False:
            self.esta_adoptado = True
            print(f"Enhorabuena por la adopción de tu {self.especie}.")
        else:
            print(f"Lo siento este {self.especie} ya está adoptado.")
        return
    
    def sonido(self):
        print("guau")

    def engordar(self):
        aumento_de_peso = int(input("¿Cuántos kilogramos engordó tu mascota?\n"))
        self.peso = self.peso + aumento_de_peso

class Gato(Animal):
    def __init__(self, nombre: str, especie: str, peso: float, altura: int, familiares: list):
        super().__init__(nombre, especie, peso, altura, familiares)
    
    def sonido(self):
        print("miau")
        super().sonido()

class Pinguino(Animal):
    def __init__(self, nombre: str, especie: str, peso: float, altura: int, familiares: list):
        super().__init__(nombre, especie, peso, altura, familiares)

    def sonido(self):
        print("pingu")
        super().sonido()

        

# alma = Animal("alma", "perro", 20.4, 110, ["muller", "ribery"])
# alma.mostrar_datos()
# alma.adoptar()
# alma.adoptar()
# alma.engordar()
# alma.mostrar_datos()

# gato = Gato("kity", "egipcio", 8.4, 77, ["silson", "staisy"])
# gato.engordar()
# gato.adoptar()
# gato.sonido()


"""
* DIFICULTAD EXTRA (opcional):
* Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
* pueden ser Gerentes, Gerentes de Proyectos o Programadores.
* Cada empleado tiene un identificador y un nombre.
* Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
* actividad, y almacenan los empleados a su cargo.
"""

class Empleado():

    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.empleados = [] # Atributo de instancia
    
    vacaciones:bool = False

    def activar_vacaciones(self):

        if self.vacaciones == False:
            self.vacaciones = True
            print("Que te cundan chaval")
        else:
            print("Continua la carrera de la rata, denegadas")

    def add_empleados_a_cargo(self, empleado):
        self.empleados.append(empleado)
    
    def mostrar_empleados_a_cargo(self):
        for empleado in self.empleados:
            print(empleado.nombre)

    def despedir(self):
        candidato = str(input("Escribe a quien quieres despedir.\n"))
        for empleado in self.empleados:
            if empleado.nombre == candidato:
                self.empleados.remove(empleado)
                print(f"Enhorabuena, te acabas de fumar a {empleado.nombre}.")
                return
        else:
            print("Ese cabrón ya no está por aquí")

class Gerente(Empleado):
    def __init__(self, id: int, nombre: str):
        super().__init__(id, nombre)

    def putear_a_empleados(self):
        print("Trabaja vago!")

class Programador(Empleado):
    def __init__(self, id: int, nombre: str):
        super().__init__(id, nombre)

    def putear_a_empleados(self):
        print("Trabaja vago!")

    def almacenar_empleados_a_cargo(self):
        print("Un programador ya tienen bastante con el mismo.")

pringado_1 = Empleado(878, "Luismi")
pringado_1.activar_vacaciones()

medio_pringado_1 = Gerente(987, "Josema")
medio_pringado_1.activar_vacaciones()

medio_pringado_1.putear_a_empleados()
# pringado_1.putear_a_empleados()

medio_pringado_1.add_empleados_a_cargo(pringado_1)
medio_pringado_1.mostrar_empleados_a_cargo()

medio_pringado_1.despedir()