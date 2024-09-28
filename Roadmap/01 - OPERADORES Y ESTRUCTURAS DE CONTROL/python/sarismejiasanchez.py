# OPERADORES ARITMETICOS
"""
https://quickref.me/python.html
Un operador aritmético toma dos operandos como entrada, realiza un cálculo y devuelve el resultado.
"""
print("OPERADORES ARITMETICOS")
result = 10 + 30 # => 40
print(f"10 + 30 = {result}")
result = 40 - 10 # => 30
print(f"40 - 10 = {result}")
result = 50 * 5  # => 250
print(f"50 * 5 = {result}")
result = 16 / 4  # => 4.0 (Float Division)
print(f"16 / 4 = {result}")
result = 16 // 4 # => 4 (Integer Division)
print(f"16 // 4 = {result}")
result = 25 % 2  # => 1
print(f"25 % 2 = {result}")
result = 5 ** 3  # => 125
print(f"5 ** 3 = {result}")


# OPERADORES LOGICOS
"""
https://ellibrodepython.com/operadores-logicos
Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones. 
Los operadores lógicos utilizados en Python son  and, or y not.
"""
print("OPERADORES LOGICOS")
# AND
    # Devuelve True si ambos operandos son True
print("AND")
print(f"True and True: {True and True}")   # True
print(f"True and False: {True and False}")  # False

# OR
    # Devuelve True si alguno de los operandos es True	
print("OR")
print(f"True or True: {True or True}")   # True
print(f"True or False: {True or False}")  # True
print(f"False or True: {False or True}")  # True
print(f"False or False: {False or False}") # False
print(f"True and True and False: {True and True and False}")
#     |-----------|
#           True  and  False
#         |------------------|
#                False
print(f"False and True or True or False: {False and True or True or False}")
#     False and True = False
#               Fase or True = True
#                       True or False = True
# True

# NOT
    # Devuelve True si alguno de los operandos False
print("NOT")
print(f"not True: {not True}")  # False
print(f"not False: {not False}") # True
print(f"not not not not True: {not not not not True}") # True
print(f"not 0: {not 0}") # True
print(f"not 1: {not 1}") # False

# COMPARACION / RELACIONALES
"""
https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/
Un operador relacional se emplea para comparar y establecer la relación entre ellos. 
Devuelve un valor booleano (true o false) basado en la condición.
"""
print("COMPARACION / RELACIONALES")

"""
Mayor que (>)
Devuelve True si el operador de la izquierda es mayor que el operador de la derecha	
"""
print(f"12 > 3: {12 > 3}") # True

"""
Menor que (>)
Devuelve True si el operador de la derecha es mayor que el operador de la izquierda	
"""
print(f"12 < 3: {12 < 3}") # False

"""
Igualdad (==)
Devuelve True si ambos operandos son iguales
"""
print(f"12 == 3: {12 == 3}") # False

"""
Mayor o Igual que (>=)
Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha
"""
print(f"12 >= 3: {12 >= 3}") # True
print(f"12 >= 12: {12 >= 12}") # True
print(f"12 >= 13: {12 >= 13}") # False
"""
Menor o Igual que (<=)
Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda	
"""
print(f"12 <= 3: {12 <= 3}") # False
print(f"12 <= 12: {12 <= 12}") # True
print(f"12 <= 13: {12 <= 11}") # False
"""
Diferente (!=)
Devuelve True si ambos operandos no son iguales	
"""
print(f"12 != 3: {12 != 3}") # True
print(f"12 != 12: {12 != 12}") # False

# OPERADORES DE ASIGNACION
"""
https://ellibrodepython.com/operadores-asignacion#operadores-de-asignaci%C3%B3n
Se utiliza un operador de asignación para asignar valores a una variable. 
Esto generalmente se combina con otros operadores (como aritmética, bit a bit) 
donde la operación se realiza en los operandos y el resultado se asigna al operando izquierdo.
"""
print("OPERADORES DE ASIGNACION")
print("Operador = 5")
"""
asigna a la variable de la izquierda el contenido que le ponemos a la derecha
"""
a = 5
print(f"a = {a}") # El valor 5 es asignado a la variable a

print("Operador += 5")
"""
El operador += en a += 5 es equivalente a a=a+5. 
"""
a += 5 # es equivalente a a = a + 5
print(f"a += {a}")

print("Operador -= 5")
"""
El operador -= es equivalente a restar y asignar el resultado a la variable inicial. 
Es decir, a-=5 es equivalente a a=a-5.
"""
a -= 5 # es equivalente a a = a - 5
print(f"a -= {a}")

print("Operador *= 5")
"""
El operador *= equivale a multiplicar una variable por otra y almacenar el resultado en la primera, 
es decir a*=5 equivale a a=a*5.  
"""
a *= 5 # es equivalente a a = a * 5
print(f"a *= {a}")

print("Operador /= 5")
"""
El operador /= equivale a dividir una variable por otra y almacenar el resultado en la primera, 
es decir a/=5 equivale a a=a/5.  
"""
a /= 5 # es equivalente a a = a / 5
print(f"a /= {a}")

print("Operador %= 5")
"""
El operador %= equivale a hacer el módulo de la división de dos variables 
y almacenar su resultado en la primera.
"""
a %= 5 # es equivalente a a = a % 5
print(f"a %= {a}")

print("Operador **= 5")
"""
El operador **= realiza la operación exponente del primer número elevado al segundo, 
y almacena el resultado en la primera variable. 
El equivalente de a**=5 sería a=a**a.
"""
a **= 5 # es equivalente a a = a ** 5
print(f"a **= {a}")

print("Operador //= 5")
"""
El operador //= realiza la operación cociente entre dos variables 
y almacena el resultado en la primera. El equivalente de a//=5 sería a=a//5.
"""
a //= 5 # es equivalente a a = a // 5
print(f"a //= {a}")

print("Operador &=")
"""
El operador &= realiza la comparación & bit a bit entre dos variables y 
almacena su resultado en la primera. El equivalente de a&=1 sería a=a&1
"""
a = 0b101010
a&= 0b111111
print(bin(a)) # # 0b101010

print("Operador |=")
"""
El operador |= realiza el operador | elemento a elemento entre dos variables 
y almacena su resultado en la primera. El equivalente de x|=5 sería x=x|5
"""
a = 0b101010
a|= 0b111111
print(bin(a)) # 0b111111

print("Operador ^=")
"""
El operador ^= realiza el operador ^ elemento a elemento entre dos variables 
y almacena su resultado en la primera. El equivalente de x^=2 sería x=x^2
"""
a = 0b101010
a^= 0b111111
print(bin(a)) # 0b10101

print("Operador »=")
"""
El operador >>= es similar al operador >> pero permite almacenar el resultado en la primera variable. 
Por lo tanto x>>=3 sería equivalente a x=x>>3
"""
a = 10
a >>= 1 # 5
print(f"a >> {a}")

print("Operador «=")
"""
Muy similar al anterior, <<= aplica el operador << y almacena su contenido en la primera variable. 
El equivalente de x<<=1 sería x=x<<1
"""
a = 10     # Inicializamos a 10
a <<=1    # Desplazamos 1 a la izquierda
print(f"a << {a}") # 20


# IDENTIDAD
print("OPERADORES DE IDENTIDAD")
"""
https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/
Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.
"""
print("Operador is devuelve True si los operandos se refieren al mismo objeto. En caso contrario devuelve False.")
print("Operador is not devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.")
a = 3
b = 3  
c = 4
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"a is b: {a is b}") # True
print(f"a is not b: {a is not b}") # False
print(f"a is not c: {a is not c}") # True

x = 1
y = x
z = y
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"z is 1: {z is 1}") # True
print(f"z is x: {z is x}") # False


str1 = "FreeCodeCamp"
str2 = "FreeCodeCamp"

print(f"str1 = {str1}")
print(f"str2 = {str2}")
print(f"str1 is str2: {str1 is str2}") # True
print(f"'Code' is str2: {"Code" is str2}") # False


a = [10,20,30]
b = [10,20,30]
print(f"a = {a}")
print(f"b = {b}")
print(f"a is b: {a is b}") # muestra False (ya que las listas son objetos mutables en Python) 


# PERTENENCIA
print("OPERADORES DE PERTENENCIA")
"""
https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/
Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).
in y not in son operadores de pertenencia.
in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.
not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.
"""
a = [1, 2, 3, 4, 5]
print(f"a = {a}")
#Esta 3 en la lista a?
print(f"3 in a: {3 in a}") # Muestra True 

#No está 12 en la lista a?
print(f"12 not in a: {12 not in a}") # Muestra True

str = "Hello World"
print(f"str: {str}")

#Contiene World el string str?
print(f"'World' in str: {'World' in str}") # Muestra True

#Contiene world el string str? (nota: distingue mayúsculas y minúsculas)
print(f"'world' in str: {'world' in str}")  # Muestra False  

print(f"'code' not in str: {'code' not in str}") # Muestra True

# BITS
print("OPERADORES BIT A BIT")
"""
https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/
Un operador bit a bit realiza operaciones en los operandos bit a bit.
Consideremos a = 2 (en binario = 10) y b = 3 (en binario = 11) para los siguientes casos.
"""
a = 2 # (en binario = 10)
b = 3 # (en binario = 11)
print("""Operador & \nRealiza bit a bit la operación AND en los operandos""")
print(f"a & b: {a & b}") # = 2(Binario: 10 & 11 = 10)

print("""
Operador | \nRealiza bit a bit la operación OR en los operandos""")
print(f"a | b: {a | b}") # = 3 (Binario: 10 | 11 = 11)

print("""
Operador ^ \nRealiza bit a bit la operación XOR en los operandos""")
print(f"a ^ b: {a ^ b}") # = 1 (Binario: 10 ^ 11 = 01)

print("""
Operador ~ \nRealiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando""")
print(f"~ a: {~ a}") # = -3 (Binario: ~(00000010) = (11111101))

print("""
Operador >> 
        Realiza un desplazamiento a la derecha bit a bit.
        Desplaza los bits del operador de la izquierda a la derecha tantos bits 
        como indica el operador de la derecha""")
print(f"a >> b: {a >> b}") # = 0 (Binario: 00000010 >> 00000011 = 0)

print("""
Operador <<
        Realiza un desplazamiento a la izquierda bit a bit. 
        Desplaza los bits del operando de la izquierda a la izquierda tantos bits 
        como especifique el operador de la derecha""")
print(f"a << b: {a << b}") # 16 (Binario: 00000010 << 00000011 = 00001000)

# ESTRUCTURAS DE CONTROL
print("ESTRUCTURAS DE CONTROL")
    # CONDICIONALES
    # ITERATIVAS
    # EXCEPCIONES
"""
https://ellibrodepython.com/estructuras-control-python#estructuras-de-control-en-python
https://jorgedelossantos.github.io/apuntes-python/Estructuras%20de%20control.html#ciclo-while
Estas estructuras de control nos permiten repetir un determinado bloque de código tantas veces como queramos.
"""
print("Condicional if-elif-else")
"""
El condicional if-elif-else es una estructura de control de selección que sirve para tomar decisiones, 
basándose en la evaluación de condiciones y/o comparaciones, en el flujo del programa. 
"""
# programa que verifica si el valor de a es mayor, menor o igual al valor de b.
a = 10
b = 30
print(f"a = {a}")
print(f"b = {b}")
if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b")

# Numero par
calificacion = 150
print(f"calificacion = {calificacion}")

if calificacion < 0 or calificacion > 100:
    print("La calificación debe estar en la escala de 0 a 100")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("No aprobado")
    
print("Ciclo for")
"""
En Python, el ciclo for se utiliza para iterar sobre una secuencia 
(como una lista, tupla, cadena de caracteres, etc.) o cualquier objeto iterable. 
El formato básico del ciclo for es el siguiente:

for variable in secuencia:
    # Código que se ejecuta en cada iteración
D
onde:

variable es una variable que toma el valor de cada elemento en la secuencia en cada iteración del bucle.
secuencia es la colección de elementos sobre la cual estás iterando.

"""

numeros = [18,50,90,-20,100,80,37]
print(f"numeros = {numeros}")
for n in numeros:
    print(n)


print("Ciclo while")
"""
En Python, el ciclo while se utiliza para ejecutar un bloque de código mientras 
una condición especificada sea verdadera. Su estructura básica es la siguiente:

while condicion:
    # Código que se ejecuta mientras la condición sea verdadera

Donde:

condicion es la expresión booleana que se evalúa en cada iteración del bucle.
El bloque de código que sigue al while se ejecutará repetidamente mientras la condición sea verdadera.
Un ejemplo sencillo sería un bucle while que imprime los números del 1 al 5:
"""
numero = 1

while numero <= 5:
    print(numero)
    numero += 1


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
print("DIFICULTAD EXTRA")
for i in range(10, 56):
    if i % 2 == 0: # Pares
        if i != 16: # No es el 16
            if i % 3 != 0: # No es multiplo de 3
                print(i)

print("Optimizado")
for i in range(10, 56):
    if (i % 2 == 0 and i != 16 and i % 3 != 0):
        print(i)