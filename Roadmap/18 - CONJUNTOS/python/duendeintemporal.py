#18 { Retos para Programadores } CONJINTOS

# Bibliography reference
# Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

""" 
* EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.

"""
import time

# Function to simulate console.log
log = print
    
log('Retosparaprogramadores #18')

# Array operations
arr = [1, 2, 3, 4, 5]
log(arr)  # [1, 2, 3, 4, 5]

# Adds an element to the end
arr.append(6)
log(arr)  # [1, 2, 3, 4, 5, 6]

# Adds an element to the beginning
arr.insert(0, 0)
log(arr)  # [0, 1, 2, 3, 4, 5, 6]

# Adds multiple elements in bulk to the end
arr2 = [7, 8, 9, 10]
arr.extend(arr2)
log(arr)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Adds multiple elements in bulk at a specific position
arr3 = [3.1, 3.2, 3.4]
arr[4:4] = arr3
log(arr)  # [0, 1, 2, 3, 3.1, 3.2, 3.4, 4, 5, 6, 7, 8, 9, 10]

# Removes an element at a specific position
del arr[6]
log(arr)  # [0, 1, 2, 3, 3.1, 3.2, 4, 5, 6, 7, 8, 9, 10]

# Updates the value of an element at a specific position
arr[-1] = 9.1
log(arr)  # [0, 1, 2, 3, 3.1, 3.2, 4, 5, 6, 7, 8, 9, 9.1]

# Checks if an element is in a set
nums = set(arr)
log('Is 10 in nums:', 10 in nums)  # Is 10 in nums: False

# Removes all content from the set
nums.clear()
log(nums)  # set()

# EXTRA DIFFICULTY (optional):

# Union
arr4 = [10, 11, 12, 13, 14]
union = set(arr) | set(arr4)
log('Union:', union)  # {0, 1, 2, 3, 3.1, 3.2, 4, 5, 6, 7, 8, 9, 9.1, 10, 11, 12, 13, 14}

# Intersection
arr5 = [1, 4, 5, 6, 15, 16, 17, 18, 19]
intersection = set()
for n in arr5:
    if n in union:
        intersection.add(n)

log('Intersection:', list(intersection))  # [1, 4, 5, 6]

# Difference
difference = set(arr)
for n in arr5:
    difference.discard(n)

log('Difference:', list(difference))  # [0, 2, 3, 3.1, 3.2, 7, 8, 9, 9.1]

# Symmetric difference
symmetric_diff = set(arr) ^ set(arr5)
log('Symmetric Difference:', list(symmetric_diff))  # [0, 2, 3, 3.1, 3.2, 7, 8, 9, 9.1, 15, 16, 17, 18, 19]
