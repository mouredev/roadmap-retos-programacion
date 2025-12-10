# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo que se llame como
# tu usuario de GitHub y tenga la extensión .txt.
# Añade varias líneas en ese fichero:
# - Tu nombre.
# - Edad.
# - Lenguaje de programación favorito.
# Imprime el contenido.
# Borra el fichero.
import os

user = "cristianfloyd"
file_name = f"{user}.txt"

with open(file_name, "w") as file:
    file.write("Cristian Floyd\n")
    file.write("48\n")
    file.write("Python\n")

with open(file_name, "r") as file:
    content = file.read()
    print(content)

os.remove(file_name)


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


class Product:
    """
    Clase que representa un producto.
    """
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name.strip()
        self.quantity = int(quantity)
        self.price = float(price)
        self.verificar_parametros()

    def verificar_parametros(self):
        """Valida los parámetros del producto."""
        if not self.name:
            raise ValueError("El nombre del producto no puede estar vacío")
        
        if self.quantity < 0:
            raise ValueError("La cantidad no puede ser negativa")
        
        if self.price < 0:
            raise ValueError("El precio no puede ser negativo")

    def to_file_format(self):
        return f"{self.name}, {self.quantity}, {self.price}\n"

    @staticmethod
    def from_file_line(line: str) -> "Product":
        """Desde una linea del archivo, crea un objeto Product."""
        parts = [p.strip() for p in line.strip().split(",")]
        if len(parts) != 3:
            raise ValueError(f"Formato inválido en línea: {line}")
        return Product(parts[0], int(parts[1]), float(parts[2]))
    
    def calcular_total(self) -> float:
        """Calcula el total del producto."""
        return self.quantity * self.price

class ProductManager:
    """
    Clase para gestionar productos en un archivo de texto.
    """
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def read_products(self) -> list[Product]:
        """Lee los productos del archivo."""
        products = []
        if not os.path.exists(self.file_name):
            return products
        try:
            with open(self.file_name, "r") as file:
                for line in file.readlines():
                    line = line.strip()
                    products.append(Product.from_file_line(line))
                return products
        except FileNotFoundError as e:
            print(f"Error al leer el archivo: {e}")
            return []

    def write_products(self, products: list[Product]) -> None:
        """Escribe los productos en el archivo."""
        try:
            with open(self.file_name, "w") as file:
                for product in products:
                    file.write(product.to_file_format())
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error al escribir el archivo: {e}")

    def add_product(self, product: Product) -> None:
        """Añade un producto al archivo."""
        with open(self.file_name, "a") as file:
            file.write(product.to_file_format())

    def get_product(self, name:str) -> Product | None:
        """Obtiene un producto por su nombre."""
        products = self.read_products()
        for product in products:
            if product.name == name:
                return product
        return None

    def delete_product(self, name:str) -> bool:
        """Elimina un producto por su nombre."""
        products = self.read_products()
        cantidad_original = len(products)
        products = [product for product in products if product.name != name]
        cantidad_final = len(products)
        if cantidad_original > cantidad_final:
            self.write_products(products)
            return True
        return False

    def update_product(self, product: Product) -> bool:
        """Actualiza un producto en el archivo."""
        productos = self.read_products()
        for producto in productos:
            if producto.name == product.name:
                producto.quantity = product.quantity
                producto.price = product.price
                self.write_products(productos)
                return True
        return False

    def get_all_products(self) -> list[Product]:
        """Obtiene todos los productos."""
        return self.read_products()

    def calcular_venta_total(self) -> float:
        """Calcula la venta total de los productos."""
        products = self.read_products()
        return sum([p.calcular_total() for p in products])

    def calcular_venta_por_producto(self, name:str) -> float:
        """Calcula la venta total de un producto."""
        product = self.get_product(name)
        if product:
            return product.calcular_total()
        return 0

class ShopApp:
    """
    Clase principal de la aplicación de gestión de productos.
    """
    def __init__(self, manager: ProductManager) -> None:
        self.manager = manager

    def run(self):
        file_name = "cristianfloyd_shop.txt"

        open(file_name, "a")

        while True:
            print("1. Añadir producto")
            print("2. Consultar producto")
            print("3. Actualizar producto")
            print("4. Borrar producto")
            print("5. Mostrar productos")
            print("6. Calcular venta total")
            print("7. Calcular venta por producto")
            print("8. Salir")

            option = input("Selecciona una opción: ")

            match option:
                case "1":
                    self.add_product_flow()
                case "2":
                    self.buscar_producto_flow()
                case "3":
                    self.update_product_flow()
                case "4":
                    self.borrar_producto_flow()
                case "5":
                    self.mostrar_productos_flow()
                case "6":
                    self.calcular_venta_total_flow()
                case "7":
                    self.calcular_venta_por_producto_flow()
                case "8":
                    self.exit_flow()

    def add_product_flow(self):
        name = input("Nombre: ").strip()
        quantity = int(input("Cantidad: ").strip())
        price = float(input("Precio: ").strip())
        try:
            product = Product(name, quantity, price)
            self.manager.add_product(product)
            print("Producto añadido.")
        except ValueError as e:
            print(f"Error al añadir producto: {e}")

    def buscar_producto_flow(self):
        name = input("Nombre: ").strip()
        producto = self.manager.get_product(name)
        if producto:
            print("\nProducto encontrado:")
            print(f"  Nombre: {producto.name}")
            print(f"  Cantidad: {producto.quantity}")
            print(f"  Precio: {producto.price}")
            print(f"  Total: {producto.calcular_total()}")
        else:
            print(f"Error: Producto '{name}' no encontrado.")

    def update_product_flow(self):
        name = input("Nombre: ").strip()
        quantity = int(input("Cantidad: ").strip())
        price = float(input("Precio: ").strip())

        producto = Product(name, quantity, price)

        try:
            self.manager.update_product(producto)
            print("Producto actualizado.")
        except ValueError as e:
            print(f"Error al actualizar producto: {e}")

    def borrar_producto_flow(self) -> None:
        name = input("Nombre: ").strip()
        if self.manager.delete_product(name):
            print("Producto borrado correctamente.")
        else:
            print(f"Error: Producto '{name}' no encontrado.")

    def mostrar_productos_flow(self):
        """flujo para mostrar todos los productos."""
        productos = self.manager.get_all_products()
        if productos:
            print("\n === Productos: ===")
            for producto in productos:
                print(f"{producto.name}, {producto.quantity}, {producto.price}")
            print(f"\nTotal de productos: {len(productos)}\n")
        else:
            print("No hay productos registrados.")

    def calcular_venta_total_flow(self):
        """flujo para calcular la venta total."""
        total = self.manager.calcular_venta_total()
        print(f"La venta total es: {total}")

    def calcular_venta_por_producto_flow(self):
        """flujo para calcular la venta total de un producto."""
        name = input("Nombre: ").strip()
        total = self.manager.calcular_venta_por_producto(name)
        print(f"La venta total de {name} es: {total}")

    def exit_flow(self):
        os.remove(self.manager.file_name)
        print("Archivo eliminado. Saliendo...")
        exit()


if __name__ == "__main__":
    tienda = ShopApp(ProductManager("cristianfloyd_shop.txt"))
    tienda.run()