"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 
"""

# Creación de estructuras de datos

# Listas

listaNumeros = [1, 2, 3, 4, 5] # Lista de números
print(listaNumeros)

listaString = ["a", "b", "c", "d", "e"] # Lista de strings
print(listaString)

listaMixta = [1, "a", 2, "b", 3, "c"] # Lista mixta
print(listaMixta)

# Tuplas

tuplaNumeros = (1, 2, 3, 4, 5) # Tupla de números
print(tuplaNumeros)

tuplaString = ("a", "b", "c", "d", "e") # Tupla de strings
print(tuplaString)

tuplaMixta = (1, "a", 2, "b", 3, "c") # Tupla mixta
print(tuplaMixta)

# Diccionarios

diccionarioNumeros = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco"} # Diccionario de números
print(diccionarioNumeros)

diccionarioString = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5} # Diccionario de strings
print(diccionarioString)

diccionarioMixto = {1: "a", "b": 2, 3: "c", "d": 4, "e": 5} # Diccionario mixto
print(diccionarioMixto)

#buscar en diccionario
print(diccionarioNumeros[1])

#insertar en diccionario
diccionarioNumeros[6] = "seis"
print(diccionarioNumeros)

#actualizar en diccionario
diccionarioNumeros[6] = "SEIS"
print(diccionarioNumeros)

#eliminar en diccionario
del diccionarioNumeros[6]
print(diccionarioNumeros)


# Operaciones de inserción, borrado, actualización y ordenación

# Listas

listaNumeros.append(6) # Insertar un elemento al final de la lista
print(listaNumeros)

listaNumeros.insert(0, 0) # Insertar un elemento en una posición específica de la lista
print(listaNumeros)

listaNumeros.pop() # Eliminar el último elemento de la lista
print(listaNumeros)

listaNumeros.pop(0) # Eliminar un elemento en una posición específica de la lista
print(listaNumeros)

listaNumeros[0] = 1 # Actualizar un elemento en una posición específica de la lista
print(listaNumeros)

listaNumeros.sort() # Ordenar la lista
print(listaNumeros)

# Tuplas

# Las tuplas son inmutables, por lo que no se pueden modificar

# Diccionarios

diccionarioNumeros[6] = "seis" # Insertar un elemento en el diccionario
print(diccionarioNumeros)

diccionarioNumeros[6] = "SEIS" # Actualizar un elemento en el diccionario
print(diccionarioNumeros)

del diccionarioNumeros[6] # Eliminar un elemento en el diccionario
print(diccionarioNumeros)

"""
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.

"""

# Agenda de contactos

agenda = {} # Diccionario vacío

control = True

opcion = 0

# Funciones de la agenda de contactos 
      
# Buscar contacto      
def buscarContacto():
  nombre = input("Introduzca el nombre del contacto: ").upper()
  if nombre in agenda:
    print("El número de teléfono de", nombre, "es", agenda[nombre])
  else:
    print("El contacto", nombre, "no existe")

# Insertar contacto
def insertarContacto():
  nombre = input("Introduzca el nombre del contacto: ").upper()
  if nombre in agenda:
    print("El contacto", nombre, "ya existe")
  else:
    numero = input("Introduzca el número de teléfono del contacto: ")
    if numero.isnumeric() and len(numero) > 11:
      agenda[nombre] = numero
      print("El contacto", nombre, "ha sido añadido")
    else:
      print("El número de teléfono introducido no es válido")

# Actualizar contacto
def actualizarContacto():
  nombre = input("Introduzca el nombre del contacto: ").upper()
  if nombre in agenda:
    numero = input("Introduzca el nuevo número de teléfono del contacto con el indicador del pais: ")
    if numero.isnumeric() and len(numero) > 11:
      agenda[nombre] = numero
      print("El contacto", nombre, "ha sido actualizado")
    else:
      print("El número de teléfono introducido no es válido")
  else:
    print("El contacto", nombre, "no existe")

# Eliminar contacto
def eliminarContacto():
  nombre = input("Introduzca el nombre del contacto: ").upper()
  if nombre in agenda:
    del agenda[nombre]
    print("El contacto", nombre, "ha sido eliminado")
  else:
    print("El contacto", nombre, "no existe")

# Mostrar agenda
def mostrarAgenda():
  print("Agenda de contactos")
  for nombre, numero in agenda.items():
    print(nombre, ":", numero)

# Salir
def salir():
  global control
  control = False
  print("Fin del programa")

# Ejecución de la agenda de contactos
while control:
  print("----------------------------------------")
  print("Agenda de contactos")
  print("----------------------------------------")
  print("1. Buscar contacto")
  print("2. Insertar contacto")
  print("3. Actualizar contacto")
  print("4. Eliminar contacto")
  print("5. Mostrar agenda")
  print("6. Salir")
  print("----------------------------------------")
  opcion = int(input("¿Qué operación desea realizar? "))
  print("----------------------------------------")
  
  if opcion == 1:
    buscarContacto()
  elif opcion == 2:
    insertarContacto()
  elif opcion == 3:
    actualizarContacto()
  elif opcion == 4:
    eliminarContacto()
  elif opcion == 5:
    mostrarAgenda()
  elif opcion == 6:
    salir()
  else:
    print("Opción incorrecta")



  






















