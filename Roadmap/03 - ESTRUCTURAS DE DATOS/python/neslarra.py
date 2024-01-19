"""
 EJERCICIO:
 - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 - Utiliza operaciones de inserción, borrado, actualización y ordenación.

 DIFICULTAD EXTRA (opcional):
 Crea una agenda de contactos por terminal.
 - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
   los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
   (o el número de dígitos que quieras)
 - También se debe proponer una operación de finalización del programa.
"""
import json                   # para poder dar persistencia a los contactos de la actividad extra.

# Tupla: es inmutable => no la puedo modificar (como se crea queda). Está indexada: a cada elemento le corresponde una posición.
print(f"-- Tuplas {'-' * 50}")
materias = ('matemáticas', 'ciencias', 'lenguas', 'deportes', 'talleres', 'sociales')
print(f"El curso cuenta con {materias.__len__()} materias -> {materias}")
materia = materias[3]
indice = materias.index("deportes")
print(f"Buscar la materia que está en el índice 3: materia = materias[3] => {materia}")
print(f"Buscar la posición de la materia 'deportes': indice = materias.index('deportes') => {indice}", end="\n\n")

# Set: es nmutable => admite remociones y agragados PERO no modificar un elemento. Es única => sus elementos NO se repiten. NO está indexado.
# Frozenset es un set INMUTABLE.
print(f"-- Set {'-' * 50}")
citricos = {'naranja', 'limón', 'manzana', 'mandarina', 'bergamota', 'naranja', 'cidra', 'limón', 'pomelo', 'lima'}
print(f"Cítricos: {citricos}")
citricos.discard('manzana')      # la diferencia entre discard y remove es que el primero NO da error si el elemento a eliminar no existe.
citricos.add('kiwi')
print(f"Elimino la 'manzana': citricos.discard('manzana')")
print(f"y agrego el 'kiwi': citricos.add('kiwi')")
print(f"Cítricos: {citricos}")
cosas_agrias = {'limón', 'ruibarbo', 'pomelo', 'berenjena', 'lima', 'rúcula', 'vinagre'}
citricos_agrios = cosas_agrias.intersection(citricos)
print(f"Cítricos Agrios: cosas_agrias.intersection(citricos) => {citricos_agrios}")
print(f"Cítricos Dulces: citricos.difference(citricos_agrios) => {citricos.difference(citricos_agrios)}", end="\n\n")

# Lista: es mutable => la puedo modificar. También está indexada.
print(f"-- Listas {'-' * 50}")
notas: list = [1, 4, 8, 5, 1, 4, 9, 9, 4, 6, 6, 5, 3, 6, 4, 1, 11, 4, 8.75, 9]
indice = notas.index(11)
notas.remove(11)
notas.insert(indice, 10)
print(f"Buscar la posición de la nota '11': indice = materias.index('11') => {indice}")
print(f"Eliminar la nota '11': notas.remove(11)")
print(f"e insertar una nueva nota '10': notas.insert(indice, 10)")
indice = notas.index(8.75)
notas[indice] = 9
print(f"Buscar la posición de la nota '8.75': indice = notas.index(8.75)")
print(f"y reemplazar con un '9': notas[indice] = 9")
notas.append(7)
print(f"Agregar nuevas notas: notas.append(7)")
print(f"También se puede ordenar la lista y operar con sus elementos.")
print(f"Notas: {notas}")
print(f"Alumnos: {notas.__len__()}")
print(f"Promedio: {(sum(notas) / notas.__len__()).__round__(2)}")
notas.sort()
print(f"Notas ordenadas: {notas}")
print(f"Mediana:{notas[(notas.__len__() // 2)]}")
moda = -1
for n in set(notas):                                    # Transformo la lista en un set para contar las ocurrencias de cada elemento.
    moda = n if notas.count(n) > moda else moda
print(f"Moda: {moda}")
print(f"Nota más baja: {min(notas)}")
print(f"Nota más alta: {max(notas)}")
desaprobados = [1 for x in notas if x < 4].__len__()
print(f"Desaprobados: {desaprobados}")
print(f"Aprobados: {notas.__len__() - desaprobados}", end="\n\n")

# Diccionario: es mutable => la puedo modificar. NO está indexada. Se accede por clave.
print(f"-- Diccionarios {'-' * 50}")
saludos = {"español": "hola", "inglés": "hello", "latín": "salve"}
print(f"{saludos}")
print(f"Busco si una clave está dentro del diccionario y muestro el valor: if 'inglés' in saludos.keys()")
if "inglés" in saludos.keys():
    print(f"Inglés: {saludos['inglés']}")
print(f"Muestro las claves: saludos.keys()")
print(f"{saludos.keys()}")
print(f"Muestro los valores: saludos.values()")
print(f"{saludos.values()}")
print(f"Agrego una nueva entrada: saludos['italiano'] = 'ciao'")
saludos["italiano"] = "ciao"
print(f"Elimino una entrada: del saludos['latín']")
del saludos["latín"]
mundo_traducido = {"español": "mundo", "inglés": "world", "latín": "orbe", "italiano": "mondo", "portugués": "mundo", "francés": "monde"}
print(f"Modifico entradas asignando un nuevo valor a la clave: saludos[key] = 'nuevo valor'")
for key, value in saludos.items():
    saludos[key] = value + " " + mundo_traducido[key]
print(f"{saludos}", end="\n\n")

# Complejidad extra:
print(f"-- Complejidad extra {'-' * 50}")
contactos = {}
contactos_modificados = False


def cargar_contactos() -> bool:
    global contactos
    try:
        with open("contactos.json", "r") as cntos:
            contactos = json.load(cntos)
        return True
    except Exception as e:
        print(f"Error cargando contactos: {e}")
        return False


def guardar_contactos() -> bool:
    global contactos
    try:
        with open("contactos.json", "w") as cntos:
            json.dump(contactos, cntos, indent=4, sort_keys=True)
        print("Contactos guardados !!!")
        return True
    except Exception as e:
        print(f"Error guardando contactos: {e}")
        return False


def validar_contacto(nombre: str) -> bool:
    if nombre in contactos.keys():
        print(f"El contacto YA existe !!!")
        return False
    return True


def validar_telefono(telefono: str) -> bool:
    if not telefono.isnumeric():
        print(f"Solo ingresar dígitos !!!")
        return False
    if telefono.__len__() not in range(5, 12):
        print(f"Faltan o sobran dígitos !!!")
        return False
    return True


def alta_contacto() -> bool:
    global contactos
    global contactos_modificados

    def nuevo_nombre() -> str:
        while True:
            nombre = input("Nombre del nuevo contacto ('--' para cancelar): ").title()
            if nombre != "--" and not validar_contacto(nombre):
                continue
            return nombre

    def nuevo_numero() -> str:
        while True:
            telefono = input("Teléfono ('--' para cancelar): ")
            if telefono != "--" and not validar_telefono(telefono):
                continue
            return telefono

    nombre = nuevo_nombre()
    telefono = nuevo_numero() if nombre != "--" else "--"

    if "--" not in (nombre, telefono):
        contactos[nombre] = telefono
        contactos_modificados = True

    return True


def baja_contacto() -> bool:
    global contactos
    global contactos_modificados

    nombre = buscar_contacto()
    if nombre != "--":
        del contactos[nombre]
        contactos_modificados = True

    return True


def buscar_contacto() -> str:
    nombre = ""
    while True:
        nombre = input("Ingresar patrón de búsqueda (-- para cancelar): ").lower()
        if nombre == "--":
            break
        nombres = [n for n in contactos.keys() if n.lower().__contains__(nombre)]

        if nombres.__len__() == 0:
            print("No hubo coincidencia.")
            continue

        nombres.append("Volver")

        for p, n in enumerate(nombres):
            print(f"{p} - Nombre: {n}  /  Teléfono: {contactos[n] if n != 'Volver' else '--'}")

        opcion = "-1"
        while int(opcion) not in range(0, nombres.__len__()):
            opcion = input(f"Seleccione un nombre de contacto (0 - {nombres.__len__() - 1}): ")
        nombre = nombres[int(opcion)]

        break

    return nombre if nombre != "Volver" else "--"


def modifica_contacto() -> bool:
    global contactos
    global contactos_modificados

    def nuevo_nombre() -> str:
        while True:
            nombre = input("Nombre del nuevo contacto (Enter si no cambia): ").title()
            if nombre and not validar_contacto(nombre):
                continue
            return nombre

    def nuevo_numero() -> str:
        while True:
            telefono = input("Teléfono (Enter si no cambia): ")
            if telefono and not validar_telefono(telefono):
                continue
            return telefono

    nombre = buscar_contacto()
    if nombre != "--":
        telefono = contactos[nombre]

        while True:
            nombre_nuevo = nuevo_nombre()
            telefono_nuevo = nuevo_numero()

            if nombre_nuevo or telefono_nuevo:
                if nombre_nuevo:
                    del contactos[nombre]
                    nombre = nombre_nuevo
                contactos[nombre] = telefono_nuevo if telefono_nuevo else telefono
                contactos_modificados = True
            break

    return True


def ver_contacto() -> bool:
    for nombre, telefono in contactos.items():
        print(f"Nombre: {nombre}  /  Teléfono: {telefono}")

    return True


def salir() -> bool:
    return False


def menu() -> str:
    opciones = {"0": "salir", "1": "alta", "2": "baja", "3": "modifica", "4": "ver", "5": "buscar"}
    opcion = "-1"
    print("""
    Elija la opción a ejecutar:
       1 - Alta de contacto
       2 - Baja de contacto
       3 - Modificación de contacto
       4 - Ver contactos
       5 - Buscar contacto
       0 - Salir
    """)
    while int(opcion) not in range(0, opciones.__len__()):
        opcion = input(f"Ingresar opcion (0-{opciones.__len__() - 1}): ")

    return opciones[opcion]


def main():
    if not cargar_contactos():
        print(F"No hay contactos disponibles => cargar el primer contacto.")
        alta_contacto()

    while True:
        operacion = menu()
        ejecutar = operacion + ("()" if operacion == "salir" else "_contacto()")
        if not eval(ejecutar):
            break

    guardar_contactos() if contactos_modificados else None


if __name__ == "__main__":
    main()
