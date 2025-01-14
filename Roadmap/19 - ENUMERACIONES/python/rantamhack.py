'''
* EJERCICIO:
* Empleando tu lenguaje, explora la definicion del tipo de dato
* que sirva para definir enumeraciones (Enum).
* Crea un Enum que represente los dias de la semana del lunes
* al domingo, en ese orden. Con ese enumerado, crea una operacion
* que muestre el nombre del dia de la semana dependiendo del numero entero
* utilizado (del 1 al 7).
'''

print("\n\n=======================================EJERCICIO=======================================\n\n")

print("\nLas enumeraciones son un conjunto de nombres simbolicos (miembros) vinculados a valores unicos y constantes\n")

from enum import Enum

week = Enum(
    value = 'week',
    names = ('MONDAY TUESDAY WEDNESDAY THURSDAY FRIDAY SATURDAY SUNDAY'),
)

print(f"El valor del primer dia de la semana (lunes) es: {week.MONDAY.value}\n")
print(f"El valor nombre del septimo dia de la semana es: {week(7)}\n")

print("El valor se asigna a cada uno de los miembros automaticamente\n")
for day in week:
    print(f"\t{day.name, '->', day.value}")

'''
"Otra forma de expresion valida es"
class week (Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    
print(week(7))
print(week.SATURDAY.value)

for day in week:
    print(day.name, '->', day.value)
'''

"=========================================================================================================================="


'''
* DIFICULTAD EXTRA (opcional):
* Crea un pequeño sistema de gestion del estado de pedidos.
* Implementa una clase que defina un pedido con las siguientes caracteri­sticas:
* - El pedido tiene un identificador y un estado.
* - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
* - Implementa las funciones que sirvan para modificar el estado:
*   - Pedido enviado
*   - Pedido cancelado
*   - Pedido entregado
*   (Establece una logica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
* - Implementa una funcion para mostrar un texto descriptivo segun el estado actual.
* - Crea diferentes pedidos y muestra como se interactua con ellos. 
'''

print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")

    
class order_management(Enum):
    PENDING = 1
    SENT = 2
    DELIVERED = 3
    CANCELED = 4        
    
class order:
    def __init__(self, id):
        self.id = id
        self.status = order_management(1)
        
    def send_order(self):
        if self.status == order_management(1):
            print(f"The order with the id {self.id} has been received and is ready to be shipped\n")
            self.status = order_management(2)
            print(f"The order with the id {self.id} has already been submitted\n")
        else: 
            self.status == order_management(4)
            print(f"The order with the id {self.id} has been cancelled\n")
            
    
    def delivered(self):
        if self.status == order_management(2):
            self.status = order_management(3)
            print(f"The order with the id {self.id} has been delivered\n")
    
    def cancelled(self):
        if self.status == order_management(1) or self.status == order_management(2):
            print(f"The order with the id {self.id} has been cancelled\n")
            self.status = order_management(4)
        else:
            self.status == order_management(3)
            print(f"The order with the id {self.id} has been delivered and cannot be cancelled\n")
    
    def show_status(self):
        print(f"The order with id {self.id} is in status {self.status.name}\n")
            
  
  
order1 = order(100)
order1.show_status()

order1.send_order()
order1.show_status()

order1.cancelled()
order1.show_status() 

order2 = order(101)
order2.show_status()

order2.send_order()
order2.show_status()

order2.delivered()
order2.show_status()

order2.cancelled()
order2.show_status()        
       

