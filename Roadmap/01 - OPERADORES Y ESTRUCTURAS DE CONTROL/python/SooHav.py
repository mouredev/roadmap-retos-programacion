#01 OPERADORES Y ESTRUCTURAS DE CONTROL

#Ejemplos de operadores con Python 

# Operadores aritméticos
print(f"Adición entre los operandos: 12 + 3 = {12 + 3}")
print(f"Substracción entre los operandos: 12 - 3 = {12 - 3}")
print(f"Multiplicación entre los operandos: 12 * 3 = {12 * 3}")
print(f"División entre los operandos: 12 / 3 = {12 / 3}")
print(f"Módulo entre los operandos: 12 % 3 = {12 % 3}")
print(f"Potencia de los operandos: 12 ** 3 = {12 ** 3}")
print(f"División con resultado de número entero: 12 // 3 = {12 // 3}")

# Operadores relacionales
print(f">  Devuelve True si el operador de la izquierda es mayor que el operador de la derecha	12 > 3 = {12 > 3}")
print(f"<  Devuelve True si el operador de la derecha es mayor que el operador de la izquierda	3 < 12 = {3 < 12}")
print(f"== Devuelve True si ambos operandos son iguales	12 == 12 = {12 == 12}")
print(f">= Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha	12 >= 3 = {12 >= 3}")
print(f"=< Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda	3 <= 12 = {3 <= 12}")
print(f"!= Devuelve True si ambos operandos no son iguales 12 != 3 = {12 != 3}")

# Operadores lógicos
print(f"and - True si ambos operandos son True: 12>1 and 3<6 = {12>1 and 3<6}")
print(f"or  - True si alguno de los operandos es True: 12>1 or 3>6 = {12>1 or 3>6}")
print(f"not - True si alguno de los operandos False: not 3<6 = {not 3>6}")

# Operadores de identidad
a = 10
b = a
print(f"is     Comprueba si dos variables hacen referencia a el mismo objeto: a is b es {a is b}")
a = [1, 2, 3]
b = [1, 2, 3]
print(f"is     Comprueba si dos variables hacen referencia a el mismo objeto: a is b es {a is b}")
print(f"is not Comprueba si dos variables NO hacen referencia a el mismo objeto: a is not b es {a is b}")

# Operadores de pertenencia
a = 2
b = [1, 2, 3]
print(f"in     Comprueba si una variable se encuentra en la otra: a in b es {a in b}")
print(f"not in Comprueba si una variable no se encuentra en la otra: a in b es {a not in b}")

# Operadores con bits
print(bin(27))
# 0b11011

##Operador &
'''recorre ambos números en su representación 
binaria elemento a elemento, y hace una operación and 
con cada uno de ellos'''
a = 0b1101
b = 0b1011
print(bin(a & b)) 
#0b1001

##Operador |
'''realiza la operación or elemento a elemento con cada 
uno de los bits de los números que introducimos'''
a = 0b1101
b = 0b1011
print(bin(a | b)) 
# 0b1111

##Operador ~
'''realiza la operación not sobre cada bit del número 
que le introducimos, es decir, invierte el valor de 
cada bit, poniendo los 0 a 1 y los 1 a 0'''
a = 40
print(bin(a))
print(bin(~a)) 
0b101000
-0b101001

##Operador ^
'''realiza la función xor con cada bit de las dos variables que se le proporciona. 
Lo que hace es devolver True o 1 cuando hay al menos un valor True pero no los dos. 
Es decir, solo devuelve 1 para las combinaciones 1,0 y 0,1 y 0 para las demás.'''
x = 0b0110 ^ 0b1010 
print(bin(x))
# 0 xor 1 = 1
# 1 xor 0 = 1
# 1 xor 1 = 0
# 0 xor 0 = 0
# 0b1100

##Operador >>
'''desplaza todos los bit n unidades a la derecha '''
a=0b1000
print(bin(a>>2)) 
# 0b10

##Operador <<
'''desplaza todos los bit n unidades a la izquierda '''
a=0b0001
print(bin(a<<3)) 
# 0b1000

# Operadores de asignación
a=5 #valor asignado
print(f"=   Asignación, el valor es asignado a una variable: a es {a}")
a += 1
print(f"+=  Suma, equivale a=(a + 1): a+=1 es {a}")
a -= 2
print(f"-=  Resta, equivale a=(a - 2): a-=2 es {a}")
a *= 3
print(f"*=  Multiplicación, equivale a=(a * 3): a*=3 es {a}")
a /= 2
print(f"/=  División, equivale a=(a / 2): a/=2 es {a}")
a %= 4
print(f"%=  Modulo, equivale a=(a % 4): a%=4 es {a}")
a **= 3
print(f"**= Potencia, equivale a=(a ** 3): a**=3 es {a}")
a //= 3
print(f"//= División entera, equivale a=(a // 3): a//=2 es {a}")
a=5 #a partir de aqui requiere numeros enteros bit a bit
a &= 3
print(f"&=  Comparación & bit a bit, equivale a=(a & 3): a&=2 es {a}")
a |= 3
print(f"|=  Operador | elemento a elemento, equivale a=(a | 3): a|=3 es {a}")
a ^= 5
print(f"^=  Operador ^ elemento a elemento, equivale a=(a ^ 5): a^=5 es {a}")
a >>= 2
print(f">>= Operador >>= elemento a elemento, equivale a=(a >> 2): a>>=2 es {a}")
a <<= 5
print(f"<<= Pperador <<= elemento a elemento, equivale a=(a << 5): a<<=5 es {a}")

#Estructuras de control con Python
"""
Las estructuras de control son herramientas que nos permiten condicionar 
la ejecución del código a ciertas circunstancias. 
En Python, las estructuras de control más comunes son las condicionales y los bucles.
-Condicional if
-Bucle for
-Bucle while
-List comprehensions
-excepciones (basicas)
"""
#Condicional if/else/elif
a = 4
b = 2
if b != 0:
    c = a/b
    d = c + 1
    print(d)

x = 5
if x == 5:
    print("Es 5")
else:
    print("No es 5")

x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
else:
    print("Es otro")

x = 6
if not x%2:  #Como detectar par/impar
    print("Es par")
else:
    print("Es impar")
    
#Bucle for (range/break/continue/zip/enumerate)
for i in (0, 1, 2, 3, 4, 5):
    print(i) 

for i in range(0, 6):
    print(i)   

for i in "Python":
    print(i)

texto = "Python"
for i in texto[::-1]: #invierte
    print(i) 

for letra in texto:
    if letra == 'h':
        print("Se encontró la h")
        break #corta el bucle
    print(letra)

for letra in texto:
    if letra == 'P':
        continue #salta unelemnto y continua hasta terminar el bucle
    print(letra)

a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b) 
"""
si pasamos dos listas a zip como entrada, 
el resultado será una tupla donde cada elemento 
tendrá todos y cada uno de los elementos i-ésimos 
de las pasadas como entrada.
"""
for numero, texto in zip(a, b):
    print("Número", numero, "Letra", texto)

lista = ["A", "B", "C"]

for indice, l in enumerate(lista):  #para acceder al indice y al elemento
    print(indice, l)

#List comprenhension
"""
Las list comprehension nos permiten crear 
listas de elementos en una sola línea de código.
"""
cuadrados = [i**2 for i in range(5)]

#Bucle While (else/pop)
x = 5
while x > 0:
    x -=1
    print(x)

x = ["Uno", "Dos", "Tres"]
while x:
    x.pop(0) #pop elimina un elemnto de la lista
    print(x)        

x = 5
while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

a = 10; b = 0
try:
    c = a/b
except ZeroDivisionError: #tipo de excepción
    print("No se ha podido realizar la división")

# DIFICULTAD EXTRA (opcional):
""" Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)

numeros = [i for i in range(56) if i%2==0 and i !=16 and i%3 !=0]
print(numeros)