### Python Inheritance ###

class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
class Dog(Animal):
  def __init__(self, name, age):
    super().__init__(name, age)
    
  def sound(self):
    return f'My dog {self.name} does guauuu'
    
class Cat(Animal):
  def __init__(self, name, age):
    super().__init__(name, age)
    
  def sound(self):
    return f'My cat {self.name} does meoww'
    
my_dog = Dog('pucho', 13)
my_cat = Cat('steve', 8)

print(my_dog.sound())
print(my_cat.sound())

#! Optional Challenge

class Employee:
  def __init__(self, id, name):
    self.id = id
    self.name = name

class Manager(Employee):
  def __init__(self, id, name):
    super().__init__(id, name)
    self.role = 'Manager'
    
class ProjectManager(Employee):
  def __init__(self, id, name):
    super().__init__(id, name)
    self.role = 'Project Manager'
    
class Programmer(Employee):
  def __init__(self, id, name):
    super().__init__(id, name)
    self.role = 'Programmer'

