from random import randint
# #01 OPERADORES Y ESTRUCTURAS DE CONTROL

## EJERCICIO

# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

n1 = randint(1,10)
n2 = randint(1,10)

## ARITMETICOS

suma = 1 + 1
print (f"la suma es {suma}")
resta = 5 - 3
print (f"la resta es {resta}")
multiplicacion = 4 * 6
print (f"la multiplicacion es {multiplicacion}")
division = 10 / 2
print (f"la division es {division}")
exponente = 2 ** 3
print (f"el exponente es {exponente}")
modulo = 17 % 5
print (f"el modulo es {modulo}")
raizcuadradra = 85 ** 2
print (f"la raiz cuadrada es {raizcuadradra}")
raizcubica = 27 ** (1/3)
print (f"la raiz cubica es {raizcubica}")
potencia = 2 ** 3
print (f"la potencia es {potencia}")
factorial = 5 * 4 * 3 * 2 * 1
print (f"el factorial es {factorial}")

## LOGICOS

print (2==2 and 1==1)
print (3==2 or 1==1)
print (not 7==7)

## COMPARACION

print ("Igualdad 1==1", 1 == 1)
print ("Desigualdad a != b es", 'a' != 'b')
print ("Mayor 7 > 3 es", 7 >3)
print ("Menor 5 < 7 es", 5<7)
print ("Mayor o igual 7 >= 7 es", 7>=7)
print ("Menor o igual 7 <= 7 es", 7<=7)

## ASIGNACION

a = 5
print (f"El valor de a es {a}")
a += 1
print (f"El valor de a es {a}")
a -= 1
print (f"El valor de a es {a}")
a *= 2
print (f"El valor de a es {a}")
a /= 2
print (f"El valor de a es {a}")
a %= 3
print (f"El valor de a es {a}")
a **= 2
print (f"El valor de a es {a}")
a //= 2
print (f"El valor de a es {a}")

## IDENTIDAD

a = 4
b = 7
c = 4
print (a is c)
print (a is not b)

## PERTENENCIA

a = [1,2,3,4,8,16]
print (3 in a)
print (9 not in a)

## BIT A BIT

x = bin(10)
print (x)

a = int('0b1011001', 2)
b = int('0b1001000', 2)
print ("a: ", a, bin(a))
print ("b: ", b, bin(b))

x = (a & b)
print ("x: ", x, bin(x), "a & b")

x = (a | b)
print ("x: ", x, bin(x), "a | b")

x = (a ^ b)
print ("x: ", x, bin(x), "a ^ b")

x = (~a)
print ("x: ", x, bin(x), "~a")

x = (~b)
print ("x: ", x, bin(x), "~b")

x = (a << 2)
print ("x: ", x, bin(x), "a << 2")

x = (a >> 2)
print ("x: ", x, bin(x), "a >> 2")

### - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
# que representen todos los tipos de estructuras de control que existan
# en tu lenguaje: Condicionales, iterativas, excepciones...

## CONDICIONALES

clasificacion = randint(1,101)

if clasificacion >= 51:
    print("aprobado")
elif clasificacion == 50:
    print("aprobado pero deberias mejorar")
else:
    print("suspenso")

## ITERATIVAS

n = [1,25,-65,1001,5555]

for i in n:
    print(i)

nombre = "Alberto"
k = 0
while k < len(nombre):
    print (nombre[k])
    k += 1

## EXCEPCIONES

a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese otro numero entero: "))

try:
    c = a / b
except ZeroDivisionError:
    print("No se puede dividir por cero")

### DIFICULTAD EXTRA
#
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)  
    else:
        print("No hay numeros que cumplan con la condicion")