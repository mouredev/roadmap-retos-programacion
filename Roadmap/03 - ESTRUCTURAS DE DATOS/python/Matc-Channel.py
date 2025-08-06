
# LISTAS
my_list: list = ["Brais", "Black", "Wolfy", "Visionos"]
print(my_list)

# AÑADIR o INSERCIÓN
my_list.append("Kramer")
print(my_list)

# ELIMINACIÓN
my_list.remove("Brais")
print(my_list)

# ACEDER A UNA POSICIÓN
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
# print(my_list[4])   # => No hay POSICIÓN 4; ERROR

# ACTUALIZACIÓN
my_list[1] = "Paquita"
print(my_list)

# ORDENACIÓN
my_list.sort()
print(my_list)  # ORDENA ALFABETICAMENTE
print(type(my_list))


# TUPLAS

# Estructura deonde podemos almacenar mas de 1 DATO
# Pero las TUPLAS son INMUTABLES
# Para uso de DATOS IMUTABLES
my_tuple: tuple = ("Brais", "Moure", "@mouredev", "36")
# ACCESO  A UNA POSICIÓN
print(my_tuple[1])
print(my_tuple[3])
# print(my_tuple[4])  # => No hay POSICIÓN 4; ERROR

# USO DE sorted()...devuelve una LISTA
my_tuple = sorted(my_tuple)     # Pero muestra ERROR por datos 36 int
# Pero se tranasforma a LISTA
# Por lo que se pude CASTEAR a TUPLA

# ORDENACIÓN
my_tuple = tuple(sorted(my_tuple))  # => sorted ordenará numeros y textosaa
print(my_tuple)
print(type(my_tuple))


# SETS
# Son otros tipos de ESTRUCTURAS
my_set: set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)
# INSERCIÓN
my_set.add("mouredev@gmail.com")
my_set.add("mouredev@gmail.com")    # => NO GUARDA DUPLICADOS
# ELIMINACIÓN
my_set.remove("Moure")
print(my_set)
# ORDENACIÓN
my_set = set(sorted(my_set))    # => NO SE PUEDE ORDENAR UN SET
print(my_set)
# print(my_set[0])    # => NO SE PUEDE ACCEDER

print(type(my_set))


# DICCIONARIOS
'''
# 03 ESTRUCTURA DE DATOS
'''

# LISTAS
# son ORDENADAS, es una ESTRUCTURA para guardar varios ELEMENTOS
my_list = ["Brais", "Black", "Wolfy", "Visionos"]
print(my_list)
# añadir una INSERCCÓN la LISTA
my_list.append("Castor")
print(my_list)
# ELIMINACIÓN
my_list.remove("Brais")
print(my_list)
# ACTUALIZACIÓN de ELEMENTOS de la LISTA
# Saber PRIMERO la POSICIÓN
my_list[1]  # => Acceder a posición Wolfy
my_list[1] = "Cuervillo"
print(my_list)
# OREDENACIÓN alfabeticamente
my_list.sort()
print(my_list)
print(type(my_list))    # => VER tipo de DATO
print("\n")

# OTRA ESTRUTURAS
# TUPLA(Podemos guardar más de 1 dato, no actualizable)
my_tuple = ("Brais", "Moure", "@mouredev", "36")
# Acceso a DATOS
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
# ORDENAR una TUPLA
my_tuple = tuple(sorted(my_tuple))  # => 1ero cambiar a 36 a str
print(my_tuple)
print(type(my_tuple))

# SETS
# Otros TIPOS DE ESTRUCTURA
# Bueno para GUARDAR, RECORRER pero no para BUSCAR DATOS
my_set = {"Brais", "Moure", "@mouredev", "36"}
# INSERIÓN
my_set.add("mouredev@gmail.com")
my_set.add("mouredev@gmail.com")    # => No inresa DATOS dobles
my_set.remove("Moure")  # => ELIMINACIÓN
print(my_set)
my_set = set(sorted(my_set))    # => NO SE PUEDE ORDENAR
print(my_set)
print(type(my_set))
print("\n")

# DICCIONARIO
# Otra ESTRUCTURA
my_dict: dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "age": "36"
}

# PRUEBAS
# INSERCIÓN
my_dict["e-mail"] = "mouredev@gmail.com"
print(my_dict)
# ELIMINACIÓN
del my_dict["surname"]
print(my_dict)
# ACCESO
print(my_dict["name"])
# ACTUALIZACIÓN
my_dict["name"] = "Kramer"
print(my_dict)
# ORDENACIÓN
my_dict = dict(sorted(my_dict.items()))
print(my_dict)
print(type(my_dict))
print("-" * 15)

'''
EXTRA

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por
 * defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere
 * realizar, y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y
 * con más de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
'''


def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Ingresa el teléfono del contacto:")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "Introducir un número de teléfono de"
                " menos de 11 dígitos"
            )

    while True:

        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("Selecciona una opción: ")
        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(
                        f"El número de teléfono de {name} es:{agenda[name]}.")
                else:
                    print(f"<<El contacto {name} no existe.>>")
                pass
            case "2":
                name = input("Ingresa el nombre del contacto: ")
                insert_contact()
                pass
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"<<El contacto {name} no existe.>>")
                pass
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print(f">>>Se eliminó el contacto {name}.<<<")
                else:
                    print(f"<<El contacto {name} no existe.>>")
                pass
            case "5":
                print("Gracias por usar la agenda\n"
                      "¡Hasta la próxima!\n"
                      ">>Saliendo de la agenda...")
                break
            case _:
                print(
                    "<<Opción no válida. Elige una opción" +
                    " correcta del 1-5.>>"
                    )


my_agenda()
