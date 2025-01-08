# Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# Utiliza operaciones de inserción, borrado, actualización y ordenación.


'''
-> La lista es una colección ordenada y modificable. Permite miembros duplicados.
-> Tupla es una colección ordenada e inmutable. Permite miembros duplicados.
-> Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
-> El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
'''

def lista():
    miListaStr = ['naranja', 'banana', 'durazno']
    miListaBool = [True, True, False]
    miListaNum = [0,1,2,3,4]
    miListaX = [0 , 1, 'naranja', True, 'banana', 3, 4, 5, False, 'durazno']
    laLista = list(('banana', 'banana', 'pomelo')) #Funcion constructor lista
    print('\n',type(miListaStr),
          '\n', miListaStr,
          '\n', miListaBool,
          '\n', miListaNum,
          '\n', miListaX,
          '\n', laLista
          ,'\n'
          )
    
    #Impresion de un valor en particular de la lista:
    print('\n', 'Primer elemento de la lista con strings: ', miListaStr[0],
          '\n', 'Ultimo elemento de la lista con booleanos: ', miListaBool[-1],
          '\n', 'Cuarto elemento de la lista numerica: ', miListaNum[3]
          )
    #Impresion de valores en un margen dentro de la lista: 
    print('\n', 'Primeros 4 valores de lista X: ', miListaX[0:4],
          '\n', 'Todos los valores desde el indice 2: ', miListaX[2:], 
          '\n', 'Todos los valores hasta el indice 4: ', miListaX[:4]  
          )
    #Verificar si existe un valor en particular dentro de la lista, de ser el caso, cambiarlo por otro mas delicioso:
    if 'durazno' in miListaX:
        print('\n', 'La lista X contiene el string DURAZNO... lo cambiare por doritos')
        miListaX[-1] = 'doritos'
        print('\n', miListaX, '\n', 'Ahora que todos los string en la lista sean doritos', '\n')
        for i in range(len(miListaX)):
            if isinstance(miListaX[i], str): #verificar si el valor es de tipo str
                miListaX[i] = 'doritos'
        print(miListaX, '\n', 'mucho mejor', '\n')


    #Cambiar los valores dentro de un margen de indices:
    miListaBool[0:] = [True, True, True, True] #cambiar todos los valores de esta lista a true
    print('\n', 'Ahora mi lista booleana tiene solo valores verdaderos.', '\n', miListaBool)
    
    miListaNum[2:4] = [0, 0, 0]
    print('\n', 'Cambie del inidice 2 al 4 los valores por 0: ', '\n', miListaNum, '\n',)
    

    #utilizando el insert es posible insertar valores en la lista, sin reemplazar los valores ya existentes en la misma
    listaDias = ['lunes', 'martes', 'jueves', 'viernes', 'sabado']
    listaDias.insert(2, 'miercoles')
    listaDias.insert(6, 'domingo')
    print('lista de dias:', listaDias)

    #Utilizando append podemos insertar elementos al final de la lista
    listaMeses2 = ['mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre']
    listaMeses2.append('noviembre')
    listaMeses2.append('diciembre')
    print('\n', 'lista de meses incompleta: ', listaMeses2)
    
    #Extend es una funcion que nos permite incorporar una lista a otra, tambien tuplas,conjuntos, diccionarios...
    listaMeses1 = ['enero', 'febrero', 'marzo', 'abril']
    listaMeses1.extend(listaMeses2)
    print('\n','lista de meses completa: ', listaMeses1)


    #Remove() y pop() para eliminar elementos de una lista 
    listaPaises = ['chile', 'argentina', 'mexico', 'peru', 'bolivia', 'ecuador'] 
    listaPaises.remove('peru')
    print('\n', 'lista de paises excluyendo a peru', listaPaises)

    listaPaises = ['chile', 'argentina', 'mexico', 'peru', 'bolivia', 'ecuador'] 
    listaPaises.pop(3)
    print('\n', 'lista de paises excluyendo a peru nuevamente', listaPaises)

    #Ordenar una lista de menor a mayor y en orden alfabetico
    listaString = ['papaya', 'kiwi', 'arandano', 'manzana', 'banana', 'palta']
    listaInt = [1, 6, 4, 3, 8, 10, 2, 2]

    listaString.sort()
    listaInt.sort()
    print('\n', listaString, '\n', listaInt)

    #Ordenar de forma descendiente 
    listaString.sort(reverse = True)
    listaInt.sort(reverse = True)
    print('\n', listaString, '\n', listaInt)

 
def tupla():
    #al igual que las listas los valores en las tuplas pueden repetirse, pero no se pueden alterar su contenido.
    tuplaSimple = ('league of legend', 'overwatch', 'rust', 'the finals', 'league of legend')

    #tuplaSimple.remove('rust') ERROR
    #tuplaSimple.insert('minecraft') ERROR
    #tuplaSimple.append('osu') ERROR

    #pueden contener cualquier tipo de dato
    tupla1 = ('apple', 'banana', 'cherry')
    tupla2 = (1, 5, 7, 9, 3)
    tupla3 = (True, False, False)
    tuplaX = ('apple', 7, 9, 3, False, False)
    print('\n', type(tuplaX),
          '\n', 'tupla con strings', tupla1, 
          '\n', 'tupla con enteros', tupla2, 
          '\n', 'tupla con booleanos', tupla3, 
          '\n', 'tupla con todo!', tuplaX, '\n'
          )
    miTupla = tuple(('banana', 'manzana', 'sandia')) #constructor de tupla


    #Cambiar su valores
    #las tuplas son inmutables, por lo que primero se deben pasar a lista para despues reconvertir en tupla
    laTupla = ('manzana', 'patata', 'melon', 'uva')
    print(laTupla)
    laLista = list((laTupla))
    laLista[0] = 'pera'
    laTupla = tuple((laLista))
    print(laTupla, '\n')

    #Agregar elementos
    #al igual que anteriormente, se puede converitir tupla en lista para agregar elementos
    laLista = list((laTupla))
    laLista.append('jugo de naranja!')
    laTupla = tuple((laLista))
    print(laTupla, '\n')

    #Eliminar elementos
    #mas de lo mismo, solo convertimos en lista y usamos remove o pop
    laLista = list((laTupla))
    laLista.remove('patata')
    laLista.pop(0)
    laTupla = tuple((laLista))
    print(laTupla, '\n')


def setF():
    miSet = {'sombrero', 'botas', 'traje', 'pantalon'}
    print('\n', 'set de ropa', miSet, '\n') #siempre saldra desordenado

    miSet = {'sombrero', 'botas', 'traje', 'pantalon', 'pantalon', 'pantalon', 'pantalon', 'pantalon'}
    print('\n', 'set de ropa con elemento repetido', miSet, '\n') #se ignoran los valores duplicados, no estan permitidos

    miSet = {'sombrero', 'botas', 'traje', 'pantalon', True, 1}
    print('True y 1  ', miSet, '\n') #son considerados como lo mismo, por lo que cuenta como elemento duplicado
    miSet = {'sombrero', 'botas', 'traje', 'pantalon', False, 0}
    print('False y 0  ', miSet, '\n')

    set1 = {"manzana", "banana", "tomate"}
    set2 = {1, 5, 7, 9, 3}
    set3 = {True, False, False}
    tuplaX = {'apple', 7, 9, 3, False, False}
    print('\n', type(tuplaX),
          '\n', set1,
          '\n', set2,
          '\n', set3, '\n'
          )
    
    crearSet = set(('banana', 'pan', 'tomate', 'leche')) #constructor de set
    print(crearSet)
    
    #no se puede acceder mediante un indice a los valores de un set
    #no obstante se pueden recorrer mediante un bucle
    for x in crearSet:
        print(x)

    #una vez creado el set no se pueden cambiar sus elementos, pero si agregar nuevos!
    crearSet.add('naranja') #mediante 'add'
    print(crearSet, '\n')

    #agregar elementos desde otro set
    set1.update(set2)
    print(set1, '\n')

    #Remover elementos de un set.
    set1.remove('manzana')
    set1.discard(3)
    print(set1, '\n')
      # tambien se puede utilizar el metodo POP() pero esto eliminara un elemento aleatorio


def diccionario():
    miDiccionario = {'rojo':'red', 'verde':'green', 'azul':'blue'}
    miDiccionario['amarillo'] = 'yellow' #INGRESAR elementos en el diccionario
    miDiccionario['rojo'] = 'RED' #CAMBIAR valor de la clave por otro(en este casos olo lo puse en mayusculas)
    miDiccionario['verde']

    print(miDiccionario['azul'], '\n') #blue
    print(miDiccionario.keys()) #solo las claves
    print(miDiccionario.values(), '\n') #solo los valores

    usuarioDatos = dict(name = 'pepe', especie = 'rana', edad = '1000 años', pais = 'chile') #constructor de diccionarios. DICT
    print(usuarioDatos, '\n')

    #Eliminar elementos de un diccionario
    usuarioDatos.pop('edad') #POP eliminara la clave especifica que le demos como argumento
    print(usuarioDatos)

    #popitem() eliminara el ultimo elemento ingresado, antiguamente eliminaba uno al azar
    #del eliminara cualquier elemento con el nombre que le demos
    #clear() es un metodo que vacia el diccionario 

lista()
tupla()
setF()
diccionario()

##################### Dificultad extra.- ##################### 
print('\n','\n','\n','\n','\n')

def agendaTelefonica():
    listaContactos = [['pepe', 10323234666], ['juan', 30142424352]]
    i = False

    def buscarContacto():
        nombre = input('Nombre del contacto: ')
        for x in range(len(listaContactos)):
            if nombre in listaContactos[x]:
                print('Numero de', nombre, ': ', listaContactos[x][1])
                break
            print('Ese contacto no se encuentra en la lista.')
                
    
    def verContactos():
        longitudLista = len(listaContactos) 
        for x in range(longitudLista):
            elemento = listaContactos[x]
            print(elemento)
    
    def agregarContacto():
        nombreContacto = input('Nombre ')

        try:
            numeroContacto = int(input('Numero: '))
        except ValueError:
            print('Debe ingresar un valor numerico!')
        
        cantDigitos = (numeroContacto)
        cantDigitos = str(cantDigitos)
        cantDigitos = len(cantDigitos)
    
        while cantDigitos > 11:
            try:
                numeroContacto = int(input('Numero no puede superar los 11 digitos: '))
            except ValueError:
                print('Debe ingresar un valor numerico!')
            cantDigitos = str(numeroContacto)
            cantDigitos = len(cantDigitos)

        registroContacto = [nombreContacto, numeroContacto]
        listaContactos.append(registroContacto)
    
    def editarContacto():
        contacto_a_editar = input('Que contacto desea editar?')
        for x in range(len(listaContactos)):
            if contacto_a_editar in listaContactos[x]:
                try:
                    opcion = int(input('Numero de la opcion->  1.- nombre 2.- numero'))
                except ValueError:
                    print('Debe ingresar un numero.')
                    break
                if opcion == 1:
                    listaContactos[x][0] = input('Ingrese nuevo nombre: ')
                elif opcion == 2:
                    try:
                         listaContactos[x][1] = int(input('Ingrese nuevo numero: '))
                    except ValueError:
                        print('Debe ingresar un valor valido.')
                        break

    def borrarContacto():
        contacto_a_eliminar = input('Nombre del contacto que desea eliminar: ')
        for x in range(len(listaContactos)):
            if contacto_a_eliminar in listaContactos[x]:
                listaContactos.remove(listaContactos[x])
                break
            else:
                print('Contacto no esta en la lista.')


    while i != True:
        print('Agenda ', '\n',
            '1.- buscar contacto', '\n',
            '2.- ver lista de contactos', '\n',
            '3.- agregar contacto', '\n',
            '4.- editar contacto', '\n',
            '5.- eliminar contacto', '\n',
            '6.- cerrar programa', '\n'
            )
        try:
            opcion = int(input('seleccione numero para una accion: '))
        except ValueError:
            print('ingrese numero solamente.')
            continue

        if opcion == 6:
            i = True
        elif opcion > 6 and opcion < 1:
            print('Opcion no valida', '\n')

        if opcion == 1:
            buscarContacto()
        elif opcion == 2:
            verContactos()
        elif opcion == 3:
            agregarContacto()
        elif opcion == 4:
            editarContacto()
        elif opcion == 5:
            borrarContacto()
    
agendaTelefonica()













