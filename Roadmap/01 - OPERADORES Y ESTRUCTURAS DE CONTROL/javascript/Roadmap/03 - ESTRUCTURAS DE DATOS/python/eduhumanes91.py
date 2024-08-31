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
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
'''

# Creación de estructuras de datos en Python
# Listas
lista = [1, 2, 3, 4, 5]
print(lista)

# Tuplas
tupla = (1, 2, 3, 4, 5)
print(tupla)

# Diccionarios
diccionario = {'clave1': 'valor1', 'clave2': 'valor2'}
print(diccionario)

# Conjuntos
conjunto = {1, 2, 3, 4, 5}
print(conjunto)

# Operaciones de inserción, borrado, actualización y ordenación
# Listas
lista.append(6)
print(lista)

lista.remove(6)
print(lista)

lista[0] = 0
print(lista)

lista.sort()
print(lista)

# Tuplas
# No se pueden modificar, por lo que no se pueden hacer inserciones, borrados ni actualizaciones
# Sí se pueden ordenar
tupla_ordenada = sorted(tupla)
print(tupla_ordenada)

# Diccionarios
diccionario['clave3'] = 'valor3'
print(diccionario)

del diccionario['clave3']
print(diccionario)

diccionario['clave1'] = 'nuevo_valor1'
print(diccionario)

# Conjuntos
conjunto.add(6)
print(conjunto)

conjunto.remove(6)
print(conjunto)

# No se pueden hacer actualizaciones ni ordenaciones
# Sí se pueden hacer inserciones y borrados
# Para ordenar un conjunto, hay que convertirlo a lista
lista_conjunto = list(conjunto)
lista_conjunto.sort()
conjunto_ordenado = set(lista_conjunto)
print(conjunto_ordenado)

# Agenda de contactos
agenda = {"Eduardo Humanes Saiz": "651488455", "Juan Pérez": "666555444", "María López": "611222333", "Ana García": "633444555"}

print("\n ****Agenda de contactos**** \n")
print("¿Que operación desea realizar? \n 1. Buscar contacto\n 2. Añadir contacto\n 3. Actualizar contacto\n 4. Eliminar contacto\n 5. Salir\n")

operacion = int(input("Por favor, introduzca el número de la operación que desea realizar: "))

def buscar_contacto():
    nombre = input("Por favor, introduzca el nombre del contacto que desea buscar: ")
    if nombre in agenda:
        print(f"El número de teléfono de {nombre} es {agenda[nombre]}")
    else:
        print(f"El contacto {nombre} no se encuentra en la agenda")
        return

def anadir_contacto():
    nombre = input("Por favor, introduzca el nombre del contacto que desea añadir: ")
    telefono = input("Por favor, introduzca el número de teléfono del contacto que desea añadir: ")
    if telefono.isdigit() and len(telefono) == 9:
        agenda[nombre] = telefono
        print(f"El contacto {nombre} con número de teléfono {telefono} ha sido añadido a la agenda")
    else:
        print("El número de teléfono introducido no es válido")
        return

def actualizar_contacto():
    nombre = input("Por favor, introduzca el nombre del contacto que desea actualizar: ")
    if nombre in agenda:
        telefono = input("Por favor, introduzca el nuevo número de teléfono del contacto: ")
        if telefono.isdigit() and len(telefono) == 9:
            agenda[nombre] = telefono
            print(f"El número de teléfono de {nombre} ha sido actualizado a {telefono}")
        else:
            print("El número de teléfono introducido no es válido")
            return
    else:
        print(f"El contacto {nombre} no se encuentra en la agenda")
        return

def eliminar_contacto():
    nombre = input("Por favor, introduzca el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido eliminado de la agenda")
    else:
        print(f"El contacto {nombre} no se encuentra en la agenda")
        return

def salir():
    print("Hasta luego!")
    exit()

if operacion == 1:
    buscar_contacto()
elif operacion == 2:
    anadir_contacto()
elif operacion == 3:
    actualizar_contacto()
elif operacion == 4:
    eliminar_contacto()
elif operacion == 5:
    salir()
else:
    print("Operación no válida")
    exit()
