# -- exercise
class FileTest:
    def __init__(self):
        self.file_name: str = input("enter file name: ")

    def create_file(self) -> None:
        with open(f"{self.file_name}.txt", "w") as file:
            name: str = input("enter your name: ")
            age: int = int(ask_value("enter your age: ", "int"))
            fav_lang: str = input("enter your favorite programming language: ")
            content: str = (
                f"name: {name}\nage: {age}\nfavorite programming language: {fav_lang}"
            )
            file.write(content)
        print("successfully created file")

    def read_file(self) -> None:
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("file not found")

    def remove_file(self) -> None:
        try:
            import os

            os.remove(f"{self.file_name}.txt")
            print("file removed")
        except FileNotFoundError:
            print("file not found")


def check_input(input_value: str, type_check: str) -> bool:
    if type_check == "int":
        try:
            int(input_value)
            return True
        except ValueError:
            return False
    elif type_check == "float":
        try:
            float(input_value)
            return True
        except ValueError:
            return False
    return False


def ask_value(description: str, type_check: str) -> str:
    value: str = input(description)
    while not check_input(value, type_check):
        print("incorrect value, try again.")
        value = input(description)
    return value


# if __name__ == "__main__":
#     file_test = FileTest()
#     file_test.create_file()
#     file_test.read_file()
#     file_test.remove_file()


# -- extra challenge
class Sales:
    def __init__(self):
        self.file_name: str = "sales"

    def add_product(self) -> None:
        with open(f"{self.file_name}.txt", "a") as file:
            product_name: str = input("enter product name: ")
            quantity: int = int(ask_value("enter quantity sold: ", "int"))
            price: float = float(ask_value("enter price: ", "float"))
            content: str = f"{product_name}, {quantity}, {price}\n"
            file.write(content)
        print("product added successfully")

    def read_products(self) -> None:
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("file not found")

    def update_product(self) -> None:
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                lines: list = file.readlines()
            product_name: str = input("enter product name to update: ")
            for i, line in enumerate(lines):
                if product_name in line:
                    quantity: int = int(ask_value("enter quantity sold: ", "int"))
                    price: float = float(ask_value("enter price: ", "float"))
                    lines[i] = f"{product_name}, {quantity}, {price}\n"
                    with open(f"{self.file_name}.txt", "w") as file:
                        file.writelines(lines)
                    print("product updated successfully")
                    break
            else:
                print("product not found")
        except FileNotFoundError:
            print("file not found")

    def remove_product(self) -> None:
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                lines: list = file.readlines()
            product_name: str = input("enter product name to remove: ")
            for i, line in enumerate(lines):
                if product_name in line:
                    del lines[i]
                    with open(f"{self.file_name}.txt", "w") as file:
                        file.writelines(lines)
                    print("product removed successfully")
                    break
            else:
                print("product not found")
        except FileNotFoundError:
            print("file not found")

    def total_sales(self) -> None:
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                lines: list = file.readlines()
            total: float = 0
            for line in lines:
                quantity, price = line.split(", ")[1:]
                total += int(quantity) * float(price)
            print(f"total sales: {total}")
        except FileNotFoundError:
            print("file not found")
            return

    def product_sales(self) -> None:
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                lines: list = file.readlines()
            product_name: str = input("enter product name to calculate sales: ")
            for line in lines:
                if product_name in line:
                    quantity, price = line.split(", ")[1:]
                    total: float = int(quantity) * float(price)
                    print(f"total sales of {product_name}: {total}")
                    break
            else:
                print("product not found")
        except FileNotFoundError:
            print("file not found")
            return

    def remove_file(self) -> None:
        try:
            import os

            os.remove(f"{self.file_name}.txt")
            print("file removed")
        except FileNotFoundError:
            print("file not found")
            return


if __name__ == "__main__":
    sales = Sales()
    continue_program: bool = True
    while continue_program:
        print("---- sales management ----")
        print("1. add product")
        print("2. read products")
        print("3. update product")
        print("4. remove product")
        print("5. total sales")
        print("6. product sales")
        print("7. exit")
        option: int = int(ask_value("choose an option: ", "int"))
        if option == 1:
            sales.add_product()
        elif option == 2:
            sales.read_products()
        elif option == 3:
            sales.update_product()
        elif option == 4:
            sales.remove_product()
        elif option == 5:
            sales.total_sales()
        elif option == 6:
            sales.product_sales()
        elif option == 7:
            sales.remove_file()
            continue_program = False
        else:
            print("incorrect option, try again.")
