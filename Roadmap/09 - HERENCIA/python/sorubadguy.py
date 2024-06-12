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
    pass

class Gerente(Empleado):

    def imprimir_gerente(self):
        print(self.id)
        print(self.nombre)
        print(self.paga)
        print(self.horario)

    def imprimir_tarea(self):
        print(f"{self.nombre} es gerente general")

class Gerente_Proyecto(Empleado):
    
    def agregar_proyecto(self, proyecto: list):
        self.proyecto = []
        self.proyecto.append(proyecto)
    
    def quitar_proyecto(self):

        salir = False
        while(not salir):
            print("Seleccione el proyecto finalizado")
            for i in range(len(self.proyecto)):
                print(f"{i}: {self.proyecto[i]}")
            
            try:
                self.proyecto.pop(int(input("Ingrese el proyecto finalizado: ")))
            except:
                print("Opcion incorrecta")
            finally:
                salir = True


class Programador(Empleado):
    pass