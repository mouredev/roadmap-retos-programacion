# Listas
lista = [1, 2, 3, 4, 5]
lista.append(6)  # Inserción
lista.remove(1)  # Borrado
lista[0] = 7  # Actualización
lista.sort(reverse=True)  # Ordenación
print("Lista:", lista)

# Tuplas
tupla = (1, 2, 3, 4, 5)
# Las tuplas son inmutables, por lo que no se pueden insertar, borrar o actualizar elementos
print("Tupla:", tupla)

# Conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)  # Inserción
conjunto.remove(1)  # Borrado
# Los conjuntos son inmutables, por lo que no se pueden actualizar elementos
# Los conjuntos no mantienen un orden, por lo que no se pueden ordenar
print("Conjunto:", conjunto)

# Diccionarios
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
diccionario['f'] = 6  # Inserción
del diccionario['a']  # Borrado
diccionario['b'] = 7  # Actualización
diccionario = dict(sorted(diccionario.items()))  # Ordenación
print("Diccionario:", diccionario)

#Dificultad Extra
agenda = {}

while True:
    print("\n1. Insertar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == '1':
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el número de teléfono del contacto: ")
        if not telefono.isdigit() or len(telefono) > 11:
            print("Número de teléfono no válido")
        else:
            agenda[nombre] = telefono

    elif opcion == '2':
        nombre = input("Introduce el nombre del contacto a buscar: ")
        if nombre in agenda:
            print("El número de teléfono es", agenda[nombre])
        else:
            print("Contacto no encontrado")

    elif opcion == '3':
        nombre = input("Introduce el nombre del contacto a actualizar: ")
        if nombre in agenda:
            telefono = input("Introduce el nuevo número de teléfono: ")
            if not telefono.isdigit() or len(telefono) > 11:
                print("Número de teléfono no válido")
            else:
                agenda[nombre] = telefono
        else:
            print("Contacto no encontrado")

    elif opcion == '4':
        nombre = input("Introduce el nombre del contacto a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
        else:
            print("Contacto no encontrado")

    elif opcion == '5':
        break

    else:
        print("Opción no válida")