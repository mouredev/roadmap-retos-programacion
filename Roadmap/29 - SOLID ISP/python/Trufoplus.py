###############################################################################
### EJERCICIO: ISP
###############################################################################

### SIN APLICAR ISP ###
class Calculator:
    """
    Una calculadora que suma, resta, multiplica y divide.
    """
    def sum(self, a, b):
        pass
    
    def subtract(self, a, b):
        pass
    
    def multiply(self, a, b):
        pass
    
    def divide(self, a, b):
        pass

# Si queremos crear una calculadora que solo sume y reste no podemos,
# estamos obligados a implementar todos los métodos en nuestro objeto.
my_simple_calculator = Calculator()


### APLICANDO ISP ###
# Separamos los métodos en diferentes clases, para poder crear nuestra calculadora simple.
class Sum:
    def sum(self, a, b):
        return a + b


class Subtract: 
    def subtract(self, a, b):
        return a - b


class Multiply:     
    def multiply(self, a, b):
        return a * b
 
 
class Divide:    
    def divide(self, a, b):
        return a / b


# Ahora sí podemos crear una calculadora que solo sume y reste
class SimpleCalculator(Sum, Subtract):
    pass


# Ejemplo de uso
my_simple_calculator = SimpleCalculator()
print(my_simple_calculator.sum(2, 2))       
print(my_simple_calculator.subtract(2, 2))




###############################################################################
### DIFICULTAD EXTRA
###############################################################################

# Aplicamos una clase para cada funcion que puede realizar nuestra impresora 
class Printer:
    def print(self, file):
        return f"Printing {file}..."


class Scanner:
    def scan(self, file):
        return f"Scaning {file}..."


class Fax:
    def send_fax(self, file, address):
        return f"Sendinf {file} to {address}"
    

# Creamos nuestras impresoras personalizadas 
class BlanckWhitePrinter(Printer):
    def print(self, file):
        return f"Printing {file} in black and white"
    def __str__(self) -> str:
        return "A black and White printer"


class ColorPrinter(Printer):
    def print(self, file):
        return f"Printinf {file} in color"
    
    def __str__(self) -> str:
        return "A color printer"


class MultifunctionDevice(Printer, Scanner, Fax):
    def __str__(self) -> str:
        return "A Multifunction device"



# Creamos los objetos y empleamos los metodos.
my_printers = [BlanckWhitePrinter(), ColorPrinter(), MultifunctionDevice()]

for printer in my_printers:
    print() # Un espacio en blanco para mejorar la visualizacion
    print(printer)
    print(printer.print("documento.txt"))
    
    if isinstance(printer, Fax):
        print(printer.send_fax("documento.txt", "moure@gmail.com"))
    else:
        print("This print doesn't send fax")
    
    if isinstance(printer, Scanner):
        print(printer.scan("documento.txt"))
    else:
        print("This printer doesn't scan")
    print() 
    

