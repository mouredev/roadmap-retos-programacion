# 05 VALOR Y REFERENCIA
# Mónica Vaquerano
# https://monicavaquerano.dev

"""
EJERCICIO:
Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
su tipo de dato.
"""
# La asignación de variables "por valor" y "por referencia" es un concepto importante
# en la programación y varía según el lenguaje de programación que estés utilizando.

# Asignación por Valor (Assignment by Value):
# Cuando se asigna una variable por valor, se crea una copia independiente del
# valor original. Esto significa que cualquier modificación realizada en la copia no
# afectará al valor original y viceversa.
print("- Asignación por Valor (Assignment by Value):")
numb = 1
str = "hello"
boolean = True

# Ejemplo de asignación
numb2 = numb
str2 = str
boolean2 = boolean

# Modificamos, y
numb = 2
str = "bye"
boolean = False

# los valores no cambian
print(numb2, str2, boolean2)  # Output: 1 hello True
print()

# Asignación por Referencia (Assignment by Reference):
# Cuando se asigna una variable por referencia, en lugar de copiar el valor, se asigna
# una referencia al mismo objeto en la memoria. Esto significa que cualquier modificación
# realizada en una variable afectará a todas las variables que hacen referencia al mismo objeto.
print("- Asignación por Referencia (Assignment by Reference):")
# Ejemplo de asignación por referencia en listas
lista1 = [1, 2, 3]
lista2 = lista1  # Se asigna una referencia a la misma lista

# Modificamos lista2, y lista1 también cambia
lista2.append(4)

print(lista1, lista2)  # Output: [1, 2, 3, 4] [1, 2, 3, 4]
print()
# Es importante tener en cuenta que en Python, las asignaciones de variables generalmente se
# realizan por referencia, pero hay algunas excepciones, como números, cadenas y tuplas, que
# se asignan por valor. Sin embargo, el comportamiento puede variar según el tipo de datos y
# el contexto de la asignación

"""
Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
"por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""
# Paso por valor (Pass by value):
# En Python, los tipos de datos simples como enteros, flotantes y cadenas se pasan por valor.
print("- Paso por valor (Pass by value):")


def modify_value(x):
    x = x + 10
    print("Inside the function:", x)


# Variable original
a = 5
print("Before function call:", a)

# Llamada a la función
modify_value(a)

# Valor de la variable original no cambia
print("After function call:", a)
print(
    "En este ejemplo, la variable a se pasa a la función modify_value por valor.\nDentro de la función, se modifica el valor de x, pero esto no afecta a la variable original a."
)
print()
# Paso por Referencia (Pass by Reference):
# Las listas y otros tipos de datos compuestos se pasan por referencia en Python.
print("- Paso por valor (Pass by value):")


def modify_list(lst):
    lst.append(4)
    print("Inside the function:", lst)


# Lista original
my_list = [1, 2, 3]
print("Before function call:", my_list)

# Llamada a la función
modify_list(my_list)

# La lista original se modifica
print("After function call:", my_list)

print(
    "En este caso, la lista my_list se pasa a la función modify_list por referencia.\nDentro de la función, se agrega un elemento a la lista original my_list, por lo que la lista original se modifica incluso fuera de la función. Esto demuestra el paso por referencia."
)
print("\nDIFICULTAD EXTRA (opcional):\n")
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""


def intercambioPorValor(param1: int, param2: int) -> tuple:
    temp = param1
    param1 = param2
    param2 = temp
    print(f"Originales durante el intercambio: x = {param1}, y = {param2}")
    return param1, param2


def intercambioPorReferencia(param1: list, param2: list) -> tuple:
    temp = param1
    param1 = param2
    param2 = temp
    print(f"Originales durante el intercambio: a = {param1}, b = {param2}")
    return param1, param2


print("Intercambio por Valor:")
x, y = 5, 10
print(f"Originales antes del intercambio: x = {x}, y = {y}")
x2, y2 = intercambioPorValor(x, y)
print(f"Originales después del intercambio: x = {x}, y = {y}")
print(f"Nuevas variables después del intercambio: x2 = {x2}, y2 = {y2}")

print("\nIntercambio por Referencia:")
a, b = [1, 2, 3], [4, 5, 6]
print(f"Originales antes del intercambio: a = {a}, b = {b}")
a2, b2 = intercambioPorReferencia(a, b)
print(f"Originales después del intercambio: a = {a}, b = {b}")
print(f"Nuevas variables después del intercambio: a2 = {a2}, b = {b2}")
