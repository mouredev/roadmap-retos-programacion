# Operadores aritméticos de python
print("-Operadores aritméticos-")

# Contamos con 7 operadores aritméticos: +, -, *, /, //, %, **

num1, num2 = 5, 2

suma = num1 + num2  # 7
resta = num1 - num2  # 3
multiplicacion = num1 * num2  # 10
division = num1 / num2  # 2.5
division_entera = num1 // num2  # 2
modulos = num1 % num2  # 1
exponente = num1**num2  # 25

print(
    f"""
    Suma: {suma}
    Resta: {resta}
    Multiplicacion: {multiplicacion}
    Division: {division}
    Division entera: {division_entera}
    Modulos: {modulos}
    Exponente: {exponente}
    """
)

print("\n-Operadores lógicos-")

# Contamos con 3 operadores lógicos: and, or, not

a, b = True, False

and_operator = a and b  # False
or_operator = a or b  # True
not_operator = not a  # False

print(
    f"""
    AND: {and_operator}
    OR: {or_operator}
    NOT: {not_operator}
    """
)

print("\n-Operadores de comparación-")

# Contamos con 6 operadores de comparación: >, <, >=, <=, ==, !=

a, b = 5, 10

mayor = a > b  # False
menor = a < b  # True
mayor_igual = a >= b  # False
menor_igual = a <= b  # True
igual = a == b  # False
diferente = a != b  # True

print(
    f"""
    Mayor: {mayor}
    Menor: {menor}
    Mayor o igual: {mayor_igual}
    Menor o igual: {menor_igual}
    Igual: {igual}
    Diferente: {diferente}
    """
)

print("\n-Operadores de asignación-")
a = 7
b = 2

"""
Los operadores de asignación o assignment operators 
nos permiten realizar una operación y almacenar su 
resultado en la variable inicial:

    +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=
    
Podemos ver como realmente el único operador nuevo es el =. 
El resto son abreviaciones de otros operadores que habíamos visto con anterioridad. 
"""

print(f"a = {a}, b = {b}")
a += b
print("a+=", a)  # 9
a -= b
print("a-=", a)  # 5
a *= b
print("a*=", a)  # 14
a /= b
print("a/=", a)  # 3.5
a %= b
print("a%=", a)  # 1

print("\n-Operadores de identidad-")
# Python reutiliza el mismo objeto en memoria por lo que ambas variables apuntan al mismo objeto
a, b = 5, 5

# Python crea dos objetos diferentes en memoria, por lo que a pesar de tener el mismo valor, no son el mismo objeto
c = [1, 2, 3]
d = [1, 2, 3]

print(
    f"""
    A is B: {a is b}
    A is not B: {a is not b}
    C is D: {c is d}
    C is not D: {c is not d}
    """
)

print("\n-Operadores de pertenencia-")

# Contamos con dos operadores de pertenencia: in y not in.
# Nos devuelve true si el elemento pertenece al segundo elemento

string_in = "Hola" in "Hola Mundo"  # True
string_not_in = "Hola" not in "Retos de Programación"  # True
string_in_false = "Hola" in "Retos de Programación"  # False
print(
    f"""
    "Hola" in "Hola Mundo": {string_in}
    "Hola" not in "Retos de Programación": {string_not_in}
    "Hola" in "Retos de Programación": {string_in_false}
    """
)

# También podemos usarlo con listas

S = [1, 2, 3, 4, 5]

list_in = 1 in S  # True
list_in_false = 6 in S  # False
list_not_in = 6 not in S  # True

print(
    f"""
    1 in [1, 2, 3, 4, 5]: {list_in}
    6 not in [1, 2, 3, 4, 5]: {list_not_in}
    6 in [1, 2, 3, 4, 5]: {list_in_false}
    """
)

print("\n-Operadores de bits-")

# Los operadores a nivel de bit o bitwise operators son operadores que actúan sobre números enteros pero usando su representación binaria.

f, g = 60, 13
bitwise_and = f & g  # And bit a bit
bitwise_or = f | g  # Or bit a bit
bitwise_xor = f ^ g  # Xor bit a bit
bitwise_not = ~f  # Not bit a bit
bitwise_left_shift = g << 2  # Desplazamiento a la izquierda
bitwise_right_shift = g >> 1  # Desplazamiento a la derecha

print(
    f"""
    Bitwise AND: {bitwise_and}
    Bitwise OR: {bitwise_or}
    Bitwise XOR: {bitwise_xor}
    Bitwise NOT: {bitwise_not}
    Bitwise Desplazamiento a la izquierda: {bitwise_left_shift}
    Bitwise esplazamiento a la derecha: {bitwise_right_shift}
    """
)

print("\n-Estructuras de control-")

print("\n-> Condicionales")
edad = 0

if edad > 0:
    print("El numero es mayor a 0 y es positivo")
elif edad == 0:
    print("El numero es 0")
else:
    print("El numero es negativo")

print("\n-> Iterativas")

print("\n-> For")
for i in range(5):
    print(i)

print("\n-> While")
while edad < 5:
    print(edad)
    edad += 1

print("\n-> Excepciones")

try:
    print(edad)
except NameError:
    print("La variable no esta definida")
finally:
    print("Se ejecuta siempre")


print("\n-Desafios-")

""" Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. """


for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
