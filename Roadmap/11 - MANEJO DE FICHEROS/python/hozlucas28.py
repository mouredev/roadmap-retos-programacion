# pylint: disable=line-too-long
# pylint: disable=missing-module-docstring
# pylint: disable=pointless-string-statement
# pylint: disable=unnecessary-dunder-call


import os
from typing import Self, TypedDict

"""
    Files...
"""

print("Files...")

print(
    """\nFILE: str = "hozlucas28.txt"

if os.path.exists(path=FILE):
    os.remove(path=FILE)


with open(file=FILE, mode="w+t", encoding="utf8") as file:
    CONTENT: list[str] = ["Lucas Hoz\\n", "22\\n", "Python"]
    file.writelines(CONTENT)
    file.close()


with open(file=FILE, mode="r+t", encoding="utf8") as file:
    for LINE in file.readlines():
        print(LINE, end="")
    file.close()


if os.path.exists(path=FILE):
    os.remove(path=FILE)\n"""
)

FILE: str = "hozlucas28.txt"

if os.path.exists(path=FILE):
    os.remove(path=FILE)


with open(file=FILE, mode="w+t", encoding="utf8") as file:
    CONTENT: list[str] = ["Lucas Hoz\n", "22\n", "Python"]
    file.writelines(CONTENT)
    file.close()


with open(file=FILE, mode="r+t", encoding="utf8") as file:
    for LINE in file.readlines():
        print(LINE, end="")
    file.close()


if os.path.exists(path=FILE):
    os.remove(path=FILE)


print(
    "\n\n# ---------------------------------------------------------------------------------- #"
)

"""
    Additional challenge...
"""


Product = TypedDict("Product", {"amount": int, "name": str, "price": float})
Total = TypedDict("Total", {"amount": int, "total": float})


class SalesFile:
    """Sales files"""

    __path: str
    __deleted: bool = False

    def __init__(self, path: str, _products: None | list[Product] = None) -> None:
        if _products is None:
            _products = []

        mapped_products: list[Product] = self.__map_products(_products=_products)

        self.__path = path
        self.__rewrite_products(_products=mapped_products)

    def __get_product_index(self, _product_name) -> int | None:
        for i, __product in enumerate(iterable=self.get_products()):
            if __product["name"].upper() == _product_name.upper():
                return i

        raise NameError("Product doesn't exist")

    def __is_deleted(self) -> bool | None:
        if self.__deleted:
            raise FileNotFoundError()

        return False

    def __map_products(self, _products: list[Product]) -> list[Product]:
        mapped_products: list[Product] = []
        products_copy: list[Product] = _products.copy()

        for i, anchor_product in enumerate(iterable=products_copy):
            for j, next_product in enumerate(iterable=products_copy[i + 1 :]):
                if anchor_product["name"].upper() == next_product["name"].upper():
                    anchor_product["amount"] += next_product["amount"]
                    anchor_product["price"] = max(
                        anchor_product["price"], next_product["price"]
                    )
                    products_copy.pop(j + i + 1)
                    i -= 1

            mapped_products.append(anchor_product)

        return mapped_products

    def __rewrite_products(self, _products: list[Product]) -> Self:
        with open(file=self.__path, mode="w+t", encoding="utf8") as _sales_file:
            if _products:
                new_products: list[str] = []
                for _product in _products:
                    new_products.append(
                        f"{_product['name']}, {_product['amount']}, {_product['price']}\n"
                    )
                new_products[len(new_products) - 1] = new_products[-1][:-1]

                _sales_file.writelines(new_products)
            _sales_file.close()

        return self

    def get_product(self, _product_name: str) -> None | Product:
        """Return saved product in the file."""
        self.__is_deleted()
        for __product in self.get_products():
            if __product["name"].upper() == _product_name.upper():
                return __product

        raise NameError("Product doesn't exist")

    def get_products(self) -> list[Product]:
        """Return saved products in the file."""
        self.__is_deleted()
        _products: list[Product] = []

        with open(file=self.__path, mode="r+t", encoding="utf8") as _sales_file:
            for _product in _sales_file.readlines():
                [_name, _amount, _price] = _product.split(sep=", ")
                _products.append(
                    {"amount": int(_amount), "name": _name, "price": float(_price)}
                )
            _sales_file.close()

        return _products

    def get_total_product(self, _product_name: str) -> None | Total:
        """Return total"""
        _product: None | Product = self.get_product(_product_name=_product_name)

        if _product is not None:
            return {
                "amount": _product["amount"],
                "total": _product["price"] * _product["amount"],
            }

        raise NameError("Product doesn't exist")

    def get_total(self) -> Total:
        """Return "amount" and "price" total of the saved products in the file."""
        self.__is_deleted()
        totals: Total = {
            "amount": 0,
            "total": 0,
        }

        for _product in self.get_products():
            totals["amount"] += _product["amount"]
            totals["total"] += _product["price"] * _product["amount"]

        return totals

    def append_product(self, _product: Product) -> Self:
        """Append products to the file."""
        self.__is_deleted()
        _products: list[Product] = self.get_products()
        _products.append(_product)

        _mapped_products: list[Product] = self.__map_products(_products=_products)
        self.__rewrite_products(_products=_mapped_products)

        return self

    def delete_file(self) -> None:
        """Delete file."""
        self.__is_deleted()
        os.remove(path=self.__path)

    def delete_product(self, _product_name: str) -> Self:
        """Delete saved product"""
        self.__is_deleted()
        _products: list[Product] = self.get_products()
        product_index: int | None = self.__get_product_index(
            _product_name=_product_name
        )

        print(product_index)

        if product_index is not None:
            _products.pop(product_index)
            self.__rewrite_products(_products=_products)

        return self

    def update_product(
        self,
        _product_name: str,
        _amount: int | None = None,
        _price: float | None = None,
    ) -> Self:
        """Update saved product"""
        self.__is_deleted()
        _products: list[Product] = self.get_products()
        product_index: int | None = self.__get_product_index(
            _product_name=_product_name
        )

        if product_index is not None:
            product_to_update: Product = _products[product_index]
            original_amount: int = product_to_update["amount"]
            original_name: str = product_to_update["name"]
            original_price: float = product_to_update["price"]

            _products.__setitem__(
                product_index,
                {
                    "amount": _amount if _amount else original_amount,
                    "name": original_name,
                    "price": _price if _price else original_price,
                },
            )

            self.__rewrite_products(_products=_products)

        return self


sales_file = SalesFile(path="sales.txt")

SHOULD_EXIT: bool = False
while not SHOULD_EXIT:
    operation: str = input(
        "\nSelect an operation ('Add', 'Delete', 'Print', 'Update', 'Total sales', 'Total sales of a product', or 'Exit'): "
    ).upper()

    if operation == "ADD":
        product_information: str = input(
            "\nProduct infomation ([Name], [Amount], [Price]): "
        )
        if not product_information:
            break

        product: list[str] = product_information.split(sep=", ")

        if len(product) == 3:
            sales_file.append_product(
                _product={
                    "amount": int(product[1]),
                    "name": product[0],
                    "price": float(product[2]),
                }
            )
        else:
            print("\nInvalid syntax! It should be, for example: Apple, 10, 50.85")

    elif operation == "DELETE":
        product_name: str = input("\nProduct name to delete: ")
        if product_name:
            sales_file.delete_product(_product_name=product_name)
    elif operation == "PRINT":
        products: list[Product] = sales_file.get_products()

        print()
        for _product in products:
            print(f"{_product['name']}, {_product['amount']}, {_product['price']}")

    elif operation == "UPDATE":
        product_name: str = input("\nProduct name to update: ")
        if not product_name:
            break

        amount: str = input("New amount (optional): ")
        price: str = input("New price (optional): ")
        new_amount: int | None = int(amount) if amount else None
        new_price: float | None = float(price) if price else None

        sales_file.update_product(
            _amount=new_amount, _price=new_price, _product_name=product_name
        )
    elif operation == "TOTAL SALES":
        total_sales: Total = sales_file.get_total()
        print(f"\nAmount = {total_sales['amount']}\nTotal = {total_sales['total']}")
    elif operation == "TOTAL SALES OF A PRODUCT":
        product_name: str = input("\nProduct name: ")
        if not product_name:
            break

        total_product_sales: Total | None = sales_file.get_total_product(
            _product_name=product_name
        )
        if total_product_sales:
            print(
                f"\nAmount = {total_product_sales['amount']}\nTotal = {total_product_sales['total']}"
            )
    elif operation == "EXIT":
        sales_file.delete_file()
        SHOULD_EXIT = True
    else:
        print("\nInvalid operation! Try again...")
