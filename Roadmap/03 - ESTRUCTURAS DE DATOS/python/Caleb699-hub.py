"""listas"""

lista = ["hola","Caleb","21","python", True, False]
print(lista)

#añadir elementos

#al final de la lista
lista.append("maracuya")

#en el índice que de indica
lista.insert(1,False)

#agrega una los elementos de una lista al final
lista.extend(["perro","gato"])


#eliminar elementos

#elimina el elemento indicado
lista.remove("maracuya")

#elimina el elemento de indice indicado
lista.pop(1)

#elimina la lista
lista.clear()

print(lista)



"""TUPLAS"""


tupla = ("hola","Caleb","21","python", True)


#buscar


#por indice
print(tupla[1])

#verifica su existencia en la tupla
v = "hola" in tupla
print(v)



"""CONJUNTOS"""

conjunto = {1,2,3,4,5}

#agregar elemento
conjunto.add(6)

#elimina elemento
conjunto.remove(1)

#operaciones con conjuntos
a = {1,2,3}
b = {3,4,5}
print(a | b) #union
print(a & b) #intersección
print(a - b) #diferencia




"""DICCIONARIOS"""


diccionario = {"Nombre": "Caleb", "Edad": 21, "Pais": "Colombia"}

#agregar elemento
diccionario["lenguaje_de_programacion"] = "Python"

#eliminar elemento
del diccionario["Pais"]

print(diccionario)


"""
DIFICULTAD EXTRA
"""

agenda_contactos = {}

def agregar_contacto():
    nombre_contacto = input("Nombre de contacto: ")
    numero_telefono = input("Numero de contacto: ")
    agenda_contactos[nombre_contacto] = numero_telefono
    print("Su contacto ha sido agregado")

def buscar_contacto():
    nombre_contacto = input("Introduzca el nombre de contacto: ")
    if nombre_contacto in agenda_contactos:
        print(f"{nombre_contacto} = {agenda_contactos[nombre_contacto]}")
    else:
        print("Contacto no encontrado")

def acualizar_contacto():
    nombre_contacto = input("Introduzca el nombre del contacto que va a actualizar: ")
    if nombre_contacto in agenda_contactos:
        numero_nuevo = input("Introduzca el nuevo número de teléfono: ")
        agenda_contactos[nombre_contacto] = numero_nuevo
        print("Contacto actualizado")
    else:
        print("Contacto no encontrado")

def eliminar_contacto():
    nombre_contacto = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre_contacto in agenda_contactos:
        del agenda_contactos[nombre_contacto]
        print("El contacto ha sido elinminado")
    else:
        print("Contacto no encontrado")

def lista_contactos():
    if len(agenda_contactos)==0:
        print("La agenda está vacía")
    else:
        for nombre_contacto,numero_telefono in agenda_contactos.items():
            print(f"{nombre_contacto}: {numero_telefono}")

def mostrar_menu():
    print("MENÚ DE AGENDA DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Lista de contactos")
    print("6. Salir")


while True:
    mostrar_menu()
    opcion = int(input("Ingrese una opcion del menú: "))

    if opcion == 1:
        agregar_contacto()
    elif opcion == 2:
        buscar_contacto()
    elif opcion == 3:
        acualizar_contacto()
    elif opcion == 4:
        eliminar_contacto()
    elif opcion == 5:
        lista_contactos()
    elif opcion == 6:
        print("Programa finalizado")
        break
    else:
        print("Opción no válida, ingrese un valor del menú")