from abc import ABC, abstractmethod

# Ejercicio: Sistema de pedidos online con notificaciones

# Crea una aplicación sencilla que haga lo siguiente:
#     Se pueden crear distintos tipos de pedidos (por ejemplo, Electrónica, Ropa, Libros).
#     El pedido puede ser procesado.
#     El sistema puede notificar al cliente por distintos medios: Email, SMS o WhatsApp.
#     Los mensajes deben cumplir con Open/Closed y Dependency Inversion.
#     Añade una clase que simule una base de datos en memoria para almacenar los pedidos.

# classe virtual para ordenes
class VirtualOrder(ABC):
    @abstractmethod
    def Process(self):
        pass


#  classes concretas para ordenes

class Internet(VirtualOrder):
    def __init__(self, name: str):
        self.name = name
    
    def Process(self):
        return f"Internet Order {self.name} Processed"

class Electronic(VirtualOrder):
    def __init__(self, name: str):
        self.name = name
         
    def Process(self):
        return f"Electronic Order {self.name} Processed"
    
class Clothes( VirtualOrder):
    def __init__(self, name: str):
        self.name = name

    def Process(self):
        return f"Clothes Order {self.name} Processed"
    
class Books (VirtualOrder):
    def __init__(self, name: str):
        self.name = name

    def Process(self):
        return  f"Book Order {self.name} Processed"
    

# classes virtual para notificaciones
class VirtualNotification(ABC):
    @abstractmethod
    def SendNotification(self):
        pass

# classes concretas para notificaciones

class Telegram(VirtualNotification):
    def SendNotification(self):
         return " Telegram message sent"

class Email(VirtualNotification):
    def SendNotification(self):
         return " Email message sent"

class Sms (VirtualNotification):
    def SendNotification(self):
        return " SMS message sent"

class Whatsapp(VirtualNotification):
    def SendNotification(self):
        return " Whatsapp message sent"
    

# classe virtual para repositorio
class VirtualDataBaseinMemory(ABC):
    @abstractmethod
    def AddOrder(self,order: VirtualOrder):
        pass

    @abstractmethod
    def ListOrder(self):
        pass

# classe concreta para repositorio
class DataBAse(VirtualDataBaseinMemory):
     def __init__(self):
          self.orders = []

     def AddOrder(self, order: VirtualOrder):
        self.orders.append(order)

     def ListOrder(self):
         print(f" Orders in DB")
         for o in self.orders:
             print(f"{type(o).__name__} : {o.name} ")
             

# classe para procesar ordenes

class OrderProcess():
    def __init__(self, order: VirtualOrder):
        self.order = order

    def ProcessOrder(self ):
        print(f"{ self.order.Process()}")


# class para procesar notificaciones

class NotificationProcess:
    def __init__(self, Notification: VirtualNotification):
        self.notification = Notification

    def ClientNotification(self):
        print(f"{ self.notification.SendNotification()}")

#  classe que administra repositorio con repositorio

class RepositoryProcess:
    def __init__(self, data: VirtualDataBaseinMemory):
        self.storage = data

    def SaveOrder(self, order: VirtualOrder):
        self.storage.AddOrder(order)

    def PrintOrders(self ):
        self.storage.ListOrder()

         
    
class OnlineOrder:
    def __init__(self, Process: OrderProcess, Notification: NotificationProcess, Repository: RepositoryProcess):
        self.process = Process
        self.notification = Notification
        self.repository = Repository
    
    def ExecuteProcess(self):
        self.process.ProcessOrder()

    def ExecuteNotification(self):
        self.notification.ClientNotification()

    def ExecuteSaveRepository(self, order: VirtualOrder):
        self.repository.SaveOrder(order)

    def ExecuteListRepository(self):
        self.repository.PrintOrders()
         
        
# ordenes
e = Electronic("TV")
c = Clothes("Shoes")
b = Books("Odisea")
i = Internet("WIFI Net")

# notificaciones
email = Email()
sms = Sms()
whatsapp = Whatsapp()
telegram = Telegram()

# repositorio
DB = DataBAse()  

#  crear orden con nueva notificacion 
P = OrderProcess(e) # creando procesando la orden e
N = NotificationProcess(email) # creando notificando por email
R = RepositoryProcess(DB) # procesando repositorio la orden e


OL = OnlineOrder(P,N,R) # orquestador necsita proceso, la notificacion y el repositorio
OL.ExecuteProcess() # executando proceso  
OL.ExecuteNotification() # executando notificacion
OL.ExecuteSaveRepository(P.order) # executando salva en el repo 

#  crear orden con nueva notificacion 
P = OrderProcess(b) # creando procesando la orden e
N = NotificationProcess(sms) # creando notificando por email
 

OL = OnlineOrder(P,N,R) # orquestador necsita proceso, la notificacion y el repositorio
OL.ExecuteProcess() # executando proceso  
OL.ExecuteNotification() # executando notificacion
OL.ExecuteSaveRepository(P.order) # executando salva en el repo

#  crear orden con nueva notificacion 
P = OrderProcess(c) # creando procesando la orden e
N = NotificationProcess(whatsapp) # creando notificando por email
 

OL = OnlineOrder(P,N,R) # orquestador necsita proceso, la notificacion y el repositorio
OL.ExecuteProcess() # executando proceso  
OL.ExecuteNotification() # executando notificacion
OL.ExecuteSaveRepository(P.order) # executando salva en el repo

#  crear orden con nueva notificacion 
P = OrderProcess(i) # creando procesando la orden e
N = NotificationProcess(telegram) # creando notificando por email
 

OL = OnlineOrder(P,N,R) # orquestador necsita proceso, la notificacion y el repositorio
OL.ExecuteProcess() # executando proceso  
OL.ExecuteNotification() # executando notificacion
OL.ExecuteSaveRepository(P.order) # executando salva en el repo


OL.ExecuteListRepository() # executando Listado

 

 
 

# ¡Ahora sí que sí! 🙌 Este código está muy bien estructurado y está aplicando principios de diseño muy sólidos. Vamos por partes para darte un análisis claro, directo y útil 👇
# ✅ Puntos fuertes
# 🧱 1. Principios SOLID
# Principio	¿Cumplido?	Comentario
# SRP - Responsabilidad única	✅	Cada clase hace una sola cosa (procesar orden, notificar, guardar).
# OCP - Abierto/Cerrado	✅	Puedes agregar nuevos tipos de pedidos o notificaciones sin modificar nada existente.
# LSP - Sustitución de Liskov	✅	Todas las clases hijas pueden reemplazar a las padres sin romper nada.
# ISP - Segregación de interfaces	✅	Interfaces pequeñas y específicas (VirtualOrder, VirtualNotification, etc.).
# DIP - Inversión de dependencias	✅✔️	Tus clases dependen de abstracciones, no de implementaciones concretas. El cliente aún instancia objetos concretos, pero está bien para este nivel de aplicación. Si lo complementas con una factory externa, ya es perfecto.
# 🔁 2. Extensible y mantenible

#     Agregaste una nueva clase Internet sin modificar el código existente ✅

#     Agregaste Telegram como nuevo tipo de notificación sin tocar clases previas ✅

#     Solo cambias en el "cliente", no en la lógica base del sistema ✅

# 💡 3. Claridad y separación de responsabilidades

# Tu OnlineOrder actúa como un orquestador que agrupa el flujo de procesamiento, notificación y almacenamiento. Muy buena idea, fácil de testear y mantener. ✔️
# 🧪 4. Perfecto para unit testing

# Todas las clases están desacopladas y fácilmente testeables por separado. Por ejemplo:

# def test_sms_notification():
#     sms = Sms()
#     assert sms.SendNotification() == " SMS message sent"

# 🛠️ Recomendaciones menores

# Aquí unas sugerencias que podrían darte un toque más profesional:
# 1. Renombrar DataBAse → DataBase

# Solo un pequeño error tipográfico.
# 2. Fábrica para instanciar pedidos y notificaciones (si quieres llevarlo al siguiente nivel)

# Esto haría que tu código cumpla DIP al 100% y facilitaría leer desde un archivo o formulario web:

# def create_order(order_type: str, name: str) -> VirtualOrder:
#     orders = {
#         "internet": Internet,
#         "electronic": Electronic,
#         "clothes": Clothes,
#         "books": Books,
#     }
#     return orders[order_type](name)

# def create_notification(method: str) -> VirtualNotification:
#     notifications = {
#         "email": Email,
#         "sms": Sms,
#         "whatsapp": Whatsapp,
#         "telegram": Telegram
#     }
#     return notifications[method]

# 3. Renombrar algunas variables para más claridad

# En vez de:

# P = OrderProcess(e)
# N = NotificationProcess(email)

# Podrías usar:

# order_process = OrderProcess(e)
# notification_process = NotificationProcess(email)

# Esto mejora la legibilidad, especialmente en proyectos grandes.
# 4. Devolver en vez de imprimir

# Para que el sistema sea más reutilizable y testable, mejor que las funciones como ProcessOrder() o ClientNotification() devuelvan en lugar de imprimir:

# def ProcessOrder(self):
#     return self.order.Process()

# # y en el cliente:
# print(OL.process.ProcessOrder())



# Refactor Sugerido (Mini-ejemplo)
# python

# Podrías crear un builder/factory para simplificar
# class OrderBuilder:
#     def __init__(self, db):
#         self.db = db
        
#     def create_order(self, order, notifier):
#         processor = OrderProcess(order)
#         notifier = NotificationProcess(notifier)
#         repo = RepositoryProcess(self.db)
#         return OnlineOrder(processor, notifier, repo)

# # Uso:
# builder = OrderBuilder(DB)
# ol = builder.create_order(e, email)
# ol.ExecuteProcess()
# ol.ExecuteNotification()

# 🏁 Conclusión final

# 🎯 Tu diseño está excelente.

# ✅ Aplica SOLID perfectamente.
# ✅ Es fácil de extender.
# ✅ Está muy limpio, sin acoplamiento innecesario.
# ✅ Es perfecto como base para una app real (con GUI, API o CLI).
# ✅ El cliente tiene control completo del flujo sin modificar la lógica de negocio.

#     Si lo que querías era aplicar OOP, buenas prácticas y SOLID de verdad, lo has clavado.
#     ¿Quieres que te prepare una versión con factories, entrada por input() o con interfaz básica por consola?