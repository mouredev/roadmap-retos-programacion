#Manejo de ficheros
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
fichero = open("Gallitolobo.txt","w+")
fichero.write("Jose Miguel Gallo Zuno\n 23 años \lenguaje:Python ")
fichero = open("Gallitolobo.txt","r")
print (fichero.read)
fichero.close
if os.path.exists("Gallitolobo.txt"):
    os.remove("Gallitolobo.txt")
else:
    print("El archivo no existe")
"""-------------------------------------------------------"""
#Dificultad extra
"""
* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
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
        with open(productos, "a") as file:
          file.write(f"{nom_prod}, {cant_venta}, {precio}\n")       
    def consultar():
        nom_prod = input("Ingrese el nombre del producto")
        with open(productos,"r") as file:
            for line in file.readlines():
                if line.split(", ")[0]== nom_prod:
                    print(line)
                    break
                else:
                    print("Producto no encontrado")
                            
    def actualizar():
        nom_prod = input("Ingrese el nombre del producto")
        cant_venta = input("Ingrese la cantidad vendida:")
        precio = input("Ingrese el precio")
        with open(productos,"r")as file:
            lines= file.readlines
        with open(productos,"r")as file:
            for line in file.readlines():
                if line.split(", ")[0]==nom_prod:
                    file.write(f"{nom_prod}", {cant_venta}, {precio})
                else:
                    file.write(line)
    def cantidad_vendida_total():
        pass
        
    def eliminar():
        print("Eliminar")
        nom_prod= input("Ingrese el nombre del producto")
   
    def cantidad_vendida_por_producto():
        pass
    def listar_prod():
        pass

    productos = "productos.txt"
    open(productos, "a") 
    while True:
        invar= input("1. Añadir | 2.Consultar | 3.Actualizar | 4.Eliminar | 5.Cantidad vendida total | 6.Cantidad vendida por producto | 7. Listar productos | 8.Salir ")
        if invar.isdigit:
            invar= int(invar)
            match invar:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    break
        else:
            print("Tiene que ser un numero!!!")        
except:
    print("Un error ha sucedido")

            
    
