########################################################################
## Recursividad del 100 al 0
########################################################################
def number_counter(max:int=100) ->int:
    if max == 0:
        return 0
    else:
        print(max)
        return number_counter(max - 1)

#resultado = number_counter()



########################################################################
## DIFICUTAD EXTRA
########################################################################

def factorial(n:int)->int:
    """
    Calcula el factorial de un numero
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

########################################################################

def fibonacci_sequence(pos1=0, pos2=1, numbers=[0,1], max=20):
    """
    Función recursiva para calcular el valor en la sucesión de Fibonacci
    """
    if len(numbers) >= max:
        print(numbers)
    else:
        suma = numbers[pos1] + numbers[pos2]
        numbers.append(suma)    
        return fibonacci_sequence(pos1+1, pos2+1)

fibonacci_sequence()
