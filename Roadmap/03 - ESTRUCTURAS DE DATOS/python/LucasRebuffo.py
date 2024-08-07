""" /*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */ """

## Estructuras de datos

## Listas --> Coleccion de elementos

from ast import main
from os import name


my_list = ["lista", "5", "False", "1.2"]
print(my_list)
my_list.append("al final")  # Agregar
print(my_list)
my_list.remove("lista")  # Borrar
print(my_list)
i = 1
my_list[i] = "valor reemplazado"  # Actualizar
print(my_list)
my_list.sort()  # Ordenar
print(my_list)

## Tuplas --> Conjunto datos no mutable

my_tuple = ("1", "tupla", "2.5", "True")
print(my_tuple)
print(my_tuple[2])  # Acceso
my_tuple = tuple(sorted(my_tuple))  # Ordenar
print(my_tuple)

## Sets --> Colleccion no ordenada con elementos no repetidos

my_set = {"set", "6", "1.3", "False"}
print((my_set))
my_set.add("pepe")  # Agregar
print(my_set)
my_set.discard("set")  # Borrar
print(my_set)
my_set = set(sorted(my_set))  # No se ordena
print(my_set)

## Diccionarios --> Coleccion de clave valor

my_dict = {
    "estructura": "dicionario",
    "1": "True",
}
print(my_dict)
my_dict["nueva llave"] = "nuevo valor"  # Agregar
print(my_dict)
print(my_dict["estructura"])  # Acceder
my_dict["estructura"] = "nuevo diccionario"  # Actualizar
print(my_dict)
del my_dict["1"]  # Borrar
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenamiento
print(my_dict)

""" 
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */  """


def agregar_contacto(agenda: dict, contacto_nombre, contacto_numero: str):

    if len(contacto_numero) <= 11 and contacto_numero.isdigit():
        agenda[contacto_nombre] = contacto_numero
        print("")
        return agenda
    else:
        print("El numero ingresado no es valido.")
        print("")
        return agenda


def listar_contactos(agenda: dict):
    print("Los contactos en tu agenda son: ")
    print("")
    for contacto, numero in agenda.items():
        print(f"Contacto: {contacto} Numero : {numero}")
    print("")


def buscar_contacto(agenda: dict, nombre_contacto):
    if agenda[nombre_contacto]:
        print(f"EL contacto {nombre_contacto} tiene nuemro: {agenda[nombre_contacto]}")
        print("")
    else:
        print("No esta en la agenda")
        print("")


def actualizar_contacto(agenda: dict, nombre_contacto, nuevo_numero):
    if agenda[nombre_contacto]:
        agenda[nombre_contacto] = nuevo_numero
        return agenda
    else:
        print("No esta en la agenda")
        print("")


def eliminar_contacto(agenda: dict, nombre_contacto):
    if agenda[nombre_contacto]:
        del agenda[nombre_contacto]
        return agenda
    else:
        print("No esta en la agenda")
        print("")

if __name__ == "__main__":

    print("")
    print("")
    print("")

    agenda: dict = {}
    while 1:

        print("Que operacion quieres realizar ?")
        print("")
        print("1 . Agregar")
        print("2 . Borrar")
        print("3 . Actualizar")
        print("4 . Buscar")
        print("5 . Listar")
        print("6 . Salir")
        print("")

        op = input("Ingrese la operacion.")
        print("")

        match op:
            case "1":
                contacto = input("Ingrese contacto: ")
                numero = input("Ingrese numero: ")
                agenda = agregar_contacto(agenda, contacto, numero)
            case "2":
                contacto = input("Ingrese contacto: ")
                agenda = eliminar_contacto(agenda, contacto)
            case "3":
                contacto = input("Ingrese contacto: ")
                numero_nuevo = input("Ingrese numero: ")
                actualizar_contacto(agenda, contacto, numero_nuevo)
            case "4":
                contacto = input("Ingrese contacto: ")
                buscar_contacto(agenda, contacto)
            case "5":
                listar_contactos(agenda)
            case "6":
                print("Saliendo de agenda ...")
                break
            case _:
                print("Operacion no soportada")
