# EJERCICIO:

# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
x = 5
y = 3
z = (8, 9)
print(x, y)

# Arithmetic operators
addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
exponentiation = x ** y
floorDivision = x // y
print('ARITHMETIC OPERATORS')
print('addition = ', {addition})
print('subtraction = ', {subtraction})
print('multiplication = ', {multiplication})
print('division = ', {division})
print('modulus = ', {modulus})
print('exponentiation = ', {exponentiation})
print('floorDivision = ', {floorDivision})
print()

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Assignment operators
print('ASSIGNMENT OPERATORS')
print('x =', x)
print('x +=', x)
print('x -=', x)
print('x *=', x)
print('x /=', x)
print('x %=', x)
print('x //', x)
print('x **', x)
print('x &=', x)
print('x |=', x)
print('x ^=', x)
print('x >>=', x)
print('x <<=', x)
print('x :=', x)
print()

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Comparison operators
print('COMPARISON OPERATORS')
print('equal:	x == y = ',x == y)
print('not equal:	x != y = ',x != y)
print('greater than:	x > y = ',x > y)
print('less than:	x < y = ',x < y)
print('greater than or equal:	x >= y = ',x >= y)
print('less than or equal:	x <= y = ',x <= y)
print()

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Logical operators
print('LOGICAL OPERATORS')
print('and: x < 3 and y > 5 = ',x < 3 and y > 5)
print('or: x < 3 or y > 5 = ',x < 3 or y > 5)
print('not: x < 3 not y > 5 = ',not(x < 3 and y > 5))
print()

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Identity operators
print('IDENTITY OPERATORS')
print('is: x is y = ',x is y)
print('is not: x is not y = ',x is not y)
print()

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Membership operators
print('MEMBERSHIP OPERATORS')
print('in: x in y = ',8 in z)
print('not in: x not in y = ',7 not in z)
print()

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Bitwise operators
print('BITWISE OPERATORS')
print('AND: x & y =', x & y)
print('OR: x | y =', x | y)
print('XOR: x ^ y =', x ^ y)
print('NOT: ~y =', ~y)
print('<<: x << 2 =', x << 2)
print('>>: x >> 2 =', x >> 2)
print()

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------




# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...
print('IF-ELIF-ELSE')
if x >=5:
	print('Good job!')
elif x > 0:
	print('Try again')
else:
	print('Repeat the lesson')
print()

print('FOR LOOP')
worker1 = 'Ben'
worker2 = 'John'
worker3 = 'Suzy'
worker4 = 'Vanessa'
team = [worker1, worker2, worker3, worker4]
for worker in team:
	print(worker)
print()

print('WHILE LOOP')
x = 1
while x < 5:
    print(x)
    x += 1
print()


# - Debes hacer print por consola del resultado de todos los ejemplos.


# DIFICULTAD EXTRA (opcional): Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
numero = 10
while numero <= 55:
    if numero == 16:
        pass
    elif numero % 3 == 0:
        pass
    elif numero % 2 == 0:
        print(numero)
    else:
        pass
  
    numero += 1

# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
