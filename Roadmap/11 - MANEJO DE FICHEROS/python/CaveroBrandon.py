"""EJERCICIO:
Desarrolla un programa capaz de crear un archivo que se llame como tu usuario de GitHub y tenga la extensión .txt.
Añade varias líneas en ese fichero:
- Tu nombre.
- Edad.
- Lenguaje de programación favorito.
Imprime el contenido.
Borra el fichero."""

import os


def exercise():
    file_name = 'CaveroBrandon.txt'

    with open(file_name, 'w') as file:
        file.write('Name: Brandon Cavero\n')
        file.write('Age: 29\n')
        file.write('Favorite programming language: Python')

    print(f'File {file_name} has been created')

    os.remove(file_name)
    print(f'File {file_name} was removed')

"""DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
- Cada producto se guarda en una línea del arhivo de la siguiente manera: 
    [nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
    actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt."""


class Sales:
    def __init__(self, file):
        self.file = file

    def add_item(self) -> None:
        product_name = input('Product Name: ')
        try:
            quantity = int(input('Quantity: '))
        except ValueError:
            print('Quantity should be a number, try again')
            return
        try:
            price = int(input('Price: '))
        except ValueError:
            print('Price should be a number, try again')
            return

        with open(self.file, 'a') as file:
            file.write(f'{product_name}, {quantity}, {price}\n')

    def search_product(self):
        search = input('Enter the product to search: ')
        try:
            element_found = False
            with open(self.file, 'r') as sales_report:
                for line in sales_report:
                    elements = line.split()
                    if elements[0].replace(',', '') == search:
                        print(f'****Product found****\n'
                              f'Product Name: {elements[0].replace(",", "")}\n'
                              f'Quantity: {elements[1].replace(",", "")}\n'
                              f'Price: {elements[2]}')
                        element_found = True
                if not element_found:
                    print(f'The product "{search}" was not found')
        except FileNotFoundError:
            print('No such file or directory to search the element, please try again')

    def update_product(self):
        product_to_update = input('Enter the product to update: ')
        product_updated = False

        new_product_name = input('Enter the new product name: ')
        try:
            new_quantity = input('Enter the new quantity of the product: ')
            new_price = int(input('Enter the new product price: '))
        except ValueError:
            print('Price and quantity should be a number, try again')
            return

        with open(self.file, "r") as sale_report:
            products = sale_report.readlines()

        with open(self.file, "w") as sale_report:
            for product in products:
                if product_to_update in product:
                    sale_report.write(f"{new_product_name}, {new_quantity}, {new_price}\n")
                    print(f'Product "{product_to_update}" updated successfully')
                    product_updated = True
                else:
                    sale_report.write(product)
        if not product_updated:
            print(f'The product "{product_to_update}" was not found')

    def remove_product(self):
        product_to_remove = input('Enter the product to remove: ')
        try:
            with open(self.file, "r") as sale_report:
                products = sale_report.readlines()

            with open(self.file, "w") as sale_report:
                for product in products:
                    if product_to_remove not in product:
                        sale_report.write(product)
                    elif product_to_remove in product:
                        print(f'The product "{product_to_remove}" was successfully removed')
        except FileNotFoundError:
            print('No such file or directory to search the element, please try again')

    def show_content(self):
        try:
            with open(self.file, 'r') as sales_report:
                print('The actual sales report is:')
                print(sales_report.read())
        except FileNotFoundError:
            print('No such file or directory to shown, try again')

    def total_sales(self):
        total_sales = 0

        with open(self.file, "r") as sales_report:
            products = sales_report.readlines()
            for product in products:
                value = product.split(",")
                total_sales += value[1]
        print(f'The total is: {total_sales}')

    def exit(self):
        try:
            os.remove(self.file)
            print(f'The file {self.file} was successfully removed')
        except FileNotFoundError:
            print('No such file or directory to remove, try again')
        except Exception as e:
            print(f'Something went wrong {e}')


exercise()

sales = Sales('sales_report')
while True:
    print('**************************************\n'
          'MENU: \n'
          '1. Add a new product\n'
          '2. Search for a product\n'
          '3. Update a product\n'
          '4. Remove a product\n'
          '5. Show the sales report\n'
          '6. Total\n'
          '7. Total per product\n'
          '8. Exit')
    try:
        option = int(input('Select an option: '))
        if option == 1:
            sales.add_item()
        elif option == 2:
            sales.search_product()
        elif option == 3:
            sales.update_product()
        elif option == 4:
            sales.remove_product()
        elif option == 5:
            sales.show_content()
        elif option == 6:
            sales.total_sales()
        elif option == 7:
            sales.exit()

    except ValueError:
        print('Select a correct value')
