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
 
from pathlib import Path
import os
    
def GetCurrentDirectory():
    return os.getcwd()

def CreateFile(path: str, text = []):
    if len(text) > 0:
        with open(path, "w") as file:
            for t in text:
                file.write(str(t)+"\n")

def ReadFile(path: str):
    if os.path.exists(path):
        file = Path(path)
        texto = file.read_text("utf-8")
        return texto
    else:
        return "No existe el archivo en la ruta especificada"
    
def DeleteFlle(path: str):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("No existe el archivo en la ruta especificada")


# EXTRA
class  Warehouse:
    def __init__(self, oid, name, items = []):
        self.oid = oid
        self.name = name
        self.products = []
        self.products.extend(items)
    
    def AddProduct(self, newProduct):
        self.products.append(newProduct)
    
    def UpdateProduct(self, oid, name = None, price = None, quantity = None, soldUnits = None):
        p = self.GetProduct(oid)
        if p != None:
            p.name = name if name != None else p.name
            p.priceByUnit = price if price != None else p.priceByUnit
            p.quantity = quantity if quantity != None else p.quantity
            p.soldUnits = soldUnits if soldUnits != None else p.soldUnits
        return p

    def GetProduct(self, oid: int):
        l = list(map(lambda x: x.oid == oid, self.products))
        index = l.index(True)
        p = self.products[index]
        return p

    def GetProducts(self):
        print(*(p for p in self.products), sep='\n')
    
    def DelteItem(self, oid: int):
        p = self.GetProduct(oid)
        if p in self.products: 
            self.products.remove(p)
        


class Product:
    def __init__(self, oid, name, priceByUnit, quantity, soldUnits: int = 0):
        self.oid = oid
        self.name = name
        self.priceByUnit = priceByUnit
        self.quantity = quantity
        self.soldUnits = soldUnits
    
    def __str__(self):
        return f"El producto {self.name} tiene un precio de {self.priceByUnit}€ por unidad, en el almacén quedan {self.quantity} unidades y ha vendido {self.soldUnits} unidades."
        
    
    


if __name__ == "__main__":
    current_directory = GetCurrentDirectory()
    print(current_directory)
    CreateFile(f"{current_directory}\elbarbero.txt", ["Mario Barbero", 35, "Python"])
    text = ReadFile(f"{current_directory}\elbarbero.txt")
    print(text)
    DeleteFlle((f"{current_directory}\elbarbero.txt"))
    
    # EXTRA
    almacen = Warehouse(1, "Almacen Burgos", [Product(1, "Chorizo", 1.65, 100, 25), Product(2, "Aceite Oliva 1L", 7.79, 550), Product(3, "Yogures", 1.90, 80), Product(4, "Pizza", 2.90, 185)])
    almacen.UpdateProduct(oid=3, name="Nuevo nombre")
    print(almacen.GetProduct(1))
    text = []
    text.extend(str(p) for p in almacen.products)
    
    CreateFile(f"{current_directory}\elbarbero.txt", text)
    DeleteFlle((f"{current_directory}\elbarbero.txt"))
