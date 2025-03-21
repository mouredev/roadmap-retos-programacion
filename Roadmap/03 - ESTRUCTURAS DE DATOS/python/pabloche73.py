# Estructuras de datos

# Listas

mi_lista = [1,2,2,3,4,2,5]
print(type(mi_lista))
print(mi_lista)
print(mi_lista.count(2)) # Cuenta cantidad de ocurrencias del valor que le pasemos
mi_lista.append(11) # Agrega e imprime al final de la lista el valor que le pasemos
print(mi_lista)
mi_lista.insert(0,0) # Agrega en el indice 0 el valor 0
print(mi_lista)
valor_eliminado =mi_lista.pop() #Elimina y devuelve por defecto el ultimo elemento de la lista
print(mi_lista)
print(f"Se elimino el {valor_eliminado}")
mi_lista.sort() # Ordena la lista de menor a mayor por defecto
mi_lista.remove(2) # Elimina la primer ocurrencia de un valor en la lista
mi_lista[2] = 32 # Actualiza el valor del indice 2 a 32
print(mi_lista)

# Tuplas

mi_tupla = (1,2,3,4,5,4,1)
print(mi_tupla)
lista = list(mi_tupla) # Para modificar una tupla primero debemos convertira en lista
print(lista)
lista.pop()
lista.append(8)
lista[0]=10
lista.insert(3,7)
lista.sort()
mi_tupla = tuple(lista) # Una vez realizadas las modificaciones convertimos la lista en tupla
print(mi_tupla)

# Sets

mi_set = {1,2,3,4} # Las tuplas no pueden repetir valores
print(mi_set)
mi_set.add(1) # Al intentar agregar un valor existente no da error pero no se agrega
print(mi_set)
mi_set.clear() # Elimina todo el contenido del set
print(mi_set)
mi_set.add(1) # Agrega un valor al Set
print(mi_set)
mi_set.add(2) # Agrega otro a continuacion
print(mi_set)
mi_set.remove(1) # Elimina el elemento cuyo valor es 1
print(mi_set)

"""
Para ordenar un Set se procede como hicimos para ordenar una tupla, pasamos el set a lista, ordenamos y volvemos a convertir la lista a set
"""

# Diccionarios

mi_dic = {
    "Nombre": "Pablo",
    "Edad": 51,
    "Pais": "Argentina"
}

print(mi_dic)
mi_dic["Nombre"] = "Alberto" # Actualiza un valor accediendo por su clave
print(mi_dic)
mi_dic["Ciudad"] = "Madrid" # Agrega una nueva clave y le da un valor
print(mi_dic)
valor_elim = mi_dic.pop("Ciudad") # Elimina la clave Ciudad y almacena el valor en una clave
print(mi_dic)
print(f"Valor eliminado: {valor_elim}")

# Extra! Extra! Agenda telefónica

mi_agenda = {} # Este diccionario va a usar los nombres como clave

def verificar_telefono(phone): # Verifica que el telefono ingresado sea digito y tenga mas de 8 caracteres
    es_digito = phone.isdigit()
    long_valida = len(phone) > 8
    return es_digito and long_valida

def contacto_existente(name): # Verifica que el contacto ingresado exista
    existe = name in mi_agenda
    return existe 

def agregar_contacto(new_contact):
    if contacto_existente(new_contact):
        print("*********  El contacto ya existe  ***********")
    else:
        b=True
        while b:
            telefono = input("Telefono: ")
            if verificar_telefono(telefono):
                mi_agenda[new_contact]=telefono
                print("******  Contacto agregado con éxito  *******")
                b=False
            else:
                print("***********  Telefono no válido  ***********")
          

def eliminar_contacto(del_contact):
    if contacto_existente(del_contact):
        del mi_agenda[del_contact]
        print("*************  Eliminado  *************")    
    else:
        print("*******  El contacto no existe  ********")

def buscar_contacto(search_contact):
    if contacto_existente(search_contact):
        print (f"Encontrado, {search_contact}, Tel: {mi_agenda[search_contact]}")
    else:
        print("*******  El contacto no existe  ********")

def modificar_contacto(mod_contact):

    if contacto_existente(mod_contact):
        print (f"Encontrado, {mod_contact}, Tel: {mi_agenda[mod_contact]}")  
        b=True
        while b:
            mod_phone = input("Ingrese nuevo telefono: ")
            if verificar_telefono(mod_phone):
                mi_agenda[mod_contact]=mod_phone
                print("************  Actualizado **************")
                b=False
            else:
                print("***********  Telefono no válido  ***********")
    else:
        print("*******  El contacto no existe  ********")

def mostrar_todos():
    if len(mi_agenda) > 0:
        print(mi_agenda)
    else:
        print("********** No hay contactos ************")
    
inicio = True

while inicio:
    print()
    print()
    print()
    print("A   G   E   N   D   A")

    print("1.Agregar contacto")
    print("2.Eliminar contacto")
    print("3.Buscar contacto")
    print("4.Modificar telefono de contacto")
    print("5.Mostrar todos los contactos")
    print("6.Salir")
    print()
    opcion = input("¿Qué desea hacer?: ")
    print("________________________________")
    print()

    match opcion:
        case "1":           
            nombre=input("Nombre a agregar: ")
            agregar_contacto(nombre)
        case "2":
            nombre=input("Nombre a eliminar: ")
            eliminar_contacto(nombre)
        case "3":
            nombre=input("Nombre a buscar: ")
            buscar_contacto(nombre)
        case "4":
            nombre=input("Nombre a buscar: ")
            modificar_contacto(nombre)
        case "5":
            mostrar_todos()
        case "6":
            inicio=False














      




