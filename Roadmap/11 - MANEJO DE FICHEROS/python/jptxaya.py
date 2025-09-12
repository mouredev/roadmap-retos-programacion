#MANEJO DE FICHEROS

import os

try:
    #Creacion y escritura
    with open("jptxaya.txt","w+") as my_fich:
        my_fich.writelines(["Jptxaya \n","45 \n"])
        my_fich.write("Java")
    #Lectura Fichero
    with open("jptxaya.txt","r") as my_fich:
        for line in my_fich:
            print(line)
    #Borrado del fichero
    os.remove("jptxaya.txt")
except Exception as exc:
    print(f"Exception {exc}")

#Dificultad Extra
    
def fich_lines_to_list():
    with open("jptx_ventas.txt","r") as my_fich:
        new_list = []
        for line in my_fich.readlines():
            lista = line.split(";")
            new_list.append(lista)
        return new_list

def list_to_fich(lista):
    with open("jptx_ventas.txt","w") as my_fich:
        for elem in lista:
            line = ";".join([elem[0],str(elem[1]),str(elem[2]),"\n"])
            my_fich.write(line)
    
        

                
    
print("Dificultad Extra")
while True:
    print("Gestion de Ventas")
    print("1-Añadir")
    print("2-Consultar")
    print("3-Actualizar")
    print("4-Eliminar")
    print("5-Venta Total")
    print("6-Salir")
    option = input("Selecciona la opcion:")
    match option:
        case "6":
            try:
                os.remove("jptx_ventas.txt")
                break
            except Exception as excep:
                print("Nos se ha podido borrar el fichero porque no existia")
        case "1":
            try:
                nombre_producto = input("Introduce el nombre producto:")
                cantidad_vendida = int(input("Cantidad Vendida:"))
                precio = int(input("Introducir Precio:"))
                with open("jptx_ventas.txt","a+") as my_fich:
                    line = ";".join([nombre_producto,str(cantidad_vendida),str(precio),"\n"])
                    my_fich.write(line)
            except Exception as exc:
                print("Datos incorrectos introducidos")
        case "2":
            lista_total = fich_lines_to_list()
            count = 1
            for lista in lista_total:
                print(f"Linea {str(count)} Product: {lista[0]} Cantidad:{lista[1]} Precio:{lista[2]}")
                count += 1
        case "3":
            try:
                lista_total = fich_lines_to_list()
                count = 1
                for lista in lista_total:
                    print(f"Linea {str(count)} Product: {lista[0]} Cantidad:{lista[1]} Precio:{lista[2]}")
                    count += 1    
                lin_act = int(input("Introducir la el número linea a actualizar:"))
                if lin_act <= len(lista_total) and lin_act >= 1:
                    nombre_producto = input("Introduce el nombre producto:")
                    cantidad_vendida = int(input("Cantidad Vendida:"))
                    precio = int(input("Introducir Precio:"))
                    lista_total[lin_act-1] = [nombre_producto,cantidad_vendida,precio]
                    list_to_fich(lista_total)
            except Exception as excp:
                print(f"Exception {excp}")
        case "4":
            try:
                lista_total = fich_lines_to_list()
                count = 1
                for lista in lista_total:
                    print(f"Linea {str(count)} Product: {lista[0]} Cantidad:{lista[1]} Precio:{lista[2]}")
                    count += 1    
                lin_act = int(input("Introducir el número linea a eliminar:"))
                if lin_act <= len(lista_total) and lin_act >= 1:
                    lista_total.pop(lin_act-1)
                    list_to_fich(lista_total)
            except Exception as excp:
                print(f"Exception {excp}")
        case "5":
            try:
                lista_total = fich_lines_to_list()
                my_dict = {}
                for elem in lista_total:
                    my_dict[elem[0]] = my_dict.get(elem[0],0) + (int(elem[1]) * int(elem[2]))
                venta_total = 0
                for elem in my_dict.keys():
                    print(f"Producto {elem} Ventas:{my_dict[elem]}")
                    venta_total += int(my_dict[elem])
                print(f"Ventas Totales:{venta_total}")
            except Exception as excp:
                print(f"Exception {excp}")




