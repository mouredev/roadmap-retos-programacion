"""
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
"""

#-------Strings-------

#Creación de una cadena de una sola línea o de varias
cadena_caracteres = "Hola Mundo!!"
print(cadena_caracteres)

cadena_varias_lineas = '''Esto es una cadena de caracteres de varias líneas.
Es igual a un string de una sola línea, pero se deben poner 3 comillas para 
ser creada'''
print(cadena_varias_lineas)

#Concatenación de cadenas
cadena_unida = cadena_caracteres + cadena_varias_lineas
print(cadena_unida)

#Formateo de de cadenas
lenguaje = "Python"
version = "3.11.4"
print(f"Estoy utilizando el lenguake de programación {lenguaje} en la versión {version}")

#Slicing de cadenas
primera_palabra = cadena_varias_lineas[0:4]
print(primera_palabra)

ultima_palabra = cadena_varias_lineas[-6:]
print(ultima_palabra)

#Revertir una cadena
cadena_invertida = cadena_varias_lineas[::-1]
print(cadena_invertida)

#Capitalize 
cadena_mayusculas = cadena_varias_lineas.upper()
print(cadena_mayusculas)

#Lower
cadena_minusculas = cadena_mayusculas.lower()
print(cadena_minusculas)

#Eliminar espacios al principio y fianl de unade una cadena
eliminar_espacios = cadena_varias_lineas.lstrip().rstrip()
print(f"Cadena sin espacios {eliminar_espacios}")

#Algunos métodos de cadenas
conteo_y = cadena_varias_lineas.count('e')
print(f"Hay {conteo_y} 'y' en la cadena")

encontrar_a = cadena_varias_lineas.find('a')
print(f"La primera a está en la possición: {encontrar_a}")

encontrar_ultima_a = cadena_varias_lineas.rfind('a')
print(f"La última 'a' está en la posición {encontrar_ultima_a}")

empieza_con = cadena_varias_lineas.startswith('A')
print(f"La cadena empiea con 'A': {empieza_con}")

acaba_con = cadena_varias_lineas.endswith('da')
print(f"La cadena acaba con 'da': {acaba_con}")

reemplazar = cadena_varias_lineas.replace('e', 'u')
print(reemplazar)

#-------Listas-------

#Creación de una lista
mi_lista = [0,5,3,2,1,4]
print(mi_lista)

#Otra forma de crear una lista
mi_lista_2 = list(["Hola", "Adios"])
print(mi_lista_2)

#Inserción de un elemento mediante el método append()
mi_lista.append(6)
print(f"Lista método append(): {mi_lista}")

#Inserción de un elemento mediante el método insert()
mi_lista.insert(0, "Hola")
print(f"Lista método inster(): {mi_lista}")

#Ampliación de de una lista mediante otra con el método extend()
mi_lista.extend(mi_lista_2)
print(f"Lista método externd(): {mi_lista}")

#Borrado de un elemento mediante el método remove()
mi_lista.remove("Adios")
print(f"Lista método remove(): {mi_lista}")

#Borrado de un elemento mediante el método pop() (elimina el último elemento)
mi_lista.pop()
print(f"Lista método pop() {mi_lista}")

#Borrado de un elemento mediante el método del
del mi_lista[0]
print(f"Lista método del: {mi_lista}")

#Borrado de todos los elementos mediante el clear()
mi_lista_2.clear()
print(f"Lista vacía con el método clear(): {mi_lista_2}")

#Ordenación de una lista con el método sort()
mi_lista.sort(reverse=True)
print(f"Lista ordenada de mayor a menor con el método sort(): {mi_lista}")

#Ordenación de una lista con el método sorted() y una función
lista_frutas = ["manzana", "pera", "plátano", "melocotón", "fresa"]

def longitud_elementos(elemento):
    return len(elemento)

lista_ordenada = sorted(lista_frutas, key=longitud_elementos)
print(lista_ordenada)


#-------Tuplas-------

#Creación de una tupla
animales = ("gato", "perro", "caballo", "vaca", "cabra", "conejo")
print(animales)

#Otra forma de crear una tupla
mi_tupla2 = tuple([1,2,3,4,5])
print(mi_tupla2)

#Unión de dos tuplas
union_tuplas = animales + mi_tupla2
print(f"Unión de las tuplas: {union_tuplas}")

#Comprobar si un elemento está en la tupla
print("caballo" in animales)

#Borrado de una tupla
del animales

#Al ser inmutables, las tuplas no se pueden alterar ni ordenar, por lo que solo podemos crearlas y borraralas.


#-------Sets-------

#Creación de un set
transportes = {"coche", "moto", "autobús", "tren", "avión"}
print(transportes)

#Otro forma de crear un set
deportes = set(["fútbol", "baloncesto", "atletismo"])
print(deportes)

#Añadir un elemento a un set con el método add()
deportes.add("balonmano")
print(deportes)

#Añadir varios elementos a un set con el método update()
deportes.update(["escalada", "natación", "tenis"])
print(deportes)

#Comprobar si son subsets o supersets
set1 = {1,2,3,4,5}
set2 = {2,4,5}
print(f"Set1 es superset de set2: {set1.issuperset(set2)}")
print(f"Set2 es subset de Set1: {set2.issubset(set1)}")

#Comprobar elemntos comunes entre sets
print(f"La itersección entre set2 y set1 es: {set2.intersection(set1)}")

print(f"set1 y set2 no tienen elementos comunes: {set1.isdisjoint(set2)}")

#Eliminar un elemento de un set con el método remove()
transportes.remove("avión")
print(transportes)

#Eliminar todos los elementos de un set con el método clear()
transportes.clear()
print(transportes)

#Eliminar un set con el método del
del transportes


#-------Diccionarios-------

#Crear un diccionario
dict_paises = {
   "España": "Madrid",
   "Francia": "París",
   "Alemania": "Berlín",
   "Italia": "Roma",
   "Reino Unido": "Londres"
}
print(dict_paises)

#Añadir una nueva clave y un valor al diccionario
dict_paises["Rusia"] = "Moscú"
print(dict_paises)

#Modificar un valor de un diccionario
dict_paises["España"] = "Barcelona"
print(dict_paises)

#Obtener un valor de un diccionario y pasar un valor si este no existe
capital_dict = dict_paises.get("Reino Unido")
print(f"La capital de Reino Unido es: {capital_dict}")

capital = dict_paises.get("Bélgica", "Bruselas")
print(f"La capital de Bélgia es: {capital}")

#Comprobar si una clave está en un diccionario
print(f"Francia está en el diccionario: {'Francia' in dict_paises}")

#Eliminar el último elemento del diccionario
dict_paises.popitem()
print(dict_paises)

#Eliminar un elemento en concreto de un diccionario
dict_paises.pop('Alemania')
print(dict_paises)

#Obtener las claves de un diccionario como una lista
claves = dict_paises.keys()
print(f"Las claves del diccionario son: {claves}")

#Obtner los valores de un diccionario como una lista
valores = dict_paises.values()
print(f"Los valores del diccionario son: {valores}")

#Eliminar todos los elementos del diccionario con el método clear()
dict_paises.clear()
print(f"El diccionario ahora sta vacío: {dict_paises}")

#Eliminar el diccionario con el método del
del dict_paises



#-------EXTRA-------

def agenda():
    dict_agenda = {"Bomberos": '1234', "Policia": '091', "Emergencias": '112'}

    while True:
        def menu():
            print("""Accediendo a la agenda de contactos...\n
                Elija una opción por favor:
                -------------------------------------------
                Opcion 1: Nuevo contacto 
                Opción 2: Busqueda de un contacto existente
                Opción 3: Editar contacto existente
                Opcion 4: Eliminar un contacto existente
                Opcion 5: Salir\n""")
            return int(input("Indique una opción: "))

        opcion = menu()

        if opcion == 1:
            agregar_contacto(dict_agenda)

        elif opcion == 2:
            buscar_contacto(dict_agenda)

        elif opcion == 3:
            editar_contacto(dict_agenda)

        elif opcion == 4:
            eliminar_contacto(dict_agenda)

        elif opcion == 5:
            print("¡Gracias por usar nuestra agenda! ¡Hasta luego!")
            break


def agregar_contacto(diccionario):
    nombre = input("Introduzca el nombre del nuevo contacto: ").lower().capitalize()
    telefono = input("Introduzca un número de teléfono de máximo 11 dígitos: ")
    
    while not (telefono.isdecimal() and len(telefono) <= 11):
        telefono = input("Número de teléfono inválido. Vuelva a intentarlo: ")
        
    diccionario[nombre] = telefono
    print(f"¡Contacto {nombre} añadido correctamente!\n")
    imprimir_contactos(diccionario)


def buscar_contacto(diccionario):
    print("-----Buscador de contactos-----")
    contacto = input("Introduzca el nombre del contacto: ").lower().capitalize()

    if contacto in diccionario:
        print(f"{contacto}: {diccionario[contacto]}\n")
    else:
        respuesta = input("No hay ningún contacto en la agenda con ese nombre. ¿Desea realizar otra acción? Y/N ").lower()
        if respuesta != 'y':
            print("¡Gracias por usar nuestra agenda! ¡Hasta luego!")


def editar_contacto(diccionario):
    print("-----Editor de contactos-----")
    imprimir_contactos(diccionario)
    contacto = input("Indique el nombre del que desea editar: ").lower().capitalize()

    if contacto in diccionario:
        respuesta = input("¿Desea editar el nombre del contacto (1) o el número (2)? : ")
        if respuesta == '1':
            nuevo_nombre = input("Introduzca el nuevo nombre de contacto: ").lower().capitalize()
            diccionario[nuevo_nombre] = diccionario.pop(contacto)
        elif respuesta == '2':
            nuevo_numero = input("Introduzca el nuevo número de teléfono: ")
            while not (nuevo_numero.isdecimal() and len(nuevo_numero) <= 11):
                nuevo_numero = input("Número de teléfono inválido. Vuelva a intentarlo: ")
            diccionario[contacto] = nuevo_numero
        print("Contacto editado correctamente.\n")
        imprimir_contactos(diccionario)
    else:
        print("No hay ningún contacto en la agenda con ese nombre.\n")


def eliminar_contacto(diccionario):
    print("-----Eliminar un contacto-----")
    imprimir_contactos(diccionario)
    contacto = input("¿Qué contacto desea eliminar? ").lower().capitalize()

    if contacto in diccionario:
        valor_eliminado = diccionario.pop(contacto)
        print(f"Se eliminó el contacto {contacto} con el valor {valor_eliminado}\n")
        imprimir_contactos(diccionario)
    else:
        print("No hay ningún contacto en la agenda con ese nombre.\n")


def imprimir_contactos(diccionario):
    print("Estos son los contactos almacenados en la agenda:")
    for nombre, telefono in diccionario.items():
        print(f"{nombre}: {telefono}")
    print()


agenda()