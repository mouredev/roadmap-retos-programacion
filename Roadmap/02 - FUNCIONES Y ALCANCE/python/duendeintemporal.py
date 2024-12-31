# { ROADMAP PARA PROGRAMADORES }  #2 FUNCIONES Y ALCANCE
# BIBLIOGRAFY REFERENCE: Python, Java, SQL JavaScript The Ultimate Crash Course for Beginners to Master the 4 Most In-Demand Programming Languages,... (Philip Robbins) (Z-Library).pdf
# Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

""" Python supports a variety of programming paradigms. The functional
programming paradigm is the most widely used programming paradigm for
developers to write code in. """ 

""" Types of Functions
System functions and user-defined functions are the two main types of
functions.
The core Python library provides system functions, which are frequently
used by developers to perform common tasks. 'print,' for example, is a
system function that displays a literal string literal on the screen.
Developers, on the other hand, create user-defined functions specifically for
their software. Users can also integrate third-party libraries' user-defined
functions into their code.
Regardless of the type of code you use, keep in mind that the primary goal
of using functions as a programmer is to solve problems with less reusable
code. """

""" How do they Work?
The philosophy behind the use of functions in programming is similar to
that of mathematical functions. The developer will first define a function
with complex code logic and a name that can be called from anywhere in
the program using unique programming components known as parameters.
The developers then explicitly define what type of parameters the user can
provide for fewer crashes.
If the function is not called, users will be unable to use the code logic that
the developer created. Function calling is frequently displayed in the front
end via buttons, tabs, and other graphical user interfaces. While it may be as
simple as a tap for the end user, a function will be called programmatically
for a software component to function properly. """

def add_pad(number, width, pad='0'):
    result = str(number)
    while len(result) < width:
        result = f"{pad}{result}"
    return result

print(add_pad(4, 3, '#'))  # ##4
print(add_pad(56, 3, '$'))  # $56
print(add_pad(7, 3))        # 007

def square(n):
    return n * n

func_array = []
func_array.append(square(8))  # Adds a new function to a list
print(func_array)  # [64]

data = {'book_name': 'Hackbook'}
data['some_method'] = lambda: print(f"{data['book_name']} is now available in z-lib.org, so hack the world.")  # Assigns a new function as a property of another object
data['some_method']()  # Hackbook is now available in z-lib.org, so hack the world.

def call(do_something):
    do_something()

call(lambda: print('Hi roadmap coders!'))  # Hi roadmap coders!

# Returned as values from functions
def return_func():
    return lambda str: print(str)

greeting = return_func()
greeting('Hi there!')  # Hi there!

# Short for print
log = print

# Functions in Python can possess properties that can be dynamically created and assigned like objects.

def call_mom():
    log('Mommmmm!')

call_mom()  # Output: Mommmmm!
call_mom.name = "Momm"  # Assigning a name property
log(call_mom.name)  # Output: Momm

call_mom.something = 'something'  # Assigning a custom property
log(call_mom.something)  # Output: something

log(call_mom)  # <function call_mom at 0x00000215FAA0ACA0>

# Functions in Python are first-class objects, meaning they can be treated like any other object.

# Class definition for Cat, which serves as a constructor for creating Cat objects.
class Cat:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

# Creating an instance of Cat
psico_cat = Cat("Psicotrogato", "Black & White", "Meaw")
log(psico_cat.color)  # Output: Black & White
psico_cat.sound = "Hey girl what's your name, what's your name?... I forgot"

# Adding a method to the Cat class
def speak(self):
    log(self.sound)

Cat.speak = speak  # Adding the speak method to the Cat class

psico_cat.speak()  # Output: "Hey girl what's your name, what's your name?.. I forgot"

# Closure example: A function that maintains state across calls.
def incrementer(n):
    local = [n]  # Use a list to hold the mutable state
    def inner():
        local[0] += 1
        return local[0] - 1
    return inner

increment = incrementer(0)  # Immediately invoked with an initial value of 0

log('incrementer value is:', increment())  # Output: incrementer value is: 0
log('incrementer value is:', increment())  # Output: incrementer value is: 1
log('incrementer value is:', increment())  # Output: incrementer value is: 2

# Function that returns another function (closure)
def square_v2(n):
    return lambda: n * n

pow64 = square_v2(64)
pow78 = square_v2(78)

log(pow64())  # Output: 4096
log(pow78())  # Output: 6084

# Recursive function example
def factor(n):
    if n == 1:
        return 1
    return n * factor(n - 1)

log(factor(8))  # Output: 40320

# Function to calculate square using a lambda expression
square_v3 = lambda n: n * n
log(square_v3(4))  # Output: 16

# Class to demonstrate method context with 'self'
class Obj:
    def __init__(self):
        self.value = 'Rutadeprogramacion Exercice #2.'

    def advertisement(self):
        log(self.value)  # Output: Rutadeprogramacion Exercice #2
        # Using a lambda function to maintain context
        import threading
        threading.Timer(1, lambda: log(f"{self.value}")).start()

obj = Obj()
obj.advertisement()  # Alerts the message after 1 second

# Function declaration example
def subtract(n, m):
    return n - m

log(subtract(8, 4))  # Output: 4

# Function expression using a lambda
multiply = lambda n, m: n * m
log(multiply(8, 9))  # Output: 72

# Named function using a lambda expression
add = lambda a, b: a + b
log(add(3, 3))  # Output: 6

# Lambda function for division
divide = lambda n, m: n / m
log(divide(543, 56))  # Output: 9.696428571428571

# Anonymous Functions: These are functions that do not have a name. They are often used in callbacks or as arguments to other functions.

# In Python, we can use lambda functions as anonymous functions.
import threading

def on_load():
    body_style = {
        'background': '#000',
        'text-align': 'center'
    }
    
    title = 'Retosparaprogramadores #2.'
    title_style = {
        'font-size': '3.5vmax',
        'color': '#fff',
        'line-height': '100vh'
    }
    
    # Simulating setting styles and appending to body
    log(f"Body style: {body_style}") # Body style: {'background': '#000', 'text-align': 'center'}
    log(f"Title: {title} with style: {title_style}") # Title: Retosparaprogramadores #2. with style: {'font-size': '3.5vmax', 'color': '#fff', 'line-height': '100vh'}
    
    log('This is an anonymous function')  # This will be logged at the end

on_load()  # Simulating the load event

def say_hi():
    log('Hi')

say_hi()  # Output: Hi

# Named functions differ from anonymous functions in multiple scenarios:
# - When debugging, the name of the function will appear in the error/stack trace.
# - Named functions are hoisted while anonymous functions are not.
# - Named functions and anonymous functions behave differently when handling recursion.

# Immediately Invoked Function Expressions (IIFE): 
# An IIFE is a function that is executed immediately after it is defined.
# In Python, we can achieve similar behavior using a function call.

def iife():
    log("This is another example of IIFE functions")  # This will be logged

iife()  # Immediately invoked

# Higher-Order Functions: These are functions that take other functions as arguments or return functions as their result.
def sum_numbers(numbers):
    total = sum(numbers)  # Using built-in sum function
    return total

def range_numbers(n, m):
    return list(range(n, m + 1))  # Creating a range of numbers

# Using the higher-order functions
log(sum_numbers(range_numbers(1, 100)))  # Output: 5050

# Generator Functions: Generator functions can pause and resume execution.
def id_generator():
    id = 0
    while True:
        id += 1
        yield f"{id:05}"  # Formatting the ID with leading zeros

id_iterator = id_generator()

log(next(id_iterator))  # Output: 00001
log(next(id_iterator))  # Output: 00002

# Async Functions: Async functions are a way to work with asynchronous code.
import asyncio
import aiohttp

async def get_lorem_ipsum(number_of_paragraphs):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://baconipsum.com/api/?type=meat-and-filler&paras={number_of_paragraphs}') as response:
            return await response.json()

async def log_paragraphs():
    try:
        result = await get_lorem_ipsum(2)
        log(result)  # Logs the result: some lorem Ipsum paragraphs
    except Exception as error:
        log(f"Error: {error}")

# Running the async function
asyncio.run(log_paragraphs())

# Functions that take multiple arguments / the Rest parameter
# In Python, we can use *args to accept a variable number of arguments.

def total(*numbers):
    return sum(numbers)  # Using built-in sum function

log('Total:', total(10, 256, 345, 465, 87, 432))  # Output: Total: 1595

# CLOSURES AND SCOPES

# Scope: A scope refers to the visibility of identifiers in certain parts of a program.
# Closure: A closure allows a function to access and manipulate variables that are external to that function.

# Hoisting is not a concept in Python like it is in JavaScript, but we can define functions before or after they are called.

# Named functions can be called before their declaration due to Python's function definition behavior.
def do_something():
    log("I'm here coding, and I'm amazed at all we can learn by following this roadmap.")

log(do_something())  # This will work

# Anonymous functions (lambdas) cannot be called before their declaration.
# Uncommenting the following line will throw an error.
# log(do_another_thing())

do_another_thing = lambda: log('never log this...') # None

friend = 'Asterix'

def show_closure():
    log(friend)  # Output: Asterix in scope
    another_friend = 'Obelix'
    
    def inner_closure():
        another_one = 'Idefix'
        log(another_friend)  # Output: Obelix in scope
        log(friend)  # Output: Asterix in scope
        log(another_one)  # Output: Idefix in scope
    
    inner_closure()
    # Uncommenting the following line will throw an error.
    # log(another_friend)  # Throws an Error: another_friend is not defined

show_closure()

# Closures allow us to define "private" variables that are visible only to a specific function or set of functions.
def make_counter():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    def reset_counter():
        nonlocal counter
        counter = 0

    return {
        'value': lambda: counter,
        'increment': increment_counter,
        'restart': reset_counter
    }

# Testing the make_counter function
counter1 = make_counter()
counter2 = make_counter()

counter2['increment']()  # Increment counter2
counter2['increment']()  # Increment counter2
log(counter1['value']())  # Output: 0
log(counter2['value']())  # Output: 2
counter2['restart']()  # Restart counter2
log(counter2['value']())  # Output: 0


# The context of the function is saved when make_counter() is called.

# Apply and Call
def speak(*sentences):
    tell = ' '.join(sentences)
    log(f"{person['name']}: {tell}")

person = {'name': "Niko"}
speak("I", "will", "go", "through", "this", "roadmap", "until", "the", "end")  # Output: I will go through this roadmap until the end
speak("But", "first", "I", "need", "some", "exercise")  # Output: But first I need some exercise

# In Python, we can use the 'self' parameter in methods to refer to the instance of the class.

# The bind method in Python can be simulated using a method within a class.
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        log(f"Hi {self.name}")

person2 = Person('Anna')
person2.say_hi()  # Output: Hi Anna

