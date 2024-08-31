from abc import ABC, abstractmethod

#Uso incorrecto
class Aveh(ABC):
    @abstractmethod
    def walk(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass

class Bird_(Aveh):
    def walk(self):
        return "El pájaro está caminando"
    
    def fly():
        return "El pájaro está volando"

class Penguin_(Aveh):
    def walk(self):
        return "El pingüino está caminando"
    
    def fly(self):
        return "El pingüino está volando"

bird_ = Bird_()
print(bird_.walk())

'''
Es incorrecto porque los pingünos no vuelan. Para que se de este principio tienen que venir de una clase
con métodos generales y cada subclase sus métodos específicos
'''

#Uso correcto
class Ave(ABC):
    @abstractmethod
    def walk(self):
        pass

class Bird(Ave):
    def walk(self):
        return "El pájaro está caminando"
    
    def fly(self):
        return "El pájaro está volando"

class Penguin(Ave):
    def walk(self):
        return "El pingüino está caminando"
    
    def swim(self):
        return "El pingüino está nadando"

bird = Bird()
print(bird.fly())
penguin = Penguin()
print(penguin.swim())

print("\n", "*"*7, "EJERCICIO EXTRA", "*"*7)
class Printer(ABC):
    @abstractmethod
    def printing(self, doc):
        return f"Imprimiendo {doc}"

class Printer_Functions(Printer):
    @abstractmethod
    def scan(self, doc):
        return f"Escaneando \"{doc}\""
    
    @abstractmethod
    def send_fax(self, doc, fax):
        return f"Enviando \"{doc}\" al {fax}"
    

class ByW_Printer(Printer):
    def printing(self, doc):
        return f"Imprimiendo en blanco y negro: {doc}"

class Color_Printer(Printer):
    def printing(self, doc):
        return f"Imprimiendo a color: {doc}"

class Multi_Printer(Printer_Functions):
    def printing(self, doc):
        return f"Imprimiendo a color: {doc}"
    
    def scan(self, doc):
        return super().scan(doc)
    
    def send_fax(self, doc, fax):
        return super().send_fax(doc, fax)

byn = ByW_Printer()
print(byn.printing("El Quijote"))

color = Color_Printer()
print(color.printing("Batman Begins"))

printer = Multi_Printer()
print(printer.send_fax("Trabajo Final", 254789630))
