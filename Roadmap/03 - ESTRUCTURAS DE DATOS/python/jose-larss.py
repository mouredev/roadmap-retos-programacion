"""
Estructuras
"""

# Listas

# Creacion
lista1 = [1, 2, 3, 5, 7, 8, 'a', 'b', 'r']
lista2 :list = [1, 2, 3, 5, 7, 8, 345, 100, 111]

print(lista1)
print(lista2)

# Inserción al final de la lista
lista1.append(345)

print(lista1)

# Eliminación
lista1.remove(1)

print(lista1)

# Acceso
print(lista1[4])

# Actualización
lista1[4] = "jose"

print(lista1)

# Ordenación
lista2.sort()
print(lista2)

# Tuplas

# Creacion
tupla1: tuple = (1, 2, 3, 5, 7, 8, 345, 100, 111)
tupla2 = (1, 2, 3, 5, 7, 8, 345, 100, 111)

print(tupla1)
print(tupla2)

# Acceso
print(tupla1[3])


# Ordenación
tupla1 = tuple(sorted(tupla1))
tupla2 = sorted(tupla2)
print(tupla1)
print(tupla2)

# SETS

# Creacion
set1 = set([1, 2, 3, 5, 7, 8, 'a', 'b', 'r'])
set2 = {1, 2, 3, 5, 7, 8, 'a', 'b', 'r'}

print(set1)
print(set2)

# Inserción al final de la lista
set1.add(5678)
set2.add("piano")

print(set1)
print(set2)

# Eliminación
set1.remove(1)
set1.discard(45678) # borra el elemento pero sino existe lo descarta

print(set1)


# Ordenación
#set1 = set(sorted(set1)) # No se puede ordenar
#print(set1)

# Diccionarios

# Creacion
dicc1 = {'name':'jose', 'apellido':'castro', 'años':45, 'nacionalidad':'España', 'pais':'España'}
dicc2 :dict = {'name':'jose', 'apellido':'castro', 'años':45, 'nacionalidad':'España', 'pais':'España'}

print(dicc1)
print(dicc2)

# Inserción al final de la lista
dicc1['email'] = "pepe@pepe.com"

print(dicc1)

# Eliminación
del dicc1['name']

print(dicc1)

# Acceso
print(dicc1['años'])

# Actualización
dicc1['años'] = 34

print(dicc1)

# Ordenación
dicc1 = dict(sorted(dicc1.items()))
dicc2 = sorted(dicc1.items())
print(dicc1)
print(dicc2)


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
 */
"""

def my_agenda():
    agenda = {}

    def insertar():
        tel = input("Introduce el teléfono del contacto.")
        if len(tel) > 0 and len(tel) <= 11 and tel.isdigit():
            agenda[nombre] = tel
        else:
            print("Debes introducir un número con menos de 11 digitos")

    while True:
        print("*************AGENDA*****************")
        print("1 Búsqueda: ")
        print("2 Inserción: ")
        print("3 Actualización: ")
        print("4 Eliminación: ")
        print("5 Salir")
        print("************************************")

        opcion = input("Que operación deseas realizar?: ")

        match opcion:
            case '1':
                nombre = input("Introduce el nombre a buscar: ")
                if nombre in agenda:
                    print(f"El numero de teléfono de {nombre} es {agenda[nombre]}.")
                else:
                    print(f"El contacto {nombre} NO existe.")
            case '2':
                nombre = input("Introduce el nombre a buscar: ")
                insertar()
            case '3':
                nombre = input("Introduce el nombre a actualizar: ")
                if nombre in agenda:
                    insertar()
                else:
                    print(f"El contacto {nombre} NO existe.")
            case '4':
                nombre = input("Introduce el nombre a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                    print(f"{nombre} se ha eliminado con éxito")
                else:
                    print(f"El contacto {nombre} NO existe.")
            case '5':
                print("Saliendo de la agenda!!")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()