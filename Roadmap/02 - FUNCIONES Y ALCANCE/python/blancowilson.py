# Funciones practica semana 2 Blancowilson

## functions with two parameters and another function inside
def validate_has_letter(word, letter):
    #function into another function
    def addition(a,b):
        print("Message into the function inside another function")
        print(f"la suma de {a} + {b} =", end=" ")
        return a + b
    print(f"{addition(3,5)}")
    return letter in word   

#calling the function an print the retun result
print(validate_has_letter("palabra",'e'))
print("")
print("Test local and global variables")
# Testing the glbal an local variables
count_local = 0 # local variable
def increment_count():
    global count_local #concerting count to a global to use in the function
    count_local += 1

def another_increment_count():
    global count_local
    count_local += 1

increment_count()
another_increment_count()
print(count_local) # Output: 1


# Functions without parameters and return values
def normal_function():
    print("Hello, this is a function without parameters or return values")

normal_function()


# Functions with optional parameters and default values
def function_with_optional_parameters(name="Unknown", age=0):
    print(f"Hello, {name}. You are {age} years old.")

# Call the function to execute it
function_with_optional_parameters()

# Functions with arbitrary positional parameters using *args
def function_with_arbitrary_parameters(*args):
    print(f"You passed {len(args)} arguments to the function.")
    for arg in args:
        print(f"Argument: {arg}")

# Call the function to execute it
function_with_arbitrary_parameters("Mathematics", 1, 2)

# Functions with keyword arguments using **kwargs
def function_with_keyword_arguments(**kwargs):
    print(f"You passed {len(kwargs)} keyword arguments to the function.")
    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")

# Call the function to execute it
function_with_keyword_arguments(name="Wilson", age=40)

# Asynchronous functions using asyncio
import asyncio

async def function_async():
    print("This is an asynchronous function.")

# Call the function to execute it
asyncio.run(function_async())

# Functions with built-in functions
def function_with_built_in_functions():
    fruits = ["apple", "banana", "cherry"]
    print(f"Length of the list: {len(fruits)}")
    print(f"List: {list(fruits)}")

# Call the function to execute it
function_with_built_in_functions()

print("")
print ("Exercise Extra Print Word instead number")
print("")
def print_text(word1,word2):
    counter_both,counter_word1,counter_word2 =0,0,0     
    for i in range(1,101):
        if (i%5==0) & (i%3==0):
            print(f"{word1} {word2}")
            counter_both += 1
        elif (i%3==0):
            print(word1, end=",")
            counter_word1 += 1
        elif (i%5==0):
            print(word2,end=',')
            counter_word2 += 1
        else:
            print(i,end=',')
    print("")
    return (counter_word1,counter_word2,counter_both)


times = print_text('fizz', 'buzz')
print(f'Se imprimieron las palabras 1,2 y ambas {times} veces en vez de los numeros')