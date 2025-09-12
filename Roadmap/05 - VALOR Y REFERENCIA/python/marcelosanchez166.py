# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#  *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  */

"""
En python las variables son referencias a objetos en memoria, por lo que no hay una distinción clara entre "por valor" y "por referencia" como en otros lenguajes.
Sin embargo, podemos simular este comportamiento con diferentes tipos de datos. como por ejemplo:
- Variables por valor: son aquellas que contienen un valor primitivo, como enteros, floats, booleanos, etc. Cuando se asigna una variable por valor, se crea una copia del valor.
- Variables por referencia: son aquellas que contienen una referencia a un objeto mutable, como listas,
diccionarios, sets, etc. Cuando se asigna una variable por referencia, se crea una referencia al objeto original,
lo que significa que cualquier cambio en el objeto original se reflejará en la variable de referencia
# Ejemplos de variables por valor y por referencia
# Variables por valor
# En Python, los tipos de datos inmutables como enteros, flotantes, cadenas de texto y tuplas se comportan como variables por valor.
# Variables por referencia 
# En Python, los tipos de datos mutables como listas, diccionarios y sets se comportan como variables por referencia.
"""

# una variable por valor es un entero, float, booleano, etc. porque se crea una copia del valor
variable_por_valor_entero = 10
# Modificando el valor de la variable por valor, esto no afecta a la variable original
variable_por_valor_entero = 20
variable_por_valor_string = "Hola"  # Variable por valor de tipo string
variable_por_valor_string = "Mundo"  # Modificando el valor de la variable
variable_por_valor_float = 3.14  # Variable por valor de tipo float
variable_por_valor_float = 2.71  # Modificando el valor de la variable por valor
variable_por_valor_booleano = True  # Variable por valor de tipo booleano
variable_por_valor_booleano = False  # Modificando el valor de la variable por valor
print("Variable por valor:", variable_por_valor_booleano)
print("Variable por valor:", variable_por_valor_float)
print("Variable por valor:", variable_por_valor_string)
print("Variable por valor:", variable_por_valor_entero)


# una variable por referencia es una lista, diccionario, set, etc. porque se puede modificar su contenido sin crear una nueva variable
variable_por_referencia = [1, 2, 3]
variable_por_referencia[0] = 100  # Modificando el contenido de la lista por referencia
print("Variable por referencia:", variable_por_referencia)
variable_por_referencia.append(4)  # Añadiendo un nuevo elemento a la lista por referencia
print("Variable por referencia:", variable_por_referencia)


variable_por_referencia = {"clave": "valor"}  # Variable por referencia de tipo diccionario
print("Variable por referencia:", variable_por_referencia)
# Modificando el contenido del diccionario por referencia
# Modificando el contenido del diccionario por referencia
variable_por_referencia["clave"] = "nuevo valor"
print("Variable por referencia:", variable_por_referencia)


variable_por_referencia = {1, 2, 3}  # Variable por referencia de tipo set
print("Variable por referencia:", variable_por_referencia)
variable_por_referencia.add(4)  # Añadiendo un nuevo elemento al set por referencia
print("Variable por referencia:", variable_por_referencia)
# Modificando el contenido del set por referencia
variable_por_referencia = {5, 6, 7}  # Modificando el contenido del set por referencia
# Imprimiendo el contenido de la variable por referencia
print("Variable por referencia:", variable_por_referencia)

variable_por_referencia = (1, 2, 3)  # Variable por referencia de tipo tupla
print("Variable por referencia:", variable_por_referencia)
# Tuplas son inmutables, no se pueden modificar, pero se puede crear una nueva tupla
variable_por_referencia = (4, 5, 6)  # Creando una nueva tupla por referencia
print("Variable por referencia:", variable_por_referencia)

# ejemplo de función que recibe parámetros por valor y por referencia

variable_por_valor1 = 10  # Variable por valor
variable_por_referencia1 = [1, 2, 3]  # Variable por referencia
# funcion que recibe parámetros por valor
def funcion_por_valor(param1, param2):
    param1 = 100  # Modificando el valor del parámetro por valor
    param2.append(4)  # Modificando el contenido del parámetro por referencia
    return param1, param2
# enviando parámetros a la función
resultado_valor, resultado_referencia = funcion_por_valor(
    variable_por_valor1, variable_por_referencia1)
print("Resultado por valor:", resultado_valor)  # Imprime el valor modificado por valor
print("Resultado por referencia:", resultado_referencia)  # Imprime el contenido modificado por


variable_ref = [1, 2, 3]  # Variable por referencia
variable_valor = 10  # Variable por valor
# función por referencia
def funcion_por_referencia(param1, param2):
    param1 = 200  # Modificando el valor del parámetro por valor
    param2[0] = 300  # Modificando el contenido del parámetro por referencia
    return param1, param2
# enviando parámetros a la función por referencia
resultado_valor_ref, resultado_referencia_ref = funcion_por_referencia(variable_valor, variable_ref)
print("Resultado por valor:", resultado_valor_ref)  # Imprime el valor modificado por valor
print("Resultado por referencia:", resultado_referencia_ref)  # Imprime el contenido modificado


# dificultad extra
# funcion que recibe dos parámetros (cada uno) definidos como variables anteriormente.
varible1 = 10
varible2 = 20
def intercambiar_valores_por_valor(param1, param2):
    temp = param1
    param1 = param2
    param2 = temp
    return param1, param2
print("Valores originales por valor:", varible1, varible2)
resultado1, resultado2 = intercambiar_valores_por_valor(varible1, varible2)
print("Valores después de intercambiar por valor:", resultado1, resultado2)


var1 = [10]
var2 = [20]
def intercambiar_valores_por_referencia(param1, param2):
    temp = param1[0]
    param1[0] = param2[0]
    param2[0] = temp
    return param1, param2
print("Valores originales por referencia:", var1[0], var2[0])
resultado1_ref, resultado2_ref = intercambiar_valores_por_referencia(var1, var2)
print("Valores después de intercambiar por referencia:", resultado1_ref[0], resultado2_ref[0])
