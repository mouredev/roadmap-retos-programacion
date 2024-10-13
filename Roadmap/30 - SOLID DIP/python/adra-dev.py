"""
EJERCICIO:
Explora el "Principio SOLID de Inversión de Dependencias (Dependency 
Inversion Principle, DIP)" y crea un ejemplo simple donde se muestre 
su funcionamiento de forma correcta e incorrecta.

DIFICULTAD EXTRA(opcional):
Crea un sistema de notificaciones.

Requisitos:
1. El sistema puede enviar Email, PUSH y SMS (implementaciones 
específicas).
2. El sistema de notificaciones no puede depender de las 
implementaciones específicas.
Instrucciones:
1. Crea la interfaz o clase abstracta.
2. Desarrolla las implementaciones específicas.
3. Crea el sistema de notificaciones usando el DIP.
4. Desarrolla un código que compruebe que se cumple el principio.

by adra-dev
"""

"""
Dependency Inversion Principle (DIP):
El principio de inversión de dependencias (DIP) es el último 
principio del conjunto SOLID. Este principio establece que:

    "Las abstracciones no deben depender de detalles. Los detalles 
    deben depender de las abstracciones."

documentacion:"https://realpython.com/solid-principles-python/"
    
Considera el siguiente ejemplo: 
Supongamos que está creando una aplicación y tiene una clase FrontEnd
para mostrar datos a los usuarios de una manera amigable. Actualmente, 
la aplicación obtiene sus datos de una base de datos, por lo que 
termina con el siguiente código
"""

# app_dip.py

class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
    
"""
En este ejemplo, la clase FrontEnd depende de la clase BackEnd y de 
su implementación concreta. Se puede decir que ambas clases están 
estrechamente acopladas. 

Este acoplamiento puede dar lugar a problemas de escalabilidad. Por 
ejemplo, supongamos que tu aplicación está creciendo rápidamente y 
quieres que pueda leer datos de una API de REST. ¿Cómo lo harías?

Puede pensar en agregar un nuevo método al backend para recuperar los
datos de la API REST. Sin embargo, eso también requerirá que 
modifique el FrontEnd, que debe estar cerrado a la modificación, de 
acuerdo con el principio de abierto-cerrado. 

Para solucionar el problema, puede aplicar el principio de inversión 
de dependencias y hacer que sus clases dependan de abstracciones en 
lugar de implementaciones concretas como BackEnd. En este ejemplo 
específico, puede introducir una clase DataSource que proporcione la 
interfaz que se usará en sus clases concretas:
"""

# app_dip.py

from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"
    

"""
En este rediseño de las clases, se ha agregado una clase DataSource 
como una abstracción que proporciona la interfaz necesaria, o el 
método .get_data(). Observe cómo FrontEnd ahora depende de la 
interfaz proporcionada por DataSource, que es una abstracción.
"""

db_front_end = FrontEnd(Database())
db_front_end.display_data()

api_front_end = FrontEnd(API())
api_front_end.display_data()


"""
Extra
"""
class NotificationInterface(ABC):
    @abstractmethod
    def get_notification(self):
        pass

class Email(NotificationInterface):
    def get_notification(self):
        return "Email notification"

class PUSH(NotificationInterface):
    def get_notification(self):
        return "PUSH notification"
    
class SMS(NotificationInterface):
    def get_notification(self):
        return "SMS notification"

    
class NotificationSystem(ABC):
    def __init__(self, notification_type):
        self.notification_type = notification_type

    def display_notification(self):
        notification = self.notification_type.get_notification()
        print("Display data:", notification)

notifiatcion_email = NotificationSystem(Email())
notifiatcion_email.display_notification()
notifiatcion_push = NotificationSystem(PUSH())
notifiatcion_push.display_notification()
notifiatcion_sms = NotificationSystem(SMS())
notifiatcion_sms.display_notification()