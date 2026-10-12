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

username_github: str = "rosendocamal"
ext: str = "txt"
filename: str = f"{username_github}.{ext}"

with open(filename, "w") as file:
    file.write("Rosendo Camal\n45 años\nNinguno, uso más Python")

with open(filename, "r") as file:
    print(file.read())

import os
file_path = filename
try:
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

# EXTRA

from pathlib import Path; import os

class Storage():
    def __init__(self):
        self.file: str = "products.txt"
        self.fields: str = "product_name; product_code; quantity; sale_quantity; price;\n"
        self.init()

    def init(self) -> None:
        if Path(self.file).exists():
            with open(self.file, "r") as storage:
                fields: str = storage.readlines()[0]
                if fields == self.fields:
                    return None

        with open(self.file, "w") as storage:
            storage.write(self.fields)

    def write(self, option: str, values: tuple):
        mapping: dict[str, int] = {
            "product_name": 0,
            "product_code": 1,
            "quantity": 2,
            "sale_quantity": 3,
            "price": 4
        }

        match option:
            case "add":
                name: str = values[mapping["product_name"]]
                code: int = values[mapping["product_code"]]
                quantity: int = values[mapping["quantity"]]
                sales: int = values[mapping["sale_quantity"]]
                price: float = values[mapping["price"]]

                with open(self.file, "a") as storage:
                    storage.write(f"\n{name};{code};{quantity};{sales};{price};")

            case "del":
                code: int = values[0]
                lines: list = []

                with open(self.file, "r") as storage:
                    lines = storage.readlines()
                with open(self.file, "w") as storage:
                    for line in lines:
                        clean_line = line.strip(";")
                        tmp_code = clean_line[mapping["product_code"]]

                        if code != tmp_code:
                            storage.write(line)

            case "upd":
                code: int = values[0]
                quantity: int = values[1]
                if quantity < 0:
                    sell: int = abs(quantity)
                lines: list = []
                
                with open(self.file, "r") as storage:
                    lines = storage.readlines()
                with open(self.file, "w") as storage:
                    for line in lines:
                        clean_line = line.strip(";")
                        tmp_code = clean_line[mapping["product_code"]]
                
                        if code == tmp_code:
                            l_name = clean_line[mapping["product_name"]]
                            l_code = clean_line[mapping["product_code"]]
                            l_quantity = clean_line[mapping["quantity"]] + quantity
                            l_sale = clean_line[mapping["sale_quantity"]] + sell
                            l_price = clean_line[mapping["price"]]
                            new_line = f"{l_name};{l_code};{l_quantity};{l_sale};{l_price};\n"

                            storage.write(new_line)
                        else:
                            storage.write(line)
            case _:
                pass        

    def read(self) -> any:
        with open(self.file, "r") as storage:
            return storage.read()

    def delete(self) -> any:
        if os.path.exists(self.file):
            os.remove(self.file)
            print("El registro del sistema ha sido eliminado.")
        else:
            print("El registro del sistema no ha sido eliminado.") 

class Producto():
    def __init__(self, name: str, ean13: int, quantity: int, price: float) -> None:
        self.name = name
        self.code = ean13
        self.quantity = quantity
        self.sales_quantity = 0
        self.price = price

    def values(self) -> tuple:
        return (self.name, self.code, self.quantity, self.sales_quantity, self.price)

class Inventario():
    def __init__(self) -> None:
        self.stock: Storage = Storage()

    def agregar_producto(self, product: Producto) -> None:
        self.stock.write("add", product.values())

    def eliminar_producto(self, ean13: int) -> None:
        self.stock.write("del", (ean13))
        # Ideas no implementadas: También se podría validar por existencias, antes de eliminar un producto, no solo por si existe el registro de este

    def actualizar_stock(self, ean13: int, quantity: int) -> None:
        self.stock.write("upd", (ean13, quantity,))

    def ver_productos(self) -> any:
        return self.stock.read()

class PuntoVenta():
    def __init__(self, inventory: Inventario) -> None:
        self.inventory = inventory

    def vender_producto(self, ean13: int, quantity: int) -> None:
        """La cantidad vendidad se ingresa en negativo, no en positivo."""
        self.inventory.actualizar_stock(ean13, -quantity)

    def buscar_producto(self, ean13: int) -> any:
        listado = self.inventory.ver_productos()
        for linea in listado:
            clean_line = linea.split(";")
            code = clean_line[2].strip()

            if code == ean13:
                return linea

class Menu():
    def __init__(self):
        self.inventory = Inventario()
        self.puntoventa = PuntoVenta(self.inventory)

    def display_menu(self):
        while True:
            print("="*30)
            print("MENÚ".center(30))
            print("="*30)
            print("OPCIONES: ")
            print("\t[1]Inventario\n\t[2]Punto de Venta\n\t[3]Salir")
            print("ELIGE UNA OPCIÓN")

            option_user: int = self.get_input({1, 2, 3})

            print()

            match option_user:
                case 1:
                    self.display_inventario()
                case 2:
                    self.display_punto_venta()
                case 3:
                    self.salir()
                    break
                case _:
                    pass

    def display_inventario(self):
        print("-"*30)
        print("INVENTARIO".center(30))
        print("-"*30)
        print("\t[1] Agregar producto\n\t[2] Eliminar producto\n\t[3] Actualizar producto\n\t[4] Listado de productos")

        option_user: int = self.get_input({1, 2, 3, 4})
        
        print()
        
        match option_user:
            case 1:
                print("~"*30)
                print("AGREGAR PRODUCTO".center(30))
                print("~"*30)

                name = input("Nombre del producto: ")
                code = input("Código EAN13: ")
                quantity = input("Cantidad: ")
                precio = input("Precio por unidad: ")

                producto = Producto(name, code, quantity, precio)
                self.inventory.agregar_producto(producto)
                
            case 2:
                print("~"*30)
                print("ELIMINAR PRODUCTO".center(30))
                print("~"*30)
                
                code = input("Código EAN13: ")
                
                self.inventory.eliminar_producto(code)
            case 3:
                print("~"*30)
                print("ACTUALIZAR PRODUCTO".center(30))
                print("~"*30)

                code = input("Código EAN13: ")
                quantity = int(input("Cantidad del producto: "))
                
                self.inventory.actualizar_stock(code, quantity)
            case 4:
                print("~"*30)
                print("VER PRODUCTOS".center(30))
                print("~"*30)
                
                listado = self.inventory.ver_productos()
                print(listado)
            case _:
                pass

    def display_punto_venta(self):
        print("-"*30)
        print("PUNTO DE VENTA".center(30))
        print("-"*30)
        print("\t[1] Registrar venta\n\t[2] Buscar producto")
        
        option_user: int = self.get_input({1, 2})
        
        print()
        
        match option_user:
            case 1:
                print("~"*30)
                print("VENTA".center(30))
                print("~"*30)
        
                code = input("Código EAN13: ")
                quantity = int(input("Cantidad: "))
        
                self.puntoventa.vender_producto(code, quantity)
        
            case 2:
                print("~"*30)
                print("BUSCAR PRODUCTO".center(30))
                print("~"*30)
        
                code = input("Código EAN13: ")

                print(self.inventory.stock.fields)
                print(self.puntoventa.buscar_producto(code))
            case _:
                pass

    def salir(self):
        print("\nSALIR\nSaliendo...\nEliminando registros...")
        self.inventory.stock.delete()

    def get_input(self, options: set[int]):
        while True:
            try:
                option = int(input("Ingresa una opción:\n>>> "))
            except ValueError:
                print("Ingresa una opción válida.")
            else:
                if option in options:
                    return option

if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()