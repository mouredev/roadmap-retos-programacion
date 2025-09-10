"""
Recursividad
"""

def tri_recursion(x):
  print(x)
  if(x==0):
    return
  else:
    tri_recursion(x-1)

print("\n\nRecursion Example Results")
tri_recursion(100)


"""
Extra
"""


def factorial(x: int) -> int:
    """This is a recursive function
    to find the factorial of an integer"""
    if x <= 0:
       print("Number must be positive")
       return 0
    elif x == 1:
        return 1
    else:
        return (x * factorial(x-1))

def fibonacci(x : int) -> int:
    if x <= 0:
        print ("Number must be positive")
        return 0
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

print(factorial(5))

print(fibonacci(5))



