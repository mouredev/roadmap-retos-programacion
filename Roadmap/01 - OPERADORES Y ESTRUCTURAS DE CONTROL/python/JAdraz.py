''' - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)'''

''' - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...'''

''' - Debes hacer print por consola del resultado de todos los ejemplos.'''

## -- Arithmethic Operators --
num1 = 1
num2 = 2

# --- Additions ---

addition = num1 + num2
print(f"Addition \n The addition results is: {addition}")

# --- Substraction ---
substraction = num2 - num1
print(f"Substraction \n The substraction result is: {substraction}")

# --- Multiplication ---
multiplication = num1 * num2
print(f"Multipliation\n The multiplication result is: {multiplication}")

# --- Division ---
division = int(num2 / num1)
print(f"Division \n The division result is: {division}")

# --- Module ---
module = num2 % num1
print(f"Module \n The module result is: {module}")

# --- Exponentation ---
exponentation = num2 ** num1
print(f"Exponentation \n The exponentation result is: {exponentation}")

# --- Floor Division ---
floor_division = num2 // num1
print(f"Floor Division \n The floor division result is: {floor_division}")

## -- Assignment Operators --

# --- Assignment ---
assignment = num1
print(f"Assignment \n The assigment result is: {assignment}")

# --- Addition Assigment ---
num1 += 1
print(f"Addition Assigment \n The addition assigment result is: {num1}")

# --- Substraction Assigment ---
num2 -= 1
print(f"Substraction Assigment \n The substraction assigment result is: {num2}")

# --- Multiplication Assigment ---
num2 *= 3
print(f"Multiplication Assigment \n The multiplication assigment result is: {num2}")

# --- Divison Assigment ---
num2 /= 1
print(f"Divison Assigment \n The division assigment result is: {num2}")

# --- Modulus Assigment ---
num2 %= 1
print(f"Modulus Assigment \n The modulus assigment result is: {num2}")

# --- Floor Division Assigment ---
num1 //= 3
print(f"Floor Division Assigment \n The floor division assigment result is: {num1}")

# --- Exponentation Assigment ---
num2 = 3
num2 **= 5
print(f"Exponentation Assigment \n The exponentation assigment result is: {num2}")

# --- Bitwise AND Assigment ---
a = 5
a &= 3
print(f"Bitwise AND Assigment \n The bitwise AND assigment result is: {a}")

# --- Bitwise OR Assigment ---
b = 5
b |= 3
print(f"Bitwise OR Assigment \n The bitwise OR assigment result is: {b}")

# --- Bitwise XOR Assigment ---
c = 5
c ^= 3
print(f"Bitwise XOR Assigment \n The bitwise XOR assigment result is: {c}")

# --- Left Shift Assigment ---
d = 5
d <<= 2
print(f"Left Shift Assigment \n The left shift assigment result is: {d}")

# --- Right Shift Assigment ---
e = 20
e >>= 2
print(f"Right Shift Assigment \n The right shift assigment result is: {e}")


## -- Comparison Operatos --
num3 = 5
num4 = 10

# --- Equal ---
print("Equal Operator")
if num3 == num4:
    print("\n They are equal")
else:
    print("\n They are not equals")

# --- Not Equal ---
print("Not Equal Operators")
if num3 != num4:
    print("\n They are differents")
else:
    print("\n They are equals")

# --- Greater Than ---
print("Greater Than Operator")
if num3 > num4:
    print(f"\n {num3} is greater than {num4}")
else:
    print(f"\n {num3} is not greater than {num4}")

# --- Less Than ---
print("Less Than Operator")
if num3 < num4:
    print(f"{num3} is less than {num4}")
else:
    print(f"{num3} is not less than {num4}")

# --- Greater Than or Equal to ---
print("Greater Than or Equal to Operator")
if num3 >= num4:
    print(f"\n {num3} is greater than or equal to {num4}")
else:
    print(f"\n {num3} is not greater than or equal to{num4}")

# --- Less Than or Equal to ---
print("Less Than or Equal to Operator")
if num3 <= num4:
    print(f"{num3} is less than or equal to {num4}")
else:
    print(f"{num3} is not less than or equal to{num4}")

## -- Logical Operators --
num5 = 3
num6 = 7

# --- AND Operator ---
print(f"AND Operator")
if num3 < num4 and num3 == num5:
    print("\n True")
else:
    print("\n False")

# --- OR Operator ---
print(f"OR Operator")
if num3 < num4 or num3 == num6:
    print("\n True")
else:
    print("\n False")
    
# --- NOT Operator ---
print(f"NOT Operator")
if not(num3 < num4 or num3 == num6):
    print("\n True")
else:
    print("\n False")

## -- Identity Operatos

# --- IS Operator ---
print("Identity Operators")
if num3 is num5:
    print("They are the same")
else:
    print("They are not the same")

## -- Membership Operators

# --- IN Operator ---
list1 = [1, 2, 3]
l1 = 1
l2 = 4

print("IN Operator")

if l1 in list1:
    print(f"\n {l1} in in the list")
else:
    print(f"\n {l1} is not in the list")

# --- NOT IN Operator ---
if l2 not in list1:
    print(f"\n {l2} is not in the list")
else:
    print(f"\n {l2} is in the list")

''' DIFICULTAD EXTRA (opcional):
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

    Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.'''

print("Optional Exercise")

for i in range(10, 56):
    if i == 16:
        pass
    elif i % 3 == 0:
        pass
    elif i % 2 == 0:
        print(i)