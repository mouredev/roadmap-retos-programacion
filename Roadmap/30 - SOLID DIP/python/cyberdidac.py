from abc import ABC, abstractmethod


class MessageService(ABC):
    @abstractmethod
    def send_message(self, message: str):
        pass


class EmailService(MessageService):
    def send_message(self, message: str):
        print(f"Enviando email con mesnaje:\n"
              f"> {message}")


class SMSService(MessageService):
    def send_message(self, message: str):
        print(f"Enviando SMS con mensaje:\n"
              f"> {message}")


class PUSHService(MessageService):
    def send_message(self, message: str):
        print("Enviando PUSH con mensaje:\n"
              f"> {message}")


class Notification:
    message_service: MessageService

    def __init__(self, message_service: MessageService):
        self.message_service = message_service

    def send(self, message: str):
        self.message_service.send_message(message)


def main():
    email_service = EmailService()
    sms_service = SMSService()
    push_service = PUSHService()

    notification_email = Notification(email_service)
    notification_sms = Notification(sms_service)
    notification_push = Notification(push_service)

    notification_email.send("Hola desde el EmailService!")
    notification_sms.send("Hola desde el SMSService!")
    notification_push.send("Hola desde el PUSHService!")


if __name__ == '__main__':
    main()
