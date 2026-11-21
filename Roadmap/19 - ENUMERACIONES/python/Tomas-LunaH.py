#  * EJERCICIO:
#  * Empleando tu lenguaje, explora la definición del tipo de dato
#  * que sirva para definir enumeraciones (Enum).
#  * Crea un Enum que represente los días de la semana del lunes
#  * al domingo, en ese orden. Con ese enumerado, crea una operación
#  * que muestre el nombre del día de la semana dependiendo del número entero
#  * utilizado (del 1 al 7).

from enum import Enum

class Days (Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

#Iterando
def find_days (num):
        found = False
        for dia in Days:
            if num == dia.value:
                print(F"El dia es {dia.name}")
                found = True
                break
        if not found :
            print("No se encontro un dia con ese numero")

#Con Enum
def foun_enum (date):
    try :
        found = Days(date)
        print(f"El dias es: {found.name}")
    except Exception as e:
        print(f"Se produjo el error {e}")


foun_enum("a")  



print(Days.DOMINGO)
print(Days.DOMINGO.name)
print(Days.DOMINGO.value)
find_days(4)

#  DIFICULTAD EXTRA (opcional):
#  * Crea un pequeño sistema de gestión del estado de pedidos.
#  * Implementa una clase que defina un pedido con las siguientes características:
#  * - El pedido tiene un identificador y un estado.
#  * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
#  * - Implementa las funciones que sirvan para modificar el estado:
#  *   - Pedido enviado
#  *   - Pedido cancelado
#  *   - Pedido entregado
#  *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
#  * - Implementa una función para mostrar un texto descriptivo según el estado actual.
#  * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 

class  Orders_Status (Enum):
    ENVIADO = "Enviado"
    PENDIENTE = "Pendiente"
    CANCELADO = "Cancelado"
    ENTREGADO = "Entregado"

class Delivers :
    def __init__(self, id: str):
        self.id = id
        self.status = Orders_Status.PENDIENTE
    def send (self):
        order = Orders_Status.PENDIENTE
        if order != self.status:
            print(f"El pedido con el id: {self.id} no se puede enviar por estos motivos (Producto Enviado, Entregado o Cancelado)")

        else:
            print(f"El produto con el id : {self.id} se ha enviado")
            self.status = Orders_Status.ENVIADO

    def delivered (self):
        order = Orders_Status.ENVIADO
        if order != self.status:
            print(f"El pedido con el id: {self.id} no ha sido entregado por estos motivos (Producto no Enviado, Cancelado o Pendiente)")
    
        else:
            print(f"El produto con el id : {self.id} se ha entregado")
            self.status = Orders_Status.ENTREGADO

    def canceled (self):
        if self.status == Orders_Status.ENTREGADO:
            print(f"El pedido con el id: {self.id} no  se puede cancelar por ya se ha entrgado")
        else:
            print(f"El produto con el id : {self.id} se ha cancelado")
            self.status = Orders_Status.CANCELADO
    def show_delivers(self):
        print(f"EL PEDIDO CON EL ID: {self.id} se encuentra en estado de: {self.status.value}")
    

my_product = Delivers("123abc")
my_product.send()
my_product.delivered()
my_product.canceled()
my_product.show_delivers()


my_new_producto = Delivers("1948xzn")
my_new_producto.delivered()
my_new_producto.send()


