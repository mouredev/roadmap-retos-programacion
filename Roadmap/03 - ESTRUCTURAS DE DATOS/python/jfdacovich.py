"""
Estructuras de datos en Python
"""

# Listas
print("----------Listas----------")
my_list = [3, 2, 1, 4, 5, 7, 8, 1, 21, 32]
print(my_list)
my_list.append("hola") # Agregar un elemento al final de la lista
print(my_list)
my_list.insert(3, "Insertado") # Insertar elementos en una posición específica
print(my_list)
my_list.remove("hola") # Eliminando elementos
print(my_list)
my_list.pop(3) # Eliminando elementos por posición
print(my_list)
my_list.sort() # Ordenando elementos
print(my_list)
print(my_list.count(1)) # Contnado elementos
my_list.reverse() # Invirtiendo el orden los elementos
print(my_list)

# Tuplas
print("----------Tuplas----------")
my_tuple = ("jfdacovich", "python", 3, 3, 2, 1)
print(my_tuple.count(3)) # Contando elementos
print(my_tuple.index("python")) # Buscando elementos
print(my_tuple[1]) # Accediendo a elementos
print(my_tuple[1:3]) # Accediendo a un rango de elementos
print(my_tuple)

# Diccionarios
print("----------Diccionarios----------")
my_dict = {"nombre": "jfdacovich", "edad": 111, "ciudad": "Xxxxxx"}
print(my_dict)
print(my_dict["nombre"]) # Accediendo a elementos
print(my_dict.get("nombre")) # Accediendo a elementos
my_dict["nombre"] = "jfdacovich2" # Modificando elementos
print(my_dict)
my_dict["apellido"] = "Python" # Agregando elementos
print(my_dict)
print(my_dict.keys()) # Obteniendo las llaves
print(my_dict.values()) # Obteniendo los valores
print(my_dict.items()) # Obteniendo los elementos
print(my_dict.pop("nombre")) # Eliminando elementos
print(my_dict)
my_dict.clear() # Limpiando el diccionario
my_dict.update({"nombre": "jfdacovich", "edad": 111, "ciudad": "Xxxxxx"}) # Actualizando el diccionario
my_dict2 = my_dict.copy() # Copiando el diccionario
print(my_dict2)
my_dict2.pop("nombre")
print(my_dict2)
del my_dict2["edad"] # Eliminando elementos

# Conjuntos
print("----------Conjuntos----------")
my_set = {"jfdacovich", "python", 3, 3, 2, 1}
print(my_set)
my_set.add("hola") # Agregando elementos
print(my_set)
print(my_set.discard("python")) # Eliminando elementos
print(my_set)
print(my_set.pop()) # Eliminando elementos
print(my_set)
# print(my_set.clear()) # Limpiando el conjunto
print(f"my_set: {my_set}")
my_set2 = {1, 2, 3, 4, "java", "sql"}
print(my_set2.union(my_set)) # Uniendo conjuntos
print(my_set2.intersection(my_set)) # Intersecando conjuntos
print(my_set2.difference(my_set)) # Diferencia de conjuntos
print(my_set2.symmetric_difference(my_set)) # Diferencia simétrica de conjuntos
my_set2.update(my_set) # Actualizando el conjunto
print(my_set2)
my_set2.remove("jfdacovich") # Eliminando elementos
print(my_set2)
my_set2.clear() # Limpiando el conjunto
print(my_set2)

"""
Extra
"""

def agenda():
    print("----------Agenda----------")
    contactos = {}
    def buscar_contacto(nombre):
        if nombre in contactos:
            print(f"El número de teléfono de {nombre} es {contactos[nombre]}")
        else:
            print("El contacto no existe")

    def validacion_actualizacion(nombre, telefono):
        if telefono.isdigit() and 0 < len(telefono) <= 11:
            contactos[nombre] = telefono
            return True
        return False

    def agregar_contacto(nombre, telefono):
        if validacion_actualizacion(nombre, telefono):
            print("Contacto agregado correctamente")
        else:
            print("Número de teléfono inválido")

    def actualizar_contacto(nombre, telefono):
        if nombre in contactos:
            if validacion_actualizacion(nombre, telefono):
                print("Contacto actualizado correctamente")
            else:
                print("Número de teléfono inválido")
        else:
            print("El contacto no existe")

    def eliminar_contacto(nombre):
        if nombre in contactos:
            del contactos[nombre]
            print("Contacto eliminado correctamente")
        else:
            print("El contacto no existe")

    while True:
        print("----------Menú:")
        print("1. Buscar contacto")
        print("2. Agregar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("\nIngrese una opción: ")

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del contacto: ")
                buscar_contacto(nombre)
            case "2":
                nombre = input("Ingrese el nombre del contacto: ")
                telefono = input("Ingrese el número de teléfono del contacto: ")
                agregar_contacto(nombre, telefono)
            case "3":
                nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
                telefono = input("Ingrese el nuevo número de teléfono del contacto: ")
                actualizar_contacto(nombre, telefono)
            case "4":
                nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
                eliminar_contacto(nombre)
            case "5":
                print("Hasta luego")
                break
            case _:
                print("La opcion que indicas no es válida, por favor intenta de nuevo")

agenda()