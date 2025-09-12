"""* EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)"""

"""Tipo de datos por Valor""" # Primitivos

numero = 10
numero2 = numero
numero2 = 50
print(numero)
print(numero2)


"""Tipo de datos por Referencia""" # Compuestos

num_lista = [10,50,100]
num_lista_Copia = num_lista
num_lista_Copia.append(200) # El valor será añadido a ambas listas, ya que la copia de la lista, apunta al espacio en memoria de la lista original
print(num_lista)
print(num_lista_Copia)


""" Función con datos por valor 'Primitivos' """

def cuadrado_valor(numero):
    numero *= numero
    print(numero)

cuadrado_valor(numero)
print(numero)

""" Función con datos por valor 'Compuestos' """

def cuadrado_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= numeros[i]
    print(numeros[:])

cuadrado_valores(num_lista[:])  # Asignamos una copia de la lista con [:]
print(num_lista)


"""Función con datos por referencia 'Compuestos' """

def mitad_numeros(numeros):
    for i,n in enumerate(numeros):
        numeros[i] /= 2
    print(numeros)

mitad_numeros(num_lista)
print(num_lista)

"""* DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras."""

num1 = 10
num2 = 20

def intercambio(valor1, valor2):
    return valor2, valor1

print(f"{num1}, {num2}")
num3, num4 = intercambio(num1,num2)
print(f"{num1}, {num2}")
print(f"{num3}, {num4}")

# Ambas funciones hacen el mismo trabajo, lo importante es el orden de los parámetros 

def intercambio_Mouredev(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

num3, num4 = intercambio_Mouredev(num1,num2)
print(f"{num3}, {num4}")
