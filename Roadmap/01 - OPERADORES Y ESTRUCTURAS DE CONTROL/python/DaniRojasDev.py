a = 10
b = 3

'''
Operadores aritméticos
'''
print (f"10 + 4 = {a + b}") #suma
print (f"10 - 4 = {a - b}")#resta
print (f"10 x 4 = {a * b}") #multiplicación
print (f"10 / 4 = {a / b}") #división
print (f"10 % 4 = {a % b}")#módulo (muestra el resto de una división)
print (f"10 ** 4 = {a ** b}") #exponente (número de la izquierda elevado al número de la derecha)
print (f"10 // 4 = {a // b}") #cociente (muestra el cociente de la división)

'''
Operadores de comparación
'''
print (f"10 = 3 is {a==b}") # Igualdad
print (f"10 is diferent than 3 is {a!=b}") # Desigualdad
print (f"10 is greater than 3 is {a>b}") # Mayor que
print (f"10 is less than 3 is {a<b}") # Menor que
print (f"10 is greater or equal than 3 is {a>=b}") # Mayor o igual que
print (f"3 is less or equal than 10 is {b<=a}") # Menor o igual que

'''
Operadores lógicos
'''
# operador "and"
print (f"10+3 = 13 y 10-3 = 7 is {a+b==13 and a-b==7}") # Si ambas operaciones son verdad es true, si no false
print (f"10+3 = 13 y 10-3 = 7 is {a+b==12 and a-b==7}") # Si ambas operaciones son verdad es true, si no false

# operador "or"
print (f"10+3 = 13 y 10-3 = 7 is {a+b==13 or a-b==7}") # Si una de las operaciones es verdad es true, si no false
print (f"10+3 = 13 y 10-3 = 7 is {a+b==12 or a-b==7}") # Si una de las operaciones es verdad es true, si no false
print (f"10+3 = 13 y 10-3 = 7 is {a+b==12 or a-b==7}") # Si una de las operaciones es verdad es true, si no false

# operador "not"
print (f"10+3 = 13 is not {not a+b == 13 }") # Si una de las operaciones es verdad es false, si no true (invierte true por false)

'''
Operadores de asignación
'''

# Asigna un valor a la constante y le realiza la operación

number = 7 # Asignación
print (number)

number += 2 # Suma el valor y asigna
print (number)

number -= 2 # Resta el valor y asigna
print (number)

number *= 2 # Multiplica el valor y asigna
print (number)

number /= 2 # Divide el valor y asigna
print (number)

number %= 2 # Modula el valor y asigna
print (number)

number //= 2 # Saca el cociente de la división y asigna
print (number)

number **= 2 # Eleva el valor por el número que se le da y asigna
print (number)

'''
Operadores de identidad
'''

print (f"the number a is the number b {a is b}") # Dice si ambos valores son el mismo
print (f"the number a is the number b {a is not b}") # Dice si ambos valores no son el mismo

'''
Operadores de identidad
'''
print (f"Hello is in Hello, Python!! {'Hello' in 'Hello, Python!!'}") # Sale true si Hello esta dentro de Hello, Python!!
print (f"Hola isn´t Hello, Python!! {'Hola' not in 'Hello, Python!!'}") # Sale true si hola  no esta dentro de Hello, Python!!

'''
Operadores de bit
'''
# Sirven para trabajar con números en binario 
print (f"The number 10 in binary is {bin (10)}")
print (f"The number 3 in binary is {bin (3)}")

print (f"AND: 10 & 3 = {10 & 3}")
print (f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")

'''
Estructuras de control condicionales
'''
# Si se cumple la condición imprime una cosa en cosa en caso contrario imprime otra

string = "Hola"

if string == "Hello":
    print ("string is Hello")
else:
    print ("string ins´t Hello")

# si se cumple la primera condición imprime una cosa, si no, comprueba la segunda condición y si se cumple imprime otra, si no se cumple ninguna de las 2 imprime otra

if string == "Hello":
    print ("string is Hello")
elif string == "Hola":
    print ("string is Hola")
else:
    print ("string ins´t Hello")

'''
Estructuras de control iterativas
'''
# Coge los números de un rango que le indiquemos desde el 0 hasta un número menos del indicado

for c in range (11):
    print (c)

# Ejecuta el codigo repetidas veces hasta que se cumple la condición que le indiquemos en este caso mientras sea mayor de 0

while c >0:
    c -=1
    print (c)

'''
Estructuras de control de excepciones
'''
# Intenta realizar la operación si se puede la realiza y si no se puede, en lugar de dar error el programa, nos sale el mensaje que le indiquemos y el programa sigue corriendo
try:
    print(10 / 0)
except:
    print("Se ha producido un error")

'''
Extra
'''
print ("Esta es la parte extra del ejercicio")

for d in range (10, 56):
    if d % 2 == 0 and d !=16 and d % 3 != 0:
        print (d)




