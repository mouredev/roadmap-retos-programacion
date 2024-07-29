import os
os.system('cls') #MAC/LINUX
#os.system('cls') #WINDOWS
"""
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
 */
"""
#CONDICIONALES CON OPERADORES DE COMPARACIÓN

mi_numero=float(input("Ingrese un numero:"))
if mi_numero > 20: #Verifica si es menor que 20
   print("El numero es mayor que 20") 
elif mi_numero < 20: #Verficia si es mayor que 20
   print("El numero es menor que 20")
elif mi_numero == 20: #Verifica si es igual a 20
   print("El numero es igual a 20")
   
if mi_numero % 2 == 0: #Verifica si el numero es multiplo de 2 o par
   print("El numero es par")
elif mi_numero % 2 !=0: #Verfifica si el numero es impar
   print("El numero es impar")
if mi_numero % 5 ==0: #Verifica si el numero es multipo de 5
   print("y multiplo de 5")

#Operadores Aritmeticos
miotro_numero = float(input("Ingrese otro numero:"))
operacion = str(input("Ingrese el tipo de operacion que desea realizar (Suma,Resta,Multiplicacion,Elevar,Resto,Division:)"))
if operacion == "Suma":
   print("La suma de los numeros es ",mi_numero + miotro_numero)
elif operacion == "Resta":
   print("La resta de los numeros",mi_numero ,"y", miotro_numero,"Es igual a:",mi_numero - miotro_numero)
elif operacion == "Multiplicacion":
   print("La multiplicacion entre",mi_numero ,"y", miotro_numero,"Es igual a:",mi_numero * miotro_numero)
elif operacion == "Elevar":
   print("El resultado al elevar ",mi_numero,"a",miotro_numero,"es:",mi_numero**miotro_numero)
elif operacion == "Resto":
   print("El resultado del resto entre ",mi_numero,"y",miotro_numero,"es:",mi_numero % miotro_numero)
elif operacion == "Division":
   print("El resultado de la division entre ",mi_numero,"y",miotro_numero,"es:",mi_numero/miotro_numero)

#Operadores logicos
print("Tablas de verdad")
Primero = bool(input("Ingrese un valor booleano, True o False: "))
Segundo = bool(input("Ingrese un valor booleano, True o False: "))
booleano = str(input("Ingrese el tipo de operador logico con el cual desea trabajar (And, Or, Not):"))
if booleano == "And":
   print ("El valor de verdad seria:",Primero and Segundo,"!")
elif booleano == "Or":
   print ("El valor de verdad seria:",Primero or Segundo,"!")
elif booleano == "Not":
   print ("El valor de verdad seria la negacion de {Primero}:",not Primero,"!")
   

#Ejercicio
for numero in range (10,56):
   if numero % 2 == 0 and numero !=16 and numero % 3 != 0:
      print(numero)
