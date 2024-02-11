#02 FUNCIONES Y ALCANCE

# Simple Python function 
def printLog():
    """Create a print. """ #Docstring
    return print("This is a console print")

printLog()

# Function with Parameters
def sumNumbers(number1: int, number2: int) -> int:
    """sum 2 numbers"""
    numberResult = number1 + number2  
    return print(f"The sum of {number1} and {number2} results {numberResult}.")

sumNumbers(5,12)

# Function Default Arguments
def func1(x, y=100):
    print("X = ", x)
    print("Y = ", y)

func1(50)
func1(50,20)
 
# Function Keyword arguments (The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.)
def student(firstname, lastname):
    print(firstname, lastname)

student(firstname='Saez', lastname='MD')
student(lastname='MD', firstname='Saez')


# Function Arbitrary Keyword Arguments [*args in Python (Non-Keyword Arguments)] & [**kwargs in Python (Keyword Arguments)]
# *args for variable number of arguments
def func2(*argv):
    for arg in argv:
        print(arg)
 
func2('Hello', 'Welcome', 'to', 'myPage') 

# *kwargs for variable number of keyword arguments
def func3(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
  
func3(first='Saez', mid='MD', last='Webpage', final='.com')

#Function within Functions
def funcOut():
    s = 'This is a combo functions'
    def funcIn():
        print(s)        
    funcIn()
 
funcOut()

#Anonymous Functions in Python (the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions)
cube_v2 = lambda x : x*x*x
print(cube_v2(7))

#Recursive Functions in Python
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
       
print(factorial(6))
      
      
#Built-in Functions:
def all(iterable):
    for element in iterable:
        if not element:
            print("False")
            return False
    print("True")
    return True
all([12,2,3,4,5,6,7])
all("home")
# all(0) ; FALSE

print(len("SaezMD"))
print(type(36))
print("SaezMD".upper())


# Variables Globales y locales
counter = 10

def restartCounter():
	global counter
	counter = 0


print(f'counter before is {counter}')
restartCounter()
print(f'counter after is {counter}')


value = 10

def func10():
	value = 20
	print(f'Inside value: {value}')

func10()
print(f'Outside value: {value}')

"""
DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""
def textFizzBuzz(text1: str, text2: str) -> int:
    """function to print all numbers from 1 to 100 (included). When number is divisible by 3/5 or both, there is a text. The return is the number of printed numbers."""
    numbersPrinted=0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("-> %s%s" % (text1, text2))
            continue
        if i % 3 == 0:
            print("-> %s" % (text1))
            continue
        if i % 5 == 0:
            print("-> %s" % (text2))
            continue
        else:
            print(i)
            numbersPrinted += 1
    return print(numbersPrinted)
textFizzBuzz("bat","woman")






