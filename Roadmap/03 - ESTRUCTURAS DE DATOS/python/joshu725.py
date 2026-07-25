# Estructuras #

# Listas (inserción, borrado, actualización y ordenación)
list = ["Pedro", "Luis", "David"]
print(list)
list.append("Fernando")
print(list)
list.remove("Luis")
print(list)
print(list[1])
list[1] = "Alejandra"
print(list)
list.sort()
print(list)
print(type(list))

# Tuplas (inmutables)
tuple = ("Jessica", 76, "Ashley", 23.12, True)
print(tuple)
print(tuple[3])
print(type(tuple))

# Sets (malas para buscar datos porque siempre estan desordenadas)
set = {"Jessica", 76, "Ashley", 23.12, True}
print(set)
set.add(13)
set.add(13)  # Evita duplicados
print(set)
set.remove("Ashley")
print(set)
print(type(set))

# Diccionario (clave: valor)
dictionary = {
    "name": "Josh",
    "username": "joshu725",
    "email": "joshu725@gmail.com"
}
print(dictionary["username"])
dictionary["age"] = 23
print(dictionary)
del dictionary["age"]
print(dictionary)
print(type(dictionary))

# Extra #

def agenda():

    contacts = {}

    def add_number(name, number):
        if number.isdigit() and len(number) == 10:
            contacts[name] = number
        else:
            print("Ingresa un número de 10 dígitos")

    while True:
        print("==========================")
        print("1. Insertar")
        print("2. Actualizar")
        print("3. Eliminar")
        print("4. Buscar")
        print("\n5. Salir")
        print("==========================")
        option = input("> ")

        match option:
            case "1":
                name = input("Introduce un nombre: ")
                number = input("Introduce el telefono: ")
                add_number(name, number)
            case "2":
                name = input("Introduce un nombre a actualizar: ")
                if name in contacts:
                    number = input("Introduce el nuevo teléfono: ")
                    add_number(name, number)
                else:
                    print("No se ha encontrado el contacto")
            case "3":
                name = input("Introduce un nombre a eliminar: ")
                if name in contacts:
                    del contacts[name]
                else:
                    print("No se ha encontrado el contacto")
            case "4":
                name = input("Introduce un nombre a buscar: ")
                if name in contacts:
                    print(f"El número de {name} es: {contacts[name]}")
                else:
                    print("No se ha encontrado el contacto")
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida, ingresa un número del 1 al 5")

agenda()
