"""
Exercise:
"""
import os


def create_txt():
    with open("restevean.txt", "w") as file:
        file.write("Name: Rafael Esteve\nAge: 51\nPreferred coding language: Python")
        print("File created and filled")
    with open("restevean.txt", "r") as file:
        print(file.read())
        file.close()

    os.remove("restevean.txt")
    print("File deleted")


"""
Extra
"""


class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Inventory:

    def __init__(self, filepath):
        self.filepath = filepath
        self.current_products = self.load_products()
        self.added_products = []

    def load_products(self):
        products = []
        try:
            with open(self.filepath, 'r') as file:
                for line in file:
                    name, quantity, price = line.strip().split(',')
                    products.append(Product(name, int(quantity), float(price)))
        except FileNotFoundError:
            pass

        return products

    def save_products(self):
        with open(self.filepath, 'w') as file:
            for product in self.current_products:
                file.write(f'{product.name},{product.quantity},{product.price}\n')

    def delete_file(self):
        os.remove(self.filepath)

    def add_product(self, name, quantity, price):
        if not self.get_product(name):  # no permitir productos duplicados
            new_product = Product(name, quantity, price)
            self.current_products.append(new_product)
            self.added_products.append(new_product)
            self.save_products()
        else:
            print("This product already exists.")

    def get_product(self, name):
        for product in self.current_products:
            if product.name == name:
                return product

    def update_product(self, name, quantity, price):
        product = self.get_product(name)
        if product is not None:
            product.quantity = quantity
            product.price = price
            self.save_products()

    def delete_product(self, name):
        product = self.get_product(name)
        if product:
            self.current_products.remove(product)
            if product in self.added_products:
                self.added_products.remove(product)
            self.save_products()

    def total_sales(self):
        return sum([product.quantity * product.price for product in self.current_products])

    def sales_by_product(self, name):
        product = self.get_product(name)
        if product is not None:
            return product.quantity * product.price
        return 0


def main():
    inventory = Inventory('sales.txt')

    while True:
        print('\n1. Add product')
        print('2. View products')
        print('3. Update')
        print('4. Delete a product')
        print('5. Total sales')
        print('6. Product sales')
        print('7. Exit')

        action = int(input('Choose option: '))

        if action == 1:
            name = input('Product name: ')
            while True:
                try:
                    quantity = int(input('Quantity sold: '))
                    break
                except ValueError:
                    print("You have input an integer for the sold quantity.")
            price = float(input('Unit price: ').replace(',', '.'))
            inventory.add_product(name, quantity, price)

        elif action == 2:  # nueva opción de consulta
            if inventory.added_products:
                for product in inventory.added_products:
                    print(f'Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}')
            else:
                print('There are no products added.')

        elif action == 3:
            name = input('Product name: ')
            quantity = int(input('New quantity: '))
            price = float(input('Unit price: ').replace(',', '.'))
            inventory.update_product(name, quantity, price)

        elif action == 4:
            name = input('Product name: ')
            inventory.delete_product(name)

        elif action == 5:
            print(f'Total sales: ${inventory.total_sales():.2f}')

        elif action == 6:
            name = input('Product name: ')
            print(f'{name} sales amount: ${inventory.sales_by_product(name):.2f}')

        elif action == 7:
            inventory.delete_file()
            break

        else:
            print('Invalid option. Try again.')


if __name__ == "__main__":
    main()
