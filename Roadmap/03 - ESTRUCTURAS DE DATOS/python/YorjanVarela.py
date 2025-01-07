"""Ejercicio: - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación."""

#Creacion de estructuras de datos

#listas
mi_lista = [1,2,3,4,5]


# Acceder al primer elemento
(mi_lista[0])  # Salida: 1

# Acceder al último elemento
(mi_lista[-1])  # Salida: 5

# Acceder a un rango de elementos
(mi_lista[1:4])  # Salida: [2, 3, 4]   

# Acceder a un rango de elementos con saltos
(mi_lista[::2])  # Salida: [1, 3, 5]

# Agregar un elemento al final de la lista
mi_lista.append(6)
(mi_lista)  # Salida: [1, 2, 3, 4, 5, 6]

# Eliminar un elemento de la lista
mi_lista.remove(3)
(mi_lista)  # Salida: [1, 2, 4, 5, 6]

# Actualizar un elemento de la lista
mi_lista[2] = 7
(mi_lista)  # Salida: [1, 2, 7, 5, 6]


#Tuplas

# Crear una tupla vacía
mi_tupla = ()

# Crear una tupla con elementos
mi_tupla = (1, 2, 3, 4, 5)

# Acceder a un elemento de la tupla
(mi_tupla[0])  # Salida: 1

# Acceder a un rango de elementos de la tupla
(mi_tupla[1:4])  # Salida: (2, 3, 4)

# Acceder a un rango de elementos de la tupla con saltos
(mi_tupla[::2])  # Salida: (1, 3, 5)   

# Acceder a la longitud de la tupla
(len(mi_tupla))  # Salida: 5

# Acceder a la cantidad de veces que aparece un elemento en la tupla
(mi_tupla.count(3))  # Salida: 1

#conjuntos

# Crear un conjunto vacío
mi_conjunto = set()

# Crear un conjunto con elementos    
mi_conjunto = {1, 2, 3, 4, 5}

# Acceder a un elemento del conjunto    
(mi_conjunto)  # Salida: {1, 2, 3, 4, 5}   

# Agregar un elemento al conjunto
mi_conjunto.add(6)
(mi_conjunto)  # Salida: {1, 2, 3, 4, 5, 6}

# Eliminar un elemento del conjunto
mi_conjunto.remove(3)
(mi_conjunto)  # Salida: {1, 2, 4, 5, 6}

# Actualizar un elemento del conjunto
mi_conjunto.update({3})
(mi_conjunto)  # Salida: {1, 2, 3, 4, 5, 6}

# DICCIONARIOS

# Crear un diccionario vacío
mi_diccionario = {}

# Crear un diccionario con elementos
mi_diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}   

# Acceder a un elemento del diccionario
(mi_diccionario["clave1"])  # Salida: "valor1"

# Acceder a todos los elementos del diccionario 
(mi_diccionario)  # Salida: {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}

# Agregar un elemento al diccionario
mi_diccionario["clave4"] = "valor4"
(mi_diccionario)  # Salida: {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3', 'clave4': 'valor4'}

# Eliminar un elemento del diccionario
del mi_diccionario["clave2"]
(mi_diccionario)  # Salida: {'clave1': 'valor1', 'clave3': 'valor3', 'clave4': 'valor4'}


#Programa extra agenda de contactos por terminal   



agenda = {
    "Lucas": 12345678,   
    "Luis": 23456789,
    "Maria": 34567890}  #parte basica de la agenda de contactos. Basicamente un diccionario y así es como quiero que se muestre en terminal

def mostrar_lista(agenda): #definimos la funcion para mostrar la lista de contactos
    print("Lista de contactos:")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")

def insertar_contacto(agenda): #definimos la funcion para insertar un contacto
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el número de teléfono: ")
    if telefono.isdigit() and len(telefono) <= 11:
        agenda[nombre] = telefono
        print("Contacto agregado.")
    else:
        print("Número de teléfono no válido.")

def buscar_contacto(agenda): #definimos la funcion para buscar un contacto
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in agenda:
        print(f"El número de teléfono de {nombre} es {agenda[nombre]}")
    else:
        print("Contacto no encontrado.")

def actualizar_contacto(agenda): #definimos la funcion para actualizar un contacto
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in agenda:
        nuevo_numero = input("Introduce el nuevo número de telón: ")
        if nuevo_numero.isdigit() and len(nuevo_numero) <= 11:
            agenda[nombre] = nuevo_numero
            print("Contacto actualizado.")
        else:
            print("Numero de telón no valido.")
    else:
        print("Contacto no encontrado.")    

def eliminar_contacto(agenda): #definimos la funcion para eliminar un contacto
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado.")
    else:
        print("Contacto no encontrado.")

def mostrar_menu(): #definimos la funcion para mostrar el menu
    print("1. Insertar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar lista de contactos")
    print("6. Salir")
    opcion = input("Seleccione una opcción: ")
    return opcion

def main(): #definimos la funcion principal
    agenda = {}
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            insertar_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            actualizar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            mostrar_lista(agenda)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main() #llamamos a la funcion principal

