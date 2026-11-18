"""
Functions defined by the user
"""

# Simple

def greet():
    print("Hello Brais!")

greet()

# With return

def return_greet():
    return "Hello Brais!"

greet_message = return_greet()
print(greet_message)

# With an argument

def arg_greet(name):
    print(f"Hello {name}!")

arg_greet("Brais")

# With arguments

def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hi", "Brais")
args_greet(name="Brais", greet="Hello")

# With a default argument

def default_arg_greet(name="Python"):
    print(f"Hello {name}!")

default_arg_greet("Brais") 
default_arg_greet()  # Uses the default value

# With arguments and return

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

greet_message = return_args_greet("Hi", "Brais")
print(greet_message)

# With return of multiple values

def multiple_return_greet():
    return "Hello", "Brais"

greet_message, name = multiple_return_greet()
print(greet_message, name)

# With variable number of arguments

def variable_args_greet(*args):
    for name in args:
        print(f"Hello {name}!")

variable_args_greet("Brais", "Python", "Elhdrond", "Mouredev", "World")

# With variable number of keyword arguments

def variable_kwargs_greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

variable_kwargs_greet(
    language="Python",
    name="Sergio",
    alias="Elhdrond",
    age=35
)


"""
Functions inside functions
"""

def outer_function():
    def inner_function():
        print("Hello from the inner function!")      
    inner_function()

outer_function()

"""
Built-in functions
"""

print("My name is Elhdrond!")
print(len("My name is Elhdrond!"))
print(type("My name is Elhdrond!"))
print("My name is Elhdrond!".upper())
print("My name is Elhdrond!".lower())
print("My name is Elhdrond!".replace("Elhdrond", "Sergio"))

"""
Local and global scope
"""

global_variable = "I am a global variable"

def local_scope_function():
    local_variable = "I am a local variable"
    print(f"{local_variable} inside the function")
    print(f"{global_variable} inside the function")

local_scope_function()
print(f"{global_variable} outside the function")

# This will raise an error because local_variable is not defined outside the function
try:
    print(f"{local_variable} outside the function")  
except NameError as e:
    print(f"Error: {e}")


"""
Extra exercise
"""

def print_numbers(text_one, text_two) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{text_one}-{text_two}")
        elif number % 3 == 0:
            print(text_one)
        elif number % 5 == 0:
            print(text_two)
        else:
            print(number)
            count += 1
    return count

print(f"Count: {print_numbers("Fizz", "Buzz")}")