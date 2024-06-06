def my_function():
  print('Hello from a function')

# call function
my_function()


# function with argument
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
def my_function(fname):
  print('Hi', fname)

my_function('Emil')
my_function('Linus')
my_function('Mark')

# function with two arguments
def my_function(fname, lname):
  print(fname + '' + lname)

my_function('Mark', 'Zuckerberg')

# arbitrary arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Mark", "Elon", "Torvals")

# Keyboards arguments
def my_function(programmer1, programmer2, programmer3):
  print('This is the first programmer:', programmer1, 'second programmer:', programmer2, 'third programmer:', programmer3)

my_function(programmer2 = "Zavitar", programmer1 = "Moure", programmer3 = "Midu")


# arbitrary keyboards arguments
def my_function(**person):
  print("His last name is " + person["lname"])

my_function(fname = "Linus", lname = "Torvals")

""" You use functions to give recursion to your program, some common functions in Python.
# print(): Used to display information in the console or another output device.
# input(): Allows the user to enter data from the keyboard.
# len(): Returns the length of an object, such as a string, list, tuple, etc.
# range(): Generates a sequence of numbers.
# open(): Used to open a file and perform read or write operations on it.
# str(), int(), float(): Used to convert between different data types.
"""

global_var = "I'm global variable"

def global_example():
    local_var = "I'm local variable"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

variable_global = 10

def funcion():
    globals() ['variable_global'] = 20

print(variable_global)  # Output: 10
funcion()
print(variable_global)  # Output: 20

def fizz_buzz(txt_1, txt_2):
   print('FIZZ BUZZ with STEROIDS')
   for numb in range(1, 101):
        if numb % 3 == 0 and numb % 5 == 0:
            print(txt_1 + ',' , txt_2)
        elif numb % 3 == 0:
           print(txt_1)
        elif numb % 5 == 0:
           print(txt_2)
        else:
           print(numb)

fizz_buzz('Hello', 'Python!')