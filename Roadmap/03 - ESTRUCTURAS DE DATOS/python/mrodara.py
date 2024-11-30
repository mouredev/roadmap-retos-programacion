# ESTRUCTURAS DE DATOS EN PYTHON

######## CADENAS DE CARACTERES (Tipo de dato inmutable) #######################

cadena = "Hola que tal"

print('Concatenación: ' + cadena + cadena)

print('Repetición: ' + cadena*3)

print('Indexación: ' + cadena[0] + cadena[1])

print('Longitud de la cadena (len): ' + str(len(cadena)))

# Las cadenas se pueden recorrer

cadena = 'informática'

for caracter in cadena:
  print(caracter, " " ,  end="")
  
'''
Operadores de pertenencia: Se puede comprobar si un elemento (subcadena) pertenece o no 
a una cadena de caracteres con los operadores in y not in.
'''
print('á' in cadena)

print('p' in cadena)

print('p' not in cadena)

"""
Slice (rebanada): Puedo obtener una subcadena de la cadena de caracteres. 
Se indica el carácter inicial, y el carácter final, además podemos indicar opcionalmente un salto. 
Si no se indica el carácter inicial se supone que es desde el primero, sino se indica el carácter final 
se supone que es hasta el final. 
Por último podemos usar salto negativo para empezar a contar desde el final.
"""

cadena = "inteligencia artifical"

print(cadena[2:5])

print(cadena[2:7:2])

print(cadena[:5])

print(cadena[5:])

print(cadena[-1:-3])

print(cadena[::-1])

print(cadena[::-2])

# Podemos convertir cualquier número en una cadena de caracteres utilizando la función str()
num = str(123)

print(type(num))


######## FIN CADENAS DE CARACTERES (Tipo de dato inmutable) #######################

######## LISTAS (Tipo de dato mutable) #######################

my_list = [1,2,3,4,5]

# Las listas pueden almacenar distintos tipos de datos
my_list2 = [1, 'hola', True]

# También se pueden definir listas vacías para luego agregarle elementos
my_list3 = []

# Podemos obtener el valor de una posición concreta de la lista mediante su índice (base-0)
# Esto quiere decir que los elementos de la lista van desde el 0 hasta el nro. de elementos - 1

print(my_list2[1]) # retorna la cadena

# Añadir elementos a una lista (método append) 
my_list3.append(1)
print(my_list3)

new_list = [2,3,4,5]

# Añadir una lista a otra lista
my_list3.extend(new_list)
print(my_list3)

# Añadimos más elementos a la lista de manera automatizada
for i in range(1,5):
    my_list3.append(i * 2)

# Actualizar un dato de la lista
my_list3[0] = 3 * my_list3[0]
print(my_list3)

# La ordenación de una lista se puede realizar mediante la función sorted()

print(sorted(my_list3))

# Importante las variables en python son por referencia luego no podemos asignar un lista a otra para copiarla
my_list4 = my_list3

print(my_list3)

my_list4[0] = 100

print(my_list3)

# Lo correcto es hacer esto

my_list4 = [i for i in my_list3] # List comprenhension

print(my_list3)
print(my_list4)

my_list4[0] = 0

print(my_list3)
print(my_list4)

# También podemos realizar operaciones de pertenencia

print(0 in my_list4)

print(100 in my_list4)

# Recorrido de listas

# Usando bucle for
for i in my_list4:
    print(i, "," ,end="")

# Mediante slice

print(my_list4[0:]) # Imprime toda la lista
print(my_list4[0:3]) # Imprime los elementos desde la posición 0 hasta la 2
print(my_list4[::-1]) # Imprime la lista en orden inverso
print(my_list4[::2]) # Imprime los elementos de la lista de 2 en 2
print(my_list4[1::2]) # Imprime los elementos de la lista de 2 en 2 pero empezando desde la posición 1


# Se pueden repetir listas

my_list5 = my_list4 * 2
print(my_list5)

# Se pueden concatenar listas
my_list6 = my_list4 + my_list5
print(my_list6)

# Se pueden eliminar elementos de una lista
my_list6.pop() # Elimina el último elemento de la lista
print(my_list6)
my_list6.pop(0) # Elimina el primer elemento de la lista
print(my_list6)

# Se pueden eliminar elementos de una lista por su valor
my_list6.remove(0) # Elimina el primer elemento que coincida con el valor
print(my_list6)

# Podemos conocer el número de elementos de una lista
print(len(my_list6))

# Podemos conocer el índice de un elemento en la lista
print(my_list6.index(2))
print(my_list6.index(2, 1)) # Busca el elemento a partir de la
# posición 1

# Podemos contar cuántas veces se repite un elemento en la lista
print(my_list6.count(2))

# Podemos invertir el orden de los elementos de una lista
my_list6.reverse()
print(my_list6)

# Uso de funciones predefinidas sobre elementos de una lista
print(max(my_list6))
print(min(my_list6))
print(sum(my_list6))
print(sum(my_list6)/len(my_list6)) # Promedio de los elementos de la lista

######## FIN DE LISTAS ###########

######## TUPLAS (TIPO DE DATO INMUTABLE) ##################################

# Las tuplas son similares a las listas pero no se pueden modificar una vez creadas
my_tuple = (1,2,3,4,5)
# print(my_tuple[0] = 10) # Esto no se puede hacer porque las tuplas son inmutables
'''
 Las tuplas se pueden recorrer.
 Operadores de pertenencia: in y not in.
 Concatenación: +
 Repetición: *
 Indexación
 Slice

Entre las funciones definidas podemos usar: len, max, min, sum, sorted
'''
######## FIN TUPLAS (TIPO DE DATO INMUTABLE) ##################################

######## DICCIONARIOS (MAPAS) ##################################

# Los diccionarios son una estructura de datos que permite almacenar pares clave-valor
# Las claves deben ser únicas y los valores pueden ser de cualquier tipo

# Creación de un diccionario
my_dict = {'nombre': 'Juan', 'edad': 25, 'cursos': ['Python', 'Java', 'JavaScript']}

my_dict2 = {} # Diccionario vacío

# Acceso a los elementos de un diccionario
print(my_dict['nombre'])
print(my_dict['edad'])

# Modificación de un valor de un diccionario
my_dict['nombre'] = 'Pedro'
print(my_dict['nombre'])

# Añadir un nuevo par clave-valor
my_dict['sexo'] = 'M'
print(my_dict)

# Eliminar un par clave-valor
del my_dict['sexo']
print(my_dict)

# Recorrer un diccionario
# Recorrer las claves

for key in my_dict.keys():
  print(key, end=" ")

# Recorrer los valores
for value in my_dict.values():
  print(value, end="")

# Recorrer los pares clave-valor
for key, value in my_dict.items():
  print(f'{key} : {value}')

######## FIN DICCIONARIOS (MAPAS) ##################################

########  EJERCICIO EXTRA - AGENDA DE CONTACTOS  ########

end = False
phone_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
contact_list = []

while not end:
  #Imprimir menu de opciones
  print('#### AGENDA DE CONTACTOS POR TERMINAL ####')
  print("1. Añadir un contacto")
  print("2. Buscar un contacto")
  print("3. Modificar un contacto")
  print("4. Eliminar un contacto")
  print("5. Salir de la agenda.")
  
  option = int(input("¿Qué deseas hacer? (1-5): "))
  
  # Control de opción introducida
  while option not in range(1, 6):
    print("Error: Debes introducir un valor entre 1 y 5.")
    option = int(input("¿Qué deseas hacer?"))
  
  # Gestión de la opción
  if option == 1:
    print("Añadir un contacto")
    name = input("Introduce el nombre del contacto: ")
    while name == "" or len(name) < 3:
      print("Error: El nombre debe tener al menos 3 caracteres.")
      name = input("Introduce el nombre del contacto: ")
      
    phone = input("Introduce el número de teléfono (máximo 11 digitos entre el 0 y el 9): ")
    while phone == "" or len(phone) > 11:
      print("Error: Debes introducir un número de teléfono válido: ")
      phone = input("Introduce el número de teléfono (máximo 11 digitos entre el 0 y el 9): ")
    
    # Comprobación adicional de que el usuario solo mete dígitos en el campo phone
    for digit in phone:
      if digit not in phone_values:
        print("Error: El número introducido tiene valores no válidos para un nro. de teléfono, se autocompleta con 0000 y después deberás modid¡ficarlo")
        phone = "0000"
        continue
    
    # Agregamos los valores 
    contact = {"name" : name, "phone" : phone}
    contact_list.append(contact)
    
    print(f"Se ha añadido el contacto: {contact} a la agenda")
    
  elif option == 2:
    print("Buscar un contacto")
    name = input("Introduce el nombre del contacto a buscar: ")
    while name == "" or len(name) < 3:
      print("Error: El nombre debe tener al menos 3 caracteres.")
      name = input("Introduce el nombre del contacto a buscar: ")
    
    for contact in contact_list:
      if contact["name"].lower() == name.lower():
        print("Contacto encontrado")
        print(f"Nombre: {contact['name']}, teléfono: {contact['phone']}")
        break
      else:
        print("Contacto no encontrado, si desea añadirlo puede hacerlo")
      
  elif option == 3:
    print("Modificar un contacto")
    name = input("Introduce el nombre del contacto a modificar: ")
    while name == "" or len(name) < 3:
      print("Error: El nombre debe tener al menos 3 caracteres.")
      name = input("Introduce el nombre del contacto a buscar: ")
    
    for contact in contact_list:
      if contact["name"].lower() == name.lower():
        print("Contacto encontrado")
        name = input("Introduce el nuevo nombre de contacto o nada si no se va a modificar este campo: ")
        phone = input("Introduce el número de teléfono (máximo 11 digitos entre el 0 y el 9): ")
        while phone == "" or len(phone) > 11:
          print("Error: Debes introducir un número de teléfono válido: ")
          phone = input("Introduce el número de teléfono (máximo 11 digitos entre el 0 y el 9): ")
        
        #Modificamos los datos
        contact["name"] = name if name != "" else contact["name"]
        contact["phone"] = phone
        
        print(f"Se ha modificado el contacto, ahora se muestra así: {contact}")
        break
      else:
        print("Contacto no encontrado, si desea añadirlo puede hacerlo")
  elif option == 4:
    print("Eliminar un contacto")
    name = input("Introduce el nombre del contacto a modificar: ")
    while name == "" or len(name) < 3:
      print("Error: El nombre debe tener al menos 3 caracteres.")
      name = input("Introduce el nombre del contacto a buscar: ")
    for contact in contact_list:
      if contact["name"].lower() == name.lower():
        print("Contacto encontrado, se procede a su eliminación...")
        del contact["name"]
        print("Proceso de eliminación completado...")
        break
      else:
        print('El contacto no se encuentra en la agenda, luego no es posible su eliminación.')
  else:
    end = True
    print("Fin de la aplicación")

########  FIN EJERCICIO EXTRA - AGENDA DE CONTACTOS  ########