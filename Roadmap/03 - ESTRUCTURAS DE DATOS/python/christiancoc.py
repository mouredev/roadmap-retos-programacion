# Listas
lista_vacia = []

# Lista con elementos
lista_str = ["a", "b", "c", "d"]
lista_num = [1, 2, 3, 4]
lista_boolean = [True, False, True, False]
lista_multiple = ["a", 1, True]
lista_anidada = [lista_str, lista_num, lista_boolean, lista_multiple]

# Insercion
lista_str.append("e")
lista_num.insert(1, 5)

# Borrado
lista_boolean.pop(3)
lista_multiple.remove("a")
lista_anidada.clear()

# Actualizacion
lista_str[0] = "f"

# Ordenacion
lista_desordenada = [4, 3, 2, 1, 0]
lista_desordenada.sort()

# Tuplas (inmutables)
tupla_vacia = ()

# Tuplas con elementos
tupla_str = ("a", "b", "c", "d")
tupla_num = (1, 2, 3, 4)
tupla_boolean = (True, False, True, False)
tupla_multiple = ("a", 1, True)
tupla_anidada = (tupla_str, tupla_num, tupla_boolean, tupla_multiple)

# Conjuntos o sets
conjunto_vacio = set()

# Conjuntos o sets con elementos
conjunto_str = {"a", "b", "c", "d"}
conjunto_num = {1, 2, 3, 4}
conjunto_boolean = {True, False, True, False}
conjunto_multiple = {"a", 1, True}

# Insercion
conjunto_vacio.add("Christian")

# Borrado
conjunto_str.remove("b")
conjunto_num.discard(4)
conjunto_multiple.pop()

# Diccionarios
diccionario_vacio = {}

# Diccionarios con elementos
mi_diccionario = {
    "nombre": "Christian",
    "apellido": "Coc",
    "edad": 26,
    "estatura": 1.90,
    "active": True,
}

# Insercion
diccionario_vacio["nacimiento"] = 2000
diccionario_vacio.update({"año": 2024})

# Borrado
del diccionario_vacio["nacimiento"]
mi_diccionario.pop("active")

# Actualizacion
mi_diccionario["estatura"] = 1.85

# Extra

def agregar_contacto(agenda, nombre, telefono):
    if len(str(telefono)) > 11 or not telefono.isdigit():
        print("El número de teléfono es incorrecto")
    else:
        contacto = {"nombre": nombre, "telefono": telefono}
        agenda[nombre] = telefono
        print("Contacto agregado:", contacto)

def buscar_contacto(agenda, nombre):
    encontrado = False
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            print("Contacto encontrado:", contacto)
            encontrado = True
            break
    if not encontrado:
        print("No se encontró el contacto")

def actualizar_contacto(agenda, nombre, nuevo_telefono):
    encontrado = False
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            contacto["telefono"] = nuevo_telefono
            print("Contacto actualizado:", contacto)
            encontrado = True
            break
    if not encontrado:
        print("No se encontró el contacto")

def eliminar_contacto(agenda, nombre):
    encontrado = False
    for i, contacto in enumerate(agenda):
        if contacto["nombre"] == nombre:
            del agenda[i]
            print("Contacto eliminado:", nombre)
            encontrado = True
            break
    if not encontrado:
        print("No se encontró el contacto")

def mi_agenda():
    agenda_contactos = []
    while True:
        print("*---------------------*")
        print("* AGENDA DE CONTACTOS *")
        print("*---------------------*")
        print("Hola, ¿qué operación deseas realizar?")
        print("1. Agregar un contacto")
        print("2. Buscar un contacto")
        print("3. Actualizar un contacto")
        print("4. Eliminar un contacto")
        print("5. Salir")

        opcion = input("Ingresa el número de la operación que deseas realizar: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del contacto: ")
            telefono = input("Ingresa el número de teléfono del contacto: ")
            agregar_contacto(agenda_contactos, nombre, telefono)
        elif opcion == "2":
            nombre = input("Ingresa el nombre del contacto: ")
            buscar_contacto(agenda_contactos, nombre)
        elif opcion == "3":
            nombre = input("Ingresa el nombre del contacto: ")
            nuevo_telefono = input("Ingresa el nuevo número de teléfono: ")
            actualizar_contacto(agenda_contactos, nombre, nuevo_telefono)
        elif opcion == "4":
            nombre = input("Ingresa el nombre del contacto: ")
            eliminar_contacto(agenda_contactos, nombre)
        elif opcion == "5":
            print("Hasta pronto")
            break
        else:
            print("Opción no válida")

mi_agenda()



