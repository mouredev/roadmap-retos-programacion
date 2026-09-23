# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.

"""
Listas
"""
frutas = ["Manzana", "Naranja", "Plátano", "Pera", "Mandarina"]

# Acceso
print(f"Todos los elementos: {frutas}")
print(f"Primer elemento: {frutas[0]}")
print(f"Último elemento: {frutas[-1]}")

# Inserción al final
frutas.append("Sandía")

# Inserción en una posición específica
frutas.insert(2, "Fresa")
print(f"Insertando una fruta: {frutas}")

# Actualización
frutas[0] = "Fresa"
print(f"Actualizando una fruta: {frutas}")

# Ordenación por defecto
frutas.sort()
print(f"Frutas ordenadas por defecto: {frutas}")

# Ordenación personalizada (longitud)
frutas.sort(key = lambda x: len(x))
print(f"Frutas ordenadas por longitud: {frutas}")

# Ordenación por defecto inversa
frutas.sort(key = lambda x: x, reverse = True)
print(f"Frutas ordenadas por defecto inversa: {frutas}")

# Borrado al final
frutas.pop()
print(f"Frutas después de borrar la última: {frutas}")

# Borrado por index
frutas.pop(0)
del frutas[0]
print(f"Frutas después de borrar las 2 primeras: {frutas}")

# Borrado por valor
frutas.remove("Mandarina")
print(f"Frutas después de borrar 'Mandarina': {frutas}")

# Borrado completo
frutas.clear()
print(f"Frutas borradas: {frutas}")
print()

"""
Tuplas
"""
vehiculos = ("Auto", "Barco", "Avión", "Bicileta", "Motocicleta")

# Acceso
print(f"Todos los elementos: {vehiculos}")
print(f"Primer elemento: {vehiculos[0]}")
print(f"Último elemento: {vehiculos[-1]}")

# Actualización (usando conversión a lista)
vehiculos = list(vehiculos)
vehiculos[0] = "Tren"
vehiculos = tuple(vehiculos)
print(f"Actualizando un vehículo (con conversión): {vehiculos}")

# Actualización completa
vehiculos = ("Tren", "Automóvil", "Patineta", "Scooter")
print(f"Nueva tupla de vehículos: {vehiculos}")

# Ordenación por defecto
vehiculos = tuple(sorted(vehiculos))
print(f"Vehículos ordenados por defecto: {vehiculos}")

# Ordenación personalizada (longitud)
vehiculos = tuple(sorted(vehiculos, key = lambda x: len(x)))
print(f"Vehículos ordenados por longitud: {vehiculos}")

# Ordenación por defecto inversa
vehiculos = tuple(sorted(vehiculos, key = lambda x: x, reverse = True))
print(f"Vehículos ordenados por defecto inverso: {vehiculos}")

# Borrado (con conversión a lista)
vehiculos = list(vehiculos)
del vehiculos[0]
vehiculos.pop(-1)
vehiculos = tuple(vehiculos)
print(f"Vehículos después de borrar el primer y último elemento (con conversión): {vehiculos}")

# Borrado completo:
vehiculos = ()
print(f"Vehículos borrados: {vehiculos}")
print()

"""
Sets
"""
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Acceso
print(f"Todos los elementos: {numeros}")

# Inserción
numeros.add(11)
numeros.add(10)
print(f"Números después de insertar 11 y otro 10: {numeros}")

# Actualización (conversión a lista)
numeros = list(numeros)
numeros[numeros.index(11)] = 0
numeros = set(numeros)
print(f"Actualizando un número (con conversión): {numeros}")

# Eliminación
numeros.discard(0)
numeros.remove(1)
numeros.pop()
print(f"Eliminando tres números: {numeros}")
print()

"""
Diccionarios
"""
usuario = {
    "nombre": "Gabriel",
    "username": "HaloGabriel",
    "edad": 25,
    "pais": "Perú"
}

# Acceso
print(f"Todos los datos: {usuario}")
print(f"Nombre: {usuario["nombre"]}")
print(f"Username: {usuario["username"]}")
print(f"Edad: {usuario["edad"]}")
print(f"País: {usuario["pais"]}")

# Inserción
usuario["tecnologias"] = ["Python", "Java", "C++", "SQL"]
print(f"Insertando tecnologías: {usuario}")

# Actualización
usuario["nombre"] = "Gabriel Halo"
usuario["username"] = "admin"
print(f"Actualizando nombre y username: {usuario}")

# Ordenación por defecto
usuario = dict(sorted(usuario.items()))
print(f"Ordenación por defecto: {usuario}")

# Ordenación personalizada (valores)
def ordenar_diccionario(item):
    v = item[1]
    if isinstance(v, (str)):
        return (1, v.casefold())
    elif isinstance(v, (int)):
        return (2, v)
    else:
        return (3, str(v))

usuario = dict(sorted(usuario.items(), key = ordenar_diccionario))
print(f"Ordenación personalizada (valores): {usuario}")

# Eliminación
del usuario["username"]
usuario.pop("tecnologias")
print(f"Eliminando 'username' y 'tecnologias': {usuario}")
print()

# DIFICULTAD EXTRA (opcional)
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#   los datos necesarios para llevarla a cabo
# - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
#   (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.

print("###########################")
print("### AGENDA DE CONTACTOS ###")
print("###########################")
continuar = True

agenda = set()

def buscar_contactos(param: str, agenda: set):
    encontrados = []
    if param != "":
        param = param.lower()
        for item in agenda:
            if param in item[0].lower() or param in item[1].lower():
                encontrados.append(item)
    if len(encontrados) == 0:
        print("No se encontraron coincidencias.")
    elif len(encontrados) == 1:
        print("¡1 coincidencia encontrada!")
    else:
        print(f"¡{len(encontrados)} coincidencias encontradas!")

    encontrados = sorted(encontrados, key = lambda x: x[1].casefold())
    for item in encontrados:
        print(f"{item[1]} : {item[0]}")

def validar_num_nom_contacto(num_con: str, nom_con: str) -> bool:
    valido = True
    if len(num_con) == 0:
        print("Número de contacto está vacío.")
        valido = False
    elif len(num_con) != 9 or not num_con.isdigit():
        print(f"Número de contacto '{num_con}' no válido.")
        valido = False
    if not nom_con:
        print("Nombre de contacto está vacío.")
        valido = False
    return valido

def validar_nuevo_numero(num_con: str, agenda: set) -> bool:
    agenda_lista = list(agenda)
    for item in agenda_lista:
        if item[0] == num_con:
            return False
    return True

def validar_num_contacto_existente(num_con: str, agenda: set) -> bool:
    if num_con != "":
        for item in agenda:
            if item[0] == num_con:
                print(f"Contacto encontrado: {item[0]} - {item[1]}")
                return True
    return False

def actualizar_contacto(agenda: set, num_con: str) -> set:
    agenda_copia = agenda.copy()
    nom_con = input("Ingresar nuevo nombre de contacto: ").strip()
    if nom_con != "":
        for item in agenda_copia:
            if item[0] == num_con:
                agenda_copia.remove((item[0], item[1]))
                agenda_copia.add((num_con, nom_con))
                print("Nombre de contacto actualizado")
                return agenda_copia
    print("Nuevo nombre de contacto está vacío")
    return agenda_copia

def eliminar_contacto(num_con: str, agenda: set) -> set:
    agenda_copia = agenda.copy()
    if num_con != "":
        for item in agenda_copia:
            if item[0] == num_con:
                agenda_copia.remove((item[0], item[1]))
                print(f"Contacto eliminado: {item[0]} - {item[1]}")
                return agenda_copia
    print("No se encontró el contacto ingresado.")
    return agenda_copia

def listar_agenda(agenda: set):
    agenda_lista = list(agenda)
    agenda_lista = sorted(agenda, key = lambda x: x[1].casefold())
    for item in agenda_lista:
        print(f"{item[1]} - {item[0]}")

while continuar:
    print("Operaciones disponibles:")
    print("1 - Búsqueda")
    print("2 - Inserción")
    print("3 - Actualización")
    print("4 - Eliminación")
    print("5 - Listado")
    print("0 - Salir")
    operacion = input("Ingresar número de operación: ")

    if operacion == "1":
        if len(agenda) > 0:
            param_busq = input("Ingresar parámetro de búsqueda: ").strip()
            buscar_contactos(param_busq, agenda)
        else:
            print("No hay contactos en la agenda.")
    elif operacion == "2":
        num_con = input("Ingresar número de contacto (9 dígitos): ").strip()
        nom_con = input("Ingresar nombre de contacto: ").strip()
        valido = validar_num_nom_contacto(num_con = num_con, nom_con = nom_con)
        if valido:
            if validar_nuevo_numero(num_con, agenda):
                agenda.add((num_con, nom_con))
                print("¡Nuevo contacto registrado!")
            else:
                print(f"Número de contacto '{num_con}' ya está registrado.")
    elif operacion == "3":
        if len(agenda) > 0:
            num_con = input("Ingresar número de contacto a actualizar: ").strip()
            if validar_num_contacto_existente(num_con, agenda):
                agenda = actualizar_contacto(agenda, num_con)
            else:
                print("No se encontró el contacto ingresado.")
        else:
            print("No hay contactos en la agenda.")
    elif operacion == "4":
        if len(agenda) > 0:
            num_con = input("Ingresar número de contacto a eliminar: ").strip()
            agenda = eliminar_contacto(num_con, agenda)
        else:
            print("No hay contactos en la agenda.")
    elif operacion == "5":
        if len(agenda) > 0:
            listar_agenda(agenda)
        else:
            print("No hay contactos en la agenda.")
    elif operacion == "0":
        continuar = False
        continue
    else:
        print("Número de operación no válido.")

    rpta_final = input("¿Continuar con el programa? ")
    if rpta_final.lower() not in ["yes", "y", "si", "sí", "s"]:
        continuar = False

print("PROGRAMA FINALIZADO")
