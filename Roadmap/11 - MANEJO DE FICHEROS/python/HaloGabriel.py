import os

# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo que se llame como
# tu usuario de GitHub y tenga la extensión .txt.
# Añade varias líneas en ese fichero:
# - Tu nombre.
# - Edad.
# - Lenguaje de programación favorito.
# Imprime el contenido.
# Borra el fichero.

os.chdir(r'Roadmap\11 - MANEJO DE FICHEROS\python')

fichero = 'HaloGabriel.txt'

f = open(fichero, 'w')
f.close()

with open(fichero, 'a') as f:
    f.write('Gabriel\n')
    f.write('25\n')
    f.write('Java\n')

f = open(fichero)
content = f.read()
print(content)
f.close()

if os.path.exists(fichero):
    os.remove(fichero)
    print('Fichero eliminado')
print()

# DIFICULTAD EXTRA (opcional)
# Desarrolla un programa de gestión de ventas que almacena sus datos en un
# archivo .txt.
# - Cada producto se guarda en una línea del archivo de la siguiente manera:
# [nombre_producto], [cantidad_vendida], [precio].
# - Siguiendo ese formato, mediante terminal, debe permitir añadir, consultar,
#   actualizar, eliminar productos y salir.
# - También debe poseer opciones para calcular la venta total y por producto.
# - La opción salir borra el .txt.

print("=== PROGRAMA DE GESTIÓN DE VENTAS ===")

fichero = 'Productos.txt'

class Producto():
    def __init__(self, id: str, nom_prod: str,
                 cant_vend: int, precio: float):
        self.__id = id
        self.__nom_prod = nom_prod
        self.__cant_vend = cant_vend
        self.__precio = precio

    def get_id(self):
        return self.__id

    def get_nom_prod(self):
        return self.__nom_prod

    def get_cant_vend(self):
        return self.__cant_vend

    def get_precio(self):
        return self.__precio

    def set_nom_prod(self, nom_prod: str):
        self.__nom_prod = nom_prod

    def set_cant_vend(self, cant_vend: int):
        self.__cant_vend = cant_vend

    def set_precio(self, precio: float):
        self.__precio = precio

    def calcular_ventas(self):
        return self.__cant_vend * self.__precio

class ProductAlreadyExistsError(Exception):
    def __init__(self, id: str):
        super().__init__(f"Product with ID '{id}' already exists.")
        self.id = id

class ProductNotFoundError(Exception):
    def __init__(self, id: str):
        super().__init__(f"Product with ID '{id}' not found.")
        self.id = id

def obtener_productos():
    prod_list = []
    with open(fichero) as f:
        next(f)
        for line in f:
            prod_list.append(line[:-1])
    for i, producto in enumerate(prod_list):
        prod_list[i] = producto.split('|')
    for i, producto in enumerate(prod_list):
        prod_list[i] = Producto(producto[0].strip(), producto[1].strip(),
                                producto[2].strip(), producto[3].strip())
        prod_list[i].set_cant_vend(int(prod_list[i].get_cant_vend()))
        prod_list[i].set_precio(float(prod_list[i].get_precio()))
    return prod_list

def buscar_producto_por_id(id: str):
    for producto in prod_list:
        if producto.get_id() == id:
            return True
    return False

def agregar_producto():
    print("\n=== AGREGAR PRODUCTO ===")
    id = input("ID: ").strip()
    if id == '':
        raise ValueError('ID ingresado no puede estar vacío.')
    if buscar_producto_por_id(id):
        raise ProductAlreadyExistsError(id)
    nom_prod = input('Nom Prod: ').strip()
    if nom_prod == '':
        raise ValueError('Nombre ingresado no puede estar vacío.')
    cant_vend = input('Cant Vend: ').strip()
    if not cant_vend.isdigit():
        raise ValueError('Cantidad ingresada no es válida.')
    cant_vend = int(cant_vend)
    precio = input('Precio: ').strip()
    try:
        precio = float(precio)
    except ValueError:
        raise ValueError('Precio ingresado no es válido.')
    if precio <= 0:
        raise ValueError('Precio no puede ser cero o negativo.')

    prod_list.append(Producto(id, nom_prod, cant_vend, precio))

    actualizar_fichero()
    print(f'\n¡Nuevo producto \'{nom_prod}\' agregado!')

def actualizar_producto():
    print("\n=== ACTUALIZAR PRODUCTO ===")
    id = input('ID de producto a actualizar: ').strip()
    if id == '':
        id = None
    producto_found = obtener_producto(id)
    print("\n¡Producto encontrado!")

    print(f"\nNom Prod actual: {producto_found.get_nom_prod()}")
    nom_prod = input('Ingresar nuevo Nom Prod: ').strip()
    if nom_prod == '':
        raise ValueError('Nombre ingresado no puede estar vacío.')

    print(f"\nCant Vend actual: {producto_found.get_cant_vend()}")
    cant_vend = input('Ingresar nueva Cant Vend: ').strip()
    if not cant_vend.isdigit():
        raise ValueError('Cantidad ingresada no válida.')
    cant_vend = int(cant_vend)

    print(f"\nPrecio actual: ${producto_found.get_precio()}")
    precio = input('Ingresar nuevo Precio: ').strip()
    try:
        precio = float(precio)
    except ValueError:
        raise ValueError('Precio ingresado no es válido.')
    if precio <= 0:
        raise ValueError('Precio no puede ser cero o negativo.')

    producto_found_index = prod_list.index(producto_found)
    prod_list[producto_found_index].set_nom_prod(nom_prod)
    prod_list[producto_found_index].set_cant_vend(cant_vend)
    prod_list[producto_found_index].set_precio(precio)

    actualizar_fichero()
    print("\n¡Producto actualizado!")

def actualizar_fichero():
    with open(fichero, 'w') as f:
        f.write('ID | Nom Prod | Cant Vend | Precio\n')
    with open(fichero, 'a') as f:
        for producto in prod_list:
            f.write(f'{producto.get_id()} | {producto.get_nom_prod()} | '
                    f'{producto.get_cant_vend()} | {producto.get_precio()}\n')

def eliminar_producto():
    print("\n=== ELIMINAR PRODUCTO ===")
    id = input('ID de producto a eliminar: ').strip()
    if id == '':
        id = None
    producto_found = obtener_producto(id)

    prod_list.remove(producto_found)
    actualizar_fichero()
    print(f"\nProducto '{producto_found.get_nom_prod()}' eliminado.")

def imprimir_datos_producto(producto: Producto):
    print(f"ID: {producto.get_id()}")
    print(f"Nombre: {producto.get_nom_prod()}")
    print(f"Cantidad Vendida: {producto.get_cant_vend()}")
    print(f"Precio: ${producto.get_precio()}")

def obtener_producto(id: str = ''):
    if id == '':
        id = input('ID de producto a buscar: ').strip()
    if not buscar_producto_por_id(id):
        raise ProductNotFoundError(id)
    for producto in prod_list:
        if producto.get_id() == id:
            return producto

def calcular_venta_total():
    total = 0.0
    for producto in prod_list:
        total += producto.calcular_ventas()
    print(f'\nVentas totales: ${total:.2f}')

def calcular_ventas_por_producto():
    producto_found = obtener_producto()
    print("\n¡Producto encontrado!")
    print(f"Nombre: {producto_found.get_nom_prod()}")
    print(f"Venta de producto: ${producto_found.calcular_ventas():.2f}")

def calcular_ventas():
    print("\n=== CALCULAR VENTAS ===")
    print("Puede calcular:")
    print("1. 'total' para venta total.")
    print("2. 'producto' para ventas por producto.")

    operacion = input("Ingresar tipo de venta: ").lower().strip()
    match operacion:
        case 'total':
            calcular_venta_total()
        case 'producto':
            calcular_ventas_por_producto()
        case _:
            print('\nTipo de venta ingresado no válido.')

def listar_productos():
    print("\n=== LISTADO DE PRODUCTOS ===")
    for producto in prod_list:
        print(f"\nID: {producto.get_id()}")
        print(f"Nom Prod: {producto.get_nom_prod()}")
        print(f"Cant Vend: {producto.get_cant_vend()}")
        print(f"Precio: {producto.get_precio()}")

prod_list = [
    Producto('001', "Lata de sardinas", 4, 10.99),
    Producto('002', "Lata de espinacas", 10, 29.99),
    Producto('003', "Lata de tomates", 1, 20.99)
]

actualizar_fichero()

while True:
    print("\nOperaciones disponibles:")
    print("1. 'agregar' para añadir un nuevo producto.")
    print("2. 'listar' para listar todos los productos.")
    print("3. 'consultar' para buscar un producto.")
    print("4. 'actualizar' para actualizar un producto.")
    print("5. 'eliminar' para eliminar un producto.")
    print("6. 'ventas' para calcular ventas.")
    print("7. 'salir' para salir del programa.")

    operacion = input("Ingresar operación: ").lower().strip()
    match operacion:
        case 'agregar':
            try:
                agregar_producto()
            except ProductAlreadyExistsError as error:
                print(f"Error: {error}")
            except ValueError as error:
                print(f"Error: {error}")
            except Exception as error:
                print(f"Unknown error: {error}")
        case 'listar':
            listar_productos()
        case 'consultar':
            try:
                print("\n=== CONSULTAR PRODUCTO ===")
                producto_found = obtener_producto()
                print("\n¡Producto encontrado!")
                imprimir_datos_producto(producto_found)
            except ProductNotFoundError as error:
                print(f"Error: {error}")
            except Exception as error:
                print(f"Unknown error: {error}")
        case 'actualizar':
            try:
                actualizar_producto()
            except ProductNotFoundError as error:
                print(f"Error: {error}")
            except Exception as error:
                print(f"Unknown error: {error}")
        case 'eliminar':
            try:
                eliminar_producto()
            except ProductNotFoundError as error:
                print(f"Error: {error}")
            except Exception as error:
                print(f"Unknown error: {error}")
        case 'ventas':
            try:
                calcular_ventas()
            except ProductNotFoundError as error:
                print(f"Error: {error}")
            except Exception as error:
                print(f"Unknown error: {error}")
        case 'salir':
            if os.path.exists(fichero):
                os.remove(fichero)
                print('\nFichero de productos eliminado')
            break
        case _:
            print("\nOperación ingresada no válida")

print("Gracias vuelva pronto")