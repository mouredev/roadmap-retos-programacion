def print_numbers_back(number):
    if number == 0:
        return
    print(number)
    print_numbers_back(number - 1)

print_numbers_back(10)


test_number=10

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

print(factorial(test_number))

fibonacci_list:list=[]

def fibonacci(number):
    if number <= 0:
        return "El número debe ser mayor a 0"
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


if test_number > 0:
    print("Los primeros", test_number, "términos de la serie de Fibonacci son:")
    for i in range(1, test_number + 1):
        print(fibonacci(i), end=" ")
else:
    print("El número ingresado no es válido")