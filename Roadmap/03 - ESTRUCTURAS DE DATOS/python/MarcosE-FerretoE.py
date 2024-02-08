"""EJERCICIO:
"""

# Estructuras


# Lista
mi_lista_lenguajes = ["Python", "Java", "Kotlin", "Dart", "JavaScript", "C"]
print(mi_lista_lenguajes)  # Lista original


mi_lista_lenguajes.append("Swift")  # Insertar al final
print(mi_lista_lenguajes)
mi_lista_lenguajes.insert(2, "Go")  # Insertar en una posición específica
print(mi_lista_lenguajes)


mi_lista_lenguajes.remove("Python")  # Borrado
print(mi_lista_lenguajes)
mi_lista_lenguajes.pop()  # Eliminar el último elemento
print(mi_lista_lenguajes)

mi_lista_lenguajes[4] = "TypeScript"  # actualización
print(mi_lista_lenguajes)

mi_lista_lenguajes.sort()
print(mi_lista_lenguajes)  # ordenación

# Tupla (No se puede alterar, es inmutable)
mi_tupla_coordenadas = (56, 112, 100)


# Set (No se puede ordenar)
mi_set_colores = {"Azul", "Rojo", "Morado", "Celeste", "Amarillo"}
print(mi_set_colores)  # Set original

mi_set_colores.add("Verde")  # Inserción
print(mi_set_colores)

mi_set_colores.remove("Azul")  # Borrado
print(mi_set_colores)

# Diccionario
mi_diccionario = {
    "Python": 1991,
    "Java": 1995,
}
print(mi_diccionario)  # Diccionario original

mi_diccionario["JavaScript"] = "1995"  # Inserción (Agregar un nuevo elemento)
print(mi_diccionario)

del mi_diccionario["Python"]  # Borrado (Eliminar un elemento por su clave)
print(mi_diccionario)

mi_diccionario["Java"] = "29"  # Actualización (Modificar el valor de una clave)
print(mi_diccionario)

# Cadenas
mi_cadena_nombre = "Python"
mi_cadena_hola = "Hola, mundo!"


"""DIFICULTAD EXTRA
"""

contactos = []


# Función para añadir un contacto
def agregar_contacto(nombre, telefono):
    # Comprueba que el número de teléfono es válido
    if not telefono.isdigit() or len(telefono) > 8:
        print("El número de teléfono no es válido.")
        print("Debes introducir un numero máximo de 8 dígitos.")
        return

    # Añadimos el contacto a la lista
    contactos.append({"nombre": nombre, "telefono": telefono})


# Función para buscar un contacto
def buscar_contacto(nombre):
    # Buscamos el contacto en la lista
    for contacto in contactos:
        if contacto["nombre"] == nombre:
            return contacto

    # Si no se encuentra el contacto, devolvemos None
    return None


# Función para actualizar un contacto
def actualizar_contacto(nombre, nuevo_nombre, nuevo_telefono):
    # Buscamos el contacto en la lista
    contacto = buscar_contacto(nombre)

    # Si no se encuentra el contacto, devolvemos None
    if contacto is None:
        return None

    # Actualizamos el contacto
    contacto["nombre"] = nuevo_nombre
    contacto["telefono"] = nuevo_telefono


# Función para eliminar un contacto
def eliminar_contacto(nombre):
    # Buscamos el contacto en la lista
    contacto = buscar_contacto(nombre)

    # Si no se encuentra el contacto, devolvemos None
    if contacto is None:
        return None

    # Eliminamos el contacto de la lista
    contactos.remove(contacto)


# Función para mostrar los contactos
def mostrar_contactos():
    if not contactos:
        print("No hay contactos.")
        return

    # Recorremos la lista de contactos y mostramos cada contacto
    for contacto in contactos:
        print(f"{contacto['nombre']}: {contacto['telefono']}")


# Función principal
def main():
    print("Agenda de contactos")
    print("-------------------")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar contactos")
    print("6. Salir")

    # Pedimos al usuario que elija una opción
    opcion = input("Elige una opción: ")

    while opcion != "6":

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            agregar_contacto(nombre, telefono)

        elif opcion == "2":
            nombre = input("Nombre: ")
            contacto = buscar_contacto(nombre)

            if contacto is None:
                print("El contacto no existe.")

            else:
                print(f"Nombre: {contacto['nombre']}")
                print(f"Teléfono: {contacto['telefono']}")

        elif opcion == "3":
            nombre = input("Nombre: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            actualizar_contacto(nombre, nuevo_nombre, nuevo_telefono)

        elif opcion == "4":
            nombre = input("Nombre: ")
            eliminar_contacto(nombre)

        elif opcion == "5":
            mostrar_contactos()

        elif opcion == "6":
            exit()

        else:
            print("Opción no válida.")

        print("Agenda de contactos")
        print("-------------------")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar contactos")
        print("6. Salir")

        opcion = input("Elige una opción: ")


if __name__ == "__main__":
    main()
