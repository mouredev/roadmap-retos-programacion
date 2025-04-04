""" #06 RECURSIVIDAD """


def showNumbers(number):
    if number == 0:
        print(number)
        return number
    print(number, end=" > ")
    showNumbers(number-1)


# number = int(input("Ingresa un valor: "))
showNumbers(10)


def factorial(number):
    if number == 1 or number == 0:
        return 1
    return number * factorial(number-1)


print(f"Factorial: {factorial(5)}")


def fibonacci(position):
    if position == 0 or position == 1:
        return position
    return fibonacci(position - 1) + fibonacci(position - 2)


print(f"Fibonacci: {fibonacci(10)}")
