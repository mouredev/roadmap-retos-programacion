#01 OPERADORES Y ESTRUCTURAS DE CONTROL

x=12
y=3

#Arithmetic Operators
z0= x + y 
z1= x - y
z2= x * y
z3= x / y
z4= x % y
z5= x ** y
z6= x // y #Floor division (Entera, sin decimales)

#Python Assignment Operators
"""
=	    x = 5	    x = 5	
+=	    x += 3	    x = x + 3	
-=	    x -= 3	    x = x - 3	
*=	    x *= 3	    x = x * 3	
#/=	    x /= 3	    x = x / 3	
%=	    x %= 3	    x = x % 3	
\//=	x //= 3	    x = x // 3	
**=	x   **= 3	    x = x ** 3	
&=	x   &= 3	    x = x & 3	
|=	x   |= 3	    x = x | 3	
^=	x   ^= 3	    x = x ^ 3	
>>=	x   >>= 3	    x = x >> 3	
<<=	x   <<= 3	    x = x << 3
"""

#Python Comparison Operators
x == y
x != y
x > y
x < y
x >= y
x <= y

#Python Logical Operators
x > 2 and x > 20
x > 3 or x < 0
not (x > 2 and x > 15)

#Python Identity Operators
x is not y
x is y

#Python Membership Operators
"""
x in y
x not in y
"""

#Python Bitwise Operators
"""
x & y   #AND
x | y   #OR
x ^ y   #XOR                    Sets each bit to 1 if only one of two bits is 1
~x      #NOT                    Inverts all the bits	
x << 2  #Zero fill left shift   Shift left by pushing zeros in from the right and let the leftmost bits fall off
x >> 2  #Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	
"""

# If statement
if x > y:
    z = 20
elif x < 0: 
    z = 0
else:
    z = 10
print(z)

# For Statements
for i in range(1,10):
    print(i)

# While loop
while x > y:
	print(y)
	y += 1


#examples
print(x > 2 and y < 20)
print(x > 3 or y < 0)
print(not(x >= 12 and y >3))

tuplecats =("red", "blue", "brown", "orange")
print("cat" in tuplecats)

print(x + y)
print(x ** y)
print(x // y )

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
print("Extra -------------------------------------------------------------")

def numConditions(startNUM: str, endNUM: str) -> str:

    for i in range(startNUM,endNUM):
        if i % 2 == 0:
            if i % 3 != 0:
                if i != 16:
                    print(i)
    return print("Done")
                
numConditions(10,56)
