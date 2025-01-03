# pylint: disable=pointless-string-statement,missing-class-docstring,missing-function-docstring,missing-module-docstring,too-few-public-methods,useless-parent-delegation

from typing import Union, Literal, Self
from abc import abstractmethod, ABCMeta

"""
    Open-Close Principle (OCP)...
"""

print("Open-Close Principle (OCP)...")

print("\nBad implementation of Open-Close Principle (OCP)...")


class AbcProduct(metaclass=ABCMeta):
    name: str
    price: float

    def __init__(self, *, name: str, price: float) -> None:
        self.name = name
        self.price = price


class Product(AbcProduct):
    def __init__(self, *, name: str, price: float) -> None:
        super().__init__(name=name, price=price)


DiscountStrategy = Union[Literal["holyday"], Literal["seasonal"]]


class BadDiscountCalculator:
    def __init__(self) -> None:
        pass

    def get_discount(
        self, *, product: AbcProduct, discount_strategy: DiscountStrategy
    ) -> float:
        if discount_strategy == "holyday":
            return product.price * 0.15

        if discount_strategy == "seasonal":
            return product.price * 0.21

        return -1


print(
    "\n```",
    """class AbcProduct(metaclass=ABCMeta):
    name: str
    price: float

    def __init__(self, *, name: str, price: float) -> None:
        self.name = name
        self.price = price


class Product(AbcProduct):
    def __init__(self, *, name: str, price: float) -> None:
        super().__init__(name=name, price=price)


DiscountStrategy = Union[Literal["holyday"], Literal["seasonal"]]


class BadDiscountCalculator:
    def __init__(self) -> None:
        pass

    def get_discount(
        self, *, product: AbcProduct, discount_strategy: DiscountStrategy
    ) -> float:
        if discount_strategy == "holyday":
            return product.price * 0.15

        if discount_strategy == "seasonal":
            return product.price * 0.21

        return -1""",
    "```",
    sep="\n",
)

print(
    "\nThis is a bad implementation of Open-Close Principle (OCP),",
    "because the method 'get_discount' of class 'BadDiscountCalculator'",
    "will must change if we have to add more discount strategies",
    sep="\n",
)

print("\nGood implementation of Open-Close Principle (OCP)...")


class AbcDiscountService(metaclass=ABCMeta):
    product: AbcProduct

    def __init__(self, *, product: AbcProduct) -> None:
        self.product = product

    @abstractmethod
    def get_discount(self) -> float:
        pass


class HolidayDiscountService(AbcDiscountService):
    def __init__(self, *, product: AbcProduct) -> None:
        super().__init__(product=product)

    def get_discount(self) -> float:
        return self.product.price * 0.15


class SeasonalDiscountService(AbcDiscountService):
    def __init__(self, *, product: AbcProduct) -> None:
        super().__init__(product=product)

    def get_discount(self) -> float:
        return self.product.price * 0.21


class AbcGoodDiscountCalculator(metaclass=ABCMeta):
    @abstractmethod
    def get_discount(self, *, discount_service: AbcDiscountService) -> float:
        pass


class GoodDiscountCalculator(AbcGoodDiscountCalculator):
    def __init__(self) -> None:
        pass

    def get_discount(self, *, discount_service: AbcDiscountService) -> float:
        return discount_service.get_discount()


print(
    "\n```",
    """class AbcDiscountService(metaclass=ABCMeta):
    product: AbcProduct

    def __init__(self, *, product: AbcProduct) -> None:
        self.product = product

    @abstractmethod
    def get_discount(self) -> float:
        pass


class HolidayDiscountService(AbcDiscountService):
    def __init__(self, *, product: AbcProduct) -> None:
        super().__init__(product=product)

    def get_discount(self) -> float:
        return self.product.price * 0.15


class SeasonalDiscountService(AbcDiscountService):
    def __init__(self, *, product: AbcProduct) -> None:
        super().__init__(product=product)

    def get_discount(self) -> float:
        return self.product.price * 0.21


class AbcGoodDiscountCalculator(metaclass=ABCMeta):
    @abstractmethod
    def get_discount(self, *, discount_service: AbcDiscountService) -> float:
        pass


class GoodDiscountCalculator(AbcGoodDiscountCalculator):
    def __init__(self) -> None:
        pass

    def get_discount(self, *, discount_service: AbcDiscountService) -> float:
        return discount_service.get_discount()""",
    "```",
    sep="\n",
)

print(
    "\nThis is a good implementation of Open-Close Principle (OCP),",
    "because the method 'get_discount' of class 'GoodDiscountCalculator' will must",
    "not change if we have to add more discount services. So, 'get_discount' is closed",
    "to modification but it is open to extension throw any discount service which implements",
    "'AbcDiscountService' abstract class.",
    sep="\n",
)

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")


class AbcMathOperation(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *, a: float, b: float) -> float:
        pass


class AddOperation(AbcMathOperation):
    def __init__(self) -> None:
        pass

    def execute(self, *, a: float, b: float) -> float:
        return a + b


class DivideOperation(AbcMathOperation):
    def __init__(self) -> None:
        pass

    def execute(self, *, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("The second parameter must not be zero")

        return a / b


class MultiplyOperation(AbcMathOperation):
    def __init__(self) -> None:
        pass

    def execute(self, *, a: float, b: float) -> float:
        return a * b


class SubtractOperation(AbcMathOperation):
    def __init__(self) -> None:
        pass

    def execute(self, *, a: float, b: float) -> float:
        return a - b


class AbcCalculator(metaclass=ABCMeta):
    operations: dict[str, AbcMathOperation]

    def __init__(self, *, operations) -> None:
        self.operations = operations

    @abstractmethod
    def add_operation(self, *, name: str, operation: AbcMathOperation) -> Self:
        pass

    @abstractmethod
    def execute_operation(self, *, name: str, a: float, b: float) -> float:
        pass


class Calculator(AbcCalculator):
    operations: dict[str, AbcMathOperation]

    def __init__(
        self, *, operations: None | dict[str, AbcMathOperation] = None
    ) -> None:
        if operations is None:
            operations = {}

        super().__init__(operations=operations)

    def add_operation(self, *, name: str, operation: AbcMathOperation) -> Self:
        operation_exist: bool = self.operations.get(name) is not None

        if operation_exist:
            raise ValueError(f"The operation with '{name}' name already exist")

        self.operations[name] = operation
        return self

    def execute_operation(self, *, name: str, a: float, b: float) -> float:
        operation_not_exist: bool = self.operations.get(name) is None

        if operation_not_exist:
            raise ValueError(f"There is not operation with '${name}' name")

        return self.operations[name].execute(a=a, b=b)


print("\nTesting the OCP system without a pow operation...")

CALCULATOR: Calculator = Calculator()

CALCULATOR.add_operation(name="add", operation=AddOperation())
CALCULATOR.add_operation(name="divide", operation=DivideOperation())
CALCULATOR.add_operation(name="multiply", operation=MultiplyOperation())
CALCULATOR.add_operation(name="subtract", operation=SubtractOperation())

A: float = 4.5
B: float = 6.1

print(
    f"\nAdd operation result ({A} + {B}):",
    CALCULATOR.execute_operation(name="add", a=A, b=B),
)

A = 5
B = 2.2

print(
    f"Divide operation result ({A} / {B}):",
    CALCULATOR.execute_operation(name="divide", a=A, b=B),
)

A = 3
B = 1.75

print(
    f"Multiply operation result ({A} * {B}):",
    CALCULATOR.execute_operation(name="multiply", a=A, b=B),
)

A = 10
B = 8.7

print(
    f"Subtract operation result ({A} - {B}):",
    CALCULATOR.execute_operation(name="subtract", a=A, b=B),
)

print("\nTesting the OCP system with a pow operation...")


class PowOperation(AbcMathOperation):
    def __init__(self) -> None:
        pass

    def execute(self, *, a: float, b: float) -> float:
        return pow(base=a, exp=b)


CALCULATOR.add_operation(name="pow", operation=PowOperation())

A = 11
B = 2

print(
    f"\nPow operation result ({A}^{B}):",
    CALCULATOR.execute_operation(name="pow", a=A, b=B),
)
