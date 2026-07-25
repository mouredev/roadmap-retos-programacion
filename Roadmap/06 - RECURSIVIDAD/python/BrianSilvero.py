"""
Ejercicios
"""
# def countdow(num:int):
#     if num >= 0: 
#         print(num)
#         countdow(num-1)

# countdow(100)

"""
Extra
"""

# Factorial
def factorial(number:int):
    if number < 0:
        print("No se admiten numero negativos")
        return 0
    elif number == 0:
        return 1 
    else:
        return number * (factorial(number - 1))
print(factorial(3))

# Fibonnacci 
def fibonnacci(number:int):
    if number <= 0:
        print("Tienen que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 2
    else:
        return 

print(fibonnacci(5))