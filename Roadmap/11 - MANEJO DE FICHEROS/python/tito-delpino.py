#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo que se llame como
#  * tu usuario de GitHub y tenga la extensión .txt.
#  * Añade varias líneas en ese fichero:
#  * - Tu nombre.
#  * - Edad.
#  * - Lenguaje de programación favorito.
#  * Imprime el contenido.
#  * Borra el fichero.

import os

file_name = "tito-delpino.txt"

with open(file_name, "w") as file:
  file.write('Alvaro Del Pino\n')
  file.write('37\n')
  file.write('Python')

with open(file_name, "r") as file:
  print(file.read())

  os.remove(file_name)


#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
#  * archivo .txt.
#  * - Cada producto se guarda en una línea del archivo de la siguiente manera:
#  *   [nombre_producto], [cantidad_vendida], [precio].
#  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#  *   actualizar, eliminar productos y salir.
#  * - También debe poseer opciones para calcular la venta total y por producto.
#  * - La opción salir borra el .txt.

# 1- agregar producto al listado
def agregar_producto(nombre_listado):
  producto = input("Indica el nombre del producto a agregar: ")
  precio = input("Indica el precio unitario: ")
  vendidos = input("Indica la cantidad vendida: ")

  with open(nombre_listado, 'a') as archivo:
    archivo.write(f"{producto}, {precio}, {vendidos}\n")

# 2- imprimir por pantalla el listado
def ver_listado(nombre_listado):
    with open(nombre_listado, 'r') as archivo:
      contenido = archivo.read()
      if contenido == '':
        print("Archivo vacio, agrega un producto")
      else:
        print(f"-Listado productos-\n{contenido}")

# 3- actualizar producto
def actualizar_producto(nombre_listado):
  producto = input("Indica el nombre del producto a actualizar: ")


  with open(nombre_listado, 'r') as archivo:
    lineas = archivo.readlines()
  
  linea_nueva = []
  existe = False

  for linea in lineas:
    nombre, precio, vendidos = linea.strip().split(',')
    if nombre == producto:
      precio_nuevo = input("Indica el nuevo precio unitario: ")
      vendidos_nuevo = input("Indica la cantidad vendida: ")
      
      total_vendidos = int(vendidos) + int(vendidos_nuevo)
      linea_nueva.append(f'{nombre}, {precio_nuevo}, {total_vendidos}\n')
      existe = True
    else:
      linea_nueva.append(linea)
    
  if not existe:
    print("Producto no existente en el listado")

  with open(nombre_listado, 'w') as archivo:
    archivo.writelines(linea_nueva)

# 4- eliminar producto de la lista
def eliminar_producto(nombre_listado):
    producto = input("Indica el nombre del producto a eliminar: ")

    with open(nombre_listado, 'r') as archivo:
      lineas = archivo.readlines()
    
    linea_nueva = []
    existe = False

    for linea in lineas:
      nombre, precio, vendidos = [x.strip() for x in linea.strip().split(',')]
      if nombre == producto:
        existe = True
      else:
        linea_nueva.append(linea)
      
    if not existe:
      print("Producto no existente en el listado")

    with open(nombre_listado, 'w') as archivo:
      archivo.writelines(linea_nueva)

# 5-operaciones de calculo de ventas
def calcular_ventas(nombre_listado):
  print("-1: Ventas totales\n-2: Total ventas de un producto")
  opcion = input("Selecciona la opcion que desees: ")

  if opcion == '1': # ventas totales
    ventas = []

    with open(nombre_listado, 'r') as archivo:
      lineas = archivo.readlines()

    for linea in lineas:
      nombre, precio, vendidos = [x.strip() for x in linea.strip().split(',')]
      vendidos_x_producto = int(precio) * int(vendidos)
      ventas.append(vendidos_x_producto)
    
    print(f"Total vendido en tienda {sum(ventas)} euros")

  if opcion == '2': # ventas por producto
    producto = input("Indica el nombre del producto a calcular: ")

    with open(nombre_listado, 'r') as archivo:
      lineas = archivo.readlines()
    
    for linea in lineas:
      nombre, precio, vendidos = [x.strip() for x in linea.strip().split(',')]
      if nombre == producto:
        vendido_x_producto = int(precio) * int(vendidos)
      else:
        print("Producto no existente en el listado")
      
    print(f"El total vendido de {producto} es {vendido_x_producto} euros")




# crear listado vacio
nombre_listado = 'listado-productos.txt'
open(nombre_listado, 'a').close()

# main
while True:
  print('-----------------MENU--------------------')
  print('-1: Agregar producto\n-2: Consultar listado\n-3: Actualizar producto\n-4: Eliminar producto\n-5: Calcular Ventas\n-6: Salir')
  eleccion = input("Selecciona la opcion que desees: ")

  if eleccion == '1':
    agregar_producto(nombre_listado)
  
  elif eleccion == '2':
    ver_listado(nombre_listado)

  elif eleccion == '3':
    actualizar_producto(nombre_listado)

  elif eleccion == '4':
    eliminar_producto(nombre_listado)

  elif eleccion == '5':
    calcular_ventas(nombre_listado)
  
  elif eleccion == '6':
    print("Saliendo del programa...")
    os.remove(nombre_listado)
    break

  else:
    print("Selecciona una de las opciones disponibles")