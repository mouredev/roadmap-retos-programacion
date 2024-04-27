import os

global global_file_path 
global_file_path = "./worlion.txt"

class Student:
    def __init__(self, name: str, age:int, lang: str) -> None:
        self.name: str = name
        self.age:int = age
        self.lang: str = lang
    
def write_student(file_path: str, student: Student):
    my_file = open(file_path, 'w')
    my_file.write(f"\nName: {student.name}")
    my_file.write(f"\nAge: {student.age}")
    my_file.write(f"\nFavourite language: {student.lang}")
    my_file.close()

def read_students(file_path: str, ):
    my_file_read = open(file_path, 'r')
    print(my_file_read.read())
    my_file_read.close()

def remove_file(file_path: str, ):
    os.remove(file_path)

def test_students_in_files():
    student: Student = Student("Worlion", 40, "Python")
    print("\nEscribiendo en fichero...")
    write_student(global_file_path, student)
    print("\nLeyendo fichero...")
    read_students(global_file_path)
    print("\nBorrando fichero...")
    remove_file(global_file_path)
    
test_students_in_files()

"""
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

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

global shop_sales_file
shop_sales_file = "shop.txt"

class Product():
    def __init__(self, product_str: str) -> None:
        split_values = product_str.split(", ")
        self.name = split_values[0]
        self.quantity = int(split_values[1])
        self.price = float(split_values[2])
    
    def to_str(self):
        return "{}, {}, {}".format(self.name, self.quantity, self.price)
    
    def total_price(self) -> float:
        return self.quantity * self.price

def write_product(product: Product):   
    with open(shop_sales_file, "a") as file:
        file.write(f"{product.to_str()}\n")

def find_product(name: str) -> Product:
    with open(shop_sales_file, "r") as file:
        for product_str in file.readlines():
            if name == product_str.split(",")[0]:
                return Product(product_str)

def update_product(name: str, product: Product):
    with open(shop_sales_file, "r") as file:
        lines = file.readlines()
    with open(shop_sales_file, "w") as file:
        for line in lines:
            if line.split(", ")[0] == name:
                file.write(f"{product.to_str()}\n")
            else:
                file.write(line)
        
def delete_product(product: Product):
    with open(shop_sales_file, "r") as file:
        lines = file.readlines()
    with open(shop_sales_file, "w") as file:
        for line in lines:
            if line.split(", ")[0] != product.name:
                file.write(line)

def totals():
    total = 0
    i = 1
    with open(shop_sales_file, "r") as file:
        print("\t\tProducto\tCantidad\tPrecio\tTotal")
        for line in file.readlines():
            line_product = Product(line)
            print(f"\t{i}\t{line_product.name}\t{line_product.quantity}\t\t{line_product.price}\t{line_product.total_price()} €")
            total += line_product.total_price()
            i+=1
        print(f"Total ventas: {total}")

def show_menu():
    print("\n¿Qué desea hacer?\n")
    print("\t1.- Añadir producto")
    print("\t2.- Consultar producto")
    print("\t3.- Actualizar producto")
    print("\t4.- Eliminar producto")
    print("\t5.- Consultar totales")
    
    print("\t0.- SALIR")
    return input("\nEscriba una opción: ")
    
def process_option(option):
    print(f"opcion: {option}")
    if   option == "1":     # Añadir producto
        name = input("Nombre del producto: ")
        quantity = int(input("Cantidad: "))
        price = float(input("Precio unitario del producto: "))
        product = Product(name +", "+ str(quantity) +", "+ str(price))
        
        write_product(product)
    
    elif option == "2":     # Consultar producto
        name = input("\nNombre del producto a consultar: ")
        product = find_product(name)
        print(f"Producto: {product.to_str()}")
        print(f'Subtotal: {product.total_price():.2f} €')
    
    elif option == "3":     # Actualizar producto
        name = input("\nNombre del producto a actualizar: ")
        product = find_product(name)
        new_name = input(f"\nNuevo nombre (actual = '{product.name}'): ")
        new_quantity = input(f"\nNueva cantidad (actual = '{product.quantity}'): ")
        new_price = input(f"\nNuevo precio/unidad (actual = '{product.price}'): ")
        product = Product(new_name +", "+ str(new_quantity) +", "+ str(new_price))
        update_product(name, product)  
    
    elif option == "4":     # Eliminar producto
        name = input("\nNombre del producto a eliminar: ")
        product = find_product(name)
        confirm = input("¿Está seguro de que desea ELIMINAR el producto? S/N: ")
        if(confirm.upper() == "S"):
            delete_product(product)
            print("se ha eliminado el producto")
        else:
            print("NO se ha eliminado el producto")
            
    elif option == "5":     # Consultar totales
        totals()
    
    elif option == "0":     # SALIR
        print("Hasta pronto...")
        os.remove(shop_sales_file)
    
    else: 
        print("Opción no valida")
        
def shop():
    print("\n\nBienvenido a nuestra tienda...")
    option = ""
    while option != "0":
        option = show_menu()
        process_option(option)

shop()
    