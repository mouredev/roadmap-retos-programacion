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

a = 10
b = 18
suma = a+b
resta = a-b
mult = a*b
div = a/b
divEntera = a // b

mayorq = a > b
menorq = a < b
igualq = a == b
desigualq = a != b

if suma > a or suma > b :
    print("variable a o variable b son distintas de 0")

for i in range(10):
    print(a+i)
    print(b-i)
    if a == 12:
        continue
    elif a == 13:
        break
while b<20 :
    print(b)
    b+=1

# aritmeticos
print("*** Operadores Aritmeticos ***")
print(f"{a}+{b}={suma}")
print(a,"-",b,"=", resta)
print("{0}*{1}={2}".format(a,b,mult))
print(b,"/",a,"=", div)
print(b,"//",a,"=", divEntera)
print(b,"%",a,"=", a%b)
print(a, "**",b,"==", a**b)

# comparacion
print("*** Operadores comparacion ***")
print(a,">",b,"=", mayorq)
print(a,"<",b,"=", menorq)
print(a,"=",b,"=", igualq)
print(a,"!=",b,"=", desigualq)

#logicos
print("*** Operadores Logicos ***")
print(f"AND 10 > 5 and 5 > 0 {10 > 5 and 5 > 0}")
print(f"OR 10 > 5 and 5 == 0 {10 > 5 or 5 == 0}")
print(f"NOT not (10 == 5 and 5 == 0) {not (10 == 5 and 5 == 0)}")

#asignacion
print("*** Operadores Asignacion ***")
age = 20
print(f"  age = 20 ... {age}")
age += 1
print(f"  age += 1 ... {age}")
age -= 10
print(f"  age -= 10 ... {age}")
age *= 2
print(f"  age *= 2 ... {age}")
age /=3
print(f"  age /= 3 ... {age}")

# identidad
print("*** Operadores Identidad ***")
oldage = age
print(f"oldage is age {oldage is age}")
oldage = age +10
print(f"oldage is age {oldage is age}")
oldage = 1.0
print(f"oldage is age {oldage is age}")
age = "aaaa"
newage = "aaaa"
print(f"newage is age {newage is age}")
print(f"newage is not age {newage is not age}")

# pertenencia
print("*** Operadores Pertenencia***")
a = [1,2,3,4,56,0]
b = 1
print(f" b is in a {b in a}")
print(f"'f' un 'fire' {'f' in 'fire'}")

#operadores con bits
print("*** Operadores con bits ***")
print(f"AND 9 & 5 = {9 & 5}") # 9 = 1001 5 = 101  and ... 1 si los dos son 1
print(f"OR 9 | 5 = {9 | 5}")  # | es 1 si al menos uno es 1
print(f"XOR 9 ^ 5 = {9 ^ 5}") # ^  es 1 si son diferentes
print(f"NOT ~9 = {~9}") #  
print(f"desplazamiento derecha 9 >> 3 = {9 >> 3}") 
print(f"desplazamiento izquierda 9 << 3 = {9 << 3}") 

# extructuras de control
# condionales 
print("*** extructuras de control condicionales ***")
if "asus" in "asustech":
    print("good")
elif "asus" not in "ASUS":
    print("asus not in ASUS")
else:
    print("ni asus ni ASUS")

# iterativas
print("*** extructuras de control Iteractivas ***")
for i in range(3,10,3):
    print(i)

a=0

while True:
    a+=1
    print(a)
    if a == 10:
        break

#excepciones
print("*** extructuras de control manejo errores ***")

try:
    print(12 / 0)
except:
    print("error")
finally:
    print("salida del try")


print(" ****** EXTRA ****** ")

# usando step2
for i in range(10,56,2):
    if i == 16 or i % 3 ==0:
        continue
    print(i)

# usando if para pares
for i in range(10,56):
    if i %2 != 0 or i == 16 or i % 3 != 0:
        continue
    print(i)

i = 10
while i < 56:
    print(i)
    i+=2


