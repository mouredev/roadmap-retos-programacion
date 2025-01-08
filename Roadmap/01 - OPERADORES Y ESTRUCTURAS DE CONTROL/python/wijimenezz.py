# # EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  *


# Tipos de operadores

# Operadores de concatenacion de caracteres
a = "Hola a Todos "
b = "Estamos Aprendiendo Python"
print(a + b)

# operadores Booleanos
print("operadores Booleanos")
x = True
y = False
print("X y Y", x and y)
print("X y X", x and x)
print("Y y Y", y and y)
print("X or Y", x or y)
print("X or x", x or y)
print("y or y", y or y)
print("not X", not x)
print("not Y", not y)

# operadores de Comparación
print("operadores de Comparación")
num = 6
num2 = 4
print("6>4", num > num2)
print("6<4", num < num2)
print("6>=4", num >= num2)
print("6<=4", num <= num2)
print("6=4", num == num2)
print("6!= 4", num != num2)

# operadores aritmeticos
print("operadores aritmeticos")
print("Suma- 10 + 5", 10 + 5)
print("Resta- 10 - 5", 10 - 5)
print("Multiplicación  10 * 5", 10 * 5)
print("potemvia  10 ** 5", 10 ** 5)
print("Division Cociente  10 / 5", 10 / 5)
print("Division Entero  10 // 5", 10 // 5)
print("Division Residuo  10 % 5", 10 % 5)

# operadores Nivel Bits
print("operadores Nivel Bits")
a = 2
b = 7

print("a | b= ", a | b)
print("a ^ b= ", a ^ b)
print("a  & b= ", a & b)
print("a << 1= ", a << 1)
print("a >> 1= ", a >> 1)
print(" ~a= ", ~a)

# operadores de asignación
print("operadores de asignación")
n1 = 10
n2 = 2
print(f"n1 = {n1}")
print(f"n2 = {n2}")
n1 += n2
print("n1+=n2", n1)
n1 -= n2
print("n1-=n2", n1)
n1 *= n2
print("n*=n2", n1)
n1 **= n2
print("n1**=n2", n1)
n1 //= n2
print("n1//=n2", n1)
n1 %= n2
print("n1%=n2", n1)

# operadores de Flujo
print("operadores de Flujo")

animal = "Vaca"
if animal == "Serpiente":
    print(f" {animal} Corra y no mire atras")
elif animal == "Vaca":
    print(f"{animal} levantese temprano a ordeñar")
elif animal == "Gallina":
    print(f"{animal}Hay que recoger huevos")
else:
    print(" no hay animal, Usted esta en la ciudad")

# while
z = 10
while z > 0:
    z -= 1
    print(z)

# for
print("for")
for i in range(0, 10):
    print(i)

 # DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

print("Extra")
lista = []
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        lista.append(i)
print(lista)
