# ejercicio de recursividad
print("\nCountdown: ")
def countdown(num: int):
    if num >= 0:
        print(num, end=" ")
        countdown(num - 1)
countdown(100)

# EXTRA
print("\nFactorial: ")
def factorial(num: int) -> int:
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))

print("Fibonacci: ")
def fibonacci(num: int) -> int:
    if num <= 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
print(fibonacci(10))