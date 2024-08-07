"""  * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación. """
 
"""--------------------------- Listas ---------------------------"""
 # Creación de una lista
mi_lista = [1, 2, 3, 4, 5]

# Inserción al final
mi_lista.append(6)

# Inserción en una posición específica
mi_lista.insert(2, 10)

# Actualización de un elemento
mi_lista[1] = 20

# Borrado de un elemento por valor
mi_lista.remove(4)

# Borrado de un elemento por índice
del mi_lista[0]

# Ordenación ascendente
mi_lista.sort()

# Ordenación descendente
mi_lista.sort(reverse=True)

print("Lista despues de operaciones:", mi_lista)

"""--------------------------- Tuplas ---------------------------"""
# Creación de una tupla
mi_tupla = (1, 2, 3, 4, 5)

# Acceso a elementos por índice
elemento = mi_tupla[2]

# Concatenación de tuplas
otra_tupla = (6, 7, 8)
nueva_tupla = mi_tupla + otra_tupla

print("Elemento de la tupla:", elemento)
print("Nueva tupla:", nueva_tupla)

"""--------------------------- Conjuntos ---------------------------"""
# Creación de un conjunto
mi_conjunto = {1, 2, 3, 4, 5}

# Inserción
mi_conjunto.add(6)

# Borrado por valor
mi_conjunto.remove(3)

# Actualización con otro conjunto
otro_conjunto = {4, 5, 6, 7}
mi_conjunto.update(otro_conjunto)

print("Conjunto después de operaciones:", mi_conjunto)

"""--------------------------- Diccionarios ---------------------------"""
# Creación de un diccionario
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Inserción o actualización de un par clave-valor
mi_diccionario['d'] = 4

# Borrado por clave
del mi_diccionario['b']

# Acceso a valores por clave
valor = mi_diccionario['c']

# Obtención de claves y valores
claves = mi_diccionario.keys()
valores = mi_diccionario.values()

print("Valor del diccionario:", valor)
print("Claves del diccionario:", claves)
print("Valores del diccionario:", valores)

""" * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa. """
 
nombres = []
telefonos = []
j = 0
 
def buscar_contacto(x):
    while(j == 0):
        contador = 0
        print("1) Buscar por nombre")
        print("2) Buscar por numero de telefono")
        print("3) Volver atras")
        try:
            opcion_busqueda = int(input("Selecciona el tipo de busqueda: "))
        except:
            print("Error: Esta opcion debe contener solo numeros")
            continue
        print("---------------------------------")
        if opcion_busqueda == 1:
            nombre = input("Ingrese el nombre del contacto que desea buscar: ")
            for i in nombres:
                if nombre == i:
                    print("Contacto encontrado con exito");
                    print("Nombre: " + nombres[contador])
                    print("Telefono: " + str(telefonos[contador]))
                    print("---------------------------------")
                    if x == 1:
                        return contador
                    break
                else:
                    contador += 1   
        elif opcion_busqueda == 2:
            while(j == 0):
                try:
                    telefono = int(input("Ingrese el numero del contacto que desea buscar: "))
                except:
                    print("Error: Esta opcion debe contener solo numeros")
                    continue   
                for i in telefonos:
                    if telefono == i:
                        print("Contacto encontrado con exito");
                        print("Nombre: " + nombres[contador])
                        print("Telefono: " + str(telefonos[contador]))
                        print("---------------------------------")
                        if x == 1:
                            return contador
                        break
                    else:
                        contador += 1  
                break
        elif opcion_busqueda == 3:
            print("---------------------------------")
            break
        else:
            print("Opcion incorrecta")
            print("---------------------------------")
            
def insertar_contacto():
    while(j == 0):
        nombres.append(input("Ingrese el nombre: "))
        try:
            telefono = int(input("Ingrese el numero de telefono: "))
        except:
            print("Error: Esta opcion debe contener solo numeros")
            continue
        telefonos.append(telefono)
        print("Contacto agregado con exito")
        print("---------------------------------")
        opcion_insertar = input("Si desea añadir otro contacto pulse la tecla 'a': ")
        if opcion_insertar != 'a':
            print("---------------------------------")
            break

def actualizar_contacto():
    indice = buscar_contacto(1)
    while(j == 0):
        print("1) Actualizar nombre")
        print("2) Actualizar numero de telefono")
        print("3) Buscar otro contacto")
        print("4) Volver atras")
        try:
            opcion_actualizar = int(input("Seleccione una opcion: "))
        except:
            print("Error: Esta opcion debe contener solo numeros")
            continue
        print("---------------------------------")
        if opcion_actualizar == 1:
            nombres[indice] = input("Ingrese el nuevo nombre para este contacto: ")
            print("Contacto actualizado con exito")
            print("---------------------------------")
        elif opcion_actualizar == 2:
            while(j == 0):
                try:
                    telefono = int(input("Ingrese el nuevo telefono para este contacto: "))
                except:
                    print("Error: Esta opcion debe contener solo numeros")
                    continue
                telefonos[indice] = telefono
                print("Contacto actualizado con exito")
                print("---------------------------------")
                break
        elif opcion_actualizar == 3:
            indice = buscar_contacto(1)
            print("---------------------------------")
        elif opcion_actualizar == 4:
            print("---------------------------------")
            break
            
def eliminar_contacto():
    indice = buscar_contacto(1)
    while(j == 0):
        opcion_eliminar = input("Pulse la tecla 'a' para confirmar la eliminacion de este contacto: ")
        print("---------------------------------")
        if opcion_eliminar != 'a':
            while(j == 0):
                print("1) Buscar otro contacto")
                print("2) Volver atras")
                try:
                    opcion_eliminar2 = int(input("Elija una opcion: "))
                except:
                    print("Error: Esta opcion debe contener solo numeros")
                    continue
                print("---------------------------------")
                break
            if opcion_eliminar2 == 1:
                indice = buscar_contacto(1)
                print("---------------------------------")
            elif opcion_eliminar2 == 2:
                print("---------------------------------")
                break
        else:
            del nombres[indice]
            del telefonos[indice]
            print("Contacto eliminado con exito")
            while(j == 0):
                print("1) Buscar otro contacto")
                print("2) Volver atras")
                try:
                    opcion_eliminar2 = int(input("Elija una opcion: "))
                except:
                    print("Error: Esta opcion debe contener solo numeros")
                    continue
                print("---------------------------------")
                break
            if opcion_eliminar2 == 1:
                indice = buscar_contacto(1)
                print("---------------------------------")
            elif opcion_eliminar2 == 2:
                print("---------------------------------")
                break
            
while(j == 0):
    print("Bienvenido a tu agenda de contactos")
    print("---------------------------------")
    print("1) Buscar un contacto")
    print("2) Insertar un contacto")
    print("3) Actualizar un contacto")
    print("4) Eliminar un contacto")
    print("5) Salir")
    print("---------------------------------")
    try:
        opcion = int(input("Selecciona la operacion a realizar: "))
    except:
        print("Error: Esta opcion debe contener solo numeros")
        continue
    if opcion == 1:
        buscar_contacto(0)
    elif opcion == 2:
        insertar_contacto()
    elif opcion == 3:
        actualizar_contacto()
    elif opcion == 4:
        eliminar_contacto()
    elif opcion == 5:
        print("Cerrando agenda de contactos")
        print("---------------------------------")
        break
    else:
        print("Opcion incorrecta, intentelo de nuevo")
        print("---------------------------------")



