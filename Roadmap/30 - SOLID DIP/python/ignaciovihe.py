"""
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
"""
from abc import ABC, abstractmethod
# Incorrecto DIP

class CardPayment:
    def pay(self, quantity):
        print(f"Pagando {quantity} mediante tarjeta")


class PayService:
    def __init__(self, payer: CardPayment):
        self.payer = payer  #Depende directamente de CardPayment, si quiero pagar por Paypal debería modificar PayService.

    def process_payment(self, quantity):
        self.payer.pay(quantity)


# Correcto DIP

class PaymentStrategy(ABC): # Clase abstracta que sirve como interfaz. La clase de clato nivel PaymentService hace referencia a ella.
    @abstractmethod
    def pay(self, quantity):
        pass


class CardPayment(PaymentStrategy):# Si hay que añadir otra metodo de pago sólo se añade una nueva clase.
    def pay(self, quantity):
        print(f"Pagando {quantity} mediante tarjeta")


class PayPalPayment(PaymentStrategy):
    def pay(self, quantity):
        print(f"Pagando {quantity} mediante PayPal")

class BizumPayment(PaymentStrategy):
    def pay(self, quantity):
        print(f"Pagando {quantity} mediante Bizum")


class PaymentService:
    def __init__(self, payment_method: PaymentStrategy):
        self.payment_method = payment_method

    def process_payment(self, quantity):
        self.payment_method.pay(quantity)


card_service = PaymentService(CardPayment())
card_service.process_payment("25€")
paypal_service = PaymentService(PayPalPayment())
paypal_service.process_payment("30€")
bizum_service = PaymentService(BizumPayment())
bizum_service.process_payment("15€")


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

class Sender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(Sender):
    def send(self, message):
        print(f"Enviando el mensaje '{message}' por email.")


class PushSender(Sender):
    def send(self, message):
        print(f"Enviando el mensaje '{message}' por push.")


class SMSSender(Sender):
    def send(self, message):
        print(f"Enviando el mensaje '{message}' por SMS.")


class NotificationService:
    def __init__(self, sender: Sender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)


email_service = NotificationService(EmailSender())
email_service.notify("Tu Pedido ha sido enviado")
sms_service = NotificationService(SMSSender())
sms_service.notify("Tu Pedido ha sido enviado")
push_service = NotificationService(PushSender())
push_service.notify("Tu Pedido ha sido enviado")