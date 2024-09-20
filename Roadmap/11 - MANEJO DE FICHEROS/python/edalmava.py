import os

github_username = "edalmava"

filename = f"{github_username}.txt"

name = "Edwin Alberto Martinez Vanegas"
age = "30"
favorite_language = "Python"

# Crear y escribir en el archivo
with open(filename, 'w') as file:
    file.write(f"Nombre: {name}\n")
    file.write(f"Edad: {age}\n")
    file.write(f"Lenguaje de programación favorito: {favorite_language}\n")

# Leer y mostrar el contenido del archivo
with open(filename, 'r') as file:
    content = file.read()
    print("Contenido del archivo:")
    print(content)

# Borrar el archivo
os.remove(filename)
print(f"Archivo '{filename}' ha sido borrado.")

print("*****RETO EXTRA*****")

# Define el nombre del archivo
filename = "ventas.txt"

def load_products():
    """Carga los productos desde el archivo."""
    products = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():  # Verifica que la línea no esté vacía
                    name, quantity, price = line.strip().split(', ')
                    products[name] = {'quantity': int(quantity), 'price': float(price)}
    return products

def save_products(products):
    """Guarda los productos en el archivo."""
    with open(filename, 'w') as file:
        for name, details in products.items():
            file.write(f"{name}, {details['quantity']}, {details['price']}\n")

def add_product(products):
    """Añade un nuevo producto."""
    name = input("Nombre del producto: ")
    quantity = int(input("Cantidad vendida: "))
    price = float(input("Precio: "))
    products[name] = {'quantity': quantity, 'price': price}
    save_products(products)
    print("Producto añadido.")

def view_products(products):
    """Muestra todos los productos."""
    if products:
        for name, details in products.items():
            print(f"{name}: Cantidad - {details['quantity']}, Precio - {details['price']}")
    else:
        print("No hay productos.")

def update_product(products):
    """Actualiza un producto existente."""
    name = input("Nombre del producto a actualizar: ")
    if name in products:
        quantity = int(input("Nueva cantidad vendida: "))
        price = float(input("Nuevo precio: "))
        products[name] = {'quantity': quantity, 'price': price}
        save_products(products)
        print("Producto actualizado.")
    else:
        print("Producto no encontrado.")

def delete_product(products):
    """Elimina un producto."""
    name = input("Nombre del producto a eliminar: ")
    if name in products:
        del products[name]
        save_products(products)
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def total_sales(products):
    """Calcula la venta total."""
    total = sum(details['quantity'] * details['price'] for details in products.values())
    print(f"Venta total: {total:.2f}")

def sales_by_product(products):
    """Calcula la venta por producto."""
    name = input("Nombre del producto: ")
    if name in products:
        details = products[name]
        total = details['quantity'] * details['price']
        print(f"Venta del producto '{name}': {total:.2f}")
    else:
        print("Producto no encontrado.")

def main():
    products = load_products()
    
    while True:
        print("\nOpciones:")
        print("1. Añadir producto")
        print("2. Consultar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Calcular venta total")
        print("6. Calcular venta por producto")
        print("7. Salir")

        choice = input("Seleccione una opción (1-7): ")

        if choice == '1':
            add_product(products)
        elif choice == '2':
            view_products(products)
        elif choice == '3':
            update_product(products)
        elif choice == '4':
            delete_product(products)
        elif choice == '5':
            total_sales(products)
        elif choice == '6':
            sales_by_product(products)
        elif choice == '7':
            os.remove(filename)
            print("Archivo eliminado. Saliendo...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
