#30 { Retos para Programadores } Principio SOLID de Inversión de Dependencias (Dependency Inversion Principle, DIP) 

# Bibliography reference:
# The Web Development Glossary (Jens Oliver Meiert) (Z-Library)
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
 *
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

""" Dependency Inversion Principle
A specific form of decoupling software modules. When following this
principle, the conventional dependency relationships established from
high-level policy-setting modules to low-level dependency modules are
reversed, thus rendering high-level modules independent of the low-level
module implementation details. The principle states 1) that high-level
modules should not depend on low-level modules, but that both should
depend on abstractions (e.g., interfaces), and 2) that abstractions should
not depend on details, but that details (concrete implementations) should
depend on abstractions.

A class that contains methods for use by other classes without having to be
the parent class of those other classes. How those other classes gain access
to the mixin’s methods depends on the language. Mixins are sometimes
described as being “included” rather than “inherited.” Mixins encourage
code reuse and can be used to avoid the inheritance ambiguity that
multiple inheritance can cause, or to work around lack of support for
multiple inheritance in a language. A mixin can also be viewed as an
interface with implemented methods. This pattern is an example of
enforcing the Dependency Inversion Principle """


log = print
log('Retos para Programadores #30')

# Incorrect Example

class USABillingService1:
    def calculate_charge(self, duration):
        return duration * 0.10  # $0.10 per minute


class CallBillingService1:
    def __init__(self):
        self.billing_service = USABillingService1()  # Direct dependency

    def bill_call(self, duration):
        charge = self.billing_service.calculate_charge(duration)
        log(f"Total charge: {charge:.2f}")


# Example usage
call_billing_service1 = CallBillingService1()
call_billing_service1.bill_call(22)  # Total charge: 2.20

# Correct Example

class IBillingService:
    def calculate_charge(self, duration):
        raise NotImplementedError("Method 'calculate_charge()' must be implemented for this Billing Service.")


class USABillingService(IBillingService):
    def __init__(self):
        super().__init__()
        self.location = 'USA'

    def calculate_charge(self, duration):
        return duration * 0.10


class EuropeBillingService(IBillingService):
    def __init__(self):
        super().__init__()
        self.location = 'Europe'

    def calculate_charge(self, duration):
        return duration * 0.15


class AsiaBillingService(IBillingService):
    def __init__(self):
        super().__init__()
        self.location = 'Asia'

    def calculate_charge(self, duration):
        return duration * 0.05


class CallBillingService:
    def __init__(self, billing_service):
        self.billing_service = billing_service  # Dependency injection

    def bill_call(self, duration):
        charge = self.billing_service.calculate_charge(duration)
        log(f"Total charge for {self.billing_service.location}: {charge:.2f}")


# Example usage for billing services
usa_billing_service = USABillingService()
europe_billing_service = EuropeBillingService()
asia_billing_service = AsiaBillingService()

call_billing_service_usa = CallBillingService(usa_billing_service)
call_billing_service_europe = CallBillingService(europe_billing_service)
call_billing_service_asia = CallBillingService(asia_billing_service)

call_billing_service_usa.bill_call(127.22)  # Total charge for USA: 12.72
call_billing_service_europe.bill_call(17.56)  # Total charge for Europe: 2.63
call_billing_service_asia.bill_call(45.23)  # Total charge for Asia: 2.26


# Extra Difficulty Exercise
class INotificationService:
    def send(self, message):
        raise NotImplementedError("Method 'send()' must be implemented in this specific Notification Service.")


class EmailService(INotificationService):
    def send(self, message):
        log(f"Sending email: {message}")


class SMSService(INotificationService):
    def send(self, message):
        log(f"Sending SMS: {message}")


class PushService(INotificationService):
    def send(self, message):
        log(f"Sending PUSH notification: {message}")


class NotificationSystem:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def notify(self, message):
        self.notification_service.send(message)


# Example usage for notification services
email_service = EmailService()
sms_service = SMSService()
push_service = PushService()

notification_system_email = NotificationSystem(email_service)
notification_system_sms = NotificationSystem(sms_service)
notification_system_push = NotificationSystem(push_service)

notification_system_email.notify("Testing sending a message via Email.")  # Sending email: Testing sending a message via Email.
notification_system_sms.notify("Testing sending a message via SMS.")  # Sending SMS: Testing sending a message via SMS.
notification_system_push.notify("Testing sending a message via PUSH.")  # Sending PUSH notification: Testing sending a message via PUSH.
