"""* EJERCICIO:
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
import re

# Tuplas - Son inmutables, se pueden iterar
print("TUPLAS")
tupla = (1, 2, 3, 4, 1)
# tupla = tuple([1, 2, 3])
print(type(tupla))
print(tupla)

# Iterar tuplas
print("ITERAR TUPLAS")
for dato in tupla:
    print(dato)

print(len(tupla))  # Muestra la cantidad de elementos

# Metodos tuplas
print("METODOS TUPLAS")
print(tupla.count(1))  # cuenta los elementos que son 1
print(tupla.index(4))  # imprime el el indice del valor 4

# Listas - Son mutables, se pueden iterar
print("LISTAS")
lista = [1, 2, 3, 4]
# lista = list("123")
print(type(lista))
print(lista)

a, b, c, d = lista
print(f"{a} - {b} - {c} - {d}")

# Iterar listas
print("ITERAR LISTAS")
for dato in lista:
    print(dato)

print(len(lista))  # Muestra la cantidad de elementos

# Metodos
print("METODOS LISTAS")
lista.remove(3)  # Remueve el elemento 3
print(lista)

lista.extend([5, 6])  # Se extiende la lsita con uno o varios elementos
print(lista)

lista.append(7)  # Se agrega un valor al final de la lista
print(lista)

lista.insert(2, 3)  # Se inserta un 3 en la posicion 2
print(lista)

lista.pop()  # Se elimina el ultimo valor
print(lista)

lista.reverse()  # La oredena en sentido inverso
print(lista)

lista.sort()  # La ordena de menor a mayor
print(lista)

print(
    lista[3]
)  # Imprime el valor de la lista en la posicion 3 (comienza a contar desde 0)

print(lista.index(4))  # Imprime la posicion del elemento 4

# Set - Son inmutables, se pueden iterar, no permite datos repetidos y desordenados
print("SETS")
s = set([2, 1, 4, 2, 3, 1])
print(type(s))
print(s)

# Iterar sets
print("ITERAR SETS")
for dato in s:
    print(dato)

print(len(s))  # Muestra la cantidad de elementos

print("METODOS DE SETS")
s.add(5)  # Agrega el valor 5
print(s)

s.remove(3)  # Remueve el valor 3
print(s)

s.pop()  # Remueve un valor al azar
print(s)

s.clear()  # Vacia el set
print(s)

# Diccionarios - Son mutables, se pueden iterar
print("DICCIONARIOS")
diccionario = {"Juan": "juan@mail.com", "Maria": "maria@mail.com"}
# diccionario = dict([("Juan", "juan@mail.com"), ("Maria", "maria@mail.com")])
print(type(diccionario))
print(diccionario)

print("ITERAR DICCIONARIOS")
for x, y in diccionario.items():
    print(f"clave: {x}, valor: {y}")

print("METODOS DE DICCIONARIOS")
print(
    diccionario.get("Juan", "No existe")
)  # Muestra el valor para la clave, si no existe muestra el segundo parametro

print(diccionario.items())  # Muestra todos los items del diccionario

print(diccionario.keys())  # Muestra todos los keys del diccionario

print(diccionario.values())  # Muestra todos los valores del diccionario

diccionario.pop("Juan")  # Elimina el item con esa key
print(diccionario)

d = {"Jose": "jose@mail.com"}
diccionario.update(d)  # Agrega un item o si existe lo modifica
print(diccionario)

diccionario.clear()  # Vacia el diccionario
print(diccionario)

"""
DIFICULTAD EXTRA
"""


# Funcion de menu de opciones
def menu():
    opciones = "1234"
    print("\nBIENVENIDO A LA AGENDA:")
    print("1 - Dar de alta")
    print("2 - Dar de baja")
    print("3 - Consultar")
    print("4 - Modificar")
    print("\n0 - Salir\n")
    global seleccion
    global decision
    seleccion = input("seleccione una opcion: ")
    if seleccion in opciones:
        decision = True
    else:
        decision = False


# Funcion para dar de alta
def alta(posicion: dict, contador: int):
    patron = "^\d{13}$"
    name = input("Ingrese el nombre: ")
    phone = input("Ingrese el telefono (debe tener 13 digitos): ")
    if re.match(patron, phone):
        prov = {str(contador): [name, phone]}
        posicion.update(prov)
        contador += 1
    else:
        print("El telefono ingresado es incorrecto")
        print("Debe tener 13 digitos")
        alta(posicion, contador)
    return posicion, contador


# Funcion para dar de baja
def baja(posicion: dict):
    mostrar(posicion)

    x = input("\nIngrese que ID quiere dar de baja: ")
    if posicion.get(x, "no") == "no":
        print("El item no existe")
        return baja(posicion)
    posicion.pop(x)

    return posicion


# Funcion de consulta
def consulta(posicion: dict):
    mostrar(posicion)
    x = input("\nPresione una tecla para continuar")
    if x != "":
        return


# Funcion para modificar
def modificar(posicion: dict):
    mostrar(posicion)

    x = input("\nIngrese que ID quiere modificar: ")
    if posicion.get(x, "no") == "no":
        print("El item no existe")
        return modificar(posicion)

    name = input("Ingrese el nombre a modificar: ")
    phone = input("Ingrese el telefono a modificar: ")
    prov = {str(x): [name, phone]}
    posicion.update(prov)

    return posicion


# Funcion para mostrar la agenda
def mostrar(posicion: dict):
    print("-" * 43)
    print(f'{"ID":4} {"NOMBRE":25} {"TELEFONO":17}')

    for i in posicion:
        print(f"{i:4} {posicion[i][0]:25} {posicion[i][1]:12}")
    print("-" * 43)


# Inicia mostrando un menu de opciones
posicion = {}
contador = 0

menu()
while decision:
    if seleccion == "1":
        posicion, contador = alta(posicion, contador)
        menu()
    elif seleccion == "2":
        posicion = baja(posicion)
        menu()
    elif seleccion == "3":
        consulta(posicion)
        menu()
    elif seleccion == "4":
        posicion = modificar(posicion)
        menu()

print("Ha salido de la agenda!!")
