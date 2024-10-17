'''
Estructuras de datos en Python
'''

# Listas
# Las listas son colecciones ordenadas de elementos que pueden ser de cualquier tipo

my_list = ["Hola", "hi", "hello", "ciao"]
print(my_list)
my_list.append("salut") # Agrega un elemento al final de la lista
print(my_list)
my_list.remove("hi") # Elimina un elemento de la lista
print(my_list)
print(my_list[0]) # Accede al primer elemento de la lista
my_list[0] = "Hola!" # Modifica el primer elemento de la lista
print(my_list)

# Tuplas
# Las tuplas son colecciones ordenadas de elementos que no pueden ser modificadas
my_tuple: tuple = ("Hola", "hi", "@hello", "22")
print(my_tuple)
print(my_tuple[0]) # Accede al primer elemento de la tupla
my_tuple = tuple(sorted(my_tuple)) # Ordena los elementos de la tupla
print(my_tuple)

#sets
# Los sets son colecciones no ordenadas de elementos únicos
my_set = {"Hola", "hi", "hello", "ciao", "22"}
print(my_set)
my_set.add("salut") # Agrega un elemento al set
print(my_set)
my_set.remove("hi") # Elimina un elemento del set
print(my_set)
my_set = set(sorted(my_set)) # el set no se pued ordenar
print(my_set)

# Diccionarios

my_dict : dict = { "spanish":"Hola", "english":"hi", "english":"@hello","number": "22"}
print(my_dict["english"])
my_dict["french"] = "salut" # Agrega un elemento al diccionario
print(my_dict)
my_dict["number"] = "33" # Modifica un elemento del diccionario
print(my_dict)
del my_dict["english"] # Elimina un elemento del diccionario
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordena los elementos del diccionario
print(my_dict)

'''
Extra
'''

def my_agenda():
    agenda = {}
    def insert_contact( ):
        phone = input("Introduce el nuevo teléfono: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Debes introducir un número de teléfono válido menor a 11 dígitos")
    while True:
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualzar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        option = input("\nSeleccione una opción: ")
        match option:
            case "1":
                name = input("Introduce el nombre: ")
                if name in agenda:
                    print(f"{name}: {agenda[name]}")
                else:
                    print("Contacto no encontrado")
            case "2":
                name = input("Introduce el nombre: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre: ")
                if name in agenda:
                    insert_contact()
                else:
                    print("Contacto no encontrado")
            case "4":
                name = input("Introduce el nombre: ")
                if name in agenda:
                    del agenda[name]
                    print("Contacto eliminado")
                else:
                    print("Contacto no encontrado")
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opción no válida")
                my_agenda()
my_agenda() # Llama a la función my_agenda