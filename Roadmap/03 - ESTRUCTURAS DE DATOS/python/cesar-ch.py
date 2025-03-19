# ----- Listas
# Creación
lista = [1, 2, 3, 4, 5]
lista_vacia = []
lista_mezclada = [1, "dos", True, 3.14]

# Inserción
lista.append(6)
lista.insert(2, 4)

# Borrado
lista.remove(2)
lista.pop()

# Actualización
lista[1] = 2

# Ordenación
lista.sort()
lista.sort(reverse=True)

# ----- Tuplas
# Creación
tupla = (1, 2, 3, 4, 5)
tupla_vacia = ()
tupla_mezclada = (1, "dos", True, 3.14)

# Inserción y borrado
# No es posible insertar o borrar elementos en una tupla

# Actualización
# No es posible actualizar elementos en una tupla

# Ordenación
# No es posible ordenar una tupla

# ----- Diccionarios
# Creación
diccionario = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5}
diccionario_vacia = {}
diccionario_mezclado = {"uno": "dos", "tres": True, "cuatro": 3.14}

# Inserción
diccionario["seis"] = 6

# Borrado
del diccionario["seis"]

# Actualización
diccionario["uno"] = 0

# Ordenación
# No es posible ordenar un diccionario

# ----- Sets
# Creación
conjunto = {1, 2, 3, 4, 5}
conjunto_vacia = set()
conjunto_mezclado = {1, "dos", True, 3.14}

# Inserción
conjunto.add(6)

# Borrado
conjunto.remove(2)
conjunto.pop()

# Actualización
# No es posible actualizar elementos en un conjunto

# Ordenación
# No es posible ordenar elemetos en un conjunto


# DIFICULTAD EXTRA
def crear_agenda():
    agenda = []
    run = True

    while run:
        operacion = input(
            """Ingrese la operación a realizar:
            1. Buscar contacto
            2. Insertar contacto
            3. Actualizar contacto
            4. Eliminar contacto
            5. Salir
        """
        )

        if operacion == "1":
            if len(agenda) == 0:
                print("Agenda vacía")
                continue

            nombre = input("Ingrese el nombre del contacto a buscar: ")

            contacto_encontrado = False
            for contacto in agenda:
                if contacto["nombre"] == nombre:
                    print("Contacto encontrado:", contacto)
                    contacto_encontrado = True
                    break

            if not contacto_encontrado:
                print("Contacto no encontrado")

        elif operacion == "2":
            nombre = input("Ingrese el nombre del contacto a insertar: ")
            telefono = input("Ingrese el teléfono del contacto a insertar: ")

            if not telefono.isdigit() or not (6 <= len(telefono) <= 11):
                print("El número de teléfono no es válido.")
                break

            nuevo_contacto = {"nombre": nombre, "telefono": telefono}
            agenda.append(nuevo_contacto)
            print("Contacto insertado:", nuevo_contacto)

        elif operacion == "3":
            nombre = input("Ingrese el nombre del contacto a actualizar: ")
            contacto_encontrado = False

            for contacto in agenda:
                if contacto["nombre"] == nombre:
                    contacto["telefono"] = input(
                        "Ingrese el nuevo teléfono del contacto: "
                    )
                    print("Contacto actualizado:", contacto)
                    contacto_encontrado = True
                    break

            if not contacto_encontrado:
                print("Contacto no encontrado")

        elif operacion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            contacto_encontrado = False

            for contacto in agenda:
                if contacto["nombre"] == nombre:
                    agenda.remove(contacto)
                    print("Contacto eliminado.")
                    contacto_encontrado = True
                    break

            if not contacto_encontrado:
                print("Contacto no encontrado")

        elif operacion == "5":
            run = False
            print("Agenda creada:", agenda)

        else:
            print("Operación no válida")


crear_agenda()
