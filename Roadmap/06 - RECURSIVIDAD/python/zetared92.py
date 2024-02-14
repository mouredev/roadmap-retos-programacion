# RECURSIVIDAD

def countdown(num: int):
    if num >= 0:
        print(num)
        countdown(num - 1)

countdown(100)



# Extra

print("🧩 DIFICULTAD EXTRA 🧩")

def factorial(num: int) -> int:
    if num < 0:
        print("Input a positive integer")
        return 0
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(4))

def fibonacci(num: int) -> int:
    if num <= 0:
        print("The position must be greater than zero")
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num -1) + fibonacci(num - 2)
    
print(fibonacci(4))
