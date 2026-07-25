'''
IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.

EJERCICIO:
Desarrolla un programa capaz de crear un archivo que se llame como
tu usuario de GitHub y tenga la extensión .txt.
Añade varias líneas en ese fichero:
- Tu nombre.
- Edad.
- Lenguaje de programación favorito.
Imprime el contenido.
Borra el fichero.'''
import os

with open("pakiuh.txt", "w") as archivo_datos:
    archivo_datos.write(f"Mi nombre es: Francisco Camps\nEdad: 53 años\nMi Lenguaje de programación favorito es: Python.")

with open("pakiuh.txt", "r") as archivo_datos:
    print(archivo_datos.read())
    print(os.getcwd())

if os.path.exists("pakiuh.txt"):
    os.remove("pakiuh.txt")
    print("archivo eliminado")
else:
    print("archivo no elimando")

'''DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera:
  [nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
  actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.'''

productos = [
    ["sables_laser", 20000, 3],
    ["pistolas_laser", 50000, 4],
    ["X-Wing",100, 20000]
    ]

with open("gestion_ventas.txt", "w", encoding="utf-8") as gestion_ventas:

    for producto in productos:
        gestion_ventas.write(f"nombre artículo: {producto[0]} {producto[1]}udds disponibles {producto[2]}€ cada udd\n")

#Añadimos nuevos elementos
def añadir():
    print("Indica los datos del nuevo producto:")
    nombre_producto = input("Nombre de Producto: ")
    unidades_vendidas = int(input("Unidades Vendidas: "))
    precio_venta = int(input("precio de venta: "))
    productos.append([nombre_producto, unidades_vendidas, precio_venta])
    with open("gestion_ventas.txt", "a", encoding="utf-8") as gestion_ventas:
        gestion_ventas.write(f"nombre artículo: {productos[-1][0]} {productos[-1][1]}udds disponibles {productos[-1][2]}€ cada udd\n")

#Para consultar productos
def consultar(nombre_producto):
    for i in range(len(productos)):
        if productos[i][0] == nombre_producto:
            print(f"El producto {productos[i][0]} ha vendido {productos[i][1]} unidades a {productos[i][2]}€ lo que hace un total de venta de {productos[i][1] * productos[i][2]}€")

#Actualizar producto
def actualizar(nombre_producto):
    for i in range(len(productos)):
        if productos[i][0] == nombre_producto:
            producto[i][1] = int(input("Indica nueva cantidad de unidades vendidas: "))
            producto[i][2] = int(input("Indica el precio al que se han vendido: "))
            print(f"El producto {productos[i][0]} ha vendido {productos[i][1]} unidades a {productos[i][2]}€ lo que hace un total de venta de {productos[i][1] * productos[i][2]}€")

#Eliminar producto
def eliminar(nombre_producto):
    for i in range(len(productos)):
        if productos[i][0] == nombre_producto:
            seguro = input(f"Vas a eliminar el producto {productos[i][0]} que ha vendido {productos[i][1]} unidades a {productos[i][2]}€ lo que hace un total de venta {productos[i][1] * productos[i][2]}€ ¿Estás seguro? pulsa S para continuar")
            if seguro == "S":
                del productos[i]

#Calcular el total de las ventas
def total_ventas():
    ventas = 0
    for i in range(len(productos)):
        ventas += (productos[i][1] * productos[i][2])
    return ventas
            

#menú para por terminal modificar los elemnentos
print(f"Selecciona una de las siguientes opciones:\n 1. Añadir Nuevo Producto.\n 2. Consultar Producto\n 3. Actualiza Producto\n 4. Elima Producto\n 5. Calcula la Total Ventas\n 6. Salir")
1
match int(input("Tu número de opción es: ")):
    case 1:
        añadir()
    case 2:
        consulta = input("Indica el nombre del producto a consultar: ")
        consultar(consulta)
    case 3:
        actualiza = input("Indica el nombre del producto a actualizar: ")
        actualizar(actualiza)
    case 4:
        elimina = input("Indica el nombre del producto a eliminar: ")
        eliminar(elimina)
    case 5:
        print(f"El total de ventas es de {total_ventas()}€")
    case 6:
        print("Adios")
    case _:
        print("opción no válida")





        