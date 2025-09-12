def count_back(counter):
    
    print(counter, end = ", ")
    counter -= 1

    if counter > 0:
        count_back(counter)
    
    elif counter == 0:
        print(counter)

number = 100
count_back(number)


print('\n', '~'*7, "EJERCICIO EXTRA", '~'*7)
print("--> EJERCICIO 1: FACTORIAL")

#multiplicación de todos los números menores que él hasta 0
def factorial(num: int) -> int:
    if num > 0:
        res = num * factorial(num-1)
        return res
    else:
        return 1

print(factorial(5))


print("--> EJERCICIO 2: FIBONACCI")
#sucesión de números que cada número es la suma de los 2 anteriores

def fibonacci(num):

    if num-1 < 2:
        return 1
    
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)

print(fibonacci(9))
