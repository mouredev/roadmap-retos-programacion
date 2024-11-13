import os

text = """Jheison Duban Quiroga Quintero
26
Python"""

with open("JheisonQuiroga.txt", "w") as f:
    f.write(text)
    
file = "JheisonQuiroga.txt"

with open(file) as f:
    if os.path.exists("./JheisonQuiroga.txt"):
        text = f.read()
        print(text)
    else:
        print("The file is not exists")


""" Extra """

my_file = "sells.txt"
products = []


def add_product(name:str, sell_total:int, price:int):
    if not os.path.exists(my_file):
        with open(my_file, "x") as file:
            file.write(f"{name}, {sell_total}, {price}\n")
            products.append({
                "name": name,
                "sell_total": sell_total,
                "price": price
            })
    else:
        with open(my_file, "a") as file:
            file.write(f"{name}, {sell_total}, {price}\n")
            products.append({
                "name": name,
                "sell_total": sell_total,
                "price": price
            })


def get_info():
    print("-" * 5, "Inventario", "-" * 5)
    for dct in products:
        print(f"{dct['name']}, {dct['sell_total']}, {dct['price']}")


def update(name, new_item_sell, new_price):
    with open(my_file, "w") as file:
        for product in products:
            if product["name"] == name:
                product["sell_total"] = new_item_sell
                product["price"] = new_price
            file.write(f"{product["name"]}, {product["sell_total"]}, {product["price"]}\n")

def remove_products(name):
    global products # Para asegurarme de borrar la lista original

    filter_products = [product for product in products if product["name"] != name]

    products = filter_products
    # Sobreescribe el archivo con los productos filtrados
    with open(my_file, "w") as file:
        for product in products:
            file.write(f"{product['name']}, {product['sell_total']}, {product['price']}\n")

def get_product():
    name = input("Nombre del producto: ")
    item_sell = int(input("Total de ventas: "))
    price = int(input("Precio: "))
    return name, item_sell, price

def sales_calculate():
    global products
    total_sales = 0
    for product in products:
        total_sale_per_product = product["sell_total"] * product["price"]
        total_sales += total_sale_per_product

    return total_sales

def remove_file(): # Funcion para borrar archivo al salir
    if os.path.exists(my_file):
        os.remove(my_file)
        print("El archivo ha sido borrado!")


def main():

    while True:
        option = int(input("""----- Sistema de Gestión de ventas -----
        1. Agregar producto
        2. Consultar inventario
        3. Actualizar
        4. Eliminar producto
        5. Total ventas
        6. Venta por producto
        7. Salir
        Elige una opcion: """))

        match option:
            case 1:
                name, item_sell, price = get_product()
                add_product(name, item_sell, price)
            case 2:
                get_info()
            case 3:
                name, item_sell, price = get_product()
                update(name, item_sell, price)
            case 4:
                name = input("Ingrese el nombre del producto a eliminar")
                remove_products(name)
            case 5:
                print(sales_calculate())
            case 6:
                name = input("Nombre del producto: ")
                with open(my_file, "r") as file:
                    for line in file.readlines():
                        components = line.split(", ")
                        if name == components[0]:
                            quantity = int(components[1])
                            price = int(components[2])
                            total = quantity * price
                            print(total)
                            break
                        
            case 7:
                remove_file()
                print("Saliendo del programa...")
                return


main()