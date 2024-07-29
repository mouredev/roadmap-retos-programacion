"""
EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""
"""
El principio segmentacion de interfaces ISP indica que es mejor tener varias interfaces pequeñas pero especializadas a una unica interfaz gran y general
"""

# Ejemplo incorrecta
class HomeDevice():

    def turn_on(self):
        pass
    def turn_off(self):
        pass
    def set_temperature(self, temperature):
        pass

class light(HomeDevice):

    def turn_on(self):
        print("Light is turned on")
    def turn_off(self):
        print("Light is turned off")
    def set_temperature(self, temperature):
        raise NotImplementedError("Lights do not support temperature setting")

class Heater(HomeDevice):

    def turn_on(self):
        print("Heater is turned on")
    
    def turn_off(self):
        print("Heater is turned off")
    def set_temperature(self, temperature):
        print(f"Setting heater to {temperature} degrees")

light = light()
light.turn_on()
light.turn_off()
#light.set_temperature(30) Esto lanzaría una excepción

heater = Heater()
heater.turn_on()
heater.set_temperature(30)
heater.turn_off()


# Ejemplo correcto

class Switchable():

    def turn_om(self):
        pass
    def turn_off(self):
        pass

class Temperature_control():

    def set_temperature(self,temperature):
        pass

class Light(Switchable):

    def turn_on(self):
        print("Light is turned on")
    def turn_off(self):
        print("Light is turned off")


class Heater(Switchable,Temperature_control):

    def turn_on(self):
        print("Heater is turned on")
    
    def turn_off(self):
        print("Heater is turned off")

    def set_temperature(self, temperature):
        print(f"Setting heater to {temperature} degrees")

light = Light()
light.turn_on()
light.turn_off()

heater = Heater()
heater.turn_on()
heater.set_temperature(22)
heater.turn_off()


"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
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
 */
"""

class PrintDocuments():

    def print_document(self, document):
        pass

class Scannable():

    def scan_document(self):
        pass

class Fax():

    def send_fax(self,document):
        pass

class BlackAndWhite(PrintDocuments):

    def print_document(self, document):
        print("Printing in black and white:", document)

class Color(PrintDocuments):

    def print_document(self, document):
        print("Printing in color:", document)

class MultifunctionPrinter(PrintDocuments, Scannable, Fax):
    def print_document(self, document):
        print("Printing document:", document)

    def scan_document(self):
        print("Scanning document")

    def send_fax(self, document):
        print("Sending fax with document:", document)


def test_printers():
    # Imprimir
    bw_printer = BlackAndWhite()
    bw_printer.print_document("Report")

    color_printer = Color()
    color_printer.print_document("Photo")

    # Multifunción
    multi_printer = MultifunctionPrinter()
    multi_printer.print_document("Manual")
    multi_printer.scan_document()
    multi_printer.send_fax("Invoice")

test_printers()


