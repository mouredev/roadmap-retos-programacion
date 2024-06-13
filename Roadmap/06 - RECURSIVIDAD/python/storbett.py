# ejericio


# def contador(number: int):
    
#     if number >= 0:
#         print (number)
#         contador(number - 1)

# contador(100)


"""
extra 
"""

def factorial (number: int) -> int:
    if number < 0:
        print("los numero negativos no son validos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial (number -1 )

print (factorial (5))


def fibonacci( number: int ) -> int:
    if number <= 0:
        print("la psicion tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci (number - 1) + fibonacci (number - 2)

print (fibonacci (7))