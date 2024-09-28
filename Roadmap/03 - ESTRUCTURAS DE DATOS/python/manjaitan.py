# ESTRUCTURAS DE DATOS en python:

# listas, tuplas, diccionarios:

# LISTAS (mutables).

deportes = ['ciclismo','atletismo','motociclismo','automovilismo']

# insertar en lista: 
deportes.append('barranquismo')
print (type(deportes))
print (deportes)


# borrado en lista:
deportes.remove('barranquismo')
print (type(deportes))
print(deportes)

# actualizar elemento de lista: (actualizamos la posición 3 de la lista, retiramos )
deportes[3] = 'barranquismo'
print (type(deportes))
print  (deportes)

# Ordenacion de listas:
deportes.sort() # ordena los items de la lista alfabeticamente.
print (type(deportes))
print(deportes)

# TUPLAS: (inmutables)

numeros = (1,2,3,4,5,6,7,8,9,10) # A diferencia de las listas, las tuplas se crean entre parentesis.
print (type(numeros))
print (numeros)

numeros = 1,2,3,4,5,6,7,8,9,10 # Otra forma de declarar las tuplas.
print (type(numeros))
print (numeros)

# DICCIONARIOS:

diccionario = {} # creamos el diccionario.
diccionario1 = {
    "nombre" : "Antonio Perez Fernández",
    "usuario" : "antonio",
    "perfil" : "admin"
    
}


print (type(diccionario))
print (diccionario)
print (type(diccionario1))
print (diccionario1)

diccionario2 = {
    "nombre" : "manjaitan",
    "usuario" : "manjaitan",
    "perfil" : "admin"
    
}

# Añadimos clave:valor del diccionario2.
diccionario2['perfil1']='propietario'
diccionario2['estado']='activo'
print (diccionario2)

# Borrar clave:valor del diccionario2.
del diccionario2["estado"]
print(diccionario2)

# Actualizar valores del diccionario2.
diccionario2["perfil1"]='delegado'
print(diccionario2)

# Eliminar diccionario completo.
del diccionario2
# print(diccionario2) # lo comentamos para no generar error.

#### OPCIONAL:

opciones = [
"1. Búsqueda de contacto",
"2. Crear nuevo contacto",
"3. Actualización de contacto",
"4. Eliminación de contacto",
"5. Salir"
]

# Creamos un diccionario con las claves y valores que necesitamos.
contacto = {
    'Angel' : '123123123',
    'Pedro' : '123123321',
    'Fran' : '321321321',
    }
    

while True:
    print ('########## MENU OPCIONES ###############')
    print ('Valores del diccionario')
    print (contacto)
    print ('#########################################')
    
    for opcion in opciones:
        print(opcion)
        
    opcion = input("Ingrese una opción: ")
    
    if (opcion == '5'): 
        break
    
    elif (opcion == '1'):
        
        print('##### BUSQUEDA DE CONTACTO ########')
        
        busca = input("Ingrese nombre de contactoa a buscar: ")
        res_get = contacto.get(busca, 2000)
        
        if ( res_get == 2000):
            
            print('elemento no encontrado')
            
        else:
            
            print ('elemento encontrado')
            print (busca)
            print (contacto.get(busca))
    
    elif (opcion == '2'):
        
        print('##### CREACION DE NUEVO CONTACTO ########')
        n = input ('Ingrese nombre de contacto: ')
        t = input('Ingrese número telefono contacto: ')
        
        if (len(t) >= 11):
            print ('nº de telefono +11 digitos no es correcto, no se inserta registro')
        elif (t.isalpha()): 
            print ('nº de telefono contiene caracteres alphanumericos')
        else:
            print ('campos OK, se inserta nuevo contacto en diccionario')
            contacto.setdefault(n,t)
    
    elif (opcion == '3'):
        
        print('##### ACTUALIZACION DE UN CONTACTO ########')
        
        nam_upd = input("Ingrese nombre de contacto a actualizar: ")
        tel_upd = input('Ingrese número telefono contacto: ')
        
        get_bus = contacto.get(nam_upd, 3000)
        
        if ( get_bus == 3000):
            print('elemento no encontrado')
        elif (tel_upd.isalpha()): 
            print ('nº de telefono contiene caracteres alphanumericos')
        elif (len(tel_upd) >= 11):
            print ('nº de telefono +11 digitos no es correcto, no se actualiza registro')
        else:
            print ('campos OK, se actualiza el contacto')
            contacto.update({nam_upd:tel_upd})
        
    elif (opcion == '4'):
    
        print ('##### ELIMINAR CONTACTO ########')
        print(contacto)
        e = input ('Ingrese nombre de contacto que desea eliminar: ')
        res_del = contacto.get(e, 5000)
        
        if ( res_del == 5000):
            print('elemento no encontrado')
        else:
            print ('elemento encontrado')
            contacto.pop(e)
            print ('elemento borrado')