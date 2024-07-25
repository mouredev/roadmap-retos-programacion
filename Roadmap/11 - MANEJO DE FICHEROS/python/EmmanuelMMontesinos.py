"""/*
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
 */"""

print("Ejercicio Base")
print("---------------")

# Necesito Importar os para borrar el archivo
import os

def crear_archivo(nombre,edad,lenguaje):
    with open(nombre,"w") as archivo:
        archivo.write(f"Nombre: {nombre[:-4]}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Lenguaje Favorito: {lenguaje}")

def imprimir_archivo(nombre):
    with open(nombre,"r") as archivo:
        for linea in archivo.readlines():
            print(linea)

def eliminar_archivo(nombre):
    try:
        os.remove(nombre)
    except FileNotFoundError as e:
        print(f"El archivo no existe: {e}")

nombre = "EmmanuelMMontesinos.txt"

crear_archivo(nombre,"33","Python")
imprimir_archivo(nombre)
eliminar_archivo(nombre)

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
"""

class BaseDatos:
    def __init__(self,archivo) -> None:
        self.archivo = archivo
    
    def add_compra(self,compra):
        nombre,cantidad,precio = compra.split(",")
        if type(nombre) == str and type(int(cantidad)) == int and type(float(precio)) == float:
            with open(self.archivo,"a") as archivo:
                archivo.write(f"{nombre},{cantidad},{precio}\n")
        else:
            print(f"Error, revise los datos: {compra}")
    def imprime_compra(self):
        with open(self.archivo,"r") as archivo:
            ciclo = 1
            for line in archivo.readlines():
                print(ciclo," - ",line,"\n")
                ciclo += 1
    
    def actualizar_compra(self,id,cambio=None,eliminar=False):
        nueva_lista = []
        with open(self.archivo, "r") as archivo:
            contador = 1
            for line in archivo.readlines():
                if contador != int(id):
                    nueva_lista.append(line)
                else:
                    if not eliminar:
                        nueva_lista.append(cambio + "\n")
                    
                contador += 1
        with open(self.archivo, "w") as archivo:
            for line in nueva_lista:
                archivo.write(line)
    def salir(self):
        os.remove(self.archivo)
                
def app():
    salida = False
    lista_01 = BaseDatos("compra_semanal.txt")
    while not salida:
        accion = input("Elija una opcion\n1-Añadir producto\n2-Consultar productos\n3-Actualizar producto\n4-Eliminar producto\n5-Salir\n")
        if accion == "1":
            producto = input("Añada el producto en el siguiente formato: nombre,cantidad,precio_unidad\n")
            lista_01.add_compra(producto)
        elif accion == "2":
            lista_01.imprime_compra()
        elif accion == "3":
            id = input("Id que quiere actualizar: ")
            cambio = input("Ingrese el nuevo producto: ")
            lista_01.actualizar_compra(id,cambio)
        elif accion == "4":
            id = input("Id que quiere eliminar: ")
            lista_01.actualizar_compra(id,eliminar=True)
        elif accion == "5":
            print("Borrando archivo txt")
            lista_01.salir()
            print("Adios!")
            salida = True

# Función por terminal
app()

# Pruebas Automatizadas
# lista_01 = BaseDatos("compra_semanal.txt")
# lista_01.add_compra("huevos,2,1.5")
# lista_01.add_compra("cafe,1,1.25")
# lista_01.add_compra("cocacola,8,2.8")
# lista_01.add_compra("cubata,4,5.2")
# lista_01.imprime_compra()
# lista_01.actualizar_compra("2","leche,7,0.5")
# lista_01.imprime_compra()
# lista_01.actualizar_compra("3",eliminar=True)
# lista_01.imprime_compra()
# lista_01.salir()