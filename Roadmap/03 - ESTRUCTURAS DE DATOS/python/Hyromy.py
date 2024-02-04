"""
las listas son arreglos de n cantidad de elementos indeterminados
sus elementos pueden variar y ser mutables (editables)
"""
lista = [55, 1.77, "Hyromy", True]


"""
las tuplas son arreglos de una cantidad de elementos definidos
sus elementos son inmutables (solo de lectura)
"""
tupla = (75, 1.70, "Chino", True)


"""
los diccionarios son un json y ya xd
"""
diccionario = {
    "clave": "valor",
    "key": "value"
}


"""
los conjuntos como unas listas pero sus elementos no son mutables (editables)
sus elementos son mutables pero no puede contener elementos repetidos
"""
conjunto = {"alan", "vale", "julian", "alan"}


#operaciones con listas
#añadir elementos a una lista
lista.append("Luis")
print(lista)

#limpiar una lista entera
lista.clear()
print(lista)

#copiar una lista sin hacer referencia al mismo espacio de memoria
lista = [1, 4.4, True]
lista_2 = lista.copy()
print(lista)
print(lista_2)

#contar elementos en una lista
lista = [1, 2, 5, 1, 7, 1, 5, 9, 1]
print(lista.count(1))

#agregar elementos de una lista a otra
lista = [1, 2, 3]
extension = [4, 5, 6]
lista.extend(extension)
print(lista)

#encontrar el indice de un elemento especificado
lista = [10, 20, 30, 40, 50]
print(lista.index(20))

#insertar un elemento en un indice especifico
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(5, 10)
print(lista)

#eliminar un elemento
lista = [1, 1.2, True, 'Amanda', 'Hyromy']
borrado_1 = lista.pop() #Hyromy
borrado_2 = lista.pop(2) # True
print(lista)
print(borrado_1)
print(borrado_2)

#eliminar la primera aparicion de una lista
lista = [1, 4, 7, 1, 9, 1]
lista.remove(1)
print(lista)

#invertir una lista
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)

#ordenar una lista
lista = [6, 2, 8, 3, 9, 1, 5, 4, 7]
lista.sort()
print(lista)

print("\n")
# ---- DIFICULTAD EXTRA ----

contactos = []

def crear():
    name = input("Nombre del contacto => ")
    phone = input(f"Ingrese numero de {name} => ")
    
    if len(phone) != 10:
        print("Numero ingresado no valido\n\n")
        menu()
    else:
        phone = int(phone)
        contacto = [name, phone]
        contactos.append(contacto)
        print("Contacto registrado con exito\n\n")
        menu()
    
def read():
    name = input("Ingrese el nombre del contacto a buscar => ").lower()
    for i in contactos:
        if i[0].lower().startswith(name):
            print(f"{i[0]}: {i[1]}")
    else:
        print("\n\n")
        menu()
    
def update():
    name = input("Escribe el nombre el contacto que quieras actualizar => ")
    for i in contactos:
        if i[0] == name:
            new_name = input(f"Escribe el nuevo nombre para {i[0]} (Deja en blanco para no modificar) => ")
            if new_name != "":
                i[0] = new_name
                
            new_phone = input(f"Escribe el nuevo numero para {i[0]} (Deja en blanco para no modificar) => ")
            if len(new_phone) != 10:
                print("Numero ingresado no valido\n\n")
            else:
                new_phone = int(new_phone)
                i[1] = new_phone
    else:
        print("\n\n")
        menu()
    
def delete():
    name = input("Escribe el nombre del contacto que quieras borrar => ")
    x = 0
    for i in contactos:
        if name == i[0]:
            confirm = input(f"Estas seguro que quieres borrar a {i[0]}: {i[1]}? (Y) (N) => ")[0:1].lower()
            if confirm == "y":
                print(f"{name} fue eliminado")
                contactos.pop(x)
        x += 1
    else:
        print("\n\n")
        menu()

def menu():
    print("¿Que operacion quieres hacer?")
    print("(B) Buscar")
    print("(I) Insertar")
    print("(A) Actualizar")
    print("(E) Eliminar")
    print("(X) Salir\n")
    option = input("=> ")[0:1].lower()
    
    if option == "b":
        read()
    elif option == "i":
        crear()
    elif option == "a":
        update()
    elif option == "e":
        delete()
    elif option == "x":
        print("")
    else:
        print("Operacion no valida\n\n")
        menu()
menu()