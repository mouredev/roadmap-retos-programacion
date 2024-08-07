"""

For this exercise I am going to follow this guide:
https://realpython.com/python-operators-expressions/

"""

'''
* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
'''

# Assignment Operator
my_var = 1


# Arithmetic Operators
1 + my_var  # Suma aritmetica
1 - my_var  # Resta
1 * my_var  # Multiplicación
1 / my_var  # División
1 % my_var  # El residuo al dividir 1 y my_var
1 // my_var  # La divisón de 1 y my_var, redondeando al menor entero.
1 ** my_var  # Potencia de 1 elevado a my_var


# Comparison Operators

a = 2  # Seting up some test values
b = 5

a == b  # Igual a
a != b  # No igual a
a < b  # a menor que b
a <= b  # a menor o igual que b
a > b  # a mayor que b
a >= b # a mayor o igual que b


# Boolean Operators
a = True
b = False

a and b  # returns b
a or b  # returns a
not a  # returns False


# Identity Operators.
    # Allow you to determine whether two operands have the same identity

x = 500
y = 500

x is y  # returns Flase
x is not y  # returns True


# Membership Operators.
    # To determine whether a value is present in a container data type, 
    # such as a list, tuple, or set

5 in [2, 3, 5, 9, 7]  # returns True
8 in [2, 3, 5, 9, 7]  # returns False


# Concatenation and Repetition Operators
"Hello, " + "World!"  # returns "Hello, World!"
"Hello" * 3  # returns "HelloHelloHello"


# Walrus Operator :=
def validate_length(string):
    if (n:= len(string)) < 8:
        print(f"Length {n} is too short, needs at least 8.")
    else:
        print(f"Length {n} is okay!")


# Bitwise Operators
    # Bitwise operators treat operands as sequences of binary 
    # digits and operate on them bit by bit 
        
# Bitwise AND
#   0b1100    12
# & 0b1010    10
# --------
# = 0b1000     8
bin(0b1100 & 0b1010)
#'0b1000'
12 & 10
#8


'''
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
'''

# Estructuras de control: if, elif, for 

a = 5
b = 10

if a < b:
    print("a is smaller")
elif b < a:
    print("b is smaller")
else:
    print("a is equal b")

a=0
while a < 10:
    print(a)
    a += 1

try:
    "hola" / 5

except TypeError:
    print("Both arguments must be numbers.")

'''
    * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 '''

for i in range(10, 56):
    if (i % 2) == 0:
        if i != 16:
            if (i % 3) != 0:
                print(i)
