# Listas

lista = [1] # Creación
print(lista)
lista[0] = 2 # Asignación
print(lista)
lista.append(3) # Insertar elemento al final
print(lista)
lista.insert(2, 4) # Insertar elemento en un indice
print(lista)
lista.pop(-1) # Eliminar elemento de la lista por el indice
print(lista)
lista.reverse() # Invertir la lista
print(lista)
lista.sort() # Ordernar la lista en orden ascendente
print(lista) 
lista.remove(2) # Elimina un elemento determinado de la lista
print(lista) 

print()

# Tuplas inmutables (no se pueden modificar)

tupla = (2, 3, 4)   

print(f"Tupla normal: {tupla}")

def cuadrado(numero:int) -> int:
    return numero ** 2

tupla_cuadrado = tuple(map(cuadrado, tupla))

print(f"Tupla de cuadrados: {tupla_cuadrado}")

print()

# Diccionarios mutable y no ordenado

diccionario = {'clave': 'valor', 'clave2': [1, 2, 3], 'clave3': False}
print(diccionario)

diccionario['clave4'] = 41 # Insertar elemento al final
print(diccionario)

diccionario.pop('clave') # Eliminar un elemento por la clave
print(diccionario)

diccionario['clave3'] = True # Actualizar valor de una clave
print(diccionario)

un_valor = diccionario['clave2'] # Acceder a un valor por la clave
print(un_valor)

if 'clave2' in diccionario: # Verificar si existe una clave en el diccionario
    print('La clave está en el diccionario.')
else:
    print('La clave no está en el diccionario.')

# Sets (conjuntos), no se permite modificar un elemento, no tienen orden.
    
lista_a_set = set(lista) # puedo crear un set a partir de una lista
print(lista_a_set)

mi_set = {1, 3, 4, 5} # Creacion del set
print(mi_set)

mi_set.add(4) # Agregar un elemento al set
print(mi_set)

mi_set.update({6, 7}) # Agregar varios elementos al set
print(mi_set)

mi_set.remove(4) # Eliminar un elemento del set
print(mi_set)

print()

# Ejercicio EXTRA

def leer_nombre():
    while True:
        entrada = input("Ingresa el nombre exacto de tu contacto\n")
        if entrada.isalpha() and len(entrada) > 0:
            return entrada
        else:
            print("La entrada debe ser un nombre.")

def leer_numero():
    while True:
        entrada = input("Ingresa el número de teléfono.\n")
        if entrada.isnumeric() and len(entrada) <= 11:
            return entrada
        else:
            print("La entrada no es numérica o tiene más de 11 números.")

contactos = {'Nombre': 400, 'Felipe': 300}

def opciones():
    while True:
        print('¿Qué deseas realizar?')
        print('1. Buscar un contacto')
        print('2. Agregar un contacto')
        print('3. Actualizar un contacto')
        print('4. Eliminar un contacto')
        print('5. Salir')

        accion = input()

        if accion == '1':
            buscar()
        elif accion == '2':
            insertar()
        elif accion == '3':
            actualizar()
        elif accion == '4':
            eliminar()
        elif accion == '5':
            print('Adiós.')
            break
        else:
            print('Inválido.')

def buscar():
    nombre = leer_nombre()
    if nombre in contactos:
        print(f"Nombre: {nombre}. Teléfono: {contactos[nombre]}.")
    else:
        print(f"El contacto '{nombre}' no existe.")

def insertar():
    nombre = leer_nombre()
    numero = leer_numero()
    contactos[nombre] = numero
    print(f"El contacto {nombre} ha sido añadido.")

def actualizar():

    nombre = leer_nombre()
    if nombre in contactos:
        print(f"Nombre: {nombre}. Teléfono: {contactos[nombre]}.")
    else:
        print(f"El contacto {nombre} no existe.")

    def actualizar_numero(nombre: str, nuevo_numero: int):
        contactos[nombre] = nuevo_numero
        print('El número de teléfono del contacto ha sido actualizado.')
    
    def actualizar_nombre(nombre: str, nuevo_nombre: str):
        contactos[nuevo_nombre] = contactos.pop(nombre)
        print('El nombre del contacto ha sido actualizado.')

    def opciones_actualizar(nombre: str):
        accion = input("1. Deseo cambiar el número.\n2. Deseo cambiar el nombre.\n")

        if accion == '1':
            nuevo_numero = leer_numero()
            actualizar_numero(nombre, nuevo_numero)
        elif accion == '2':
            nuevo_nombre = leer_nombre()
            actualizar_nombre(nombre, nuevo_nombre)
        else:
            print('Inválido.')
            opciones_actualizar()

    opciones_actualizar(nombre)
        

def eliminar():
    nombre = leer_nombre()
    if nombre in contactos:
        print(f"Nombre: {nombre}. Teléfono: {contactos[nombre]}.")
    else:
        print(f"El contacto {nombre} no existe.")
    
    def opciones_eliminar():
        acccion = input('¿Quieres eliminar este contacto?\n1. Sí.\n2. No\n')

        if acccion == '1':
            contactos.pop(nombre)
            print('El contacto ha sido eliminado.')
        elif acccion == '2':
            print('Te perdono.')
        else:
            opciones_eliminar()
        
    opciones_eliminar()

opciones()