# Listas
print("Listas")
my_list = ["Victor", "Ana", "Luis", "Maria"]
print(my_list)

my_list.append("Carlos") # Insertar un nuevo elemento al final de la lista
print(my_list)
my_list.remove("Ana") # Eliminar un elemento de la lista
print(my_list)
print(my_list[0]) # Acceder al primer elemento de la lista
print(my_list[1]) # Acceder al segundo elemento de la lista
my_list[0] = "Andres" # Modificar el primer elemento de la lista
print(my_list) # Modificar el primer elemento de la lista
my_list.sort() # Ordenar la lista por defecto (alfabéticamente)
print(my_list) # Imprimir la lista ordenada
print(type(my_list)) # Imprimir el tipo de dato de la variable my_list

# Tuplas
print("\nTuplas")
tupla = ("Victor", "Morales", "30", "Programador")
print(tupla)
print(tupla[0]) # Acceder al primer elemento de la tupla
print(tupla[2]) # Acceder al tercer elemento de la tupla
print(type(tupla)) # Imprimir el tipo de dato de la variable tupla
tupla = tuple(sorted(tupla))
print(tupla) # Imprimir la tupla ordenada


# Sets
print("\nSets")

my_set = {"Victor", "Morales", "30", "Programador"}
print(my_set)
my_set.add("optiai@email.com") # Agregar un nuevo elemento al set
print(my_set) 
print(type(my_set)) 
my_set.remove("30") # Eliminar un elemento del set
print(my_set) 
my_set = sorted(my_set) # Ordenar el set
print(my_set) 
print(type(my_set)) 
my_set = set(my_set) # No se puede orderar
print(my_set) 

# Diccionario
print("\nDiccionario")
my_dict = {
    "nombre": "Victor", 
    "apellido": "Morales", 
    "edad": 30, 
    "profesion": "Programador"}
print(my_dict)
print(type(my_dict))
my_dict["email"] = "victor@optiai.com"   # inserción
del my_dict["edad"]                       # borrado
my_dict["ciudad"] = "Colombia"            # actualización
print(my_dict)
print(type(my_dict))
my_dict = dict(sorted(my_dict.items())) # Ordenar el diccionario por clave
print(my_dict)
print(type(my_dict))

# Dificultad Extra
print("\nDificultad Extra:")

print("\nAgenda de Contactos")

def my_agenda():
    agenda = {}
    while True:

        print("\n1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nElige una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre a buscar: ")
                if name in agenda:
                    print(f"Teléfono de {name}: {agenda[name]}")
                else:
                    print(f"Contacto {name} no encontrado.")
            case "2":
                name = input("Introduce el nombre: ")
                phone = input("Introduce el teléfono: ")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone
                    print(f"Contacto {name} agregado.")
                else:
                    print("Número de teléfono inválido. Debe contener solo dígitos y tener entre 1 y 11 caracteres.")
            case "3":
                name = input("Introduce el nombre a actualizar: ")
                if name in agenda:
                    phone = input("Introduce el nuevo teléfono: ")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                        print(f"Contacto {name} actualizado.")
                    else:
                        print("Número de teléfono inválido. Debe contener solo dígitos y tener entre 1 y 11 caracteres.")
                else:
                    print(f"Contacto {name} no encontrado.")
            case "4":
                name = input("Introduce el nombre a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print(f"Contacto {name} eliminado.")
                else:
                    print(f"Contacto {name} no encontrado.")
            case "5":
                print("saliendo de la agenda...")
                break
            case _:
                print("Opción no válida. Por favor, elige una opción del 1 al 5.")

my_agenda()