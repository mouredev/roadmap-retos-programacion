# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
#### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24
## Ejercicio
'''
/*
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

'''

### Operadores Aritméticos ###
print("***operadores enteros***")

# Suma
print(4+5)
# Resta 
print(4-5)
# Multiplicación
print(4*5)
# Divición
print(4/5)
# Resto
print(4%5)
# Exonente
print(4**5)
# División entera
print(4//5)

print("***Operadores de Comparación***")
print("comparación de enteros")
print(4>5)

print(4<5)

print(4>=5)

print(4<=5)

print(4!=5)

print(4==5)

print(4>=5)

print("comparación de cadenas")
print("mama"<"papa")
print ("mama">"papa")
print ("mama">="papa")
print ("mama"<="papa")
print ("mama"!="papa")
print ("mama"=="papa")

print(len("mama") == len("papa"))

print("*** operadores logicos****")

print(4<5 and 5>3)
print(4<5 and 5<3)
print(4>5 and 5>3)
print(4>5 and 5<3)


print(4<5 or 5>3)
print(4<5 or 5<3)
print(4>5 or 5>3)
print(4>5 or 5<3)

print('True or False:', True or False)

print(not(5>3))
print(not(4>5))
print(4<5 and not(5<3))

print("*** identidad ***")

a=4
b=5
print(a is b)

print(a is not b)

a=[4,5]
b=[4,5]
print(a is b)#sale falso por que aunque tiene los mismo numeros son distintos objetos en la memoria

print(a is not b)


print("***operadores de permanencia ***")

a=[4,5]
print(4 in a)

print(6 in a)

print(6 not in a)
#DIFICULTAD EXTRA (opcional):
"""""
Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""""
print("***Condicionales, iterativas, excepciones...***")

numbers=range(10,56)
for number in numbers: 

    if (number%2)==0:
        if number!=16:
            if (number%3)!=0:
                print(number)   
print("otra forma ")
for number in numbers: 

    if (number%2)==0 and number!=16 and number%3!=0:
        print(number) 
