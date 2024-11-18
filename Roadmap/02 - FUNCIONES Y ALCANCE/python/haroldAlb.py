'''
FUNCIONES Y ALCANCE
'''
print('##Ejemplos de funciones')
def hola():
    print('Hola gente')

def suma(num1, num2):
    print(f'La suma de {num1} y {num2} es {num1 + num2}')

def suma2(num1= 0, num2= 0):
    print(f'La suma de {num1} y {num2} es {num1 + num2}')

def iteracion(principio, fin):
    numeros=[]
    for num in range(principio, fin+1):
        numeros.append(num)
    return numeros

hola()

n1= 5
n2= 6
suma(n1, n2)

suma2()
suma2(n1, n2)

print(iteracion(2, 10))

print('##Funciones dentro de funciones')
def dobleFuncion(x):
    doble= x * 2
    def cuadrado(y):
        cuad= y**2
        return cuad
    print(cuadrado(doble))

dobleFuncion(5)

print('##Ejemplos de funciones ya creadas en el lenguaje')

x= 'hola que ase'
print(len(x)) # devuelve la cantidad de objetos que tiene un objeto

entero= '1991'
print(int(entero)) # convierte números de formato texto en números enteros

numbers= [4,6,8,1,22,30,13,0,108,24,7,56]
print(max(numbers)) # Retorna el elemento mayor en un iterable o el mayor de dos o más argumentos.

print('##Variables LOCALES y GLOBALES')
miVariableGlobal_1= 'Soy una variable local'

def variables():
    miVarLOCAL= 'Soy local'
    print(miVarLOCAL)
    print(miVariableGlobal_1)

variables()
# print(miVariableLOCAL) # esto produciría un error

def modificar_variable():
    global miVariableGlobal_1 # indicamos con la palabra reservada 'global' que queremos modificar a 'miVariableGlobal_1'
    miVariableGlobal_1= 'Ahora estoy modificada dentro de la función'

print(miVariableGlobal_1)
modificar_variable()
print(miVariableGlobal_1)

###DIFICULTAD EXTRA###
print('###EJERCICIO EXTRA###')

def multiplos3_5(txt1, txt2):
    count= 0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(txt1 + txt2)
        elif num % 3 == 0:
            print(txt1)
        elif num % 5 == 0:
            print(txt2)
        else:
            print(num)
            count += 1
    return count

impresos= multiplos3_5('ni', 'no')
print(f"Se han impreso {impresos} números.")