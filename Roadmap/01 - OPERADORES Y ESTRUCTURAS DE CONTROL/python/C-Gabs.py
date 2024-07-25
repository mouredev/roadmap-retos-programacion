#Reto 01

'''EJERCICIO:
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
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.'''


#tipos de operadores

#Aritmeticos

suma = 5 + 3
print(f'suma:',suma)

resta = 5 - 3
print(f'resta:',resta)

multiplicacion = 5*3
print(f'Multiplicación:',multiplicacion)

division = 15/3
print(f'División:',division)

div_entera = 15//3
print(f'División:',div_entera)

potencia = 5**3
print(f'Potencia:',potencia)

resto = 15%3
print(f"Resto:", resto)

#Lógicos

conjuncion = True and True
print(f'conjunción:',conjuncion)

conjuncion = True and False
print(f'conjunción:',conjuncion)

disyuncion = True or False
print(f'Disyunción:',disyuncion)

disyuncion = False or False
print(f'Disyunción:',disyuncion)

disyuncion = True or True
print(f'Disyunción:',disyuncion)

negacion = not True
print(f'Negación:',negacion)

negacion = not False
print(f'Negación:',negacion)

#Comparación

mayor_que = 5 > 3
print(f'Mayor qué:',mayor_que)

menor_que = 5 < 3
print(f'Menor qué:',menor_que)

igual = 5 == 4
print(f'Igual:',igual)

igual = 4 == 4
print(f'Igual:',igual)

diferente = 5 != 4
print(f'Diferente:',diferente)

diferente = 5 != 5
print(f'Diferente:',diferente)

mayor_igual_que = 5 >= 4
print(f'Mayor o igual qué:',mayor_igual_que)

mayor_igual_que = 5 >= 8
print(f'Mayor o igual qué:',mayor_igual_que)

mayor_igual_que = 8 >= 8
print(f'Mayor o igual qué:',mayor_igual_que)

menor_igual_que = 5 <= 4
print(f'Menor o igual qué:',menor_igual_que)

menor_igual_que = 5 <= 8
print(f'Menor o igual qué:',menor_igual_que)

menor_igual_que = 5 <= 5
print(f'Menor o igual qué:',menor_igual_que)

#Asignación

var = 5
print(f'Asignación básica:', var)

var += 6
print(f'Asignación con suma:', var)

var -= 7
print(f'Asignación con resta:', var)

var *= 8
print(f'Asignación con multiplicación:', var)

var /= 5
print(f'Asignación con división:', var)

var *= 3
print(f'Asignación con potencia:', var)

var %= 2
print(f"Asignación con resto:", var)

#Operadores de identidad

print('Operador "is": ', 5 is True)
print('Operador "is": ', 5 is False)
print('Operador "is": ', 5 is 4)
print('Operador "is": ', 5 is 3 + 2)

print('Operador "is not": ', 5 is not True)
print('Operador "is not": ', 5 is not False)
print('Operador "is not": ', 5 is not 4)
print('Operador "is not": ', 5 is not 3 + 2)

#Operadores de pertenencia

string = "Hola mundo"

print("Hola" in string)
print("Python" in string)
print("Hola" not in string)
print("Python" not in string)

#Operadores de bits

print("Operador &: ", 1010 & 1100)
print("Operador |: ", 1010 | 1100)
print("Operador ~: ", ~1100)
print("Operador ^: ", 1010 ^ 1100)
print("Operador >>: ", 1010 >> 2)
print("Operador <<: ", 1010 << 2)

#Operadores de conjuntos

set_1 = {2,4,6,8,10}
set_2 = {1,3,5,7,9}
set_3 = set_1 | set_2
print(f"Unión de conjuntos:", set_3)
print(f"Intersección de conjuntos:", set_1 & set_3)
print(f"Diferencia de conjuntos:", set_2 - set_1, "(set_2 - set_1)")
print(f"Diferencia de conjuntos:", set_1 - set_2, "(set_1 - set_2)")
print(f"Diferencia simétrica de conjuntos:", set_1 ^ set_2)
print(f"Inclusión de conjuntos:", set_1 <= set_3, "(set_1 subconjunto de set_2)")
print(f"Inclusión de conjuntos:", set_1 >= set_3, "(set_1 superconjunto de set_2)")
set_4 = {1,2,3,4,5,6,7,8,9,10}
print(f"Ingualdad de conjuntos:", set_4 == set_3)

#Operador de concatenación

string_2 = string + "," + " hola Python!"
print(string_2)

lista = [1,2,3] + [4,5,6]
print(lista)

#Estructuras de control
print("Estructura iterativa for")
for char in string_2:
    print(char)

print("Estructura iterativa while y estructura condicional")
num = 0
while num < 10:
    if num == 5:
        print("Se cumple la coondición")
    else:
        print(num)
    num +=1

#Excepciones

try:
    ejemplo = input("Ingrese un número: ")
    int(ejemplo)
except:
    print("Hubo un error")
finally:
    print("Entra en el finally")

#Ejercicio extra
for number in range(10,56):
    if (number != 16 and number % 3 != 0) and number % 2 == 0:
        print(number)
