"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
 */
"""
'Sin Aplicar'
class Saludo:
    def accion(self):
        print("Buenos Dias")

class Persona:
    def __init__(self,saludo:Saludo) -> None:
        self.saludo = saludo
    
# Prueba
yo = Persona(Saludo())
yo.saludo.accion()

'Aplicado'
class Interacion:
    def accion(self):
        pass

class Saludo(Interacion):
    def accion(self):
        print("Buenos dias")

class Insulto(Interacion):
    def accion(self):
        print("Eres un Pechso Lata")

class Persona:
    def __init__(self,interacion:Interacion) -> None:
        self.interacion = interacion
    
yo = Persona(Saludo())
otro = Persona(Insulto())

yo.interacion.accion()
otro.interacion.accion()
print()

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
"""
class Notificacion:
    def enviar(self):
        pass

class Email(Notificacion):
    def __init__(self,mail) -> None:
        self.mail = mail
    def enviar(self):
        print(f"Enviando un Email a {self.mail}")

class Push(Notificacion):
    def __init__(self,push) -> None:
        self.push = push
    
    def enviar(self):
        print(f"Haciendo Push a {self.push}")

class Sms(Notificacion):
    def __init__(self,tlf) -> None:
        self.tlf = tlf

    def enviar(self):
        print(f"Enviando SMS al telefono {self.tlf}")

class Aviso:
    def __init__(self,notificacion) -> None:
        self.notificacion = notificacion

# Prueba
def test_notificacion():
    email = Aviso(Email("emmanuelmmontesinos@gmail.com"))
    push = Aviso(Push("github@EmmanuelMMontesinos"))
    sms = Aviso(Sms("666555444"))

    email.notificacion.enviar()
    push.notificacion.enviar()
    sms.notificacion.enviar()

test_notificacion()