from abc import ABC, abstractmethod


class BWPrinter(ABC):
    @abstractmethod
    def print_BW(self, file):
        pass


class ColorPrinter(ABC):
    @abstractmethod
    def print_color(self, file):
        pass


class Scanner(ABC):
    @abstractmethod
    def scann(self, file):
        pass


class Fax(ABC):
    @abstractmethod
    def send(self, file):
        pass


class PrinterBW(BWPrinter):
    def print_BW(self, file):
        print(f"Imprimiendo {file} en blanco y negro")


class PrinterColor(ColorPrinter):
    def print_color(self, file):
        print(f"Imprimiendo {file} en color")


class Multiprinter(BWPrinter, ColorPrinter, Scanner, Fax):
    def print_BW(self, file):
        print(f"Imprimiendo {file} en blanco y negro")

    def print_color(self, file):
        print(f"Imprimiendo {file} en color")

    def scann(self, file):
        print(f"Escaneando {file}")

    def send(self, file):
        print(f"Enviando {file}")


def main():
    bw_printer = PrinterBW()
    color_printer = PrinterColor()
    multiprinter = Multiprinter()

    bw_printer.print_BW("CV")
    color_printer.print_color("CV")
    multiprinter.print_BW("CV")
    multiprinter.print_color("CV")
    multiprinter.scann("CV")
    multiprinter.send("CV")


if __name__ == '__main__':
    main()
