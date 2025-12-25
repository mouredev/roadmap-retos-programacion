# -------------------- Estructuras de datos -----------------
# Coleccion ordenada, mutables, permiten duplicados
lista = [1, 2, 3]
# Coleccion ordenada, inmutables, permiten duplicados
tupla = (1, 2, 3, 8, 5, 4)
# Coleccion desordenada, sin duplicados
conjuntos = {1, 2, 3, 3}
# Pares clave:valor, mutables, no permiten claves repetidas
diccionario = {
    1: {"nombre": "Ivan", "edad": 25},
    2: {"nombre": "Camilo", "edad": 20},
    3: {"nombre": "vanessa", "edad": 30},
}


# ------------------- Operaciones ---------------------------
# ---------------------- Lista ------------------------------
# Insercion
lista.append("Hola")  # Inserta al final de la lista
lista.insert(0, "Posicion 0")  # Inserta en la posicion especifica
lista.extend([2, 4])  # Agrega varios elemetnos de una vez
print(lista)

# Borrado
lista.remove("Hola")  # Elimina la primera aparicion del valor pasado
lista.pop()  # Elimina y retorna el elemento en el indice
# lista.clear()  # Vacia la lista
print(lista)

# Actualizacion
lista[1] = "Actualizacion"
print(lista)

# Ordenacion
lista_2 = ["a", "b", "c", "x", "y", "z", "e"]
lista_2.sort()  # Ordena la lista
print(lista_2)
lista_2.sort(reverse=True)  # Orden descendente
print(lista_2)
nueva_lista = sorted(lista_2)  # Nueva lista ordenada

print(nueva_lista)

# ---------------------------------- Tupla ----------------------------
# No permite insercion, borrado, actualizacion
# Ordenacion
nueva_tupla = sorted(tupla)
print(nueva_tupla)

# -------------------- Conjuntos -------------------------------------
# NO hay actualizacion
# Insercion
conjuntos.add("Hola")  # Inserta al final del conjunto
print(conjuntos)
conjuntos.update("A", "B", "C")  # Agrega varios elementos
print(conjuntos)

# Borrado
conjuntos.remove("A")  # Elimina un elemento si existe - error si no existe
print(conjuntos)
conjuntos.discard("B")  # Elimina un elemento si existe - no error
print(conjuntos)
conjuntos.pop()  # Elimina y retorna un elemento arbitrario
print(conjuntos)
# conjuntos.clear()  # Vacia el conjunto

# Ordenacion
conjunto_1 = {1, 2, 5, 3, 4}
nuevo_conjunto = sorted(conjunto_1)
print(nuevo_conjunto)

# ----------------------- Diccionarios ------------------------------
# Inserccion
diccionario["nombre"] = "Raul"  # Agrega o reemplaza
print(diccionario)
diccionario.update({"nombre": "hernesto"})  # Agregao o actualiza
print(diccionario)

# Borrado
pop = diccionario.pop("nombre")  # Elimina y devuelve el valor
print(pop)
popitem = diccionario.popitem()  # Elimina y devuelve el ultimo valor
print(popitem)
del diccionario[1]  # Elimina par por clave
print(diccionario)
# diccionario.clear()  # Vacia el diccionario

# Actualizacion -> Igual que inserccion

# Ordenacion no tiene directamente, se usa sorted
nuevo_diccionario = sorted(diccionario)
print(nuevo_diccionario)


# DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#  *   los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
#  *   (o el número de dígitos que quieras)
#  * - También se debe proponer una operación de finalización del programa.
#

print("------------------ Agenda de Contactos ----------------")
agendaContactos = {}
contador_id = 1


def busqueda():
    valor = input("Que contacto busca: ")
    for id, datos in agendaContactos.items():
        if datos["nombre"].lower() == (valor.lower()):
            return print(id, datos)
    return print("No existe")


def insercion():
    global contador_id
    global agendaContactos
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese Telefono: ")

    if telefono.isdigit() and len(telefono) <= 11:
        agendaContactos[contador_id] = {"nombre": nombre, "telefono": int(telefono)}
        contador_id += 1
        print("Contacto agregado")
    else:
        print("Numero telefono no puede superar los 11 digitos")


def actualizacion():
    global agendaContactos
    nombre = input("Ingrese contacto que busca: ")
    nuevo_Nombre = input("Ingrese nuevo nombre: ")
    telefono = input("Ingrese Telefono: ")
    for id_contacto, datos in agendaContactos.items():
        if datos["nombre"].lower() == nombre.lower():
            if telefono.isdigit() and len(telefono) <= 11:
                datos["nombre"] = nuevo_Nombre
                datos["telefono"] = int(telefono)
                print("Contacto actualizado")
                return
    print("No existe el contacto")


def eliminar():
    nombre = input("Que contacto desea eliminar: ")
    encontrado = False
    id_eliminar = None
    for id, datos in agendaContactos.items():
        if datos["nombre"].lower() == nombre.lower():
            id_eliminar = id
            encontrado = True
            break

    if encontrado:
        agendaContactos.pop(id_eliminar)
        print("Contacto eliminado")
    else:
        print("No existe el contacto")


# insercion("Ivan", 1111111111)
# insercion("Raul", 9999999999)
# print(agendaContactos)

# actualizacion("Ivan", "Ivan G", 123456789)
# print(agendaContactos)

# print(busqueda())
# print(eliminar())
# print(agendaContactos)

while True:
    opcion = input(
        "---- Agenda de contactos ---- \nIngrese su opcion: \n1. Buscar contacto. \n2. Agregar contacto. \n3. Actualizar contacto. \n4. Eliminar contacto. \n5. Salir\nIngrese su opcion: "
    )

    match opcion:
        case "1":
            busqueda()
        case "2":
            insercion()
        case "3":
            actualizacion()
        case "4":
            eliminar()
        case "5":
            print("Fin")
            break
