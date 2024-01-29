# Listas

# Lista vacia
lista: list = []

# Lista con elementos
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)

# Inserción al final de la lista
mi_lista.append(6)
print(mi_lista)

# Borrado de un elemento por valor
mi_lista.remove(3)
print(mi_lista)

# Borrado de un elemento por posición
del mi_lista[1]
print(mi_lista)

# Actualización de un elemento por índice
mi_lista[1] = 10
print(mi_lista)

# Búsqueda de un elemento por posición
elemento_en_posicion = mi_lista[2]
print(elemento_en_posicion)

# Ordenación de la lista
mi_lista.sort()
print(mi_lista)

# -----------------------------------------------

# Tuplas

# Creación de una tupla
mi_tupla: tuple = (1, 2, 3, 4, 5)
print(mi_tupla)
# No se pueden realizar operaciones de inserción, borrado o actualización en tuplas

# Tipo de estructura de datos
print(type(mi_tupla))

# Ordenación de la tupla
mi_tupla_ordenada = tuple(sorted(mi_tupla))
print(mi_tupla_ordenada)

# -----------------------------------------------

# Sets

# Update - Elimina y agrega un nuevo dato

# Sort - NO se pueden ordenar

# Creación de un conjunto
mi_conjunto: set = {1, 2, 3, 4, 5}

# Inserción de un elemento
mi_conjunto.add(6)

# Borrado de un elemento por valor
mi_conjunto.remove(3)

# No se pueden realizar operaciones de actualización en conjuntos
# No se garantiza un orden específico en los conjuntos

print(mi_conjunto)

conjunto_ordenado = set(sorted(mi_conjunto))


# -----------------------------------------------

# Diccionarios

# Creación de un diccionario
mi_diccionario: dict = {'a': 1, 'b': 2, 'c': 3}

# Acceder a un valor por medio de la clave
print(mi_diccionario['a'])

# Inserción/Actualización de un par clave-valor
mi_diccionario['d'] = 4

# Borrado de un elemento por clave
del mi_diccionario['b']

# No se pueden realizar operaciones de ordenación en diccionarios

print(mi_diccionario)

# Ordenación

dict_ordenado = dict(sorted(mi_diccionario.items()))
print(dict_ordenado)

# ----------------------------------------------

# DIFICULTAD EXTRA (opcional):

# Busqueda, inserción, actualización y eliminación
# Contacto (nombre, numero de telefono)
# Solicita que operación desea realizar y luego los datos para realizarla
# Evaluar los numeros de telefono para que sean solo numeros y de 11 dijitos
# También se debe proponer una operación de finalización del programa.

def validar_telefono(telefono):
    return len(telefono) == 11 and telefono.isdigit()

def mi_agenda(agenda: dict):
    while True:
        print("--- Agenda personal ---")
        print('''
            Opciones:
                1. Buscar
                2. Insertar
                3. Actualizar
                4. Eliminar
                0. Salir
            ''')
        
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            contacto_buscar = input("Ingresa el nombre del contacto que deseas buscar: ")
            if contacto_buscar in agenda:
                print("Nombre: ", contacto_buscar, " - Teléfono: ", agenda[contacto_buscar])
            else:
                print("Contacto no encontrado")

        elif opcion == 2:
            nombre_agregar = input("Ingresa el nombre: ")
            telefono_agregar = input("Ingresa el número telefónico: ")
            if validar_telefono(telefono_agregar):
                agenda[nombre_agregar] = telefono_agregar
                print("Agenda: \n", agenda.items())
            else:
                print("El número de teléfono no tiene el formato correcto")

        elif opcion == 3:
            nombre_actualizar = input("Ingresa el nombre del contacto que deseas actualizar: ")
            if nombre_actualizar in agenda:
                print("No se permite actualizar el nombre, solo el número de teléfono")
                numero_actualizar = input("Ingresa el número del contacto que deseas actualizar (11 dígitos y solo caracteres numéricos): ")
                if validar_telefono(numero_actualizar):
                    agenda[nombre_actualizar] = numero_actualizar
                    print("Agenda: \n", agenda.items())
                else:
                    print("El número de teléfono no tiene el formato correcto")
            else:
                print("El contacto no existe")

        elif opcion == 4:
            nombre_eliminar = input("Ingresa el nombre del contacto que deseas eliminar: ")
            if nombre_eliminar in agenda:
                del agenda[nombre_eliminar]
                print("Contacto eliminado satisfactoriamente")
                print("Agenda: \n", agenda.items())
            else:
                print("Contacto no encontrado")

        elif opcion == 0:
            print("Ha salido de su agenda de contactos")
            break

mi_agenda({"Jesus": "3209029933", "Maria": "3150987732"})


