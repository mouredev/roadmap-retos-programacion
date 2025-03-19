#1 Estructuras de datos soportadas por defecto en Python

# Listas (mutables, ordenadas)
lista_numeros = [5, 2, 8, 1, 9]
print("Lista original:", lista_numeros)

# Inserción
lista_numeros.append(3)  # Agrega al final
lista_numeros.insert(2, 7)  # Inserta en una posición específica
print("Lista después de inserciones:", lista_numeros)

# Borrado
del lista_numeros[0]  # Borra por índice
lista_numeros.remove(8)  # Borra por valor
print("Lista después de borrados:", lista_numeros)

# Actualización
lista_numeros[1] = 4
print("Lista después de actualización:", lista_numeros)

# Ordenación
lista_numeros.sort()  # Ordena de forma ascendente
print("Lista ordenada:", lista_numeros)

# Tuplas (inmutables, ordenadas)
tupla_colores = ("rojo", "verde", "azul")
print("\nTupla original:", tupla_colores)

# Conjuntos (mutables, no ordenados, sin duplicados)
conjunto_frutas = {"manzana", "pera", "banana"}
print("\nConjunto original:", conjunto_frutas)

conjunto_frutas.add("uva")  # Inserción
conjunto_frutas.remove("pera")  # Borrado
print("Conjunto después de operaciones:", conjunto_frutas)

# Diccionarios (mutables, no ordenados, pares clave-valor)
diccionario_edades = {"Ana": 25, "Carlos": 30, "Laura": 22}
print("\nDiccionario original:", diccionario_edades)

diccionario_edades["Pedro"] = 35  # Inserción
del diccionario_edades["Carlos"]  # Borrado
diccionario_edades["Laura"] = 23  # Actualización
print("Diccionario después de operaciones:", diccionario_edades)

# Ejercicio

contactos = {}  # Diccionario para almacenar los contactos

def agregar_contacto(nombre, telefono):
    if nombre in contactos:
        print("El contacto ya existe.")
    else:
        contactos[nombre] = telefono
        print("Contacto agregado exitosamente.")

def buscar_contacto(nombre):
    if nombre in contactos:
        print(f"El número de teléfono de {nombre} es: {contactos[nombre]}")
    else:
        print("El contacto no existe.")

def actualizar_contacto(nombre, nuevo_telefono):
    if nombre in contactos:
        contactos[nombre] = nuevo_telefono
        print("Contacto actualizado exitosamente.")
    else:
        print("El contacto no existe.")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado exitosamente.")
    else:
        print("El contacto no existe.")

while True:
    operacion = input("¿Qué deseas hacer? (agregar, buscar, actualizar, eliminar, salir): ")

    if operacion == "agregar":
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono del contacto: ")
        agregar_contacto(nombre, telefono)
    elif operacion == "buscar":
        nombre = input("Nombre del contacto: ")
        buscar_contacto(nombre)
    elif operacion == "actualizar":
        nombre = input("Nombre del contacto: ")
        nuevo_telefono = input("Nuevo teléfono del contacto: ")
        actualizar_contacto(nombre, nuevo_telefono)
    elif operacion == "eliminar":
        nombre = input("Nombre del contacto: ")
        eliminar_contacto(nombre)
    elif operacion == "salir":
        break
    else:
        print("Operación no válida.")