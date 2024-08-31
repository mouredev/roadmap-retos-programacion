# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como
#  * variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime
#  *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
#  *   su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  */

# Asignación de variables por valor y por referencia

# Por valor

# En Python, los tipos de datos primitivos (int, float, string, bool) se asignan por valor.
# Esto significa que si se asigna una variable a otra, se copia el valor de la primera
# en la segunda, y si se modifica la segunda, la primera no se ve afectada.

# Ejemplo:

a = 5 # Se asigna el valor 5 a la variable a
b = a # Se asigna el valor de a a la variable b
b = 10 # Se modifica el valor de b
print(a) # Imprime 5
print(b) # Imprime 10

# Por referencia

# En Python, los tipos de datos compuestos (listas, diccionarios, conjuntos, tuplas) se asignan por referencia.
# Esto significa que si se asigna una variable a otra, ambas apuntan a la misma dirección de memoria,
# y si se modifica una de ellas, la otra se ve afectada.

# Ejemplo:

lista1 = [1, 2, 3] # Se asigna una lista a la variable lista1
lista2 = lista1 # Se asigna la lista de lista1 a la variable lista2
lista2[0] = 4 # Se modifica el primer elemento de lista2
print(lista1) # Imprime [4, 2, 3]
print(lista2) # Imprime [4, 2, 3]

# Funciones con variables por valor y por referencia

# Por valor

# Si se pasa una variable por valor a una función, se crea una copia de la variable en la función,
# y si se modifica la variable en la función, la original no se ve afectada.

# Ejemplo:

def duplicar(x):
  x = x * 2
  return x

a = 5
print(duplicar(a)) # Imprime 10
print(a) # Imprime 5

# Por referencia

# Si se pasa una variable por referencia a una función, se pasa la dirección de memoria de la variable,
# y si se modifica la variable en la función, la original se ve afectada.

# Ejemplo:

def duplicar_elementos(lista): # Se pasa una lista por referencia
  for i in range(len(lista)): # Se recorre la lista
      lista[i] = lista[i] * 2 # Se duplica cada elemento
  return lista # Se retorna la lista modificada

lista = [1, 2, 3]
print(duplicar_elementos(lista)) # Imprime [2, 4, 6]  
print(lista) # Imprime [2, 4, 6]

# Dificultad extra (opcional)

# Programa que recibe dos parámetros por valor, los intercambia y los retorna

# Por valor

def intercambiar_valores(a:int, b:int) -> tuple: # recibe los valores enviados por al invocarla la funcion
  temp = a
  a = b
  b = temp
  return a, b

c = 10
d = 20
e , f = intercambiar_valores(c , d)

print(f"valor inicial de c:{c},y de d:{d}")
print(f"valor retoranado por la funcion en e:{e},y en f:{f}")

# Por referencia

def por_referencia (g:int, h:int) -> tuple: # recibe los parametros
  temp = g
  g = h 
  h = temp
  return g, h

i = [10, 20]
j = [30, 40]
k , l = por_referencia(i, j)
print(f"Valor original de i: {i},y de j: {j}")
print(f"Valor que retorna la funcion en k: {k},y en l: {l}")