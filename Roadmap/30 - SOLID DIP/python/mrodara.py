### Principio de Inversión de Dependencias (Dependency Inversion Principle, DIP)

'''
Este principio establece que:

Los módulos de alto nivel NO deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones.

Las abstracciones NO deben depender de los detalles. Los detalles DEBEN depender de las abstracciones.

En resumen, el DIP promueve que las clases principales (alto nivel) dependan de interfaces o abstracciones, 
en lugar de depender directamente de clases concretas (bajo nivel).
'''

'''
Ventajas:

+ Reduce el acoplamiento:
    Los módulos de alto nivel no dependen de los detalles específicos de implementación.
+ Facilita el mantenimiento:
    Los detalles de implementación pueden cambiar sin afectar a las clases principales.
+ Aumenta la flexibilidad y la extensibilidad:
    Es más sencillo sustituir o añadir implementaciones concretas al depender de abstracciones.

'''

# EJEMPLO QUE VIOLA EL PRINCIPIO

class CreditCardPayment():
    
    def proccess_payment(self, amount):
        print(f"Procesando pago con tarjeta de crédito: {amount} €")

class OrderProccesor():
    
    def __init__(self):
        self.payment_proccessor = CreditCardPayment()
    
    def proccess_order(self, amount):
        self.payment_proccessor.proccess_payment(amount=amount)

'''
Problemas detectados:

+ Dependencia directa:
    OrderProcessor está acoplada directamente a CreditCardPayment. 
    No se puede usar otro método de pago sin modificar OrderProcessor.
+ Falta de flexibilidad:
    Si necesitas añadir PayPalPayment o CryptoPayment, tendrás que modificar el código de OrderProcessor.
'''

# FIN EJEMPLO QUE VIOLA EL PRINCIPIO

# REDISEÑO PARA CUMPLIR CON EL PRINCIPIO
from abc import ABC, abstractmethod

class PaymentProccessor(ABC):
    
    @abstractmethod
    def proccess_payment(self, amount):
        pass

class CreditCardPayment(PaymentProccessor):
    
    def proccess_payment(self, amount):
        print(f"Procesando pago con tarjeta de crédito: {amount} €")

class PayPalPayment(PaymentProccessor):
    
    def proccess_payment(self, amount):
        print(f"Procesando el pago mediante Paypal: {amount} €")

class BizumPayment(PaymentProccessor):
    
    def proccess_payment(self, amount):
        print(f"Procesando el pago mediante Bizum: {amount} €")


# Clase de Alto nivel
class OrderProccessor():
    
    def __init__(self, payment_proccessor):
        self.payment_proccessor = payment_proccessor
    
    def proccess_order(self, amount):
        self.payment_proccessor.proccess_payment(amount=amount)

order = OrderProccessor(CreditCardPayment())
order.proccess_order(amount=100)

order = OrderProccessor(PayPalPayment())
order.proccess_order(amount=200)

order = OrderProccessor(BizumPayment())
order.proccess_order(amount=300)

# FIN REDISEÑO PARA CUMPLIR CON EL PRINCIPIO

## EJERCICIO EXTRA

# CLASE ABSTRACTA
class Notifier(ABC):
    
    @abstractmethod
    def send_notification(self, message):
        pass

#Específicas
class EmailNotifier(Notifier):
    
    def send_notification(self, message):
        print(f"Enviando eamil con el mensaje {message}")

class PushNotifier(Notifier):
    
    def send_notification(self, message):
        print(f"Enviando mensaje Push con texto: {message}")

class SmsNotifier(Notifier):
    def send_notification(self, message):
        print(f"Enviando mensaje SMS con texto: {message}")

# Alto nivel
class NotificationSender():
    
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    
    def send_notification(self, message):
        self.notifier.send_notification(message)
        

# Batería de pruebas
email_sender = NotificationSender(EmailNotifier())
email_sender.send_notification("Hola soy un Email")

push_sender = NotificationSender(PushNotifier())
push_sender.send_notification("Hola soy un Push")

sms_sender = NotificationSender(SmsNotifier())
sms_sender.send_notification("Hola soy un SMS")


## FIN EJERCICIO EXTRA

### FIN Principio de Inversión de Dependencias (Dependency Inversion Principle, DIP)