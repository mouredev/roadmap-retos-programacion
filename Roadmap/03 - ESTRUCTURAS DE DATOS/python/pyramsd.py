'''
Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''
#   Lista:
lista = [1, 2, 3, 4, 5, 15, 30]
print(lista)

#       insercion
lista.append(60) # --> se añade al ultimo
print(lista)

lista.insert(0, 50) # --> .insert(indice, elemento)

#       borrado
elementoBorrado = lista.pop(4) # --> eliminamos el elemento de dicho indice
lista.remove(15) # --> eliminamos con el nombre del elemento
print(elementoBorrado)
print(lista)

#       actualizacion
lista[5] = 20
print(lista)

#       ordenacion
listOrdenada = sorted(lista) # --> sin modificar la lista original
lista.sort() # --> modificando la lista original
print(listOrdenada)
print(lista)

print()

#   Tupla. NOTA: En las tuplas no se pueden hacer ningun tipo de modificaciones
tupla = (100, 25, 3, 47, 5, 61, 7, 88, 93)
print(tupla)

#       ordenacion
tuplaOrdenada = sorted(tupla)
print(tuple(tuplaOrdenada))

print()

#   Sets. NOTA: No se pueden ordenar
miSet = {123, 235235, 46, 345, 3453, 2323}
print(miSet)

#       insercion
miSet.add(90)
print(miSet)
miSet.update([77, 11])
print(miSet)

#       borrado
miSet.remove(90) # --> borra indicando el elemento
print(miSet)
miSet.discard(123)
print(miSet)

print()

#   Diccionarios
dicc = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
print(dicc)

#       insercion
dicc[6] = 'f'
print(dicc)

#       borrado
del dicc[4]
print(dicc)

#       actualizacion
dicc[1] = 'Sergio'
print(dicc)

#       ordenacion
diccionarioOrdenado = sorted(dicc.items())
print(diccionarioOrdenado)

print()

# EXTRA
'''
Crea una contactos de contactos por terminal.
Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
Cada contacto debe tener un nombre y un número de teléfono.
El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
los datos necesarios para llevarla a cabo.
El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
(o el número de dígitos que quieras)
También se debe proponer una operación de finalización del programa.
'''
import re

contactos = {}

while True:
    print('CONTACTOS')
    print('1. Buscar contacto\n2. Añadir contacto \
          \n3. Actualizar contacto\n4. Borrar contacto\
          \n5. Mostrar contactos\n6. Salir')

    choice = input("Ingrese el número de la operación que desea realizar: ")

    if choice == '1':
        nombre = input("Buscar nombre: ")
        if nombre in contactos:
            print(f"Nombre: {nombre}, Teléfono: {contactos[nombre]}")
            print()
        else:
            print(f"El contacto {nombre} no existe en la contactos.\n")

    elif choice == '2':
        nombre = input("Ingrese el nombre del contacto: ")
        telf = input("Ingrese el número de dicho contacto: ")
        if re.match(r'^\d{9}$', telf):
            contactos[nombre] = telf
            print(f"Contacto {nombre} añadido correctamente.\n")
        else:
            print("Error!. Debe ser numérico y tener 9 dígitos.\n")

    elif choice == '3':
        nombre = input("Ingrese el nombre del contacto a actualizar: ")
        if nombre in contactos:
            telf = input("Ingrese el nuevo número de teléfono: ")
            if re.match(r'^\d{9}$', telf):
                contactos[nombre] = telf
                print(f"Contacto {nombre} actualizado correctamente.\n")
            else:
                print("Error!. Debe ser numérico y tener 9 dígitos.\n")
        else:
            print(f"El contacto {nombre} no existe en la contactos.\n")

    elif choice == '4':
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre in contactos:
            del contactos[nombre]
            print(f"Contacto {nombre} eliminado correctamente.\n")
        else:
            print(f"El contacto {nombre} no existe en la contactos.\n")

    elif choice == '5':
        print("\n--- Lista de Contactos ---")
        if len(contactos) != 0: 
            for nombre, telf in contactos.items():
                print(f"Nombre: {nombre}, Telf: {telf}")
        else:
            print('No Hay contactos\n')
        print()

    elif choice == '6':
        print("Saliste del programa")
        break

    else:
        print("Opción no válida. Ingrese un número del 1 al 6.")

