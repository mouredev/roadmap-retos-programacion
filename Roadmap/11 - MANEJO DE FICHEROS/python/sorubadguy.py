from os import remove
from os import system
"""
*Ficheros
"""

try:
    archivo = open("sorubadguy.txt", "x") #?crea el archivo, de existir, tira error
except:
    archivo = open("sorubadguy.txt", "w")#?sobreescribe un archivo existente, de no existir lo crea
finally:
    print("archivo creado")

archivo.write("Sorubadguy\n")#?añade contenido al archivo
archivo.write("30\n")
archivo.write("Python\n")
archivo.close()
archivo = open("sorubadguy.txt","r")
print(archivo.read())
archivo.close()
remove("sorubadguy.txt")

input("pulse Enter para continuar")
"""
!Extra
"""
nombre_archivo = "ventas_realizadas.txt"

try:
    archivo = open(nombre_archivo, "a")
except:
    archivo = open(nombre_archivo, "w")
finally:
    archivo.close()

def levantar_datos_archivo(nombre_archivo):
    productos = {}
    archivo = open(nombre_archivo, "r")
    prod = archivo.readlines()
    for i in prod:
        j = i.split(",")
        productos[j[0]] = [float(j[1]), float(j[2])]
    archivo.close()
    return productos

def ventas(nombre_archivo):
    

    op = 1
    while op != "0":
        #os.system("cls")
        print("Ingrese la opcion deseada:")
        print("1: Añadir Producto")
        print("2: Consultar Producto")
        print("3: Consultar Venta Total")
        print("4: Actualizar Producto")
        print("5: Eliminar Producto")
        print("0: Salir")
        op = input("Opcion: ")
        match op:
            case "1":
                producto = []
                archivo = open(nombre_archivo, "a")
                print("Ingrese Los datos del productos:")
                producto.append(input("Ingrese Nombre del Producto: "))
                producto.append(input("Ingrese Cantidad Vendida: "))
                producto.append(input("Ingrese presio: "))
                for i in (range(0, len(producto))):
                    if i == len(producto)-1:
                        archivo.write(producto[i]+"\n")
                    else:
                        archivo.write(producto[i]+",")
                archivo.close()
            case "2":
                productos = levantar_datos_archivo(nombre_archivo)
                print("Productos: ")
                for i in productos.keys():
                    print(i)
                producto_mostrar = input("Que producto desea consultar?: ")
                os.system("cls")
                print(f"{producto_mostrar}: \n se han vendido {productos[producto_mostrar][0]} unidades a ${productos[producto_mostrar][1]}\n ganancia: {productos[producto_mostrar][0] * productos[producto_mostrar][1]}")
            case "3":
                productos = levantar_datos_archivo(nombre_archivo)
                ventas_totales = 0
                for i in productos:
                    ventas_totales += productos[i][0]*productos[i][1]
                print(f"Las ventas totales dan un valor de: ${ventas_totales}")
            case "4":
                productos = levantar_datos_archivo(nombre_archivo)
                print("Actualizar")
                if productos != {}:
                    for i in productos:
                        print(i)
                    producot_actualizar = input("Ingrese el producto a actualizar")
                    productos[producot_actualizar][0] += float(input("Ingrese nueva cantidad vendida: "))
                    productos[producot_actualizar][1] = float(input("Ingrese nuevo precio del producto: "))
                    archivo = open(nombre_archivo, "w")
                    for i in productos:
                        archivo.write(f"{i},{str(productos[i][0])},{str(productos[i][1])}\n")
                    archivo.close()
                else:
                    print("No hay productos")
            case "4":
                productos = levantar_datos_archivo(nombre_archivo)
                print("Eliminar")
                if productos != {}:
                    for i in productos:
                        print(i)
                    productos.pop(input("Ingrese el elemento a eliminar: "))
                    archivo = open(nombre_archivo, "w")
                    for i in productos:
                        archivo.write(f"{i},{str(productos[i][0])},{str(productos[i][1])}\n")
                    archivo.close()                    
            case "0":
                remove(nombre_archivo)
                print("El programa se cerrara, Adios")
            case "_":
                print("Opcion incorrecta")


ventas(nombre_archivo)