from enum import Enum
    
class Weekday(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7
def what_day_is(number):
    try:
        if number > 0 or number < 8:
            print(Weekday(number).name)
    except:
        print("Solo hay 7 días a la semana introduce un número del 1 al 7")
what_day_is(2)
what_day_is(5)

#EXTRA
class Status(Enum):
    PENDIENTE = 0
    ENVIADO = 1
    ENTREGADO = 2
    CANCELADO = 3

class Order:
    
    status = Status.PENDIENTE.name
    #Constructor
    def __init__(self, id):
        self.id = id

    #Mostrar estado pedido
    def show_status(self):
        print(f"El pedido con ID {self.id} esta en estado {self.status}")

    #Modificar estado pedido
    def send(self):
        if self.status == "PENDIENTE":
            self.status = Status.ENVIADO.name
            return self.show_status()
    
    def deliver(self):
        if self.status == "ENVIADO":
            self.status = Status.ENTREGADO.name
            return self.show_status()    
        else:
            print(f"El pedido con ID {self.id} no puede ser entregado ya que aún no ha sido enviado")

    def cancel(self):
        if self.status == "PENDIENTE":
            self.status = Status.CANCELADO.name
            return self.show_status()
        else:
            print(f"El pedido con ID {self.id} no se ha podido cancelar porque ya ha sido {self.status}")

order_1 = Order(1)
order_1.show_status()
order_1.send()
order_1.deliver()
order_1.cancel()

order_2 = Order(2)
order_2.show_status()
order_2.cancel()

order_3 = Order(3)
order_3.show_status()
order_3.deliver()