"""
*Herencia
"""

class Animal:
    
    def __init__(self, patas: int, color_pelo: str, tipo_pelo: str, raza: str) -> None:
        self.patas = patas
        self.color_pelo = color_pelo
        self.tipo_pelo = tipo_pelo
        self.raza = raza
    
    def imprimir_caracteristicas(self):
        print(self.raza)
        print(self.color_pelo)
        print(self.tipo_pelo)
        print(self.patas)

class Perro(Animal):
    
    def sonido(self, sonido = "Guau"):
        self.sonido = sonido

    def imprimir_sonido(self):
        print(self.sonido)

class Gato(Animal):

    def sonido(self, sonido = "Miau"):
        self.sonido = sonido


    def imprimir_sonido(self):
        print(self.sonido)

perro = Perro(4, "negro", "corto", "labrador")
perro.sonido("Guau")
gato = Gato(4, "marron", "largo", "gato")
gato.sonido("Miau")
perro.imprimir_caracteristicas()
perro.imprimir_sonido()
gato.imprimir_caracteristicas()
gato.imprimir_sonido()

"""
!Extra
"""

class Empleado():

    def __init__(self, carga_horaria: int, paga: float, id: int, nombre: str) -> None:
        self.carga_horaria = carga_horaria
        self.paga = paga
        self.nombre = nombre
        self.id = id
    
    def mostrar_datos_base(self):
        print(f"id: {self.id}\nnombre: {self.nombre}\ncarga horaria: {self.carga_horaria} horas\npaga: {self.paga}")

class Gerente(Empleado):

    def imprimir_tarea(self):
        print(f"{self.nombre} es gerente general")

class Gerente_Proyecto(Empleado):
    
    def agregar_proyecto(self, proyecto: list):
        self.proyecto = []
        self.proyecto.append(proyecto)

    def mostrar_proyectos(self):
        for i in range(0, len(self.proyecto)):
            print(self.proyecto[i])


class Programador(Empleado):

    def estoy_programando(self):
        print(f"{self.nombre} esta programando")

empleado1 = Empleado(4, 35.5, 1, "Pedrito")
empleado1.mostrar_datos_base()

gerente1 = Gerente(8, 20, 2, "pancho")
gerente1.mostrar_datos_base()
gerente1.imprimir_tarea()

gerente2 = Gerente_Proyecto(10, 15.4, 3, "Pablo")
gerente2.agregar_proyecto(["web organizacion", "pagos"])
gerente2.mostrar_datos_base()
gerente2.mostrar_proyectos()

programador1 = Programador(5, 8, 4, "Fede")
programador1.estoy_programando()