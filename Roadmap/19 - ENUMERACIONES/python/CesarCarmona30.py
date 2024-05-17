from enum import Enum

class Weekday(Enum):
  MONDAY = 1
  TUESDAY = 2
  WEDNESDAY = 3
  THURSDAY = 4
  FRIDAY = 5
  SATURDAY = 6
  SUNDAY = 7

def name_day(number):
  try:
    return Weekday(number).name.capitalize()
  except ValueError:
    return "Invalid day"
  
'''
  EXTRA
'''

class Status(Enum):
  PENDING = 1
  SHIPPED = 2
  DELIVERED = 3
  CANCELED = 4

class Order:
  def __init__(self, identifier):
    self._identifier = identifier
    self._status = Status.PENDING

  def send(self):
    if self._status == Status.PENDING:
      self._status = Status.SHIPPED
      print(f'{self._identifier} shipped')
    else:
      print('Shipped invalid operation')

  def canceled(self):
    if self._status == Status.PENDING:
      self._status = Status.CANCELED
      print(f'{self._identifier} canceled')
    else:
      print('Canceled invalid operation')

  def delivered(self):
    if self._status == Status.SHIPPED:
      self._status = Status.DELIVERED
      print(f'{self._identifier} delivered')
    else:
      print('Delivered invalid operation')

  def show_details(self):
    print(f'{self._identifier}: {self._status.name}')


print(name_day(3))
print(name_day(6))
print(name_day(9))


product1 = Order('Keyboard')
product2 = Order('Sweater')

product1.show_details()
product1.send()
product1.show_details()
product1.delivered()
product1.show_details()
product1.canceled()
product1.show_details()

product2.show_details()
product2.canceled()
product2.show_details()
product2.delivered()
product2.show_details()