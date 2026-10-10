# Listas en Python
from re import match
from unittest import case


mi_lista = [1, 2, 3, 4, 5]
mi_lista.append(6) # Inserción al final de la lista
print(mi_lista)
if 3 in mi_lista: # Busqueda
    print("El número 3 está en la lista.")
mi_lista.remove(2) # Eliminación de un elemento
print(mi_lista)
mi_lista.insert(1, 2) # Inserción en una posición específica
print(mi_lista)
print(type(mi_lista)) # Mostrar el tipo de dato
#Tuplas
mi_tupla = ("1", "2", "3", "4", "5")
print(mi_tupla)
mi_tupla = mi_tupla.count("3") # Contar cuántas veces aparece un elemento
print(f"El número 3 aparece {mi_tupla} veces en la tupla.")
#Conjuntos
mi_conjunto = {1, 2, 3, 4, 5}
mi_conjunto.add(6) # Inserción de un elemento
print(mi_conjunto)
if 3 in mi_conjunto: # Búsqueda
    print("El número 3 está en el conjunto.")
else:
    print("El número 3 no está en el conjunto.")    
mi_conjunto.remove(2) # Eliminación de un elemento
print(mi_conjunto)
mi_conjunto.add(2) # Inserción de un elemento
print(mi_conjunto)
#Diccionarios
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario)
mi_diccionario["edad"] = 31 # Modificación de un valor
print(mi_diccionario)
if "nombre" in mi_diccionario: # Búsqueda de una clave
    print("La clave 'nombre' está en el diccionario.")
print(mi_diccionario["nombre"]) # Mostrar el valor de la clave "nombre"
del mi_diccionario["ciudad"] # Eliminación de una clave
print(mi_diccionario)
print(type(mi_diccionario)) # Mostrar el tipo de dato
mi_diccionario["pais"] = "España" # Inserción de una nueva clave-valor
print(mi_diccionario)

#Extra

def comprobar_telefono(telefono):
    if len(telefono) <= 11 and telefono.isdigit():
        return True
    else:
        print("El número de teléfono debe tener como máximo 11 dígitos y solo contener números.")

    
mi_directorio = {}

while True:
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")                                               
    opcion = input("Seleccione una opción: ")
    match(opcion):
        case "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            if comprobar_telefono(telefono):
                mi_directorio.update({nombre: telefono})
        case "2":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            if nombre in mi_directorio:             
                 print(f"Nombre: {nombre}, Teléfono: {mi_directorio[nombre]}")
            else:
                print("Contacto no encontrado.")        
        case "3":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if nombre in mi_directorio:
                del mi_directorio[nombre]
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")        
        case "4":
            print(f"Contacto en el directorio: {mi_directorio}")
        case "5":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")    