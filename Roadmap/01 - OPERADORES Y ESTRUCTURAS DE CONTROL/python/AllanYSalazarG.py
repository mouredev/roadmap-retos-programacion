"""#01 OPERADORES Y ESTRUCTURAS DE CONTROL"""

numero1 = 2
numero2 = 4

# Aritmeticos
suma = numero1 + numero2  # Suma los valores
resta = numero1 - numero2  # Resta los valores
multiplicacion = numero1 * numero2  # Multiplica los valores
division = numero1 / numero2  # Divide los valores, regresando un float siempre
# Divide los valores, regresando un int siempre (descarga el decimal)
divisionEntera = numero1 // numero2
modulo = numero1 % numero2  # Divide los valores y regresa el residuo
potencia = numero1 ** numero2  # b ^ e Multiplica la b, e veces por si misma

# Relacional, comparacion (Devuelve True o False basado en la expresión)
# > indica si el numero de la izquierda es mayor que el de la derecha
mayorQue = numero1 > numero2
# < indica si el numero de la izquierda es menor que el de la derecha
menorQue = numero1 < numero2
igualQue = numero1 == numero2  # == indica si ambos valores son iguales
# >= indica si el valor de la izquierda es mayor o igual que el de la derecha
mayorIgualQue = numero1 >= numero2
# <= indica si el valor de la izquierda es menor o igual que el de la derecha
menorIgualQue = numero1 <= numero2
diferenteDe = numero1 != numero2  # != indica si los valores son diferentes

# Operadores Bit a Bit
AND = numero1 & numero2  # Hace la operacion AND
OR = numero1 | numero2  # Hace la operacion OR
XOR = numero1 ^ numero2  # Hace la operacion XOR
cejilla = ~numero1  # Hace la operacion NOT
despDer = numero1 >> numero2  # Desplaza a la derecha
despIzq = numero1 << numero2  # Desplaza a la izquierda

# Estos dos ultimos dezplazan a la izquierda o a la derecha los bits del operador de la izquierda
# tantos bits como indica el operando de la derecha

# Operadores de asignación
""" 
= : a = 1: El valor 1 se asigna a la variable a
Todos los demás, equivalen "a = a + 1" (cambiando el operador)
+=: a += 1
-=: a -= 1
*=: a *= 1
/=: a /= 1
%=: a %= 1
**=: a **= 1
//=: a //= 1
&=: a &= 1
|=: a |= 1
^=: a ^= 1
>>=: a >>= 1
<<=: a <<= 1
"""

# Operadores logicos
""" and: Devuelve True si ambos operandos son True: a and b
or: Devuelve True si al menos un operando es True: a or b
not: Devuelve True si alguno de los operandos es False: not a"""

# Operadores de pertenencia
""" in: Devuelve True si el valor especificado se encuentra en la secuencia
not in: Devuelve True si el valor no se encuentra en la secuencia """

a = [1, 2, 3]
print(3 in a)  # Muestra True
print(4 not in a)  # Muestra True

# Estructuras de control

# IF, ELIF, ELSE

if numero1 > numero2:
    print(f"{numero1} es mayor")
else:
    print(f"{numero2} es mayor")

# FOR

for numero in range(2):
    print(numero)

# WHILE
contador = 0
while contador < 5:
    print(contador, end=" -> ")
    contador += 1

# Comprension de Listas

listaNumeros = [a for a in range(1, 5)]
print(listaNumeros)

# Sentencias de control de bucles (break, continue y pass)

"""
break: se usa para finalizar el ciclo
continue: se usa para saltar a la siguiente iteración
pass: no hace nada, sirve como marcador de posición"""

# EJERCICIO OPCIONAL
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for valor in range(10, 56):
    if valor == 55:
        print(valor)
    if valor != 16:
        if valor % 3 != 0:
            if valor % 2 == 0:
                print(valor, end=" ")
