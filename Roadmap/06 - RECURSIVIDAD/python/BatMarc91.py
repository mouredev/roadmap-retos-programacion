def countdown(numero: int):
    if numero >= 0:
        print(numero)
        countdown(numero - 1)

countdown(5)

# Extra #

# Sin recursividad 
def factorial(number: int) -> int: # Li dic que m'ha de retorna un enter
    calculo = 1
    for i in range(1,number + 1):
        calculo = i * calculo
    print(f"Este és el primer factorial {calculo}")

factorial(5)

# Con recursividad
def factorial_2(number: int) -> int: # Li dic que m'ha de retornar un enter
    if number < 0:
        print("Els números negatius")
        return 0
    elif number == 0:
        return 1
    
    return number * factorial_2(number - 1)

      
# print(factorial_2(5))

numeros = [0,1]

def fibonnacci(posicio: int)-> int:
    num1 = numeros[(len(numeros)-1)]
    num2 = numeros[(len(numeros)-2)]
    sum_fibo = num1 + num2
    numeros.append(sum_fibo)
    if (len(numeros) <= posicio):
        fibonnacci(posicio)
    else:
        return print(numeros[posicio])
fibonnacci(13)
