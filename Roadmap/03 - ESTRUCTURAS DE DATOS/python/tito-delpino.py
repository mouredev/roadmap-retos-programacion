# * EJERCICIO:
# * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

# Listas
lista = [6,3,7,4,8,9,2]
print(lista)

lista.append(34) # agregar elementos
print(lista)
lista.remove(2) # eliminar elementos
print(lista)
lista[1] = 22 # cambiar valor de un indice, en este caso el 1
print(lista)
lista.sort() # ordenar de menor a mayor valor
print(lista)

# Tuplas - Solo permiten acceso a ellas, son inmutables
tupla = (6,3,7,4,8,9,2)
print(tupla)

print(tupla[3]) # printea indice 3
tupla = tuple(sorted(tupla)) # indicamos el tipo de dato (tuple) ya que sorter funciona con listas
print(tupla)

# Sets - un set no puede ser ordenado o actualizado, tiene un orden aleatorio
set_conjunto = {6,3,7,4,8,9,2}
set_conjunto.add(99)
print(set_conjunto)
set_conjunto.add(99) # solo contiene elementos unicos sin repeticion, no se agregara este valor
print(set_conjunto)
set_conjunto.remove(2) # elimina el elemento con valor 2, sin tener cuenta el indice, si el elemento no existe, lanza error
print(set_conjunto)
set_conjunto.discard(2) # si el elemento 2 no existe no lanza error
print(set_conjunto)
set_conjunto.update([23,44]) # agregamos varios valores de golpe
print(set_conjunto)
print(type(set_conjunto))
set_conjunto.clear() # vacia el set completo
print(set_conjunto)

# Diccionarios
diccionario = {'clave': 'valor', 'esto es la clave':'esto es el valor de esa clave'}
print(diccionario)
diccionario['nueva clave'] = 'valor agregado'
print(diccionario)
diccionario['nueva clave'] = 'valor actualizado'
print(diccionario)

print(diccionario['clave']) # printea 'valor'
diccionario['clave'] = 'valor actualizado'
print(diccionario['clave']) # valor actualizado'

print(diccionario['esto es la clave']) # printea 'esto es el valor de esa clave'
print(diccionario['nueva clave']) # printea 'valor agregado'

for clave, valor in diccionario.items():
    print(clave) # podemos printear las claves
    print(valor) # podemos printear los valores

print("/" * 50)

""" DIFICULTAD EXTRA (opcional):
    Crea una agenda de contactos por terminal.
* Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
* Cada contacto debe tener un nombre y un número de teléfono.
* El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
* los datos necesarios para llevarla a cabo.
* El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
* (o el número de dígitos que quieras)
* También se debe proponer una operación de finalización del programa."""

def mostrar_agenda():
    for nombre, telefono in agenda.items():
        print("--Nombre:", nombre, "- Telefono:", telefono )

def buscar_contacto(contacto):
    try:
        print("--Telefono -", agenda[contacto])
    except:
        print("No existe este contacto")

def agregar_contacto(contacto):
    if contacto in agenda:
        print("Contacto ya en agenda")
    else:
        telefono = input("Indica el telefono: ")
        if len(telefono) >= 10:
            print("El telefono no puede contener mas de 10 digitos")
        else:
            print("Agregado a agenda")
            agenda[contacto] = int(telefono)

def actualizar_contacto(contacto):
    if contacto not in agenda:
        print("No existe este contacto")
    else:
        eleccion = input("Si quieres actualizar tambien el nombre pulsa 1 sino pulsa 2: ")
        if eleccion == '1':
            nuevo_nombre = input("Indica el nuevo nombre: ")
            del agenda[contacto]
            agregar_contacto(nuevo_nombre.title())
        elif eleccion == '2':
            nuevo_telefono = input("Indica el nuevo telefono: ")
            if len(nuevo_telefono) >= 10:
                print("El telefono no puede contener mas de 10 digitos")
            else:
                print("Contacto actualizado")
                agenda[contacto] = int(nuevo_telefono)

def eliminar_contacto(contacto):
    if contacto not in agenda:
        print("Este nombre no esta entre tus contactos")
    else:
        print("Contacto eliminado")
        del agenda[contacto]


# main
agenda = {"Tito Del Pino":123456, "Ana":654321, "Brais":456789, "Siri": 987654}

while True:
    # menu
    print("---------------Agenda telefonica----------------")
    print("Selecciona un numero de operacion a realizar")
    print("1 - Mostar agenda\n"
        "2 - Buscar contacto\n" \
        "3 - Agregar contacto\n" \
        "4 - Actualizar contacto\n" \
        "5 - Eliminar contacto\n" \
        "6 - Salir")
    print('-' * 50)
    
    # input de usuario
    eleccion_usuario = int(input("Indica la opcion a realizar: "))

    # acciones del menu
    if eleccion_usuario == 1:
        mostrar_agenda()
    elif eleccion_usuario == 2:
        contacto_a_buscar = input("Nombre del contacto a buscar: ")
        buscar_contacto(contacto_a_buscar.title())
    elif eleccion_usuario == 3:
        contacto_a_agregar = input("Nombre del contacto a agregar: ")
        agregar_contacto(contacto_a_agregar.title())
    elif eleccion_usuario == 4:
        contacto_a_actualizar = input("Nombre del contacto a actualizar: ")
        actualizar_contacto(contacto_a_actualizar.title())
    elif eleccion_usuario == 5:
        contacto_a_eliminar = input("Nombre del contacto a eliminar: ")
        eliminar_contacto(contacto_a_eliminar.title())
    elif eleccion_usuario == 6:
        print("Saliendo de la agenda...")
        break
    else:
        print('Debe selecionar una de las opciones del menu')