"""
Estructuras de datos por defecto de python
"""

# Listas
my_list = ["orange", 'banana', 'pear', 'apple', 'kiwi']
print(my_list)

my_list.append("grape") # Inserción
print(my_list)

my_list.remove("pear") # Eliminación
print(my_list)

my_list[1] = 'strawberry' # Actualización
print(my_list)

my_list.sort() # Ordenación
print(my_list)
print(type(my_list))

# Tuplas -> son inmutables
my_tuple = ("Marcos", "Plata", "@mplatab", "25")
print(my_tuple[1]) # Acceso
print(my_tuple[3])

my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets -> por definición es una estructura desordenada y no agrega datos duplicados
my_set = {"Marcos", "Plata", "@mplatab", "25"}
print(my_set)
my_set.add("mjsilver98") # Inserción

my_set.remove("25") # Eliminacion

my_set = set(sorted(my_set)) # no se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario -> key:value

my_dict: dict = {"age": 25, "name": "Marcos", "last_name": "Plata"}

my_dict["email"] = "example@gmail.com" # Inserción
print(my_dict)

del(my_dict["last_name"]) # Eliminación
print(my_dict)

my_dict["age"] = 26 # Actualización
print(my_dict)


my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)
print(type(my_dict))

"""
DIFICULTAD EXTRA (opcional):ẞ
"""

def my_agenda():
    agenda = {}

    def insert_contact():
        phone = input("Ingrese el nuevo número de telefono: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Introduccion un número de telefeno máximo de 11 dígitos")

    while True:
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSeleciona una opción: ")
        match option:
            case "1":
                name = input("Ingrese el nombre del contacto que desee buscar: ").lower()
                if name in agenda:
                    print(f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe")    
            case "2":
                name = input("Ingresa el nombre de contacto: ").lower()
                insert_contact()
            case "3":
                name = input("Ingrese el nombre del contacto que desea actualizar: ").lower()
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe")    
            case "4":
                name = input("Ingrese el nombre del contacto que desea eliminar: ").lower()
                if name in agenda:
                    del(agenda[name])
                else:
                    print(f"El contacto {name} no existe")    

            case "5":
                print("Salir de la agenda")
                break
            case _:
                print("Opción no valida. Elige una opción del 1 al 5")
    

my_agenda()