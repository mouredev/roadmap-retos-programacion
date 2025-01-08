'''
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
'''

#Python tiene 4 estructuras de almacenamiento de datos, estas son las listas, tuplas, set(conjuntos) y diccionarios

#------- LISTAS -------

'''
Las listas son un tipo de conjunto de datos que pueden ser
ordenados, modificados y permite tener elementos duplicados

'''

lista_1 = [1, 2, 3, 4, 5, 6, 7] #Esto es una lista
lista_2 = ["Hola", 34, 'D', True, 7.0]
lista_3 = ["Auto", "Tren", "Barco", "Avion"]

n_item_l1 = 0
print("---- Elementos lista 3 ----")

for l1 in lista_1:
    print(f"Elemento {n_item_l1}: {l1}")
    n_item_l1 += 1

n_item_l2 = 0
print("---- Elementos lista 3 ----")

for l2 in lista_2:
    print(f"Elemento {n_item_l2}: {l2}")
    n_item_l2 += 1

n_item_l3 = 0
print("---- Elementos lista 3 ----")

for l3 in lista_3:
    print(f"Elemento {n_item_l3}: {l3}")
    n_item_l3 += 1

# -------- Operaciones de inserción, borrado, actualización y ordenación --------

# append() --> Agregar elementos
lista_1.append(8)
print(f"Usando comando .append añadimos 8 a lista_1: {lista_1}")

#remove() --> Remover elementos
lista_2.remove("Hola")
print(f"Usando comando .remove quitamos 'Hola' de lista_2: {lista_2}")

#pop() --> Eliminar el ultimo elemento
lista_3.pop()
print(f"Usando comando .pop quitamos el ultimo elemento de lista_3: {lista_3}")

#reverse() --> Invertir el orden
lista_1.reverse()
print(f"Usando comando .reverse invertimos el orden de lista_3: {lista_1}")

#sort() --> Ordenar en de manera ascendente
lista_3.sort()
print(f"Usando comando .sort ordenamos lista_3 en orden ascendente(alfabetico): {lista_3}")

#insert() --> Añade un elemento en una determinada posición
lista_2.insert(5, "Amigo")
print(f"Usando comando .insert añadimos un elemento en una determinada posición de lista_2: {lista_2}")

#count() --> Revisa cuantas veces se repite un determinado item dentro de la lista
conteo = lista_1.count(4)
print(f"Usando comando .count obentemos la cantidad 4s que contiene lista_1: {conteo}")

#extend() --> Extiende una lista a partir de otra (une 2 listas)
lista_2.extend(lista_3)
print(f"Usando comando .extend agregamos los elementos de lista_3 a lista_2 (imprimimos la lista a la que se le agregaron): {lista_2}") 


#------- TUPLAS -------
'''
Las tuplas son vaiable que pueden almacenar diferentes valores,
a diferencia de las listas sus valores son inmutables (no se pueden
o agregar nuevo valores).
'''

tupla_1 = ("Ivan", "Sebastian", "Dante", "Benjamin", "Diego") #Esta es una tupla con un solo tipo de dato
tupla_2 = ("Hola", 3, True, 4.5, 'S') #Esto es una tupla con diferentes tipos de datos
tupla_3 = (1, 2, 3, 4, 5, 6, 7)

n_item = -1
print("---- Tupla 1 ----")
for t1 in tupla_1:
    n_item += 1
    print(f"Elemento de tupla {n_item} = {t1}")

print("---- Tupla 2 ----")
for t2 in tupla_2:
    n_item += 1
    print(f"Elemento de tupla {n_item} = {t2}")

# -------- Formas de acceder a una tupla --------

print(f"Elemento de la tupla 1, posición 0: {tupla_1[0]}") #Acceder a un elemento de una tupla es por medio del indice
print(f"Elemento de la tupla 1, posición 4: {tupla_1[-1]}") #Acceder a un elemento de una tupla hacia atras (ultimo elemento)
print(f"Elemento de la tupla 2, posición 2 a 4: {tupla_2[2:5]}") #Acceder a un rango de elementos de la tupla (2 al 4)
print(f"Elemento de la tupla 2, posición 0 a 2: {tupla_2[:2]}") #Acceder a un rango de elementos desde la primera posición hasta n (0:2)
print(f"Elemento de la tupla 3, posición 3 a 0: {tupla_3[3:]}") #Acceder a un rango de elementos desde la ultima posición hasta n (3:)

# -------- Revisar si hay elementos en tuplas --------

if 4 in tupla_3:
    print("4 está en la tupla")
else:
    print("4 no está en la tupla")


# -------- Operaciones de inserción, borrado, actualización y ordenación --------
    
i = tupla_3.count(5) #count(): Retorna el número de veces un valor especifico de una tupla
print(f"El elemento 5 está {i} veces")

f = len(tupla_3) #len(): Retorna el largo de una tupla
print(f"El largo de la tupla es {f}")

r = tupla_1.index("Sebastian")
print(f"La posición de Sebastian en la tupla es {r}")

'''
---- Operaciónes que NO están permitidas en las tuplas ----
- append() --> Agregar elementos
- remove() --> Remover elementos
- pop() --> Eliminar el ultimo elemento
- reverse() --> Invertir el orden
- sort() --> Ordenar en de manera ascendente
- insert() --> Añade un elemento en una determinada posición
'''

 
#------- CONJUNTOS(SET) -------

'''
Los sets son conjuntos de datos no ordenados, inmutables y sin
valores duplicados, además no se sabe en que orden aparecen al
imprimirse (toman posiciones aleatorias).

Los items de un set no pueden cambiarse despues de que han sido
creados, pero si se pueden añadir y remover items, además, los
set pueden tener valores de diferentes tipos.
'''

set_1 = {"apple", "bananna", "carrot", "lemon", "pinapple", "watermelon"}
set_2 = {1, 2, 3, 4, 5, 6, 7}
set_3 = {"hola", 3, 5.7, True, 'D', False}

#Los items aparecen en orden diferente a los que tenian al crear el set

print("---- Elementos Set 1 ----")
n_itemSet_1 = 0
for e in set_1:
    print(f"Elemento posición {n_itemSet_1}: {e}")
    n_itemSet_1 += 1

print("---- Elementos Set 2 ----")
n_itemSet_2 = 0
for e in set_2:
    print(f"Elemento posición {n_itemSet_2}: {e}")
    n_itemSet_2 += 1

print("---- Elementos Set 3 ----")
n_itemSet_3 = 0
for e in set_3:
    print(f"Elemento posición {n_itemSet_3}: {e}")
    n_itemSet_3 += 1

# -------- Formas de acceder a un set --------

'''
Las formas de acceder a un item dentro de un set es iterando sobre el
con un bucle for o bien consultando directamente si está dentro del set.
'''

print("pinapple" in set_1)
print(10 in set_2)
print(3 in set_3) #En los sets, se toma al valor 1 como True, al 0 como False y viceversa

# -------- Operaciones de inserción, borrado, actualización y ordenación --------

#Para añadir un elemento al set utilizamos el método ADD()
set_1.add("Blueberry")
print(set_1)

#Para combinar sets utilizamos el método UPDATE()
set_4 = {"Potatoe", "Tomatoe", "Lettuce", "Onion"} #En este caso el set_2 recibe los items del set_4, al imprimir el set_2 se visualizan los nuevos datos
set_1.update(set_4)
print(set_1)

#Para remover elementos de un set utilizamos el método REMOVE()
set_3.remove(5.7)
print(set_3)

#Para remover un elemento del set utilizamos el método POP() (este método remueve un elemento random del set)
set_4.pop("Onion")
print(set_4)

'''
Tambien se pueden ver otros tipos de métodos:

- clear() -> Elimina todos los elementos de un set
- copy() -> Copia un set
- difference() -> Retorna un set que contiene la diferencia entre 2 o más sets
- discard() -> Remueve un elemento especifico
- intersection() -> Retorna un set que es la intersección de los otros sets
''' 


#------- DICCIONARIOS -------
'''
Diccionarios son usados para guardar datos en parejas clave:valor.
Un diccionario es una colección la cual está ordenada, es mutable y admite
elementos duplicados.
'''
dictionary_1 = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
print(dictionary_1)

#Se puede referenciar un elemento del diccinario por medio de clave entre corchetes
print(dictionary_1["Model"])

#Los diccionarios pueden guardar varios tipos de datos

dictionary_2 = {
    "boolean": True,
    "String": "hola",
    "Integger": 25,
    "Float": 7.5,
    "List": [1, 2, 3, 4, 5]
}
print(dictionary_2)

#Podemos usar un método especial para construir diccionarios
valor_1 = 0
valor_2 = 0
valor_3 = 0

dictionary_3 = dict(valor_1 = 23, valor_2 = 43, valor_3 = 65)
print(dictionary_3)

# -------- Formas de acceder a un diccionario --------

'''
Podemos usar 2 métodos particulares, llamar al elemento a partir de su clave
o bien usar el método "get()". Tambien podemos usar el método "keys()" para obtener una lista
de todas las claves del diccionario. Por otro lado, se pueden obtener los valores del diccionario
usando el metodo "values()", además podemos imprimir las parejas "clave:valor" en forma de tupla.
Finalmente, podemos revisar si una clave en particular está dentro del diccionario.
'''

#Usando la clave
item_1 = dictionary_2["List"]
print(item_1)

#Usando get
item_2 = dictionary_2.get("String")
print(item_2)

#Consiguiendo las claves del diccionario
item_3 = dictionary_1.keys()
print(item_3)

#Consiguiendo los valores del diccionario
item_4 = dictionary_1.values()
print(item_4)

#Consiguiendo las parejas del diccionario en forma de tupla
item_5 = dictionary_3.items()
print(item_5)

#Tanto en Keys, Values e Items no se reflejan los cambios en el diccionario solo los valores que tiene registrados hasta el momento que se le llame

#Revisando si una clave está en el diccionario
if "valor_4" in dictionary_3:
    print("Valor 4 está en el diccionario 3")
else:
    print("El valor 4 no está en el diccionario 3")

# -------- Operaciones de inserción, borrado, actualización y ordenación --------

#Ya se vieron get(), keys(), values() e items()

#El método POP elimina un elemento del diccionario, para ello se debe acceder por medio de su clave
dictionary_1.pop("Brand")
print(dictionary_1)

#El método POP ITEM elimina la ultima pareja clave-valor del diccionario
dictionary_2.popitem()
print(dictionary_2)

#El método UPDATE inserta un valor especifico en el diccionario
dictionary_3.update(valor_4 = 74)
print(dictionary_3)


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

def updateInfo(name, number): #Recibimos el nombre y número actual del usuario
    print("----- Item to Update -----")
    print("1) Update Name - 2) Update Number")
    itemUpdate = int(input("Selec item: "))
    if itemUpdate == 1:
        newName = input("New Name contact: ")
        contacts.pop(name)
        contacts[newName] = number
    elif itemUpdate == 2:
        newNumber = input("New number contact: ")
        contacts[name] = newNumber
    else:
        print("The option is not allowed")
    return contacts #Eventualmente el diccionario podría retornar los valores 2 en forma de lista o tupla y no todo el diccionario

# Construcción del programa
contacts = {}
while True:
    print("--- Functions Available ---")
    print("1. Insertion")
    print("2. Update")
    print("3. Delete")
    print("4. Search Contact")
    funcSelected = int(input("Selec a function: "))

    if funcSelected == 1: #---------- Añadir contactos ---------
        print("--- Add a new Contact ---")
        contactName = input("New Contact: ")
        while True:
            contactNumber = input("Contact Number: ")
            if len(contactNumber) < 11:
                contacts[contactName] = contactNumber
                break
            else:
                print("Number excess the limit, try again")
    elif funcSelected == 2: #---------- Editar contactos ---------
        print("--- Update a Contact ---")
        print(contacts) #Se imprimen los nombres contactos para ver los datos a cambiar
        selecUser = input("Contact: ")
        info_update = updateInfo(selecUser, contacts[selecUser])
    elif funcSelected == 3: #---------- Eliminar contactos ---------
        print("--- Delete a Contact ---")
        print(contacts)
        userToDelete = input("User to Delete: ")
        contacts.pop(userToDelete)
    elif funcSelected == 4:
        print("--- Search Contact ---")
        searchContact = input("Contact Name: ")
        if searchContact in contacts:
            print(f"The contact {searchContact} exists")
        else:
            print(f"The contact {searchContact} dosen't exist")
    else:
        print("The number is not an option allowed")
    # Consultamos si desea seguir realizando operaciones
    wishContinue = input("Another operation (yes/no)?: ")
    if wishContinue == "no":
        print("Program Ended")
        print(contacts)
        break
    else:
        continue
