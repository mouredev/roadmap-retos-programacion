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

# ---------- ARITHMETIC OPERATORS -----------

from re import match


A = 50
B = 77
C = 21
D = 3

addition = (A + C) + (A + B)
sustraction = (C - D) - (B - A)
multiplication = A * B
float_division = B / D
int_division = A // D
exponential = A**D #It's like 50^3
rest = A % D
# ---------- LOGIC & COMPARISON OPERATORS -----------


# equals ------------->       ==
my_boolean_1 = A == B
# different ---------->       !=
my_boolean_2 = A != B           
# minor -------------->       <
my_boolean_3 = A < B
# superior ----------->       >
my_boolean_4 = A > B
# minor or equals ---->       <=
my_boolean_5 = A <= B
# superior or equals ->       >=
my_boolean_6 = A >= B


# AND
and_test = A > D and C < B
print(and_test) #True

# OR
or_test = A > B or B == D
print(or_test) #False

# NOT
not_test = not(A <= D) #A is superior than D (False), but this proposition are negated (True)
print(not_test)


# ---------------------- CONTROL STRUCTURES ----------------------

# selectives structures (IF-ELSE, MATCH(SWITCH))
if B >= A:
    print(f"{B} >= {A}")

if A > B or A < C:
    print(A)
elif B + C == A:
    print(B + C)
else:
    D = D * 4
    print(D)
# ------------------------------------------------
day = 7
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("this is a default form")

# loop structures

while D < B:
    D = D + 1
    print(D)

# --------------
print("-"*30)

for i in range(0,100,2):
    print(i)


# ---------------------- CHALLENGE ----------------------
print("\n\n\n\n")
print("CHALLENGE")
for i in range (10,56):
    if(i % 2 == 0 and i != 16):
        if(i % 3 != 0):
            print(f"{i}, ", end="")
    if(i >= 55):
        print(i)