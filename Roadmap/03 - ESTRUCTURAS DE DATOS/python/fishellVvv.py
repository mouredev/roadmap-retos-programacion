# Estructura - Listas
my_list = ["Marcelino", "Victor", "Juanlu", "Jose"]
print(my_list[1]) # acceso
print(my_list)
my_list.append("Pepito") # inserción
print(my_list)
my_list.remove("Victor") # borrado
print(my_list)
my_list[1] = "Juan Luis" # actualización
print(my_list)
my_list.sort() # ordenación
print(my_list)

# Estructura - Tuplas
my_tuple = ("Victor", "Vigil", "fishell", "1983")
print(my_tuple[2]) # acceso
print(my_tuple)
my_tuple = tuple(sorted(my_tuple)) # ordenación
print(my_tuple)

# Estructuras - Sets
my_set = {"Picual", "Cornezuelo", "Manzanilla"}
print(my_set)
my_set.add("Verdial") # inserción
print(my_set)
my_set.remove("Manzanilla") # borrado
print(my_set)

# Estructura - Diccionario
my_dict = {
    "model": "CL500", 
    "year": "2023",
    "brand": "Honda"
}
print(my_dict["model"]) # acceso
print(my_dict)
my_dict["style"] = "Scrambler" # inserción/actualización
print(my_dict)
del my_dict["year"] # borrado
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # ordenación
print(my_dict)

# Extra
def my_agenda():

    contact_book = {
        "Marcelino": 600220001,
        "Juan Luis": 600220002,
        "Jose": 600220003, 
        "Pepito": 600220004
    }

    while True:

        print("\n***Agenta de contactos***")
        print("1. Buscar contacto")
        print("2. Añadir contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("0. Salir")

        option = input("\nIndica una opción: ")

        match option:
            case "0":
                conf = input("Escribe SALIR para confirmar: ")
                if conf.lower() == "salir":
                    print("Saliendo de la agenda...")
                    break
            case "1":
                buscado = input("Nombre: ")
                if buscado in contact_book:
                    print(f"Tlf: {contact_book[buscado]}")
                else:
                    print(f"El contacto {buscado} no existe")
            case "2":
                name = input("Nombre: ")
                phone = input("Tlf: ")
                if phone.isdigit() and len(phone) == 9:
                    contact_book[name] = phone
                    print("Contacto guardado")
                else:
                    print("Número de teléfono no válido, debe tener 9 dígitos")
            case "3":
                buscado = input("Nombre: ")
                if buscado in contact_book:
                    phone = input("Tlf: ")
                    if phone.isdigit() and len(phone) == 9:
                        contact_book[buscado] = phone
                        print("Contacto actualizado")
                    else:
                        print("Número de teléfono no válido, debe tener 9 dígitos")
                else:
                    print(f"El contacto {buscado} no existe")
            case "4":
                buscado = input("Nombre: ")
                if buscado in contact_book:
                    del contact_book[buscado]
                    print("Contacto eliminado")
                else:
                    print(f"El contacto {buscado} no existe")
            case _:
                print("Indica un valor de 1 a 4 (0 para salir)")

        input("Pulsa ENTER para continuar")

my_agenda()