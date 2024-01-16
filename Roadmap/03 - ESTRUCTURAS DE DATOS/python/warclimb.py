# #03 ESTRUCTURAS DE DATOS
#### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

## Ejercicio
"""
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
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 """

# Los tipos de estrucutras de datos en Python son: listas, tuplas, diccionarios y conjuntos

"""LISTAS
    - conjunto de datos ordenados por índices"""
herramientas = ["martillo", "destornillador", "sierra", "taladro"]

# insercion
herramientas.append("alicates")
# borrado
herramientas.remove("sierra")
# actualizacion
herramientas[2] = "serrucho"
# ordenacion
herramientas.sort()

"""TUPLAS
    - Igual que las tablas pero inmutables, se usan para datos que no van a cambiar"""
power_rangers = ("Jason", "Zack", "Billy", "Trini", "Kimberly")

# Las tuplas no se pueden editar, asi que: ¯\_(ツ)_/¯

"""Diccionarios:
    - conjunto de datos ordenados por claves. en este caso la clave es la herramienta y el valor representa la resistencia."""
herramientas_dict = {"martillo": 40, "destornillador": 6, "sierra": 20, "taladro": 80}

# insercion
herramientas_dict["alicates"] = 10
# borrado
del herramientas_dict["sierra"]
# actualizacion
herramientas_dict["taladro"] = 90

"""CONJUNTOS / SETS
- conjunto de datos no ordenados, no se pueden repetir"""
herramientas_set = {"martillo", "destornillador", "sierra", "taladro"}

# insercion
herramientas_set.add("alicates")
# borrado
herramientas_set.remove("sierra")
# actualizacion
herramientas_set.add("serrucho")

""" DIFICULTAD EXTRA """
""" * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""


def agregar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el teléfono del contacto: ")
    contactos[nombre] = telefono

def buscar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in contactos:
        print(nombre, ":", contactos[nombre])
    else:
        print("No existe el contacto")

def actualizar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in contactos:
        telefono = input("Introduce el teléfono del contacto: ")
        contactos[nombre] = telefono
    else:
        print("No existe el contacto")

def borrar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in contactos:
        del contactos[nombre]
    else:
        print("No existe el contacto")

def agenda():
    contactos = {}
    while True:
        print("¿Qué quieres hacer?")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Borrar contacto")
        print("5. Salir")
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            agregar_contacto(contactos)
        elif opcion == 2:
            buscar_contacto(contactos)
        elif opcion == 3:
            actualizar_contacto(contactos)
        elif opcion == 4:
            borrar_contacto(contactos)
        elif opcion == 5:
            break
        else:
            print("Opción incorrecta")
    print("Fin")

if __name__ == "__main__":
    agenda()