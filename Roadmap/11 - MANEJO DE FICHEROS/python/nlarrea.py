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

file_path = "nlarrea.txt"

# Write data to the file
with open(file_path, "w") as f:
    f.write("Naia\n")
    f.write("25\n")
    f.write("Python\n")

# Read the file and print the content
# OPTION 1: Read all the content
print("Print file - Option 1:")
with open(file_path, "r") as f:
    print(f.read())

# OPTION 2: Read line by line
print("Print file - Option 2:")
with open(file_path, "r") as f:
    for line in f.readlines():
        print(line.strip())

# Remove the file
import os

os.remove(file_path)


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


file_path = "sales.txt"


def ask_option(options: tuple) -> int:
    print("\nMENU")
    for index, option in enumerate(options):
        print(f"{index}. {option}")

    while True:
        try:
            chosen_option = input("What do you want to do?\n> ")
            if not chosen_option.isnumeric():
                raise TypeError(f"Chosen option must be a number!")
            elif int(chosen_option) < 0 or int(chosen_option) >= len(options):
                raise ValueError(
                    f"Chosen option must be a number between {0}-{len(options) - 1}!"
                )
        except Exception as error:
            print(error)
        else:
            return int(chosen_option)


def run():
    while True:
        options: tuple = (
            "Exit",
            "Add products",
            "See single product",
            "See all products",
            "Update products",
            "Remove products",
            "Calculate total sales",
            "Calculate sales by product",
        )
        option = ask_option(options)
        print("\nChosen option:", options[int(option)], "\n")

        if option == 0:
            try:
                os.remove(file_path)
            except FileNotFoundError:
                # If there is no file yet -> nothing happens
                pass

            return

        try:
            if option == 1:
                # ADD PRODUCTS
                try:
                    product = input("Product name:\n > ")

                    amount_sold = input("Amount sold:\n > ")
                    if not amount_sold.replace(".", "", 1).isnumeric():
                        raise TypeError("Amount must be a number!")

                    price = input("Price:\n > ")
                    if not price.replace(".", "", 1).isnumeric():
                        raise TypeError("Price must be a number!")

                except Exception as error:
                    print(f"{type(error).__name__}: {error}")

                else:
                    with open(file_path, "a") as f:
                        f.write(f"{product}, {amount_sold}, {price}\n")

            elif option == 2:
                # SEE SINGLE PRODUCT
                product = input("Product name:\n > ")

                with open(file_path, "r") as f:
                    for line in f.readlines():
                        if line.split(", ")[0] == product:
                            print("\n", line)

            elif option == 3:
                # SEE ALL PRODUCTS
                with open(file_path, "r") as f:
                    print("\n", f.read())

            elif option == 4:
                # UPDATE PRODUCT
                try:
                    product = input("Product name:\n > ")

                    amount_sold = input("New amount sold:\n > ")
                    if not amount_sold.replace(".", "", 1).isnumeric():
                        raise TypeError("Amount must be a number!")

                    price = input("New price:\n > ")
                    if not price.replace(".", "", 1).isnumeric():
                        raise TypeError("Price must be a number!")

                except Exception as error:
                    print(f"{type(error).__name__}: {error}")

                else:
                    # Read current data
                    with open(file_path, "r") as f:
                        lines = f.readlines()

                    # Write old and new data
                    with open(file_path, "w") as f:
                        for line in lines:
                            if (
                                line.split(", ")[0].strip().lower()
                                == product.strip().lower()
                            ):
                                f.write(f"{product}, {amount_sold}, {price}\n")
                            else:
                                f.write(line)

            elif option == 5:
                # REMOVE PRODUCT
                product = input("Product name:\n > ")

                with open(file_path, "r") as f:
                    lines = f.readlines()

                with open(file_path, "w") as f:
                    for line in lines:
                        if (
                            line.split(", ")[0].strip().lower()
                            != product.strip().lower()
                        ):
                            f.write(line)

            elif option == 6:
                # CALCULATE TOTAL SALES
                with open(file_path, "r") as f:
                    lines = f.readlines()

                sales = 0
                for line in lines:
                    amount_sold = int(line.split(", ")[1].strip())
                    price = float(line.split(", ")[2].strip())
                    sales += amount_sold * price

                print("Total sales:", sales)

            elif option == 7:
                # CALCULATE SINGLE PRODUCT'S SALES
                product = input("Product name:\n > ")

                with open(file_path, "r") as f:
                    lines = f.readlines()

                for line in lines:
                    components = line.split(", ")
                    if components[0] == product:
                        amount_sold = int(components[1].strip())
                        price = float(components[2].strip())
                        sales = amount_sold * price

                        print("Product sales:", sales)
                        break
                else:
                    print(f"No '{product}' product has been found.")

        except FileNotFoundError:
            print("There is no product data yet.")


run()
