import os
os.system('clear') #MAC/LINUX
#os.system('cls') #WINDOWS


"""
* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *"""


#CONDICIONALES CON OPERADORES DE COMPARACIÓN

mi_numero = int(input('Escriba un número: '))

if mi_numero > 10:
   print ("Tu número es mayor de 10")
elif mi_numero == 10:
   print ("Tu número es 10")
else:
   print("Tu número es menor a 10") 

if mi_numero % 2 == 0:
   print("Tu número es par") 
elif mi_numero % 2 != 0:
   print("Tu número es impar")
if mi_numero % 5 == 0:
   print(" y múltiplo de 5") 




#OPERADORES ARITMÉTICOS ENTRE 2 NÚMEROS:
   
mi_otro_numero =  int(input('Escriba otro número: '))
print ("Tu primer número y tu segundo número suman:" , (mi_numero + mi_otro_numero))
print ("Tu primer número menos tu segundo número es:" , (mi_numero - mi_otro_numero))
print ("Tu primer número multiplicado por tu segundo número es:" , (mi_numero * mi_otro_numero))
print ("Tu primer número dividido por tu segundo número es:" , (mi_numero / mi_otro_numero))



#ESTRUCTURAS DE CONTROL:

condicion = True
if condicion:
 print("se ejecuta la condición si es true")

#Si aquí hay un else entra por él si condición es false y no entra al siguiente if

 condicion = 5*2
if condicion == 10:
     print ('se ejecuta la condicion del segundo if')

     print ("la ejecución continúa")

condicion=0
while condicion<100:
    print(condicion)
    condicion += 11
    if condicion==55:
     print ('hemos cortado la ejecución en', condicion)
     break
     """con break el programa finaliza al cumplirse la condición del if,
       sino continúa hasta cumplirse la condición del while-else"""
     
else:
    print("ya ha llegado a" , condicion)





#CONTROL DE EXCEPCIONES:
    
primer_numero = 4
segundo_numero = 0
#Comentar y descomentar la siguiente asignación de segundo_numero para ver cambios
segundo_numero = "5"


### try-except
try:
  print(primer_numero + segundo_numero)
  print("operación correcta")
except:
    print("operación incorrecta")

### try-except-else
try:
   print(primer_numero + segundo_numero)
   print("operación correcta")
except: #obligatorio para completar try
    print("operación incorrecta")
else: # opcional para continuar sin excepciones
    print ("la ejecución continúa")

   ### try-except-else-finally
try: 
   print(primer_numero + segundo_numero)
   print("operación correcta")
except: #obligatorio para completar try
    print("operación incorrecta")
else: # opcional para continuar sin excepciones
    print ("la ejecución contitúa")
finally: #opcional para continuar con y sin excepciones
    print("la ejecución continúa pero puede haber errores")

   ###prevención de excepciones por tipo
try: 
   print(primer_numero + segundo_numero)
   print("operación correcta")
except TypeError: #TypeError limita la excepción al tipo de dato
    print("tipos de dato incompatibles para esta opración")

   ###prevención de excepciones por tipo y/o por valor
try: 
   print(primer_numero + segundo_numero)
   print("operación correcta")
except ValueError: #ValueError limita la excepción al valor del dato
    print("valores incompatibles con esta operación")
except TypeError: #TypeError limita la excepción al tipo de dato
    print("tipos de dato incompatibles para esta operación")


    ###prevención y captura de fallos (concretos o genéricos)
try: 
   print(primer_numero / segundo_numero)
   print("operación correcta")
except Exception as fallo: #Exception nos permite capturar cualquier excepción en una variable
    print(fallo)





#EJERCICIO PROPUESTO
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""

for i in range (10,56):
   if i % 2 == 0 and i % 3 != 0 and i != 16:  
     print (i)
   