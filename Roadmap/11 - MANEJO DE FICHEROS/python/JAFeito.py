"""
EJERCICIO:
 Desarrolla un programa capaz de crear un archivo que se llame como
 tu usuario de GitHub y tenga la extensión .txt.
 Añade varias líneas en ese fichero:
 - Tu nombre.
 - Edad.
 - Lenguaje de programación favorito.
 Imprime el contenido.
 Borra el fichero.
 
 DIFICULTAD EXTRA (opcional):
 Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 archivo .txt.
 - Cada producto se guarda en una línea del archivo de la siguiente manera:
   [nombre_producto], [cantidad_vendida], [precio].
 - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
   actualizar, eliminar productos y salir.
 - También debe poseer opciones para calcular la venta total y por producto.
 - La opción salir borra el .txt.
 """
 
import os

with open("JAFeito.txt","w") as fichero:
  fichero.write("Jose Angel\n45\nPython")
  
with open("JAFeito.txt","r") as fichero:
  print(fichero.read())
os.remove("JAFeito.txt")

#DIFICULTAD EXTRA

open("Archivo.txt","a")

def busca_prod(producto):
  with open("Archivo.txt","r") as archivo:
      for line in archivo.readlines():
        if line.split(", ")[0] == producto:
          return line
      return "El producto no esta en la lista."
    
def cargar():
  with open("Archivo.txt","r") as archivo:
    buffer = archivo.readlines()
  return buffer

repetir = True    
while repetir:
  eleccion = input("""Seleccione la opcion que desee escribiendo el numero correspondiente:
    1- Añadir producto.
    2- Consultar producto.
    3- Actualizar producto.
    4- Borrar producto.
    5- Ventas totales.
    6- Ventas por producto.
    7- Salir.\n""")
  if eleccion == "1":
    
    print("Introduzca los siguientes datos:")
    nombre = input(f"Nombre del articulo:")
    cantidad = input("Cantidad:")
    precio = input("Precio del articulo:")
    with open("Archivo.txt","a") as archivo:
      archivo.write(f"{nombre}, {cantidad}, {precio}\n")
    
  elif eleccion == "2":
    
    producto = input("Introduzca el nobre del producto que desea consultar:")
    print(busca_prod(producto))
          
  elif eleccion == "3":
    
    producto = input("Introduzca el nombre del producto que desea actualizar:")
    buffer = cargar()
    with open("Archivo.txt","w") as archivo:
      for i in buffer:
        if i.split(", ")[0] == producto:
          print(f"Introduzca los los nuevos datos para el articulo {producto}:")
          nombre = input("Nombre del articulo:")
          cantidad = input("Cantidad:")
          precio = input("Precio del articulo:")
          archivo.write(f"{nombre}, {cantidad}, {precio}\n")
        else:
          archivo.write(i)
      
    
  elif eleccion == "4":
    producto = input("Introduzca el nombre del producto que desea eliminar:")
    buffer = cargar()
    with open("Archivo.txt","w") as archivo:
      for i in buffer:
        if i.split(", ")[0] != producto:
          archivo.write(i)
        
    
  elif eleccion == "5":
    total = 0
    buffer = cargar()
    for i in buffer:
      datos = i.split(", ")
      cantidad = int(datos[1])
      precio = float(datos[2])
      total += cantidad * precio
    print(f"{total}€")
    
  elif eleccion == "6":
    producto = input("Introduzca el nombre del producto que desea consultar:")
    encontrado = busca_prod(producto)
    print(f"{int(encontrado.split(", ")[1]) * float(encontrado.split(", ")[2])}€")
    
  elif eleccion == "7":
    os.remove("Archivo.txt")
    repetir = False
  else:
    print("El valor introducido no es correcto")
    
