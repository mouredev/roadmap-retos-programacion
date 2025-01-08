# ESTRUCTURAS - inserción, borrado, actualización y ordenación

# LIST ARRAY 

print("LISTAS")

list_user: list = ["Angel", "Borja", "Zaida",  "Carlos", "Maite", "Pedro"]
print(list_user)

# inserción
list_user.append("Carolina")
print(list_user)

# borrado
list_user.remove("Carlos")
print(list_user)

# actualización

list_user[0] = "Ángel"
print(list_user)

# ordenación
list_user.sort(reverse=False)
print(list_user)


# TUPLAS 
print("TUPLAS: son inmutables")
list_compra: tuple = ("pan", "leche", "verduras", "huevos", "aceite")
print(list_compra)

#ordenación - se tiene que transformar en lista
list_compra_ordenada = sorted(list_compra)
print(list_compra_ordenada, type(list_compra_ordenada))
print(tuple(list_compra_ordenada), type(tuple(list_compra_ordenada)))

# SET - CONJUNTOS
print("SETs: elementos únicos, no repetidos")
set_coches: set = {"Ford", "Toyota", "Mercedes", "BMW", "Renault"}

print(set_coches)

#inserción
set_coches.add("Hyundai")
print(set_coches)
set_coches.add("Ford") # NO SE AÑADE PORQUE ESTARÍA DUPLICADO

# borrado
set_coches.remove("Renault")
print(set_coches)

# ordenar
set_coches_ord = sorted(set_coches) 
print(set_coches_ord, type(set_coches_ord))
print(set(set_coches_ord), type(set(set_coches_ord))) # NO SE PUEDEN ORDENAR, TIENEN QUE SER LISTAS

# DICCIONARIOS 
print("DICCIONARIOS")

bbdd_coches: dict = {
    "Ford": 23445,
    "BMW": 43525,
    "Toyota": 34543,
    "Mercedes": 34885,
}

print(bbdd_coches)

# inserción

bbdd_coches["Hyundai"] = 45356
print(bbdd_coches)

# borrado

bbdd_coches.pop("Toyota")
del bbdd_coches["BMW"]
print(bbdd_coches)

# actualización

bbdd_coches["Ford"] = "No disponible"
print(bbdd_coches)

# ordenación

print(sorted(bbdd_coches))

# EJERCICIO 

def func_agenda():
    
    agenda = {
        "borja": 234234243
    }
    
    def nuevo_contacto(nombre, telefono):
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) < 11:
            agenda[nombre] = telefono
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")

    option = input("""
            Introduce una de las siguientes opciones:

            1. Buscar un contacto
            2. Añadir un nuevo contacto
            3. Actualizar un contacto
            4. Eliminar un contacto
            5. Salir """)
            
    if option == "1": 
        nombre = input("Buscar por nombre: ")
        if nombre in agenda:
            print(f"El numero de telefóno de {nombre} es {agenda[nombre]}")
        else:
            print("el nombre no está en la agenda")
    elif option == "2":
        nombre = input("Introduce el nombre del nuevo contacto: ")
        telefono = input("Introduce el telefono del nuevo contacto: ")
        nuevo_contacto(nombre, telefono) 

    elif option == "3":
        nombre = input("Introduce el nombre que quieres actualizar: ")
        if nombre in agenda:
            telefono = input("Introduce el nuevo telefono del contacto: ")
            nuevo_contacto(nombre, telefono) 
        else:
            print("El contacto no existe")

    elif option == "4": 
        nombre = input("Introduce el contacto que quieres eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
        else:
            print("El contacto no existe")
    elif option == "5":
        print("saliendo del programa...")

func_agenda()