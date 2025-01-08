#Operadores aritméticos: +, -, *, /, %
suma = (7 + 5)
resta = (10 - 8)
multiplicacion = (3 * 9)
division = (21 / 2)
divisionEntera = (21 // 2) #Devuelve solo la parte entera de la división
modulo = (21 % 2) #Devuelve el resto de la división (en este caso, 1)
potencia = (2 ** 5) #Imprime el numero de la izquierda elevado al de la derecha

#Operadores de asignación y comparación: =, !=, <, >, ==
asignacion = 1 #El simbolo '=' se usa para asignar valores a las variables
print(9==3) #El '==' se utiliza para comparar la igualdad entre valores (devolviendo verdadero o falso)
print(9!=3) #El '!=' se utiliza para comparar si existe diferencia entre dos valores (devolviendo verdadero o falso)
print(9<3) #El '<' devuelve true cuando el valor a su izq es menor
print(9>3) #El '>' devuelve true cuando el valor a su izq es mayor

#Operadores lógicos: and, or, not
print(True and False) #Con 'and' evaluamos si se cumplen dos o más condiciones
print(True or False) #Con 'or' evaluamos si se cumple al menos una condición
print(not True) #Con 'not' negamos/revertimos una condición

#Operadores de identidad: is, is not
#Estos operadores se utilizan para saber si dos variables apuntan o no al mismo objeto en memoria
first = 10
second = 10
third = first
print(first is second)
print(first is not second)
print(first is third)
print(first is not third)

#Operadores de pertenencia: in, not in
#Estos operadores se utilizan para saber si un valor esta presente en un conjunto de datos (string, arrays, etc)
palabra = "Operadores"
print("u" in palabra)
print(not "u" in palabra)

#Estructuras de control
#If-Else, se utiliza para seguir por un camino u otro en base a una condición
number = 10
if number > 10:
    print("El numero es mayor que 10")
elif number == 10:
    print("El numero es 10")
else:
    print("El numero es menor que 10")

#Estructuras de repetición
#For, se utiliza para ejecutar instrucciones en bucle una cantidad de veces determinada

for i in range(10):
    print(i)

#While, se utiliza para ejecutar instrucciones en bucle una cantidad de veces indeterminada (por lo general hasta cumplir cierta condición)
userInput = int(input("Ingrese un numero para ver su doble, o '0' para finalizar: "))
while userInput != 0:
    print(userInput*2)
    userInput = int(input("Ingrese un numero para ver su doble, o '0' para finalizar: "))

#Estructuras de excepciones
try:
    print(19 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Fin del manejo de excepciones")

#EJERCICIO EXTRA

for value in range(10, 56):
    if (value%2 == 0) and (value%3 != 0) and (value != 16):
        print(value)

print("Fin del programa")