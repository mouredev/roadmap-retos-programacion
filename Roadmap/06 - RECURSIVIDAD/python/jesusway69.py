import os
os.system('cls')


"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
"""
num = 101
def countdown (num):#Definimos la función y le pasamos el número 101 en la primera ejecución
    num -=1#En la primera iteración deja el número en 100 y va restando 1 en cada entrada a la función
    if num >= 0:#Establecemos la condición de parada en 0 
        print(num, end=' ') #imprimimos cada número horizontalmente y separado en cada ejecución de la función
        if num % 10 == 0 and num != 100: #establecemos un salto de línea cada 10 números para hacerlo más visual (opcional)
            print('')#Salto de línea
        countdown(num) #Llamada recursiva a la función con el número ya modificado restándole 1
countdown(num)#Llamada inicial a la función


"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""


#FUNCIÓN FIBONACCI POR RECURSIVIDAD
list_fibonacci = [0,1]
copy, counter1, counter2 = 0, 0, 1

def fibonacci (fib_position:int):
    global copy , counter1, counter2 
    if fib_position>copy:
     copy = fib_position
    if fib_position <=0:
        print("el nº debe ser mayor a 0")
        return
    if fib_position==2:
        print(f"\nLa posición {copy} de la secuencia Fibonacci tiene el valor {list_fibonacci[copy-1]}\n")
        return
    if fib_position == 1:
        print ("\nLa posición 1 de la secuencia Fibonacci tiene el valor 0 ")
        return
    elif fib_position >2:   
        list_fibonacci.append(list_fibonacci[counter1]+list_fibonacci[counter2])
        counter1 +=1
        counter2 +=1    
        fib_position -=1
        fibonacci(fib_position)


 # FUNCIÓN FACTORIAL POR RECURSIVIDAD
acc = 1
def factorial (factorial_num:int):
  global acc, copy
  if factorial_num>copy:
      copy=factorial_num
  if factorial_num>1:
      acc = factorial_num * acc
      factorial_num -=1
      factorial(factorial_num)
  else:
      print(f"\nEl factorial de {copy} es: {acc}\n")
      return




def menu ():   
 while True:
  num = input("""
            1- Mostrar posición en la secuencia Fibonacci
            2- Mostrar factorial
            3- Salir
              Elija una opción:  """)
  try:
   num = int(num)
   num == 1 or num == 2
   if num == 1:
        num = int(input("\nIntroduzca un número para calcular su posición en la secuencia Fibonacci: "))
        fibonacci(num)
        return
   if num == 2:
        num = int(input("\nIntroduzca un número para calcular su factorial: "))
        factorial(num)
        return
   if num == 3:
        print("\nFin del programa\n")
        return
   else:
        print ("\nSólo se pueden elegir opciones entre 1 y 2, pruebe de nuevo")
        menu()
     
   break
  except ValueError:
    print("\nSólo se pueden introducir números enteros, pruebe de nuevo")
menu()
