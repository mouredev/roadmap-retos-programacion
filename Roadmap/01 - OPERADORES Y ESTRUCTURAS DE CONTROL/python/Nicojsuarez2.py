'''
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
'''
a = 2
b = 3

# OPERADORES ARITMÉTICOS
print(a + b)    # Suma -> 5
print(a - b)    # Resta -> -1
print(a / b)    # División -> 0.6666666666666666
print(a // b)   # División entera -> 0
print(a * b)    # Multiplicación -> 6
print(a % b)    # Módulo -> 2
print(a ** b)   # Potencia -> 8
print(a ** 0.5) # Raíz cuadrada -> 1.4142135623730951
print(a)

# OPERADORES LÓGICOS
print(a and b)   # AND -> False
print(a or b)    # OR -> True
print(a is not b)  # NOT -> False

# OPERADORES DE COMPARACIÓN
print(a > b)    # Mayor que -> False
print(a < b)    # Menor que -> True
print(a >= b)   # Mayor o igual que -> False
print(a <= b)   # Menor o igual que -> True
print(a == b)   # Igual que -> False
print(a != b)   # Diferente a -> True

# OPERADORES DE ASIGNACIÓN
assign_sum = 7
assign_sum += 3                 # Suma y asignación
print(assign_sum)               # 10

assign_subtract = 7
assign_subtract -= 4            # Resta y asignación
print(assign_subtract)          # 3

# OPERADORES DE IDENTIDAD
list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(3 is list_b) #True, el mismo contenido en la "misma" memoria
print(1 in list_a) #True

# OPERADORES ITERADORES Y DE PERTENENCIA
for i in range(1, len(list_a)):
        print(i)

while a < 3:
    print("todavia no")
    a += 1
    
if a > b:
    print("a es mayor que b")
elif a < b:
     print("a es menor que b")
else:
        print("a es igual a b")


# OPERADORES DE BITS
num_1 = 3 #0011
num_2 = 8 #1000

for i in range(10, 55):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
                print(i)
