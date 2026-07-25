"""
Enumeracion (enums)
"""

# Es una coleccion de nombres que esta asociado a valores
# Es una forma de darle significado claro y legible a los datos
# Se crean importando el modulo 'enum' y luego y luego se define la clase que herada enum

from enum import Enum

class Color(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3

# Cada iembro tiene un nombre(ROJO) y un valor(1) asociado 

print(Color.ROJO)
print(Color.ROJO.value)
print(Color.ROJO.name)


"""
Caracteristicas
"""

# Unicos: Los valores en una enumeracion son unicos
# se usa el decorador @unique para asegurarnos de que no existan duplicados

from enum import Enum, unique

@unique
class Dia(Enum):
    LUNES = 1
    MARTES = 2
    # MIERCOLES = 1  Esto lanzaria un error

# Iterables: Pueden recorrer los miembros de una enumeracion

for color in Color:
    print(color)


# Inmutables: Una vez definidos no pueden cambiar su valor

# Tipos especiales: 
    # IntEnum: Para valores enteros y compatibles con operaciones matematicas
    # Flag: Para convinar valores como banderas binarias

from enum import Enum

class Semaforo(Enum):
    ROJO = 'Alto'
    AMARILLO = 'Preparate'
    VERDE = 'Avanza'

luz_actual = Semaforo.AMARILLO
print(f'Estado del semaforo: {luz_actual.value}')


"""
Por que usar enumeraciones
"""

# Claridad: El codigo es ma legible y menos propenso a errores
# Seguridad: Evita que se usen valores invalidos accidentalmente
# Mantenibilidad: Si se requiere cambiar un valor, solo se hace en la definicion de la enumeracion 


"""
Ejercicio
"""

from enum import Enum, unique

@unique
class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def obtener_dia(numero: int):
    print(f'Dia de la semana: {DiaSemana(numero).name}')

obtener_dia(1)
obtener_dia(5)


"""
Extra
"""

from enum import Enum, unique

@unique
class Estado(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Orden:

    status = Estado.PENDIENTE

    def __init__(self, id) -> None:
        self.id = id

    def enviado(self):
        if self.status == Estado.PENDIENTE:
            self.status = Estado.ENVIADO
            self.mostrar_estado()
        else:
            ('El pedido ya ha sido enviado o cancelado.')

    def entregado(self):
        if self.status == Estado.ENVIADO:
            self.status = Estado.ENTREGADO
            self.mostrar_estado()
        else:
            print('El pedido debe ser enviado antes de entregarse.')

    def cancelado(self):
        if self.status != Estado.ENTREGADO:
            self.status = Estado.CANCELADO
            self.mostrar_estado()
        else:
            print('El pedido no se puede cancelar.')

    def mostrar_estado(self):
        print(f'El estado del pedido {self.id} es: {self.status.name}')


orden_uno = Orden(1)
orden_uno.mostrar_estado()
orden_uno.entregado()
orden_uno.enviado()
orden_uno.entregado()
orden_uno.cancelado()