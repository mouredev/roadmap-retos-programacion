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

# Forma Incorrecta de aplicar el OCP(Open Close Principle)

class Order:

    items= []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Procesando el tipo de pago 'débito'")
        print(f"Verificando codigo de seguridad: {security_code}")
        order.status = "paid"
    def pay_credit(self, order, security_code):
        print("Procesando el tipo de pago 'credito'")
        print(f"Verificando codigo de seguridad: {security_code}")
        order.status = "paid"
    def pay_paypal(self, order, security_code):
        print("Procesando el tipo de pago 'Paypal'")
        print(f"Verificando codigo de seguridad: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "0372846")

# Forma correcta de aplicar el principio (OCP)

from abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.items= []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
class PaymentProcessor(ABC):
    @abstractmethod
    def pay (self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Procesando el tipo de pago 'débito'")
        print(f"Verificando codigo de seguridad: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Procesando el tipo de pago 'credito'")
        print(f"Verificando codigo de seguridad: {security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Procesando el tipo de pago 'Paypal'")
        print(f"Verificando codigo de seguridad: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(f"El precio total es: {order.total_price()}")
processor = PaypalPaymentProcessor()
processor.pay(order, "0372846")
print(f"Estatus: {order.status}")


########### ---------------------------------- EXTRA ------------------------------------------ #############

from abc import ABC, abstractmethod

class Calculator:
    
    def __init__(self):
        self.operations = {
            "suma": SumaOperation(),
            "resta": RestaOperation(),
            "multiplicacion": MultiOperation(),
            "division": DivisionOperation()
        }

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def get_operation(self, name):
        return self.operations.get(name)
    
    def execute(self, name, num1, num2):
        operation = self.get_operation(name)
        if operation:
            return operation.calculate(num1, num2)
        else:
            raise ValueError(f"Operacion '{name}' no soportada.")

class Operation(ABC):
    @abstractmethod
    def calculate(self, num1, num2):
        pass

class SumaOperation(Operation):
    def calculate(self, num1, num2):
        return num1 + num2
    
class RestaOperation(Operation):
    def calculate(self, num1, num2):
        return num1 - num2
    
class MultiOperation(Operation):
    def calculate(self, num1, num2):
        return num1 * num2
    
class DivisionOperation(Operation):
    def calculate(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    
class PoteciaOperation(Operation):
    def calculate(self, num1, num2):
        return num1 ** num2
    

calculator = Calculator()
calculator.add_operation("potencia", PoteciaOperation())

print(f"Suma: {calculator.execute('suma', 4, 3)}")
print(f"Resta: {calculator.execute('resta', 10, 5)}")
print(f"Multiplicación: {calculator.execute('multiplicacion', 7, 6)}")
print(f"División: {calculator.execute('division', 8, 2)}")
print(f"Potencia: {calculator.execute('potencia', 2, 3)}")

try:
    print(f"Mod: {calculator.execute('mod', 10, 3)}")
except ValueError as e:
    print(e)



