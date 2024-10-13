
from abc import ABC, abstractmethod
#Bad example: Open for mofification but not closed
class Character:
    def __init__(self,type):
        self.type = type
    def attack(self):
        if self.type == "Fire":
            print("Fire attack")
        elif self.type == "Water":
            print("Water attack")
        elif self.type == "Electricity":
            print("Electrical attack")

#Correct example

class Character2(ABC):
    def __init__(self,type):
        self.type = type
    @abstractmethod
    def attack(self):
        pass

class FireCharacter(Character2):
    def attack(self):
        print("Fire attack")

class WaterCharacter(Character2):
    def attack(self):
        print("Water attack")

class ElectricityCharacter(Character2):
    def attack(self):
        print("Electrical attack")

#Extra

class Operation(ABC):
    @abstractmethod
    def operate(self,a,b):
        pass

class Sum(Operation):
    def operate(self, a, b):
        return a +b
class Diff(Operation):
    def operate(self, a, b):
        return a - b
class Multiply(Operation):
    def operate(self, a, b):
        return a*b
class Division(Operation):
    def operate(self, a, b):
        if not b==0:
            return a/b

class Calculator:
    def __init__(self) -> None:
        self.operations = []

    def add_operation(self,name,op):
        self.operations.append((name,op))
    def operate(self,operation,a,b):
        element = list(filter(lambda x: x[0]==operation,self.operations))
        if element:
            return element[0][1].operate(a,b)    
calc = Calculator()
calc.add_operation("Sum",Sum())
calc.add_operation("Diff",Diff())
calc.add_operation("Multiply",Multiply())
calc.add_operation("Division",Division())
print("Sum",calc.operate("Sum",3,5))
print("Diff",calc.operate("Diff",4,3))
print("Multiply",calc.operate("Multiply",4,3))
print("Division",calc.operate("Division",4,2))

class Pow(Operation):
    def operate(self, a, b):
        return a**b

calc.add_operation("Pow",Pow())
print("Pow",calc.operate("Pow",2,2))    