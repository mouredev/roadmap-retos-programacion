#Recursividad
def countdown (number : int):
    if number >= 0:
        print(number)
        countdown(number - 1)
countdown(100)

"""
Extra
"""
#Facorial
def factorial (number:int):
    if number ==1 or number == 0:
        return 1
    else:
        return number * factorial(number-1)

    
print(factorial(5))

def funibucci(position:int):
    if position <= 0:
        print("numero negativo")
        return 0
    elif position ==1:
        return 0
    elif position == 2:
        return 1
    else:
        return funibucci(position-1) + funibucci(position - 2)
print(funibucci(50))

