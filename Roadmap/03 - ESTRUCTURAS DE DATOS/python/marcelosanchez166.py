# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.

# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#   los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
#   (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.

lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
sets = {1, 2, 3, 4, 5}
# Operaciones con lista
lista.append(6)  # Inserción
lista.remove(2)  # Borrado
lista[0] = 10  # Actualización
lista.sort()  # Ordenación
print("Lista:", lista)

# Operaciones con tupla (inmutable, no se pueden modificar)
print("Tupla:", tupla)
# Tuplas no permiten inserción, borrado o actualización, pero se pueden crear nuevas tuplas
tupla_nueva = tupla + (6,)  # Creación de nueva tupla
print("Nueva tupla:", tupla_nueva)
# Tuplas no permiten ordenación, pero se pueden convertir a lista
tupla_a_lista = list(tupla)
print("Tupla convertida a lista:", tupla_a_lista)


# Operaciones con diccionario
diccionario["edad"] = 31  # Actualización
diccionario["pais"] = "España"  # Inserción
print("Diccionario:", diccionario)
diccionario.pop("ciudad")  # Borrado
print("Diccionario después de borrar ciudad:", diccionario)
# Ordenación de diccionario por claves
diccionario_ordenado = dict(sorted(diccionario.items()))
print("Diccionario ordenado por claves:", diccionario_ordenado)
# Ordenación de diccionario por valores
diccionario_ordenado_valores = dict(sorted(diccionario.items()))
print("Diccionario ordenado por valores:", diccionario_ordenado_valores)


# Operaciones con sets
sets.add(6)  # Inserción
sets.discard(2)  # Borrado
print("Set:", sets)
# Sets no permiten actualización, pero se pueden crear nuevos sets
sets_nuevo = sets.union({7, 8})  # Creación de nuevo set
print("Nuevo set:", sets_nuevo)

# Agenda de contactos
agenda = {}


def agregar_contacto(nombre, telefono):
    if telefono.isdigit() and len(telefono) <= 11:
        agenda[nombre] = telefono
        print(f"Contacto {nombre} agregado con éxito.")
    else:
        print("Número de teléfono no válido. Debe ser numérico y tener hasta 11 dígitos.")


def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"Contacto encontrado: {nombre} - {agenda[nombre]}")
    else:
        print(f"Contacto {nombre} no encontrado.")


def actualizar_contacto(nombre, telefono):
    if nombre in agenda:
        if telefono.isdigit() and len(telefono) <= 11:
            agenda[nombre] = telefono
            print(f"Contacto {nombre} actualizado con éxito.")
        else:
            print("Número de teléfono no válido. Debe ser numérico y tener hasta 11 dígitos.")
    else:
        print(f"Contacto {nombre} no encontrado.")


def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print(f"Contacto {nombre} no encontrado.")


def mostrar_agenda():
    if agenda:
        print("Agenda de contactos:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    else:
        print("La agenda está vacía.")


def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar agenda")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agregar_contacto(nombre, telefono)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a actualizar: ")
            telefono = input("Ingrese el nuevo número de teléfono: ")
            actualizar_contacto(nombre, telefono)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == "5":
            mostrar_agenda()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
