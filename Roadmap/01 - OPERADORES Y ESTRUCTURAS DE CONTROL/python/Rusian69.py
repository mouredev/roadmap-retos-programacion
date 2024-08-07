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

# ejemplos de operadores

print(3 + 4) # suma
print(3 - 4) # resta
print(3 * 4) # multiplicacion
print(3 / 4) # division
print(10 % 3) # residuo de la divicion
print(10 // 3) #divicion con resultado entero forzado
print(2 ** 3) # potenciacion

# Operaciones con enteros
print(3 > 4) # mayor
print(3 < 4) # menor
print(3 >= 4) # mayor o igual
print(4 <= 4) # menor o igual
print(3 == 4) # igualdad (resultado bool)
print(3 != 4) #desigualdad (resultado bool)

# Operadores Lógicos #
print(3 > 4 and "Hola" > "Python") # retorna verdad si ambos son verdaderos
print(3 > 4 or "Hola" > "Python") # retorna verdad si uno de los enunciados es verdaderos
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4)) # da el valor contrario al real

# DIFICULTAD EXTRA (opcional)
def contador():
    result = []
    for index in range(10,51):
        if index % 2 == 0 and index % 3 != 0 and index != 16:
            result.append(index)
    print(result)
contador()
