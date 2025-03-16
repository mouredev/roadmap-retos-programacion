"""
/*
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
"""
"""
Lectura y escritura de archivos en Python:
* 'r' (Read): valor default. Abre un archivo y lo lee. Indica un error si el archivo no existe
* 'a' (Append): abre un archivo para agregar informacion. Si no existe, lo crea
* 'w' (Write): abre un archivo para escribir. Si no existe, lo crea.
* 'x' (Create): crea un archivo con el nombre especificado. Retorna un error si ya existe.
* 'b' (Binario): abrir en modo binario
* '+' (Adicional): al agregar este simbolo a un modo ya sea de lectura o escritua puedo combinarlo con otra forma (escritura + lectura)
"""
"""
Para tener en cuenta 
* Al leer un archivo cada linea de ejecucion abrira el archivo y lo leera. Es continua la lectura.
* Si yo imprimo la lectura total del archivo y luego una lectura por cantidad de caracteres, 
* esta ultima no tendra efecto ya que he terminado de leer el archivo por completo.
"""
"""
Metodos:
* read(): lee el fichero. Tambien le puedo pasar como argumento un numero de caracteres a leer.
* readline(): lee una linea y la devuelve como una cadena.
* readlines(): lee todas las lineas del fichero y las devuelve como elementos de cadena en una lista, uno para cada linea.
* write(): escribe una cadena
* writelines(): escribe varias cadenas al mismo tiempo
"""
"""
Gestores de contexto (context managers)
* Contexto: conjunto de datos utilizados por un recurso que deben ser guardados para su posterior reutilizacion. 
* Gestor de contexto: permite aplicar una serie de acciones a la entrada y salida del bloque de codigo que engloba.
* with: gestor de contexto. Es una clase que contiene los metodos __enter__() y __exit__(). Estos abren y cierran los archivos para manipularlos.
"""

# Para borrar el fichero debo importar la libreria 'os' para acceder a los modulos del sistema operativo.
import os

def files():
    with open('C:/Users/pau87/OneDrive/Documentos/Roadmap 11/file.txt','w+') as file:
        # Escribir lineas
        file.write('Paula Adgi Romano\n')
        file.write('36\n')
        file.write('Python\n')
        
        # Lee archivo completo
        print(file.read())
             
        # Lee una linea
        print(file.readline())
        
        # Lee y genera una lista. Si leyo una linea anteriormente comienza desde donde quedo. Si ya se leyo el archivo completo, retorna una lista vacia.
        print(file.readlines())

        # Leer lineas. No se ejecuta si el archivo ya fue leido.
        for line in file:
            print(line)
            
    # Borramos el archivos
    os.remove('C:/Users/pau87/OneDrive/Documentos/Roadmap 11/file.txt')
    print('Archivo eliminado')
            
#files()

"""
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
"""
def mi_empresa():
    while True:
        print("""
        BIENVENIDO AL SISTEMA DE GESTION DE VENTAS
        Por favor, ingrese una opcion:
        1. Agregar producto
        2. Consultar producto
        3. Actualizar producto
        4. Eliminar producto
        5. Calcular venta total
        6. calcular venta por producto 
        7. Salir
        """)
        opcion = int(input())
        if opcion == 1:
            nombre_producto = input('Ingrese el nombre del producto: ')
            cantidad_producto = input('Ingrese la cantidad del producto: ')
            precio_producto = input('Ingrese el precio del producto: ')
            with open("C:/Users/pau87/OneDrive/Documentos/Roadmap 11/ventas.txt", 'a') as file:
                file.write(f'{nombre_producto} - {cantidad_producto} - {precio_producto}\n')
                print('Producto agregado con exito')
                continue
        elif opcion == 2:
            nombre_a_buscar = input('Ingrese el nombre del producto a consultar: ')
            with open("C:/Users/pau87/OneDrive/Documentos/Roadmap 11/ventas.txt", 'r') as file:
                for line in file.readlines():
                    if line.split(', ')[0] == nombre_a_buscar:
                        print(line)
                        break
        elif opcion == 3:
            nombre_a_buscar = input('Ingrese el nombre del producto para actualizar: ')
            nuevo_nombre = input('Ingrese el nuevo nombre: ')
            nueva_cantidad = input('Ingrese el nuevo nombre: ')
            nuevo_precio = input('Ingrese el nuevo nombre: ')
            with open("C:/Users/pau87/OneDrive/Documentos/Roadmap 11/ventas.txt", 'r') as file:
                lineas = file.readlines()
                for linea in lineas:
                    if linea.split(' - ')[0] == nombre_a_buscar:
                        file.write(f'{nuevo_nombre}, {nueva_cantidad}, {nuevo_precio}\n')
                        break
        elif opcion == 4:
            nombre_a_buscar = input('Ingrese el nombre del producto a eliminar: ')
            with open("C:/Users/pau87/OneDrive/Documentos/Roadmap 11/ventas.txt", 'r') as file:
                lineas = file.readlines()
            with open("C:/Users/pau87/OneDrive/Documentos/Roadmap 11/ventas.txt", 'w') as file:
                for linea in lineas:
                    if linea.split(', ')[0] != nombre_a_buscar:
                        file.write(linea)
        elif opcion == 5:
            venta_total = 0
            with open("C:/Users/pau87/OneDrive/Documentos/Roadmap 11/ventas.txt", 'r') as file:
                lineas = file.readlines()
                for linea in lineas:
                    venta_total = linea.split(', ')[1] * linea.split(', ')[2]
            print(f'El total de ventas es de: {venta_total}')
        elif opcion == 6:
            nombre_a_buscar = input('Ingrese el nombre del producto que desea calcular: ')
            venta_producto = 0
            with open("C:/Users/pau87/OneDrive/Documentos/Roadmap 11/ventas.txt", 'r') as file:
                lineas = file.readlines()
                for linea in lineas:
                    if linea.split(', ')[0] == nombre_a_buscar:
                        venta_producto = linea.split(', ')[1] * linea.split(' - ')[2]
            print(f'La venta del producto es de: {venta_producto}')
        elif opcion == 7:
            os.remove("C:/Users/pau87/OneDrive/Documentos/Roadmap 11/ventas.txt")
            print('Archivo eliminado. Programa terminado')            
        else:
            print('La opcion no es correcta, por favor, intentelo de nuevo')
            print("""
            BIENVENIDO AL SISTEMA DE GESTION DE VENTAS
            Por favor, ingrese una opcion:
            1. Agregar producto
            2. Consultar producto
            3. Actualizar producto
            4. Eliminar producto
            5. Calcular venta total
            6. calcular venta por producto 
            7. Salir
            """)
            opcion = int(input())

mi_empresa()
