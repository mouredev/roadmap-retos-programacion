#29 { Retos para Programadores } Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP) 

# Bibliography reference:
# The Web Development Glossary (Jens Oliver Meiert) (Z-Library)
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
* EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 """

""" Interface Segregation Principle
The principle that no client should be forced to depend on methods it does
not use. ISP splits interfaces that are very large into smaller and more
specific ones so that clients will only have to know about the methods that
are of interest to them. Such shrunken interfaces are also called role
interfaces. ISP is intended to keep a system decoupled and thus easier to
refactor, change, and redeploy.  """


# Shorthan for print
log = print

# Incorrect Example

class PaymentService:
    def process_credit_card_payment(self, amount):
        pass

    def process_paypal_payment(self, amount):
        pass

    def process_bitcoin_payment(self, amount):
        pass


class CreditCardPayment(PaymentService):
    def process_credit_card_payment(self, amount):
        log(f"Processing credit card payment of {amount}")

    def process_paypal_payment(self, amount):
        raise Exception("This payment method does not support PayPal payments")

    def process_bitcoin_payment(self, amount):
        raise Exception("This payment method does not support Bitcoin payments")


class PayPalPayment(PaymentService):
    def process_credit_card_payment(self, amount):
        raise Exception("This payment method does not support credit card payments")

    def process_paypal_payment(self, amount):
        log(f"Processing PayPal payment of {amount}")

    def process_bitcoin_payment(self, amount):
        raise Exception("This payment method does not support Bitcoin payments")


class BitcoinPayment(PaymentService):
    def process_credit_card_payment(self, amount):
        raise Exception("This payment method does not support credit card payments")

    def process_paypal_payment(self, amount):
        raise Exception("This payment method does not support PayPal payments")

    def process_bitcoin_payment(self, amount):
        log(f"Processing Bitcoin payment of {amount}")


# Example usage
credit_card_payment = CreditCardPayment()
credit_card_payment.process_credit_card_payment(250)  # Processing credit card payment of 250
# credit_card_payment.process_paypal_payment(87)  # This will raise an exception
# Exception: This payment method does not support PayPal payments

# Correct Example

class CreditCardPaymentService:
    def process_credit_card_payment(self, amount):
        print(f"Processing credit card payment of {amount}")


class PayPalPaymentService:
    def process_paypal_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")


class BitcoinPaymentService:
    def process_bitcoin_payment(self, amount):
        print(f"Processing Bitcoin payment of {amount}")


# Example usage
credit_card_payment1 = CreditCardPaymentService()
credit_card_payment1.process_credit_card_payment(400)  # Processing credit card payment of 400

pay_pal_payment = PayPalPaymentService()
pay_pal_payment.process_paypal_payment(130)  # Processing PayPal payment of 130

bitcoin_payment = BitcoinPaymentService()
bitcoin_payment.process_bitcoin_payment(0.020)  # Processing Bitcoin payment of 0.02


# Extra Difficulty Exercise

class BlackAndWhitePrinter:
    def print(self, doc):
        print(f"Printing: {doc} in Black & White")


class ColorPrinter:
    def print(self, doc):
        print(f"Printing: {doc} in Color")


class MultiFunctionPrinter:
    def print_in_black_and_white(self, doc):
        print(f"Printing: {doc} in Black & White")

    def print(self, doc):
        print(f"Printing: {doc} in Color")

    def fax(self, doc):
        print(f"Faxing: {doc}")

    def scan(self, doc):
        print(f"Scanning: {doc}")


# Example usage for printers
book = 'vuelointemporal.odt'

bw_printer = BlackAndWhitePrinter()
bw_printer.print(book)  # Printing: vuelointemporal.odt in Black & White

c_printer = ColorPrinter()
c_printer.print(book)  # Printing: vuelointemporal.odt in Color

m_printer = MultiFunctionPrinter()
m_printer.print_in_black_and_white(book)  # Printing: vuelointemporal.odt in Black & White
m_printer.print(book)  # Printing: vuelointemporal.odt in Color
m_printer.fax(book)  # Faxing: vuelointemporal.odt
m_printer.scan(book)  # Scanning: vuelointemporal.odt
