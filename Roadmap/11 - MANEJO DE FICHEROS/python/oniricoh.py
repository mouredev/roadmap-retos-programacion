
#Abrimos archivo en modo escritura
archivo = open(r"11 Manejo de ficheros\archivo.txt", "w")
archivo.write("Nombre: Daniel\nEdad: 34\nLenguaje de programación: Python")
archivo.close()

#Arbimos archivo en modo lectura
archivo = open(r"11 Manejo de ficheros\archivo.txt", "r")
print(archivo.read())
archivo.close()

#salto de linea
print()

#Para escribir en un archivo existente sin borrar su contenido previo
with open(r"11 Manejo de ficheros\archivo.txt", "a") as archivo:
    archivo.write("\nEste es un nuevo contenido agregado al final.")

# No es necesario cerrar el archivo explícitamente aquí, se cerrará automáticamente al salir del bloque 'with'
with open(r"11 Manejo de ficheros\archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#salto de linea
print()

#Leyendo un archivo linea por linea
with open(r"11 Manejo de ficheros\archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea)

print()
print()
print()

###############################################################################
## DIFICULTAD EXTRA: Programa de ventas
###############################################################################

class SalesManagement:
    """Clase para gestionar las ventas y productos."""
    
    def __init__(self, file) -> None:
        """Inicializa la instancia de SalesManagement.
        
        Args:
            file (str): Ruta del archivo que contiene los datos de los productos.
        """
        self.file = file
    
    def __str__(self) -> str:
        """Devuelve una representación en cadena de los productos y las ventas totales."""
        try:
            with open(self.file, "r") as items:
                content = items.read()
                total_sales = self.total_sales(items)
                string_output = f"{content}\nTotal de ventas y beneficios:\n  - Vendidos: {total_sales['Total vendidos']}\n  - Beneficios: {total_sales['Total Beneficios']}"
                return string_output    
        except FileNotFoundError:
            return f"El archivo {self.file} aún no ha sido creado, agrega algún artículo para comenzar"

    def add_product(self, product_name, price, quantity_sold=0, profit=0):
        """Añade un nuevo producto al archivo.
        
        Args:
            product_name (str): Nombre del producto.
            price (float): Precio del producto.
            quantity_sold (int, optional): Cantidad vendida del producto. Defaults to 0.
            profit (float, optional): Beneficio del producto. Defaults to 0.
        """
        lines = self._read_lines()
        product = f"Nombre del producto: {product_name}, Precio: {price}, Cantidad vendida: {quantity_sold}, Beneficio: {profit}\n"
        if any(product_name in line for line in lines):
            print("No se puede agregar el producto porque ya ha sido agregado anteriormente.")
            return
        else:
            lines.append(product)
        self._write_lines(lines)
        print(f"Se ha agregado '{product_name}' al listado de productos.")
        
    def update_product(self, product_name, price, quantity_sold=0, profit=0):
        """Actualiza la información de un producto existente en el archivo.
        
        Args:
            product_name (str): Nombre del producto a actualizar.
            price (float): Nuevo precio del producto.
            quantity_sold (int, optional): Cantidad vendida adicional del producto. Defaults to 0.
            profit (float, optional): Nuevo beneficio del producto. Defaults to 0.
        """
        lines = self._read_lines()
        found = False
        for i, line in enumerate(lines):
            if product_name in line:
                product_data = line.split(", ")
                product_data[1] = f"Precio: {price}"
                product_data[2] = f"Cantidad vendida: {int(product_data[2].split(': ')[-1]) + quantity_sold}"
                product_data[3] = f"Beneficio: {float(product_data[1].split(': ')[-1]) * int(product_data[2].split(': ')[-1])}"
                lines[i] = ", ".join(product_data) + "\n"
                found = True
                break   
        if not found:
            print(f"El producto '{product_name}' no existe o no ha sido creado.")
            return
        self._write_lines(lines)
        print(f"Se ha actualizado el producto: {product_name}.")    
    
    def total_sales(self, items):
        """Calcula el total de ventas y beneficios.
        
        Args:
            items (file): Objeto de archivo que contiene los datos de los productos.
        
        Returns:
            dict: Diccionario con el total de ventas y beneficios.
        """
        lines = items.readlines()
        total = {"Total vendidos": 0, "Total Beneficios": 0}
        for line in lines:
            product_data = line.split(", ")
            total["Total vendidos"] += int(product_data[2].split(": ")[-1])
            total["Total Beneficios"] += float(product_data[3].split(": ")[-1])
        return total 

    def remove_product(self, product_name):
        """Elimina un producto del archivo.
        
        Args:
            product_name (str): Nombre del producto a eliminar.
        """
        lines = self._read_lines()
        updated_lines = [line for line in lines if product_name not in line]
        self._write_lines(updated_lines)
        if len(lines) != len(updated_lines):
            print(f"Se ha eliminado el producto '{product_name}'.")
        else:
            print(f"El producto '{product_name}' no está registrado")

    def _read_lines(self):
        """Lee las líneas del archivo de productos.
        
        Returns:
            list: Lista de líneas del archivo.
        """
        try:
            with open(self.file, "r") as items:
                return items.readlines()
        except FileNotFoundError:
            return []

    def _write_lines(self, lines):
        """Escribe las líneas en el archivo de productos.
        
        Args:
            lines (list): Lista de líneas a escribir en el archivo.
        """
        with open(self.file, "w") as items:
            items.writelines(lines)


class IncorrectSelection(Exception):
    """Excepción para manejar selecciones incorrectas."""
    pass                

def main():
    file = r"11 Manejo de ficheros\articulos.txt"
    sales = SalesManagement(file)
    
    while True:
        print("\n\nMenu Principal")
        print("1.- Añadir un nuevo producto")
        print("2.- Consultar listado de productos")
        print("3.- Actualizar un producto")        
        print("4.- Eliminar un producto")
        print("5.- Salir del programa")
        try:
            select = int(input("\nSelecciona la opción deseada (1, 2, 3, 4 o 5): "))
            
            if select < 1 or select > 5:
                raise IncorrectSelection("Selecciona una opción válida.")
            
            elif select == 1:
                print("\n¿Qué producto quieres agregar?")
                product = input("Nombre del producto: ")
                price = float(input("Precio del producto: "))
                sales.add_product(product, price)
            
            elif select == 2:
                print("\nListado de productos:")
                print(sales)
            
            elif select == 3:
                print("\n¿Qué producto quieres actualizar?")
                product = input("Nombre del producto: ")
                price = float(input("Precio del producto: "))
                sale = int(input("Cantidad vendida: "))
                sales.update_product(product, price, sale)
            
            elif select == 4:
                print("\n¿Qué producto quieres eliminar?")
                product = input("Nombre del producto: ")
                sales.remove_product(product)
            
            elif select == 5:
                break
                                        
        except ValueError:
            print("Error: Por favor, introduce un número válido.")
        except IncorrectSelection as err:
            print("Error:", err)

if __name__ == "__main__":
    main()
