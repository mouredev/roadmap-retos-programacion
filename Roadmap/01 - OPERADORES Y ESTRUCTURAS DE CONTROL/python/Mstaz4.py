# EJERCICIO 01

"""
1. - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
"""

print("Operadores Aritméticos:\n")
a = 3
b = 4

print("\tadición. 3 + 4 =", a + b)
print("\tsustracción. 3 - 4 =", a - b)
print("\tmultiplicación. 3 * 4 =", a * b)
print("\tmodulo. 3 % 4 =", a % b)
print("\tdivision. 3 / 4 =", a / b)
print("\texponencial. 3 ** 4 =", a ** b)
print("\tfloor division. 3 // 4 =", a // b)

print("\nOperadores Lógicos:")
a = True
b = False

print("\ta and b =", a and b)
print("\ta or b =", a or b)
print("\tnot a =", not a)

print("\nOperadores Relacionales:")
a = 5
b = 67

print("\t a > b =", a > b)
print("\t a < b =", a < b)
print("\t a == b =", a == b)
print("\t a >= b =", a >= b)
print("\t a <= b =", a <= b)
print("\t a != b =", a != b)

print("\nOperadores de Bit a Bit:")
a = 2
b = 3

print("\t a & b =", a & b)
print("\t a | b =", a | b)
print("\t ~a =", ~a)
print("\t a >> b =", a >> b)
print("\t a << b =", a << b)

print("\nOperadores de asignación:")
a = 5
print("\ta = ", a)
a += 5
print("\ta = a + 5 ->", a)
a -= 5
print("\ta = a - 5 ->", a)
a *= 5
print("\ta = a * 5 ->", a)
a /= 5
print("\ta = a / 5 ->", a)
a %= 5
print("\ta = a % 5 ->", a)
a **= 5
print("\ta = a ^ 5 ->", a)
a //= 5
print("\ta = a // 5 ->", a)

print("\nOperadores de pertenencia:")
lista = [1, 2, 3, 4, 5, 6, 7, 9]
print(lista)
print("\tEl número 8 está en la lista? ", 8 in lista)
print("\tEl número 63 no está en la lista? ", 8 not in lista)

print("\nOperadores de identidad:")
a = 1
b = 2
c = 1

print("a =", a, "b=", b, "c=", c)
print("\ta es b? ", a is b)
print("\ta no es b? ", a is not b)
print("\ta es c? ", a is c)

""" 
2. - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:
  Condicionales, iterativas, excepciones...
"""
# Condicionales
print("Ejemplo de condicional if")
edad = 20
if edad < 18:
    print("Menor de edad\n")
elif edad > 65:
    print("Adulto mayor\n")
else:
    print("Adulto\n")

# Iterativas
print("Ejemplo de estructura iterativa for")
for i in range(5):
    print(i)

print("\nEjemplo de estructura iterativa while")
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Excepciones
print("\nEjemplo de try, except y finally")
try:
    num = int(input("Ingrese un número: "))
except ValueError:
    print("Error: Debe ingresar un número")
finally:
    print("Operación finalizada")

""" 
3. - Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. 
"""
print("\nImprime por consola los números del 10 al 55 sin el 16 ni los multiplos de 3")
for i in range(10, 56):
    if i == 16 or i % 3 == 0:
        continue
    print(i)
