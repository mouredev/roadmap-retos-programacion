# LISTAS EN PYTHON

# formas de declarar una lista  
from unittest import case


Lista_vacia =  list() # nueva lista
Lista_vacia2 = [] # nueva lista

Lista_numeros = [1, 2, 3, 4, 5] # lista de numeros
lista_nombres = ["Juan", "Pedro", "Maria", "Ana", "Luis"] # lista de nombres

print("Lista vacia:", Lista_vacia, "El largo de la lista es:",len(Lista_vacia))
print("Lista vacia2:", Lista_vacia2, "El largo de la lista es:",len(Lista_vacia2))
print("Lista numeros:", Lista_numeros, "El largo de la lista es:",len(Lista_numeros))
print("lista nombres:", lista_nombres, "El largo de la lista es:",len(lista_nombres))

Lista_diferentes = [1, "Juan", 3.14, True] # lista de diferentes tipos de datos
print("Lista diferentes tipos de datos:", Lista_diferentes, "El largo de la lista es:",len(Lista_diferentes))

#imprimir un elemento de la lista
print("segundo elemento de la lista nombres:", lista_nombres[1])


#imprimir un elemento de la lista de atras a adelante
print("ultimo elemento de la lista nombres:",    lista_nombres[-1])

#desempaquetar una lista
a, b, *c = lista_nombres
print("desempaquetar una lista:", a, b, c)

nueva_lista_nombres = lista_nombres[1:3] # crear una nueva lista a partir de otra lista
print("lista nombres inicial:", lista_nombres, "El largo de la lista es:",len(lista_nombres))
print("nueva lista nombres:", nueva_lista_nombres, "El largo de la lista es:",len(nueva_lista_nombres))


print("lista nombres inicial:", lista_nombres)
lista_nombres[0] = "Carlos" # cambiar un elemento de la lista
print("lista nombres modificando el primero nombre:", lista_nombres)

#Varias existencias de un elemento en una lista
print("Carlos esta en la lista:", "Carlos" in lista_nombres)
print("Gaby esta en la lista:", "Gaby" in lista_nombres)

#Agregar un elemento a la lista
lista_nombres.append("Gaby") # agregar un elemento al final de la lista
print("lista nombres despues de agregar Gaby:", lista_nombres)

#incertar un elemento en una posicion especifica
lista_nombres.insert(1, "Luis") # agregar un elemento en la posicion 1
print("lista nombres despues de insertar Luis:", lista_nombres)

#Eliminar un elemento de la lista usando remove
lista_nombres.remove("Luis") # eliminar un elemento de la lista     
print("lista nombres despues de eliminar Luis:", lista_nombres)

#eliminar un elemento de la lista usando pop
print("lista nombres andes del pop:", lista_nombres)
lista_nombres.pop(1) # eliminar un elemento de la lista en la posicion 1    
print("lista nombres despues de eliminar el elemento en la posicion 1:", lista_nombres)

#elimar elemento de la lista usando del
print("lista nombres andes del del:", lista_nombres)
del lista_nombres[1] # eliminar un elemento de la lista en la posicion 1
print("lista nombres despues de eliminar el elemento en la posicion 1 usando del:", lista_nombres)

#clear una lista
print("lista nombres andes del clear:", lista_nombres)
 # eliminar todos los elementos de la lista
print("lista nombres despues del clear:", lista_nombres.clear())

lista_nombres = ["Juan", "Pedro", "Maria", "Ana", "Luis", "Gaby", "Juan"] # lista de nombres
print("lista nombres inicial:", lista_nombres)

 #unir dos listas
lista_nombres2 = ["Gaby", "Carlos", "Luis"] # lista de nombres
lista_unida = lista_nombres + lista_nombres2 # unir dos listas
print("lista nombres 1:", lista_nombres)    
print("lista nombres 2:", lista_nombres2)
print("lista unida:", lista_unida)

#contar elementos de una lista
print("lista nombres:", lista_nombres)
print("cantidad de veces que aparece Juan en la lista nombres:", lista_nombres.count("Juan")) # contar cuantas veces aparece un elemento en la lista

#encontrar la posicion de un elemento en la lista
print("lista nombres:", lista_nombres)
print("posicion de Juan en la lista nombres:", lista_nombres.index("Juan")) # encontrar la posicion de un elemento en la lista

#cambiar el orden de los elementos de la lista de atras a adelante
print("lista nombres:", lista_nombres)
lista_nombres.reverse()
print("lista nombres despues de cambiar el orden de los elementos:", lista_nombres) # cambiar el orden de los elementos de la lista

#ordenar los elementos de la lista
print("lista nombres:", lista_nombres)
lista_nombres.sort() # ordenar los elementos de la lista
print("lista nombres despues de ordenar los elementos:", lista_nombres) # ordenar los elementos de la lista
lista_nombres.sort(reverse=True) # ordenar los elementos de la lista de atras a adelante
print("lista nombres ordenada de atras a adelante:", lista_nombres) # ordenar los elementos de la lista de atras a adelante

#TUPLAS EN PYTHON

tupla_vacia = tuple() # nueva tupla
tupla_vacia2 = () # nueva tupla

tupla_numeros = (1, 2, 3, 4, 5) # tupla de numeros
tupla_nombres = ("Juan", "Pedro", "Maria", "Ana", "Luis") # tupla de nombres
tupla_diferentes = (1, "Juan", 3.14, True) # tupla de diferentes tipos de datos

print("tupla vacia:", tupla_vacia)
print("tupla vacia2:", tupla_vacia2)
print("tupla numeros:", tupla_numeros)
print("tupla nombres:", tupla_nombres)
print("tupla diferentes tipos de datos:", tupla_diferentes)
print("segundo elemento de la tupla nombres:", tupla_nombres[1]) # imprimir un elemento de la tupla

tupla_nombres2 = tupla_nombres[1:3] # crear una nueva tupla a partir de otra tupla
print("tupla nombres inicial:", tupla_nombres)
print("nueva tupla nombres:", tupla_nombres2)
lista_tupla_nombres = list(tupla_nombres) # convertir una tupla en una lista
print("lista nombres a partir de la tupla nombres:", lista_tupla_nombres)
lista_tupla_nombres.append("Gaby") # agregar un elemento a la lista
print("lista nombres despues de agregar Gaby:", lista_tupla_nombres)
tupla_lista_tupla_nombres = tuple(lista_tupla_nombres) # convertir la lista en una tupla
print("tupla nombres modificada:", tupla_lista_tupla_nombres) # convertir la lista en una tupla
print("Gaby esta en la tupla:", "Gaby" in tupla_lista_tupla_nombres) # verificar si un elemento esta en la tupla
#Unir dos tuplas
tupla_nombres3 = ("Gaby", "Carlos", "Luis") # tupla de nombres
tupla_unida = tupla_nombres + tupla_nombres3 # unir dos tuplas
print("tupla nombres:", tupla_nombres)
print("tupla nombres 3:", tupla_nombres3)
print("tupla unida:", tupla_unida)
del tupla_nombres # eliminar una tupla

#SETS EN PYTHON

Set_vacio = set() # nuevo set
Set_vacio2 = {} # nuevo set

set_numeros = {1, 2, 3, 4, 5} # set de numeros
set_nombres = {"Juan", "Pedro", "Maria", "Ana", "Luis"} # set de nombres
set_diferentes = {1, "Juan", 3.14, True} # set de diferentes tipos de datos
print("Set vacio:", Set_vacio)
print("Set vacio2:", Set_vacio2)
print("Set numeros:", set_numeros)
print("Set nombres:", set_nombres)
print("Set diferentes tipos de datos:", set_diferentes)

print("Juan esta en el set nombres:", "Juan" in set_nombres) # verificar si un elemento esta en el set

set_nombres.add("Gaby") # agregar un elemento al set
print("set nombres despues de agregar Gaby:", set_nombres)

set_nombres.remove("Gaby") # eliminar un elemento del set
print("set nombres despues de eliminar Gaby:", set_nombres)

set_nombres.discard("Gaby") # eliminar un elemento del set sin generar error si no existe
print("set nombres despues de eliminar Gaby sin generar error si no existe:", set_nombres)

set_nombres.update({"Gaby", "Carlos", "Luis"}) # agregar varios elementos al set
print("set nombres despues de agregar varios elementos:", set_nombres)

print("set nombres:", set_nombres.clear()) # eliminar todos los elementos del set

#Unidos dos sets
set_nombres2 = {"Gaby", "Carlos", "Luis"} # set de nombres
set_unido = set_nombres.union(set_nombres2) # unir dos sets
print("set nombres:", set_nombres)
print("set nombres2:", set_nombres2)
print("set unido:", set_unido)

#DICCIONARIOS EN PYTHON

diccionario_vacio = dict() # nuevo diccionario
diccionario_vacio2 = {} # nuevo diccionario

diccionario_numeros = {"key01": "uno", "key02": "dos", "key03": "tres", "key04": "cuatro", "key05": "cinco"} # diccionario de numeros
diccionario_nombres = {"Juan": 25, "Pedro": 30, "Maria": 28, "Ana": 22, "Luis": 35} # diccionario de nombres
diccionario_diferentes = {1: "uno", "Juan": 25, 3.14: "pi", True: "verdadero"} # diccionario de diferentes tipos de datos
print("diccionario vacio:", diccionario_vacio)
print("diccionario vacio2:", diccionario_vacio2)
print("diccionario numeros:", diccionario_numeros)
print("diccionario nombres:", diccionario_nombres)
print("diccionario diferentes tipos de datos:", diccionario_diferentes)
print(diccionario_numeros["key03"]) # imprimir un elemento del diccionario
print(diccionario_diferentes[3.14]) # imprimir un elemento del diccionario

print(diccionario_diferentes.get("Juan")) # imprimir un elemento del diccionario
diccionario_diferentes["Juan"] = 26 # cambiar un elemento del diccionario
print(diccionario_diferentes) # imprimir el diccionario de diferentes tipos de datos
diccionario_diferentes["Gaby"] = 20 # agregar un elemento al diccionario
print(diccionario_diferentes) # imprimir el diccionario de diferentes tipos de datos
print("Gaby" in diccionario_diferentes) # verificar si un elemento esta en el diccionario
diccionario_diferentes.pop("Gaby") # eliminar un elemento del diccionario
print(diccionario_diferentes) # imprimir el diccionario de diferentes tipos de datos

def agenda():
    agenda = {}

    while True:
        print("\nAgenda de Contactos")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            
            case "1":
                nombre = input("Ingrese el nombre del contacto a buscar: ")
                if nombre in agenda:
                    print(f"Teléfono de {nombre}: {agenda[nombre]}")
                else:
                    print(f"Contacto {nombre} no encontrado.")
            
            case "2":
                nombre = input("Ingrese el nombre del contacto: ")
                telefono = input("Ingrese el teléfono del contacto: ")
                if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
                    agenda[nombre] = telefono
                    print(f"Contacto {nombre} agregado con el teléfono {telefono}.")
                else:
                    print("El número de teléfono no es válido.")

            case "3":
                nombre = input("Ingrese el nombre del contacto a actualizar: ")
                if nombre in agenda:
                    telefono = input("Ingrese el nuevo teléfono del contacto: ")
                    agenda[nombre] = telefono
                    print(f"Contacto {nombre} actualizado con el teléfono {telefono}.")
                else:
                    print(f"Contacto {nombre} no encontrado.")

            case "4":
                nombre = input("Ingrese el nombre del contacto a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                    print(f"Contacto {nombre} eliminado.")
                else:
                    print(f"Contacto {nombre} no encontrado.")

            case "5":   
                if len(agenda) > 0:
                    print("Contactos en la agenda:")
                    for nombre, telefono in agenda.items():
                        print(f"{nombre}: {telefono}")
                else:
                    print("La agenda está vacía.")

            case "6":
                print("Saliendo de la agenda.")
                break

            case _:
                print("Opción no válida. Intente nuevamente.")

agenda()  # Llamada a la función para iniciar la agenda
