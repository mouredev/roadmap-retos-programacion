#Ejercicio 01 operadores y estructuras de control
'''/*
 * EJERCICIO:
 
 
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *

 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
 '''



""" - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
"""
def Aritméticos():
    #suma
    suma = 1 + 1
    print("suma: ", suma)
    #resta
    resta = 1 - 1
    print("resta: ", resta)
    #multiplicacion
    multiplicacion = 1 * 1
    print("multiplicacion: ", multiplicacion)
    #division
    division = 1 / 1
    print("division: ", division)
    #modulo
    modulo = 1 % 1
    print("modulo: ", modulo)
    #exponente
    exponente = 1 ** 1
    print("exponente: ", exponente)
    #division entera
    divisionEntera = 1 // 1
    print("division entera: ", divisionEntera)

def Logicos():
    #and
    andLogico = True and True
    print("and: ", andLogico)
    #or
    orLogico = True or False
    print("or: ", orLogico)
    #not
    notLogico = not True
    print("not: ", notLogico)

def Comparacion():
    #igual
    igual = 1 == 1
    print("igual: ", igual)
    #diferente
    diferente = 1 != 2
    print("diferente: ", diferente)
    #mayor que
    mayorQue = 1 > 2
    print("mayor que: ", mayorQue)
    #menor que
    menorQue = 1 < 2
    print("menor que: ", menorQue)
    #mayor o igual que
    mayorOIgualQue = 1 >= 2
    print("mayor o igual que: ", mayorOIgualQue)
    #menor o igual que
    menorOIgualQue = 1 <= 2
    print("menor o igual que: ", menorOIgualQue)

def identidad():
    #is
    isIdentidad = 1 is 1
    print("is: ", isIdentidad)
    #is not
    isNotIdentidad = 1 is not 2
    print("is not: ", isNotIdentidad)

def pertenencia():
    #in
    inPertenencia = 1 in [1,2,3]
    print("in: ", inPertenencia)
    #not in
    notInPertenencia = 1 not in [1,2,3]
    print("not in: ", notInPertenencia)

def bits():
    #and
    andBits = 1 & 1
    print("and: ", andBits)
    #or
    orBits = 1 | 1
    print("or: ", orBits)
    #xor
    xorBits = 1 ^ 1
    print("xor: ", xorBits)
    #not
    notBits = ~ 1
    print("not: ", notBits)
    #desplazamiento a la izquierda
    desplazamientoIzquierda = 1 << 1
    print("desplazamiento a la izquierda: ", desplazamientoIzquierda)
    #desplazamiento a la derecha
    desplazamientoDerecha = 1 >> 1
    print("desplazamiento a la derecha: ", desplazamientoDerecha)

""""
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
"""

def condicionales():
    #if
    if 1 == 1:
        print("if")
    #if else
    if 1 == 1:
        print("if")
    else:
        print("else")
    #elif
    if 1 == 1:
        print("if")
    elif 1 == 2:
        print("elif")
    else:
        print("else")

def iterativas():
    #for
    for i in range(0,10):
        print("for")
    #while
    while True:
        print("while")
        break

def excepciones():
   #try except
   while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    #try except finally
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    finally:
        print("Finally, I executed!")
    #raise
    x = "hello"
    if not type(x) is int:
        raise TypeError("Only integers are allowed")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
"""

def dificultadextra():
    for i in range(10,56):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i)

dificultadextra()
# Perdon por el codigo tan largo pero es la manera mas ordenada que pude hacerlo jaja