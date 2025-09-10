'''
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
   tu usuario de GitHub y tenga la extensión .txt.
   Añade varias líneas en ese fichero:
   - Tu nombre.
   - Edad.
   - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
   archivo .txt.
   - Cada producto se guarda en una línea del archivo de la siguiente manera:
     [nombre_producto], [cantidad_vendida], [precio].
   - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
     actualizar, eliminar productos y salir.
   - También debe poseer opciones para calcular la venta total y por producto.
   - La opción salir borra el .txt.
'''

import os

file = "jesusgdev.txt"

with open(file, "w", encoding="utf-8") as archivo:
    archivo.write("Nombre: Jesus Garcia\n" + "Edad: 41\n" + "Lenguaje favorito: Pyhton")

with open(file, "r", encoding="utf-8") as archivo:
    content = archivo.read()
    print("Contenido del archivo:\n" + content)

os.remove(file)
print(f"\nEl archivo '{file}' ha sido eliminado")

'''
Extra
'''

# 📦 Importamos el módulo 'os' que nos permite trabajar con archivos del sistema (como crear, borrar, verificar si existen, etc.)
import os

# 🧾 Función principal del programa de gestión de ventas
def sales_managment():
    # 📂 Nombre del archivo donde se almacenarán los productos
    file = "sale_managment_book.txt"

    # 🔁 Iniciamos un bucle infinito que mostrará el menú hasta que el usuario elija salir
    while True:
        
        # 🧭 Menú principal
        print("\n🛒 GESTOR DE VENTAS")
        print("1️⃣ Añadir producto")
        print("2️⃣ Consultar productos")
        print("3️⃣ Actualizar producto")
        print("4️⃣ Eliminar producto")
        print("5️⃣ Ver ventas totales")
        print("6️⃣ Salir y eliminar archivo")

        # 🧠 Solicitamos al usuario que seleccione una opción del menú
        option = input("\n🔽 Seleccione una opción (1-6): ")

        # 🧩 Usamos 'match' para manejar la opción seleccionada (como un menú inteligente)
        match option:

            # ➕ OPCIÓN 1: Añadir producto
            case "1":
                product_name = input("📌 Ingrese el nombre del producto: ")
                quantity_units_sold = input("📦 Ingrese la cantidad de unidades vendidas: ")
                unit_price = input("💲 Ingrese el precio de venta unitario: ")

                # ✍️ Abrimos el archivo en modo "agregar" (append) y escribimos los datos
                with open(file, "a", encoding="utf-8") as archivo:
                    archivo.write(f"{product_name},{quantity_units_sold},{unit_price}\n")
                    print("✅ Producto agregado exitosamente.")

            # 📄 OPCIÓN 2: Consultar productos
            case "2":
                if not os.path.exists(file):
                    print("⚠️ No hay productos registrados aún.")
                    return

                with open(file, "r", encoding="utf-8") as archivo:
                    lines = archivo.readlines()
                    
                    if len(lines) == 0:
                        print("📭 El archivo está vacío. No hay productos registrados.")
                    else:
                        print("\n📋 LISTA DE PRODUCTOS REGISTRADOS:")
                        for line in lines:
                            product_name, quantity_units_sold, unit_price = line.strip().split(",")
                            print(f"🔹 Nombre: {product_name} | Unidades: {quantity_units_sold} | Precio Unitario: ${unit_price}")

            # 🛠️ OPCIÓN 3: Actualizar producto
            case "3":
                update_name_product = input("📝 Ingrese el nombre del producto que desea actualizar: ")
                updated = False

                if not os.path.exists(file):
                    print("⚠️ No hay productos registrados aún.")
                    return
                
                with open(file, "r", encoding="utf-8") as archivo:
                    lines = archivo.readlines()

                # 🧽 Reescribimos el archivo con la información actualizada
                with open(file, "w", encoding="utf-8") as archivo:
                    for line in lines:
                        product_name, quantity_units_sold, unit_price = line.strip().split(",")
                        if update_name_product == product_name:
                            update_quantity_units_sold = input("🔁 Nueva cantidad de unidades vendidas: ")
                            update_unit_price = input("🔁 Nuevo precio unitario: ")
                            archivo.write(f"{product_name},{update_quantity_units_sold},{update_unit_price}\n")
                            updated = True
                        else:
                            archivo.write(line)
                            
                    if not updated:
                        print(f"❌ El producto '{update_name_product}' no fue encontrado. No se realizaron cambios.")

            # 🗑️ OPCIÓN 4: Eliminar producto
            case "4":
                remove_name_product = input("🗑️ Ingrese el nombre del producto que desea eliminar: ")
                removed = False

                if not os.path.exists(file):
                    print("⚠️ No hay productos registrados aún.")
                    return
                
                with open(file, "r", encoding="utf-8") as archivo:
                    lines = archivo.readlines()

                with open(file, "w", encoding="utf-8") as archivo:
                    for line in lines:
                        product_name, quantity_units_sold, unit_price = line.strip().split(",")
                        if remove_name_product != product_name:
                            archivo.write(line)
                        else:
                            removed = True
                            print(f"✅ El producto '{remove_name_product}' ha sido eliminado del registro.")

                if not removed:
                    print(f"❌ El producto '{remove_name_product}' no fue encontrado. No se eliminaron productos.")

            # 💰 OPCIÓN 5: Ver ventas totales
            case "5":
                if not os.path.exists(file):
                    print("⚠️ No hay productos registrados aún.")
                    return

                with open(file, "r", encoding="utf-8") as archivo:
                    lines = archivo.readlines()
                    
                    if len(lines) == 0:
                        print("📭 El archivo está vacío. No hay ventas registradas.")
                    else:
                        print("\n📈 VENTAS TOTALES POR PRODUCTO:")
                        quantity_sold = 0
                        for line in lines:
                            product_name, quantity_units_sold, unit_price = line.strip().split(",")
                            quantity_sold_per_product = int(quantity_units_sold) * int(unit_price)
                            quantity_sold += quantity_sold_per_product
                            print(f"🔸 {product_name}: ${quantity_sold_per_product}")
                        print(f"\n💵 TOTAL GENERAL DE VENTAS: ${quantity_sold}")
                        return  # Finaliza la función después de mostrar las ventas

            # 🚪 OPCIÓN 6: Salir y eliminar archivo
            case "6":
                os.remove(file)
                print(f"\n🗃️ El archivo '{file}' ha sido eliminado correctamente. ¡Hasta pronto!")
                break  # Salimos del bucle para terminar el programa

# ▶️ Ejecutamos la función
sales_managment()
