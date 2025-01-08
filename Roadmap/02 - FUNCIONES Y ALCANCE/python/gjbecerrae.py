#Funcion sin parametros ni retorno
def printFunction():
    print('Esta es una funcion sin parametros ni retorno')

#Funcion con 1 parametro sin retorno
def oneParameterFunction(a):
    print(f'Esta es una funcion de un parametro -> {a}')

def twoParameterFunction(a,b=1,c=2):
    print(f'Esta funcion tiene 3 parametros {a}, {b} y {c}. Si c no esta en los parametros toma el valor por defecto de 2')

def returnFuncionNoParameters():
    print('Esta es una funcion con retorno y sin parametros')
    return 'return'

def returnFuncionParameters(param1):
    print('Esta es una funcion con retorno y con parametros. El retorno es ->')
    return param1*2

def internalFunction():
    value = 6
    return value

def Externalfunction():
    internalValue = internalFunction()
    newValue = internalValue * 2
    if newValue == 12:
        print ('Las funciones se pueden utilizar dentro de otras funciones')
    else:
        print ('Las funciones no se pueden utilizar dentro de otras')

def gobalVarFunction():
    print(f'{myGlobal} dentro de una funcion')

#Ejercicio Opcional:
def stringToNumber(string1, string2):
    counter = 0
    for i in range (1,101):
        if  i % 3 == 0 and i % 5 == 0:
            print(string1,string2)
            counter += 1        
        elif i % 3 == 0:
            print (string1)
            counter += 1
        elif i % 5 == 0:
            print (string2)
            counter += 1
        else:
            print(i)
    numero = 100 - counter
    return  numero

#Llamadas a funciones
print("\n-----------------------------------------------------------")
print('Llamadas a Funciones \n')
printFunction()
oneParameterFunction('Hola soy el parametro')
twoParameterFunction(10,20)
print(returnFuncionNoParameters())
retorno = returnFuncionParameters(3)
print(retorno)
Externalfunction()
print("\n-----------------------------------------------------------")

#Python build-in functions
print("\nLa funcion Len nos permite obtener la talla de una lista ->")
miLista = ['esta','es','mi','lista']
print (f'Mi lista es => {miLista} \nY tiene una talla de {len(miLista)}')

print("\n-----------------------------------------------------------")

myGlobal = 'Esta es una variable global'

for i in range (3):
    myLocal = 'Esta es una variable local'
    if i == 0:
        print (f'{myLocal}. No puedo usarla fuera de este loop')
   
    if i == 2:
        print (f'{myGlobal} Puedo usarla dentro de mi for loop ')
        gobalVarFunction()

print("\n-----------------------------------------------------------")
print('Ejercicio Opcional \n')

opcional = stringToNumber('primer parametro','segundo parametro')
print(f'El numero se ha impreso {opcional} veces')




