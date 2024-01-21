"""
#03 ESTRUCTURAS DE DATOS
Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

Ejercicio

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
"""

# listas: colección ordenada y mutable de elementos
print("::::::::::::::::::::::::::::::::::::: LISTAS :::::::::::::::::::::::::::::::::::::")
lista_colores = ["rojo", "verde", "azul", "amarillo", "marrón", "naranja", "blanco", "negro"]

print(f"Lista inicial:\n{lista_colores}\n")


# Inserción en listas
lista_colores.append("violeta")

print(f"Añadido color violeta:\n {lista_colores}\n")


# Actualización del nuevo color (cambio de violeta por fucsia).
lista_colores[-1] = "fucsia"

print(f"Cambiado color violeta por fucsia:\n {lista_colores}\n")


# Borrado del color
lista_colores.remove("fucsia")

print(f"Eliminado color fucsia:\n {lista_colores}\n")


# Ordenado alfabético
lista_colores.sort()

print(f"Lista ordenada:\n {lista_colores}\n\n")



# Tuplas: colección ordenada e inmutable (no se puede modificar una vez creada ni añadir ni eliminar nada)
print("::::::::::::::::::::::::::::::::::::: TUPLAS :::::::::::::::::::::::::::::::::::::")
tupla_paises = ("España", "Portugal", "USA", "Alemania", "Suecia")

print(f"Tupla inicial:\n{tupla_paises}\n")


# Ordenar tupla (indirectamente)
tupla_ordenada = tuple(sorted(tupla_paises))

print(f"Tupla ordenada:\n{tupla_ordenada}\n\n")



# Conjuntos: colección desordenada y mutable de elementos únicos (no se pueden modificar ni ordenar)
print("::::::::::::::::::::::::::::::::::::: CONJUNTOS :::::::::::::::::::::::::::::::::::::")
conjunto_numeros = {1, 2, 3, 4, 5}
print(f"Conjunto inicial:\n{conjunto_numeros}\n")

conjunto_numeros.add(10)
print(f"Conjunto con añadido:\n{conjunto_numeros}\n")

conjunto_numeros.remove(2)
print(f"Conjunto eliminando el nº2:\n{conjunto_numeros}\n\n")



# Diccionarios: colección desordenada (ordenada a partir de Python 3.7) y mutable de pares clave-valor.
print("::::::::::::::::::::::::::::::::::::: DICCIONARIOS :::::::::::::::::::::::::::::::::::::")
diccionario_spa_eng = {"manzana": "apple", "hola": "Hello", "silla": "chair"}
print(f"Diccionario original:\n {diccionario_spa_eng}\n")

# Añadir un elemento
diccionario_spa_eng["mundo"] = "word"
print(f"Diccionario con añadido:\n{diccionario_spa_eng}\n")

# Modificar un elemento
diccionario_spa_eng["mundo"] = "world"
print(f"Diccionario con corrección:\n{diccionario_spa_eng}\n")

# Eliminar un elemento
del diccionario_spa_eng["silla"]
print(f"Diccionario con elemento eleminado:\n{diccionario_spa_eng}\n")

# Ordenar diccinario
diccionario_ordenado = dict(sorted(diccionario_spa_eng.items()))
print(f"Diccionario ordenado:\n{diccionario_ordenado}\n\n")




print("::::::::::::::::::::::::::::::::::::: EXTRA :::::::::::::::::::::::::::::::::::::")

agenda = {}


def buscar_contacto():
    contacto_a_buscar = input("Introduce el nombre del contacto a buscar: ")

    if contacto_a_buscar in agenda.keys():
        print(f"{contacto_a_buscar}: {agenda[contacto_a_buscar]}\n")

    else:
        print("El contacto no existe, inténtalo de nuevo.")
        pass


def anadir_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    numero = int(input("Introduce el número de 9 cifras: "))

    while len(str(numero)) != 9 or numero in agenda.values():

        if len(str(numero)) != 9:
            numero = int(input("Error. Tiene que tener 9 cifras: "))

        elif numero in agenda.values():
            numero = int(input(f"Error. El número {numero} ya existe en la agenda: "))

    else:
        print(f"{nombre} se ha agregado a la agenda correctamente.\n")

        agenda[nombre] = numero


def modificar_contacto():
    contacto_a_modificar = input("Introduce el nombre del contacto a modificar: ")

    if contacto_a_modificar not in agenda.keys():
        print("El nombre no existe en la agenda, inténtalo de nuevo.")
        modificar_contacto()

    else:
        del agenda[contacto_a_modificar]

        nombre = input("Introduce el nuevo nombre del contacto: ")
        numero = int(input("Introduce el nuevo número de 9 cifras: "))

        while len(str(numero)) != 9 or numero in agenda.values():

            if len(str(numero)) != 9:
                numero = int(input("Error. Tiene que tener 9 cifras: "))

            elif numero in agenda.values():
                numero = int(input(f"Error. El número {numero} ya existe en la agenda: "))

        agenda[nombre] = numero
        print(f"{contacto_a_modificar} se ha modificado correctamente.\n")


def eliminar_contacto():
    contacto_a_eliminar = input("Introduce el nombre del contacto a eliminar: ")

    if contacto_a_eliminar in agenda.keys():

        del agenda[contacto_a_eliminar]

        print(f"El contacto {contacto_a_eliminar} se ha eliminado correctamente.\n")

    else:
        print("El contacto no existe, inténtalo de nuevo.")
        pass


def ver_contactos():

    agenda_ordenada = dict(sorted(agenda.items()))

    for contacto, numero in agenda_ordenada.items():
        print(f"{contacto}: {numero}")


opcion_elegida = 0

while opcion_elegida != 6:

    # Creación del menú y bucle
    print("""

        ### Agenda Telefónica ###

        ¿Qué deseas hacer?:

              [1] - Buscar
              [2] - Añadir
              [3] - Modificar
              [4] - Eliminar
              [5] - Ver todos los contactos
              [6] - Salir
    """)

    opcion_elegida = int(input())

    match opcion_elegida:
        case 1:
            buscar_contacto()
        case 2:
            anadir_contacto()
        case 3:
            modificar_contacto()
        case 4:
            eliminar_contacto()
        case 5:
            ver_contactos()
        case 6:
            opcion_elegida = 6


print("\nGracias por utilizar la agenda. Hasta pronto!!!")




