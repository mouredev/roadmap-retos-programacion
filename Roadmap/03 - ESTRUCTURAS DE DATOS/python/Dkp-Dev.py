"""
EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 """

# Listas

lista: list = ["Perro","Gato","Conejo","Tortuga"]     # Es una lista definida por []
print(type(lista))
print(lista)

lista.append("Cuervo")  # Insercion
print(lista)

lista.remove("Gato")    # Eliminacion
print(lista)

print(lista[2])         # Acceso

lista[2] = "Serpiente"  # Modificacion en posicion
print(lista)

lista.sort()            # Orden alfabetico por defecto
print(lista)

# Tuplas son listas inmutables

tupla = ("Numeros","Letras","Simbolos")         # Es una tupla definida por () a diferencia de la lista []
print(type(tupla))
print(tupla)

print(tupla[2])         # Acceso unicamente
print(tupla[0])

tupla = tuple(sorted(tupla))    # Ordenar una tupla consiste en crear una lista a partir de la tupla, ordenarla y transformarla a tupla nuevamente
print(type(tupla))
print(tupla)

# Sets son basicamente listas desordenadas con el proposito de ser "eficientes" y no permite datos duplicados

sett: set = {"Cuadrado","Circulo","Rectangulo","Triangulo"}
print(type(sett))
print(sett)

sett.add("Ovalo")            # Insercion
sett.add("Cuadrado")         # Aunque se inserte nuevamente un dato, el sistema no lo tomara en cuenta
print(sett)

sett.remove("Rectangulo")    # Eliminacion
print(sett)                  # La unica forma de "modificar" es mediante la insercion y eliminacion de dato

sett = set(sorted(sett))     # No se puede ordenar, se puede convertir a lista y entonces ordenar
print(type(sett))
print(sett)

# Diccionario se crea con {} pero aqui se asignan claves:valores

mi_dict: dict = {
    "Canino": "Perro",      
    "Canino": "Lobo",           # Lobo termina borrando a Perro
    "Felino": "Gato",
    "Roedor": "Conejo"
}
print(type(mi_dict))
print(mi_dict)

mi_dict["Ave"] = "Cotorro"      # Insercion
print(mi_dict)

print(mi_dict["Felino"])        # Acceso mediante claves

mi_dict["Roedor"] = "Liebre"    # Modificacion mediante insercion
print(mi_dict)

del mi_dict["Felino"]           # Eliminacion
print(mi_dict)

mi_dict = dict(sorted(mi_dict.items()))     # Ordenar mediante items, cambia a lista y termina en dict, pero ordena las claves
print(type(mi_dict))
print(mi_dict)

"""
 DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

# Como la agenda en si misma es una funcion entonces desde el inicio se crea.


def mi_agenda():

    agenda = {}     # Esta es la agenda como tal
    def up_numero():        # Esta es la funcion para añadir/modificar un contacto
        numero = input("Introduce numero de contacto:")
        if numero.isdigit() and len(numero) > 0 and len(numero) <= 10:
            agenda[name] = numero
            print("Contacto añadido.")
        else:
            print("Solo se aceptan numeros de hasta 10 digitos.")
    
    while True:     # De esta manera se mantiene la funcion en bucle

        # Se inicia imprimiendo el menu

        print("")
        print("1 - Buscar contacto")
        print("2 - Agregar Contacto")
        print("3 - Actualizar contacto")
        print("4 - Eliminar contactos")
        print("5 - Salir")
        print("6 - Ver agenda")

        option = input("Elige la opcion deseada:")      # Input se utiliza para poder interactuar con terminal

        match option:       # Se puede usar if, elif y else, pero en python existe match
            case "1":
                name = input("Introduce el nombre de contacto:")
                if name in agenda:
                    print(
                        f"El numero de {name} es {agenda[name]}")
                else:
                    print(f"El nombre {name} no existe en la agenda.")
            case "2":
                name = input("Introduce nombre de contacto:")
                up_numero()
            case "3":
                name = input("Introduce el nombre de contacto que desea actualizar:")
                if name in agenda:
                    up_numero()
                else:
                    print(f"El nombre {name} no existe en la agenda.")

            case "4":
                name = input("Introduce el nombre de contacto que desea eliminar:")
                if name in agenda:
                    del agenda[name]
                    print("El contacto se ha borrado.")
                else:
                    print(f"El nombre {name} no existe en la agenda.")
            case "5":
                print("Saliendo")
                break
            case "6":
                    print(agenda)
            case _:
                print("Opcion invalida. Elige del 1 al 6")


mi_agenda()
