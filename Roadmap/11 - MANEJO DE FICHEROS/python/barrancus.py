"#[número] - [lenguaje_utilizado]"
# 
# IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
# 
# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo que se llame como
# tu usuario de GitHub y tenga la extensión .txt.
# Añade varias líneas en ese fichero:
# - Tu nombre.
# - Edad.
# - Lenguaje de programación favorito.
# Imprime el contenido.
# Borra el fichero.
# 
# DIFICULTAD EXTRA (opcional):
# Desarrolla un programa de gestión de ventas que almacena sus datos en un 
# archivo .txt.
# - Cada producto se guarda en una línea del archivo de la siguiente manera:
#   [nombre_producto], [cantidad_vendida], [precio].
# - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#   actualizar, eliminar productos y salir.
# - También debe poseer opciones para calcular la venta total y por producto.
# - La opción salir borra el .txt.
# 
import os
from random import randint

def serparacion(cadena):
    print('{}'.format(cadena * 20))

def first():
    bfile = open(file='barrancus.txt', mode='w+', encoding='UTF-8')
    print(f'Se puede escribir en el archivo {bfile.name}: {bfile.writable()}')
    print(f'Se puede leer el archivo {bfile.name}: {bfile.readable()}')
    bfile.write("David Miño\n")
    bfile.write("47\n")
    bfile.write("Python\n")
    if randint(0,1): bfile.close()
    serparacion('---')
    if bfile.closed:
        bfile = open(file='barrancus.txt', mode='r+', encoding='UTF-8')
        print(f'Se puede escribir en el archivo {bfile.name}: {bfile.writable()}')
        print(f'Se puede leer el archivo {bfile.name}: {bfile.readable()}')
        print(bfile.read())
        bfile.close()
    else:
        bfile.seek(0)
        print(bfile.read())
        bfile.close()
    os.remove(bfile.name)
    serparacion('---')

STOCK = 'stock.txt'

class NoProduct(Exception):
    pass

class Producto:
    
    def __init__(self,*args: list):
        self.nombre_producto, self.cantidad_vendida, self.precio, *self.trash = args
        self.nombre_producto = self.nombre_producto.strip()
        self.cantidad_vendida = int(self.cantidad_vendida)
        self.precio = float(self.precio)
        
    def ventas(self) -> float:
        return self.cantidad_vendida * self.precio
    
class Archivo:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.stock = ""
        self.stock_dict = {}
    
    def file_check(self) -> bool:
        if self.nombre_archivo in os.listdir():
            self.stock = open(self.nombre_archivo, 'r+', encoding='UTF-8')
            self.stock.seek(0)
            self.file_content()
            self.stock.close()
            return False
        else:
            return True

    def file_content(self) -> dict:
        if len(self.stock.read()) != 0:
            self.stock.seek(0)
            stock_id = 0
            for line in self.stock.readlines():
                self.stock_dict[stock_id] = Producto(*line.split(','))
                stock_id += 1
        self.file_print()
        
    def file_find(self, product: str) -> list:
        for fid in self.stock_dict.keys():
            if product in self.stock_dict[fid].nombre_producto:
                return self.stock_dict[fid], fid
        raise NoProduct('No existe el producto en el stock')

    def file_add_update(self, product: str, precio: float, cantidad_vendida: int) -> object:
        try:
            objprod, fid = self.file_find(product)
            del self.stock_dict[fid]
            if cantidad_vendida != "": objprod.cantidad_vendida = int(cantidad_vendida)
            if precio != "": objprod.precio = float(precio)

        except NoProduct:
            if len(self.stock_dict.keys()) == 0:
                fid = 0
            else:
                fid = 0
                for keyid in self.stock_dict.keys():
                    if keyid > fid:
                        fid = keyid
                fid = keyid + 1
            objprod = Producto(product, cantidad_vendida, precio)

        finally:
            self.stock_dict[fid] = objprod
            self.file_uptade()

        return self.stock_dict[fid]

    def file_del(self, product) -> bool:
        try:
            objprod, fid = self.file_find(product)
            del self.stock_dict[fid]
            sorted(self.stock_dict)
        except NoProduct as baderror:
            print(f'{NoProduct.__name__}: {baderror}')
        finally:
            self.file_uptade()

        return True

    def file_close(self):
        self.file_uptade()
        self.stock.close()

    def file_print(self) -> print:
        for element in self.stock_dict.values():
            print(f'Producto: {element.nombre_producto}, Ventas: {element.cantidad_vendida}, Precio: {element.precio}')

    def file_uptade(self):
        self.stock = open(self.nombre_archivo, 'w', encoding='UTF-8')
        for objprod in self.stock_dict.values():
            self.stock.write(f'{objprod.nombre_producto}, {objprod.cantidad_vendida}, {objprod.precio}\n')

    def total_sells(self, products = []) -> float:
        print(products)
        print(type(products))
        print("melones" in products)
        print(len(products))
        if len(products) == 0:
            return sum([objprod.precio * objprod.cantidad_vendida for objprod in self.stock_dict.values()])
        else:
            return sum([objprod.precio * objprod.cantidad_vendida for objprod in self.stock_dict.values() if objprod.nombre_producto in products])
            

def main():
    first()
    my_file = Archivo(STOCK)
    menu = my_file.file_check()
    while True:
        if menu:
            print('\nEl archivo se ha creado nuevo.')
            print('Por favor seleccione una de las siguientes opciones:')
            menu = False
        else:
            print('\nPor favor seleccione una de las siguientes opciones:')
        
        print('1.- Añadir productos al stock.')
        print('2.- Encontrar productos en stock.')
        print('3.- Actualizar estado del producto en stock.')
        print('4.- Eliminar productos del stock.')
        print('5.- Imprimir stock.')
        print('6.- Imprimir Ventas Totales.')
        print('7.- Imprimir Ventas por productos.')
        print('0.- Salir del programa\n')
        option = input('OPCION>')

        match option:
            case "1":
                while True:
                    print('\nSi quiere terminar de introducir productos ingrese salir en el nombre del producto')
                    product = input('\nIngrese el nombre del producto: ').lower()
                    if product == "salir": break
                    productprice = input('Ingrese el precio del producto: ').lower()
                    productsells = input('Ingrese las ventas del producto: ').lower()
                    my_file.file_add_update(product, productprice, productsells)
            case "2":
                product = input('\nIngrese el producto a buscar: ').lower()
                try:
                    answer, ident = my_file.file_find(product)
                    print(f'\nEl producto {answer.nombre_producto} tiene un precio de {answer.precio} y se han vendido {answer.cantidad_vendida}', end =" ")
                    print(f'con unas ganancias de {answer.ventas():n}€')
                except NoProduct as baderror:
                    print(f'{NoProduct.__name__}: {baderror}')
                finally:
                    print('\nContinuamos con las operaciones.')
            case "3":
                product = input('\nIngrese el producto a actualizar: ').lower()
                productprice = input('Ingrese el precio del producto a actualizar: ').lower()
                productsells = input('Ingrese las ventas del producto a actualizar: ').lower()
                try:
                    answer = my_file.file_add_update(product, productprice, productsells)
                    print(f'\nEl producto {answer.nombre_producto} tiene un precio de {answer.precio} y se han vendido {answer.cantidad_vendida}', end =" ")
                    print(f'con unas ganancias de {answer.ventas():n}€')
                except NoProduct as baderror:
                    print(f'{NoProduct.__name__}: {baderror}')
                finally:
                    print('\nContinuamos con las operaciones.')
            case "4":
                product = input('\nIngrese el producto a eliminar: ').lower()
                my_file.file_del(product)
            case "5":
                my_file.file_print()
            case "6":
                print(f'\nVentas totales: {my_file.total_sells():n}€')
            case "7":
                products = input('\nIngrese el producto a eliminar, separados por ",": ').lower()
                products = products.strip().replace(", ", ",").split(",")
                print(f'Ventas totales de {products}: {my_file.total_sells(products):n}€')
            case "0":
                my_file.file_close()
                borrar = input('Desea borrar el archivo(yes/no):\n>').lower()
                while borrar != 'yes' and borrar != 'no':
                    borrar = input('Desea borrar el archivo(yes/no):\n>').lower()
                    print(borrar != 'yes' and borrar != 'no')
                if borrar == 'yes': os.remove(STOCK)
                break
            case _:
                print('\nSeleccione una opción correcta por favor.\n')

main()
serparacion('---')
