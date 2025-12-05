# #03 ESTRUCTURAS DE DATOS
#### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24
'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
'''

# Estructuras de datos en Python
# Listas
mi_lista = [3, 1, 4, 1, 5]
print(mi_lista)
mi_lista.append(9)  # Inserción
print("Inserción: " + str(mi_lista))
mi_lista.insert(1, 2)  # Inserción en posición concreta
print("Inserción en posición concreta: " + str(mi_lista))
mi_lista.remove(1)  # Borrado
print("Borrado: " + str(mi_lista))
mi_lista2 = [2,4,6,8,4,10,4,12]
while 4 in mi_lista2:
    mi_lista2.remove(4)
print("Borrado de todas las ocurrencias" + str(mi_lista2))  # Borrado de todas las ocurrencias
mi_lista[0:2] = 10, 11    # Actualización utilizando slicing
print("Actualización utilizando slicing: " + str(mi_lista))
mi_lista.sort()  # Ordenación
print("Orden ascendente: " + str(mi_lista))
mi_lista.sort(reverse=True)  # Ordenación inversa
print("Orden descendente: " + str(mi_lista))

# Tuplas
mi_tupla = (3, 1, 4, 1, 5)
print(mi_tupla)

# Conjuntos
mi_conjunto = {3, 1, 4, 1, 5}
print(mi_conjunto)
mi_conjunto.add(9)  # Inserción
print("Inserción: " + str(mi_conjunto))
mi_conjunto.discard(1)  # Borrado
print("Borrado: " + str(mi_conjunto))

# Diccionarios
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
print(mi_diccionario)
mi_diccionario['d'] = 5  # Inserción
print("Inserción: " + str(mi_diccionario))
mi_diccionario['d'] = 4  # Actualización
print("Actualización: " + str(mi_diccionario))
del mi_diccionario['a']  # Borrado
print("Borrado: " + str(mi_diccionario))
mi_diccionario2 = {'h': 7, 'u': 10, 'e': 6, 'v': 0, 'i': 9, 't': 8, 'o': 5, 'r': 4}
mi_diccionario2 = dict(sorted(mi_diccionario2.items()))  # Ordenación por clave
print("Ordenación por clave: " + str(mi_diccionario2))
mi_diccionario2 = dict(sorted(mi_diccionario2.items(), key=lambda item: item[1]))  # Ordenación por valor
print("Ordenación por valor: " + str(mi_diccionario2))

# Dificultad extra: Agenda de contactos
agenda={}
def mostrar_menu():
    print("\n--- Agenda de Contactos ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")
def es_numero_valido(numero):
    return numero.isdigit() and len(numero) <= 11
while True:
    mostrar_menu()
    opcion=input("Seleccione una opción (1-6): ")
    if opcion=="1":
        nombre=input("Ingrese el nombre del contacto: ")
        numero=input("Ingrese el número de teléfono: ")
        if es_numero_valido(numero):
            agenda[nombre]=numero
            print(f"Se ha agregado el contacto {nombre} con el número: {numero}.")
        else:
            print("Número de teléfono no válido.")
    elif opcion=="2":
        nombre=input("Ingrese el nombre del contacto a buscar: ")
        if nombre in agenda:
            print(f"Contacto encontrado: {nombre} - {agenda[nombre]}")
        else:
            print("Contacto no encontrado.")
    elif opcion=="3":
        nombre=input("Ingrese el nombre del contacto a actualizar: ")
        if nombre in agenda:
            numero=input("Ingrese el nuevo número de teléfono: ")
            if es_numero_valido(numero):
                agenda[nombre]=numero
                print(f"El numero de contacto de {nombre} se ha actualizado.")
            else:
                print("Número de teléfono no válido.")
        else:
            print("Contacto no encontrado.")
    elif opcion=="4":
        nombre=input("Ingrese el nombre del contacto a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto {nombre} eliminado.")
        else:
            print("Contacto no encontrado.")
    elif opcion=="5":
        if agenda:
            print("\n--- Contactos en la Agenda ---")
            for nombre, numero in agenda.items():
                print(f"{nombre}: {numero}")
        else:
            print("La agenda está vacía.")
    elif opcion=="6":
        print("Saliendo de la agenda. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")



        




