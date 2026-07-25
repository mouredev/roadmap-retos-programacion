#27 { Retos para Programadores } Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP) 

# Bibliography reference:
# https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
  
 """


""" In object-oriented programming, the open–closed principle (OCP) states "software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification";[1] that is, such an entity can allow its behaviour to be extended without modifying its source code.

The name open–closed principle has been used in two ways. Both ways use generalizations (for instance, inheritance or delegate functions) to resolve the apparent dilemma, but the goals, techniques, and results are different. """

# Not using Open-Close Principle (OCP)

class SimpleCalculator:
    def calculate(self, operation, a, b):
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError("Operation not supported")

# Example usage
calculator1 = SimpleCalculator()
print(calculator1.calculate('add', 856, 30))  # 886
print(calculator1.calculate('divide', 220, 4423))  # 0.04973999547818223

# Using Open-Close Principle (OCP)

import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

log.info('Retos para Programadores #27')  # Retos para Programadores #27

# Base class for operations
class Operation:
    def execute(self, a: float, b: float) -> float:
        raise NotImplementedError("Method not implemented")

# Concrete operation classes
class Addition(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtraction(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b

class Multiplication(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b

class Division(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class Power(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b

# Calculator class that uses the operations
class Calculator:
    def __init__(self):
        self.operations = {}

    def add_operation(self, name: str, operation: Operation):
        self.operations[name] = operation
        log.info(f"Added operation: [ {name} ]")

    def calculate(self, operation_name: str, a: float, b: float) -> float:
        operation = self.operations.get(operation_name)
        if not operation:
            raise ValueError(f"Operation '{operation_name}' not supported")
        return operation.execute(a, b)

def setup_calculator() -> Calculator:
    calculator = Calculator()
    calculator.add_operation('add', Addition())
    calculator.add_operation('subtract', Subtraction())
    calculator.add_operation('multiply', Multiplication())
    calculator.add_operation('divide', Division())
    calculator.add_operation('power', Power())
    return calculator

def add_custom_operation(calculator: Calculator):
    name = input("Enter operation name: ")
    action = input("Enter operation action (use 'a' and 'b' for inputs, e.g., a + b): ")
    sign = input("Enter operation sign: ")

    if not name or not action or not sign:
        log.warning("You have to fill all the fields: name, operation, and sign to add a new operation!")
        return

    # Create a new operation class for the custom operation
    class CustomOperation(Operation):
        def __init__(self, action: str):
            self.action = action

        def execute(self, a: float, b: float) -> float:
            try:
                # Replace 'a' and 'b' in the action string with the actual values
                expression = self.action.replace('a', str(a)).replace('b', str(b))
                return eval(expression)
            except Exception as e:
                log.error(f"Error in operation: {e}")
                return None

    # Add the new operation to the calculator
    calculator.add_operation(name, CustomOperation(action))
    log.info(f"Custom operation '{name}' added successfully!")

def get_float_input(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            log.error("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    calculator = setup_calculator()

    # Example calculations
    try:
        result_add = calculator.calculate('add', 856, 30)
        log.info(f"Result of addition: {result_add}")  # 886

        result_divide = calculator.calculate('divide', 220, 4423)
        log.info(f"Result of division: {result_divide}")  # 0.04973999547818223
    except ValueError as e:
        log.error(e)

    # Adding a custom operation
    add_custom_operation(calculator)

    # Example of using the custom operation
    custom_operation_name = input("Enter the name of the custom operation to use: ")
    a = get_float_input("Enter first number: ")
    b = get_float_input("Enter second number: ")

    try:
        result_custom = calculator.calculate(custom_operation_name, a, b)
        log.info(f"Result of custom operation '{custom_operation_name}': {result_custom}")
    except ValueError as e:
        log.error(e)

# Output:
"""  
INFO:__main__:Retos para Programadores #27
INFO:__main__:Added operation: [ add ]
INFO:__main__:Added operation: [ subtract ]
INFO:__main__:Added operation: [ multiply ]
INFO:__main__:Added operation: [ divide ]
INFO:__main__:Added operation: [ power ]
INFO:__main__:Result of addition: 886
INFO:__main__:Result of division: 0.04973999547818223
Enter operation name: add4
Enter operation action (use 'a' and 'b' for inputs, e.g., a + b): a + 4 + b
Enter operation sign: +4+
INFO:__main__:Added operation: [ add4 ]
INFO:__main__:Custom operation 'add4' added successfully!
Enter the name of the custom operation to use: add4
Enter first number: 12
Enter second number: 4
INFO:__main__:Result of custom operation 'add4': 20.0

"""