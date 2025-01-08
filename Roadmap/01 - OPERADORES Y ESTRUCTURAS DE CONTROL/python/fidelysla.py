
# * EJERCICIO:
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


# ? TIPOS DE OPERADORES

# **Operadores Aritmeticos**

num1 = 3
-num1 # -3

num1 + num1
num1 - num1
num1 * num1
num1 / num1
num1 % num1  # Devuelve el resto de la división
num1 ** num1 # Calcula el exponente
num1 // num1 # Devuelve el cociente de la división

# **Operador de asignacion**
num2 = 20
num2 += 1  # num2 = num2 + 1
num2 -= 1
num2 *= 1
num2 /= 2
num2 %= 2  # num2 = num2 % 2
num2 **= 2 # num2 = num2 ** 2
num2 //= 2 # num2 = num2 // 2

# **Operadores de comparacion**

print(3 == "3") #False
print(4 != "4") #True
print(3 > 2) #True
print(4 < 5) #True
print(6 >= 5) #True


# **Operadores Logicos**
isString = True
isNum = False

print(isString and isNum)   # False
print(isString or isNum)    # True
print(not isNum)            # True


# **Operadores Bit a Bit**
a = 5;  # Representación binaria: 0101
b = 3;  # Representación binaria: 0011

print(a & b)  # 1 (AND a nivel de bits)
print(a | b)  # 7 (OR a nivel de bits)
print(a ^ b)  # 6


# **Operadores de Pertenecia**
a = [1,2,3,4,5]

print(3 in a)       # True
print(12 not in a)  # True


# **Operadores de Identidad**
"""
Un operador de identidad se emplea para comprobar
si dos variables emplean la misma ubicación en memoria.
"""
a = 3
b = 3
c = 4

print(a is b)       # True
print(a is not b)   # False
print(a is not c)   # True



# ? Ejemplos de tipos de estructuras de control

#! **Condicionales**

#* If-elif-else

if isString and isNum:
    print("Son tipos de datos verdaderos")
elif isString or isNum:
    print("Por lo menos uno es tipo de dato verdadero")

if ( 15 > 16 ):
    print("Consola 1")
elif (15 < 16):
    print("Consola 2")


#! **Ciclos**

#* For

for i in range(0,11):
    if i % 2 == 0:
        print(i)


abc = { "a": 1, "b": 2, "c": 3 }
for (k, v) in abc.items():
    print(f"{k}: {v}")


arr1 = ["a","b","c","d","e"]
for i in arr1:
    print(i)

for (index, value) in enumerate(arr1):
    print(f"Index: {index}, Value: {value}")


#* While
# Numeros entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

num3 = 10
while (num3 <= 55):
    if (num3 == 10):
        print(num3)
    elif (num3 % 3 == 0 or num3 == 16):
        pass
    else:
        print(num3)
    num3 += 2


# **Manejo de Errores**
x = 2
y = 0
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Division por cero!")
else:
    print("Resultado:", result)
finally:
    print("Ejecutando la cláusula finalmente")