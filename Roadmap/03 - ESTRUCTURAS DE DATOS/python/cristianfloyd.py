# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
#  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#  *
#  */


# Ejemplos de estructuras de datos en Python
# Lista
from typing import Optional

print("=" * 80)
print("Listas en Python:")
mi_lista = [3, 1, 4, 1, 5]
print("Lista original:", mi_lista)
mi_lista.append(9)  # Inserción
print("Después de insertar 9:", mi_lista)
mi_lista.remove(1)  # Borrado
print("Después de borrar 1:", mi_lista)
mi_lista[0] = 10  # Actualización
print("Después de actualizar el primer elemento a 10:", mi_lista)
mi_lista.sort()  # Ordenación
print("Después de ordenar:", mi_lista)

# Diccionario
print("=" * 80)
print("\nDiccionarios en Python:")
mi_dict = {"nombre": "Cristian", "edad": 30, "ciudad": "Quilmescity"}
print("\nDiccionario original:", mi_dict)

mi_dict.pop("ciudad")  # borrado
print(f"Eliminada la ciudad: {mi_dict}")

mi_dict["edad"] = 31  # actualización
print(f"Actualizada la edad: {mi_dict}")

mi_dict["profesion"] = ["Desarrollador"]  # inserción
print(f"Insertada la profesión: {mi_dict}")

mi_dict["profesion"].append("Profesor")  # actualización
print(f"Actualizada la profesión: {mi_dict}")

mi_dict_ordenado = dict(sorted(mi_dict.items()))  # ordenación
print(f"Diccionario ordenado por claves: {mi_dict_ordenado}")

# Conjunto
print("=" * 80)
print("\nConjuntos en Python:")
mi_set = {1, 5, 8, 0, 6, 7, 9}
print("\nConjunto original:", mi_set)

# No se puede actualizar un set directamente, pero se puede eliminar y añadir
mi_set.add(10)  # Inserción
print("Después de insertar 10:", mi_set)

mi_set.remove(0)  # Borrado
print("Después de borrar 0:", mi_set)

print("=" * 80)
print("Tuplas en Python:")

mi_tupla: tuple = (4, 2, 10, 6, 8)
print("Tupla original:", mi_tupla)

mi_tupla_ordenada = tuple(sorted(mi_tupla))  # Ordenación
print("Tupla ordenada:", mi_tupla_ordenada)

#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#  *   los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
#  *   (o el número de dígitos que quieras)
#  * - También se debe proponer una operación de finalización del programa.


def mi_agenda():
    agenda: dict = {}

    def opciones():
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

    def contacto_existe(nombre: str) -> bool:
        if nombre in agenda:
            return True
        else:
            return False
    
    def get_nombre(prompt: str) -> str:
        return str(input(prompt)).strip().upper()
    
    def get_telefono(prompt: str) -> str:
        telefono = str(input(prompt)).strip()
        if es_nro_telefono_valido(telefono):
            return telefono
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos."
            )
            return ""

    def es_nro_telefono_valido(telefono: str) -> bool:
        return telefono.isdigit() and 0 < len(telefono) <= 11

    def eliminar_contacto(nombre: str):
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido eliminado.")

    def insertar_contacto(nombre: str, telefono: str):
        agenda[nombre] = telefono

    def actualizar_contacto(nombre: str, telefono: Optional[str] = None) -> bool:
        if contacto_existe(nombre) and (
            telefono is None or es_nro_telefono_valido(telefono)
        ):
            if telefono is not None:
                agenda[nombre] = telefono
                return True
            elif telefono is None:
                nuevo_telefono = input("Introduce el nuevo teléfono del contacto: ")
                if es_nro_telefono_valido(nuevo_telefono):
                    agenda[nombre] = nuevo_telefono
                    return True
                else:
                    print(
                        "Debes introducir un número de teléfono un máximo de 11 dígitos."
                    )
                    return False
        else:
            print(f"El contacto {nombre} no existe.")
            return False

    while True:
        opciones()
        input_option = input("\nSelecciona una opción: ")

        match input_option:
            case "1":
                nombre = get_nombre("Introduce el nombre del contacto a buscar: ")
                if nombre in agenda:
                    print(f"\nEl número de teléfono de {nombre} es {agenda[nombre]}.")
                    while True:
                        input("Presione cualquier tecla para continuar...")
                        break
            case "2":
                nombre = get_nombre("Introduce el nombre del contacto a insertar: ")
                phone = get_telefono("Introduce el teléfono del contacto: ")
                insertar_contacto(nombre, phone)
            case "3":
                nombre = get_nombre("Introduce el nombre del contacto a actualizar: ")
                actualizar_contacto(nombre) if contacto_existe(nombre) else print(
                    f"El contacto {nombre} no existe."
                )
            case "4":
                nombre = get_nombre("Introduce el nombre del contacto a eliminar: ")
                eliminar_contacto(nombre) if contacto_existe(nombre) else print(
                    f"El contacto {nombre} no existe."
                )
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida")
                continue


mi_agenda()
