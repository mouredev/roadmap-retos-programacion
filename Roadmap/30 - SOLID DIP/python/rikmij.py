from abc import ABC, abstractmethod

#Uso incorrecto
class Worker:
    def __init__(self, name):
        self.name = name
    
    def to_work(self):
        return f"Soy {self.name} y estoy trabajando"

class Proyect:
    def __init__(self, project):
        self.project = project
    
    def work_in_project(self):
        worker_name = Worker("John")
        return f"{worker_name.name} está trabajando en {self.project}"

proy = Proyect("Google")
print(proy.work_in_project())

'''
Aquí incumplimos el DIP porque vemos que el proyecto depende del trabajador, y si cambiara el trabajador
el proyecto se rompe, y eso no debe ocurrir
'''

#Uso correcto
class Department(ABC):
    @abstractmethod
    def work(self):
        pass

class Employee(Department):
    def __init__(self, name):
        self.name = name
    
    def work(self):
        return f"Soy {self.name} y estoy trabajando"

class Project(Department):
    def __init__(self, project_name):
        self.project_name = project_name
    
    def work(self):
        return f"El equipo está trabajando en {self.project_name}"

proj = Project("BushiGPT")
print(proj.work())

print("\n", "*"*7, " EJERCICIO EXTRA ", "*"*7)

class Notification(ABC):
    @abstractmethod
    def send_notification(user):
        pass

class Send_email(Notification):
    def send_notification(user):
        dest = input("Para: ")
        subject = input("Asunto: ")
        text = input("Mensaje: ")

        return f"De: {user}\nPara: {dest}\nAsunto: {subject}\n {text}"

class Send_push(Notification):
    def send_notification(user):
        text = input("Mensaje: ")

        return f"@{user}\n {text}"

class Send_sms(Notification):
    def send_notification(user):
        text = input("Mensaje: ")

        return f"De: {user}\n {text}"

def send_message():
    print("¿Qué tipo de notificación quieres enviar?\n",
                "1.- Correo\n",
                "2.- Push\n",
                "3.- SMS\n")
    option = int(input())

    match option:
        case 1:
            print(Send_email.send_notification("ejemplo@prueba.com"))
        case 2:
            print(Send_push.send_notification("TipodeIncognito"))
        case 3:
            print(Send_sms.send_notification(123456789))

send_message()
