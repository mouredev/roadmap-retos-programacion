import os, enum
os.system ('cls')

"""* EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
  """

weekdays_list = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
weekdays_tuple = "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"
weekdays_set = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"}
weekdays_dict = dict(enumerate(weekdays_list, start=1))# Se puede crear un diccionario a partir de una lista o tupla 
                                        # donde los valores numéricos serán las claves y los elementos los valores
class Weekdays(enum.Enum): # Creación de clase con Enum desde la cual podremos acceder diréctamente a sus elementos
    Lunes = 1
    Martes = 2
    Miércoles = 3 
    Jueves = 4 
    Viernes =5 
    Sábado = 6 
    Domingo = 7

[print(i,d , end=" ") for i, d in enumerate(weekdays_list, 1)]# Podemos iterar sobre una lista mostrando elemento y valor con enumerate
print()
[print(i,d , end=" ") for i, d in enumerate(weekdays_tuple, 1)]# También sobre una tupla
print()
[print(i,d , end=" ") for i, d in enumerate(weekdays_set, 1)]# Con un set los elementos se asignarán desordenados a los valores 
print()
[print(i,d , end=" ") for i, d in weekdays_dict.items()]
print() 
print(f"El día de la semana correspondiente al número {Weekdays.Miércoles.value} es el {Weekdays.Miércoles.name}")



def show_day(key:int):
    days = list(enumerate(weekdays_list,1))
    if key < (len(weekdays_list)) and key > 0:
        print (f"El día de la semana correspondiente al número {key} es el {days[key-1][1]}")
    else:
        print ("El número debe ser mayor a 0 y menor a 8")
show_day(6)
print("\n\n\n")



"""* DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos."""

class Status (enum.Enum):
    PENDIENTE=1
    ENVIADO=2
    ENTREGADO=3
    CANCELADO=4
class Orders():
    status = Status.value=1
    def __init__(self, id):
        self.id = id
    def waiting_to_cancelled(self):
        if self.status == 1:
           self.status = 4
           self.show_status()
        else:
            print("No se puede cancelar un producto que ya se ha enviado o entregado")  
    def waiting_to_sent(self):
        if self.status==1:
           self.status=2
           self.show_status()
        else:
            print("No se puede enviar un producto que ya se ha enviado, entregado o cancelado")
    def sent_to_delivered(self):
        if  self.status==2:
            self.status=3
            self.show_status()
        else:
            print("No se puede marcar como entregado un producto que no se ha enviado, ya se ha entregado o se ha cancelado")
    def cancelled_to_waiting(self):
        if self.status == 4 or self.status == 1:
           self.status = 1
           self.show_status()
        else:
            print("No se puede volver a poner pendiente un producto que ya se ha enviado o entregado")  
    def show_status(self):
        print(f"El estado del producto {self.id} es: {Status(self.status).name}")
    
orders_instance_1 = Orders(1)
orders_instance_1.sent_to_delivered()# Se intenta entregar un producto que no se ha enviado, devuelve aviso.
orders_instance_1.waiting_to_sent()# El pedido sigue estando pendiente, se envía y devuelve el mensaje de enviado.
orders_instance_1.sent_to_delivered()# El pedido está enviado, se entrega y devuelve el mensaje de entregado.
orders_instance_1.waiting_to_cancelled()# Se intenta cancelar el pedido y devuelve aviso de que ya ha sido enviado o entregado.
orders_instance_2 = Orders(2)
orders_instance_2.cancelled_to_waiting()# Esta función devuelve el producto de cancelado a pendiente, como no se ha cancelado sigue pendiente.
orders_instance_2.waiting_to_cancelled()# Se cancela el producto pendiente y muestra el estado de cancelado.
orders_instance_2.cancelled_to_waiting()# Ahora sí devolvemos el pedido cancelado a pendiente.
orders_instance_2.sent_to_delivered()# Se intenta entregar el pedido y devuelve el aviso de que aun no ha sido enviado.
orders_instance_2.show_status()# Al llamar a este método imprimirá el estado actual del pedido.
orders_instance_1.show_status()
    
    
    
    
    
    
    
    
  

            

