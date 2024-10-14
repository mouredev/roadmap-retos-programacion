# pylint: disable=missing-class-docstring,pointless-string-statement,missing-function-docstring,broad-exception-raised,too-few-public-methods,missing-module-docstring

from abc import ABCMeta, abstractmethod

"""
    Interface Segregation Principle (ISP)...
"""

print("Interface Segregation Principle (ISP)...")


class AbcBadWorker(metaclass=ABCMeta):
    @abstractmethod
    def eat(self) -> None:
        pass

    @abstractmethod
    def work(self) -> None:
        pass


class BadProgrammer(AbcBadWorker):
    def eat(self) -> None:
        print("Eating!")

    def work(self) -> None:
        print("Working!")


class BadRobot(AbcBadWorker):
    def eat(self) -> None:
        raise Exception("A robot can not eat")

    def work(self) -> None:
        print("Working!")


print("\nBad implementation of Interface Segregation Principle (ISP)...")

print(
    "\n```",
    """class AbcBadWorker(metaclass=ABCMeta):
  @abstractmethod
  def eat(self) -> None:
    pass

  @abstractmethod
  def work(self) -> None:
    pass


class BadProgrammer(AbcBadWorker):
  def eat(self) -> None:
    print("Eating!")

  def work(self) -> None:
    print("Working!")


class BadRobot(AbcBadWorker):
  def eat(self) -> None:
    raise Exception("A robot can not eat")

  def work(self) -> None:
    print("Working!")""",
    "```",
    sep="\n",
)

print(
    "\nThis is a bad implementation of Interface Segregation Principle (ISP),",
    "because the 'BadRobot' class should not implement an interface with methods",
    "that it is going to never use. So, the implemented interface ('AbcBadWorker')",
    "is to general for the 'BadRobot' class, but perfect for the 'BadProgrammer' class.",
    sep="\n",
)

print("\nGood implementation of Interface Segregation Principle (ISP)...")


class AbcHumanWorker(metaclass=ABCMeta):
    @abstractmethod
    def eat(self) -> None:
        pass

    @abstractmethod
    def work(self) -> None:
        pass


class AbcNotHumanWorker(metaclass=ABCMeta):
    @abstractmethod
    def work(self) -> None:
        pass


class GoodProgrammer(AbcHumanWorker):
    def eat(self) -> None:
        print("Eating!")

    def work(self) -> None:
        print("Working!")


class GoodRobot(AbcNotHumanWorker):
    def work(self) -> None:
        print("Working!")


print(
    "\n```",
    """class AbcHumanWorker(metaclass=ABCMeta):
  @abstractmethod
  def eat(self) -> None:
    pass

  @abstractmethod
  def work(self) -> None:
    pass


class AbcNotHumanWorker(metaclass=ABCMeta):
  @abstractmethod
  def work(self) -> None:
    pass


class GoodProgrammer(AbcHumanWorker):
  def eat(self) -> None:
    print("Eating!")

  def work(self) -> None:
    print("Working!")


class GoodRobot(AbcNotHumanWorker):
  def work(self) -> None:
    print("Working!")""",
    "```",
    sep="\n",
)

print(
    "\nThis is a good implementation of Interface Segregation Principle (ISP),",
    "because the 'GoodRobot' class only implements the necessary methods, without",
    "any extras. Also, the 'GoodProgrammer' class utilizes an interface perfectly",
    "suited to its needs, with no extra methods.",
    sep="\n",
)

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")


class AbcBlackAndWhitePrinter(metaclass=ABCMeta):
    @abstractmethod
    def print_(self) -> None:
        pass


class BlackAndWhitePrinter(AbcBlackAndWhitePrinter):
    def print_(self) -> None:
        print("Paper printed in black and white!")


class AbcColorPrinter(metaclass=ABCMeta):
    @abstractmethod
    def print_(self) -> None:
        pass


class ColorPrinter(AbcColorPrinter):
    def print_(self) -> None:
        print("Paper printed in color!")


class AbcMultifunctionalPrinter(metaclass=ABCMeta):
    @abstractmethod
    def print_(self) -> None:
        pass

    @abstractmethod
    def scan(self) -> None:
        pass

    @abstractmethod
    def send_fax(self) -> None:
        pass


class MultifunctionalPrinter(AbcMultifunctionalPrinter):
    def print_(self) -> None:
        print("Paper printed!")

    def scan(self) -> None:
        print("Scan completed!")

    def send_fax(self) -> None:
        print("Fax sent!")


black_and_white_printer: BlackAndWhitePrinter = BlackAndWhitePrinter()
color_printer: ColorPrinter = ColorPrinter()
multifunctional_printer: MultifunctionalPrinter = MultifunctionalPrinter()

print()
black_and_white_printer.print_()

print()
color_printer.print_()

print()
multifunctional_printer.print_()

print()
multifunctional_printer.scan()

print()
multifunctional_printer.send_fax()
