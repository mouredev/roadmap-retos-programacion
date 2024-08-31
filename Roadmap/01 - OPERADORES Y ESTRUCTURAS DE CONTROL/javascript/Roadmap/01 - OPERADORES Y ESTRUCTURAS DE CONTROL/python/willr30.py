'''


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
 */


'''

#Operadores aritméticos

suma= 1 + 2
resta = 3 + 4
multiplicacion = 5 * 6
division = 7 / 8
potencia = 2**2
modulo = 10%5
division_con_barra_doble= 5//2  #En Python, se usa el operador barra doble // para realizar una división. Este operador // divide al primer número por el segundo número y redondea hacia abajo el resultado al entero más cercano.


#operadores logicos

print(f"{True or False}")
print(f"{True and False}")
print(f"{True != False}")


#Operadores relaconales
# < Menor que
# > Mayor que
# == exactamente igual
#>= mayor o igual que
#<= menor o igual que
#!= diferente de 


#Asginaciones de valor
a=5 #se asigna el valor de la variable 
a+=1 # se guarda el valor enterior y se suma el nuevo [a = (a=5) + 1 ]
a-=2 # se guarda el valor enterior y se resta el nuevo [a = (a=6) - 2 ]
a *=3 # se guarda el valor enterior y se multiplica el nuevo [a = (a=4) * 3 ]
a /= 4 #  se guarda el valor enterior y se divide el nuevo [a = (a=12) /4 ]
a %=5 #  se guarda el valor enterior y se obtiene el modulo juto con  nuevo valor [a = (a=3) % 1 ]


#operaores de pertenencia
#in devuelve True si el valor especificado se encuentra en la secuencia sino devuelve False
#not in, devuelve True si el valor especificado no se encuentra en la secuencia, sino devuelve False
#Ejemplo
a = [1,2,3,4,5]
  
print(3 in a) # Muestra True 
print (80 not in a) # Muestra True

#Lo anterior tambien se aplica al comparar cadenas de texto

#operadores de identidad
#se hace una comparaciíon si son exactamente iguales
w=1
r=2

print(w is r)
print(w is not r)



#Extra-----------------------------------------------------------

for i in range (10, 55):
    if (i % 2 ==0 and  i != 16 and i%3!=0):
        print(i)



