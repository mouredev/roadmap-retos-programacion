# Creación de una lista
mi_lista = [1, 2, 3, 4, 5]

# Inserción
mi_lista.append(6)

# Borrado
mi_lista.remove(3)

# Actualización
mi_lista[0] = 10

# Ordenación
mi_lista.sort()

print(mi_lista)


# Creación de una tupla
mi_tupla = (1, 2, 3, 4, 5)

# Las tuplas son inmutables, por lo que no se pueden actualizar ni modificar después de la creación
# Puedes acceder a elementos de la tupla, pero no puedes cambiarlos

# Ordenación (creando una nueva tupla ordenada)
tupla_ordenada = tuple(sorted(mi_tupla))

print(tupla_ordenada)


# Creación de un conjunto
mi_conjunto = {1, 2, 3, 4, 5}

# Inserción
mi_conjunto.add(6)

# Borrado
mi_conjunto.remove(3)

# No hay actualización en los conjuntos, ya que los elementos son únicos

# No hay ordenación en los conjuntos, ya que son desordenados por naturaleza

print(mi_conjunto)


# Creación de un diccionario
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}

# Inserción
mi_diccionario["clave4"] = "valor4"

# Borrado
del mi_diccionario["clave2"]

# Actualización
mi_diccionario["clave1"] = "nuevo_valor"

# No hay ordenación en los diccionarios, ya que son estructuras basadas en claves

print(mi_diccionario)


# Ejercicio extra
usuarios = {}
identificadores = []


def new_user():
    nombre = input("Ingrese el nombre: ")

    numero_telefono = input("Ingrese el numero de telefono: ")
    while not numero_telefono.isdigit() or len(numero_telefono) != 10:
        print("Error: El numero debe contener 10 digitos")
        numero_telefono = input("Igrese el numero de telefono: ")

    identificador = len(identificadores) + 1
    identificadores.append(identificador)

    usuarios[identificador] = {"nombre": nombre, "numero_telefono": numero_telefono}

    print(
        f"Usuario guardado correctamente. Identificador: {identificador}, nombre: {nombre}"
    )


def show_user(id_usuario):
    if id_usuario in usuarios:
        usuario = usuarios[id_usuario]
        print(f"Informacion del usuario con ID {id_usuario}")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Numero de telefono: {usuario['numero_telefono']}")
    else:
        print(f"No se encontro el usuario con ID {id}")


def edit_user(id_usuario):
    if id_usuario in usuarios:
        usuario_actual = usuarios[id_usuario]

        nombre = (
            input(f"Ingrese el nuevo nombre ({usuario_actual['nombre']}): ")
            or usuario_actual["nombre"]
        )

        numero_telefono = (
            input(
                f"Ingrese el nuevo número de teléfono ({usuario_actual['numero_telefono']}): "
            )
            or usuario_actual["numero_telefono"]
        )

        usuarios[id_usuario] = {
            "nombre": nombre,
            "numero_telefono": numero_telefono,
        }

        print(f"Información del usuario con ID {id_usuario} actualizada con éxito.")
    else:
        print(f"No se encontró un usuario con el ID {id_usuario}.")


def delete_user(id_usuario):
    if id_usuario in usuarios:
        del usuarios[id_usuario]
        identificadores.remove(id_usuario)
        print(f"Usuario con ID: {id_usuario} eliminado con exito")
    else:
        print(f"No se encontro el usuario con ID: {id_usuario}")


def list_user():
    print("\nLista de usuarios registrados:")
    for identificador in identificadores:
        print(identificador)


# Menu Principal
while True:
    print("\nMenú:")
    print("A.- Registrar nuevos usuarios")
    print("B.- Listar usuarios")
    print("C.- Ver información de un usuario por ID")
    print("D.- Editar información de un usuario por ID")
    print("E.- Eliminar usuario por ID")
    print("F.- Finalizar el programa")

    opcion = input("Seleccione una opción (A/B/C/D/E/F): ").upper()

    if opcion == "A":
        new_user()
    elif opcion == "B":
        list_user()
    elif opcion == "C":
        id_usuario = int(input("Ingrese el ID del usuario que desea ver: "))
        show_user(id_usuario)
    elif opcion == "D":
        id_usuario = int(input("Ingrese el ID del usuario que desea editar: "))
        edit_user(id_usuario)
    elif opcion == "E":
        id_usuario = int(input("Ingrese el ID del usuario que desea eliminar: "))
        delete_user(id_usuario)
    elif opcion == "F":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción correcta.")
