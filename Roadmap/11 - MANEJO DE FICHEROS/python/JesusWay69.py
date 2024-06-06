import os
os.system('cls')


"""
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
 
"""


#Asignando a una variable la sentencia open() y pasándole como argumentos el nombre del archivo
# y la letra "w" generamos el mismo y nos permite escribir en él
file=open("JesusWay69.txt", "w")
file.write("Jesus\n") #Con el método .write escribimos en archivo creado antes de cerrarlo.
file.write("99\n")
file.write("Python\n")
file.close()# Con el método .close() cerramos el archivo, si lo volvemos a abrir con "w" se vuelve a generar vacío
# o lo que es lo mismo borra todo el contenido.

file=open("JesusWay69.txt", "r")# Con "r" nos permite leer todo el contenido del archivo
readfile = file.read()# asignando a una variable el método .read que devuelve el contenido en un string.
file.close
print(readfile)

with open("JesusWay69.txt", "a") as file:#Abriéndolo con with el archivo se cierra automáticamente 
  file.write("linea nueva añadida\n")# cuando termine el bloque de código tabulado.
with open("JesusWay69.txt", "r") as file:
  readfile = file.read()
print(readfile)

file = open("JesusWay69.txt", "r+")#Con "r+" nos permite leer y añadir contenido al fichero de una vez
#También existe el parámetro "w+" que nos permite leer y escribir pero al igual que con "w" con la llamada
# a .write() se "autogenera" de nuevo el fichero existente borrando el contenido o crea uno nuevo si no existe
# permitiendo leerlo tambien despues de generarlo y antes de cerrarlo.
readfile = file.read()
file.write("otra linea nueva añadida\n")
readfile = file.read()
file.close
print(readfile)
print("\n")

#El método .readline() nos devuelve el contenido de todo el fichero en un string o, si le pasamos
# un número nos devolverá la línea correspondiente empezando por la 1 y descartando la 0 (dará fallo si la línea está vacía)
#El método .readlines() nos devolverá una lista de strings conteniendo cada línea como un elemento de la misma.


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

def create(file):
    try:
        file = open (file, "x")
        file.write("PRODUCTO , UDS VENDIDAS, PRECIO\n")
        file.close()
    except:
        print(f"El fichero \"{file}\" ya existe")
   
   
def add(file,producto, cantidad, precio):
    file = open(file,"a")
    file.write(f"{producto}, {cantidad}, {precio}\n")
    file.close

def show_all(file): 
     file = open(file, "r")
     content = file.read()
     
     print(content)

def find(file, substring:str):
    if not substring.isdigit():
        product_list =[]
        line_num = 0
        file =  open(file, 'r+')
        line = file.readline()
        for line in file:
            line_num +=1
            if substring in line:
                line = str(line_num) + "- " + line
                product_list.append(line)
                continue
            elif substring not in line:
                continue
    else:
        print("La búsqueda de un producto no se puede hacer con valores numéricos únicamente")
    if len(product_list)>0:
                  print(f"Productos encontrados que contienen el nombre \"{substring}\":\n")
                  for i in product_list:
                      print(i)
                  file.close()
                  return True, product_list
    else:
        print("Artículo no encontrado\n")
        return False, product_list
        

print ("""
Elija una opción:
1-Crear nuevo archivo
2-Mostrar contenido de un archivo por consola
3-Añadir producto
4-Editar producto
5-Calcular ventas totales 
6-Calcular ingresos y ventas por producto
7-Eliminar producto
8-Eliminar archivo y salir
 
       """)
option = input("Introduzca una opción del 1 al 7: ")
if option == "1":
    file = input ("Escriba el nombre del archivo que desea crear con su extensión: ")
    create(file)
    print(f"El fichero \"{file}\" se ha creado correctamente")

if option == "2":
    while True:
        file = input("Introduzca el nombre del fichero cuyo contenido quiera ver: ")
        if not os.path.isfile(file):
            print(f"El archivo {file} no existe")
        else:
            print(f"\nContenido del fichero \"{file}\":\n")
        show_all(file)
        break

if option == "3":
 while True:
    file = input("Introduzca el nombre del fichero donde añadir datos: ")
    if not os.path.isfile(file):
        print (f"El archivo {file} no existe")
        continue   
    product = input("Introduzca el nombre del producto: ").title()
    sales = input("Introduzca la cantidad de uds vendidas: ")
    price = input("Introduzca el precio por unidad: ")
    if not sales.isdigit() or not price.isdigit():
        print("ERROR: los campos 'ventas' y 'precio' deben ser valores numéricos, intente de nuevo")
    else:
    
        add(file, product, sales, price)
        print(f"El producto \"{product}\" con {sales} uds vendidas y valor de {price}€/ud se ha añadido al fichero {file}")
        break

if option == "4":
    while True:
        file = input ("Escriba el nombre del fichero donde buscar: ")
        if not os.path.isfile(file):
            print (f"El archivo {file} no existe")
            continue
        product = input("Escriba la marca y/o el modelo del producto que busca: ").title()
        if find(file, product):
          line = int(input("Introduzca el número del producto que desea editar: "))
          column =int(input("Introduzca el número del campo que desea editar, 1-Producto , 2-Uds vendidas o 3-Precio: "))
          new_data = input("Introduzca el nuevo dato: ")
          content = []
          with open(file, 'r+') as file1:
              content = file1.readlines()
              columns = content[line].split(", ")
              columns[column-1] = new_data
              content[line] = ", ".join(columns)
          with open(file, 'w') as file1:
            file1.writelines(content)
          break

if option == "5":
    file = input ("Escriba el nombre del fichero del cual desee calcular las ventas totales: ")
    with open(file, 'r+') as file:
            content = file.readlines()
            acc = 0
            for i in range (1,(len(content))):
                element = content[i]
                column = element.split(", ")
                sales = int(column[1])
                acc += sales
            print(f"Las uds totales vendidas de todos los productos es: {acc}")  

if option == "6":
    file = input ("Escriba el nombre del fichero sobre el que quiera hacer la consulta: ")
    product = input("Escriba la marca y/o el modelo del producto que busca: ").title()
    result_tuple = find (file, product)
    if result_tuple[0] == True:
        my_elements = result_tuple[1]
        total,result,total_sales = 0, 0, 0
        for elements in my_elements:
            elements = str(elements)
            columns = elements.split(", ")
            quantity = columns[1]
            unit_price = columns[2]
            result = int(quantity) * int(unit_price)
            total_quantity = int(quantity)
            total_sales += total_quantity
            total += result        
        print (f"El total de artículos vendidos con nombre \'{product}\' es de  {total_sales} uds")
        print (f"La suma total de dinero ingresado por las ventas de los productos con nombre \'{product}\' es de: {total}€")

   

if option == "7":
    while True:
        file = input ("Escriba el nombre del fichero donde buscar: ")
        if not os.path.isfile(file):
            print (f"El archivo {file} no existe")
            continue
        product = input("Escriba la marca y/o el modelo del producto que busca: ").title()
        result_tuple = find (file, product)
        if result_tuple[0] == True:
          try:
            line = int(input("Introduzca el número del producto que desea borrar: "))
          except:
              print("Sólo se pueden introducír números")
              continue
      
        file1 = open(file , "r+")
        lines = file1.readlines()
        if line <1 or line > len(lines):
            print(f"el número {line} no pertenece a ningún producto")
        else:
          line = lines[line]
          lines.remove(line)
          line.replace("\n", "")
          print(f"El artículo {line} ha sido eliminado")
        file1.close()
        file1 = open (file, "w")
        for line in lines:
            file1.write(line)
        break

if option == "8":
    while True:
        file = input ("Escriba el nombre del fichero a eliminar o exit para salir sin borrar: ")
        if os.path.isfile(file):
            confirmed = input(f"""¿Seguro que quiere eliminar el fichero \"{file}\"? 
  pulse enter para confirmar o escriba cualquier cosa para salir sin borrar: """)
            if confirmed == "":
                os.remove(file)
                print(f"El fichero {file} se ha eliminado con éxito, fin del programa.")
                break
            else:
                print("Fin del programa.") 
                break
        elif file == "exit":
            print("Fin del programa.")
            break
        else:
            print(f"El fichero {file} no existe, pruebe de nuevo\n")