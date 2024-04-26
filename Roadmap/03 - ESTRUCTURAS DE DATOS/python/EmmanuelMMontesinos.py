"""
/*
 * EJERCICIO:
 * x Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * x Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 */
"""
# Tipos de estructuras:

# Tupla -> Inmutable
tupla: tuple = ("dato_1", "dato2", "dato_3")

# Lista -> Mutable
lista: list = ["dato_1", "dato_2", "dato_3"]

"""Agragar o Actualizar según índice"""
lista.insert(0, "dato_4")

"""Agregar al final"""
lista.append("dato_5")

"""Borrar el último o según índice"""
lista.pop()

"""Borra según el contenido"""
lista.remove("dato_3")

"""Orden normal"""
lista.sort()

"""Invertir Orden"""
lista.reverse()


# Set -> Mutable No Ordenado
set: set = {"dato_1", "dato_2", "dato_3"}

"""Agregar"""
set.add("dato_4")

"""Borrar"""
set.remove("dato_2")

"""Borrar el último"""
set.pop()

# Diccionario -> Mutable
diccionario: dict[str:str] = {"llave": "valor"}

"""Agregar"""
diccionario["llave2"] = "valor2"

"""Actualizar"""
diccionario["llave"] = "valor3"

"""Borrar"""
diccionario.pop("llave")

"""Borrar y mueve el ultimo elemento"""
element = diccionario.popitem()

"""
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 """

# Diccionario usado como agenda
agenda = {}

# Clase para crear y gestionar la agenda


class Contacto():
    def add(nombre: str, tlf: str) -> None:
        check = int(tlf)
        if len(tlf) <= 11 and isinstance(check, int) == True:
            agenda[nombre.lower()] = tlf
            print(f"{nombre} ha sido guardado")
        else:
            print(f"El Número {tlf} no es válido")
    # funcion plantilla para imprimir contactos

    def imprimir(nombre):
        print(f"Nombre: {nombre.capitalize()}\nTlf: {agenda[nombre]}")

    # función para buscar contacto, no es necesario el nombre exacto
    def buscar(nombre):
        if nombre.lower() in agenda.keys():
            Contacto.imprimir(nombre)
        else:
            posibles = []
            for contactos in agenda.keys():
                for letras in nombre:
                    if letras in contactos and contactos not in posibles:
                        posibles.append(contactos)
            if len(posibles) >= 1:
                print(
                    f"No se ha encontrado al contacto -> {nombre} <-, posibles coincidencias:")
                for posible in posibles:
                    print(f"- {posible}")
            else:
                print(f"No hay ninguna coincidencia con -> {nombre} <-")
    # Actualizar contacto

    def actualizar(nombre):
        if nombre in agenda.keys():
            print(f"información actual:")
            Contacto.imprimir(nombre)
            opcion = input("¿Qué quiere cambiar?\n1-Nombre\n2-Tlf\n--> ")
            if opcion == "1":
                nuevo_nombre = input("Nuevo nombre: ")
                tlf = agenda[nombre]
                agenda.pop(nombre)
                agenda[nuevo_nombre] = tlf
                print("Contacto cambiado:")
                Contacto.imprimir(nuevo_nombre)
            elif opcion == "2":
                nuevo_tlf = input("Nuevo Tlf: ")
                check = int(nuevo_tlf)
                if len(nuevo_tlf) <= 11 and isinstance(check, int) == True:
                    agenda[nombre] = nuevo_tlf
                    print("Contacto cambiado:")
                    Contacto.imprimir(nombre)
                else:
                    print(f"{nuevo_tlf} tiene más de 11 digitos o no es un número")
            else:
                print("Opción incorrecta")

    def borrar(nombre):
        if nombre in agenda.keys():
            agenda.pop(nombre)
            print(f"{nombre} ha sido borrado")
        else:
            print(f"{nombre} no esta en la agenda")


def main():
    salir = False
    while not salir:
        print("Agenda")
        print("OPCIONES")
        print("1- Agregar Contacto")
        print("2- Buscar Contacto")
        print("3- Actualizar Contacto")
        print("4- Borrar Contacto")
        print("5- Mostrar Toda la agenda")
        print("6- Salir")
        opcion = input("--> ")
        if opcion == "1":
            nombre = input("Nombre: ")
            tlf = input("Tlf: ")
            Contacto.add(nombre, tlf)
        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            Contacto.buscar(nombre)
        elif opcion == "3":
            nombre = input("¿Qué contacto quiere cambiar?(nombre): ")
            Contacto.actualizar(nombre)
        elif opcion == "4":
            nombre = input("Nombre del contacto a borrar: ")
            Contacto.borrar(nombre)
        elif opcion == "5":
            ciclo = 1
            for contac in agenda:
                print(f"{ciclo}nº - {contac}")
        elif opcion == "6":
            salir = True
            print("Adíos!")


main()
