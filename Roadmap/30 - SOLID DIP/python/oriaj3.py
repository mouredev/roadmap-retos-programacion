""" 
30 - SOLID DIP - Principio de Inversión de Dependencias
Autor de la solución: oriaj3

Teoría: 
El principio de inversión de dependencias (DIP) establece que las entidades de alto nivel no deben 
depender de las entidades de bajo nivel. Ambas deben depender de abstracciones. Además, las abstracciones 
no deben depender de los detalles. Los detalles deben depender de las abstracciones.

En otras palabras, las clases de alto nivel no deben depender de las clases de bajo nivel. Ambas deben
depender de abstracciones. Las abstracciones no deben depender de los detalles. Los detalles deben depender
de las abstracciones.

Por ejemplo, si una clase A depende de una clase B, y la clase B depende de una clase C, entonces la clase A
depende de la clase C. Esto viola el principio de inversión de dependencias.

class C():

class B(C):

class A(B):

En este caso, la clase A depende de la clase C, lo que viola el principio de inversión de dependencias.
"""

"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
"""

### Ejemplo sin cumplir el DIP Un sistema de registro (logging) que puede escribir en diferentes destinos (consola, web, base de datos).

class LoginConsola:
    def __init__(self, user, psswd):
        self.user = user
        self.psswd = psswd

    def log(self, user, passwd):
        if self.user == user and self.psswd == passwd:
            print(f"Usuario: {user} logueado en consola")
        else:
            print("Usuario o contraseña incorrectos")

class LoginWeb:
    def __init__(self, user, psswd):
        self.user = user
        self.psswd = psswd

    def log(self, user, psswd):
        if self.user == user and self.psswd == psswd:
            print(f"Usuario: {user} logueado en web")
        else:
            print("Usuario o contraseña incorrectos")
    
class LoginBD:
    def __init__(self, user, psswd):
        self.user = user
        self.psswd = psswd

    def log(self, user, psswd):
        if self.user == user and self.psswd == psswd:
            print(f"Usuario: {user} logueado en base de datos")
        else:
            print("Usuario o contraseña incorrectos")
class GestorLogin:
    def __init__(self):
        self.login_consola = LoginConsola("admin", "admin")
        self.login_web = LoginWeb("admin", "admin")
        self.login_bd = LoginBD("admin", "admin")

    def login(self, user, psswd, destino):
        if destino == "consola":
            self.login_consola.log(user, psswd)
        elif destino == "web":
            self.login_web.log(user, psswd)
        elif destino == "bd":
            self.login_bd.log(user, psswd)
        else:
            print("Destino incorrecto")

gestor = GestorLogin()

gestor.login("admin", "admin", "consola")
gestor.login("admin", "admin", "web")
gestor.login("admin", "admin", "bd")

### Ejemplo cumpliendo el DIP
from abc import ABC, abstractmethod

class loginInterface(ABC):
    @abstractmethod
    def log(self, user, psswd):
        pass
    
class Login_Consola(loginInterface):
    def __init__(self, user, psswd):
        self.user = user
        self.psswd = psswd

    def log(self, user, passwd):
        if self.user == user and self.psswd == passwd:
            print(f"**Usuario: {user} logueado en consola")
        else:
            print("Usuario o contraseña incorrectos")
            
class Login_Web(loginInterface):
    def __init__(self, user, psswd):
        self.user = user
        self.psswd = psswd

    def log(self, user, psswd):
        if self.user == user and self.psswd == psswd:
            print(f"**Usuario: {user} logueado en web")
        else:
            print("Usuario o contraseña incorrectos")

class Login_BD(loginInterface):
    def __init__(self, user, psswd):
        self.user = user
        self.psswd = psswd

    def log(self, user, psswd):
        if self.user == user and self.psswd == psswd:
            print(f"**Usuario: {user} logueado en base de datos")
        else:
            print("Usuario o contraseña incorrectos")

class gestorLogin:
    def __init__(self):
        self.logins = [Login_Consola("admin", "admin"), Login_Web("admin", "admin"), Login_BD("admin", "admin")]
        
    def login(self, user, psswd):
        for login in self.logins:
            login.log(user, psswd)

gestor = gestorLogin()
gestor.login("admin", "admin")


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un sistema de notificaciones.
 * Requisitos:
 * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 * Instrucciones:
 * 1. Crea la interfaz o clase abstracta.
 * 2. Desarrolla las implementaciones específicas.
 * 3. Crea el sistema de notificaciones usando el DIP.
 * 4. Desarrolla un código que compruebe que se cumple el principio.
 */
""" 

#Ejemplo sin cumplir el DIP
class NotificacionEmail1:
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")
        
class NotificacionSMS1:
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")
        
class NotificacionPush1:
    def enviar(self, mensaje):
        print(f"Enviando PUSH: {mensaje}")
        
class GestorNotificaciones1:
    def __init__(self):
        self.email = NotificacionEmail1()
        self.sms = NotificacionSMS1()
        self.push = NotificacionPush1()
        
    def enviarNotificacion(self, mensaje):
        self.email.enviar(mensaje)
        self.sms.enviar(mensaje)
        self.push.enviar(mensaje)



#Ejemplo cumpliendo el DIP
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class NotificacionEmail(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")

class NotificacionSMS(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")
        
class NotificacionPush(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando PUSH: {mensaje}")
        
class GestorNotificaciones:
    def __init__(self):
        self.notificaciones = []
        
    def agregarNotificacion(self, notificacion):
        self.notificaciones.append(notificacion)
        
    def enviarNotificacion(self, mensaje):
        for notificacion in self.notificaciones:
            notificacion.enviar(mensaje)
            
gestor = GestorNotificaciones()
gestor.agregarNotificacion(NotificacionEmail())
gestor.agregarNotificacion(NotificacionSMS())
gestor.agregarNotificacion(NotificacionPush())

gestor.enviarNotificacion("Hola mundo")

