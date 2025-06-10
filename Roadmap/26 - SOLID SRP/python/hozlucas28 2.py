# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,pointless-string-statement,line-too-long

from typing import Self


"""
    Single Responsibility Principle (SRP)...
"""

print("Single Responsibility Principle (SRP)...")

print("\nBad implementation of Single Responsibility Principle (SRP)...")


class BadOrder:
    dish: str
    owner: str
    price: float
    uid: int

    def __init__(self, *, dish: str, owner: str, price: float, uid: int) -> None:
        self.dish = dish
        self.owner = owner
        self.price = price
        self.uid = uid

    def process(self) -> Self:
        print(f"\nOrder {self.uid} processed!")
        return self

    def send_invoice(self) -> Self:
        print(f"\nInvoice of order {self.uid} sent!")
        return self


print(
    "\n```",
    """class BadOrder:
    dish: str
    owner: str
    price: float
    uid: int

    def __init__(self, *, dish: str, owner: str, price: float, uid: int) -> None:
        self.dish = dish
        self.owner = owner
        self.price = price
        self.uid = uid

    def process(self) -> Self:
        print(f"\\nOrder {self.uid} processed!")
        return self

    def send_invoice(self) -> Self:
        print(f"\\nInvoice of order {self.uid} sent!")
        return self""",
    "```",
    sep="\n",
)

print(
    "\nThis is a bad implementation of Single Responsibility Principle (SRP), ",
    "because the class 'BadOrder' has three responsibilities:\n",
    "1°) Order creation.",
    "2°) Order process.",
    "3°) Invoice communication.",
    sep="\n",
)


print("\nGood implementation of Single Responsibility Principle (SRP)...")


class GoodOrder:
    dish: str
    owner: str
    price: float
    uid: int

    def __init__(self, *, dish: str, owner: str, price: float, uid: int) -> None:
        self.dish = dish
        self.owner = owner
        self.price = price
        self.uid = uid


class GoodOrderProcessor:
    order: GoodOrder

    def __init__(self, *, order: GoodOrder) -> None:
        self.order = order

    def process(self) -> Self:
        print(f"\nOrder {self.order.uid} processed!")
        return self


class GoodOrderInvoice:
    order: GoodOrder

    def __init__(self, *, order: GoodOrder) -> None:
        self.order = order

    def send(self) -> Self:
        print(f"\nInvoice of order {self.order.uid} sent!")
        return self


print(
    "\n```",
    """class GoodOrder:
    dish: str
    owner: str
    price: float
    uid: int

    def __init__(self, *, dish: str, owner: str, price: float, uid: int) -> None:
        self.dish = dish
        self.owner = owner
        self.price = price
        self.uid = uid


class GoodOrderProcessor:
    order: GoodOrder

    def __init__(self, *, order: GoodOrder) -> None:
        self.order = order

    def process(self) -> Self:
        print(f"\\nOrder {self.order.uid} processed!")
        return self


class GoodOrderInvoice:
    order: GoodOrder

    def __init__(self, *, order: GoodOrder) -> None:
        self.order = order

    def send(self) -> Self:
        print(f"\\nInvoice of order {self.order.uid} sent!")
        return self""",
    "```",
    sep="\n",
)

print(
    "\nThis is a good implementation of Single Responsibility Principle (SRP), ",
    "because each class ('GoodOrder', 'GoodOrderProcessor', and 'GoodOrderInvoice') ",
    "has only one responsability (order creation, order processing, and order invoice communication).",
    sep="\n",
)
