'''
/*
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
 */
 '''

import os

# txt_file = open("./juserdev.txt", "w") # Crea el archivo y lo sobreescribe
# txt_file.write("Nombre: Sebastian\nEdad: 34\n")
# txt_file = open("./juserdev.txt", "a") # De esta manera puedo agregar contenido sin sobreescribir el contenido anterior
# txt_file.write("Lenguaje de programacion favorito: TypeScript")

# with open("./juserdev.txt", "r") as file: # Lee el archivo
#   contenido = file.read()
#   print(contenido)

# de esta manera estoy leyendo el contenido del archivo juserdev.txt
# usando el metodo read() puedo leer el contenido completo del archivo

# with open("./juserdev.txt", "r+") as file: # lee y escribe dentro del archivo
#   contenido = file.read()
#   print(contenido)
#   file.write("\nAlias: Juserdev")

# with open("./juserdev.txt", "r") as file:
#   print(file.read(10)) # lee las 10 primeras posiciones
#   print(file.readline()) # lee la primera linea
#   file.close()

# os.remove("./juserdev.txt") # importando el modulo os elimino el archivo conrrespondiente

def sell():
  print("GESTION DE VENTAS\n")

  with open("./gestion_de_ventas.txt", "w") as file:
    file.write("### GESTION DE VENTAS ###\n\n")
    file.write("NOMBRE  | CANTIDAD  | PRECIO  | TOTAL\n")

  def add_product():
    product_name = input("Cual es el nombre del producto: ")
    count = input("Cual es la cantidad vendida del producto: ")
    price = input("Cual es el precio del producto: ")

    total = int(count) * int(price)

    with open("./gestion_de_ventas.txt", "a") as add:
      add.write(f"{product_name} | {count} | ${price}  | ${total}\n")
  
  def read_products():
    with open("./gestion_de_ventas.txt", "r") as reader:
      print(f"\n{reader.read()}")

  def update_products():
    with open("./gestion_de_ventas.txt", "r") as file:
      lines = file.readlines()
      line = input("Cual es la linea que quieres modificar: ")

      try:
        if (int(line) < 4):
          print("\nlinea invalida, seleccion una linea valida\n")
          return
        else:
          product_name = input("Cual es el nombre del producto: ")
          count = input("Cual es la cantidad vendida del producto: ")
          price = input("Cual es el precio del producto: ")

          total = int(count) * int(price)

          lines[int(line) -1 ] = f"{product_name} | {count} | ${price}  | ${total}\n"

          with open("./gestion_de_ventas.txt", "w") as file:
            file.writelines(lines)
          
      except ValueError as e:
        print("Entrada invalida, asegurate de escribir numeros donde corresponde: ", type(e), e)
      except IndexError as e:
        print("Numero de linea fuera del rango: ", type(e),e)
      except Exception as e:
        print("ocurrio un error inesperado: ", type(e),e)

  def delete_product():
    with open("./gestion_de_ventas.txt", "r") as file:
      lines = file.readlines()
      line = input("Cual es la linea que quieres borrar: ")
      int_line = int(line) - 1
      try:
        if int(line) < 4:
          print("\nlinea invalida, seleccion una linea valida\n")
          return
        else:
          del lines[int_line]
      
          with open("./gestion_de_ventas.txt", "w") as file:
            file.writelines(lines)

      except ValueError as e:
        print("Entrada invalida, asegurate de escribir numeros donde corresponde: ", type(e), e)
      except IndexError as e:
        print("Numero de linea fuera del rango: ", type(e),e)
      except Exception as e:
        print("ocurrio un error inesperado: ", type(e),e)
  

  def totalSell():
    total_general = 0

    with open("./gestion_de_ventas.txt", "r") as file:
      lines = file.readlines()[3:]

      for line in lines:
        try:
          parts = line.strip().split("|")
          total = parts[3].strip().replace("$", "")
          total_general += int(total)
        except Exception as e:
          print("Ocurrion un error inesperado", type(e), e)
    
    print(f"\nEl total en ventas es de -> ${total_general}")

  def total_per_product():
    search_product = input("Escriba el nombre del producto: ").strip().lower()
    total_product = 0
    found = False
    with open("./gestion_de_ventas.txt", "r") as file:
      lines = file.readlines()[3:]

      for line in lines:
        parts = line.strip().split("|")
        name = parts[0].strip().lower()
        if name == search_product:
          total = parts[3].strip().replace("$", "")
          total_product += int(total)
          found = True
        
      if found == True:
        print(f"\nVenta total del producto {search_product}: ${total_product}\n")
      else:
        print("\nProducto no encontrado\n")


  while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Ventas totales")
    print("6. Ventas totales por producto")
    print("7. Salir")

    option = input("\nSeleccione una opcion: ")

    match option:
      case "1":
        add_product()
        print("\n -> Producto añadido\n")
      case "2":
        read_products()
        print("\n -> Producto consultados\n")
      case "3":
        update_products()
        print("\n -> Producto actualizado\n")
      case "4":
        delete_product()
        print("\n -> Producto eliminado\n")
      case "5":
        totalSell()
        print("\n -> Este es el total en ventas\n")
      case "6":
        total_per_product()
        print("\n -> Este es el total en ventas por producto\n")
      case "7":
        print("\n -> Saliendo del gestor de ventas\n")
        os.remove("./gestion_de_ventas.txt")
        break
      case _:
        print("\n -> Opcion no valida, escribe una opcion valida del 1 al 5.\n")


sell()

