#11 { Retos para Programadores } MANEJO DE FICHEROS

# Bibliography reference
# Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# GPT

"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.

"""
# @by Niko Zen

import os
import json

# Short for print
log = print

# File path setup
github_user = 'duendeintemporal'
file_path = f"{github_user}.txt"

# Data to write in the file
name = 'Niko Zen'
age = '41'
favorite_language = 'JavaScript'

# Create and write to the file
with open(file_path, 'w') as file:
    file.write(f"Name: {name}\nAge: {age}\nFavoriteLanguage: {favorite_language}\n")
    log(f"File {github_user}.txt created successfully.")

# Read the content of the file
try:
    with open(file_path, 'r') as file:
        data = file.read()
        log('Content of the file:')
        log(data)
except Exception as e:
    log(f'Error reading the file {github_user}.txt: {e}')

# Delete the file
try:
    os.remove(file_path)
    log(f"File {github_user}.txt deleted successfully.")
except Exception as e:
    log(f'Error deleting the file {github_user}.txt: {e}')

# Extra Difficulty Exercise
def menu():
    log('\n--- Sales Management ---')
    log('1. Add Product')
    log('2. View Products')
    log('3. Update Product')
    log('4. Delete Product')
    log('5. Calculate Total Sales')
    log('6. Calculate Sales by Product')
    log('7. Exit')
    option = input('Select an option: ')
    handle_menu_option(option)

def handle_menu_option(option):
    if option == '1':
        add_product()
    elif option == '2':
        view_products()
    elif option == '3':
        update_product()
    elif option == '4':
        delete_product()
    elif option == '5':
        calculate_total_sales()
    elif option == '6':
        calculate_sales_by_product()
    elif option == '7':
        exit_program()
    else:
        log('Invalid option, choose a number between 1 and 7. Please try again.')
        menu()

def add_product():
    name = input('Product Name: ')
    quantity = input('Quantity Sold: ')
    price = input('Price: ')
    product = f"{name}, {quantity}, {price}\n"
    with open('sales.txt', 'a') as file:
        file.write(product)
    log('Product added.')
    menu()

def view_products():
    try:
        with open('sales.txt', 'r') as file:
            data = file.read()
            log('\nProducts:\n' + (data or 'No products registered.'))
    except Exception as e:
        log(f'Error reading products: {e}')
    menu()

def update_product():
    name = input('Product Name to Update: ')
    new_quantity = input('New Quantity Sold: ')
    new_price = input('New Price: ')
    
    try:
        with open('sales.txt', 'r') as file:
            data = file.readlines()
        
        products = []
        for line in data:
            if line.startswith(name):
                products.append(f"{name}, {new_quantity}, {new_price}\n")
            else:
                products.append(line)
        
        with open('sales.txt', 'w') as file:
            file.writelines(products)
        
        log('Product updated.')
    except Exception as e:
        log(f'Error updating product: {e}')
    
    menu()

def delete_product():
    name = input('Product Name to Delete: ')
    
    try:
        with open('sales.txt', 'r') as file:
            data = file.readlines()
        
        products = [line for line in data if not line.startswith(name)]
        
        with open('sales.txt', 'w') as file:
            file.writelines(products)
        
        log('Product deleted.')
    except Exception as e:
        log(f'Error deleting product: {e}')
    
    menu()

def calculate_total_sales():
    try:
        with open('sales.txt', 'r') as file:
            data = file.readlines()
        
        total = sum(int(line.split(', ')[1]) * float(line.split(', ')[2]) for line in data if line.strip())
        log(f'Total Sales: {total:.2f}')
    except Exception as e:
        log(f'Error calculating total sales: {e}')
    
    menu()

def calculate_sales_by_product():
    name = input('Product Name: ')
    
    try:
        with open('sales.txt', 'r') as file:
            data = file.readlines()
        
        total = sum(int(line.split(', ')[1]) * float(line.split(', ')[2]) for line in data if line.startswith(name))
        log(f'Total Sales for {name}: {total:.2f}')
    except Exception as e:
        log(f'Error calculating sales for product: {e}')
    
    menu()

def exit_program():
    try:
        os.remove('sales.txt')
        log('Exiting the program and deleting the sales data file.')
    except Exception as e:
        log(f'Error deleting the file: {e}')
    finally:
        log('Program terminated.')

# Start the program
if __name__ == "__main__":
    # Delay before showing the menu
    import time
    time.sleep(1.2)
    menu()



