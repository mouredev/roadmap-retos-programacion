import os
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
os.remove("sorubadguy.txt")

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

def ventas(nombre_archivo):

    op = 1
    while op != "0":
        os.system("cls")
        print("Ingrese la opcion deseada:")
        print("1: Añadir Producto")
        print("2: Consultar Producto")
        print("3: Actualizar Producto")
        print("4: Eliminar Producto")
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
                pass
            case "3":
                pass
            case "4":
                pass
            case "0":
                print("El programa se cerrara, Adios")
            case "_":
                print("Opcion incorrecta")


ventas(nombre_archivo)