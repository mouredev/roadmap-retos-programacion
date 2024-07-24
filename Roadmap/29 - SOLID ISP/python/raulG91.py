from abc import ABC, abstractmethod

#Incorrect example
class Phone(ABC):
    @abstractmethod
    def call(self):
        pass
    def play_game(self):
        pass
    def install_app(self):
        pass
    def gps_nav(self):
        pass

class OldPhone(Phone):
    def call(self):
        print("Making a call")
    def play_game(self):
        print("Playing snake game")
    def install_app(self):
        raise NotImplementedError("You can not install applications")
    def gps_nav(self):
        raise NotImplementedError("You can not use gps")

class NewPhone(Phone):
    def call(self):
        print("Making a call")
    def play_game(self):
        print("Playing a game")
    def install_app(self):
        print("Intalling application")
    def gps_nav(self):
        print("Using Maps navigation")

nokia = OldPhone()
nokia.call()
try:
    nokia.install_app()
except  Exception as e:
    print(e)    
nokia.play_game()    

iphone5 = NewPhone()
iphone5.play_game()
iphone5.install_app()
iphone5.gps_nav()

#Correct example

class PhoneV2(ABC):
    def call(self):
        pass
    def play_game(self):
        pass

class PhoneApp(ABC):
    @abstractmethod
    def install_app(self):
        pass

class PhoneGPS(ABC):
    def gps_nav(self):
        pass

class OldPhone2(PhoneV2):
    def call(self):
        print("Making a call")
    def play_game(self):
        print("Playing snake game") 

class NewPhone2(PhoneV2,PhoneApp,PhoneGPS):
    def call(self):
        print("Making a call")
    def play_game(self):
        print("Playing a game")
    def install_app(self):
        print("Intalling application")
    def gps_nav(self):
        print("Using Maps navigation")   

iphone15 = NewPhone2()
iphone15.gps_nav()
iphone15.call()

alcatel = OldPhone2()
alcatel.call()

#Extra
print("--Extra--")

class PrinterColor(ABC):
    @abstractmethod
    def printColor(self,text):
        pass
class PrinterBlackWhite(ABC):
    @abstractmethod
    def printBlack(self,text):
        pass    

class Scan(ABC):
    @abstractmethod
    def scan(self):
        pass
class Fax(ABC):
    @abstractmethod
    def send_fax(self):
        pass


class OldPrinter(PrinterBlackWhite):
    def printBlack(self, text):
        print(f'Printing {text} black and white')

class ModernPrinter(PrinterColor):
    def printColor(self, text):
        print(f'Printing {text} in color')

class MultifunctionPrinter(PrinterColor,PrinterBlackWhite,Scan,Fax):
    def printBlack(self, text):
        print(f'Printing {text} black and white from multifunction printer')
    def printColor(self, text):
        print(f'Printing {text} in color from multifunction printer') 
    def scan(self):
        print("Scaning document")
    def send_fax(self):
        print("Sending fax")        

printer1 = OldPrinter()
printer1.printBlack("Some text ")
printer2 = ModernPrinter()
printer2.printColor("Text in color")
printer3 = MultifunctionPrinter()
printer3.printColor("En un lugar de la mancha")
printer3.printBlack("Hey!")
printer3.scan()
printer3.send_fax()