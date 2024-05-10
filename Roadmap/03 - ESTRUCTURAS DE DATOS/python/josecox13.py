
#Lista
print('\n -----Listas-----')
lista_nombre = ['Juan', 'Pepe', 'Fran'] #Definición
print(lista_nombre)
lista_nombre.append('Jaime') #Inserción
print(lista_nombre)
lista_nombre.remove('Pepe') #Eliminación
print(lista_nombre)
lista_nombre[1] = 'Jorge' #Actualización
print(lista_nombre)
lista_nombre.sort() #Ordenación
print(lista_nombre)

#Conjunto o set 
print('\n -----Set-----')
mi_set = {1,1,3,4,7}
print(mi_set)
mi_set.add(8) #Inserción
print(mi_set)
mi_set.remove(1) #Eliminación
print(mi_set)
mi_set = sorted(mi_set) #esto lo convertirá en una lista

#Diccionario
print('\n -----Diccionarios-----') #definición
mi_diccionario = {'nombre':'Juan',
                'trabajo':'desarrollador IA',
                'edad':'30'}
print(mi_diccionario)
print(mi_diccionario['edad']) #acceso
mi_diccionario['empresa'] = 'Microsoft' #actualización o añadir una entrada
print(mi_diccionario)
del mi_diccionario['edad'] #borrado de una entrada
diccionario_ordenado = dict(sorted(mi_diccionario.items())) #ordenación
print(diccionario_ordenado)



#Tupla
print('\n -----Tuplas-----')
mi_tupla = ('Fran', 'Cuesta', 'Microsoft', 'Madrid')
#No se puede alterar ni modificar, solo acceder
print(mi_tupla[2])
mi_tupla = tuple(sorted(mi_tupla)) #Siempre que todos los componentes de la tupla sean del mismo tipo de dato

#Ejercicio extra
print('\n -----Ejercicio extra -----')
contactos = {'Lola':'672456241', 'Javi':'613782346'} 
def agenda():
    while True: #esto se va a ejecutar infinitas veces
        print('Bienvenido a su agenda. Las opciones disponibles son:')
        print('1. Buscar un contacto')
        print('2. Insertar contacto')
        print('3. Actualizar contacto')
        print('4. Eliminar contacto')
        print('5. Finalizar sesión')
        opcion = input(str('¿Qué desea realizar? '))
        if opcion == '1':
            nombre = input(str('Introduzca el nombre del contacto a buscar: '))
            if nombre in agenda:
                telefono = contactos[nombre]
                print(f'El teléfono de {nombre} es {telefono} \n')
            else:
                print('Teléfono no encontrado')
        elif opcion == '2':
            nombre = input(str('Introduzca el nombre del contacto que quiere añadir: '))
            telefono = input(str(f'Introduzca el teléfono de {nombre}: '))
            while len(telefono) >= 11:
                print('Telefono no válido. Introduzca un teléfono con la longitud correcta')
                telefono = input(str(f'Introduzca el teléfono de {nombre}: '))
            contactos[nombre] = telefono
            print ('Teléfono correctamente añadido')
        elif opcion == '3':
            nombre = input(str('Introduzca el nombre del contacto que quiere modificar: '))
            telefono = input(str(f'Introduzca el nuevo teléfono de {nombre}: '))
            while len(telefono) >= 11:
                print('Telefono no válido. Introduzca un teléfono con la longitud correcta')
                telefono = input(str(f'Introduzca el teléfono de {nombre}: '))
            contactos[nombre] = telefono
            print ('Teléfono correctamente modificado')
        elif opcion == '4':
            nombre = input(str('Introduzca el nombre del contacto que quiere borrar: '))
            if nombre in agenda:
                del agenda[nombre]
            else:
                print('No existe en su agenda este contacto')
        elif opcion == '5':
            print('Sesion terminada')
            break
        else:
            print('Comando no válido. Vuelva a introducir un comando')    

agenda()
