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


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

num = 5
print("The factorial of", num, "is", factorial(num))

print("The fibonacci number of position", num, "is", fibonacci(num))



