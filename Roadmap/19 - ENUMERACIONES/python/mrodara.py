### ENUMERACIONES
'''
Las enumeraciones (enums) son un conjunto de nombres simbólicos (miembros) asignados a valores únicos. 
En Python, el módulo estándar enum permite trabajar con enumeraciones de manera sencilla, 
facilitando la organización y manipulación de conjuntos de valores relacionados.
'''
from enum import Enum

class Week(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7
    
print(Week.LUNES.name)
print(Week.LUNES.value)

def get_week_day(number: int = 1):
    if number < 1 or number > 7:
        print("Error!!!")
        return None
    
    return Week(number).name

print(get_week_day(2))
print(get_week_day(4))
print(get_week_day(7))

### EJERCICIO EXTRA

class Estado(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido:
    def __init__(self, id_pedido, estado):
        self.__id_pedido = id_pedido
        self.__estado = estado

    @property
    def id_pedido(self):
        return self.__id_pedido

    @id_pedido.setter
    def id_pedido(self, id: int):
        self.__id_pedido = id

    @property
    def estado(self):
        return self.__estado

    def cambiar_estado(self, estado: Estado):
        if self.__estado.value == 1 and estado.value == 3:
            print("Error: El estado no puede cambiar de pendiente a entregado hasta que no se haya enviado")
        elif self.__estado.value == 3 and estado.value == 4:
            print("Error: El estado no puede cambiar de entregado a cancelado")
        else:
            print(f"Cambiando el pedido {self.__id_pedido} de {self.__estado.name} a {estado.name}")
            self.__estado = estado

p1 = Pedido(1, Estado.PENDIENTE)
p2 = Pedido(2, Estado.ENVIADO)
p3 = Pedido(3, Estado.ENTREGADO)

print(f"Id: {p1.id_pedido}, Estado: {p1.estado.name}")
print(f"Id: {p2.id_pedido}, Estado: {p2.estado.name}")
print(f"Id: {p3.id_pedido}, Estado: {p3.estado.name}")

# P1 pasa a estado enviado
p1.cambiar_estado(Estado.ENVIADO)
p3.cambiar_estado(Estado.CANCELADO) # Este cambio no se puede realizar
print(p3.estado.name)

### FIN EJERCICIO EXTRA


### FIN ENUMERACIONES