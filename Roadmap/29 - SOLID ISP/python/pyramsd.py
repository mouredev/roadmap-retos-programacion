## USO CORRECTO
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def imprime(self, documento): print(f"Documento {documento} impreso")

class Escaner(ABC):
    @abstractmethod
    def escanear(self, documento): print(f"Documento {documento} escaneado")

class Fax(ABC):
    @abstractmethod
    def fax(self, documento): print(f"Documento {documento} faxeado?")


class BasicPrinter(Printer):
    def imprime(self, document):
        return super().imprime(document)

class BasicScanner(Escaner):
    def escanear(self, document):
        return super().escanear(document)
    
class BasicFax(Fax):
    def fax(self, document):
        return super().fax(document)
    
class MultiFunctionalMachine(Printer, Escaner, Fax):
    def imprime(self, documento):
        return super().imprime(documento)
    
    def escanear(self, documento):
        return super().escanear(documento)
    
    def fax(self, documento):
        return super().fax(documento)

impresora_basica = BasicPrinter()
impresora_basica.imprime("secret.txt")

escaner_basica = BasicScanner()
escaner_basica.escanear("secret.txt")

fax_basica = BasicFax()
fax_basica.fax("secret.txt")

maquina_multifuncional = MultiFunctionalMachine()
maquina_multifuncional.imprime("response.txt")
maquina_multifuncional.escanear("response.txt")
maquina_multifuncional.fax("response.txt")


# USO INCORRECTO
from abc import ABC, abstractmethod

class Machine(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

# Implementación de una impresora básica que no necesita escanear ni enviar faxes
class ImpresoraBasica(Machine):
    def print(self, document):
        print(f"Printing document: {document}")

    def scan(self, document):
        print("Esta impresora no escanea")

    def fax(self, document):
        print("Esta impresora no faxea?")

basic_printer = ImpresoraBasica()
basic_printer.print("My report")
basic_printer.scan("My report")  # Esto lanzará una excepción


"""
EXTRA
"""
class ImpresoraBW(ABC):
    @abstractmethod
    def imprimeBW(self, documento):
        print(f"Esta impresora imprime solo a blanco y negro el documento {documento}")

class ImpresoraRGB(ABC):
    @abstractmethod
    def imprimeRGB(self, documento):
        print(f"Esta impresora imprime a color el documento {documento}")

class Escaner(ABC):
    @abstractmethod
    def escanear(self, documento): print(f"Documento {documento} escaneado")

class Fax(ABC):
    @abstractmethod
    def fax(self, documento): print(f"Documento {documento} faxeado?")

class Impresora2Colors(ImpresoraBW):
    def imprimeBW(self, documento):
        return super().imprimeBW(documento)

class ImpresoraAllColors(ImpresoraRGB):
    def imprimeRGB(self, documento):
        return super().imprimeRGB(documento)

class AllInOneMachine(ImpresoraBW, ImpresoraRGB, Escaner, Fax):
    def imprimeBW(self, documento):
        return super().imprimeBW(documento)
    
    def imprimeRGB(self, documento):
        return super().imprimeRGB(documento)
    
    def escanear(self, documento):
        return super().escanear(documento)
    
    def fax(self, documento):
        return super().fax(documento)
    

impresoraBW = Impresora2Colors()
impresoraRGB = ImpresoraAllColors()
maquinaAllInOne = AllInOneMachine()

impresoraBW.imprimeBW("passwords.txt")
impresoraRGB.imprimeRGB("images")
maquinaAllInOne.imprimeBW("response.txt")
maquinaAllInOne.imprimeRGB("response.txt")
maquinaAllInOne.escanear("Images")
maquinaAllInOne.fax("text.txt")
