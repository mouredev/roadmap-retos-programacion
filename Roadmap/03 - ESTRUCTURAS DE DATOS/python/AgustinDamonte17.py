# ===================================
# PARTE 1: ESTRUCTURAS Y OPERACIONES
# ===================================

print("====== ESTRUCTURAS DE PYTHON ======")

# LISTA
lista = [3, 1, 4]
print("Lista inicial:", lista)
lista.append(2)  # inserción
print("Lista tras append:", lista)
lista[1] = 10  # actualización
print("Lista tras actualización:", lista)
lista.remove(4)  # borrado
print("Lista tras remove:", lista)
lista.sort() #ordenación
print("Lista ordenada:", lista)
print()

# TUPLA (inmutable, pero se puede crear)
tupla = (1, 2, 3)
print("Tupla:", tupla)
print()

# SET (Posición variable - no se puede ordenar)
conjunto = {5, 2, 8}
print("Set inicial:", conjunto)
conjunto.add(10)  # inserción
print("Set tras add:", conjunto)
conjunto.discard(2)  # borrado
print("Set tras discard:", conjunto)
# No se puede ordenar un set directamente, pero sí convertir
print("Set ordenado (como lista):", sorted(conjunto))
print()

# DICCIONARIO
diccionario = {"a": 1, "b": 2}
print("Diccionario inicial:", diccionario)
diccionario["c"] = 3  # inserción
print("Diccionario tras inserción:", diccionario)
diccionario["a"] = 100  # actualización
print("Diccionario tras actualización:", diccionario)
del diccionario["b"]  # borrado
print("Diccionario tras borrado:", diccionario)
# Ordenar por clave
print("Diccionario ordenado por clave:", dict(sorted(diccionario.items())))
print()

# STRING
texto = "hola mundo"
print("Texto original:", texto)
print("Texto en mayúsculas:", texto.upper())
print("Texto reemplazado:", texto.replace("hola", "hello"))
print()


# ===================================
# PARTE 2: AGENDA DE CONTACTOS (MENÚ)
# ===================================

def validar_telefono(numero):
    return numero.isdigit() and len(numero) <= 11

def mostrar_menu():
    print("\n====== AGENDA DE CONTACTOS ======")
    print("1. Insertar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos")
    print("6. Salir")

agenda = {}

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-6): ")

    if opcion == "1":
        nombre = input("Nombre: ").strip()
        telefono = input("Teléfono: ").strip()
        if validar_telefono(telefono):
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' agregado.")
        else:
            print("Teléfono inválido. Debe ser numérico y de hasta 11 dígitos.")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ").strip()
        if nombre in agenda:
            print(f"{nombre}: {agenda[nombre]}")
        else:
            print("Contacto no encontrado.")

    elif opcion == "3":
        nombre = input("Nombre a actualizar: ").strip()
        if nombre in agenda:
            nuevo_telefono = input("Nuevo teléfono: ").strip()
            if validar_telefono(nuevo_telefono):
                agenda[nombre] = nuevo_telefono
                print("Contacto actualizado.")
            else:
                print("Teléfono inválido.")
        else:
            print("Contacto no encontrado.")

    elif opcion == "4":
        nombre = input("Nombre a eliminar: ").strip()
        if nombre in agenda:
            del agenda[nombre]
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")

    elif opcion == "5":
        if not agenda:
            print("Agenda vacía.")
        else:
            print("Contactos:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")
