'''
EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
'''
#OPERADORES ARITMETICOS
num_a = 3
num_b = 3
print("Suma: ", num_a + num_b) # Suma
print("Resta: ", num_a - num_b) # Resta
print("Multiplicacion: ", num_a * num_b) # Multiplicación
division = num_a / num_b # División
print("División: ", division)
print("Modulo: ", num_a % num_b) # Módulo
print("Potencia: ", num_a ** num_b) # potencia
print("Divisioón: ", num_a // num_b) # division con numero entero de resultado
# OPERADOR DE COMPARACIÓN
print("\nComparaciones:\n")
print(f"¿Es num_a mayor a num_b? {num_a > num_b}") # Mayor a
print(f"¿Es num_a menor a num_b? {num_a < num_b}") # Menor a
print(f"¿El numero a es igual al numero b? {num_a == num_b}") #sson iguales?
print(f"¿El numero a es distinto al numero b? {num_a != num_b}") #sson distintos?

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''
print("")
#Ejercicio de dificultad extra
print("Ejercicio Dificultad Extra: \n")
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
     print(i)
    