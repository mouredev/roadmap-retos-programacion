### estructuras ###

## Listas

# Crear una lista
list_a =list()
list_b =[]

print(type(list_a))
print(type(list_b))
# datos de una lista
list_b = ['txuky', 'Francesc', 'More', 56, 169.5, True,56]

#acceso a los datos
print('=*' * 30)

print(list_b)
print(list_b[0])
print(list_b.index('Francesc'))
print(list_b.count(56))
list_b.pop()

# insertar, añadir y eliminar datos de la lista
print('=*' * 30)

list_b.append(55)
list_b.insert(3, 'Verde')
print(list_b)
list_b[3]='Amarillo'
print(list_b)
list_b.remove('Amarillo')
print(list_b)
list_b[0]='Azul'
print(list_b)
del list_b[0]
print(list_b)


# assignar datos de una lista a variables 
print('=*' * 30)

# segun orden de lista
name, surname, age, weight, subscribed, age_2 = list_b

if subscribed == True:
    print(f'Me llamo {name}{surname} tengo {age} y mido {weight} y estoy subscrito ')
else:
    print(f'Me llamo {name}{surname} tengo {age} y mido {weight} y no estoy subscrito ')

# segun indice
age, weight, surname, name, age_2, subscribed = list_b[2], list_b[3], list_b[1], list_b[0], list_b[5], list_b[4]

if subscribed == True:
    print(f'Me llamo {name}{surname} tengo {age} y mido {weight} y estoy subscrito ')
else:
    print(f'Me llamo {name}{surname} tengo {age} y mido {weight} y no estoy subscrito ')

# manejo de las listas
print('=*' * 30)

list_a = list_b.copy()
print(list_a)

list_a.reverse()
print(list_a)

list_a.pop(-1)
list_a.pop(-1)
list_a.pop(1)
print(list_a)
list_a.sort() #solo funciona si los elementos son del mimoo typo o num o str
print(list_a)

list_a.clear()
print(list_a)

## Tuplas


# Crear una tuple
tuple_a =tuple()
tuple_b =()

print(type(tuple_a))
print(type(tuple_b))
# datos de una tuple
tuple_b = ('txuky', 'Francesc', 'More', 56, 169.5, True,56)
print(type(tuple_b))

#acceso a los datos
print('=*' * 30)

print(tuple_b)
print(tuple_b[0])
print(tuple_b.index('Francesc'))
print(tuple_b.count(56))
# tuple_b.pop()

# insertar, añadir y eliminar datos de la lista
print('=*' * 30)

#tuple_b.append(55)
#tuple_b.insert(3, 'Verde')
#tuple_b[3]='Amarillo'
#tuple_b.remove('Amarillo')
#tuple_b[0]='Azul'
#del tuple_b[0]
print(tuple_b)
print('Las tuples sin INMUTABLES')

# assignar datos de una lista a variables 
print('=*' * 30)

# desempaquetado de tupla

alias, name, surname, age, weight, subscribed, age_2 = tuple_b

if subscribed == True:
    print(f'Me llamo {name}{surname} tengo {age} y mido {weight} my alias es : {alias} y estoy subscrito ')
else:
    print(f'Me llamo {name}{surname} tengo {age} y mido {weight} my alias es : {alias} y no estoy subscrito ')

''' # segun indice no funciona
age, weight, surname, name, alias, age_2, subscribed = tuple_b[3], tuple_b[4], tuple_b[2], tuple_b[1], alias[0] tuple_b[6], tuple_b[5]
'''
# manejo de las listas
print('=*' * 30)

tuple_a = tuple_b
print(tuple_a)
print(type(tuple_a))

tuple_c = tuple_a, (1, 2, 3, 4)
print(tuple_c)
print(type(tuple_c))
elem_tupla = len(tuple_c)
print(f'Cuantos elementos tiene tuple_c: {elem_tupla} ')
print('Elemento 0 :',end=" " ) 
print(tuple_c[0])
print('Elemento 1 ', tuple_c[1])
print('Cada uno de los dos elemntos de la tuple es una lista, pero la tuple solo tiene 2 elemntos')

# como son inmutables no funciona nada que las pueda modificar tipo .sort .reverse ,clear

# Sets 
print('=*' * 30)

celta_staff = set()
celta_gamers = {'Coke', 'Aidoo', 'Alfon', 'Javi','Javi', 'Manu', 'Martin', 'Hugo', 'Alfon' }
print(type(celta_staff))
print(type(celta_gamers))

print(celta_gamers)
#devuelve los elementos no repetidos
#los sets sobre todo se indican par verificacion de permanencia y eliminacion de duplicados

celta_staff = {'Claudio', 'Nando', 'Alejandro', 'Jesus', 'Nando'}

personaje = 'Nando'

if personaje in celta_gamers:
    print ('Coke es jugador del Celta')
elif personaje in celta_staff:
    print ('Coke es parte del staff del Celta')
else:
    print('Coke no pertenece al Celta')

print('=*' * 30)

nums_a = {1, 2, 4 ,5 ,6 ,7}
nums_b = {3, 5, 5, 7, 8, 4, 22, 9, 0}
print(nums_a)
print(nums_b)

print(nums_a - nums_b)
print(nums_a & nums_b)
print(nums_a | nums_b)
print(nums_a ^ nums_b)

# podemos eliminar elementos o limpiar el set y añadir nuevos

celta_gamers.remove('Alfon')
print(celta_gamers)

celta_staff.clear()
print(len(celta_staff))

celta_staff.add('Alfon')
print(len(celta_staff))
print(celta_staff)
celta_staff.add('Claudio')
print(len(celta_staff))
print(celta_staff)


# diccionarios 
print('=*' * 30)

# construccion
codig_cli = {'Francesc':'c125', 'Ricardo':'c135', 'Carmen':'c100'}
alias_cli = dict(c125='Txuky', c135 = 'King', c100 = 'Mqueen')
#alias_cli = dict(one='Txuky', two = 'King', three = 'Mqueen')

print(type(codig_cli))
print(type(alias_cli))

print(list(codig_cli))
print(len(codig_cli))
print(alias_cli['c125'])
print('Ricardo' in codig_cli)
print('King' in alias_cli)
print('c135' in alias_cli)

codig_cli['Pedro'] = 'c180' #inserta una nueva key con su valor
print(codig_cli)

codig_cli = dict(sorted(codig_cli.items()))
print(codig_cli)

# podemos operar con los diccionarios 
print('=*' * 30)

print(alias_cli)
alias_cli['c100'] = 'Toga' # Asigna el valor [key]
print(alias_cli['c100'])

del alias_cli['c135'] # Elimina [key]
print(alias_cli)

alias_cli_2 = alias_cli.copy()
print(alias_cli_2.items())
print(alias_cli_2.keys())
print(alias_cli_2.values())

alias_cli_2.setdefault('c135', 'NeTeam')
print(alias_cli_2)

list_contc = ['Tel', 'Email', 'Adres' ]
contact_cli = dict.fromkeys(list_contc)
print(contact_cli)


### Extra
print('=*' * 30)

def agenda_cont():
    
    agenda = {}

    def ins_contac():
        telef = input('Introducir telefono: ')
        if telef.isdigit() and len(telef) <= 9:
            agenda[nom] = telef
        else:
            print('El telefono no puede tener  mas de 9 igitos')

    while True:
        print('')
        print('Menu Opciones')
        print('1. Buscar contacto')
        print('2. Insertar contacto')
        print('3. Actualizar contacto')
        print('4. Eliminar contacto')
        print('5. Salir')

        option = input('\nSeleccione una opcion: ')

        match option:
            case '1':
                nom = input('Introduce el nombre del contacto a buscar: ')
                if nom in agenda:
                    print(f'El telefono de {nom} es {agenda[nom]}.')
                else:
                    print(f'El contacto {nom} no existe.')
            case '2':
                nom = input('Introduce el nombre del contacto: ')
                ins_contac()
            case '3':
                nom = input('introduce nombre del contacto a actulizar: ')
                if nom in agenda:
                    ins_contac()
                else:
                    print(f'El contacto {nom} no existe debes crearlo.')
            case '4':
                nom = input('Introduce el nombre del contacto a borrar: ')
                if nom in agenda:
                    del agenda[nom]
                else:
                    print(f'El contacto {nom} no existe no se puede borrar.')
            case '5':
                print('Hasta pronto')
                break
            case _:
                print('Opcion no valida elije una opcion entre el 1 y el 5')

agenda_cont()