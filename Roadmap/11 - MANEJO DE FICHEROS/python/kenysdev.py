# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# MANEJO DE FICHEROS 
# -----------------------------------
# Mas info: https://ellibrodepython.com/ficheros-python

import os
class File(): 
    def __init__(self, path):
        self._path = path

    def write_line(self, ln):
        try:
            # r, w, a, x, b
            with open(self._path, 'a+') as file:
                file.write(ln + '\n')
        except Exception as ex:
            print("Error -> f.write_line ->", ex)

    def write_lines(self, lines: list):
        try:
            with open(PATH, 'w') as file:
                file.writelines(lines)
        except Exception as ex:
            print("Error -> f.write_lines ->", ex)

    def read_line(self) -> str:
        try:
            with open(self._path, 'r') as file:
                return file.readline()
        except Exception as ex:
            print("Error -> f.read_line ->", ex)
    
    def read_lines(self) -> list:
        try:
            with open(self._path, 'r') as file:
                return file.readlines()
        except Exception as ex:
            print("Error -> f.read_line ->", ex)

    def delete_file(self):
        try:
            os.remove(self._path)
            print(f"{self._path} -> eliminado.")
        except Exception as ex:   
            print("Error -> f.delete ->", ex)

    def print_all(self):
        try:
            with open(self._path, 'r') as file:
                print(file.read())
        except Exception as ex:   
            print("Error -> f.print_all ->", ex)

    def query_file(self, qry) -> int:
        try:
            with open(self._path, 'r') as file:
                for i, line in enumerate(file):
                    ln = line.split(",")[0]
                    if  ln == f"[{qry}]": 
                        print(line)
                        return i
                print("No existe.")
                return None                    
        except Exception as ex:   
            print("Error ->  f.query_file ->", ex)


user = File("kenysdev.txt")
user.write_line("Name: ken")
user.write_line("Age: 121")
user.write_line("PL: Python")
user.print_all()
print(user.read_line())
user.delete_file()

# ___________________________________
'''
* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
'''

def add_product(prod = None, qty = None, price= None) -> str:
    while True:
        if not prod or not prod.isalpha():
            print("Debe ingresar un nombre de producto.")
            prod = input("Producto: ")  
        elif not qty or not qty.isdigit():
            print("Debe ingresar una cantidad.")
            qty = input("Cantidad: ")  
        elif not price or not (price.replace('.', '').isdigit()):
            print("Debe ingresar un precio.")
            price = input("Precio: ")
        else:
            line = f"[{prod}], [{qty}], [{price}]"
            sale.write_line(line)
            print("\nGuardado", MSG)
            return f"{line}\n"

def query_product(qry = ""):
    if len(qry) == 0: 
        qry = input("\nConsultar Producto.\nNombre: ")
    sale.query_file(qry)

def delete_product(qry = ""):
    if len(qry) == 0: 
        qry = input("\nEliminar Producto.\nNombre: ")  
    num_line = sale.query_file(qry)
    if num_line is not None:
        lt_products = sale.read_lines()
        del lt_products[num_line]
        sale.write_lines(lt_products)
        print("Producto eliminado") 

def update_product(qry = ""):  
    if len(qry) == 0: 
        qry = input("\nEditar Producto.\nNombre: ")    
    num_line = sale.query_file(qry)
    if num_line is not None:
        lt_products = sale.read_lines()
        line = add_product()
        lt_products[num_line] = line
        sale.write_lines(lt_products) 

def invoice():
    print("\nFactura\n-------------------------")
    lt_products = sale.read_lines()
    monto_total = 0
    for line in lt_products:
        a = (line.split(",")[1]).strip()
        qty = int(a.strip('[]'))
        b = (line.split(",")[2]).strip()
        price = float(b.strip('[]'))
        ln = line.strip('\n')

        sub_total = "${:.2f}".format(qty * price)
        print(f"{ln} -> {sub_total}")
        monto_total += (qty * price)

    print("\nMonto Total -> " + "${:.2f}".format(monto_total))

MSG = ("""
        Gestión de Ventas:
╔═════════════════════════════════╗
║ 1. Agregar        4. Editar     ║  
║ 2. Consultar      5. Facturar   ║
║ 3. Eliminar       6. salir.     ║
╚═════════════════════════════════╝
""")

PATH = "sale_mgt.txt"
print(MSG)
sale = File(PATH)

while True:
    option = input("\nOpción: ")
    match option:
        case "1": add_product()
        case '2': query_product()
        case '3': delete_product()
        case '4': update_product()
        case '5': invoice()
        case '6': 
            print("Adios")
            sale.delete_file()
            break
        case _: print("Opción 1 -> 6")
