"""
Functions defined by user
"""

# Basic
def name():
    print("My names is Jesus!")

name()

# With return
def return_age():
    return "I am 27"

age =return_age()
print(age)

# With 1 parameter
def greet_one(name):
    print(f"Hola, {name}!")

greet_one("Jesus")

# With parameters
def greet_two(name, age):
    print(f"{name} and {age}")

greet_two("Jesus", "27")

# With a predetermined parameter
def default_greet(name="Python"):
    print(f"Hola, {name}")

default_greet()
default_greet("Pedro")

# With positional argument
def greet_three(name, age):
    print(f"{name} and {age}")

greet_three(name="Jesus", age="27")

# With parameters and return
def greet_four(name, age):
    return f"{name} and {age}"

print(greet_four("Pedro", 30))

# With several returns
def multiple_returns():
    return "Hi", "Python"

saludo, nombre = multiple_returns()
print(saludo)
print(nombre)

# With a variable number of parameters (Args)
def variable_arg_greet(*name):
    for i in name:
        print(f"Hola, {i}")

variable_arg_greet("Pedro", "Brais", "Jesus")

# With a variable number of parameters and keywords (Kwargs)
def variable_kwarg_greet(**name):
    for key, value in name.items():
        print(f"({key}) {value}")

variable_kwarg_greet(
    language="English", 
    name="Jesus", 
    age=27, 
    alias="JAdraz"
)

"""
Functions inside functions
"""

def outer_functions():
    def inner_function():
        print("Inner function: Hello, World!")
    inner_function()

outer_functions()

"""
Built-In Functions
"""

print("Hello, World")
print(len("Hello, World!"))
print(sorted("987654321"))
print("Jesus".upper())


"""
Local Scope
"""

def myfunc():
    x = 1500
    print(x)

myfunc()

def myfunc2():
    x = 2000
    def myfunc3():
        print(x)
    myfunc3()

myfunc2()

"""
Global Scope
"""

x = 3000

def my_glob_func():
    x = 4000
    print(x)

my_glob_func()
print(x)

def my_glob_func2():
    global x
    print(x)

my_glob_func2()
print(x)

"""
Exercise (Optional)
"""

def func(text1=str, text2=str)-> int:
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(text1 + text2)
        elif i % 5 == 0:
            print(text2)
        elif i % 3 == 0:
            print(text1)
        print(i)

func("Jesus", " Adraz")