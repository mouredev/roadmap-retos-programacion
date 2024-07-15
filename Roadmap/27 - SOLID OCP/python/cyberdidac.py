from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, operand1, operand2):
        pass


class Addition(Operation):
    def execute(self, operand1, operand2):
        return operand1 + operand2


class Substraction(Operation):
    def execute(self, operand1, operand2):
        return operand1 - operand2


class Multiplication(Operation):
    def execute(self, operand1, operand2):
        return operand1 * operand2


class Division(Operation):
    def execute(self, operand1, operand2):
        if operand2 != 0:
            return operand1 / operand2
        else:
            raise ValueError("Cannot divide by zero")


class Power(Operation):
    def execute(self, operand1, operand2):
        return operand1 ** operand2


class Calculator:
    def perform_operation(self, operation, operand1, operand2):
        return operation.execute(operand1, operand2)


def main():
    add = Addition()
    sub = Substraction()
    mult = Multiplication()
    div = Division()
    power = Power()

    calc = Calculator()

    print(calc.perform_operation(add, 1, 2))
    print(calc.perform_operation(sub, 1, 2))
    print(calc.perform_operation(mult, 1, 2))
    print(calc.perform_operation(div, 1, 2))
    print(calc.perform_operation(power, 3, 2))


if __name__ == '__main__':
    main()
