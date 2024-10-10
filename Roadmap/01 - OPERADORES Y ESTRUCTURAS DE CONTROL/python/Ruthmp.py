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
         */
"""

# OPERADORES ARITMÉTICOS
a = 5
b = 3
print (f" SUMA: a + b = {a+b}")
print (f"Resta: a - b = {a-b}")
print (f"Multiplicación: a * b ={a*b}")
print (f"División: a / b = {a/b}")
print (f"Modulo: a % b = {a%b}")
print (f"Exponente: a ** b = {a**b}")
print (f"División entera: a // b = {a//b}")

# OPERADORES DE COMPARACIÓN
print (f"Igualdad: a == b es {a==b}")
print (f"Desigualdad: a != b es {a!=b}")
print (f"Mayor que: a > b es {a>b}")
print (f"Menor que: a < b es {a<b}")
print (f"Mayor o igual: a >= b es {a>=b}")
print (f"Menor o igual que: a <= b es {a<=b}")

#OPERADORES LÓGICOS
print (f"AND &&: a>b and b==3 es {a>b and b==3} ")
print (f"OR || :a>b or b>a es {a>b or b>a} ")
print (f"NOT ! : not a + b == 10 es { not a + b == 10}")

#OPERADORES DE ASIGNACIÓN
num = 10
print(f"ASIGNACIÓN: num = 10 es {num}")
num+=1
print(f"SUMA Y ASIGNACIÓN: num += 1 es {num}")
num-=1
print(f"RESTA Y ASIGNACIÓN: num -= 1 es {num}")
num*=2
print(f"MULTIPLICACIÓN Y ASIGNACIÓN: num *= 2 es {num}")
num/=2
print(f"DIVISIÓN Y ASIGNACIÓN: num /=2 es {num}")
num%=3
print(f"MODULO Y ASIGNACIÓN: num %= 3 es {num}")
num**=3
print(f"EXPONENTE Y ASIGNACIÓN: num **= 3 es {num}")
num //=3
print(f"DIVISIÓN ENTERA Y ASIGNACIÓN: num //= 3 es {num}")

#OPERADORES DE IDENTIDAD
num2 = num
print(f"IS: num 2 is num es {num2 is num}")
print(f"IS NOT: num2 is not num es {num2 is not num}")

#OPERADORES DE PERTENENCIA
array = ["pera", "manzana", "melón"]
print("pera" in array)
print("tomate" not in array)

#OPERADORES DE BITS

"""
ESTRUCTURAS DE CONTROL
"""

#CONDICIONALES
hora = 12
if hora>=7 and hora<=14:
    print("Buenos días")
elif hora>14 and hora<20:
    print("Buenas tardes")
else:
    print("Buenas noches")

#ITERATIVAS
for x in range (10):
    print(x)

i=0
while i<6:
    print(i)
    i+=1

#EXCEPCIONES

try:
    print(5/0)
except:
    print("Se ha producido un error")
finally:
    print("El manejo de excepciones ha finalizado")

"""
EXTRA
"""

for num_extra in range (10,56):
    if num_extra %2==0 and num_extra !=16 and num_extra %3!=0:
        print(num_extra)