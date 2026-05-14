
lista = list()
lista = [2 ,5 ,3 ,4, 1]
lista.append(6) #añade al final
lista.remove(6)
print(lista[2])
lista[2] = 8
print(lista)
lista.sort()
print(lista)

tupla = tuple()
tupla = (2, 5, 3, 4, 1)
print(tupla[2])
print(tupla)
tupla = tuple(sorted(tupla))
print(tupla)

mi_set = set()
mi_set = {2, 5, 3, 4, 1}
mi_set.add(6)
print(mi_set)
mi_set.remove(6)
print(mi_set)

diccionario = {}
diccionario = {
    "numero1": 3, 
    "numero2": 5, 
    "numero3": 1, 
    "numero4": 2
    }

print(diccionario)
diccionario["numero5"] = 4

diccionario["numero2"] = 8
print(diccionario)
print(diccionario["numero1"])

del(diccionario["numero3"])
print(diccionario)

diccionario = dict(sorted(diccionario.items()))
print(diccionario)


 # DIFICULTAD EXTRA (opcional):

contactos = {}
def validar_telefono(telefono):
    if telefono.isdigit() == False:
        print("El telefono es incorrecto")
        return False
    elif len(telefono) != 11:
        print("el telefono debe contener 11 numeros")
        return False
    else:
        return True

def insertar():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el telefono: ")
    if validar_telefono(telefono) == True:
        contactos[nombre] = telefono
    print(contactos)

def buscar():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in contactos:
        print(f"El telefono del contacto {nombre} es: {contactos[nombre]}")
    else:
        print("El contacto no se encuentra")


def actualizar():
    nombre = input("Ingrese el nombre del contacto a Actualizar: ")
    if nombre in contactos:
        telefono = input("Ingrese el telefono a actualizar: ")
        if validar_telefono(telefono) == True:
            contactos[nombre] = telefono
        print("El telefono del contacto se ha actualizado")
    else:
        print("El contacto no se encuentra")

def eliminar():
    nombre = input("Ingrese el nombre del contacto a Eliminar: ")
    if nombre in contactos:
        del(contactos[nombre])
        print("El contacto se ha eliminado")
    else:
        print("El contacto no se encuentra")


def menu():
    while True:
        opcion = input("""Ingrese la operacion deseada
                       I:Insertar
                       B:Buscar
                       A:Actualizar
                       E:Eliminar
                       S:Salir\n""")
        if opcion == "I":
            insertar()
        elif opcion == "B":
            buscar()
        elif opcion == "A":
            actualizar()
        elif opcion == "E":
            eliminar()
        elif opcion == "S":
            break
        else:
            print("la opcion es incorrecta, selecciones una de la lista")

menu()