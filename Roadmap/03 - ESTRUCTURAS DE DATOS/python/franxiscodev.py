# Listas
my_list = ["a", "b", "z", "c", "y", "e"]
print(my_list)
print(my_list[0])
print(my_list[1])
my_list.append("f")
print(my_list)
my_list.insert(0, "b")
print(f"insert 0,b {my_list}")
# my_list.remove("b")
print(my_list.pop(0))
print(my_list)
my_list.sort()
print(my_list)
# Crear una lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# tuplas ()
print("Tuplas")
my_tuple: tuple = ("z", "b", "c", "a", "y", "e")
print(my_tuple)
print(my_tuple[0])
'''
# inmutables
my_tuple = my_tuple.append("d")
print(my_tuple)
'''
my_tuple = tuple(sorted(my_tuple))
print(my_tuple)
print(type(my_tuple))

# Sets
my_set = {"a", "b", "z", "c", "y", "e"}
print(my_set)
my_set.add("f")
print(my_set)   # {'a', 'b', 'c', 'e', 'f', 'y', 'z'}
my_set.remove("f")  # {'a', 'b', 'c', 'e', 'y', 'z'}
print(my_set)   # {'a', 'b', 'c', 'e', 'y', 'z'}
my_set.discard("f")  # {'a', 'b', 'c', 'e', 'y', 'z'}
print(my_set)   # {'a', 'b', 'c', 'e', 'y', 'z'}
my_set.pop()
print(my_set)   # {'b', 'c', 'e', 'y', 'z'}

# Diccionarios
my_dict = {
    "name": "Francisco",
    "last_name": "Gonzalez",
    "age": 25
}
print(my_dict)
print(my_dict["name"])
print(my_dict["last_name"])  # Gonzalez
print(my_dict["age"])   # 25
my_dict["age"] = 26
print(my_dict["age"])   # 26
my_dict["city"] = "Medellin"
print(my_dict)
# {'name': 'Francisco', 'last_name': 'Gonzalez', 'age': 26}
my_dict.pop("city")
print(my_dict)
del my_dict["age"]
print(my_dict)

print("get")
print(my_dict.get("name", "No encontrado"))  # Francisco
print(my_dict.get("nombre", "No encontrado"))  # No encontrado

'''
Extra
'''


def my_agenda():
    agenda = {}

    def print_no_contact(name: str) -> str:
        return f"Contacto no encontrado {name}"

    def insert_contact(name: str, phone: str) -> None:
        if (phone.isdigit() and len(phone) < 10):
            agenda[name] = phone
            print(f"Contacto agregado/actualizado {name}: {phone}")
        else:

            print("Número de teléfono inválido")

    while True:  # Ciclo infinito
        print("\nAgenda")
        print("1. Buscar contacto")
        print("2. Agregar contacto")
        print("3. Actualizar contactos")
        print("4. Eliminar contactos")
        print("5. Print dict")
        print("6. Salir")
        option = input("Opción: ")
        match option:
            case "1":
                name = input("Buscar Nombre: ")
                if name in agenda:
                    print(f"{name}: {agenda[name]}")
                else:
                    print(print_no_contact(name))
            case "2":
                name = input("Agregar Nombre: ")
                phone = input("Agregar Teléfono: ")
                insert_contact(name, phone)
            case "3":
                name = input("Nombre para actualizar: ")
                if name in agenda:
                    phone = input("Teléfono: ")
                    insert_contact(name, phone)
                else:
                    print(print_no_contact(name))
            case "4":
                name = input("Eliminar Nombre: ")
                if name in agenda:
                    del agenda[name]
                    print(f"Contacto eliminado  {name}")
                else:
                    print(print_no_contact(name))
            case "5":   # Print dict
                print(agenda)
            case "6":
                break
            case _:
                print("Opción no válida")


my_agenda()
