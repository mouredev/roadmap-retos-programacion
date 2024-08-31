"""
  EJERCICIO:
  - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
  - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
  - Debes hacer print por consola del resultado de todos los ejemplos.
 
 *DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
 *entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
#Operadores aritméticos

#Suma 
suma = 1 + 2

#Resta 
resta = 7 - 8

#Multiplicación
multiplicacion = 2 * 2

#División
division = 10 / 2

#División con cociente entero
divisionEntero = 13 # 4

#Módulo (es el resto de la división)
modulo = 9 % 2

#Exponente 
exponente = 3**3


# Operadores lógicos (vamos a declarar antes para este apartado)
VALORTRUE = True
VALORFALSE = False

#Operación AND (la salida será True cuando todas las variables sean true)
AND = VALORFALSE and VALORTRUE

#Operación OR (la salida será True cuando alguna variable sea true)
OR = VALORFALSE or VALORTRUE

#Devuelve false si su único operando es true, de lo contrario devuelve true
NOT = not VALORTRUE


#Operadores de comparación

#Igualdad 
igualdad = 3==3

#No igualdad
noIgualdad = 4 !=56

#Mayor que 
mayorQue = 23 > 18

#Menor que
menorQue = 12 < 34

#Mayor o igual que 
mayorOIgual = 33 >= 33

#Menor o igual que 
menorOIgual = 12 <= 13


#Operadores de asignación
numero1 = 3
numero2 = 5

#Operador suma
numero1 += numero2 # numero1 = numero1 + numero 2

#Operador resta 
numero2 -= numero1 #numero2 = numero2 - numero1

#Operador multiplicación
numero1 *= numero2 # numero1 = numero1 * numero2

#Operador división
numero1 /= numero2 # numero1 = numero1 / numero2

#Operador módulo
numero2 %= numero1 # numero2 = resto de la división entre numero 2 y numero 1

#Operador exponente 
numero1 **= numero2 #numero1 = numero1 ** numero2

#Operador división entera
numero2 #= numero1 #numero2 = numero2 / numero1 pero el cociente será un numero entero


#Operadores de identidad
numero3 = 7
numero4 = 9
#Operador de igualdad esctricta
numero3 is numero4 #En caso de que sean estrictamente iguales el terminal devolverá true
#Operador de desigualdad estricta
numero3 is not numero4 #Si son desiguales en algo el ternimal devuelve true


#Operadores de pertenencia
myList = [1,2,3,4,5,6]

pertTrue = 3 in myList #Devuelve true

pertFalse = 33 in myList #Devuelve false


#Operadores bit a bit (Los números se convierten a numeros binarios y se hacen las operaciones lógicas correspondientes bit a bit)
numero5 = 15
numero6 = 9
#AND a nivel de bits (Devuelve un uno en cada posición del bit para los que los bits correspondientes de ambos operandos son unos)
bitAnd = numero5 & numero6 # 1111 (15) & 1001 (9)= 1001, la operación AND devuelve 1 cuando ambos bits sean 1 y 0 para el resto de los casos
#OR a nivel de bits (Devuelve un uno en cada posición del bit para los que los bits correspondientes de ambos operandos no sean 0)
bitOr = numero5 | numero6 # 1111 (15) & 1001 (9)= 1111, la operación OR devuelve 1 cuando ambos bits sean 1 o 0 y 0 para el resto de los casos
#XOR a nivel de bits
bitXor = numero5 ^ numero6 # 1111 (15) & 1001 (9)= 0110, la operación XOR devuelve 1 cuando ambos bits sean distintosy 0 para cuando sean iguales
#NOT a nivel de bits
bitNot = ~numero5 #Convierte los bits los que son 1 pasan a 0 y vicerversa 
#Desplazamiento a la izquierda
bitIzq = numero6<< 3 # 9<<3 desplaza el numero6 3 ceros a la izquierda y da resultado 1001000
#Desplazamiento a la derecha 
bitDcha = numero6 >> 3# 9>>3 desplaza el numero6 3 ceros a la derecha y da resultado 1


#Estructuras de control

#Sentencia IF si se cumple la condición se ejecuta el bloque de código que hay dentro de la sentencia, en caso contrario se ejecuta otro código
print("Resultado Sentencia IF:")

if (numero1 < numero2):

    print("Número 1 es mayor que número 2") 

else :
    
    print("Número 2 es mayor que número 1")

# Bucle WHILE la acción se ejecuta hasta que la condición deja de cumplirse (ideal para cuando no sabemos el número de iteraciones del bucle)
print("Resultado Bucle WHILE:")
numero7 = 1

while (numero7 <= 9):
    print(numero7)
    numero7 = numero7 + 1

 # Bucle FOR la acción se ejecuta hasta que se cumple con el número máximo de iteraciones
print("Resultado Bucle FOR:")
numero8 = 1
for numero8 in range (1,10):
    print("Es mi primer bucle for en Python")

#Excepciones
    
#Sentencias try y except

try: #EL PROGRAMA VA A EJECUTAR ESTE CÓDOGO PRIMERO
    numero12 = int(input("Introduce un número"))
    numero14 = int (input("Introduce otro número"))
    resultado = numero12 + numero14
    print (resultado)
except: # SI NO SE INTRODUCEN NÚMEROS EL PROGRAMA EJECUTA ESTO EN VEZ DE QUEDARSE BLOQUEADO
    print("Debes introducir números")

#Sentencia finally (esto se ejecuta si o si de error o no)
try: 
    numero12 = int(input("Introduce un número"))
    numero14 = int (input("Introduce otro número"))
    resultado = numero12 + numero14
    print (resultado)
except: 
    print("Debes introducir números")
finally:
    print ("Esto se ejecuta si o si")






#DIFICULTAD EXTRA  

numero9 = 10

for numero9 in range (9,55):
    numero9 = numero9 + 1
    if (numero9 % 2 == 0 and numero9 != 16 and numero9 % 3 !=0):
        print (numero9)
    


       

        
       




