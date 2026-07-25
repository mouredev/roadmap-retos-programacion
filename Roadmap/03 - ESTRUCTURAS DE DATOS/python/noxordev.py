"""
Listas
"""

from re import search


my_list = ["Victor", "Juan", "Maria", "Pedro", "Ana"] #Declaración de una lista
print(my_list)

my_list.append("Luis") #Inserción al final de la lista
print(my_list)

my_list[2] = "Andrea" #Actualización de un elemento
print(my_list)

my_list.remove("Juan") #Eliminación de un elemento
print(my_list)

my_list.insert(1, "Carlos") #Inserción en una posición específica
print(my_list)

my_list.pop(2) #Eliminación de un elemento por índice
print(my_list)

my_list.sort() #Ordenación de la lista
print(my_list)
print(my_list[1]) #Acceso a un elemento específico
print(my_list.count("Victor")) #Contar el número de veces que aparece un elemento
print(my_list.index("Victor")) #Buscar el índice de un elemento
print(my_list[1:3]) #Acceso a un rango de elementos
print(my_list[:3]) #Acceso a los primeros elementos
print(my_list[3:]) #Acceso a los últimos elementos

# Tuplas (inmutables. Solo acceso)

my_tuple = ("Victor", "Juan", "Maria", "Pedro", "Ana", "11") #Declaración de una tupla
print(my_tuple)
print(my_tuple[1]) #Acceso a un elemento específico
print(my_tuple.count("Victor")) #Contar el número de veces que aparece un elemento
print(my_tuple.index("Victor")) #Buscar el índice de un elemento
print(my_tuple[1:3]) #Acceso a un rango de elementos
print(my_tuple[:3]) #Acceso a los primeros elementos
print(my_tuple[3:]) #Acceso a los últimos elementos

# Sets (conjunto sin orden y sin duplicados) (convvierte a hash table)

my_set = {"Victor", "Juan", "Maria", "Pedro", "@Ana", "11"} #Declaración
print(my_set)
print((my_set))
my_set.add("Luis")
print(my_set)
my_set.remove("Juan")
print(my_set)
my_set.discard("Maria")
print(my_set)
my_set.update(["Carlos", "Ana"])
print(my_set)
my_set.remove("Carlos")
print(my_set)
my_set.discard("Ana")
print(my_set)
my_set.clear()
print(my_set)

# Diccionarios (clave-valor)

my_dict: dict = {
    "name": "Victor",
    "username": "noxordev",
    "age": 32,
    "email": "victor@gmail.com"
} #Declaración de un diccionario

my_dict["email"] = "victor@gmail.com" #Inserción de un elemento
print(my_dict)
del my_dict["email"] #Eliminación de un elemento
my_dict["age"] = 33 #Actualización de un elemento
print(my_dict)
my_dict = dict(sorted(my_dict.items())) #Ordenación de un diccionario
print(my_dict)

"""
Extra
""" 

def agenda():

    agenda = {}

    def search_contact():
        name = input("Introduce el nombre del contacto a buscar: ")
        if name in agenda:
            print(f" -> Contacto encontrado. Nombre: {name} - Teléfono: {agenda[name]}")
        else:
            print("El contacto no existe")
    
    def add_contact():
        name = input("Introduce el nombre del contacto: ")
        phone = input("Introduce el teléfono del contacto: (máximo 11 dígitos) ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            print("Formato de teléfono correcto")
            agenda[name] = phone
            print(f"Contacto {name} añadido correctamente")
        else:
            print("Formato de teléfono incorrecto. Vuelve a introducir el teléfono del contacto.")
    
    def update_contact():
        name = input("Introduce el nombre del contacto a actualizar: ")
        phone = input("Introduce el nuevo teléfono del contacto: (máximo 11 dígitos) ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            print("Formato de teléfono correcto")
            agenda[name] = phone
            print(f"Contacto {name} actualizado correctamente")
        else:
            print("Formato de teléfono incorrecto. Vuelve a introducir el teléfono del contacto.")
    
    def delete_contact():
        name = input("Introduce el nombre del contacto a eliminar: ")
        if name in agenda:
            del agenda[name]
            print(f"Contacto {name} eliminado correctamente")
        else:
            print("El contacto no existe.")
    
    while True:
    
        print("Introduce la operación que quieres realizar: ")
        print("1. Buscar contacto")
        print("2. Añadir contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        operation = input("Introduce la operación: ")
        if operation == "1":
            search_contact()
        elif operation == "2":
            add_contact()
        elif operation == "3":
            update_contact()
        elif operation == "4":
            delete_contact()
        elif operation == "5":
            print("Saliendo de la agenda...")
            break
        else:
            print("Operación no válida. Escribe una operación del 1 al 5.")

agenda()
