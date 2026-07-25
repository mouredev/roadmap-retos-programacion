"""Exceptions"""

# TypeError

n1 = 10
n2 = "Pizza"
try:
	add_nums = n1 + n2 # We get a TypeError
except TypeError:
    print("Something Went Wrong") # Handling the exception
finally:
	print("The clause Finally always run")
    
# ValueError

my_str:str = "10"
print(type(my_str))
str_to_int = int(my_str)
print(f"{type(str_to_int)} : {str_to_int}")

my_str = "Duban"
try:
	str_to_int = int(my_str) # ValueError
except ValueError:
	print("Cannot cast literal str to int")
    
    
# ZeroDivisionError

try:
	div = 10/0
except ZeroDivisionError:
	print("Can not Div by Zero IDIOT!")
    

# IndexError

fruits = ["banana", "strawberry", "watermelon"]
try:
	print(fruits[3])
except IndexError:
	print("The first index is zero my bro, continue studying")
    
    
# Printting the error

fruits = ["banana", "strawberry", "watermelon"]
try:
	print(fruits[3])
except IndexError as e:
	print("The first index is zero my bro, continue studying")
	print(e)
    
 
""" Extra """

def add(n1, n2):
	return n1 + n2
    
def sub(n1, n2):
	return n1 - n2
    
def mul(n1, n2):
	return n1 * n2

def div(n1, n2):
	return n1 / n2
    

class MyException(Exception): # Inherit of superclass Exception
    pass

 
def calculator(func, n1: int, n2: int):
    if n2 == 0:
        raise ZeroDivisionError("The second number cannot be Zero")
    elif type(n2) == str:
        raise TypeError("The second number cannot be str")
    return func(n1, n2)
	
try:
    print(calculator(add, 10, 9))
except TypeError as error:
    print("Cannot do operations without int data type")
    print(f"Error: {type(error).__name__}") # Error: TypeError
except MyException as e:
    print(f"My exception has caught the error: {e}")
except Exception as e:
    print("Something was wrong")
    print(f"{type(e).__name__}: {e}")
else:
    print("Everithing went well")
finally:
    print("This clause always run")