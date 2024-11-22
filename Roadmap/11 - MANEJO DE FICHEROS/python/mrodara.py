import os

############################ MANEJO DE FICHEROS EN PYTHON ######################################
'''
1. Apertura de ficheros con open()
En Python, el método principal para manejar ficheros es open(). 
La función open() permite abrir un fichero y especificar el modo en el que se va a abrir (lectura, escritura, etc.).
'''

# Ejemplo de apertura de un fichero en modo lectura
#try:
#    my_file = open("test.txt", "r")
#
#except FileNotFoundError:
#    print("El fichero no exite y este modo no permite crearlo")
#finally:
#    print("Creando el fichero...")
#    my_file = open("test.txt", "a")
#    print("Fichero creado...")

'''
Modos principales:
'r' - Leer (por defecto). Da error si el fichero no existe.
'w' - Escribir. Crea un fichero nuevo o sobreescribe si existe.
'a' - Añadir. Escribe al final del fichero si existe, o lo crea.
'r+' - Leer y escribir.
'''



'''
2. Escritura de ficheros con write()
Para escribir en un fichero, se utiliza el método write().
Para escribir en un fichero, se usa el modo 'w' o 'a'. 
El modo 'w' sobreescribirá el contenido, mientras que 'a' añadirá al final.
'''

# Ejemplo sobreescribir un fichero
#with open("text.txt", "w") as fichero:
#    fichero.write("Hola, mundo!")
#    
## Ejemplo añadiendo contenido nuevo al fichero
#with open("test.txt", "a") as fichero:
#    fichero.write("Esta frase se añade al final del documento \n")

'''
3. Lectura de ficheros con read()
Python ofrece varios métodos para leer el contenido de un fichero:

read(): Lee todo el contenido del fichero como una cadena.
readline(): Lee una sola línea del fichero.
readlines(): Lee todas las líneas y devuelve una lista.
'''

'''
El bloque with es la forma recomendada de abrir ficheros en Python, 
ya que asegura que el fichero se cierre automáticamente al terminar el bloque.
'''

# Ejemplo de lectura de un fichero
#with open("test.txt", "r") as file:
#    content = file.read()
#    print(content)# Imprime el contenido del fichero
#
## Ejemplo de lectura de un fichero línea a línea
#with open("test.txt", "r") as file:
#    for line in file.readlines():
#        print(line)# Imprime cdada línea del fichero


'''
4. Borrado y manipulación de archivos con os
El módulo 'os' permite realizar operaciones con ficheros como borrar, renombrar o mover.
'''
# Renombrar un fichero
#os.rename("test.txt", "new_name.txt")

# Borrar un fichero
#try:
#    os.remove("test.txt")
#except FileNotFoundError:
#    print("El fichero no existe, luego no se puede borrar")
    

# EJERCICIO PROPUESTO DEL RETO

try:
    os.remove("mrodara.txt")
except FileNotFoundError:
    pass

with open("mrodara.txt", "w") as file:
    file.write('Name: Manu \n')
    file.write('Age: 44 \n')
    file.write('Favourite Programming Language: Python \n')

print("Lectura del fichero")
with open("mrodara.txt", "r") as file:    
    for line in file.readlines():
        print(line)
print('Fin de fichero')
    
try:
    os.remove('mrodara.txt')
except FileNotFoundError:
    print("El fichero no existe, luego no se puede borrar")
finally:
    print("El fichero ha sido borrado")

############################ FIN MANEJO DE FICHEROS EN PYTHON ######################################

############################ EXTRA ######################################
# Gestión de Ventas

def show_menu() -> None:
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Buscar producto")
    print("5. Actualizar producto")
    print("6. Mostrar venta total por producto")
    print("7. Mostrar venta total")
    print("8. Salir")
    
def get_sales(file: str) -> list:
    try:
        with open(file, "r") as file:
            sales = file.readlines()
        return sales
    except FileNotFoundError:
        print("Aún no ha registrada ninguna venta...")
        return []

def insert_sale(file: str, name: str, qty: int, price: float) -> None:
    with open(file, "a") as file:
        file.write(f"{name}, {qty}, {price}.\n")
    
    print('Venta registrada correctamente...')

def delete_sale(file: str, product_name: str) -> None:
    
    updated_lines = []
    
    lines = get_sales(file)
        
    for line in lines:
        if product_name.lower() not in line.lower():
            updated_lines.append(line)
    
    with open(file, "w") as file:
        file.writelines(updated_lines)
    
    print(f"Linea del producto {product_name} eliminada")

def update_sale(file: str, search: str, name: str ="", qty: int = 0, price: float = 0.0) -> None:
    # Localizar la línea a actualizar
    updated_lines = []
    
    lines = get_sales(file)
    for line in lines:
        if search.lower() in line.lower():
            updated_lines.append(f"{name}, {qty}, {price}")
        else:
            updated_lines.append(line)
    
    with open(file, "w") as file:
        file.writelines(updated_lines)
        
    print("Línea actualizada")

def read_sale(file: str, name: str = "") -> list:
    sales = get_sales(file)
    
    for line in sales:
        if name.lower() in line.lower():
            return line.split(", ")

def delete_sales_file(file: str) -> None:
    try:
        os.remove(file)
    except FileNotFoundError:
        print("No existe el fichero de ventas")
    except Exception as e:
        print(f"Error al eliminar el fichero de ventas: {e}")
    finally:
        print("Fichero de ventas eliminado")

def get_total_sales_by_product(file: str) -> dict:
    
    total_sales = {}
    
    sales = get_sales(file)
    
    for sale in sales:
         data = sale.split(", ")
         clean_price = float(data[2].strip("\n").strip("."))
         total_sales[data[0]] = {"qty":data[1], "price":data[2], "total": int(data[1])*clean_price}

    return total_sales

def get_total_sales(file: str) -> None:
    total_sales = 0
    
    sales = get_sales(file)
    
    for sale in sales:
        data = sale.split(", ")
        total_sales += int(data[1]) * float(data[2].strip("\n").strip("."))
    
    print(f"El total de ventas de todos los productos es de: {total_sales} €")
        
end = False

while not end:
    show_menu()
    option = int(input('Indique una opción a realizar: '))
    
    if option == 1: # Mostrar todas las ventas
        sales = get_sales(file="sales.txt")
        for sale in sales:
            print(sale)
    elif option == 2: # Agregar una venta
        product_name = input("Ingrese el nombre del producto: ")
        quantity = int(input("Ingrese la cantidad vendida: "))
        price = float(input("Ingrese el precio del producto: "))
        insert_sale(file="sales.txt", name=product_name, qty=quantity, price=price)
    elif option == 3: # Eliminar una venta
        product = input("Indica el producto a eliminar: ")
        delete_sale(file="sales.txt", product_name=product)
    elif option == 4: # Buscar venta
        product = input("Indica el producto a buscar: ")
        result = read_sale(file="sales.txt", name=product)
        if result:
            print(f'Información de la venta de {product}: {result}')
    elif option == 5: # Actualizar venta
        product = input("Indica el producto a actualizar: ")
        result = read_sale(file="sales.txt", name=product)
        if result:
            product_name = input("Ingrese el nombre del producto: ")
            quantity = int(input("Ingrese la cantidad vendida: "))
            price = float(input("Ingrese el precio del producto: "))
            update_sale(file="sales.txt", search=product, name=product_name, qty=quantity, price=price)
        else:
            print("No se encontró la venta del producto") 
    elif option == 6: # Ventas totales por producto
        result = get_total_sales_by_product(file="sales.txt")
        if result:
            for key, value in result.items():
                print(f'Producto: {key}, Total ventas: {value["total"]}')
    elif option == 7:
        get_total_sales("sales.txt")          
    else: # Salir
        end = True
        delete_sales_file(file="sales.txt")
############################ FIN EXTRA ######################################