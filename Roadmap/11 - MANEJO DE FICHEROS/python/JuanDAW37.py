"""* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
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
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt."""
import os

fichero = 'JuanDAW37.txt'

f = open(fichero, 'w') # Abro el fichero en modo escritura
f.write('Juan Jesús Tenreiro Rodríguez\n56\nJavaScript')

f = open(fichero) # Abro el fichero en modo lectura, por omisión
for linea in f:
    print(linea, end='')

f.close() #Cierro el flujo de escritura para poder borrar el fichero     
os.remove(fichero) # Borro el fichero

# EXTRA

def gestion_ventas():
    fichero = 'JuanDAW37.txt'        
    while True:
        print('\n********GESTION DE VENTAS*******')
        print('[A/a]ñadir producto')
        print('[C/c]onsultar producto')
        print('[M/m]modificar producto')
        print('[E/e]liminar producto')
        print('[T/t]Calcular venta total')
        print('[P/p]Calcular venta por producto')
        print('[S/s]alir')
        print('********************************')
        opc = str(input('Pulsa en la operación deseada 👉 -> '))
        match opc:
            case 'A' | 'a':
                anadir(fichero)                
            case 'C' | 'c':
                consultar(fichero)                
            case 'M' | 'm':
                modificar(fichero)                
            case 'E' | 'e':
                eliminar(fichero)                
            case 'T' | 't':
                ventaTotal(fichero)                
            case 'P' | 'p':
                ventaProducto(fichero)
            case 'S' | 's':                
                try:
                    os.remove(fichero)
                    break
                except:
                    print('No se puede eliminar el fichero de ventas porque no existe!!!')
                    break
            case _:
                print('Opción no válida')
                
def anadir(fichero):
    nombre = str(input('Nombre del producto-> '))
    cantidad = input('Cantidad de productos-> ')
    precio = input('Precio del producto-> ')    
    f = open(fichero, 'a')
    f.write(f'{nombre}; {cantidad}; {precio}\n')
    f.close()

def consultar(fichero):
    nombre = str(input('Nombre del producto-> '))
    for  linea in open(fichero, 'r'):
        if nombre in linea:
            print(linea)
    
def modificar(fichero):    
    nombre = str(input('Nombre del producto-> '))
    cantidad = input('Precio del producto-> ')
    precio = input('Precio del producto-> ')
    with open(fichero, 'r') as f:
        lineas = f.readlines() # Guardo los datos del fichero
    with open(fichero, 'w') as f: # Al abrir el fichero en modo escritura, borro el fichero
        for linea in lineas: # Se recorre todo el fichero, buscando el nombre del producto
            if linea.split('; ')[0] == nombre:
                f.write(f'{nombre}; {cantidad}; {precio},\n') # Si encuentra el nombre, modifica la línra
            else:
                f.write(linea) # Si no coincide con el nombre, conserva la línea

def ventaTotal(fichero):
    total = 0
    with open(fichero, 'r') as f:
        for linea in f.readlines():
            campos = linea.strip().split('; ')
            cantidad = campos[1]            
            precio = campos[2]            
            total += int(cantidad) * float(precio)
    print(total)

def ventaProducto(fichero):
    nombre = str(input('Nombre del producto-> '))
    total = 0
    with open(fichero, 'r') as f:
        for linea in f.readlines():
            if nombre in linea:
                campos = linea.strip().split('; ')
                cantidad = campos[1]            
                precio = campos[2]            
                total += int(cantidad) * float(precio)
    print(total)

def eliminar(fichero):
    nombre = str(input('Nombre del producto-> '))
    with open(fichero, 'r') as f:
        lineas = f.readlines() # Guardo los datos del fichero
    with open(fichero, 'w') as f: # Al abrir el fichero en modo escritura, borro el fichero
        for linea in lineas: # Se recorre todo el fichero, buscando el nombre del producto
            if linea.split('; ')[0] != nombre:
                f.write(linea) # Aquellas líneas que no coincidan con el nombre de producto, las conserva

gestion_ventas()