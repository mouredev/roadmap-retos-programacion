

# Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:

print("\nOperadores aritméticos\n")

numero1 = 13
numero2 = 8

resultado = print(f"El resultado de la suma (+) es: {numero1+numero2}")
resultado = print(f"El resultado de la resta (-) es: {numero1-numero2}")
resultado = print(f"El resultado de la multiplicación (*)es: {numero1*numero2}")
resultado = print(f"El resultado de la división (/) es: {numero1/numero2}")
resultado = print(f"El resultado de la división entera (//) es: {numero1 // numero2}")
resultado = print(f"El resultado de la multiplicación xponencial (**) es: {numero1 ** numero2}")
resultado = print(f"El resultado del módulo (%) es: {numero1 % numero2}")

# *******Operadores de comparación*******

print("\nOperadores de comparación\n")

resultado = print(f"¿Ambos números son iguales (==)?: {numero1 == numero2}")
resultado = print(f"¿Ambos números son diferentes (!=)?: {numero1 != numero2}")
resultado = print(f"el primer número es mayor que el segundo (>)?: {numero1 > numero2}")
resultado = print(f"el primer número es menor que el segundo (<)?: {numero1 < numero2}")
resultado = print(f"el primer número es mayor o igual que el segundo (>=)?: {numero1 >= numero2}")
resultado = print(f"el primer número es menor o igual que el segundo (<=)?: {numero1 <= numero2}")

#*******Operadore Logicos*******

print("\nOperadores lógicos\n")

# AND - se evalúan x condicioes y todas deben ser verdaderas
resultado = print(f"¿El primer número es mayor que el segundo Y (AND) el segundo número es impar? : {numero1 > numero2 and numero2 %2 != 0 }")

# OR - se evalúan x condicioes y al menos una debe ser verdadera
resultado = print(f"¿el primer número es mayor que el segundo O (OR) el segundo número es impar? : {numero1 > numero2 or numero2 %2 != 0 }")

# NOT -se evalúan x condicioes y el resultado es la negación de la evaluación
resultado = print(f"Negación (NOT) ¿El primer número es mayor que el segundo Y el segundo número es impar? : {numero1 > numero2 or numero2 %2 != 0 }")

#*******Operadore de pertencia*******

print("\nOperadores de pertenencia\n")

edades = [21, 18, 33, 28]

# in - evalua si un vaalor está en la lista
print(edades)
print(f"El número 44 está (IN) en la lista? {44 in edades} ")

# not in - evalua si un vaalor está NO la lista
print(f"El número 44 NO está (NOT IN) en la lista? {44 not in edades} ")

# *******operadores e Identidad *******
#- Usados para comprobar si dos variables son el mismo objeto en memoria

edades2 = [12, 17, 23, 18, 33]
edades3 = [12, 17, 23, 18, 33]
edades4 = edades2

# IS - valida si dos variables son el mismo objeto 

print(f"¿edades2 ES el mismo objeto (IS) que edades3 ? {edades2 is edades3}")
print(f"¿edades2 ES el mismo objeto que edades4 ? {edades2 is edades4}")

# IS NOT - valida si dos variables NO SON el mismo objeto

print(f"¿edades2 NO ES el mismo objeto (IS NOT) que edades3 ? {edades2 is not edades3}")

# ******Operadores de bit*******

print("\nOperadores de bit\n")
# - Permiten realizar operaciones de bit en números enteros, compara bit a bit y devuelve el resultado en entero.

number1 = 10 # binario 1010
number2 = 7 # binario 0111

print("AND = valdrá 1 si ambos bit son =1 (&): ", number1 & number2) # resultante 0010 = 2
print("OR = valdrá 1 si al menos un bit es =1 (|): ", number1 | number2) # resultante 1111 = 15
print("XOR = valdrá 1 los bit son diferentes (^): ", number1 ^ number2 ) # resultante 1101 = 13
print("NOT = invierte bit por bit (~)", ~number2)
print("Desplazamientro a la izquierda (<<): ", 10 << 2 )
print("Desplazamientro a la derecha(>>): ", 10 >> 2 )


#*******Estructuras de control*******

# Condicionales

print("\nEstructuras de control\n Condicionales: \n")

edad1= 17

if edad1 >= 18:
  print("Mayor de edad, puede ingresar.")
else:
  print("Menor de edad no puede ingresar.\n")

# CicloS

edades_clase = [12,13,14,22,33,14,58,23,45,17]
print("edades de la clase impresas con el ciclo for. ")
for edad in edades_clase:
  print(edad)


contador = 0
while contador < 10:
  print("Ciclo while contador ",  contador)
  contador += 1


for i in range (10):
  if i % 2 ==0:
    print(i)

# control de exxcepciones

numero = 18
try:
  resultado = numero / 0 # Esta división no es posible
except:
  print("Verifique los valores y operación")
finally:
  print("Manejo de excepción try, except y finally terminado.")

#Ejercicio de dificultad extra#
"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
for i in range(10,56):

  if i != 16 and i %3 != 0 and i%2 == 0:
    print(i, end=" - ")
