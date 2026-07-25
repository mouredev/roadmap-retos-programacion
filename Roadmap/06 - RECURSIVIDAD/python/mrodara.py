################ Recursividad ###################
'''
Decimos que una función es recursiva cuando dentro de la función se llama a si misma
Para hacer que sea recursiva debemos tener un caso base que hará finalizar el bucle de llamadas.
'''

def countdown(number: int = 100):
    if number == 0:
        print(0)
    else:
        print(number)
        countdown(number=number-1)
        
countdown(100)


#####################  EXTRA  ################################

#Calcular el factorial de un número
def factorial(number: int) -> int:
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number=number-1)

print(factorial(6))

# Calcular valor de un elemento según su posición en la sucesión de Fibonacci


def calcular_valor_fibonacci(position: int) -> int:    
    
    if position == 1:
        return 0
    elif position == 2:
        return 1
    else:        
        return calcular_valor_fibonacci(position=position-1) + calcular_valor_fibonacci(position=position-2) 

print(calcular_valor_fibonacci(7))
#####################  FIN EXTRA  ################################