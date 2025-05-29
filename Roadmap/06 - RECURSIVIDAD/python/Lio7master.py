
#  EJERCICIO:
#  Entiende el concepto de recursividad creando una función recursiva que imprima
#  números del 100 al 0.

#  DIFICULTAD EXTRA (opcional):
#  Utiliza el concepto de recursividad para:
#  - Calcular el factorial de un número concreto (la función recibe ese número).
#  - Calcular el valor de un elemento concreto (según su posición) en la 
#    sucesión de Fibonacci (la función recibe la posición).


# La recurdividad es una funcion que se llama asi misma para terminar una tarea repetitiva

#La profundidad maxima de recursividad es de 999 en python
def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number-1)

countdown(100)

#Extra

#Calculo de Factorial
def factorial(number: int)-> int:
    if number < 0:
        print("los numeros negativos no son validos")
        return 0
    elif number == 0:
        return 1
    else:
       return number * factorial(number - 1) #aqui la idea es n! = n * (n - 1) * (n - 2) * ... * 1
#siendo que se manda a llamar asi mismo puesto que regresa el numero ya restado,ejemplo con 5:  5 * por la funcion de 4 y susecibamente  4 pediria la funcion 3... 
# hasta llegar a 0 que auto finaliza la funcion, y en se momento retrocede para el calculo final desde el que se multiplicarioa 1*1*2*3*4*5 ya que se acumularon.

print(factorial(5)) 

#Fibonacci
def fibonacci(number: int) -> int:
    
    if number <= 0:
        print("No es una posición validad para contar")
        return 0
    # elif number == 1 :
    #     return 0 
    #lo condensamos en el siguiente elif porque logicamente podemos entender que si el se solicita seran menores en -1  a la posicion solicitada 
    # 1 = 0 y 2 = 1 en la calculo de fibonacci
    elif number <= 2:
        return number - 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
    #la suma se realiza de modo que la posicion marcara fib(7) = fib(6) + fib(5), donde se llaman bajo los criterios hasta llegar a posicion p1 = 0 y p2 = 1 de la cadena donde
    # sucecibamente realizara hasta hacer la suma desde las posiciones mas bajas desde donde se ira calculan por pocision para posterior suma:
    # (desgloce los fib a la izquierda, pero aplica el mismo para todos los elmentos hacer recursion) 
    # fib(p1)= 0 + fib(p2)= 1 -> fib(p3)=1 + fib(p4)=2 -> fib(p5)=3 + fib(p6)=5 -> fib(7)= 8
    #al hacer el analicis anterior se puede entender que no seria lo mas optimo para el calculo posiciones altas ya que seria mejor un manejo distribuido
    #para el calculo y con algun algoritmo mas pulido puesto que calculariamos varias veces las mismas posiciones con esta logica,
    #conveniendo guardar los valores previmente calculados.

    #COMO OBJETO DE EJEMPLIFICACION DE RECURCIVIDAD ES UTIL UNICAMENTE.

print(fibonacci(7))

