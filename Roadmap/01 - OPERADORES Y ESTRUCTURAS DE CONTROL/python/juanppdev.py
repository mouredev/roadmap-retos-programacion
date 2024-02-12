"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 """

# Operadores Aritmeticos
print(f"5 + 5 = {5 + 5}") # Suma
print(f"5 - 5 = {5 - 5}") # resta
print(f"5 * 5 = {5 * 5}") # Multiplicacion
print(f"5 / 5 = {5 / 5}") # Division
print(f"5 % 5 = {5 % 5}") # Modulo
print(f"5 ** 5 = {5 ** 5}") # Exponente
print(f"5 // 5 = {5 // 5}") # Cociente

# Operadoes Logicos
print(True and True)   # and
print(False or True)   # or
print(not True)   # not

# Operadores de Comparacion
x = 4
y = 8
print(x > y) # >
print(x >= y) # >=
print(x < y) # <
print(x <= y) # <=
print(x == y) # ==
print(x != y) # !=

# Operadores de Asignacion
a = 7
b = 2
print("Operadores de Asignacion")
x=a; x+=b;  print("x+=", x)  # 9
x=a; x-=b;  print("x-=", x)  # 5
x=a; x*=b;  print("x*=", x)  # 14
x=a; x/=b;  print("x/=", x)  # 3.5
x=a; x%=b;  print("x%=", x)  # 1
x=a; x//=b; print("x//=", x) # 3
x=a; x**=b; print("x**=", x) # 49
x=a; x&=b;  print("x&=", x)  # 2
x=a; x|=b;  print("x|=", x)  # 7
x=a; x^=b; print("x^=", x)   # 5
x=a; x>>=b; print("x>>=", x) # 1
x=a; x<<=b; print("x<<=", x) # 28

# Operadores de Identidad
a = 10
b = 10

print(a is b) # is
print(a is not b) # is not

# Asignacion de pertenencia
lista = [1, 3, 2, 7, 9, 8, 6]
print(4 in lista) # in
print(6 not in lista) # not in

# Asignacion de bitwise
a = 0b1101
b = 0b1011
print(bin(a & b)) # &
print(bin(a | b)) # |
a = 40
print(bin(a))
print(bin(~a)) # ~
x = 0b0110 ^ 0b1010
print(bin(x)) # ^
a=0b1000
print(bin(a>>2)) # >>
a=0b0001
print(bin(a<<3)) # <<

# Condicionales
numero = int(input("Escriba un número positivo: "))
if numero < 0:
    print("¡Le he dicho que escriba un número positivo!")
print(f"Ha escrito el número {numero}")

# Iteradores
contador = 1
while contador <= 10:
    print("Paso: ",str(contador))
    contador+=1

# Excepciones
while True:
    try:
        x = int(input("Ingresa un Numero: "))
        break
    except ValueError:
        print("Oops!  Ese no es un numero valido.  Intentalo nuevamente...")


"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

for numbers in range(10, 56):
    if numbers % 2 == 0 and numbers != 16 and numbers % 3 != 0:
        print(numbers)