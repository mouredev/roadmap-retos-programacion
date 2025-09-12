from enum import Enum

class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    def showDayWeek(number):
        if number == 1:
            return Week.MONDAY.name
        elif number == 2:
            return Week.TUESDAY.name
        elif number == 3:
            return Week.WEDNESDAY.name
        elif number == 4:
            return Week.THURSDAY.name
        elif number == 5:
            return Week.FRIDAY.name
        elif number == 6:
            return Week.SATURDAY.name
        elif number == 7:
            return Week.SUNDAY.name
        else:
            return "Elige el número de día de la semana, del 1 al 7"

# print(Week.showDayWeek(1)) # Monday

# Clase para definir los distintos estados de un pedido
class Status(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELED = 4

    
# Clase para definir un pedido
class Order ():
    # Constructor
    def __init__(self, id, numberStatus):
        self.id = id
        self.numberStatus = numberStatus
        
    # Función para mostrar el estado del pedido
    def showStatus(self):
        status = ""
        if self.numberStatus == 1:
            status = Status.PENDING.name
        elif self.numberStatus == 2:
            status = Status.SHIPPED.name
        elif self.numberStatus == 3:
            status = Status.DELIVERED.name
        elif self.numberStatus == 4:
            status = Status.CANCELED.name
        else:
            status = "Error en el pedido"
        return status


    # Función para modificar el estado
    def changeStatus (self):
        if self.numberStatus == 1: # si está pendiente puede pasar a enviado
            self.numberStatus = 2
        elif self.numberStatus == 2: #si está enviado puede pasar a entregado
            self.numberStatus = 3
        elif self.numberStatus == 3: # si está entregado no se puede modificar su estado
            print ("El pedido ya ha sido entregado")
        elif self.numberStatus == 4: # si se ha cancelado no se puede modificar su estado
            print ("El pedido ha sido cancelado")
        else:
            print("Hay algún error en su pedido")
        return self.numberStatus
    
    # Función para mostrar un texto descriptivo según el estado actual
    def commentStatus(self):
        comment = ""
        if self.numberStatus == 1:
            comment = f"El estado de su pedido es: {Status.PENDING.name}. Se enviará en los próximos días."
        elif self.numberStatus == 2:
            comment = f"El estado de su pedido es: {Status.SHIPPED.name}. Lo recibirá en los próximos días."
        elif self.numberStatus == 3:
            comment = f"El estado de su pedido es: {Status.DELIVERED.name}."
        elif self.numberStatus == 4:
            comment = f"El estado de su pedido es: {Status.CANCELED.name}. Si desea que se lo enviemos vuelva a solicitarlo"
        else:
            comment = "Hay un error en su pedido."
        return comment
 
                
# Diferentes pedidos de ejemplo

order1 = Order(1, 1) # primer objeto order1
print("ID:", order1.id)
print("Número de estado:", order1.numberStatus)
print("Estado:", order1.showStatus())
print("Comentario:", order1.commentStatus())
print("Cambio de estado:", order1.changeStatus())
print("Nuevo estado:", order1.showStatus())
print("Comentario del estado nuevo:", order1.commentStatus())

order2 = Order(2, 4) # segundo objeto order2
print("ID:", order2.id)
print("Número de estado:", order2.numberStatus)
print("Estado:", order2.showStatus())
print("Comentario:", order2.commentStatus())
print("Cambio de estado:", order2.changeStatus())
print("Nuevo estado:", order2.showStatus())
print("Comentario del estado nuevo:", order2.commentStatus())