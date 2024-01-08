#01 OPERADORES Y ESTRUCTURAS DE CONTROL
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

# Operadores aritmeticos
print("--Operadores aritmeticos--")
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 // 2)
print(1 % 2)
print(1 ** 2)

# Operadores logicos
print("--Operadores logicos--")
print(True and False)
print(True or False)
print(not False)
      
# Operadores comparacion
print("--Operadores comparacion--")
print(1 > 2)    
print(1 < 2)    
print(1 >= 2)   
print(1 <= 2)   
print(1 == 2) 
print(1 != 2) 

# Operadores de asignacion
print("--Operadores de asignacion--")
# Suma
as_1 = 1
as_1 += 2                 
print(as_1)     
# Resta
as_2 = 1
as_2 -= 2            
print(as_2)          
# Mult
as_3 = 1
as_3 *= 2      
print(as_3)    
# Div
as_4 = 1
as_4 /= 2            
print(as_4)          
# Div Ent
as_5 = 1
as_5 //= 2       
print(as_5)      
# Modulo
as_6 = 1
as_6 %= 2              
print(as_6)            
# Potenica
as_7 = 1
as_7 **= 2
print(as_7)

# Operadores binarios
print("--Operadores binarios--")
# And
print(1 & 2)
# Or        
print(1 | 2)
# Xor
print(1 ^ 2)
# Not
print(~1)
# Desplazamiento left
print(1 << 2)
# Desplazamiento right
print(1 >> 2)

# Operador pertenencia
print("--Operador pertenencia--")
arr = [i for i in range(10)]
print(3 in arr)
print(11 in arr)

# estructuras de control
print("--Estructuras de control--")
age = 30
if age >= 30:
    print("Ya no eres joven!")
elif age < 30:
    print("Eres joven!")
else:
    print("Eres tan anciano como el universo.")


# Estructura de control iterativo for
print("--Estructura de control iterativo for--")
for i in range(10):
    print(i)

# Estructura de control iterativo while
print("--Estructura de control iterativo while--")
j = 0
while j < 10:
    print(j)
    j += 1

# Estructura de control try-except
print("--Estructura de control try-except--")
# Ejemplo clasico de division por 0
try:
    print(1 / 0)
except:
    print("Error de division")

# Extra
    print("--DIFICULTAD EXTRA--")
"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
numbers = [i for i in range(10, 56) if i % 2 == 0 and i != 16 and i % 3 != 0]
print(numbers)
