"""
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
"""

from pathlib import Path

def manage_my_file():
    with open("ignaciovihe.txt","a") as my_file:# Si no existe el archivo lo crea. En este caso modo append.
        my_file.write("Ignacio\n40\nPython\n")

    try:
        with open("ignaciovihe.txt", "r") as my_file:
            print(my_file.read())
    except FileNotFoundError as e:
        print(e)

    my_file = Path("ignaciovihe.txt")# Borra el archivo
    if my_file.exists():
        my_file.unlink()

manage_my_file()


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

def sells_management():

    file_name = "sells_resume.txt"

    def _add_product(product: str, quantity: int, price: float):
        """#Escribe una nueva linea al final del fichero."""

        with open(file_name, "a") as f:
            f.write(f"{product}, {quantity}, {price}\n")

    def _write_lines_to_file(lines: list):
        """Escribe las lineas, incluida la modificada, nuevamente en el fichero"""

        with open(file_name, "w") as f:
            f.writelines(lines)

    def _is_number(param: str)-> bool:
        """Comprueba si el parametro str pasado en númerico."""

        try:
            float(param)
            return True
        except ValueError:
            print("Introduce un número.")
            return False
        
    def _get_product_info(option = False):
        """
        Pide al usuario los datos del producto.
        Si se pasa "True" como parametro, pide la cantidad y el precio.
        Si no se pasa parametro, sólo pide el nombre del producto.
        """

        product = input("Introduce el nombre de producto: ")

        if option: #Para añadir y actualizar pido la cantidad y precio

            while True:
                quantity = input("Introduce cantidad vendida: ")
                if not _is_number(quantity):
                    continue
                break

            while True:
                price = input("Introduce precio de venta: ")
                if not _is_number(price):
                    continue
                break
            
            return product, quantity, price
        
        else:

            return product

    def update_product(product: str, quantity: int, price: float):
        already_in = False

        try:
            with open(file_name, "r") as f:
                lines = f.readlines()
                for i,line in enumerate(lines):
                    parts = line.split(", ")
                    if product == parts[0]:
                        lines[i] = f"{product}, {quantity}, {price}\n"
                        already_in = True
                        print("Producto actualizado.")
                        break
                if not already_in:
                    _add_product(product, quantity, price)
                else:
                    _write_lines_to_file(lines)
        except FileNotFoundError:
            _add_product(product, quantity, price)

    def search(product: str, mode = "s"):
        try:
            with open(file_name,"r") as f:
                lines = f.readlines()

                for index, line in enumerate(lines):
                    parts = line.split(", ")
                    if product == parts[0]:
                        if mode == "s":
                            return f"{parts[0]}, {parts[1]}, {parts[2].strip("\n")}"
                        else:
                            element = lines.pop(index)
                            print(f"Elemento [{element.strip("\n")}] eliminado")
                            _write_lines_to_file(lines)
                            return True
                return "No se encuentra el producto"
        except FileNotFoundError:
            print("El archivo no existe.")
            return False

    def calculate_total()-> float:
        with open(file_name,"r") as f:
            lines = f.readlines()
            total = 0
            for line in lines:
                product, quantity, price = line.strip("\n").split(", ")
                total_product = float(quantity) * float(price)
                print(f"[{product}] = [{total_product}]")
                total += total_product
            print(f"[Total de ventas: {total}]")

    def show_products():
        try:
            with open(file_name,"r") as f:
                print(f.read())
        except FileNotFoundError:
            print("El fichero no existe")

    def exit():
        my_file = Path("sells_resume.txt")# Borra el archivo
        if my_file.exists():
            my_file.unlink()
        print("Hasta pronto")




    while True:
        print("SELLS MANAGEMENT")
        print("1. Añadir producto.")
        print("2. Actualizar producto.")
        print("3. Consultar producto.")
        print("4. Eliminar producto.")
        print("5. Total ventas.")
        print("6. Total ventas de un producto.")
        print("7. Mostrar productos")
        print("8. Salir.")
        option = input("Elige una opción: ")

        match option:
            case "1" | "2":
                product, quantity, price = _get_product_info(True)               
                update_product(product, quantity, price)

            case "3":
                product = _get_product_info()
                print(f"[{search(product)}]")

            case "4":
                product = _get_product_info()
                search(product,"d")

            case "5":
                calculate_total()

            case "6":
                product = _get_product_info()
                try:
                    full_product = search(product).split(", ")
                    print(f"Total ventas de {full_product[0]}: {float(full_product[1]) * float(full_product[2])}€")
                except IndexError:
                    print("No se encontro el producto. Operación abortada.")
                except AttributeError:
                    print("Operación abortada.")

            case "7":
                show_products()

            case "8":
                exit()
                break

            case _:
                print("Opcion invalida.")






sells_management()



