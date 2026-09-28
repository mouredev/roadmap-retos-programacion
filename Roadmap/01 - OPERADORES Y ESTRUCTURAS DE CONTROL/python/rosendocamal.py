""""
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

"""
==========
OPERADORES
==========
"""

# ========== ARIMÉTICOS ==========

a = 10
b = 3

print(a + b) # Suma
print(a - b) # Resta
print(a * b) # Multiplicación
print(a / b) # División
print(a // b) # Función suel de división
print(a % b) # Módulo
print(a ** b) # Potencia

# Operador de multiplicación de matrices y vectores
class Mat(list):
    def __matmul__(self, B):
        A = self
        return Mat([[sum(A[i][k]*B[k][j] for k in range(len(B)))
                    for j in range(len(B[0])) ] for i in range(len(A))])

A = Mat([[1,3],[7,5]])
B = Mat([[6,8],[4,2]])

print(A @ B)


# ========== COMPARACIÓN ==========

print(a < b) # Menor que
print(a > b) # Mayor que
print(a <= b) # Menor o igual que
print(a >= b) # Mayor o igual que
print(a == b) # Igual a
print(a != b) # Distinto de

# ========== OPERADORES BOOLEANOS ==========

x = True
y = False

print(x and y) # Conjunción
print(x or y) # Disyunción
print(not x) # Negación

# ========== BITWISE ==========

a = 6
b = 3

print(a & b) # AND bit a bit
print(a | b) # OR bit a bit
print(a ^ b) # XOR bit a bit
print(~a) # NOT bit a bit
print(a << 1) # Desplazamiento a la izquierda
print(a >> 1) # Desplazamiento a la derecha

# ========== ASIGNACIÓN ==========

a = 10

print(a) # Asignación

a += 5
print(a) # Suma y asignación

a -= 3
print(a) # Resta y asignación

a *= 2
print(a) # Multiplicación y asignación

a /= 4
print(a) # División y asignación

a //= 2
print(a) # División entera y asignación

a %= 3
print(a) # Módulo y asignación

a **= 2
print(a) # Potencia y asignación

a &= 3
print(a) # AND y asignación

a |= 3
print(a) # OR y asignación

a ^= 3
print(a) # XOR y asignación

a <<= 1
print(a) # Desplazamiento izquierdo de bits y asignación

a >>= 1
print(a) # Desplazamiento derecho de bits y asignación

# A @= B, Multiplicación matricial y asignación

# ========== IDENTIDAD ==========

lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]

print(lista1 is lista2) # Identidad
print(lista1 is not lista3) # No identidad

# ========== PERTENENCIA ==========

lista = [1, 2, 3, 4, 5]

print(3 in lista) # Pertenencia
print(10 not in lista) # No pertenencia

# ========== CONCATENACIÓN Y DESEMPAQUETADO  =========

''''
*    Desempaquetado iterable
**   Desempaquetado de mapeo
'''

# ========== CONDICIONAL ===========

'''
x if condición else y    Expresión condicional
'''

# ========== ASIGNACIÓN EXPRESIVA ============

'''
:=    Asignación expresiva (walrus)
'''

# ========== OPERADORES SINTÁCTICOS ============

'''
.     Acceso a atributo
[]    Indexación o slicing
()    Llamada o agrupación
,     Separación o construcción de tuplas
:     Slicing, anotaciones, diccionarios o bloques de sintaxis
;     Separación de instrucciones
'''

# https://docs.python.org/3/library/operator.html

"""
==========
ESTRUCTURAS DE CONTROL
==========
"""

# =========== IF - ELSE ===========

if (True or False):
    print("Es verdadero.")
else:
    print("Es falso.")
    
False if 1 else True

if a < 5:
    print(f"{a} es menor que 5.")
elif a > 5:
    print(f"{a} es mayor que 5.")
else:
    print("Felicidades.")
    
# =========== FOR ===========    
    
for i in range(12342,23424141, 9999):
    print(i * 2)

print()    
for i in range(5, 500, 50):
    print(i)
else:
    print()
    
# =========== WHILE ===========

contador: int = 5

while contador <= 500:
    print(contador)
    if contador % 73:
        contador -= 73
    else:
        contador -= 1
        
# =========== BREAK ===========

contador: int = 5

while contador <= 500:
    print(contador)
    if contador // 2 == 3:
        break
    else:
        contador += 73
        
# =========== CONTINUE ===========

for i in range(0, 100):
    if i == 0:
        continue
    print(0 / i)
    
lecturas = [25.3, 24.8, -1, 26.1, 999, 25.7]

for temperatura in lecturas:
    if temperatura < 0 or temperatura > 100:
        continue

    print(f"Temperatura válida: {temperatura} °C")

# =========== PASS ===========

for i in range(0, 10000):
    if i / 1:
        pass
    
for i in range(0, 1000):
    if i % 2 == 0 or i % 3 == 0:
        i = 0
    if i == 0:
        pass

# =========== TRY ===========

try:
    result = 0 / 0
except:
    print("No se puede dividir entre cero.")

a, b = 0, 0
try:
    result = a / b
except:
    print("Error en los datos.")
else:
    result: tuple[int, int] = (a, b)

try:
    result = 0 / 0
except:
    result = 0
finally:
    print(result)

# =========== WITH ===========

# with open("file.txt", "r") as txt:
#     text = txt.read()
#     print(text)

# =========== RETURN ===========

def hello_language(programming_language: str = "Python"):
    return f"Hello, {programming_language}!"

print(hello_language())
print(hello_language("C++"))

# =========== YIELD ===========

# yield

# =========== RAISE ===========

raise TypeError("Error con raise")

"""
==========
DIFICULTAD EXTRA
==========
"""
 
LIM_INFERIOR: int = 10
LIM_SUPERIOR: int = 55

RANGO: range = range(LIM_INFERIOR, LIM_SUPERIOR + 1, 2)

for num in RANGO:
    if num % 16 == 0 or num % 3 == 0:
        continue
    print(num)
else:
    print("EJERCICIO TERMINADO")