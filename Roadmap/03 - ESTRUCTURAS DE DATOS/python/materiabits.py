#listas  (como un array)
mi_lista = [1, 2, 3, 4, 5]
print(f"mi_lista: {mi_lista}")

#agrega un elemento
mi_lista.append(6)
print(f"mi_lista: {mi_lista}")

#elimina un elemento
mi_lista.remove(3)
print(f"mi_lista: {mi_lista}")  

#agrega un elemento en la posicion 2
mi_lista.insert(2, 3)
print(f"mi_lista: {mi_lista}")

#toma el primer valor
mi_lista.pop()
print(f"mi_lista: {mi_lista}")

#asignaun valor a un elemento del array
mi_lista[2] = 10
print(f"mi_lista: {mi_lista}")

#ordena
mi_lista.sort()
print(f"mi_lista: {mi_lista}")  

#elimina
mi_lista.remove(10)
print(f"mi_lista: {mi_lista}")

#amplia los datos que ya estan en el set
#mi_lista.update ([7, 8, 9])
print(f"mi_lista: {mi_lista}")


#diccionario
mi_diccionario = {"nombre": "Juan", 
                "edad": 30, 
                "ciudad": "Madrid"}
print(f"mi_diccionario: {mi_diccionario}")

#tipo de datos
print(type(mi_diccionario))

#update de un valor dando una clave
mi_diccionario["edad"] = 31
print(f"mi_diccionario: {mi_diccionario}")

#borra una clave y su valor
del mi_diccionario["ciudad"]
print(f"mi_diccionario: {mi_diccionario}")

mi_diccionario = dict(sorted(mi_diccionario.items()))
print(f"mi_diccionario: {mi_diccionario}")

#ejercicio extra de estructura de datos

def pedir_telefono():
    while True:
        telefono = input("Número de teléfono (máximo 11 dígitos): ").strip()
        if telefono.isascii() and telefono.isdigit() and len(telefono) <= 11:
            return telefono
        print("El teléfono debe contener solo dígitos y tener como máximo 11.")


def encontrar_contacto(contactos, nombre):
    clave = nombre.casefold()
    return next(
        (nombre_guardado for nombre_guardado in contactos if nombre_guardado.casefold() == clave),
        None,
    )


def buscar_contacto(contactos, nombre):
    contacto = encontrar_contacto(contactos, nombre)
    if contacto is None:
        print("No se encontró ese contacto.")
    else:
        print(f"{contacto}: {contactos[contacto]}")
    return contacto


def agenda_contactos():
    contactos = {}

    while True:
        print("\nAgenda de contactos")
        print("1. Buscar contacto")
        print("2. Añadir contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        operacion = input("Elige una operación: ").strip()

        operaciones = {
            "1": "Buscar contacto",
            "2": "Añadir contacto",
            "3": "Actualizar contacto",
            "4": "Eliminar contacto",
            "5": "Salir",
        }
        if operacion not in operaciones:
            print("Operación no válida. Elige una opción del 1 al 5.")
            continue
        print(f"Operación seleccionada: {operaciones[operacion]}")

        if operacion == "1":
            nombre = input("Nombre que quieres buscar: ").strip()
            buscar_contacto(contactos, nombre)

        elif operacion == "2":
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
            elif encontrar_contacto(contactos, nombre) is not None:
                print("Ya existe un contacto con ese nombre.")
            else:
                contactos[nombre] = pedir_telefono()
                print("Contacto añadido.")

        elif operacion == "3":
            nombre = input("Nombre del contacto que quieres actualizar: ").strip()
            contacto = encontrar_contacto(contactos, nombre)
            if contacto is None:
                print("No se encontró ese contacto.")
            else:
                nuevo_nombre = input("Nuevo nombre: ").strip()
                if not nuevo_nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                contacto_existente = encontrar_contacto(contactos, nuevo_nombre)
                if contacto_existente is not None and contacto_existente != contacto:
                    print("Ya existe un contacto con ese nombre.")
                    continue
                telefono = pedir_telefono()
                del contactos[contacto]
                contactos[nuevo_nombre] = telefono
                print("Contacto actualizado.")

        elif operacion == "4":
            nombre = input("Nombre del contacto que quieres eliminar: ").strip()
            contacto = encontrar_contacto(contactos, nombre)
            if contacto is None:
                print("No se encontró ese contacto.")
            else:
                del contactos[contacto]
                print("Contacto eliminado.")

        elif operacion == "5":
            print("Agenda finalizada.")
            break


if __name__ == "__main__":
    agenda_contactos()

