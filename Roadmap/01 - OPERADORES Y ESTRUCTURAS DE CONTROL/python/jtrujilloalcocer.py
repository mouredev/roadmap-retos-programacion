# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
## Ejercicio

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
 '''
 
 #OPERADORES DE ASIGNACION
a=5
b=10
c=15
d=25
 
 #OPERADORES ARITMETICOS
print(a + b) #Suma
print(a - c) #Resta
print(c * a) #Multimplicacion
print(a / d) #Division
print(d % a) #Resto division
print(a // c)#Cociente Division
print(a**2, b**3)#Exponentes

#OPERADORES RELACIONALES

#OPERADORES COMPARACION
print(a > b) #si a es mayor que b imprime un True, de lo contrario un False
print(c < d) #si c es menor que d imprime un True, de lo contrario un False
print(a >= d) #si a es mayor o igual que d imprime un True, de lo contrario un False
print(c <= b) #si c es menor o igual que b imprime un True, de lo contrario un False

#OPERADORES LOGICOS 
print(a < b and b > c) #si las dos comparaciones se cumplen imprime un True, de lo contrario un False
print(c > a or b < a) #si una de las dos comparaciones se cumple imprime un True, de lo contrario un false
print(not(c < b)) #Invierte el resultado de la comparacion.

#DIFICULTAD
'''DIFICULTAD EXTRA (opcional):
 Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3'''
 
def main():
    for i in range(10,56): #Itera entre 10 y 55
        if i % 2 == 0 and i != 16 and i % 3 != 0: #Si el numero es par, no es 16 y no es multiplo de 3
            print(i)
          
if __name__ == "__main__": 
    main()
