'''
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
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
'''

#! Listas: estructura que permite almacenar datos de cualquier tipo en forma ordenada.
print(" --- Listas --- ")
my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list.append(6)
print(my_list, "Agrego un elemento al final de la lista")

my_list.pop()
print(my_list, "Elimino el último elemento de la lista")

my_list.insert(2, 10) # (posición, elemento) === my_list[2] = 10
print(my_list, "Inserto un elemento en la posición 2")

my_list.remove(10)
print(my_list, "Elimino el elemento 10 de la lista")

my_list.sort()
print(my_list, "Ordeno la lista")

my_list.reverse()
print(my_list, "Invierto la lista")

#! Tuplas: estructura que permite almacenar datos de cualquier tipo en forma ordenada.
print(" --- Tuplas --- ")
# La diferencia con las listas es que las tuplas son inmutables, es decir, no se pueden modificar.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# my_tuple.append(6) # Error

# Acceso a la tupla
print(my_tuple[0]) # 1
# Ordeno la tupla (devuelve una lista porque hace como un iterable)
print(sorted(my_tuple)) # [1, 2, 3, 4, 5]
print(type(sorted(my_tuple))) # <class 'list'>
print(type(my_tuple)) # <class 'tuple'>

#! Sets: estructura que permite almacenar datos de cualquier tipo en forma desordenada. Permite eliminar elementos repetidos.
print(" --- Sets --- ")
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
my_set.add(6) # No se puede repetir elementos en un set (no se agrega porque ya existe)
print(my_set, "Agrego un elemento al set")

my_set.remove(6)
print(my_set, "Elimino un elemento del set")

#? No se puede acceder a un elemento del set porque no tiene índices (no es ordenado)
# print(my_set[0]) # Error

my_set.update([6, 7, 8, 9, 10])
print(my_set, "Agrego varios elementos al set")

#! Diccionarios: se guardan los datos en pares clave-valor. No se pueden repetir las claves. Los diccionarios no son ordenados.
print(" --- Diccionarios --- ")

my_dict: dict = {
    "nombre": "Tobias",
    "apellido": "Bordino",
    "edad": 21
}
print(my_dict)

my_dict["edad"] = 22
print(my_dict, "Actualizo la edad")

my_dict["ubicación"] = "Córdoba"
print(my_dict, "Agrego un elemento al diccionario")

my_dict.pop("ubicación")
print(my_dict, "Elimino un elemento del diccionario")
del my_dict["edad"]
print(my_dict, "Elimino un elemento del diccionario")

# Forma de ordenar un diccionario
my_dict = dict(sorted(my_dict.items()))
print(my_dict, "Ordeno el diccionario")

"""
EXTRA
"""
#! Agenda de contactos
print(" --- Agenda de contactos --- ")

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Ingrese el nuevo teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
            print("Contacto actualizado con éxito")
        else:
            print("El teléfono ingresado es inválido")

    while True:
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = int(input("\nIngrese una opción: "))

        match option:
            case 1:
                print("Buscar contacto")
                name = input("Ingrese el nombre del contacto: ")
                if name in agenda:
                    print(f"El teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe")

            case 2:
                print("Insertar contacto")
                name = input("Ingrese el nombre del contacto: ")
                insert_contact()
                    
            case 3:
                print("Actualizar contacto")
                name = input("Ingrese el nombre del contacto: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe")

            case 4:
                print("Eliminar contacto")
                name = input("Ingrese el nombre del contacto: ")
                if name in agenda:
                    del agenda[name]
                    print(f"El contacto {name} ha sido eliminado")
                else:
                    print(f"El contacto {name} no existe")

            case 5:
                print("Saliendo de la agenda...")
                break
            case _:
                print("Opción inválida (Opción de 1 a 5)")
                my_agenda()

my_agenda()