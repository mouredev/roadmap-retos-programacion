from re import match


var1 = 5
var2 = 3

print("OPERADORES EN PYTHON")
print("1. Variables")
print("1.1 'var1' =", var1)
print("1.2 'var2' =", var2)
print("_____________________________")

print("2. Operadores aritméticos")
print("2.1 'suma' 5+3 =", var1 + var2)
print("2.2 'resta' 5-3 =", var1 - var2)
print("2.3 'multiplicación' 5*3 =", var1 * var2)
print("2.4 'división' 5/3 =", var1 / var2)
print("2.5 'módulo' 5%3 =", var1 % var2)
print("2.6 'potencia' 5**3 =", var1 ** var2)
print("2.7 'división entera' 5//3 =", var1 // var2)
print("_____________________________")

print("3. Operadores de comparación")
print("3.1 'igualdad' 5==3 =", var1 == var2)
print("3.2 'desigualdad' 5!=3 =", var1 != var2)
print("3.3 'mayor que' 5>3 =", var1 > var2)
print("3.4 'menor que' 5<3 =", var1 < var2)
print("3.5 'mayor o igual que' 5>=3 =", var1 >= var2)
print("3.6 'menor o igual que' 5<=3 =", var1 <= var2)
print("_____________________________")

print("4. Operadores lógicos")
print("4.1 'and' 5>3 and 3<5 =", var1 > var2 and var2 < var1)
print("4.2 'or' 5>3 or 3<5 =", var1 > var2 or var2 < var1)
print("4.3 'not' not(5>3) =", not(var1 > var2)) # Invierte el valor lógico, 5 es mayor que 3, por eso el resultado sale falso.
print("_____________________________")

print("5. Operadores de asignación")
var1 = 6
print("5.1 'asignación' var1 =", var1)
var1 += 3
print("5.2 'suma y asignación' var1 += 3 =", var1)
var1 -= 3
print("5.3 'resta y asignación' var1 -= 3 =", var1)
var1 *= 3
print("5.4 'multiplicación y asignación' var1 *= 3 =", var1)
var1 /= 3
print("5.5 'división y asignación' var1 /= 3 =", var1)
var1 %= 4
print("5.6 'módulo y asignación' var1 %= 4 =", var1)
var1 **= 3
print("5.7 'potencia y asignación' var1 **= 3 =", var1)
var1 //= 3
print("5.8 'división entera y asignación' var1 //= 3 =", var1)
print("Al final queda var1 =", var1)
print("______________________________")

print("6. Operadores de identidad")
var1 = var2
print("var1 = var2")
print("6.1 'is' var1 is var2 =", var1 is var2)
print("6.2 'is not' var1 is not var2 =", var1 is not var2)
print("______________________________")

print("7. Operadores de pertenencia")
print("7.1 'in' 3 in [1,2,3] =", 3 in [1,2,3])
print("7.2 'not in' 3 not in [1,2,3] =", 3 not in [1,2,3])
print("______________________________")

print("8. Operadores bit a bit")
var1 = 1
print("var1 = 1, 0001 en binario")
var2 = 3
print("var2 = 3, 0011 en binario")
print("8.1 'AND': compara con & a dígito a dígito en binario")
print(" y devuelve 1 por campo como true  1&3 (var1 & var2) =", var1 & var2)
print(" el resultado es 1, porque 0001 (1) & 0011 (3) = 0001 (1)")
print("8.2 'OR': compara con 'or' dígito a dígito en binario")
print(" y devuelve 1 por campo como true  1|3 (var1 | var2) =", var1 | var2)
print(" el resultado es 3, porque 0001 (1) | 0011 (3) = 0011 (3)")
print("8.3 'XOR': compara dígito a dígito en binario y devuelve")
print(" 1 por campo que no sea igual  1^3 (var1 ^ var2) =", var1 ^ var2)
print(" el resultado es 2, porque 0001 (1) ^ 0011 (3) = 0010 (2)")
print("8.4 'NOT': invierte dígito a dígito el binario ~1 (~var1) =", ~var1)
print(" el resultado es -2, porque ~0001 (1) = 1110 (-2)")
print("8.5 'desplazamiento a la izquierda' 1<<1 (var1 << 1) =", var1 << 1)
print(" el resultado es 2, porque 0001 (1) << 1 = 0010 (2)")
print("es 00010, pero el cero a la izquierda no se cuenta")
print("8.6 'desplazamiento a la derecha' 1>>1 (var1 >> 1) =", var1 >> 1)
print(" el resultado es 0, porque 0001 (1) >> 1 = 0000 (0)")
print("8.6 otro ejemplo de desplazamiento a la derecha 10 >> 2 =", 10 >> 2)
print("el resultado es 2, porque 1010 (10) >> 2 = 0010 (2)")
print("8.5 otro ejemplo de desplazamiento a la izquierda 10 << 2 =", 10 << 2)
print("el resultado es 40, porque 1010 (10) << 2 = 101000 (40)")
print("______________________________")

print(" 9. Delimitadores de agrupación")
var1 = 3
print("var 1 = 3", var1)
var2 = 5
print("var 2 = 5", var2)
print("9.1 'paréntesis' (3+5)*2 =", (var1 + var2) * 2)
print("9.2 'corchetes' [3,5,7][1] =", [var1, var2, 7][1])
print(" selecciona la posición 1 del arreglo, que es 5")
print("9.3 'llaves' {'a':3,'b':5}['b'] =", {'a':var1,'b':var2}['b'])
print(" selecciona la llave 'b' del diccionario, que es 5")
print("______________________________")

print("10. Otros operadores")
print("Hay más operadores en https://docs.python.org/es/3.14/reference/lexical_analysis.html#operators-and-delimiters")
print("______________________________")

print("ESTRUCTURAS DE CONTROL EN PYTHON")
print("1. Estructuras de control de flujo")
print("1.1 'if' if var1>var2: print('var1 es mayor que var2')")
if var1>var2: 
    print('var1 es mayor que var2')
print(" la estructura no se imprime, por que no es verdadera2")
print("1.2 'if-else' if var1>var2: print('var1 es mayor que var2')" \
" else: print('var1 es menor o igual que var2')")
if var1>var2: 
    print('var1 es mayor que var2')
else: print('var1 es menor o igual que var2')
print("1.3 'if-elif-else' if var1>var2: print('var1 es mayor que var2')" \
" elif var1<var2: print('var1 es menor que var2')" \
" else: print('var1 es igual a var2')")
if var1>var2: 
    print('var1 es mayor que var2')
elif var1<var2: 
    print('var1 es menor que var2')
else: print('var1 es igual a var2')
print("1.4 'match-case' match var1: case 1: print('var1 es 1') " \
"case 2: print('var1 es 2') case _: print('var1 no es ni 1 ni 2')")
match var1:
    case 1: print('var1 es 1')
    case 2: print('var1 es 2')
    case _: print('var1 no es ni 1 ni 2')

print("______________________________")
print("2. Estructuras de control de bucle")
print("2.1 'while' while var1<var2: print('var1 es menor que 10') var1+=1")
while var1<var2:
    print('var1 es menor que 10')
    var1+=1
print("2.2 'for' for i in range(var1): print(i)")
var1 = 3
print("var1 =", var1)
for i in range(var1):
    print(i)
print("2.3 'break' for i in range(var1): if i==1: break print(i)")
for i in range(var1):
    if i==1: break
    print(i)
print("2.4 'continue' for i in range(var1): if i==1: continue print(i)")
for i in range(var1):
    if i==1: continue
    print(i)
print("2.5 'match-case' match var1: case 1: print('var1 es 1') case 2: print('var1 es 2') case _: print('var1 no es ni 1 ni 2')")
match var1:
    case 1: print('var1 es 1')
    case 2: print('var1 es 2')
    case _: print('var1 no es ni 1 ni 2')
print("2.6 'try-except' try: print(var1/0) except ZeroDivisionError: print('No se puede dividir entre cero')")
try:
    print(var1/0)
except ZeroDivisionError:
    print('No se puede dividir entre cero')
finally:
    print('Ejecutado finalmente')
print("______________________________")

print("EJERCICIO EXTRA")
print("Crea un programa que imprima por consola todos los números comprendidos \
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.")

print("for i in range(10, 56): \
    if i % 2 == 0 and i != 16 and i % 3 != 0: \
        print(i)")

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)