# 01 - OPERADORES Y ESTRUCTURAS DE CONTROL

## 1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...(Ten en cuenta que cada lenguaje puede poseer unos diferentes)


### Operadores Aritméticos : permiten realizar operaciones aritméticas y devolver su resultado.
#-----------------------------------------------------------------------------
x = 2; y = 3
print("Operadores aritméticos")
print("x+y =", x+y)   # operador +  (suma)
print("x-y =", x-y)   # operador -  (resta)
print("x*y =", x*y)   # operador * (multiplicación)
print("x/y =", x/y)   # operador / (dividion)
print("x%y =", x%y)   # opoerador % (modulo)
print("x**y =", x**y) # operador ** (potencia)
print("x//y =", x//y)  # operador // (división entera)

# Nota: el orden de prioridad de losoperadores aritméticos es el siguiente: 
# () Parentesis, 
# ** Potencia, 
# -x Negacion, 
# * / // % Multiplicación, División, Cociente, Módulo
# + - Suma, Resta



### Operadores de Asignación : permiten realizar una operacion y asignar el resultado a una variable.
#-----------------------------------------------------------------------------
# Operador  = asigna un valor a una variable
# Operador += equivalente a sumar y asignar el resultado a la variable inicial.
# Operador -= equivalente a restar y asignar el resultado a la variable inicial.
# Operador *= equivale a multiplicar una variable por otra y almacenar el resultado en la primera.
# Operador /= equivale a dividir una variable por otra y almacenar el resultado en la primera.
# Operador %= equivale a hacer el módulo de la división de dos variables y almacenar su resultado en la primera.
# Operador //= la operación cociente entre dos variables y almacena el resultado en la primera.
# Operador **= equivale  a realiza la operación exponente del primer número elevado al segundo, y almacena el resultado en la primera variable.
# Operador &= equivale  a realiza la operación AND entre dos variables y almacena el resultado en la primera variable.

a=2; b=3
print("Operadores de asignación")
x=a; x+=b;  print("x+=", x) #5
x=a; x-=b;  print("x-=", x) #-1
x=a; x*=b;  print("x*=", x) #6
x=a; x/=b;  print("x/=", x) #0.6666666666666666
x=a; x%=b;  print("x%=", x) #2
x=a; x//=b; print("x//=", x) #0
x=a; x**=b; print("x**=", x) #8
x=a; x&=b;  print("x&=", x) #2 
x=a; x|=b;  print("x|=", x) #3


### Operadores Relacionales : permiten realizar operaciones de comparación y devolver True o False.
#-----------------------------------------------------------------------------
x=2; y=3
print("Operadores Relacionales")
print("x==y =", x==y) # False  Operador de comparación (igualdad)
print("x!=y =", x!=y) # True   Operador de comparación (desigualdad)
print("x>y  =", x>y)  # False  Operador de comparación (mayor que)
print("x<y  =", x<y)  # True   Operador de comparación (menor que)
print("x>=y =", x>=y) # False  Operador de comparación (mayor o igual que)
print("x<=y =", x<=y) # True   Operador de comparación (menor o igual que)


### Operadores Lógicos : permiten realizar operaciones logicas y devolver True o False.
#-----------------------------------------------------------------------------
# and   Devuelve True si ambos elementos son True	            True and True = True
# or	Devuelve True si al menos un elemento es True	        True or False = True
# not	Devuelve el contrario, True si es Falso y viceversa	     not True = False


# AND: 
#El operador and evalúa si el valor a la izquierda y el de la derecha son True, y en el caso de ser cierto, devuelve True. Si uno de los dos valores es False, el resultado 
# será False.
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False


# OR:
# El operador or devuelve True cuando al menos uno de los elementos es igual a True. Es decir, evalúa si el valor a la izquierda o el de la derecha son True.

print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False


# NOT:
# El operador not devuelve el opuesto de un valor. Es decir, True se convierte en False y False se convierte en True.
print(not True)  # False
print(not False) # True
print(not not not not True) # True

# Se puede usar 0 y 1 para representar False y True respectivamente. 
print(not 0) # True
print(not 1) # False


# Nota: el orden de aplicación de los operadores puede influir en el resultado. De mayor a menor prioridad: not, and y or.
print(False and False or True) # True
print(True or False and False) # True
print(0 and not 1 or 1 and not 0 or 1 and 0) #(False and False or True and True or True and False) --> # True


# Operadores de Identidad: permiten comprobar si dos variables hacen referencia al mismo objeto, devolviendo True en el cado  de ser cierto.
#-----------------------------------------------------------------------------
# is	    Devuelve True si hacen referencia a el mismo objeto
# is not	Devuelve False si no hacen referencia a el mismo objeto

a = 10 ; b = 10 ; print(a is b) # True
# La funcion id() Devuelve el identificador único de un objeto. Ambos apuntan a la misma ubicación en memoria al ser el mismo valor.
print(id(a)) # 9756512  Este valor es la dirección de memoria del objeto
print(id(b)) # 9756512  Este valor es la dirección de memoria del objeto

a = 10 ; b = 10 ; print(a is not b) # False --> ambas variables apuntan a el mismo objeto.
a = 10 ; b = 20 ; print(a is not b) # True --> las variables no apuntan a el mismo objeto.


# Operadores de pertenecia: permiten comprobar si un objeto pertenece a una secuencia ( lista, tupla , conjunto o cadena), devolviendo True en el caso de ser cierto.
#-----------------------------------------------------------------------------
# in	    Devuelve True si el objeto pertenece a la secuencia
# not in	Devuelve False si el objeto no pertenece a la secuencia

a = 10  ; print(a in [10,20,30]) # True
a = 50  ; print(a in [10,20,30]) # False
print([1, 2] in [4, [1, 2], 7]) # True
print(3 not in [1, 2, 4, 5]) # True
x = ["apple", "banana"] ; print("banana" in x) # True
print('s' in 'perro') # False


# Operadores de bitwise
#-----------------------------------------------------------------------------
# AND (&)	Realiza una operación AND bit a bit  --> Compara cada bit de dos operandos y devuelve 1 si ambos bits son 1, de lo contrario devuelve 0.
a = 4 ; bin_a = bin(a)
b = 5; bin_b = bin(b)

print(f"AND: {bin_a} & {bin_b} = {bin(a & b)}")

# OR (|)	Realiza una operación OR bit a bit --> compara cada bit de dos operandos y devuelve 1 si al menos uno de los bits es 1.
print(f"OR: {bin_a} | {bin_b} = {bin(a | b)}")

# NOT (~)	Realiza una operación NOT bit a bit --> ealiza la operación not sobre cada bit del número que le introducimos, es decir, invierte el valor de cada bit, 
# poniendo los 0 a 1 y los 1 a 0. El comportamiento en Python puede ser algo distinto del esperado. En realidad  ~a sería -a-1

print(f"NOT: ~{bin_a} = {bin(~a)}")

# XOR (^)	Realiza una operación XOR bit a bit -->  compara cada bit de dos operandos y devuelve 1 si exactamente uno de los bits es 1, pero no ambos.
print(f"XOR: {bin_a} ^ {bin_b} = {bin(a ^ b)}")

# Operadores de Desplazamiento:Los operadores de desplazamiento mueven los bits de un número hacia la izquierda (<<) o hacia la derecha (>>) en la cantidad especificada.
#-----------------------------------------------------------------------------

# Desplazamiento Derecha (>>)	Desplaza los bits a la derecha

print(f'{bin_a} >> 2  = {bin(a>>2)}')
print(f'{bin_b} >> 2  = {bin(b>>2)}')

# Desplazamiento Izquierda (<<)	Desplaza los bits a la izquierda

print(f'{bin_a} << 2  = {bin(a<<2)}')
print(f'{bin_b} << 2  = {bin(b<<2)}')


## 2. Utilizando las operaciones con operadores que tú quieras, crea ejemplos:
# que representen todos los tipos de estructuras de control que existan en tu lenguaje:
# Condicionales, iterativas, excepciones...

## Estrcuturas de control
# Condicionales

# If-elif-else
def grupo_edad(edad):
    if edad <=0:  
        print('la edad no puede ser negativa, ni igual a 0')  
    elif 0 > edad <=3:
        print('bebe')
    elif 4 >= edad <=12:
        print('niño')
    elif 13 >= edad <=17:
        print('adolescente')
    elif 18>= edad <=60:
        print('adulto')
    else:
        print('mayor de 60')

grupo_edad(-5)
grupo_edad(0)
grupo_edad(4)
grupo_edad(17)
grupo_edad(25)
grupo_edad(80)


# Iterativas
for i in range(5):
    print(i)


# Ciclos anidados
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(item)


x = 3
while x > 0: 
    x -=1
    print(x)   

# Excepciones
# Una excepción es un evento inesperado que ocurre durante la ejecución del programa.
# Control de excepciones: try, except, else, finally.

"""
Principales tipos de excepciones:
* TypeError : Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.
* ZeroDivisionError : Ocurre cuando se itenta dividir por cero.
* OverflowError : Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
* IndexError : Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
* KeyError : Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
* FileNotFoundError : Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
* ImportError : Ocurre cuando falla la importación de un módulo.

"""

def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)
    except TypeError as e:
        print('catch TypeError:', e)
    else:
        print("result is", result)
    finally:
        print("'This is always executed'")

division(10, 0)
division('a', 'b')
division(12, 3)


## 3. Debes hacer print por consola del resultado de todos los ejemplos.

##DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
# Resultado : 10, 14, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52


# solucion 1
print("Solucion 1")
for i in range(10, 56,2):
    if i != 16 and i % 3 != 0:
        print(i)
    

# solucion 2
print("Solucion 2")
for i in range(10, 56):
    if i%2 == 0 and i != 16 and i % 3 != 0:
        print(i)
    