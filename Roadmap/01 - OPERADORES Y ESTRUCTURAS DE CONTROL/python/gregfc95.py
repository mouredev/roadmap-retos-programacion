""" 
* Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
"""
# *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

# Variables
x = 12
y = 3
z = 5

#Operadores Aritmeticos
print(f"Sumando 12 + 5 = {x+z}")
print(f"Restando 12 - 5 = {x-z}")
print(f"Multiplicando 12 * 5 = {x*z}")
print(f"Dividiendo 12/5 {x/y}")
print(f"Modulo 12%5 {x%y}")
print(f"Dividiendo con rendondeo 12/5 {x//y}")
print(f"Expontente 12^5 {x**y}")

#Operadores Comparacion

print(f"igualdad 2 == 3 { 3 == 3}")
print(f"No igual 2 != 3  {2 != 3}")
print(f"Mayor que 2 > 3 {2 > 3}")
print(f"menor que 2 < 3 {2 < 3}")
print(f"mayor igual que 2 >= 3 {2 >= 3}")
print(f"menor igual que 2 <= 3 {2 <= 3}")

#Python Logical Operators
print(f"And &&: 2 == 3 and 5 == 5 { 2 == 3 and 5 == 5}")
print(f"or ||: 2 == 3 or 5 == 5 { 2 == 3 or 5 == 5}")
print(f"not negacion !: 2 + 3 and 5 == 5 { not 2 + 3 == 5}")

#Python operador de precedencia
print(f"() parentesis (((2 + 3) * 5) - 1) { (((2 + 3) * 5) - 1)}")

#Python operador de identidad
#Compara el valor de la posicion de memoria, si es igual (is) si no lo es (is not)
posA = 3
posB = posA
print(f"Si posA, la (posA) de mem. is (posB), return false { posA is posB }")
print(f"Si posA, la (posA) de mem. is not (posB), return false { posA is not posB }")


#Python Mermership o de conjuntos, recordar diagrama de Venn
print(f"'o' in 'jose' { 'o' in 'jose' }")
print(f"'o' not in 'jose' { 'o' not in 'jose' }")

#Python Operadores de asignacion
valorA = 55 #Asignacion
print(valorA)
valorA += 1 #Suma y asignacion
print(valorA)
valorA -=1 #Resta y asignacion
print(valorA)
valorA *=1 #Mult. y asignacion  
print(valorA)
valorA /= 1 #Division y asignacion
print(valorA)
valorA %= 2 # Resto y asginacion
print(valorA)
valorA //= 2 # Division Redondeada y asiginacion
print(valorA)
valorA **= 2 # Exponente y asginacion
print(valorA)
valorA = 10
valorA &= 1 # And en bit y asignacion
print(valorA)
valorA |= 1 # OR en bit y asignacion
print(valorA)
valorA ^= 1 # XOR en bit y asignacion 0 0 = 0, 1 1 = 0
print(valorA) 
valorA >>= 1 # Desplazamiento a la derecha en bit y asignacion 0 0 = 0, 1 1 = 0
print(valorA)
valorA <<= 1 # Desplazamiento a la izq en bit y asignacion 0 0 = 0, 1 1 = 0
print(valorA)  

#Python Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {a & b}")
print(f"OR: 10 | 3 = {a | b}")
print(f"XOR: 10 ^ 3 = {a ^ b}")
print(f"NOT: 10 = {~a}")
print(f"Desplazacion a la izq 10 << 2 = {a<<2}")
print(f">>Desplazamiento a la derecha 10 >> 2 = {a>>2}")


#Ejercicio
"""
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

numero = 0

for numero in range(10, 56, 2):
    if ((numero != 16) and (numero % 3 != 0)):
         print(numero)
        