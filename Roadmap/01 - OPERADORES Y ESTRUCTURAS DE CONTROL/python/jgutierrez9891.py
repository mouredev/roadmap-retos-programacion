# #01 OPERADORES Y ESTRUCTURAS DE CONTROL - SOLUCION

# Arithmetic operators
op_suma = 3 + 5
print ("Operador suma: 3 + 5 = " + str(op_suma))

op_resta = 10 - 3
print ("Operador resta: 10 - 3 = " + str(op_resta))

op_multiplicacion = 3 * 2
print ("Operador multiplicacion: 3 * 2 = " + str(op_multiplicacion))

op_division = 9 / 2
print ("Operador division: 9 / 2 = " + str(op_division))

op_exponente = 2**4
print ("Operador exponente: 2**4 = " + str(op_exponente))

op_modulo = 7 % 2
print ("Operador módulo: 7 % 2 = " + str(op_modulo))

op_division_entera = 9 // 2
print ("Operador division entera: 9 // 2 = " + str(op_division_entera))

# Logic operators

op_NOT = not True
print ("Operador NOT: not True = " + str(op_NOT))

op_AND = 3 > 2 and 2 < 8
print ("Operador AND: 3 > 2 and 2 < 8 = " + str(op_AND))

op_OR = 3 < 2 and 2 > 8
print ("Operador OR: 3 < 2 and 2 > 8 = " + str(op_OR))

# Comparison operators

op_mayor_que = 3 > 2
print ("Operador mayor que: 3 > 2 = " + str(op_mayor_que))

op_menor_que = 3 < 2
print ("Operador menor que: 3 < 2 = " + str(op_menor_que))

op_igualdad = 3==3
print ("Operador igualdad: 3 == 3 = " + str(op_igualdad))

op_diferente = 4 != 41
print ("Operador diferente: 4 != 41 = " + str(op_diferente))

op_menor_igual = 4 <= 4.1
print ("Operador menor o igual: 4 <= 4.1 = " + str(op_menor_igual))

op_mayor_igual = 4.2 >= 4.1
print ("Operador mayor o igual: 4.2 >= 4.1 = " + str(op_mayor_igual))

# Assignment operators

x = 5; x += 1
print ("Operador 5+=1 => " + str(x))

x = 5; x -= 2
print ("Operador 5-=2 => " + str(x))

x = 5; x *= 8
print ("Operador 5*=8 => " + str(x))

x = 5; x /= 3
print ("Operador 5/=3 => " + str(x))

x = 5; x %= 3
print ("Operador 5%=3 => " + str(x))

x = 5; x //= 2
print ("Operador 5//=2 => " + str(x))

x = 5; x **= 2
print ("Operador 5**=2 => " + str(x))

x = 5; x &= 2
print ("Operador 5&=2 => " + str(x))

x = 5; x |= 2
print ("Operador 5|=2 => " + str(x))

x = 5; x ^= 2
print ("Operador 5^=2 => " + str(x))

x = 5; x >>= 2
print ("Operador 5>>=2 => " + str(x))

# Identity operators

print ("Operador is: " + str(4 is 3))
print ("Operador is not: " + str(4 is not 3))

# Conditional structures

#if
if 3 < 5:
    print("Condición if se cumple")

#if-else
if 3 > 5:
    print("Condición if se cumple")
else:
    print("Condición no se cumple")

#if-elif-else
if 5 - 2 < 3:
    print("Condición if se cumple")
elif 5 - 3 < 3:
    print("Condición elif se cumple")
else:
    print("Condición no se cumple")

# Iterative structures

# while

x = 10
while x > 5:
    x-=1
    print("x es igual a: " + str(x))

# for

brands = ['apple', 'BMW', 'Ford', 'Nvidia', 'BYD', 'MacDonalds', 'Dior']
for i in brands:
    print ("La marca actual es: " + i)
    if i == 'MacDonalds':
        break

# Exceptions

a = 5; b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("No se ha podido realizar la división")
except Exception:
    print("Ha saltado una excepción diferente")

# Opcional

for i in range(10,56):
    if i  % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)