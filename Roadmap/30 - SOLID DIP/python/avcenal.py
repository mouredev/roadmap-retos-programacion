"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
"""
#INCORRECTO
class OtherPaymentService():
    def paypal_payment(self,quantity:int|float):
        print(f"Estas pagando {quantity} EUR a través de Paypal")

    def stripe_payment(self,quantity:int|float):
        print(f"Estas pagando {quantity} EUR a través de Stripe")

other_payment_service = OtherPaymentService()
other_payment_service.paypal_payment(255.30)
other_payment_service.stripe_payment(125.50)
print("\n")

#CORRECTO
from abc import ABC, abstractmethod

class PaymentService(ABC):
    @abstractmethod
    def payment(self,quantity:int|float):
        pass

class PayPalPaymentService(PaymentService):
    def payment(self,quantity:int|float):
        print(f"Estas pagando {quantity} EUR a través de Paypal")

class StripePaymentService(PaymentService):
    def payment(self,quantity:int|float):
        print(f"Estas pagando {quantity} EUR a través de Stripe")

class PaymentProcessor():
    def process_payment(self,payment_service:PaymentService,quantity:int|float):
        payment_service.payment(quantity)

paypal_payment = PayPalPaymentService()
stripe_payment = StripePaymentService()
payment_processor = PaymentProcessor()
payment_processor.process_payment(payment_service=paypal_payment,quantity=255.30)
payment_processor.process_payment(payment_service=stripe_payment,quantity=125.50)
print("\n")

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
class MessagingChannel(ABC):
    @abstractmethod
    def send_message(self,message:str):
        pass

class SMSChannel(MessagingChannel):
    def send_message(self,message:str):
        print(f"Estás enviando a través de SMS el siguiente mensaje:\n\"{message}\"\n")

class PushChannel(MessagingChannel):
    def send_message(self,message:str):
        print(f"Estás enviando a través de PUSH el siguiente mensaje:\n\"{message}\"\n")

class EmailChannel(MessagingChannel):
    def send_message(self,message:str):
        print(f"Estás enviando a través de PUSH el siguiente mensaje:\n\"{message}\"\n")

class NotificationSystem():
    def send_notification(self,message:str,channel:MessagingChannel):
        channel.send_message(message)

notification_system = NotificationSystem()

notification_system.send_notification(message="Alex, ya tienes tu pedido preparado",channel=SMSChannel())
notification_system.send_notification(message="Alex, tienes un nuevo mensaje en tu bandeja de entrada",channel=PushChannel())
notification_system.send_notification(message="Alex, aquí tienes la newsletter quincenal de la comunidad",channel=EmailChannel())
