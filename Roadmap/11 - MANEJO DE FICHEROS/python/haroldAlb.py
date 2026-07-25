# EJERCICIO MANEJO DE FICHEROS #
import os

try:
    f = open("haroldAlb.txt", "a") # Creamos/abrimos el archivo en modo append
    f.writelines("Harold Albiñana Márquez\n") # Escribimos
    f.writelines("45\n")
    f.writelines("Python\n")
    f.close()

    f = open("haroldAlb.txt", "r")
    print(f.read())
    f.close()

    os.remove("haroldAlb.txt")
except Exception as e:
    print(f"Ha ocurrido un error: {e} - {type(e).__name__}")

# EXTRA #
def main_menu():
    # Da a elejir opciones entre el 1 y el 8. Hasta que no introduces una opcion correcta no termina.
    # Lanza un error controlado si se introduce letra o caracter
    # Sólo retorna un str numérico entre 1 y 8.
    isOk = True
    menu = '''### GESTOR DE VENTAS ###
    
    1. AÑADIR ARTÍCULO
    2. CONSULTAR ARTÍCULO
    3. ACTUALIZAR ARTÍCULO
    4. VER TODOS LOS ARTÍCULOS
    5. BORRAR ARTÍCULO
    6. CALCULAR VENTAS TOTALES
    7. VENTAS DE UN ARTÍCULO
    8. SALIR'''
    print(menu)
    while isOk:
        try:
            choice = input("Elije una opción del 1 al 8: ")
            if int(choice) >=1 and int(choice) <=8:
                isOk = False
                return choice
        except ValueError as e:
            print(f"{e} - Vuelve a elegir una opción válida")

def askfor_data():
    # Pide artículo, cantidad vendida y precio unitario.
    # Retorna los valores introducidos (str)

    item = input("Artículo: ")
    amount_sold = input("Cantidad vendida: ")
    price = input("Precio por unidad: ")

    return item, amount_sold, price

def add_article(file_name=str, item=str, amount_sold=int, price=float):
    # Abre un archivo en modo adjuntar y escribe una línea con los valores pedidos.

    with open(file_name, "a") as file:
        file.write(f"{item}, {amount_sold}, {price}\n")

def read_txt(file_name):
    # Abre un archivo en modo lectura. Retorna el contenido del archivo
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return f.read() # Retorna un string con el contenido del archivo
    else:
        raise FileNotFoundError("No hay ningín artículo. Añada artículos con la opción 1.")
    
def readlines_txt(file_name):
    # Abre un archivo txt en modo lectura y retorna una lista con las líneas del archivo.

    with open(file_name, "r") as f:
        return f.readlines() # Retorna una lista donde cada item es una línea
    
def update(file_name, search: str, option_change: str, new_value):
    
    lines_file = readlines_txt(file_name)
    aux_name = "auxFile.txt"
    
    for line in lines_file:

        with open(aux_name, "a") as aux_f:
            if search in line:
                line_split = line.split(", ")
                line_split[int(option_change) - 1] = new_value
                new_line = ", ".join(line_split)

                aux_f.write(f"{new_line}")
            else:
                aux_f.write(f"{line}")

    if os.path.exists(file_name): # comprueba que existe el archivo. si el archivo no existe remove() retorna una exceepción
        os.remove(file_name)

    os.rename(aux_name, file_name)

def erase(file_name, search):
    lines_file = readlines_txt(file_name)
    aux_name = "auxFile.txt"

    for line in lines_file:
        with open(aux_name, "a") as aux_f:
            if search not in line:
                aux_f.write(line)

    os.remove(file_name)
    os.rename(aux_name, file_name)
    
def total_sales(file_name):
    total = 0
    with open(file_name, "r") as f:
        f_lines = f.readlines()

    for line in f_lines:
        line_split = line.split(", ")
        total += (int(line_split[1]) * float(line_split[2]))

    return total
 
def search_item(item: str,lines_file: list):
    # Busca el artículo especificado en la lista de líneas de un archivo. Cada item (str) de la lista tiene este formato: "[Articulo], [Cantidad_vendida], [Precio_unitario]."
    # Cuando encuentra el artículo en una línea, crea una lista con lo que hay en ella, haciendo la división por las comas ya preestablecidad.
    for line in lines_file:
        if item in line:
            return line.split(", ") # Divide la cadena en una lista donde cada palabra es un elemento de la lista

def erase_file(file_name=str):
    os.remove(file_txt)

if __name__ == "__main__":
    file_txt = "ventasRoadmap.txt"
    while True:
        choice = main_menu()

        if choice == "1":# Añadir
            item, amount_sold, price = askfor_data()
            add_article(file_txt, item, amount_sold, price)

        elif choice == "2": # Consultar
            print("# CONSULTAR ARTÍCULO #")
            item = input("Artículo: ")
            lines_file = readlines_txt(file_txt)

            line_split = search_item(item, lines_file)
            print(f"{line_split[0]} | Cantidad vendida: {line_split[1]} | Precio unidad: {line_split[2]}")

        elif choice == "3": # Actualizar
            search = input("Artículo a actualizar: ")
            print("Qué desea modificar del artículo:\n  1. Nombre\n  2. Cantidad vendida\n  3. Precio por unidad")
            option = input("Elija una opción del 1 al 3: ")
            new_value = input("Introduzca valor nuevo: ")

            if option == "3":
                new_value = new_value + "\n"

            update(file_txt, search, option, new_value)

        elif choice == "4": # Ver todo
            try:
                print(read_txt(file_txt))
            except Exception as e:
                print(f"{e} | {type(e).__name__}")

        elif choice == "5": # Borrar
            search = input("Artículo a eliminar: ")
            erase(file_txt, search)

        elif choice == "6": # Calcular ventas totales
            print("Las ventas totales son: " + str(total_sales(file_txt)) + " Euros")

        elif choice == "7": # Ventas de un artículo
            item = input("Introduce el artículo para saber sus ventas: ")
            lines_file = readlines_txt(file_txt)
            line_split = search_item(item, lines_file)

            print(f"Se han vendido {int(line_split[1])} {line_split[0]}. Hace un total de {int(line_split[1]) * float(line_split[2])} euros")

        elif choice == "8": # Salir
            if os.path.exists(file_txt): # comprueba que existe el archivo. si el archivo no existe remove() retorna una excepción
                os.remove(file_txt)
            break
            
        else:
            print("Opción incorrecta. Debe elegir un número entre el 1 y el 8.")