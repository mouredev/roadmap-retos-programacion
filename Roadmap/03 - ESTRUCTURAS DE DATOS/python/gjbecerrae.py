### Estructuras de datos ###

#listas ----
print('\n\nListas --------------------------------------\n ')
miLista = ['item1', 'item2', 'item3', 'item4', 'item5', 'item0']
miLista.append('item6')
miLista.extend(['item7','item8'])
print('miLista completa -> ', miLista)
print('Veces que item1 esta en la lista -> ', miLista.count('item1'))
print('El index de item3 es -> ', miLista.index('item3'))
miLista.remove('item2')
print('item2 ha sido removido -> ', miLista)
print('Lista actual -> ', miLista)
miLista.sort()
print('Lista ordenada -> ', miLista)

#
#Tuplas ---
print('\nTuplas --------------------------------------\n ')
print('Son inmutables\n ')
miTupla = ('hola','Python')
print('Mi tupla es ', miTupla)
print('El numero de veces que \'hola\' se encuentra en miTupla es ->', miTupla.count('hola'))
print('el Indice de \'Pytnon\, es -> ', miTupla.index('Python'))
miTupla2 = ([1,2,3],[4,5,6])
print('miTupla2 es ', miTupla2 )
print('Las listas dentro de miTupla2 son objetos mutables, voy a cambiar el item \'3\' pour un \'10\'')
miTupla2[0][2] = 10
print('miTupla2 es ', miTupla2 )

#Conjuntos ---
print('\nConjuntos -------------------------------------- ')
print('se usa para evitar duplicados\n ')
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)    
print('Orange esta en el basket? ','orange' in basket)

#Diccionarios ---
print('\nDiccionarios -------------------------------------- ')
miDict = {'key1':'value1', 'key2':'value2'}
print('miDict es ', miDict)
miDict['key3'] = 'value3'
print('Adiciiono key3: \n', miDict )
miDict.pop('key2')
print('Borro key2: \n', miDict )

#Ejercicio Opcional ---
print('\nejercicio Opcional -------------------------------------- \n')
agenda = {}

#La agenda sera un diccionario key= nombre appellido value=telefono
#ej {'Juan Montoya':'07071010101, 'Pedro Perez':'07071010102'}, se puede buscar al usuario por su nombre y apellido
continuar = True
while continuar:

    opcion = input('''Que quieres hacer?:\n 
    1. Crear un nuevo contacto\n 
    2. Buscar un contacto\n 
    3. Modificar un contacto\n
    4. Eliminar un contacto\n
    5. Salir\n''')

    if opcion == '1':
        print('Has seleccionado crear un nuevo contacto\n')
        nuevoContacto = input('Ingresa el nombre de tu contacto\n').lower()

        while True:
            numeroNuevoContacto = input('Por favor incluye solo digitos sin espacios en tu numero y maximo 11\n')
            if numeroNuevoContacto.isdigit() and len(numeroNuevoContacto) < 12:
                agenda[nuevoContacto] = numeroNuevoContacto
                break
        print(f'Tu contacto {agenda} ha sido guardado\n ')


    elif opcion == '2':
        print('Has seleccionado buscar un contacto ')
        buscarContacto = input('Cual es el nombre y appellido de tu contacto ')

        if buscarContacto.lower() in agenda:
            #Capitalize nombre y apellido solo para mostrarlo lindo
            nombre = buscarContacto.split()
            for i in range (len(nombre)):
                nombre[i] = nombre[i].capitalize()
            nombreCapitalized = ' '.join(nombre)        
            print(f'Tu contacto existe -> Nombre: {nombreCapitalized} Numero: {agenda[buscarContacto.lower()]}')

    elif opcion == '3':
        modificarContacto = input('Cual es el nombre y apellido de tu contacto? ').lower()
        opcionModificar = input('Ingresa \'nombre\' o \'numero\' depende lo que quieras modificar ')
        
        if opcionModificar == 'nombre':
            nuevoNombre = input('Cual es el nuevo nombre y appellido del contacto? ').lower()
            mantenerNumero = agenda[modificarContacto]
            agenda.pop(modificarContacto)
            agenda[nuevoNombre] = mantenerNumero

        elif opcionModificar == 'numero':
            while True:
                nuevoNumero = input('Cual es el nuevo numero del contacto?\n')
                if nuevoNumero.isdigit():
                    agenda[modificarContacto] = nuevoNumero
                    break
                else:
                    print('Por favor incluye solo digitos en tu numero\n')
        print(f'Tu contacto {agenda} ha sido modificado\n ')
    
    elif opcion == '4':
        eliminarContacto = input('Cual es el nombre y appellido del contacto que deseas eliminar? ').lower()

        if eliminarContacto in agenda:
            agenda.pop(eliminarContacto)
            print('El contacto ha sido eliminado ')
        
        else:
            print('Este contacto no existe ')
    
    elif opcion == '5':
        continuar = False

