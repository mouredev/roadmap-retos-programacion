#  IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
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
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
#  * archivo .txt.
#  * - Cada producto se guarda en una línea del archivo de la siguiente manera:
#  *   [nombre_producto], [cantidad_vendida], [precio].
#  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#  *   actualizar, eliminar productos y salir.
#  * - También debe poseer opciones para calcular la venta total y por producto.
#  * - La opción salir borra el .txt.

# Formas para abrir un archivo:
# ‘r’: Por defecto, para leer el fichero.
# ‘w’: Para escribir en el fichero.
# ‘x’: Para la creación, fallando si ya existe.
# ‘a’: Para añadir contenido a un fichero existente.
# ‘b’: Para abrir en modo binario.

import os

nombre_fichero = 'RicardiJulio.txt'
with open(nombre_fichero,'w') as fichero:
    fichero.write('Julio Ricardi.\n')
    fichero.write('23 años.\n')
    fichero.write('Python.')
    
with open(nombre_fichero,'r') as fichero:
    contenido = fichero.read()
    print (contenido)        
    
os.remove(nombre_fichero)

# DIFICULTAD EXTRA:
def crear_archivo(nombre_archivo,titulo):
    with open(nombre_archivo,'w')as archivo:
        archivo.write(f'{titulo}\n')
        
def añadir(archivo,nombre,cantidad,precio):
    lineas_actualizadas = []
    with open(archivo,'r')as archivo2:
        lineas = archivo2.readlines()
        for linea in lineas:
            lineas_actualizadas.append(linea)
    with open(archivo,'w') as archivo3:
        archivo3.writelines(lineas_actualizadas)
        archivo3.write(f'[{nombre}],[{cantidad}],[{precio}]\n')
        
def consultar(archivo,nombre):
    with open(archivo,'r') as archivo:
        lineas = archivo.readlines()
    encontrado = False
    for linea in lineas:
        datos = linea.strip().split(',')
        if datos[0] == str(f'[{nombre}]'):
            print(f'{datos[0]},{datos[1]},{datos[2]}')
            encontrado = True
    if not encontrado:
        print(f'{nombre} no ha sido encontrado.') 

def actualizar(archivo,nombre_p,nueva_cantidad,nuevo_precio):
        with open(archivo,'r') as archivo1:
            lineas = archivo1.readlines()
        
        productos_actualizados = []
        encontrado = False
        
        for linea in lineas:
            datos = linea.strip().split(',')
            if datos[0] == str(f'[{nombre_p}]'):
                cantidad = nueva_cantidad if nueva_cantidad is not None else datos[1]
                precio = nuevo_precio if nuevo_precio is not None else datos[2]
                nueva_linea = f'[{nombre_p}],[{cantidad}],[{precio}]\n'
                productos_actualizados.append(nueva_linea)
                encontrado = True
            else:
                productos_actualizados.append(linea)
                
        if not encontrado:
            print(f'{nombre_p} no ha sido encontrado')
            
        with open(archivo,'w')as archivo2:
            archivo2.writelines(productos_actualizados)
            
        print('Producto actualizado correctamente.')

def eliminar(archivo,nombre):
    with open(archivo,'r')as archivo1:
        lineas = archivo1.readlines()
    
    productos_actualizados = []
    encontrado = False
    
    for linea in lineas:
        datos = linea.strip().split(',')
        if datos[0] == f'[{nombre}]':
            encontrado = True
            print(f'{nombre} eliminado correctamente.')
            pass
        else:
            productos_actualizados.append(linea)
            
    if not encontrado:
        print(f'{nombre} no ha sido encontrado')
            
    with open(archivo,'w')as archivo2:
        archivo2.writelines(productos_actualizados)
    
programa = True
contador = 0
while programa == True:
    bienvenida = 'Bienvenido al programa de gestion de ventas.'
    opciones = '1. Crear base de datos.\n2. Añadir un producto.\n3. Consultar un producto.\n4. Actualizar un producto.\n5. Eliminar un producto.\n6. Salir.'
    if contador == 0:
        print(bienvenida)
    print(opciones)
    entrada = int(input('Indique el numero de opcion que desea: '))
    hay_archivo = False
    if entrada == 1 and not hay_archivo:
        nombre_a = input('Indique el nombre del archivo: ')
        titulo = 'Productos, ventas y precios.'
        crear_archivo(nombre_a,titulo)
        hay_archivo = True
        print(f'{nombre_a} creado correctamente.')
    
    elif entrada == 2:
        nombre_p = input('Nombre del producto: ')
        cantidad_p = input('Cantidad del producto: ')
        precio_p = input('Precio del producto: ')
        añadir(nombre_a,nombre_p,cantidad_p,precio_p)
        print(f'{nombre_p} añadido correctamente')
        
    elif entrada == 3:
        nombre_p = input('Nombre del producto: ')
        consultar(nombre_a,nombre_p)
    
    elif entrada == 4:
        nombre_p = input('Nombre del producto: ')
        nueva_c = input('Nueva cantidad: ')
        nuevo_p = input('Nuevo precio: ')
        actualizar(nombre_a,nombre_p,nueva_c,nuevo_p)
    
    elif entrada == 5:
        nombre_p = input('Nombre del producto: ')
        eliminar(nombre_a,nombre_p)
    
    elif entrada == 6:
        print('Hasta luego.')
        programa = False
    
    contador =+ 1
