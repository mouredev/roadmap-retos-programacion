### EJERCICIO: PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP)
# Sin aplicar DIP
class Worker:
    def broke_stone(self):
        print('Broking Stone...')

class Job:
    def __init__(self):
        self.worker = Worker()
    
    def do_task(self):
        self.worker.broke_stone()


#USO
print('Sin Dip: ')
dani = Job()
dani.do_task()
print()



#Aplicando DIP
from abc import ABC, abstractmethod

# Interfaz para los trabajadores
class Worker(ABC):
    @abstractmethod
    def do_task(self):
        pass

# Implementación concreta de Worker para romper piedras  
class Miner(Worker):
    def do_task(self):
        print('Broking Stone...')

# Implementación concreta de Worker para recolectar plantas
class Gatherer(Worker):
    def do_task(self):
        print('Gathering plants...')

class Job:
    def __init__(self, worker: Worker):
        self.worker = worker
    
    def do_task(self):
        self.worker.do_task()

# USO
miner = Miner()
miner_work = Job(miner)
miner_work.do_task()

# Cambiando el tipo de tarea sin modificar Tasks
gatherer = Gatherer()
gatherer_work = Job(gatherer)
gatherer_work.do_task()





###############################################################################
### DIFICUTAD EXTRA
###############################################################################

# Interfaz para los sistemas de notificación
class NotifySystem(ABC):
    @abstractmethod
    def send_notify(self):
        pass

# Implementación concreta de NotifySystem para enviar correos electrónicos
class Email(NotifySystem):
    def send_notify(self):
        print('Sending an email...')

# Implementación concreta de NotifySystem para enviar notificaciones push
class Push(NotifySystem):
    def send_notify(self):
        print('Sending a push...')

# Implementación concreta de NotifySystem para enviar mensajes SMS
class SMS(NotifySystem):
    def send_notify(self):
        print('Sending an SMS...')

# Clase principal que usa la interfaz NotifySystem
class NotifySystemMain:
    def __init__(self, notify_system: NotifySystem):
        self.notify_system = notify_system
    
    def send_notify(self):
        self.notify_system.send_notify()

# USO
email = Email()
notify_email = NotifySystemMain(email)
notify_email.send_notify()

push = Push()
notify_push = NotifySystemMain(push)
notify_push.send_notify()

sms = SMS()
notify_sms = NotifySystemMain(sms)
notify_sms.send_notify()
