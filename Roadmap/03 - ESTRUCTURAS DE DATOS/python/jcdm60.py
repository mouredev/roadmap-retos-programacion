# #03 ESTRUCTURAS DE DATOS
#### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

## Ejercicio

#
# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#
# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#   los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
#   (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.
#

# LISTAS
# Creación de una lista
mi_lista = [1, 2, 3, 4, 5]

# Inserción de un elemento al final de la lista
mi_lista.append(6)

# Borrado de un elemento por valor
mi_lista.remove(2)

# Actualización de un elemento por índice
mi_lista[1] = 15

# Ordenación de la lista
mi_lista.sort()

print(mi_lista)

# TUPLAS
# Creación de una tupla
mi_tupla = (1, 2, 3, 4, 5)

# Acceso a un elemento por índice
elemento = mi_tupla[3]

# Concatenación de tuplas
nueva_tupla = mi_tupla + (6, 7, 8)

print(elemento)
print(nueva_tupla)

# CONJUNTOS
# Creación de un conjunto
mi_conjunto = {1, 2, 3, 4, 5}

# Inserción de un elemento
mi_conjunto.add(6)

# Borrado de un elemento por valor
mi_conjunto.remove(3)

# Actualización del conjunto con otro conjunto
mi_conjunto.update({7, 8, 9})

print(mi_conjunto)

# AGENDA DE CONTACTOS
agenda = {}

def mostrar_menu():
    print("\n** Agenda de Contactos **")
    print("1. Mostrar contactos")
    print("2. Buscar contacto")
    print("3. Añadir contacto")
    print("4. Actualizar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")

def mostrar_contactos():
    print("\n** Lista de Contactos **")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print(f"{nombre} no encontrado en la agenda.")

def añadir_contacto():
    nombre = input("Ingrese el nombre del nuevo contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    
    if telefono.isdigit() and len(telefono) <= 11:
        agenda[nombre] = telefono
        print(f"Contacto {nombre} añadido correctamente.")
    else:
        print("Número de teléfono no válido. Asegúrate de ingresar un número numérico máximo de 11 dígitos.")

def actualizar_contacto():
    nombre = input("Ingrese el nombre del contacto a actualizar: ")
    if nombre in agenda:
        nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
        
        if nuevo_telefono.isdigit() and len(nuevo_telefono) <= 11:
            agenda[nombre] = nuevo_telefono
            print(f"Contacto {nombre} actualizado correctamente.")
        else:
            print("Número de teléfono no válido. Asegúrate de ingresar un número numérico máximo de 11 dígitos.")
    else:
        print(f"{nombre} no encontrado en la agenda.")

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado correctamente.")
    else:
        print(f"{nombre} no encontrado en la agenda.")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == '1':
        mostrar_contactos()
    elif opcion == '2':
        buscar_contacto()
    elif opcion == '3':
        añadir_contacto()
    elif opcion == '4':
        actualizar_contacto()
    elif opcion == '5':
        eliminar_contacto()
    elif opcion == '6':
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 6.")

