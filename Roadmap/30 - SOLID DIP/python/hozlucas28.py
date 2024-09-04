# pylint: disable=pointless-string-statement,missing-function-docstring,missing-class-docstring,too-few-public-methods,line-too-long

from abc import ABCMeta, abstractmethod
from multiprocessing.util import abstract_sockets_supported

"""
    Dependency Inversion Principle (DIP)...
"""

print("Dependency Inversion Principle (DIP)...")

print("\nBad implementation of Dependency Inversion Principle (DIP)...")


class AbcEmailService(metaclass=ABCMeta):
    @abstractmethod
    def send(self, content: str) -> None:
        pass


class EmailService(AbcEmailService):
    def send(self, content: str) -> None:
        print("Email with {content=} sent!")


class AbcBadNotificationService(metaclass=ABCMeta):
    @abstractmethod
    def send_email(self, content: str) -> None:
        pass


class BadNotificationService(AbcBadNotificationService):
    email_service: EmailService

    def __init__(self) -> None:
        self.email_service = EmailService()

    def send_email(self, content: str) -> None:
        self.email_service.send(content=content)


print(
    "\n```",
    """class AbcEmailService(metaclass=ABCMeta):
    @abstractmethod
    def send(self, content: str) -> None:
        pass


class EmailService(AbcEmailService):
    def send(self, content: str) -> None:
        print("Email with {content=} sent!")


class AbcBadNotificationService(metaclass=ABCMeta):
    @abstractmethod
    def send_email(self, content: str) -> None:
        pass


class BadNotificationService(AbcBadNotificationService):
    email_service: EmailService

    def __init__(self) -> None:
        self.email_service = EmailService()

    def send_email(self, content: str) -> None:
        self.email_service.send(content=content)""",
    "```",
    sep="\n",
)

print(
    "\nThis is a bad implementation of Dependency Inversion Principle (DIP),",
    "'BadNotificationService' class depends directly on the 'EmailService' class \n",
    "rather than on an abstract class. So, if the 'email_service attribute in the'\n",
    "'BadNotificationService' class needs to be changed, the constructor must also be\n",
    "modified.",
    sep="\n",
)

print("\nGood implementation of Dependency Inversion Principle (DIP)...")


class GmailService(AbcEmailService):
    def send(self, content: str) -> None:
        print(f"Email with {content=} sent!")


class YahooService(AbcEmailService):
    def send(self, content: str) -> None:
        print(f"Email with {content=} sent!")


class AbcGoodNotificationService(metaclass=ABCMeta):
    @abstractmethod
    def send_email(self, content: str) -> None:
        pass


class GoodNotificationService(AbcGoodNotificationService):
    email_service: AbcEmailService

    def __init__(self, email_service: AbcEmailService) -> None:
        self.email_service = email_service

    def send_email(self, content: str) -> None:
        self.email_service.send(content=content)


print(
    "\n```",
    """class GmailService(AbcEmailService):
    def send(self, content: str) -> None:
        print(f"Email with {content=} sent!")


class YahooService(AbcEmailService):
    def send(self, content: str) -> None:
        print(f"Email with {content=} sent!")


class AbcGoodNotificationService(metaclass=ABCMeta):
    @abstractmethod
    def send_email(self, content: str) -> None:
        pass


class GoodNotificationService(AbcGoodNotificationService):
    email_service: AbcEmailService

    def __init__(self, email_service: AbcEmailService) -> None:
        self.email_service = email_service

    def send_email(self, content: str) -> None:
        self.email_service.send(content=content)""",
    "```",
    sep="\n",
)

print(
    "\nThis is a good implementation of Dependency Inversion Principle (DIP),",
    "because 'GoodNotificationService' class depends solely on injected dependencies",
    "that implement the 'AbcEmailService' abstract class. So, if the 'email_service' attribute",
    "in the 'GoodNotificationService' class needs to be changed, the constructor does not require",
    "modification (only the class call needs to be updated). For example, I could inject inside the",
    "'email_service' attribute an instance of 'GmailService' or 'YahooService' classes.",
    sep="\n",
)

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")


class AbcNotificationService(metaclass=ABCMeta):
    @abstractmethod
    def send(self) -> None:
        pass


class EmailService_(AbcNotificationService):
    def __init__(self) -> None:
        pass

    def send(self) -> None:
        print("Email sent!")


class PushService(AbcNotificationService):
    def __init__(self) -> None:
        pass

    def send(self) -> None:
        print("Push sent!")


class SMSService(AbcNotificationService):
    def __init__(self) -> None:
        pass

    def send(self) -> None:
        print("SMS sent!")


class AbcNotificationSystem(metaclass=ABCMeta):
    @abstractmethod
    def send_notification(self) -> None:
        pass


class NotificationSystem(AbcNotificationSystem):
    notification_service: AbcNotificationService

    def __init__(self, notification_service: AbcNotificationService) -> None:
        self.notification_service = notification_service

    def send_notification(self) -> None:
        self.notification_service.send()


emailService: EmailService_ = EmailService_()
pushService: PushService = PushService()
smsService: SMSService = SMSService()

emailNotificationSystem: NotificationSystem = NotificationSystem(emailService)
pushNotificationSystem: NotificationSystem = NotificationSystem(pushService)
smsNotificationSystem: NotificationSystem = NotificationSystem(smsService)

print()
emailNotificationSystem.send_notification()

print()
pushNotificationSystem.send_notification()

print()
smsNotificationSystem.send_notification()
