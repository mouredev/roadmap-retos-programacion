
#Tipos de operadores del lenguaje python

"Aritmeticos"

#suma 
resultado_suma = 5+3
print("El resultado de la suma es:",resultado_suma)

#Resta
resultado_resta = 5-3
print("El resultado de la resta es:",resultado_resta)

#multiplicación 
resultado_multiplicación = 5*3
print("El resultado de la multiplicación es:",resultado_multiplicación)

#División entera y decimal
resultado_division = 8/2
print("El resultado de la division es:", resultado_division)

#Division entera
division_entera = 10//5
print("El resultado de la division entera es:",division_entera)

#Modulo o residuo de una operacion 
modulo = 9%2
print("El residuo de la operacion es:",modulo)

#Exponenciacion o elevar a 
potencia = 4**2
print("El resultado del numero elevado es:",potencia)

"Logicos"

#and Este operador devuelve True si ambos operandos son verdaderos. Si uno de los operandos es falso, devuelve False.
a = False
b = True
resultado = a and b
print("El resultado es:", resultado)

#or Este operador devuelve True si al menos uno de los operandos es verdadero. Si ambos operandos son falsos, devuelve False.
resultado1 = a or b
print("El resultado es",resultado1)

#not Este operador invierte el valor booleano del operando. Si el operando es True, devuelve False, y si el operando es False, devuelve True.
variable = not False
print ("La variable no es falsa sino:",variable)

"Operadores de comparacion"

#igual Comprueba si los valores de dos operandos son iguales.
a=5
b=5
print("¿5 es igual a 5?",a==b)

#Distinto de. Comprueba si los valores de dos operandos no son iguales.
c=6
d=5
print(c != d)

#Mayor que. Comprueba si el valor del operando de la izquierda es mayor que el valor del operando de la derecha.
print(c > d)

#Menor que. Comprueba si el valor del operando de la izquierda es menor que el valor del operando de la derecha.
print(d < c)

#Mayor o igual que. Comprueba si el valor del operando de la izquierda es mayor o igual que el valor del operando de la derecha.
print (c >= d)

#Menor o igual que.
print(d <= c)




