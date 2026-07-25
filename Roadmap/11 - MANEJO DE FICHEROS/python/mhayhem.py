# @Author Mhayhem

# IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.

# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo que se llame como
# tu usuario de GitHub y tenga la extensión .txt.
# Añade varias líneas en ese fichero:
# - Tu nombre.
# - Edad.
# - Lenguaje de programación favorito.
# Imprime el contenido.
# Borra el fichero.
import os

with open("mayhem.txt", "w+") as f:
    f.write("Nombre: Daniel\nEdad: 42\nLenguaje favorito: Python")

with open("mayhem.txt", "r") as f:
    read = f.read()
print(read)

try:
    os.remove("mayhem.txt")
except FileNotFoundError as e:
    print(f"{e}")

# DIFICULTAD EXTRA (opcional):
# Desarrolla un programa de gestión de ventas que almacena sus datos en un 
# archivo .txt.
# - Cada producto se guarda en una línea del archivo de la siguiente manera:
#   [nombre_producto], [cantidad_vendida], [precio].
# - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#   actualizar, eliminar productos y salir.
# - También debe poseer opciones para calcular la venta total y por producto.
# - La opción salir borra el .txt

def eshop(archive: str):
    
    while True:
        print("Añadir producto.           [1]\n"
              "Consultar albarán.         [2]\n"
              "Actualizar albarán.        [3]\n"
              "Eliminar producto.         [4]\n"
              "Precio total pedido.       [5]\n"
              "Precio total por producto. [6]\n"
              "Salir                      [7]")
        option = input()
        match option:
            case "1":
                add_product(archive)
            case "2":
                consult_delivery_note(archive)                   
            case "3":
                update_sales_order(archive)
            case "4":
                remove_product(archive)
            case "5":
                display_total_amount(archive)
            case "6":
                display_total_for_product(archive)
            case "7":
                    os.remove(archive )
                    break
            case _:
                print("Opción inválida.")
                
def add_product(archive):
    with open(archive , "a") as f:
        product = input("Producto ha añadir: \n").capitalize()
        quantity = int(input("Cantidad pedida: \n"))
        price = float(input("Precio del producto: \n"))
        f.write(f"{product}, {quantity}, {price}\n")
                    
def consult_delivery_note(archive):
    try:
        with open(archive , "r") as f:
            consult = f.read()
            print(consult)
    except FileNotFoundError as e:
         print(f"{e}")

def update_sales_order(archive):
    update_lines = []
    product_found = False
    
    try:
        product = input("¿Que producto quiere modificar?").capitalize()
        with open(archive , "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split(", ")
                if line[0] == product:
                    product_found = True
                    new_product, quantity, price = line[0], line[1], line[2]
                    modify = input("¿Qué quiere modificar? Producto, cantidad o precio.").strip().lower()
                    match modify:
                        case "producto":
                            new_product = input("Producto: ").capitalize()
                        case "cantidad":
                            quantity = int(input("Cantidad: "))
                        case "precio":
                            price = float(input("Precio: "))
                        case _:
                            print("Opción inválida" )
                    line = f"{new_product}, {quantity}, {price}"
                    update_lines.append(line)
                else:
                    update_lines.append(", ".join(line))
                    
    except FileNotFoundError as e:
        print(f"{e}")
        return
    
    if not product_found:
        print("Producto no encontrado.")
        return
    
    with open(archive , "w+") as f:
        for line in update_lines:
            f.write(line.strip() + "\n")
                
    modify_again = input("¿Quiere actualizar algún producto más? si[1], no [2].\n").lower()
    match modify_again:
        case "1":
            update_sales_order(archive)
        case "2":
            print("Albarán actualizado.")
        case _:
            print("Opción no disponible, actualizaremos albarán igualmente")
            
def remove_product(archive):
    deleted_product = input("¿Qué producto quiere eliminar?\n").capitalize()
    saved_lines = []
    product_found = False
    
    try:
        with open(archive, "r") as f:
            lines = f.readlines()
            for line in lines:
                line_parts = line.strip().split(", ")
                if line_parts[0] == deleted_product:
                    product_found = True
                    print(f"La linea [{', '.join(line_parts)}], se elimino con éxito.")
                else:
                    saved_lines.append(", ".join(line_parts))
                    
    except FileNotFoundError as e:
        print(f"{e}")
        return
    
    if not product_found:
        print("Producto no encontrado.")
        return
    
    with open(archive, "w+") as f:
        for line in saved_lines:
            f.write(line + "\n")
            
def display_total_amount(archive):
    total = 0
    try:
        with open(archive, "r") as f:
            for line in f:
                line = line.strip().split(", ")
                quantity, price = int(line[1]) , float(line[2])
                total += quantity * price
            if total != 0:    
                print(f"El total del albarán es {total:.2f} €.")
            else:
                print("El albarán esta vacío.")
                
    except FileNotFoundError as e:
        print(f"{e}")
    
def display_total_for_product(archive):
    product_total_price = []
    try:
        with open(archive) as f:
            for line in f:
                line = line.strip().split(", ")
                product, quantity, price = line[0], int(line[1]), float(line[2])
                product_total_price.append(f"Producto: {product}, total: {quantity * price:.2f} €")
            
            if product_total_price:
                for item in product_total_price:
                    print(item)
            else:
                print("El albarán esta vacío.")
                
    except FileNotFoundError as e:
        print(f"{e}")
        
if __name__ == "__main__":
    eshop("albaran.txt")