import os

# ------ Ejercicio

FILENAME = "ycanas.txt"

with open(FILENAME, 'w', encoding="utf-8") as f:
    f.write("Yair Cañas\n")
    f.write("24\n")
    f.write("Python")

with open(FILENAME, 'r') as f:
    print(f.read())

os.remove(FILENAME)
print()


# ------ Extra

FILE = "ventas.txt"
OPTIONS = (
    "Añadir producto",
    "Consultar producto",
    "Consultar productos",
    "Actualizar producto",
    "Eliminar producto",
    "Calcular precio total",
    "Calcular precio por producto",
    "Salir"
)

open(FILE, 'a')
print("Bienvenido 👋")

while True:
    print()
    for i, option in enumerate(OPTIONS):
        print(f"   {i + 1}. {option}")

    option = input("\n> Ingrese el número correspondiente a la operación deseada: ")

    if not option.isdigit():
        print("\n* Error, debe ingresar un número entero.")
        continue

    option = int(option)

    if option == 1:
        product_name = input("\n> Nombre: ")
        product_quantity = input("> Cantidad: ")
        product_price = input("> Precio: ")

        with open(FILE, 'a', encoding="utf-8") as f:
            f.write(f"{product_name}, {product_quantity}, {product_price}\n")
            print("\n* Producto añadido.")

        continue

    elif option == 2:
        product_name = input("\n> Nombre: ")

        with open(FILE, 'r') as f:
            for line in f:
                if product_name == line.split(", ")[0]:
                    print("\n- " + line, end='')
                    break
            else:
                print("\n* Producto no encontrado.")
        
        continue

    elif option == 3:
        with open(FILE, 'r') as f:
            print()

            for line in f:
                if line == '':
                    break

                print('-', line, end='')
        
        continue

    elif option == 4:
        product_name = input("\n> Nombre: ")

        with open(FILE, 'r+', encoding='utf-8') as f:
            for line in f:
                data = line.split(", ")

                if product_name == data[0]:
                    new_product_name = input("\n> Nombre (enter para no cambiar): ")
                    new_product_quantity = input("> Cantidad (enter para no cambiar): ")
                    new_product_price = input("> Precio (enter para no cambiar): ")

                    if new_product_name == '':
                        new_product_name = data[0]

                    if new_product_quantity == '':
                        new_product_quantity = data[1]

                    if new_product_price == '':
                        new_product_price = data[2]

                    f.write(f"{new_product_name}, {new_product_quantity}, {new_product_price}\n")
                    print("\n* Producto Actualizado.")
                    break
            else:
                print("\n* Producto no encontrado.")

        continue

    elif option == 5:
        product_name = input("\n> Nombre: ")        

        with open(FILE, 'r') as f:
            lines = f.readlines()

        for line in lines:
            if line.split(", ")[0] == product_name:
                break

        else:
            print("\n* Producto no encontrado.")
            continue

        with open(FILE, 'w', encoding="utf-8") as f:
            for line in lines:
                if line.split(", ")[0] != product_name:
                    f.write(line)
        
        print("\n* Producto eliminado.")
        continue

    elif option == 6:
        with open(FILE, 'r') as f:
            total = 0

            for line in f:
                data = line.split(", ")
                quantity = float(data[1])
                price = float(data[2])

                total += quantity * price
        
        print(f"\n* Precio total del inventario: {total:,.2f} COP")
        continue

    elif option == 7:
        product_name = input("\n> Nombre: ")

        with open(FILE, 'r') as f:
            for line in f:
                data = line.split(", ")
                if product_name == data[0]:
                    quantity = float(data[1])
                    price = float(data[2])

                    total = quantity * price
            else:
                print("\n* Producto no encontrado.")

        print(f"\n* Precio total del inventario del producto: {total:,.2f} COP")
        continue

    elif option == 8:
        os.remove(FILE)
        print("\nSaliendo...")
        break

    else:
        print("\n* Error, debe ingresar un número entero entre 1 y 7.")
        continue
