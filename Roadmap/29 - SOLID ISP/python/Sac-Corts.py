from abc import ABC, abstractmethod

# Incorrecto
class Vehicle:
    def drive(self):
        raise NotImplementedError

    def play_music(self):
        raise NotImplementedError

    def open_trunk(self):
        raise NotImplementedError

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

    def play_music(self):
        print("Playing music in the car")

    def open_trunk(self):
        print("Opening the car trunk")

class Bicycle(Vehicle):
    def drive(self):
        print("Riding a bicycle")

    def play_music(self):
        pass

    def open_trunk(self):
        pass

# Correcto
class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass

class MusicPlayable(ABC):
    @abstractmethod
    def play_music(self):
        pass

class TrunkOpenable(ABC):
    @abstractmethod
    def open_trunk(self):
        pass

class Car(Drivable, MusicPlayable, TrunkOpenable):
    def drive(self):
        print("Driving a car")

    def play_music(self):
        print("Playing music in the car")

    def open_trunk(self):
        print("Opening the car trunk")

class Bicycle(Drivable):
    def drive(self):
        print("Riding a bicycle")


car = Car()
car.drive()
car.play_music()
car.open_trunk()

bicycle = Bicycle()
bicycle.drive()

### Ejercicio Extra ###
class Printer(ABC):
    @abstractmethod
    def print(self, content: str):
        pass

class ColorPrinter(ABC):
    @abstractmethod
    def print_color(self, content: str):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, content: str):
        pass

class Fax(ABC):
    @abstractmethod
    def send_fax(self, content: str):
        pass

class BlackAndWhitePrinter(Printer):
    def print(self, content: str):
        print(f"Printing in black and white: {content}")

class ColorPrinterOnly(ColorPrinter):
    def print_color(self, content: str):
        print(f"Printing in color: {content}")

class MultifunctionPrinter(Printer, ColorPrinter, Scanner, Fax):
    def print(self, content: str):
        print(f"Printing in black and white: {content}")

    def print_color(self, content: str):
        print(f"Printing in color: {content}")

    def scan(self, content: str):
        print(f"Scanning: {content}")

    def send_fax(self, content: str):
        print(f"Sending fax: {content}")


bw_printer = BlackAndWhitePrinter()
bw_printer.print("Thesis")

color_printer = ColorPrinterOnly()
color_printer.print_color("Images")

multifunction_printer = MultifunctionPrinter()
multifunction_printer.print("Thesis")
multifunction_printer.print_color("Images")
multifunction_printer.scan("Credential")
multifunction_printer.send_fax("Report")
