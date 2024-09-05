# /*
#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  *
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo que se llame como
#  * tu usuario de GitHub y tenga la extensión .txt.
#  * Añade varias líneas en ese fichero:
#  * - Tu nombre.
#  * - Edad.
#  * - Lenguaje de programación favorito.
#  * Imprime el contenido.
#  * Borra el fichero.
#  *



# Usando Pathlib
from pathlib import Path as p
# Usando open y os
import os
profile = "NAme : Rayner\n"
profile+= "AGe : 45\n"
profile += "Languaje : Python, GO\n"
name= "raynerpv2022.txt"

def CreateFile(name):

    file = p(name)
    
    try:
        file.write_text(profile)
    except Exception as e:
        print("Ocurrio error inesperado")
    else:
        print("Archivo creado con datos del usuario de github")
    finally:
        print("Terminada la creacion")
    

def Readfile(name):
    file = p(name)
    
    try:
        datos = file.read_text()
    except Exception as e:
        print("Ocurrio error inesperado")
    else:
        print(datos)
    finally:
        print( "FIn de lectura")
    
    

def RemoveFile(name):
    file = p(name)
    try:
        file.unlink()
    except Exception as e:
        print("Ocurrio error inesperado")
    else:
        print("Archivo eliminado con exito")
    finally:
        print("eliminacion concluida")



def ejercicio():
    # path
    CreateFile(name)
    Readfile(name)
    RemoveFile(name)
    # os
    open_CreateFile(name)
    open_ReadFile(name)
    open_DeleteFile(name)



 
def open_CreateFile(name):
    try:

        with open(name,"w+") as f:
            f.write(profile)
    except Exception as e:
        print("Ocurrio error inesperado")
    else:
        print("Archivo creado con exito")
    finally:
        print("Finalizado CREAR")

            

def open_ReadFile(name):
    try:

        with open(name,"r") as f:
            data = f.read()
    except Exception as e:
        print("Ocurrio error inesperado")
    else:
        print(data)
    finally:
        print("Finalizado LEER")

def open_DeleteFile(name):
    try:

        os.remove(name)
    except Exception as e:
        print("Ocurrio error inesperado")
    else:
        print("Archivo eliminado")
    finally:
        print("Finalizado ELIMINAR")



##  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un programa de gestión de ventas que almacena sus datos en un
#  * archivo .txt.
#  * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
#  *   [nombre_producto], [cantidad_vendida], [precio].
#  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#  *   actualizar, eliminar productos y salir.
#  * - También debe poseer opciones para calcular la venta total y por producto.
#  * - La opción salir borra el .txt.
#  */

def add_prod(name):
    nombre =  input("Nombre : ")
    cantidad =  input("Cantidad vendida : ")
    precio = input("Precio de venta : ")
    with open(name,"a") as f:
        f.write(f"{nombre},  {cantidad}, {precio}\n")
         
    print("archivo creado")

def exit(name):
    print("Al salir se eleiminara el archivo...si existe")
    try:
        os.remove(name)
    except:
        print("Archivo no exste")
    else:
        print("Archivo eliminado...")
    finally:
        print(" saliendo ...")

def consultar(name):
    with open(name,"r") as f:
        print("Lista de todos los productos")
        print("Nombre\tCantidad\tPrecio")
        for linea in f:
             linea  = linea.strip()
             print(linea)
    
     
def buscar_item(name) :
    prod = input("Nombre : ")
    with open(name,"r") as f:
        lineas = f.readlines()
        
    try:
        pass
        lista_nombre = [linea.strip().split(", ")[0] for linea in lineas]
        index = lista_nombre.index(prod)

        return index, lineas
    except ValueError:
        return -1,[]

def consultar_producto(name):
     
    index, lineas = buscar_item(name)
    if index == -1:
        print("Producto no encontrado")
    else:
        print(lineas[index])




    
                
def actualizar(name):
  
            index,lineas = buscar_item(name)
            if index == -1 :
                print("Producto no encontrado")
            else:
                
                ncantidad = input("Emtre NUeva Cantidad del producto : ")
                nprecio = input("Entre Nuevo precio del producto : ")
                temp =  f"{lineas[index].split(", ")[0]}, {ncantidad}, {nprecio}\n"
                lineas.pop(index)
                lineas.insert(index,temp)
                with open(name,"w") as f:
                  f.writelines(lineas)
                  print("Producto actualizado")
               
            
     
        


def eliminar(name):
     
            index,lineas = buscar_item(name)
            if index == -1 :
                print("Producto no encontrado")
            else:
                deleteItem = lineas.pop(index)
                print(f"{deleteItem} eliminado")
            with open(name,"w") as f:
                f.writelines(lineas)


def ventasTotales(name):
    
    with open(name,"r") as f:
        lineas = f.readlines()
        Total = 0
        for linea in lineas:
            linea = linea.strip().split(", ")
            print(linea) 
            Total+= int(linea[1])*int(linea[2])
        print("Ventas Totales : ", Total)



def ventasTotalesProducto(name):
            print(" *** Ventas Totales por Producto ***")
            index,lineas = buscar_item(name)
            if index == -1 :
                print("Producto no encontrado")
            else:
                total_p = int(lineas[index].split(", ")[1])*int(lineas[index].split(", ")[2])
                print(f" Del product {lineas[index].split(", ")[0]} se vendieron {total_p}")  
                          


def Gestion():
    name_file = "ventas.txt"
    while True:
        print(" *********** Gestion de Ventas por Productos***********")
        print("1 - Anadir")
        print("2 - Consultar un producto")
        print("3 - MOstrar todos")
        print("4 - Actualizar")
        print("5 - Eliminar")
        print("6 - Ventas totales")
        print("7 - Ventas totales por producto")
        print("8 - Salir")
        op = input()
        match op:
            case "1":
                add_prod(name_file)
            case "2":
                consultar_producto(name_file)
            case "3":
                consultar(name_file)
            case "4":
                actualizar(name_file)
            case "5":
                eliminar(name_file)
            case "6":
                 ventasTotales(name_file)
            case "7":
                ventasTotalesProducto(name_file)
            case "8":
                exit(name_file)
                break
            case _:
                print("Opcion Invalida 1-5 ")




def main():
    while True:
        print("     opcionnes")  
        print("1- Ejercicio")      
        print("2- Extra")  
        print("3 - Salir")
        op = input() 
        match op:
            case "1":
                ejercicio()
            case "2":
                Gestion()
            case "3":
               break
            case _:
                print("Opcion Invalida 1-3 ")

main()
