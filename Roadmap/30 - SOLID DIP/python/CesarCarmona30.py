'''
  EJERCICIO
'''

# Sin DIP

class Keyboard:
  def get_input(self):
    return "User input from keyboard"
  
class Computer:
  def __init__(self) -> None:
    self.keyboard = Keyboard()

  def collect_input(self):
    return self.keyboard.get_input()
  
# computer = Computer()
# print(computer.collect_input())

# Con DIP

from abc import ABC, abstractmethod

class InputDevice(ABC):
  @abstractmethod
  def get_input(self):
    pass

class Keyboard(InputDevice):
  def get_input(self):
    return "User input from keyboard"
  
class Computer:
  def __init__(self, input_device: InputDevice):
    self.input_device = input_device

  def collect_input(self):
    return self.input_device.get_input()
  
keyboard = Keyboard()
computer = Computer(keyboard)
print(computer.collect_input())

class Mouse(InputDevice):
  def get_input(self):
    return "User input from mouse"

mouse = Mouse()
computer = Computer(mouse)
print(computer.collect_input())

'''
  EXTRA
'''

class Notifier(ABC):
  @abstractmethod
  def notify(self, to, message):
    pass

class EmailService(Notifier):
  def notify(self, to, message):
    print("Sending email to {to}: {message}")
  
class SMSService(Notifier):
  def notify(self, to, message):
    print(f"Sending SMS to {to}: {message}")
  
class PUSHService(Notifier):
  def notify(self, to, message):
    print(f"Sending PUSH to {to}: {message}")

class Notification:
  def __init__(self, notifier: Notifier):
    self.notifier = notifier

  def send_notification(self, user, message):
    self.notifier.notify(user, message)


def test_services():
  email_service = EmailService()
  sms_service = SMSService()
  push_service = PUSHService()

  notification = Notification(email_service)
  notification.send_notification("pedro@gmail.com", "Hola. ¿Cómo estás?")
  notification = Notification(sms_service)
  notification.send_notification("5555555555", "Hola, espero te encuentres bien.")
  notification = Notification(push_service)
  notification.send_notification("Leroy", "Hola amigo")

test_services()