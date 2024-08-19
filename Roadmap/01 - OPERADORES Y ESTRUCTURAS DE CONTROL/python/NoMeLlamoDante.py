#### EJERCICIO: ###
"""- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
"""

# Arithmetic Operators
print(f"Addition 9 + 6 = {9 + 6}")
print(f"Subtraction 9 - 6 = {9 - 6}")
print(f"Multiplication 9 * 6 = {9 * 6}")
print(f"Exponentiation 9 ** 6 = {9 ** 6}")
print(f"Division 9 / 6 = {9 / 6}")
print(f"Floor_division 9 // 6 = {9 // 6}")
print(f"Modulus 9 % 6 = {9 % 6}")

#Logic Operators
print(f" True And False : {True and False}")
print(f"True Or False : {True or False}")
print(f"Not False : {not False}")

#Comparison Operators
print(f"Equal: 10 == 10 {10 == 10}")
print(f"Not Equal: 10 != 5 {10 != 5}")
print(f"Greater than 5 > 10 {5 > 10}")
print(f"Greater than or equal to 5 >= 10 {5 >= 10}")
print(f"Less than 5 < 10 {5 < 10}")
print(f"Less than or equal to 5 > 10 {5 <= 10}")

#Bitwise Operators
x = 10
y = 7
print(f"x({x}, {bin(x)}) & y({y}, {bin(y)}) = {x & y}, {bin(x & y)}")
print(f"x({x}, {bin(x)}) | y({y}, {bin(y)}) = {x | y}, {bin(x | y)}")
print(f"x({x}, {bin(x)}) ^ y({y}, {bin(y)}) = {x ^ y}, {bin(x ^ y)}")
print(f"~ ( x({x}, {bin(x)}) ) = {~x}, {bin(~x)}")
print(f"x ({x},{bin(x)} >> 2 = {x >> 2}, {bin(x>>2)}")
print(f"x ({x},{bin(x)} << 2 = {x << 2}, {bin(x<<2)}")

#Assignment Operators
x = 10 
print(f"x = 10:  {x}")
x += 10
print(f"x = x + 10:  {x}")
x -= 10
print(f"x = x - 10:  {x}")
x *= 10
print(f"x = x * 10:  {x}")
x /= 5
print(f"x = x / 5:  {x}")
x %= 11
print(f"x = x % 11:  {x}")
x //= 3
print(f"x = x // 3:  {x}")
x **=2
print(f"x = x ** 2:  {x}")

#Assignment Bitwise Operators
x = int(x)
print(f"x = {bin(x)}")
print(f"8 = {bin(3)}")
x &= 8
print(f"x = x &= 8:  {bin(x)}: {x}")
print(f"7 = {bin(7)}")
x |= 7
print(f"x = x &= 7:  {bin(x)}: {x}")
print(f"5 = {bin(5)}")
x ^= 5
print(f"x = x ^= 5:  {bin(x)}: {x}")
x>>=2
print(f"x >>= 2 = {x}, {bin(x)}")
x<<=2
print(f"x <<= 2 = {x}, {bin(x)}")

#Identity Operators
x = [1,2,3]
y = [1,2,3]
z = x
print(f"x= {x}, y= {y}, z= x")
print(f"x is z? {x is z} || x is y? {x is y}")
print(f"x is not z? {x is not z} || x is not y? {x is not y}")

#Membership Operators
text = "refrigerator"
print(f"text = {text}")
print(f"'t' in {text}= {'t' in text}")
print(f"'z' not in {text}= {'z' not in text}")
"""- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
"""
text = "digital"
for char in text:
    if char == "a":
        index = 5
        while index >=0:
            index-=1
            if index %3 == 0 and index!=0:
                continue
            try:
                print(f"5 / index = {5/index}")
            except Exception as e:
                print(f"error: {e}")
        else :
            print("end while")
    elif char == "g":
        while True:
            print("other while")
            break
    else: 
        print(f"char: {char}")
    
"""- Debes hacer print por consola del resultado de todos los ejemplos."""


"""DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
for index in range(10,56):
    if index % 2 == 0 and index != 16 and not index%3 == 0:
        print(f"index = {index}")
