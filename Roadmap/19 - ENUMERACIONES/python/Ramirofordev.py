from enum import Enum

'''
Ejercicio 
Empleando tu lenguaje, explora la definicion del tipo de dato que sirva para definir enumeraciones(Enum)

Crea un Enum que represente los dias de la semana del lunes al domingo, en ese orden. Con ese enumerado, crea una operacion que muestre el nombre del dia de la semana dependienod del numero entero utilizando (del 1 al 7)
'''

# Con una lista y enumerate
week_days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

for number, day in enumerate(week_days, start = 1):
    print(f"{number}: {day}")

class Weekdays(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7

for day in range(1 ,8):
    print(Weekdays(day).name)


'''
Dificultad extra:
Crea un pequeño sistema de gestion del estado de pedidos.
Implementa una clase que defina un pedido con las siguientes caracteristicas:
    * EL pedido tiene un identificador y un estado.
    * El estado es un enum con estos valores: Pendiente, enviado entregado y cancelado.
    * Implementa las funciones que sirvan para modificar el estado:
        * Pedido enviado
        * Pedido cancelado
        * Pedido entregado
    * Implementa una funcion para mostrar un texto descriptivo segun el estado actual
    * Crea diferentes pedidos y muestra como se interactua con ellos
'''

class Estado(Enum):
    Pendiente = 0
    Entregado = 1
    Enviado = 2
    Cancelado = 3

class GestionPedidos():
    def __init__(self, id, estado = Estado.Pendiente):
        self.id = id
        self.estado = estado

    def pendiente(self):
        self.estado = Estado.Pendiente

    def enviar(self):
        if self.estado == Estado.Pendiente:
            self.estado = Estado.Enviado

    def entregar(self):
        if self.estado == Estado.Enviado:
            self.estado = Estado.Entregado
   
    def cancelado(self):
        if self.estado != Estado.Entregado:
            self.estado = Estado.Cancelado

    def show_estado(self):
        print(f"El estado del producto {self.id}, es: {self.estado.name}")

pedido_1 = GestionPedidos(123, Estado.Pendiente)
pedido_1.show_estado()
pedido_1.enviar()
pedido_1.show_estado()
pedido_1.entregar()
pedido_1.show_estado()
pedido_1.cancelado()
pedido_1.show_estado()
