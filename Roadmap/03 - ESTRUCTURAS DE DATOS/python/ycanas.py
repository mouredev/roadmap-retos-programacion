# --------- Estructuras de Datos

# I. Listas

print("\n" + " Listas ".center(60, "-") + "\n")

mi_lista = [1, 2, 3, 4, 5]
print("creación", mi_lista)

mi_lista.append(6)
print("inserción (append)", mi_lista)

mi_lista.extend([7, 8])
print("inserción (extend)", mi_lista)

mi_lista.insert(0, 0)
print("inserción (insert)", mi_lista)

mi_lista[8] = -1
print("actualización ([])", mi_lista)

mi_lista.sort()
print("ordenación (sort)", mi_lista)

mi_lista.remove(-1)
print("borrado (remove)", mi_lista)

mi_lista.pop(0)
print("borrado (pop)", mi_lista)

mi_lista.clear()
print("borrado (clear)", mi_lista)


# II. Tuplas

print("\n" + " Tuplas ".center(60, "-") + "\n")

mi_tupla = (1, 2, 3, 4)
print("creación", mi_tupla)

print("Las tuplas son inmutables, no se pueden insertar, borrar o actualizar elementos una vez creadas.")


# III. Conjuntos

print("\n" + " Conjuntos ".center(60, "-") + "\n")

mi_conjunto = {"manzana", "pera", "naranja", "durazno"}
print("creación", mi_conjunto)

mi_conjunto.add("mandarina")
print("inserción (add)", mi_conjunto)

mi_conjunto.update(["fresa", "lulo"])
print("actualización", mi_conjunto)

print("Los diccionarios no son colecciones ordenadas")

mi_conjunto.remove("manzana")
print("borrado (remove)", mi_conjunto)

mi_conjunto.discard("fresa")
print("borrado (discard)", mi_conjunto)


# IV. Diccionarios

print("\n" + " Diccionarios ".center(60, "-") + "\n")

mi_diccionario = {"nombre": "yair", "apellido": "cañas"}
print("creación", mi_diccionario)

mi_diccionario["altura"] = 1.76
print("inserción ([])", mi_diccionario)

mi_diccionario.update({"altura": 1.75})
print("actualización (update)", mi_diccionario)

mi_diccionario["altura"] = 1.76
print("actualización ([])", mi_diccionario)

mi_diccionario = dict(sorted(mi_diccionario.items()))
print("ordenación (sorted())", mi_diccionario)

mi_diccionario.pop("altura")
print("borrado (pop)", mi_diccionario)

mi_diccionario.popitem()
print("borrado (popitem)", mi_diccionario)

mi_diccionario.clear()
print("borrado (clear)", mi_diccionario)


# --------- Extra

contactos = {"Esposa": 3123456789, "Novia1": 3112345678, "Novia2": 3101234567}
print("\n" + " Agenda ".center(60, "-"))

while True:
    opcion = None

    while opcion is None:
        numero = input(
            "\n1. Ver Contactos" + 
            "\n2. Buscar contacto" + 
            "\n3. Guardar contacto" + 
            "\n4. Eliminar contacto" + 
            "\n5. Actualizar contacto." + 
            "\n0. Salir." + 
            "\n\nOpcion: "
        )

        if numero.isdigit():
            opcion = int(numero)


    if opcion == 1:
        print("\nContactos: \n")
        for nombre, numero in sorted(contactos.items()):
            print(nombre + ':', numero)


    elif opcion == 2:
        if not bool(contactos):
            print("contactos vacios")
            continue
        
        
        busqueda = input("\nNombre del contacto: ")

        if not busqueda in contactos:
            print("El contacto no existe.")
            continue
        
        print("Número:", contactos[busqueda])


    elif opcion == 3:
        numero = input("Número de contacto: ")

        if not numero.isdigit():
            print("Número no valido.")
            continue

        if int(numero) in contactos.values():
            print("El número ya existe.")
            continue

        numero = int(numero)

        nombre = input("Nombre del contacto: ")

        if nombre in contactos.keys():
            print("El contacto ya existe.")
            continue

        contactos[nombre.title()] = numero


    elif opcion == 4:
        nombre = input("Nombre del contacto: ")

        if not nombre in contactos.keys():
            print("El contacto no existe.")
            continue

        contactos.pop(nombre)
        print("Contacto eliminado.")


    elif opcion == 5:
        nombre = input("Nombre del contacto: ")

        if not nombre in contactos.keys():
            print("El contacto no existe.")
            continue

        
        numero = input("Número de contacto: ")

        if not numero.isdigit():
            print("Número no valido.")
            continue

        contactos[nombre] = numero

    else:
        break