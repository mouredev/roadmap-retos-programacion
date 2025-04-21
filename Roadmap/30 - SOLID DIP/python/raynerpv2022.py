# /*
#  * EJERCICIO:
#  * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
#  * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
#  * de forma correcta e incorrecta.
from abc import ABC, abstractmethod



 
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un sistema de notificaciones.
#  * Requisitos:
#  * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
#  * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
#  * Instrucciones:
#  * 1. Crea la interfaz o clase abstracta.
#  * 2. Desarrolla las implementaciones específicas.
#  * 3. Crea el sistema de notificaciones usando el DIP.
#  * 4. Desarrolla un código que compruebe que se cumple el principio.
#  */


# Sistema de Notificaciones 
# DIP incorrecto



class PostNotification:
    def SendMessage(self):
        print("Sended Notificacion per Post")

# addicionando clase para enviar por email, necesitamos modificar la clase Notificacion

class EmailNotification:
    def SendMessage(self):
        print("Sended Notificacion per Email ") 
     

class Notification:
    def __init__(self, m : PostNotification, e : EmailNotification):
        self.Message = m
        self.email = e

    def PostMessage(self):
        self.Message.SendMessage()

    def EmailMessage(self):
        self.email.SendMessage()

e = EmailNotification()
p = PostNotification()
Mess1 = Notification(p,e)
Mess1.PostMessage()
Mess1.EmailMessage()

# Correcto


class GenericNotification(ABC):
    @abstractmethod
    def SendMessage(self ): 
        pass

class PostNotification(GenericNotification):
    def __init__(self, message):
        self.message = message

    def SendMessage(self):
        print(f"Message {self.message} was sent via POst")

class EmailNotification(GenericNotification):
    def __init__(self, message):
        self.message = message

    def SendMessage(self ):
         print(f"Message {self.message} was sent via Email")
        
class WhatsAPPNotification(GenericNotification):
    def __init__(self, message):
        self.message = message
        
    def SendMessage(self):
         print(f"Message {self.message} was sent via WhatsAPP")

class TelegramNotification(GenericNotification):
    def __init__(self, message):
        self.message = message
    
    def SendMessage(self):
         print(f"Message {self.message} was sent via Telegram")


class Notification:
    def __init__(self, Noti: GenericNotification):
        self.notification = Noti

#  aqui almaceno el mensaje directo en la la instancia de la clase a enviar sea, sms, email, etc.
    def Send(self):
        self.notification.SendMessage()



w = WhatsAPPNotification("Hallo")
p = PostNotification("Hola")
e = EmailNotification("HI")
t = TelegramNotification("Telegram")

n = Notification(w)
n.Send()
n = Notification(p)
n.Send()
n = Notification(e)
n.Send()
n = Notification(t)
n.Send()


 
 

 
# Respuesta de CHatGPT
# Has implementado correctamente el Principio de Inversión de Dependencias (DIP)! Ahora, si deseas seguir aplicando los demás principios SOLID a este ejemplo, podemos revisar cómo mejorar el diseño con cada uno de ellos. Vamos a hacer un breve repaso de cada uno:
# 1. Single Responsibility Principle (SRP):

# Cada clase tiene una única responsabilidad.

#     PostNotification, EmailNotification, y WhatsAPPNotification son responsables de enviar un tipo específico de notificación.

#     Notification es responsable de recibir una notificación y enviarla.
#     Cumple con SRP.

# 2. Open/Closed Principle (OCP):

# El sistema está abierto para su extensión, pero cerrado para su modificación.

#     Si quisieras agregar otro tipo de notificación (como SMS, Push, etc.), simplemente crearías una nueva clase que implemente GenericNotification, sin necesidad de modificar las clases existentes.
#     Cumple con OCP.

# 3. Liskov Substitution Principle (LSP):

# Las subclases deben poder sustituir a sus clases base sin afectar la funcionalidad del sistema.

#     PostNotification, EmailNotification, y WhatsAPPNotification son clases que implementan GenericNotification, lo que asegura que todas se comporten de manera esperada al ser usadas de forma intercambiable.
#     Cumple con LSP.

# 4. Interface Segregation Principle (ISP):

# Las interfaces deben ser específicas y no imponer métodos innecesarios.

#     La interfaz GenericNotification tiene solo el método necesario SendMessage. Si alguna notificación requiere más métodos (como establecer una prioridad, por ejemplo), puedes agregar una nueva interfaz sin hacer cambios innecesarios en las demás.
#     Cumple con ISP.

# 5. Dependency Inversion Principle (DIP):

# Ya lo has implementado correctamente. La clase Notification depende de la interfaz GenericNotification, no de clases concretas, lo que permite que cualquier tipo de notificación sea inyectada sin modificar el comportamiento de Notification.
# Cumple con DIP.
# Resumen:

# Tu diseño sigue correctamente los 5 principios SOLID. Las clases están bien estructuradas y mantienen una separación clara de responsabilidades, haciendo que el código sea extensible, mantenible y fácil de probar.

# Si quieres explorar más sobre estos principios o tienes alguna duda en particular, no dudes en preguntar. ¡Buen trabajo!


         
# ¡Perfecto! Vamos a revisar tu código en Python paso a paso para ver cómo se alinean (o no) con los 5 principios SOLID. Aquí te dejo el análisis detallado:
# ✅ 1. Single Responsibility Principle (SRP)

#     Una clase debe tener una sola responsabilidad.

# ✔️ Cumplido:

# Cada clase tiene una única responsabilidad clara:

#     PostNotification, EmailNotification y WhatsAPPNotification solo envían mensajes por un canal específico.

#     Notification solo coordina el envío.

#     No hay mezcla de lógicas adicionales.

# ✅ 2. Open/Closed Principle (OCP)

#     Abierto para extensión, cerrado para modificación.

# ✔️ Cumplido:

#     Si mañana agregas un nuevo canal (por ejemplo, TelegramNotification), puedes extender el sistema sin modificar las clases existentes.

#     Solo necesitas crear una nueva subclase de GenericNotification.

# class TelegramNotification(GenericNotification):
#     def __init__(self, message):
#         self.message = message

#     def SendMessage(self):
#         print(f"Message {self.message} was sent via Telegram")

# ✅ 3. Liskov Substitution Principle (LSP)

#     Las subclases deben poder sustituir a sus clases base sin problemas.

# ✔️ Cumplido:

#     Todas las clases (PostNotification, EmailNotification, WhatsAPPNotification) pueden reemplazar a GenericNotification en Notification sin romper nada.

# n = Notification(EmailNotification("Hi"))  # funciona igual con cualquier clase hija
# n.Send()

# ✅ 4. Interface Segregation Principle (ISP)

#     Los clientes no deben depender de interfaces que no usan.

# ✔️ Cumplido:

#     GenericNotification tiene una única función abstracta, SendMessage(), y todas las subclases la implementan.

#     No estás forzando a las subclases a implementar métodos que no necesitan.

# ✅ 5. Dependency Inversion Principle (DIP)

#     Depender de abstracciones, no de implementaciones concretas.

# ✔️ Cumplido:

#     La clase Notification depende de GenericNotification (una abstracción), no de clases concretas como EmailNotification.

#     Esto permite intercambiar implementaciones sin tocar Notification.

# class Notification:
#     def __init__(self, Noti: GenericNotification):  # <- buena práctica
#         self.notification = Noti

    

    # EXTRA EXTAR

#     Crear un sistema que permita ejecutar comandos (Start, Shutdown, Login, Logout, Reset, etc.) 
# en distintos sistemas operativos (Windows, Ubuntu, etc.) siguiendo los 5 principios SOLID.

# Requisitos:

#     SRP – Principio de Responsabilidad Única:

#         Cada clase debe encargarse de una sola cosa: enviar un comando, representar un sistema operativo, o coordinar la ejecución.

#     OCP – Abierto para extensión, cerrado para modificación:

#         Debes poder agregar nuevos comandos o nuevos sistemas operativos sin modificar las clases existentes.

#     LSP – Sustitución de Liskov:

#         Las clases hijas (Windows, Ubuntu, etc.) deben poder sustituir a la clase base del sistema operativo sin alterar el comportamiento del programa.

#     ISP – Principio de Segregación de Interfaces:

#         Divide los comandos en interfaces específicas (por ejemplo, ILogin, IShutdown) en lugar de una sola interfaz gigante.

#     DIP – Principio de Inversión de Dependencias:

#         Las clases de alto nivel (como CommandExecutor) deben depender de interfaces abstractas, no de implementaciones concretas.

    
class VirtualCommand(ABC):
    @abstractmethod
    def Execute(self):
        pass



class iStart(VirtualCommand):
    def Execute(self):
        return "Start"

class iShutDown(VirtualCommand):
    def Execute(self):
        return " ShutDown"


class VirtualSO(ABC):
    @abstractmethod
    def Command(self, command : VirtualCommand):
        pass

class iWindows(VirtualSO):
    def Command(self, command: VirtualCommand):
        print(f" Command {command.Execute()} in Windows")

class iUbuntu(VirtualSO):
    def Command(self, command : VirtualCommand):
         print(f" Command {command.Execute()} in Ubuntu")


class ExecutTerminal:
    def __init__(self,command: VirtualCommand, so: VirtualSO):
        self.command = command
        self.so = so

    def Execute(self):
        self.so.Command(self.command)

start = iStart()
shutdown = iShutDown()
so_w = iWindows()
so_u = iUbuntu()
ex = ExecutTerminal(start,so_w)
ex.Execute()
ex = ExecutTerminal(shutdown, so_u)
ex.Execute()



 


# ✅ 1. SRP – Principio de Responsabilidad Única

# Cada clase tiene una responsabilidad única:

#     VirtualCommand define una interfaz para comandos.

#     iStart e iShutDown implementan comandos concretos.

#     VirtualSO es la abstracción para los sistemas operativos.

#     iWindows e iUbuntu ejecutan comandos específicos en su SO.

#     ExecutTerminal orquesta la ejecución, pero no se encarga de los detalles internos de comandos ni SO.

# ✅ Cumplido.
# ✅ 2. OCP – Principio de Abierto/Cerrado

# Tu código está abierto a extensión (puedes crear nuevos comandos o SOs), pero cerrado a modificación (no necesitas tocar las clases existentes para extender).

# Por ejemplo:

#     Puedes agregar iRestart() sin tocar ExecutTerminal.

#     Puedes crear un nuevo SO como iMacOS.

# ✅ Cumplido.
# ✅ 3. LSP – Principio de Sustitución de Liskov

# Las instancias de VirtualCommand (iStart, iShutDown) pueden reemplazar sin problema a su clase base VirtualCommand en cualquier parte del código sin romper nada.

# ✅ Cumplido.
# ✅ 4. ISP – Principio de Segregación de Interfaces

# Estás usando interfaces (VirtualCommand, VirtualSO) con métodos mínimos y necesarios. No obligas a las clases a implementar métodos que no necesitan.

# ✅ Cumplido.
# ✅ 5. DIP – Principio de Inversión de Dependencias

# ExecutTerminal depende de abstracciones, no de clases concretas:

# def __init__(self, command: VirtualCommand, so: VirtualSO)

# Eso te da flexibilidad total para cambiar implementaciones sin afectar la lógica de ExecutTerminal.

# ✅ Cumplido.
# 🔧 Sugerencias mínimas (opcional):

#     Los nombres como iStart e iShutDown podrían cambiarse a StartCommand y ShutDownCommand para ser más claros (prefijo "i" se usa a veces para interfaces, lo cual puede llevar a confusión).

#     Si más adelante quieres ejecutar múltiples comandos en fila, podrías añadir una lista de comandos o un patrón Command más completo (con undo, etc.).
