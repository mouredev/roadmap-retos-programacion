import os 
# /*
#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  *
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo que se llame como
#  * tu usuario de GitHub y tenga la extensión .txt.
#  * Añade varias líneas en ese fichero:
#  * - Tu nombre.
#  * - Edad.
#  * - Lenguaje de programación favorito.
#  * Imprime el contenido.
#  * Borra el fichero.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
#  * archivo .txt.
#  * - Cada producto se guarda en una línea del archivo de la siguiente manera:
#  *   [nombre_producto], [cantidad_vendida], [precio].
#  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#  *   actualizar, eliminar productos y salir.
#  * - También debe poseer opciones para calcular la venta total y por producto.
#  * - La opción salir borra el .txt.
#  */

file = open('rayn1er.txt','w')
file.write("Raul")
file.write("\n26")
file.write('\nPython')
file.close()
file = open('rayn1er.txt','r')
print(file.read())
file.close()
os.remove('rayn1er.txt')

#extra

store = open('store.txt','x')
store.close()

while True:
    print(f'''
        {"-" * 25}
        Gestor de Ventas
        {"-" * 25}
        Seleccione una opcion
        1 - Agregar producto
        2 - Actualizar producto
        3 - Consultar producto
        4 - Eliminar producto
        5 - Ver productos
        6 - Ver ventas totales
        7 - ver ventas por producto
        8 - Salir del Gestor
''')
    option = int(input("Seleccione una opcion -> "))

    if option == 1:
        product_name = input("Ingrese el nombre del producto -> ")
        product_sold = int(input("Ingrese la cantidad de elementos vendidos -> "))
        product_price = int(input("Ingrese el precio del producto -> "))
        with open('store.txt','a') as store:
            store.write(f'\n[{product_name}], [{product_sold}],[{product_price}]')
            print("Sus elementos han sido agregados a la lista")

    elif option == 2:
        pass
    
    elif option == 3:
        pass

    elif option == 4:
        pass

    elif option == 5:
        with open('store.txt','r') as store:
            print("Elementos en la lista")
            print(store.read())

    elif option == 6:
        pass

    elif option == 7:
        pass

    elif option == 8:
        print("Cerrando el gestor, hasta luego!")
        os.remove('store.txt')

    else:
        print("Seleccione una opcion valida ")

