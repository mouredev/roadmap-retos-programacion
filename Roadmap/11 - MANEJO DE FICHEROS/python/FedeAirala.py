# 11 MANEJO DE FICHEROS

## Ejercicio

"""
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.

 """

import os

fichero = open("FedeAirala.txt","w+")                           # Se crea un fichero de tipo escritura
fichero.write("Federico Airala \n43 Años \nLenguaje: Python")   # Escribo varias líneas en el fichero

fichero = open("FedeAirala.txt","r")                            # Fichero en modo lectura
print (fichero.read())                                          # Imresión por pantalla del fichero
fichero.close()                                                 # Se cierra el fichero

if os.path.exists("FedeAirala.txt"):                            # Compruebo si existe el fichero
  os.remove("FedeAirala.txt")                                   # Elimino el fichero si existe
else:
  print("El archivo no existe")                                 # Aviso de fichero inexistente

"""

 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 
 """

try:

  def añadir():
    nom_prod = input("Ingrese nombre del producto: ")
    cant_venta= int(input("Cantidad vendida: "))
    precio = float(input("Ingrese precio: "))

    with open(productos, "a") as file:                          # abro el fichero y lo etiqueto con file
      file.write(f"{nom_prod}, {cant_venta}, {precio}\n")       # file.write escribe en el fichero las variables pasadas en el orden establecido
   
  def consultar():
      nom_prod = input("Nombre: ")
      with open(productos, "r") as file:                      # se abre el fichero en modo lectura y lo etiqueto con file
        for line in file.readlines():                         # file.readlines lee la línea del fichero como una lista y recorre esa lista con for
                if line.split(", ")[0] == nom_prod:           # line.split convierte la cadena en una lista y pregunto si el elemento 0 es igual al ingresado para consulta
                    print(line)                               # lo imprime en caso de encontrarlo
                    break                                     # salgo del bucle en cuando encuentra el nombre, sino se recorre el bucle hasta leer todo el fichero
        else:
           print ("Producto no encontrado")

           
  def actualizar():
    nom_prod = input("Nombre: ")                              # Ingreso producto que deseo actualizar
    cant_venta= input("Cantidad: ")
    precio = input("Precio: ")
    with open(productos, "r") as file:                        # se abre fichero productos en modo lectura
      lines = file.readlines()                                # en variable lines guardo leo y guardo las líneas del fichero
    with open(productos, "w") as file:                        # se abre el fichero en modo escritura
      for line in lines:                                      # se recorren las líneas 
        if line.split(", ")[0] == nom_prod:                   # pregunta si la el nombre de la línea leída es igual al nombre a actualizar
          file.write(f"{nom_prod}, {cant_venta}, {precio}\n") # si es verdadero actuliza la línea
        else:
          file.write(line)                                    # sino la agrega
  
  def cantidad_total():
    total = 0                                               # inicio variable para almacenar la suma total
    with open(productos, "r") as file:                      # abro el fichero en modo lectura y lo etiqueto como file
      for line in file.readlines():                         # se recorre el fichero por cada línea del mismo
          producto = line.split(", ")                       # creo una lista por cada línea del fichero
          cantidad = int(producto[1])                       # a la variable cantidad se le asigna la cantidad leída en cada línea
          precio = float(producto[2])                       # a la variable precio se le asigna el precio leído en cada línea
          total += cantidad * precio                        # a la variable total se le va sumando el total de cada línea del fichero
      print(total)                                          # se imprime la cantidad total de capital 

  def cantidad_producto():
      nom_prod = input("Nombre: ")
      total = 0                                             # inicio variable para almacenar el total del capital por producto
      with open(productos, "r") as file:                    # abro el fichero en modo lectura y lo etiqueto como file
        for line in file.readlines():                       # se recorre el fichero por cada línea del mismo
          producto = line.split(", ")                       # creo una variable en donde se almacena la lista de las líneas leídas del fichero
          if producto[0] == nom_prod:                       # pregunto si el nombre ingresado es igual al nombre del producto de la línea del fichero
            cantidad = int(producto[1])                     # si es igual a cantidad le asigno la cantidad leída en el fichero
            precio = float(producto[2])                     # si es igual a precio le asigno el precio leído en el fichero
            total += cantidad * precio                      # realizo la operación para saber el capital por el producto
            break
        print(total)                                        # se imprime el capital por producto

  def listar_productos():
    with open(productos, "r") as file:                      # se abre fichero productos en modo lectura
     print(file.read() )                                    # se imprimen las líneas del fichero
   

  def eliminar():
    nom_prod = input("Nombre: ")                            # Ingreso nombre de producto a eliminar
    with open(productos, "r") as file:                      # leo el fichero en modo lectura
      lines = file.readlines()                              # asigno a la variable lines la lista de líneas del fichero
    with open(productos, "w") as file:                      # leo el fichero en modo escritura
      for line in lines:                                    # recorro las líneas del fichero
        if line.split(", ")[0] != nom_prod:                 # pregunto si el producto a eliminar se encuantra en la línea
           file.write(line)                                 # mientras el nombre sea distinto al que quiero eliminar se escribe nuevamente cada línea del fichero


  def salir():
    if os.path.exists("productos.txt"):                     # Compruebo si existe el fichero
      os.remove("productos.txt")                            # Elimino el fichero si existe
    else:
     print("El archivo no existe")                          # Se imprime en el caso de no existir el fichero
  

  # Creo el fichero
     
  productos = "productos.txt"
  open(productos, "a")

  while True:
    accion = input("1. Añadir | 2.Consultar | 3.Actualizar | 4.Eliminar | 5.Cantidad vendida total | 6.Cantidad vendida por producto | 7. Listar productos | 8.Salir ")

    if accion.isdigit():
      accion = int(accion)

      match accion:
        case 1:
            añadir()
        case 2:
            consultar()
        case 3:
            actualizar()
        case 4:
            eliminar()
        case 5:
            cantidad_total()
        case 6:
            cantidad_producto()
        case 7:
            listar_productos()
        case 8:
            salir()
            break
        case _:
            print ("La opción no es correcta")

except:
   print ("Error en la ejecución del programa")