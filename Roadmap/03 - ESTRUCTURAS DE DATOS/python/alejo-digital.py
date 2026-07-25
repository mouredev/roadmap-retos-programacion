# 03 ESTRUCTURA DE DATOS

"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

# Estructuras de datos en Python

# Listas
mi_lista = [1, 2, 3, 4, 5]
mi_lista.append(6)  # Inserción
mi_lista.remove(3)  # Borrado
mi_lista[0] = 10  # Actualización
mi_lista.sort()  # Ordenación
print("Mi lista es:", mi_lista)
# Tuplas
mi_tupla = (1, 2, 3, 4, 5)
# Las tuplas son inmutables, no se pueden modificar directamente
print("Mi tupla es:", mi_tupla)
# Conjuntos
mi_conjunto = {1, 2, 3, 4, 5}
mi_conjunto.add(6)  # Inserción
mi_conjunto.discard(3)  # Borrado
print("Mi conjunto es:", mi_conjunto)
# Diccionarios
mi_diccionario = {'nombre': 'Alejandro', 'edad': 30}
mi_diccionario['edad'] = 31  # Actualización
mi_diccionario['telefono'] = '123456789'  # Inserción
del mi_diccionario['nombre']  # Borrado
print("Mi diccionario es:", mi_diccionario)

# DIFICULTAD EXTRA: Agenda de contactos por terminal

def agenda_contactos():
    agenda = {}

    while True:
        print("\nAgenda de Contactos")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Introduce el nombre del contacto a buscar: ")
            if nombre in agenda:
                print(f"Contacto encontrado: {nombre} - {agenda[nombre]}")
            else:
                print("Contacto no encontrado.")

        elif opcion == '2':
            nombre = input("Introduce el nombre del nuevo contacto: ")
            telefono = input("Introduce el número de teléfono: ")
            if telefono.isdigit() and len(telefono) <= 11:
                agenda[nombre] = telefono
                print(f"Contacto {nombre} añadido.")
            else:
                print("Número de teléfono no válido.")

        elif opcion == '3':
            nombre = input("Introduce el nombre del contacto a actualizar: ")
            if nombre in agenda:
                telefono = input("Introduce el nuevo número de teléfono: ")
                if telefono.isdigit() and len(telefono) <= 11:
                    agenda[nombre] = telefono
                    print(f"Contacto {nombre} actualizado.")
                else:
                    print("Número de teléfono no válido.")
            else:
                print("Contacto no encontrado.")

        elif opcion == '4':
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto {nombre} eliminado.")
            else:
                print("Contacto no encontrado.")

        elif opcion == '5':
            print("Saliendo de la agenda, hasta pronto.")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Llamada a la función de la agenda de contactos
agenda_contactos()
print("\nFin del reto. ¡Sigue practicando y aprendiendo!")