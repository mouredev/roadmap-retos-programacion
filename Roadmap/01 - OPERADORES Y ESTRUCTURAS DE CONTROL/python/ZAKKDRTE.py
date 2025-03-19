##01 - OPERADORES Y ESTRUCTURAS DE CONTROL
"""
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

"""

# Operadores Aritmeticos #
print(20 + 10)  # Suma
print(20 - 10)  # Resta
print(20 * 10)  # Multiplicacion
print(20 / 10)  # Dvision con resultado float
print(20 // 10) # Division con resultado entero
print(20 ** 2)  # Exponentes
print(20 % 10)  # Residuo

# Operadores Logicos #
print(True or False)    # Devuelve True 
print(True and False)   # Devuelve False
print(not( True or False))  # Devuelve False 
print(not(True and False))  # Devuelve True

# Operadores de Comparacion
print(5 < 10)   # Devuelve True porque 5 es menor que 10
print(5 <= 10)  # Devuelve True porque 5 es menor que 10    *NOTA* Este da True si es menor o igual
print(5 > 10)   # Devuelve False porque 5 no es mayor que 10
print(5 >= 10)  # Devuelve False porque 5 no es mayor que 10    *NOTA* Este da True si es mayor o igual
print(5 == 10)  # Devuelve False porque 5 no es igual que 10
print(5 != 10)  # Devuelve True porque 5 es diferente que 10

# Operadores de asignacion #
a = 5   # Se le asigna valor igual a 5
print(a)
a += 10 # Se le asigna un +10 y da como resultado 15
print(a)
a -= 10 # Se le asigna un -10 y da como resultado 5
print(a)
a *= 10 # Se le asigna un *10 y da como resultado 50
print(a)
a //= 5 # Se le asigna un //5 y da como resultado 10 sin float
print(a)
a **= 2 # Se le asigna un exponente 2 y da como resultado 100
print(a)
a /= 2  # Se le asigna un /5 y da como resultado 50.0 con float
print(a)
a %= 9  # Se le asigna un %9 y da como resultado 5.0
print(a)

# Operadores de Identidad #
    ## Este operadores es boolean y devuelve True si ambos operandos apuntan al mismo objeto de memoria ##
a = 5
b = 5
c = 3

print(a is b)   # Devuelve True
print(a is not b)   # Devuelve False
print(a is c)   # Devuelve False
print(a is not c)   # Devuelve True

# Operadores de Pertenencia #
list = [1, 2, 3, 4, 5]

print(3 in list)    # Devuelve True
print(6 in list)    # Devuelve False
print(3 not in list)    # Devuelve False
print(6 not in list)    # Devuelve True

# bits
## Se hace uso de las tablas de la verdad ##
a = 5    # Representación binaria: 0b0101
b = 3    # Representación binaria: 0b0011
print(a & b ) # Resultado: 0b0001 (1 en binario)
a = 5    # Representación binaria: 0b0101
b = 3    # Representación binaria: 0b0011
print(a | b ) # Resultado: 0b0111 (7 en binario)
a = 5    # Representación binaria: 0b0101
b = 3    # Representación binaria: 0b0011
print(a ^ b)  # Resultado: 0b0110 (6 en binario)
a = 5    # Representación binaria: 0b0101
print(~a ) # Resultado: Dependiente de la representación en complemento a dos, en este caso, -6
a = 5    # Representación binaria: 0b0101
print(a << 1 ) # Resultado: 0b1010 (10 en binario)
a = 5    # Representación binaria: 0b0101
print(a >> 1)  # Resultado: 0b0010 (2 en binario)

# Estructuras de Control #
num = 0

while num < 11:
    if num < 10:
        print("Es menor que 10")
        num += 1
    elif num == 10:
        print("Es igual a 10")
        num += 1
    else:
        break

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

try:
    resultado = 10 / 0
except Exception as e:
    print(f"Se produjo una excepción: {type(e).__name__}")



# Ejercicio Extra #



def nums():
    for i in range(10, 56):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i)

nums()