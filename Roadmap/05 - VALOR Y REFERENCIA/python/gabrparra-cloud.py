"""
# #05 VALOR Y REFERENCIA
> #### Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24

## Ejercicio

```
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
"""

# Tipos de datos por valor

a=10  # Entero
b=a   # Asignación por valor    

print("Valor de a:", a)  # Imprime: Valor de a: 10
print("Valor de b:", b)  # Imprime: Valor de b: 10  

b=20  # Modificación de b
print("Valor de a después de modificar b:", b) 

a=30  # Modificación de a
print("Valor de a después de modificar a:", a)  

#Tipos de datos por referencia

Lista1 = [1, 2, 3]  # Lista
Lista2 = Lista1     # Asignación por referencia
print("Valor de Lista1:", Lista1)  # Imprime: Valor de Lista1
print("Valor de Lista2:", Lista2)  # Imprime: Valor de Lista2

Lista2.append(4)  # Modificación de Lista2
print("Valor de Lista1 después de modificar Lista2:", Lista1)  # Imprime: Valor de Lista1 después de modificar Lista2: [1, 2, 3, 4]
print("Valor de Lista2 después de modificar Lista2:", Lista2)  # Imprime: Valor de Lista2 después de modificar Lista2: [1, 2, 3, 4]

Lista1.append(5)  # Modificación de Lista1
print("Valor de Lista1 después de modificar Lista1:", Lista1)  # Imprime: Valor de Lista1 después de modificar Lista1: [1, 2, 3, 4, 5]
print("Valor de Lista2 después de modificar Lista1:", Lista2)  # Imprime: Valor de Lista2 después de modificar Lista1: [1, 2, 3, 4, 5]

#Funciones con variables por valor

def modificar_valor(x:int):
    x = 100  # Modificación de x
    print("Valor de x dentro de la función:", x)  # Imprime: Valor de x dentro de la función: 100

print("Valor de a antes de llamar a la función:", a)  # Imprime: Valor de a antes de llamar a la función: 30
modificar_valor(a)  # Llamada a la función con a como argumento
print("Valor de a después de llamar a la función:", a)  # Imprime: Valor de a después de llamar a la función: 30    

#Funciones con variables por referencia

Lista3 = [1, 2, 3, 4, 5]  # Lista

def modificar_referencia(lista:list):
    lista.append(100)  # Modificación de la lista
    print("Valor de lista dentro de la función:", lista)  # Imprime: Valor de lista dentro de la función: [1, 2, 3, 4, 5, 100]

print("Valor de Lista3 antes de llamar a la función:", Lista3)  # Imprime: Valor de Lista3 antes de llamar a la función: [1, 2, 3, 4, 5]
modificar_referencia(Lista3)  # Llamada a la función con Lista3 como argumento
print("Valor de Lista3 después de llamar a la función:", Lista3)  # Imprime: Valor de Lista3 después de llamar a la función: [1, 2, 3, 4, 5, 100]

def intercambiar_valores_por_valor(x:int, y:int):
    print("Valores originales:", x, y)  # Imprime: Valores originales: x y
    x, y = y, x  # Intercambio de valores
    print(x, y)  # Retorno de los valores intercambiados

def intercambiar_valores_por_referencia(lista_a:list, lista_b:list):
    print(lista_a,lista_b)
    temp=lista_a
    lista_a=lista_b
    lista_b=temp
    print(lista_a, lista_b ) # Retorno de las listas modificadas

intercambiar_valores_por_valor(10, 20)

intercambiar_valores_por_referencia([1, 2], [3, 4])