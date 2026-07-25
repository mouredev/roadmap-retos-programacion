#Python cuenta con multiples operadores, a continuación se enlistan los diferentes que existen

#Operadores numericos

suma = 13 + 12
resta = 45 - 12
division = 21 / 9
multiplicacion = 12 * 89
potencia = 12 ** 12
division_entera = 45 // 6
modulo = 12 % 8

#Operadores de comparación 
igualdad = 'Hola' == 'Hola'
mayor_que = 5 > 12 #tambien existe el mayor o igual >=
menor_que = 6 < 0  #tambien existe el menor o igual <=
diferente = 'hola' != 'hola'

#operadores booleanos
y_and = True and False
o_or = (5 > 32) or ('perro' != 'gato')
no_not = not(True)

#Operaciones con strings
concatenacion = 'Hola' + ' como estas?'
repeticion = 'hola' * 3 #da 'holaholahola'

# condicionales
a = 89
b = 12

if a > b:
    print(f'El numero {a} es mayor que {b}')
elif b > a:
    print(f'El numero {a} es menor que {b}')
else:
    print('a y b son iguales')

#Ciclos

#Ciclo for
for i in range(0,10):
    pass

#Ciclo while
# while True:
#     #Hacer esto
#     pass

def operar(a,b):
    try:
        operacion = a/b
        print(a/b)
    except ZeroDivisionError:
        print("No se peude dividir entre cero")

operar(12,0)


# Ejercicio opcional
for i in range(10,56):
    if i % 2 == 0 and i != 16 and not(i % 3 == 0):
        print(i)