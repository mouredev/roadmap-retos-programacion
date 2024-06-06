# LISTS

# Crear listas
myList = [1, 2, 3, 4, 5]
combinedList = ['Hello', 1, 2, True]

# Acceder a listas
print(myList[0])
print(myList[-1]) # Acceder al ultimo elemento

# Modificar valores de una lista
myList[3] = 'New'
print(myList)

# Eliminar elementos de una lista
del myList[2]
print(myList)


# SETS
mySet = set([2, 2, 1, 6, 4, 3, 3, 5, 6])
print(mySet)

otherSet = {4, 6, 5, 2, 1, 3}
print(otherSet)

# Agregar elementos a un set
mySet.add(8)

# Eliminar elementos de un set
mySet.remove(3)
mySet.pop() # Elimina un elemento aleatoreo

# Vaciar un set
mySet.clear()

# Unit sets
firstSet = {1, 3, 5}
secoundSet = {2, 4, 6}
print(firstSet.union(secoundSet))



# TUPLA
myTupla = (1, 2, 3, 3, 4)
print(myTupla)

# Contar la cantidad de veces que un elemento se encuentra en la tupla
print(myTupla.count(3))

# Devolver el indice del objeto
print(myTupla.index(4))


# DICCIONARIO
myDiccionario = dict([
      ('Nombre', 'Andres'),
      ('Edad', 26),
      ('Lenguaje', 'Python'),
])
otherDiccionario = dict([
      ('Nombre', 'Edith'),
      ('Edad', 26),
      ('Lenguaje', 'JavScript'),
])
print(myDiccionario)

# Acceder a valores
print(myDiccionario.get('Nombre'))

# Devolver una lista de llaves y valores
print(myDiccionario.items())

# Devolver una lista de llaves
print(myDiccionario.keys())

# Devolver una lista de valores
print(myDiccionario.values())

# Vaciar diccionario
myDiccionario.clear()

def agenda():
  
  myAgenda = {}

  def addNewContact(name):
    phone = input("Ingresar numero de telefono: ")
    if len(phone) > 0 and len(phone) <= 11:
      myAgenda[name] = phone
    else:
      print('El numero no debe ser mayor a 11 caracteres.')

  def searchContactByName(name):
    if name in myAgenda:
      print(name, myAgenda[name])
    else:
      print('No existe un contacto con el nombre {name}')

  def listAllContacts():
    for name in myAgenda:
      print(name, '->', myAgenda[name])

  def deleteContact(name):
    del myAgenda[name]
    

  while True:
    print(
      """
            AGENDA:
            1. Agregar contacto
            2. Buscar contacto
            3. Actualizar contacto
            4. Eliminar contacto
            5. Lista de contactos
            6. Salir
      """
    )
    option = input('\nEscoger del menu: ')

    match option:
      case "1":
        print('Agregar contacto')
        name = input('Introduzca el nombre del contacto: ')
        addNewContact(name)
      case "2":
        print('Buscar contacto')
        name = input('Introduzca el nombre del contacto a buscar: ')
        searchContactByName(name)
      case "3":
        print('Actualizar contacto')
        name = input('Introduzca el nombre del contacto a actualizar: ')
        if name in myAgenda:
          addNewContact(name)
        else:
          print('No existe un contacto con el nombre {name}')
      case "4":
        print('Eliminar contacto')
        name = input('Introduzca el nombre del contacto a eliminar: ')
        if name in myAgenda:
          deleteContact(name)
        else:
          print('No existe un contacto con el nombre {name}')
      case "5":
        print('Lista de contactos')
        listAllContacts()
      case "6":
        print('Saliendo...')
        break
      case _:
        print('Opcion no valida. Intentar de nuevo.')
    

agenda()