# * - EJERCICIO * :
""" - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
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
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo """

# * ------------------------------------------------------------------------------------ * #

""" - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits..."""
# * Aritméticos
suma = 2+2
resta = 2-2
multiplicacion = 2*2
division = 2/2
modulo = 2%2
parte_entera = 2//2
potencia = 2**2
print("\n")
print("Suma: ", suma, "\nResta: ", resta, "\nMultiplicacion: ", multiplicacion, "\nDivision: ", division, "\nModulo: ", modulo, "\nParte entera: ", parte_entera, "\nPotencia: ", potencia)
print("\n------------------------------------------------------------------------------------- \n")

# * lógicos (and, or o not)
#AND ambas deben ser verdad para delvolver True.
print("\nAND")
if(1==1 and 2==2):
    print (True)
else:
    print("ERROR!")

#OR con que una sea verdadera bastará para retornar True
print("\nOR")
if (1!=2 | 1!=1): 
    print (True)
else:
    print (False)

#NOT solo dará verdadero cuando su condición sea negada.
print("\nNOT")
if (1!=0):
    print(True)
else:
    print(False)
print("------------------------------------------------------------------------------------- \n")

# * Asignación
num = 2
print ("\n", num)
# Asignación compuesta
num+=2
print ("\n", num)
num-=2
print ("\n", num)
num*=2
print ("\n", num)
num/=2
print ("\n", num)
num%=2
print ("\n", num)
num//=2
print ("\n", num)
num**=2
print ("\n", num)
print("------------------------------------------------------------------------------------- \n")

#* Operadores bits a bits o bitwise
num = 27
numb = 28
print(bin(num))
print(bin(numb))
num&=numb
print ("\n", num)
num|=numb
print ("\n", num)
num^=numb
print ("\n", num)
num>>=numb
print ("\n", num)
num<<=numb
print ("\n", num)
print("------------------------------------------------------------------------------------- \n")

# * Operadores de identidad
print("Identidad")
print(1 is 2)
print(1 is not 2)
print("------------------------------------------------------------------------------------- \n")

# * Operadores de pertenencia
print("Membresia")
print(1 in [1,2,3])
print(1 not in [2,3,4,5])
print("------------------------------------------------------------------------------------- \n")


# * ------------------------------------------------------------------------------------ * #

"""- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
Debes hacer print por consola del resultado de todos los ejemplos."""
print("Condicionales\n")
print("IF")
a = 4
b = 2
if (a > b):
    print("Resultado: ", a/b)
else:
    print("B es mas grande que A, y no tengo ganas de dividir de esa manera.")

print("\nFor")
num = 1
lista = [1,2,3,4,5]
for num in lista:
    print(num)

print("\nForRange")
for i in range (0, 5):
    print(i)

print("\nWhile")
num = 1
while (num != 5):
    print(num)
    num+=1

print("\nSwitch se puede emular, pero no tiene de manera nativa")
condicion = 5
if condicion == 1:
    print("Haz a")
elif condicion == 2:
    print("Haz b")
elif condicion == 3:
    print("Haz c")
else:
    print("Haz d")

print("\n")

print("\nBreak") #Permite alterar el while y el for.

cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontro la h")
        break
    print(letra)

print("\nContinue") #También permite alterar el while y el for.
cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        print("Se encontro la P")
        continue
    print(letra)


print("\nFuncion zip()") #Viene incluída por defecto. Si le pasamos dos listas nos dará una tupla combinada. También podemos utilizarla con diccionarios.
a = [5, 2, 3, 4, 9]
b = ["Uno", "Dos", "Tres", "Cuatro", "Nueve"]
c = zip(a, b)

print(list(c))

print("\nEnumerate") #Sirve para recorrer algo y además de buscar un valor, podemos extraer facilmente la posición.
lista = ["A", "B", "C"]

for indice, letra in enumerate(lista):
    print(indice, letra)

print("\nList Comprehensions") #Nos permite crear una lista en una sola línea: lista = [expresión for elemento in iterable]
cuadrados = [i**2 for i in range(5)]
print(cuadrados)

print("\nIteradores e Iterables") #Permite iterar colecciones que sean iterables

# * ------------------------------------------------------------------------------------ * #
""" * DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""
print("\n Desafio EXTRA")
for i in range(10, 56):
    if (i % 2 == 0):
        if (i % 3 != 0):
            if(i != 16):
                print(i)


# * ------------------------------------------------------------------------------------ * #
